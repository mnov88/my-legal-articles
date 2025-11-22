# Repository Guidelines

## Project Structure & Module Organization
- Folder for legal research papers
- One research project = one subfolder
- PhD-level academic publications for top EU law journals
- Root working draft: `root/subfolder/draft.md` (always the latest).
- Prior drafts: `root/subfolder/Drafts/` (use “draft N - short description.md”).
- Sources and notes: `root/subfolder/Materials/`.
- Outlines: `root/subfolder/Outlines/`.
- External analyses: `root/subfolder/Research reports/`.
- Resource maps: `root/subfolder/Mappings/` (per‑chapter tables consolidating sources + refs).
- Style rules: `style.md` (mandatory). General context: `README.md`.

Workflow: On a major edit, copy the current `draft.md` to `Drafts/` with the next number, then continue in `draft.md`. Record each major change in `CHANGELOG.md` (newest entry on top). For literature synthesis, maintain per‑chapter maps in `Mappings/`.

## Build, Preview, and Lint
- No build step required; files are Markdown.
- Optional lint: `markdownlint "**/*.md"` (or `npx markdownlint-cli2 "**/*.md"`).
- Optional link check: `markdown-link-check draft.md`.

## Writing Style & Naming
- Writing must follow `style.md` (OSCOLA footnotes, sentence case headings, no lists in draft prose, strong signposting).
- File names: `Drafts/` → `draft <number> - <short-description>.md`. Use spaces or hyphens consistently; keep lowercase descriptions.
- Keep paragraphs 150–300 words as per `style.md` and end major sections with crystallizing conclusions.

## Testing / Review Checklist
- Conform to all sections in `style.md` (structure, citations, banned language).
- Verify forward/backward references and that section endings draw explicit conclusions.
- Run optional Markdown lint/link checks; fix headings, links, and trailing whitespace.
- Ensure OSCOLA footnote numbering is sequential after edits.

## Commits & Pull Requests
- Commit messages: imperative mood, scoped prefix.
  - Examples: `draft: advance main argument`, `materials: add lit review notes`, `style: refine citation rules`.
- PRs must include:
  - Summary of changes and rationale.
  - Affected files (e.g., `draft.md`, `Drafts/draft 9 - framing.md`).
  - Any open questions for review (substance, structure, sources).

## Agent‑Specific Notes
- Agents must strictly apply `style.md` when generating or editing prose.
- Do not introduce bullet lists in drafts; enumerate within prose.
- When creating new versions, write to `Drafts/` and preserve `draft.md` as the working tip.
