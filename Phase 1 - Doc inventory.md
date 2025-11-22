# Phase 1: Document Inventory & Initial RQ Mapping

## Task Overview

Create an initial inventory of all analysis documents and map them to research questions (RQs). This provides the foundation for Phase 2's deep source extraction.

<investigation_before_answering>
Read each file completely before making claims about its contents. Never speculate.
</investigation_before_answering>

---

## Before You Begin: Read Context Files

**Required reading:**
1. `/00-Project-Meta/README.md` - Extract research questions, project goals
2. `/00-Project-Meta/DOCUMENT-TYPE-GUIDE.md` - Document type definitions
3. `/00-Project-Meta/Outline/` (if present) - Argument structure

**Optional:**
- `/06-Index-Files/PHASE0-REORGANIZATION-REPORT.md` - Note any ambiguous placements
- `/01-Primary-Sources/Case-Law/Case-Index.md` - Case reference table

---

## Step 1: Extract Research Questions

Read the README and extract the project's research questions. If not explicitly numbered, infer them from project structure.

**Begin your output with:**
```markdown
## Research Questions Identified
**Source:** [README explicit / inferred from outline]

**RQ1:** [Exact phrasing]
**RQ2:** [Exact phrasing]
...
```

---

## Step 2: Analyze All Documents

**Read all documents in:**
- `/02-Analysis-Legal/` (all subfolders)
- `/03-Analysis-[Domain]/` (if exists, all subfolders)

**For each document, record:**
- Filename and location (relative path)
- Document type (use DOCUMENT-TYPE-GUIDE categories)
- Length: short (<1000 words), medium (1000-5000), long (>5000)
- Primary RQ (which RQ is the main focus)
- Secondary RQs (others substantially addressed)
- Summary: 3-4 sentences on what it does, its contribution, and what makes it distinctive

**Summary quality:** Be specific about contributions, not just topics. "Provides comprehensive doctrinal analysis applying EU consumer protection law to AI pricing, arguing vague multipliers violate UCPD/CRD/UCTD through mathematical impossibility framing" not "Discusses AI and consumer law."

---

## Step 3: Create Inventory Document

**Create:** `/06-Index-Files/PHASE1-DOCUMENT-INVENTORY.md`
```markdown
# Phase 1: Document Inventory & Initial RQ Mapping
**Completed:** [Date]
**Project:** [Name from README]

---

## Research Questions Identified
[Your RQ extraction]

---

## Summary Statistics
- Total documents analyzed: [N]
- Document types: [list with counts]
- Documents by length: Short [N], Medium [N], Long [N]
- Documents per RQ: RQ1: [N] primary/[N] secondary [continue for all]

---

## Documents by RQ Assignment

### RQ1: [Full RQ statement]

#### Primary Documents (main focus on RQ1):
**[[Document Name]]**
- Location: `/path/to/file`
- Type: [type]
- Length: [short/medium/long]
- Also addresses: [other RQs if any]
- Summary: [3-4 sentences]

[Repeat for all]

#### Supporting Documents (partially addresses RQ1):
**[[Document Name]]**
- Location: `/path/to/file`
- Type: [type]
- Primary RQ: [N]
- How it supports RQ1: [1-2 sentences]

---

[Repeat structure for all RQs]

---

## Documents That Don't Clearly Map to RQs
[List with explanations, or state "All documents successfully mapped"]

---

## Analysis & Observations

### Coverage Patterns
**Strengths by RQ:** [Which RQs are well-supported]
**Gaps by RQ:** [Which RQs need more work]
**Document type distribution:** [Patterns observed]

### Cross-Cutting Documents
[Documents addressing 3+ RQs substantially - these are integrative pieces]

### Questions for Phase 2
- Which RQs need intensive source extraction?
- What ambiguities need resolving?
- Which RQ to start with?

---

## Recommendations for Human Review
[Priority items to verify before Phase 2]

---

## Ready for Phase 2
Recommend starting with: [RQ number - typically the one with most legal sources]
```

---

## Step 4 (Optional): Structure Maps for Long Documents

**For documents marked "long" (>1500 words):**

Create a structure map showing heading hierarchy. This helps Phase 2 understand document organization without re-reading entire files.

**Create:** `/06-Index-Files/PHASE1-STRUCTURE-MAPS.md`
```markdown
# Structure Maps for Long Documents

**Purpose:** Heading-level overviews of long documents (>5000 words) to facilitate Phase 2 extraction

---

## [Document Name]
**Location:** `/path/to/file`
**Estimated length:** [words/pages]

### Document Structure:
# Main Title
## Section 1
### Subsection 1.1
### Subsection 1.2
## Section 2
### Subsection 2.1
...

[Extract only markdown heading lines: #, ##, ###, ####]
[Preserve heading hierarchy]
[Do not include any body text]

---

[Repeat for each long document]
```

**Only create this file if you have documents >15000 words. If all documents are short, skip this step.**

---

## Quality Criteria

<success_criteria>
- Every analysis document is listed with accurate RQ assignment
- Summaries reflect actual document content (verified by reading)
- Uncertainties are flagged
- Clear foundation created for Phase 2
</success_criteria>

---

## When Complete

Present the inventory, highlight key findings, suggest which RQ to start Phase 2 with, and stop. Wait for researcher review before Phase 2.