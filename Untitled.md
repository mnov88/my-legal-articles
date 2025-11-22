
# Phase 2: Deep Source & Argument Extraction

## Task Overview

Extract detailed information about sources, arguments, and evidence for each RQ. This creates the foundation for indexes, YAML metadata, and the final framework document.

<investigation_before_answering>
Read documents completely. Verify all citations against actual document text. Never speculate about content.
</investigation_before_answering>

---

## Before You Begin: Review Phase 1 Outputs

**Required review:**
1. `/06-Index-Files/PHASE1-DOCUMENT-INVENTORY.md` - Which docs address which RQs, document summaries
2. `/06-Index-Files/PHASE1-STRUCTURE-MAPS.md` (if exists) - Section-level navigation for long docs

**Keep these references handy:**
- `/01-Primary-Sources/Case-Law/Case-Index.md` - Verify case citations and numbers
- `/00-Project-Meta/DOCUMENT-TYPE-GUIDE.md` - Understand document categories and purposes

**Use structure maps efficiently:**
- For long documents (>1200 words), use structure maps to locate relevant sections
- Note which sections contain which arguments/sources
- Avoid re-reading entire long documents when structure map enables targeted reading

---

## Work Process: One RQ at a Time

**CRITICAL: Complete extraction for one RQ fully before moving to the next.**

**For each RQ:**
1. Review all documents Phase 1 identified for that RQ (primary + supporting)
2. Extract all information per template below
3. Present the complete RQ section
4. Provide brief summary of findings (coverage, key sources, patterns)
5. Ask "Ready to proceed to RQ[N+1]?"
6. **WAIT for confirmation before starting next RQ**

This allows for course-correction on detail level, format adjustments, or additional guidance.

---

## What to Extract Per RQ

### 1. Sub-Topics & Specific Arguments
- Identify distinct sub-topics within the RQ
- For each: main argument, which documents discuss it, evidence used

### 2. Legal Sources Cited
**Adapt extraction based on legal system:**
- **For EU law:** Directives/Regulations (with article numbers), CJEU cases (with paragraph numbers)
- **For US law:** Statutes (USC sections), regulations (CFR), SCOTUS/Circuit cases (with page/paragraph)
- **For UK law:** Acts, Statutory Instruments, case citations
- **For mixed/comparative:** Use flexible "Source Type" categorization

Extract:
- Full citation
- Specific provisions/paragraphs cited
- What principle or rule is extracted
- Which documents cite this source

### 3. Secondary Sources (if applicable)
- Economic sources (for law & economics projects)
- Academic scholarship (if analyzed substantively, not just cited)
- Empirical studies
- Historical sources (for legal history)

**Skip this section if RQ is purely legal/doctrinal.**

### 4. Empirical Evidence & Data
- References to datasets, surveys, provider examples
- Statistical evidence
- Case studies or practical examples

### 5. Key Tests, Frameworks, or Legal Standards
- Doctrinal tests established by cases
- Analytical frameworks used across documents
- Standards or criteria repeatedly applied

---

## Output Format

**Create:** `/06-Index-Files/PHASE2-SOURCE-EXTRACTION.md`

**Work through RQs sequentially.** Add each completed RQ section to this file.

