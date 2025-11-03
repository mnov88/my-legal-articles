#!/usr/bin/env python3
"""
Topic mapping tool

Scans `draft.md` for subchapter headings and searches other Markdown files for
related sections. Produces per-topic mapping docs with a table capturing:
- Source file
- Section
- Relevant arguments (snippet)
- External refs (URLs detected)

Usage:
  python3 tools/map_topics.py \
    --draft-file draft.md \
    --out-dir "Topic maps" \
    --include Materials Drafts Outlines "Research reports"

Notes:
- Matching is token-overlap based on heading keywords (simple heuristic).
- Edit `MIN_TOKEN_MATCH` or stopwords to tune recall/precision.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


STOPWORDS = {
    # basic stopwords and markdown tokens
    "the", "a", "an", "of", "in", "to", "for", "and", "or", "on", "with",
    "by", "as", "at", "from", "into", "about", "how", "why", "what", "when",
    "is", "are", "be", "this", "that", "these", "those", "use", "uses",
    "chapter", "section", "part", "ii", "iii", "iv", "v", "i"
}

MIN_TOKEN_MATCH = 1  # minimum overlapping tokens between draft heading and candidate section


@dataclass
class Section:
    file: Path
    heading: str
    level: int
    content: str  # text until the next heading


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return path.read_text(errors="ignore")


HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.+?)\s*$")


def parse_sections(md: str, file: Path) -> List[Section]:
    lines = md.splitlines()
    sections: List[Section] = []
    current: Section | None = None
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            # close previous section
            if current is not None:
                sections.append(current)
            level = len(m.group("hashes"))
            title = m.group("title").strip()
            current = Section(file=file, heading=title, level=level, content="")
        else:
            if current is not None:
                current.content += ("\n" if current.content else "") + line
    if current is not None:
        sections.append(current)
    return sections


TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z\-']+")


def keywords(text: str) -> List[str]:
    toks = [t.lower() for t in TOKEN_RE.findall(text)]
    return [t for t in toks if t not in STOPWORDS and len(t) > 2]


def url_refs(text: str) -> List[str]:
    # Capture explicit links and bare URLs
    urls = set()
    for m in re.finditer(r"\[[^\]]*\]\((https?://[^)\s]+)\)", text):
        urls.add(m.group(1))
    for m in re.finditer(r"(?<!\()\bhttps?://[^\s)]+", text):
        urls.add(m.group(0))
    return sorted(urls)


def first_sentences(text: str, max_chars: int = 400) -> str:
    # Simplistic sentence split; good enough for snippets
    cleaned = re.sub(r"\s+", " ", text).strip()
    if len(cleaned) <= max_chars:
        return cleaned
    # try to cut at sentence boundary
    cut = cleaned[:max_chars]
    last_dot = max(cut.rfind("."), cut.rfind(";"))
    if last_dot > 100:  # avoid overly short
        return cut[: last_dot + 1].strip()
    return cut.strip() + " …"


def sanitize_filename(name: str) -> str:
    # Keep letters, numbers, space, dash, underscore; replace others with dash
    safe = re.sub(r"[^A-Za-z0-9 _\-]", "-", name)
    safe = re.sub(r"\s+", " ", safe).strip()
    return safe


def discover_markdown_files(root: Path, include_dirs: List[str]) -> List[Path]:
    results: List[Path] = []
    for p in root.glob("*.md"):
        results.append(p)
    for d in include_dirs:
        dd = root / d
        if dd.exists():
            results.extend(dd.rglob("*.md"))
    return results


def main(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(description="Generate topic mapping docs from draft headings.")
    ap.add_argument("--draft-file", default="draft.md", help="Path to main draft file")
    ap.add_argument("--out-dir", default="Topic maps", help="Output directory for mapping docs")
    ap.add_argument("--include", nargs="*", default=["Materials", "Drafts", "Outlines", "Research reports"], help="Dirs to scan for sources")
    ap.add_argument("--min-match", type=int, default=MIN_TOKEN_MATCH, help="Minimum token overlap to match")
    args = ap.parse_args(argv)

    root = Path.cwd()
    draft_path = root / args.draft_file
    if not draft_path.exists():
        print(f"draft file not found: {draft_path}", file=sys.stderr)
        return 2

    out_dir = root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    exclude_basenames = {draft_path.name, "AGENTS.md", "CHANGELOG.md", "README.md", "style.md"}

    # Parse draft headings
    draft_sections = [s for s in parse_sections(read_text(draft_path), draft_path) if s.level in (1, 2, 3)]
    draft_topics = [(s.heading, set(keywords(s.heading))) for s in draft_sections]

    # Gather candidate sections from other files
    files = [p for p in discover_markdown_files(root, args.include) if p.name not in exclude_basenames]
    candidates: List[Section] = []
    for fp in files:
        try:
            text = read_text(fp)
        except Exception:
            continue
        sections = parse_sections(text, fp)
        # include whole-file section if no headings
        if not sections:
            sections = [Section(file=fp, heading="(full file)", level=1, content=text)]
        candidates.extend(sections)

    # Index by topic
    mappings: Dict[str, List[Tuple[Section, int]]] = defaultdict(list)
    for topic, tks in draft_topics:
        if not tks:
            continue
        for sec in candidates:
            sec_tokens = set(keywords(sec.heading)) | set(keywords(sec.content[:500]))
            overlap = len(tks & sec_tokens)
            if overlap >= args.min_match:
                mappings[topic].append((sec, overlap))

    # Write per-topic files
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    index_lines = ["# Topic Maps Index", "", f"Generated: {now}", ""]

    for topic, matches in mappings.items():
        safe = sanitize_filename(topic)
        out_path = out_dir / f"Resources — {safe}.md"
        matches.sort(key=lambda x: (-x[1], x[0].file.name.lower()))
        rows: List[str] = []
        for sec, score in matches:
            snippet = first_sentences(sec.content)
            urls = ", ".join(url_refs(sec.content))
            rel = os.path.relpath(sec.file, root)
            sec_title = sec.heading.replace("|", "/")
            rows.append(f"| `{rel}` | {sec_title} | {snippet} | {urls} |")

        header = [
            f"# Resources — {topic}",
            "",
            f"Generated: {now}",
            "",
            "| Source file | Section | Relevant arguments (snippet) | Novel/Important to include | External refs |",
            "|---|---|---|---|---|",
        ]
        # Insert a blank column for Novel/Important to include before external refs
        rows_with_blank = []
        for r in rows:
            # r is: | file | section | snippet | urls |
            parts = r.strip().split("|")
            # ['', ' file ', ' section ', ' snippet ', ' urls ', ''] typically
            if len(parts) >= 5:
                parts.insert(-2, " Novel: — ")
                r = "|".join(parts)
            rows_with_blank.append(r)
        content = "\n".join(header + rows_with_blank) + "\n"
        out_path.write_text(content, encoding="utf-8")
        index_lines.append(f"- [{topic}]({out_path.name}) — {len(matches)} matches")

    # Write index
    (out_dir / "INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    print(f"Wrote {len(mappings)} topic files to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
