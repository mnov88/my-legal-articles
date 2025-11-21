# Marker quick usage

- **Install** (already done): `pipx install marker-pdf --python /opt/homebrew/bin/python3.12` then `pipx inject marker-pdf psutil`
- **Check** which binary: `which marker` (currently `/opt/homebrew/bin/marker`)
- **Single file**: `marker_single /path/to/file.pdf --output_dir ~/marker-out`
- **Folder, PDFs only**: `./marker_pdf_only.sh /path/to/dir ~/marker-out`
- **Workers**: keep `--workers 1` on Mac to save memory.
- **Notes**: hidden/non-PDF files trigger PDFium errors; MPS table model always falls back to CPU on Apple Silicon. Use a clean directory or the helper script to avoid noisy errors.


# Marker quick usage

 
 marker_single /path/to/file.pdf --output_dir ~/marker-out`
 
 ./marker_pdf_only.sh '/Users/milos/Desktop/Conformity/Conformity/Individual decisions' ~/marker-out
 