# Obsidian Footnote Converter Plugin

Convert HTML/marker-style footnotes to Obsidian's native footnote format with a single command!

## Features

- **Convert Current Note**: Instantly convert all footnotes in your active note
- **Conversion Modal**: Paste and convert text before adding it to your vault
- **Smart Conversion**:
  - **Marker-style** inline references: `[1](#page-3-2)` or `[10\)](#page-2-1)` → `[^1]`, `[^10]`
  - **Word-style** inline references: `[[10]](#_ftn10)` → `[^10]`
  - **Marker-style** definitions: `<sup>1</sup> Content` → `[^1]: Content`
  - **Word-style** definitions: `[[1]](#_ftnref1) Content` → `[^1]: Content`
  - Handles escaped parentheses and complex HTML structures
- **Optional EOF Placement**: Move all footnotes to the end of your document in a "Footnotes" section
- **Clean Output**: Automatically removes HTML spans, anchors, and cleans up formatting

## Use Cases

Perfect for converting documents exported from:
- PDFs converted with marker library
- Microsoft Word documents (HTML export)
- Academic papers with HTML footnotes
- Web articles with reference links
- Any document using HTML-style footnotes

## Installation

### From GitHub (Manual)

1. Download the latest release from the [releases page](https://github.com/yourusername/obsidian-footnote-converter/releases)
2. Extract the files into your vault's `.obsidian/plugins/footnote-converter/` folder
3. Reload Obsidian
4. Enable "Footnote Converter" in Settings → Community Plugins

### From Obsidian Community Plugins (Coming Soon)

Once published to the community plugins directory:
1. Open Settings → Community Plugins
2. Search for "Footnote Converter"
3. Click Install, then Enable

## Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/obsidian-footnote-converter.git

# Navigate to the plugin directory
cd obsidian-footnote-converter

# Install dependencies
npm install

# Build the plugin
npm run build

# For development with auto-rebuild
npm run dev
```

### Testing in Obsidian

1. Copy the built files to your vault:
   ```bash
   cp main.js manifest.json styles.css /path/to/your/vault/.obsidian/plugins/footnote-converter/
   ```
2. Reload Obsidian (Ctrl/Cmd + R)
3. Enable the plugin in Settings

## Usage

### Command: Convert Footnotes in Current Note

1. Open a note with HTML-style footnotes
2. Open the command palette (Ctrl/Cmd + P)
3. Search for "Convert footnotes in current note"
4. Press Enter

Your footnotes will be instantly converted!

### Command: Open Footnote Converter Modal

1. Open the command palette (Ctrl/Cmd + P)
2. Search for "Open footnote converter modal"
3. Paste your text with HTML footnotes
4. Click "Convert"
5. Copy the result or insert it directly into your current note

### Settings

**Move footnotes to end of file** (Default: On)
- When enabled, all footnote definitions are moved to a "Footnotes" section at the end
- When disabled, footnotes remain in their original positions

## Examples

### Example 1: Marker-style (PDF conversions)

**Input:**
```markdown
In its Communication on implementation and simplification ("A simpler and faster Europe"[1](#page-3-2) ), the Commission presented its approach.

<span id="page-3-2"></span><sup>1</sup> Communication from the Commission, COM(2025)47 final, 11 February 2025
```

**Output (with EOF enabled):**
```markdown
In its Communication on implementation and simplification ("A simpler and faster Europe"[^1] ), the Commission presented its approach.

## Footnotes

[^1]: Communication from the Commission, COM(2025)47 final, 11 February 2025
```

### Example 2: Word-style (Microsoft Word exports)

**Input:**
```markdown
The GDPR governs whether and under what conditions profiling may lawfully occur.[[10]](#_ftn10)

---

[[10]](#_ftnref10) DSA (n 1) recital 68.
[[11]](#_ftnref11) ibid recital 69.
```

**Output (with EOF enabled):**
```markdown
The GDPR governs whether and under what conditions profiling may lawfully occur.[^10]

## Footnotes

[^10]: DSA (n 1) recital 68.
[^11]: ibid recital 69.
```

## Reliability

✅ **Very High** for both marker library and Microsoft Word HTML exports
✅ Handles inline references with various formats
✅ Converts both marker and Word-style footnote definitions
✅ Cleans up HTML spans and anchors
✅ Works with multi-line content

⚠️ **May need review** if:
- Footnotes have complex nested HTML
- Source format varies significantly from common exports

💡 **Tip**: Use the included test files (TEST_MARKER_FORMAT.md and TEST_WORD_FORMAT.md) to verify the plugin works with your document format

## Testing

The plugin includes two test files to help you verify it works correctly:

- **TEST_MARKER_FORMAT.md** - Test with marker library PDF conversions
- **TEST_WORD_FORMAT.md** - Test with Microsoft Word HTML exports

Simply paste the sample text into Obsidian and run the converter to see the results.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - See LICENSE file for details

## Support

If you find this plugin helpful, consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs via GitHub Issues
- 💡 Suggesting features
- 📝 Contributing improvements

## Changelog

### 1.0.0 (Initial Release)
- Convert HTML-style footnotes to Obsidian format
- Support for inline references and definitions
- Optional EOF placement
- Conversion modal
- Settings panel

## Credits

Inspired by the need to convert academic papers and documents exported via the marker library to Obsidian-friendly format.