```markdown
# Phase 2: Source & Argument Extraction by RQ

**Project:** [Name]
**Extraction Date:** [Date]
**RQs Completed:** [List as you go - e.g., "RQ1, RQ2"]

---

## RQ1: [Full RQ statement from Phase 1]

### Documents Analyzed for RQ1
**Primary:** [List from Phase 1]
**Supporting:** [List from Phase 1]

### Sub-Topics & Arguments Discovered

**Sub-Topic 1: [Name]**
- **Main argument:** [2-3 sentences describing the core claim/position]
- **Found in:** [[Document 1]], [[Document 2]]
- **Evidence used:** [What data, examples, or empirical support is provided]
- **Relationship to other sub-topics:** [How this connects to other arguments in this RQ]

**Sub-Topic 2: [Name]**
[Same structure]

[Continue for all sub-topics]

---

### Legal Sources Cited for RQ1

**[Primary Legal Instruments]:** (Adapt label based on jurisdiction - e.g., "EU Directives", "US Statutes", "UK Acts")

| Citation | Article/Section | Principle/Provision | Used For | Found In |
|----------|-----------------|---------------------|----------|----------|
| [e.g., UCPD] | Art 7(1) | Misleading omissions | [argument it supports] | [[Doc A]], [[Doc B]] |
| [e.g., 15 USC] | §1692d | Harassment prohibition | [argument it supports] | [[Doc C]] |

**[Case Law]:** (Adapt based on court system - e.g., "CJEU Cases", "SCOTUS Cases", "Circuit Courts")

| Case | Citation | Paragraph/Page | Principle/Holding | Found In |
|------|----------|----------------|-------------------|----------|
| C-92/11 RWE | [full cite] | ¶49, ¶50 | Economic foreseeability test | [[Doc 1]], [[Doc 2]] |

**[Regulatory Materials]:** (if applicable - guidance, agency decisions, enforcement actions)

| Source | Type | Key Point | Used For | Found In |
|--------|------|-----------|----------|----------|
| FTC Guidance | Agency interpretation | [key point] | [argument] | [[Doc X]] |

**[Other Legal Sources]:**
[Legislative history, scholarly commentary treated as authority, international law, etc.]

---

### Secondary Sources for RQ1 (if applicable)

**Skip this section if RQ is purely legal/doctrinal.**

**Economic/Theoretical Sources:**
| Source | Author/Concept | Theory/Framework | Used For | Found In |
|--------|----------------|------------------|----------|----------|
| [Paper/book] | [Author] | [e.g., Price discrimination theory] | [application] | [[Doc]] |

**Empirical Studies:**
| Study | Methodology | Key Finding | Used For | Found In |
|-------|-------------|-------------|----------|----------|

---

### Empirical Evidence & Data for RQ1

**Datasets referenced:**
- [Name/description] - Found in: [[Doc]]

**Provider examples/case studies:**
- [e.g., OpenAI pricing structure] - Analyzed in: [[Doc]]

**Statistical evidence:**
- [Description] - Source: [[Doc]]

---

### Key Tests, Frameworks & Standards for RQ1

**[Test/Framework Name 1]:**
- **Established by:** [Case or source]
- **Definition:** [What the test/framework is]
- **Elements/Criteria:** [List if multi-part test]
- **Applied in:** [[Doc 1]], [[Doc 2]]
- **Application:** [How documents use this test - e.g., "Applied to show vague multipliers fail transparency requirement"]

**[Test/Framework Name 2]:**
[Same structure]

---

### RQ1 Extraction Summary

**Coverage assessment:**
- Sub-topics well-developed: [list]
- Sub-topics needing more work: [list]
- Source concentration: [e.g., "Heavy reliance on 3-4 cases; diverse directive coverage"]

**Key findings:**
- [Notable patterns, strong sources, gaps observed]

**Questions/notes:**
- [Anything unclear, ambiguous docs, recommended follow-up]

---

## RQ2: [Full statement]

[Repeat full structure for RQ2]

---

[Continue for all RQs]

---

# Cross-RQ Observations (Complete at end)

**After all RQs extracted, add this section:**

### Sources Appearing Across Multiple RQs

| Source | RQs | Different Uses |
|--------|-----|----------------|
| [e.g., C-92/11 RWE] | RQ1, RQ2, RQ4 | [How used in each context] |

### Thematic Connections

**Theme 1:** [Cross-RQ theme]
- Appears in: RQ[N], RQ[N]
- How it connects arguments: [explanation]

### Source Type Distribution

| RQ | Primary Legal | Case Law | Secondary | Empirical |
|----|---------------|----------|-----------|-----------|
| RQ1 | [count] | [count] | [count] | [count] |
| RQ2 | [count] | [count] | [count] | [count] |

### Overall Assessment

**Strengths:**
- [What's well-sourced across project]

**Gaps:**
- [What's missing or under-developed]

**Recommendations for next steps:**
- [What indexing tools to build based on this extraction]
```

---

## Quality Check Before Moving to Next RQ

Before asking to proceed to next RQ, verify:
- [ ] All primary documents for this RQ reviewed
- [ ] All supporting documents checked
- [ ] Legal sources extracted with full citations (not just mentions)
- [ ] Paragraph/page numbers included where provided in documents
- [ ] Sub-topics accurately reflect document arguments (not assumed)
- [ ] Tests/frameworks properly defined
- [ ] No speculation - everything based on actual document text
- [ ] Structure maps consulted for long documents

---

## Flexibility Notes

**Adapt extraction format based on project:**

1. **Pure doctrinal projects:** Focus on legal sources, skip secondary sources section
2. **Interdisciplinary projects:** Expand secondary sources, include all relevant methodologies
3. **Comparative projects:** Add jurisdiction column to tables
4. **Heavily case-driven projects:** Expand case table, condense others
5. **Statutory interpretation projects:** Expand statutory provisions, fewer cases

**If uncertain about format:** Present first RQ extraction, get feedback, adjust for remaining RQs.

---

## After All RQs Complete

1. **Add Cross-RQ Observations section** (template above)
2. **Present complete extraction document**
3. **Provide overall assessment:**
   - Which RQs have strongest source foundation
   - Where gaps exist
   - What should be built next (Legal Source Registry? Topic Maps? Other indexes?)
4. **Recommend next steps for Phase 3**

**Wait for review before proceeding to Phase 3 (Synthesis & Framework Creation).**

---
