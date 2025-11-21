#!/usr/bin/env bash

# Run marker_single only on PDFs in a directory, skipping dotfiles and caches.
# Usage: ./marker_pdf_only.sh <input_dir> [output_dir]

set -euo pipefail

print_usage() {
  cat <<'EOF'
Usage: ./marker_pdf_only.sh <input_dir> [output_dir]
 - input_dir: directory to scan for PDFs (non-PDFs are ignored)
 - output_dir: optional directory for marker outputs (defaults to marker default)
EOF
}

INPUT_DIR="${1:-}"
OUTPUT_DIR="${2:-}"

if [[ -z "${INPUT_DIR}" ]]; then
  print_usage
  exit 1
fi

if [[ ! -d "${INPUT_DIR}" ]]; then
  echo "Input directory not found: ${INPUT_DIR}" >&2
  exit 1
fi

found_any=0
while IFS= read -r -d '' pdf; do
  found_any=1
  if [[ -n "${OUTPUT_DIR}" ]]; then
    marker_single "${pdf}" --output_dir "${OUTPUT_DIR}"
  else
    marker_single "${pdf}"
  fi
done < <(find "${INPUT_DIR}" -type f -iname '*.pdf' ! -name '.*' -print0)

if [[ "${found_any}" -eq 0 ]]; then
  echo "No PDFs found under ${INPUT_DIR}" >&2
  exit 1
fi
