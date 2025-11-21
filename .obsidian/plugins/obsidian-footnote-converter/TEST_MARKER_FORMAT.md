# Test Document with Marker-Style Footnotes

This is a test document you can use to verify the plugin works with marker library PDF conversions.

## Sample Text with Footnotes

In its Communication on implementation and simplification ("A simpler and faster Europe"[1](#page-3-2) ), the Commission presented its approach to adapting the Union's regulatory framework to a more volatile world: a new drive to simplify, clarify and improve our common acquis.[2](#page-3-3)

This vision reflects the broader plan for Europe's competitiveness laid out by Commission President von der Leyen in her political guidelines for the 2024-2029 term.[3](#page-3-4) As also highlighted in the Draghi[4](#page-3-5) and Letta reports, the accumulation of rules has sometimes had an adverse effect on competitiveness.

---

## Footnotes (Original Format)

<span id="page-3-2"></span><sup>1</sup> Communication from the Commission to the European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions, A simpler and faster Europe: Communication on implementation and simplification, COM(2025)47 final, 11 February 2025

<span id="page-3-3"></span><sup>2</sup> European Council, Conclusions, EUCO 1/25, Brussels, 20 March 2025, paragraph. 13.

<span id="page-3-4"></span><sup>3</sup> Von der Leyen, U. (2024) *Europe's Choice: Political Guidelines for the Next European Commission 2024-2029*.

<span id="page-3-5"></span><sup>4</sup> Draghi, M. (2024) *The future of European competitiveness*.

---

## Expected Output After Conversion

After running the converter, the footnotes should look like this:

In its Communication on implementation and simplification ("A simpler and faster Europe"[^1] ), the Commission presented its approach to adapting the Union's regulatory framework to a more volatile world: a new drive to simplify, clarify and improve our common acquis.[^2]

This vision reflects the broader plan for Europe's competitiveness laid out by Commission President von der Leyen in her political guidelines for the 2024-2029 term.[^3] As also highlighted in the Draghi[^4] and Letta reports, the accumulation of rules has sometimes had an adverse effect on competitiveness.

## Footnotes

[^1]: Communication from the Commission to the European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions, A simpler and faster Europe: Communication on implementation and simplification, COM(2025)47 final, 11 February 2025

[^2]: European Council, Conclusions, EUCO 1/25, Brussels, 20 March 2025, paragraph. 13.

[^3]: Von der Leyen, U. (2024) *Europe's Choice: Political Guidelines for the Next European Commission 2024-2029*.

[^4]: Draghi, M. (2024) *The future of European competitiveness*.

---

## Test Instructions

1. Copy the "Sample Text with Footnotes" section (including the original footnotes)
2. Paste it into a new Obsidian note
3. Run the "Convert footnotes in current note" command
4. Verify the output matches the "Expected Output After Conversion" section
5. Check that all footnote links work correctly

## Additional Test Cases

### Test with Escaped Parentheses
Some marker outputs may have escaped parentheses like this: [10\)](#page-2-1)

This should convert to: [^10]
