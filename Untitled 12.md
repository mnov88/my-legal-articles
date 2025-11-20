**Absolutely!** Much better approach. Here's the 3-phase breakdown:

---

# Phase 1 Instructions: Document Inventory & Initial RQ Mapping

## Task Overview

You are helping organize a legal research project for an academic article. This is **Phase 1 of 3**: Create an initial inventory of all analysis documents and make preliminary assignments of which RQs each document addresses.

## The 5 Research Questions (for reference)

**RQ1:** Major AI services are marketed and sold under conditions which make it impossible to determine how much usage is included

**RQ2:** This is a clear violation of EU consumer protection laws

**RQ3:** Switching to billing models which are more transparent is not necessarily a net benefit

**RQ4:** Lessons from other industries (electricity/utilities, telecoms) and economics show similar challenges

**RQ5:** So what may work?

## Your Phase 1 Task

<investigation_before_answering> Read each file completely before making any claims about its contents. Never speculate. </investigation_before_answering>

### What to Do

1. **Systematically read** all documents in:
    
    - `/02-Analysis-Legal/` (and all subfolders)
    - `/03-Analysis-Economic/` (and all subfolders)
    - `/00-Project-Meta/README.md`
2. **For each document, record:**
    
    - Filename and location
    - Document type (legal analysis / economic analysis / framework mapping / hypothesis testing / etc.)
    - Estimated length (short <1000 words / medium 1000-5000 / long >5000)
    - Primary RQ addressed (your best assessment)
    - Secondary RQs addressed (if any)
    - One-paragraph summary (3-4 sentences) of what the document does

### Output Format

Create: `/06-Index-Files/PHASE1-DOCUMENT-INVENTORY.md`

```markdown
# Phase 1: Document Inventory & Initial RQ Mapping
**Completed:** [Date]

## Summary Statistics
- Total documents analyzed: [N]
- Legal analysis documents: [N]
- Economic analysis documents: [N]
- Documents per RQ:
  - RQ1: [N] documents
  - RQ2: [N] documents
  - RQ3: [N] documents
  - RQ4: [N] documents
  - RQ5: [N] documents

---

## Documents by RQ Assignment

### RQ1: Marketing Under Impossible-to-Determine Conditions

#### Primary Documents (mainly about RQ1):
**[[Document Name]]** 
- Location: `/path/to/file`
- Type: [legal analysis / economic analysis / etc.]
- Length: [short / medium / long]
- Also addresses: [RQ numbers if any]
- Summary: [3-4 sentence description of what this document contributes]

[Repeat for all primary RQ1 documents]

#### Supporting Documents (partially addresses RQ1):
[Same format, briefer]

---

### RQ2: Clear Violation of EU Consumer Protection Laws

[Same structure as RQ1]

---

[Continue for RQ3, RQ4, RQ5]

---

## Documents That Don't Clearly Map to RQs

[List any documents whose purpose or RQ assignment is unclear]

**[[Document Name]]**
- Location: 
- Why unclear: [explanation]

---

## Initial Observations

**Coverage patterns observed:**
- [e.g., "RQ2 has many legal analysis documents; RQ3 has many economic analyses"]

**Potential issues noted:**
- [e.g., "Several documents discuss pricing models but unclear if for RQ3 or background"]

**Questions for Phase 2:**
- [Specific things to investigate more deeply in Phase 2]
```

### Quality Criteria

<success_criteria>

- Every document in `/02-Analysis-Legal/` and `/03-Analysis-Economic/` is listed
- RQ assignments are preliminary but reasonable based on document content
- Summaries are accurate (verified by reading the files)
- Any uncertainties are explicitly flagged
- The output gives a clear overview of what exists </success_criteria>

### When Complete

After you finish Phase 1, stop and present the inventory. The researcher will review it before asking you to proceed to Phase 2 (deep source extraction).

---

# Phase 2 Instructions: Deep Source & Argument Extraction

**[These will be given AFTER Phase 1 is reviewed]**

## Task Overview

Building on Phase 1's document inventory, now extract detailed information about sources, arguments, and evidence for each RQ.

## Your Phase 2 Task

