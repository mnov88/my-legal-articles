# Phase 2: Deep Source & Argument Extraction

**[Given AFTER Phase 1 review and confirmation]**

<task_context>
This phase extracts detailed source citations, arguments, and evidence from analysis documents. The extraction creates structured data that will power:
- Legal Source Registry (quick lookup of cases/statutes)
- YAML metadata for document files
- Topic maps and argument matrices
- Phase 3's comprehensive framework document

Accuracy is critical—this extraction becomes the single source of truth for all downstream indexing work.
</task_context>

<investigation_before_answering>
Read documents completely. Verify all citations against actual document text. Base everything on what documents actually say, not assumptions about what they should say.
</investigation_before_answering>

---

## Reference Materials (Review Before Starting)

<required_context_files>
**Phase 1 outputs to review:**
- `/06-Index-Files/PHASE1-DOCUMENT-INVENTORY.md` - Which docs address which RQs, document summaries
- `/06-Index-Files/PHASE1-STRUCTURE-MAPS.md` (if exists) - Section-level navigation for long docs

**Project reference files:**
- `/01-Primary-Sources/Case-Law/Case-Index.md` - Verify case citations and numbers
- `/00-Project-Meta/DOCUMENT-TYPE-GUIDE.md` - Understand document categories and purposes
- `/00-Project-Meta/README.md` - Project goals and context

**Using structure maps effectively:**
For documents over 1200 words, the structure map shows the heading hierarchy. Use this to:
- Locate specific sections quickly without re-reading entire document
- Identify which sections discuss which sources/arguments
- Navigate efficiently to relevant content
- Note in extraction which sections contain which information (helps future lookup)
</required_context_files>

---

## Work Process: Sequential RQ Extraction

<work_rhythm>
**Complete one RQ fully before moving to the next.** This allows for format adjustments and detail-level calibration.

**For each RQ:**
1. Review all documents Phase 1 identified (primary + supporting)
2. Extract all information per template below
3. Present the complete RQ section
4. Provide brief findings summary (coverage, key sources, patterns, gaps)
5. Ask: "Ready to proceed to RQ[N+1]? Any format adjustments needed?"
6. Wait for confirmation before starting next RQ

**Why this matters:** The first RQ extraction serves as a template. If the detail level isn't right, or if certain sections need more/less depth, we can adjust before processing remaining RQs. This prevents redoing work.
</work_rhythm>

---

## What to Extract

<extraction_targets>

### 1. Sub-Topics & Specific Arguments

**Goal:** Break down each RQ into distinct sub-topics showing the argument structure.

**What to capture:**
- Sub-topic name (concise, descriptive)
- Main argument being made (2-3 sentences)
- Which documents discuss this sub-topic
- Evidence supporting the argument (data, examples, case studies)
- How sub-topics relate to each other (build on, contrast with, support)

**Example of good sub-topic extraction:**
```
**Sub-Topic: Mathematical Impossibility of Evaluating Vague Multipliers**
- Main argument: Consumers cannot foresee economic consequences when purchasing "5x more usage" if baseline is undefined, because multiplying an unknown variable by a constant produces an unknown result. This is not merely difficult—it's mathematically impossible, distinguishing it from ordinary transparency violations.
- Found in: [[EU consumer protection law Claude]], [[EU consumer protection vague terms]]
- Evidence used: RWE Vertrieb ¶49 requirement that consumers "foresee economic consequences," mathematical logic demonstrating impossibility, actual provider examples (OpenAI "dynamically adjusted" caps)
- Relationship: This argument strengthens the UCPD Art 7 violation claim by showing information doesn't just need better communication—it may not exist in determinate form
```

### 2. Legal Sources

**Goal:** Create comprehensive catalog of every legal source cited, with precise citations.

**Adapt extraction format based on legal system:**
- **EU law:** Directives/Regulations (article numbers), CJEU cases (paragraph numbers)
- **US law:** Statutes (USC sections), Regulations (CFR citations), Court cases (page/paragraph)
- **UK law:** Acts, Statutory Instruments, case citations
- **Mixed/Comparative:** Use flexible categorization by source type

**What to extract for each source:**
- Full citation as it appears in documents
- Specific provisions/paragraphs cited (not just "generally cited")
- Principle, rule, or holding extracted from this source
- Which documents cite it (helps assess how central it is)
- How it's used (establishes test, supports argument, provides exception, etc.)

