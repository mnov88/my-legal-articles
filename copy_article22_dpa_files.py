#!/usr/bin/env python3
"""Copy machine-translated DPA files linked to GDPR Article 22 into the project."""

from pathlib import Path
import shutil
import pandas as pd


CSV_PATH = Path(
    "/Users/milos/Downloads/eurlextract/fast_scrape/authorities_summary_enriched.csv"
)
DEST_DIR = Path(
    "/Users/milos/Desktop/Conformity/Conformity/Automated decisions/DPAs"
)


def article_22_filter(value: str) -> bool:
    """Return True if the comma-separated gdpr_articles entry includes 22."""
    if not isinstance(value, str):
        value = "" if pd.isna(value) else str(value)
    try:
        return any(int(part.strip()) == 22 for part in str(value).split(","))
    except ValueError:
        return False


def main() -> None:
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(CSV_PATH, usecols=["gdpr_articles", "source_path"])
    subset = df[df["gdpr_articles"].apply(article_22_filter)]

    copied, missing = [], []
    for raw_src in subset["source_path"]:
        src_path = Path(str(raw_src))
        if not src_path.exists():
            missing.append(src_path)
            continue

        dest_path = DEST_DIR / src_path.name
        shutil.copy2(src_path, dest_path)
        copied.append(dest_path)

    print(f"Copied {len(copied)} files to {DEST_DIR}")
    if copied:
        for path in copied:
            print(f"  - {path}")
    if missing:
        print("Missing sources:")
        for path in missing:
            print(f"  - {path}")


if __name__ == "__main__":
    main()