For each RQ, working one RQ at a time:

### What to Extract

1. **Sub-topics and specific arguments** made in the documents
2. **Legal sources cited:**
    - Directive articles (e.g., "UCPD Art 7(1)")
    - CJEU cases with paragraph numbers if provided (e.g., "C-92/11 RWE ¶49")
    - Other legal sources
3. **Economic/academic sources referenced**
4. **Empirical evidence** mentioned
5. **Key tests or frameworks** established

### Output Format

Create: `/06-Index-Files/PHASE2-SOURCE-EXTRACTION.md`

Work through one RQ at a time. For each RQ, create a detailed section:

```markdown
# Phase 2: Source & Argument Extraction by RQ
**Completed:** [Date]

---

## RQ1: [Full statement]

### Sub-Topics & Arguments Discovered

**[Sub-topic name]:**
- Main argument: [2-3 sentences]
- Found in: [[Document 1]], [[Document 2]]
- Evidence used: [what data/examples support this]

[Repeat for each sub-topic]

### Legal Sources Cited for RQ1

**EU Directives:**
| Article | Full Citation | Used For | Found In |
|---------|--------------|----------|----------|
| UCPD Art 7(1) | [exact text if quoted] | [what argument] | [[Doc name]] |

**CJEU Cases:**
| Case | Paragraph(s) | Principle/Holding | Found In |
|------|-------------|-------------------|----------|
| C-92/11 RWE | ¶49, ¶50 | Economic foreseeability test | [[Doc 1]], [[Doc 2]] |

**Other Legal Sources:**
[Enforcement actions, guidance documents, etc.]

### Economic/Academic Sources
[For economics-heavy RQs]
| Source | Concept/Theory | Used For | Found In |
|--------|---------------|----------|----------|

### Key Tests & Frameworks Established
- **[Test name]**: [Description - which case/source establishes it]
  - Applied in: [[Documents]]
  - Application: [how it's used in the argument]

---

[Repeat for RQ2, RQ3, RQ4, RQ5]
```

**Work systematically through the RQs. After completing extraction for each RQ, provide that section and wait for confirmation before moving to the next RQ.**

This allows for course-correction if the level of detail isn't right.

---

# Phase 3 Instructions: Synthesis & Gap Analysis

**[These will be given AFTER Phase 2 is reviewed]**

## Task Overview

Using Phases 1 and 2, create the final comprehensive framework with cross-cutting analysis and actionable recommendations.

## Your Phase 3 Task

### What to Create

1. **Cross-cutting analysis:**
    
    - Themes appearing across multiple RQs
    - Case law distribution patterns
    - Source type distribution
2. **Gap analysis:**
    
    - Which RQs are well-sourced vs. under-developed
    - Missing legal sources
    - Areas needing more evidence
3. **Strategic recommendations:**
    
    - Which RQs need what kind of indexing tools next
    - Priority order for further work

### Output Format

Create: `/06-Index-Files/00-RESEARCH-QUESTIONS-FRAMEWORK.md`

This is the final comprehensive document that combines all three phases into one complete framework. Use the structure from your original prompt but now informed by the detailed work from Phases 1 and 2.

**Include:**

- All RQ sections (synthesized from Phases 1 & 2)
- Cross-cutting analysis section
- Document-to-RQ mapping table
- Case law distribution by RQ
- Source type distribution
- **Next Steps & Recommendations** (this is the most important part - be specific about what indexing tools to build and why)

---

## Summary: The 3-Phase Approach

**Phase 1 (Start Here):** Document inventory - what exists and which RQs

- Output: Simple inventory with RQ assignments
- Stop and review before Phase 2

**Phase 2 (After Phase 1 approved):** Deep extraction - sources, arguments, evidence per RQ

- Output: Detailed source extraction, work one RQ at a time
- Pause for review between RQs if needed

**Phase 3 (After Phase 2 complete):** Synthesis - create final framework with gaps and recommendations

- Output: Complete comprehensive framework document
- This becomes the master reference

**Give the local AI Phase 1 instructions first. Review the inventory. Then give Phase 2. Review extractions. Then give Phase 3.**

Does this phased approach work better?