**Example of good legal source extraction:**
```
| Case | Citation | Paragraph(s) | Principle/Holding | Used For | Found In |
|------|----------|--------------|-------------------|----------|----------|
| C-92/11 RWE Vertrieb | [2013] ECR I-1 | ¶49 | Consumers must "foresee economic consequences" based on "clear, intelligible criteria" | Economic foreseeability test—core transparency requirement | [[Doc A]], [[Doc B]], [[Doc C]] |
| C-92/11 RWE Vertrieb | [2013] ECR I-1 | ¶50 | Transparency requires "specific functioning of mechanism," not just grammatical clarity | Substantive vs. formal transparency distinction | [[Doc A]], [[Doc D]] |
```

### 3. Secondary Sources (If Applicable)

**When to extract this:** Only if RQ has significant interdisciplinary component (economics, empirical studies, history, sociology).

**Skip entirely if:** RQ is purely legal/doctrinal.

**What to capture:**
- Economic theories or frameworks
- Empirical studies with methodologies
- Academic scholarship analyzed substantively
- Historical sources (for legal history projects)

### 4. Empirical Evidence & Data

**What to capture:**
- References to datasets or surveys
- Statistical evidence or quantitative claims
- Provider examples or case studies (e.g., "OpenAI's pricing structure")
- Real-world examples used as evidence

**Why this matters:** Distinguishes between pure legal argument and argument supported by real-world data. Helps identify where claims need empirical backing.

### 5. Key Tests, Frameworks & Legal Standards

**What to capture:**
- Doctrinal tests established by cases (e.g., "three-part test from Smith v. Jones")
- Analytical frameworks used across documents (e.g., "proportionality assessment")
- Standards or criteria repeatedly applied
- Multi-element tests with defined components

**Include:**
- Which case/source establishes the test
- Definition and elements
- How documents apply it
- What conclusion the test supports

</extraction_targets>

---

## Output Structure

<output_format>

**Create:** `/06-Index-Files/PHASE2-SOURCE-EXTRACTION.md`

Add each completed RQ section sequentially to this file.

**File header:**
```markdown
# Phase 2: Source & Argument Extraction by RQ

**Project:** [Name from README]
**Extraction Date:** [Date]
**RQs Completed:** [Update as you go - e.g., "RQ1, RQ2, RQ3"]
**Total RQs:** [N]

---
```

**For each RQ, use this structure:**
```markdown
## RQ[N]: [Full RQ statement from Phase 1]

### Documents Analyzed for RQ[N]
**Primary documents:** [[Doc 1]], [[Doc 2]], [[Doc 3]]
**Supporting documents:** [[Doc A]], [[Doc B]]

---

### Sub-Topics & Arguments

**Sub-Topic 1: [Descriptive Name]**
- **Main argument:** [2-3 sentences]
- **Found in:** [[Docs]]
- **Evidence used:** [Specific data, examples, or sources]
- **Relationship to other sub-topics:** [How it connects]

**Sub-Topic 2: [Name]**
[Same structure]

[Continue for all sub-topics identified]

---

### Legal Sources for RQ[N]

**[Primary Legal Instruments]:** [Adapt label - e.g., "EU Directives & Regulations", "US Statutes", "UK Acts"]

| Source | Article/Section | Specific Provision | Used For | Found In |
|--------|-----------------|-------------------|----------|----------|
| [Name] | [Art/§] | [Principle or rule stated] | [What argument it supports] | [[Docs]] |

**[Case Law]:** [Adapt label - e.g., "CJEU Cases", "SCOTUS Cases", "Circuit Courts", "National Cases"]

| Case | Citation | Paragraph/Page | Principle/Holding | Used For | Found In |
|------|----------|----------------|-------------------|----------|----------|
| [Name] | [Full cite] | [¶ or p.] | [What case establishes] | [Application] | [[Docs]] |

**[Regulatory Materials]:** [If applicable - guidance, agency decisions, enforcement]

| Source | Type | Key Point | Used For | Found In |
|--------|------|-----------|----------|----------|
| [Name] | [Agency guidance/decision/etc.] | [Main principle] | [Application] | [[Docs]] |

**[Other Legal Sources]:**
[Legislative history, commentary, international law, model laws, restatements, etc.]

---

### Secondary Sources for RQ[N]

**[Skip this section if RQ is purely doctrinal]**

**Economic/Theoretical:**
| Source | Author/Theory | Key Concept | Used For | Found In |
|--------|---------------|-------------|----------|----------|

**Empirical Studies:**
| Study | Methodology | Key Finding | Application | Found In |
|-------|-------------|-------------|-------------|----------|

**[Other relevant categories]:**
[Historical sources, sociological studies, etc.]

---

### Empirical Evidence & Data for RQ[N]

**Datasets/Surveys:**
- [Description] - Found in: [[Doc]]

**Provider Examples/Case Studies:**
- [Specific example, e.g., "Anthropic Claude Pro '5x usage' claim without baseline"] - Analyzed in: [[Doc]]

**Statistical Evidence:**
- [Specific statistic or quantitative claim] - Source: [[Doc]]

**Real-World Examples:**
- [Practical examples used as evidence]

---

### Key Tests, Frameworks & Standards for RQ[N]

**[Test/Framework Name]:**
- **Established by:** [Case, statute, or source]
- **Definition:** [What the test is]
- **Elements/Criteria:** [If multi-part test, list components]
- **Applied in:** [[Doc 1]], [[Doc 2]]
- **Application & Conclusion:** [How documents use this test and what it shows]

[Repeat for all key tests]

---

### RQ[N] Extraction Summary

**Coverage strength:**
- Well-developed sub-topics: [List]
- Under-developed areas: [List]
- Source depth: [Assessment - e.g., "Heavy reliance on 3-4 seminal cases; broad directive coverage"]

**Key findings:**
- [Notable patterns, especially strong sources, central arguments]

**Gaps or questions:**
- [Anything unclear, contradictions, areas needing more sources]

**Estimated readiness:** [For this RQ: Strong foundation / Adequate / Needs more development]

---
```

