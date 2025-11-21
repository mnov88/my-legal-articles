# Test Document with Word-Style Footnotes

This is a test document you can use to verify the plugin works with Microsoft Word HTML exports.

## Sample Text with Footnotes

The DSA prohibition, rather clearly, does not displace the GDPR.[[10]](#_ftn10) Recital 68 emphasizes that the transparency requirements in Article 26(1) and (2) are "without prejudice" to the GDPR.[[11]](#_ftn11) Put differently, the GDPR governs whether and under what conditions profiling using special categories of personal data may lawfully occur; the DSA adds a display-layer constraint.[[12]](#_ftn12)

The EDPB has embraced this interpretation. In its draft Guidelines on the interplay between the DSA and the GDPR, the EDPB states that Article 26(3) "prohibits the presentation of any advertising based on profiling using such special categories of personal data."[[13]](#_ftn13)

---

## Footnotes (Original Format)

[[10]](#_ftnref10) DSA (n 1) recital 68.

[[11]](#_ftnref11) ibid recital 69.

[[12]](#_ftnref12) European Data Protection Board, Guidelines 3/2025 on the interplay between the Digital Services Act and the General Data Protection Regulation (adopted 12 September 2025) para 76.

[[13]](#_ftnref13) IAB Tech Lab, OpenRTB API Specification Version 2.6 (April 2022) https://iabtechlab.com/standards/openrtb/

---

## Expected Output After Conversion

After running the converter, the footnotes should look like this:

The DSA prohibition, rather clearly, does not displace the GDPR.[^10] Recital 68 emphasizes that the transparency requirements in Article 26(1) and (2) are "without prejudice" to the GDPR.[^11] Put differently, the GDPR governs whether and under what conditions profiling using special categories of personal data may lawfully occur; the DSA adds a display-layer constraint.[^12]

The EDPB has embraced this interpretation. In its draft Guidelines on the interplay between the DSA and the GDPR, the EDPB states that Article 26(3) "prohibits the presentation of any advertising based on profiling using such special categories of personal data."[^13]

## Footnotes

[^10]: DSA (n 1) recital 68.

[^11]: ibid recital 69.

[^12]: European Data Protection Board, Guidelines 3/2025 on the interplay between the Digital Services Act and the General Data Protection Regulation (adopted 12 September 2025) para 76.

[^13]: IAB Tech Lab, OpenRTB API Specification Version 2.6 (April 2022) https://iabtechlab.com/standards/openrtb/

---

## Test Instructions

1. Copy the "Sample Text with Footnotes" section (including the original footnotes at the bottom)
2. Paste it into a new Obsidian note
3. Run the "Convert footnotes in current note" command
4. Verify the output matches the "Expected Output After Conversion" section
5. Check that all footnote links work correctly