</output_format>

---

## Examples of Good vs. Poor Extraction

<quality_examples>

### Example 1: Sub-Topic Extraction

❌ **Poor extraction:**
```
**Sub-Topic: Transparency**
- Main argument: Terms must be transparent
- Found in: [[Doc 1]]
- Evidence: Cases say so
```

✅ **Good extraction:**
```
**Sub-Topic: Substantive Transparency Requirement Beyond Formal Clarity**
- Main argument: CJEU requires substantive transparency—not just grammatically clear language, but information enabling consumers to evaluate economic consequences. Terms may be formally clear ("5x more") yet fail substantive transparency if underlying mechanism is undefined.
- Found in: [[EU consumer protection law Claude]], [[Framework Mapping]]
- Evidence: RWE Vertrieb ¶49-50 (economic foreseeability test), Kásler ¶75 ("not purely formal"), Andriciuc ¶50 (evaluate consequences), real-world example of Anthropic's "5x" claim without published baseline
- Relationship: Distinguishes this violation from ordinary vagueness; supports argument that compliance requires mechanism disclosure, not just clearer wording
```

### Example 2: Legal Source Extraction

❌ **Poor extraction:**
```
| Case | Used For |
|------|----------|
| RWE case | Transparency |
```

✅ **Good extraction:**
```
| Case | Citation | Paragraph(s) | Principle/Holding | Used For | Found In |
|------|----------|--------------|-------------------|----------|----------|
| C-92/11 RWE Vertrieb AG v Verbraucherzentrale | [2013] ECR I-1 | ¶49 | Consumers must "foresee economic consequences" based on "clear, intelligible criteria" | Core test for transparency compliance under UCTD Art 5—applied to show undefined baseline prevents foreseeability | [[Doc A]], [[Doc B]], [[Doc C]] |
| C-92/11 RWE Vertrieb | [2013] ECR I-1 | ¶50 | Transparency requires contract "set out transparently the specific functioning of the mechanism" | Substantive transparency requirement—shows that "5x more" alone insufficient; mechanism must be disclosed | [[Doc A]], [[Doc D]] |
```

### Example 3: Test/Framework Extraction

❌ **Poor extraction:**
```
**Economic foreseeability test:** From RWE case. Used in documents.
```

✅ **Good extraction:**
```
**Economic Foreseeability Test:**
- **Established by:** C-92/11 RWE Vertrieb ¶49
- **Definition:** Consumers must be able to "foresee, on the basis of clear, intelligible criteria, the alterations which may be made" to contractual terms, particularly price-related terms
- **Elements:** (1) Clear criteria must exist; (2) Criteria must be intelligible to average consumer; (3) Consumer must be able to foresee economic consequences based on those criteria
- **Applied in:** [[EU consumer protection law Claude]], [[Framework Mapping]], [[Doctrinal Analysis X]]
- **Application & Conclusion:** Documents apply this test to AI pricing claims like "5x more usage" and demonstrate mathematical impossibility of foreseeability when baseline undefined: 5 × [unknown] = [unknown]. Test fails at element (3) not because consumer lacks sophistication, but because the information needed to foresee consequences doesn't exist in determinate form. Documents conclude this transforms transparency failure into fundamental contract formation issue.
```

</quality_examples>

---

## Format Flexibility Guidelines

<adaptability>

**Adjust extraction based on project characteristics:**

**For pure doctrinal projects:**
- Deep extraction of legal sources
- Skip or minimize secondary sources section
- Focus on tests and doctrinal frameworks

**For interdisciplinary projects:**
- Balance legal and non-legal sources
- Expand secondary sources section
- Show how different methodologies interact

**For comparative law projects:**
- Add jurisdiction column to all tables
- Note where sources align/diverge across jurisdictions
- Track jurisdiction-specific applications

**For case-heavy projects:**
- Expand case law tables with more detail
- May consolidate statutory provisions if fewer
- Track how cases interpret statutes

**For statutory interpretation projects:**
- Deep extraction of statutory provisions (article-by-article if needed)
- Track interpretive sources (cases, guidance, commentary)
- Map how different sources interpret same provisions

**If format needs adjustment after RQ1:** Present what you've done, explain what might work better, and adjust for remaining RQs based on feedback.

</adaptability>

---

## Quality Verification

<success_criteria>

Before completing each RQ extraction, verify:

**Completeness checks:**
- [ ] All primary documents for this RQ reviewed
- [ ] All supporting documents checked
- [ ] Long documents navigated using structure maps where available

**Citation accuracy:**
- [ ] Legal sources include full citations (not just names)
- [ ] Paragraph/page numbers included where documents provide them
- [ ] Article/section numbers specified
- [ ] Case names and numbers match Case Index

**Content accuracy:**
- [ ] Sub-topics reflect actual document arguments (not assumed)
- [ ] Source uses verified against document text
- [ ] Tests/frameworks properly defined with all elements
- [ ] No speculation—everything traceable to specific documents

**Utility checks:**
- [ ] Extraction provides enough detail to be useful without re-reading documents
- [ ] Tables are complete and consistent
- [ ] Relationships between sub-topics are explained
- [ ] Gaps and strengths clearly identified

</success_criteria>

---

## After Completing All RQs

<final_synthesis>

**Add this section to the extraction file:**

### Cross-RQ Analysis

**Sources Appearing Across Multiple RQs:**

| Source | RQs Where Used | Different Applications |
|--------|----------------|----------------------|
| [Source] | RQ1, RQ2, RQ4 | RQ1: [how used]; RQ2: [how used]; RQ4: [how used] |

**Thematic Connections:**

**[Theme Name]:**
- Appears in: RQ[N], RQ[N], RQ[N]
- Connection: [How this theme ties together different parts of the argument]

**Source Type Distribution:**

| RQ | Primary Legal | Case Law | Secondary | Empirical |
|----|---------------|----------|-----------|-----------|
| RQ1 | [count] | [count] | [count] | [count] |
| RQ2 | [count] | [count] | [count] | [count] |

**Overall Assessment:**

**Project-wide strengths:**
- [What's well-sourced across all RQs]
- [Especially strong areas]

**Project-wide gaps:**
- [What's missing or under-sourced]
- [RQs needing more development]

**Recommendations for next steps:**
Based on this extraction, recommend:
- Which indexing tools to build (Legal Source Registry for case-heavy RQs? Topic Maps for complex arguments? Argument Matrix for conflicting interpretations?)
- Priority order (which RQs need indexes first)
- Any structural adjustments to improve usability

</final_synthesis>

---

## Completion and Next Steps

<workflow_transition>

**After presenting complete extraction:**

1. **Provide overall assessment:**
   - Which RQs have strongest source foundation
   - Where critical gaps exist
   - Source concentration patterns (relying on few vs. many sources)

2. **Recommend specific next steps:**
   - "Based on RQ2's heavy case law reliance, recommend building Legal Source Registry next"
   - "RQ3's complex argument structure suggests Topic Map would be most useful"
   - Prioritize by: (a) what's most needed for drafting, (b) what RQ is written first

3. **Note on metadata:**
   - This extraction provides all information needed for YAML frontmatter
   - After review, a separate mini-task will add YAML to individual files
   - These extraction tables are the single source of truth for metadata

4. **Wait for review before Phase 3**

Phase 3 will synthesize everything into the final Research Questions Framework document with comprehensive analysis and strategic recommendations.

</workflow_transition>