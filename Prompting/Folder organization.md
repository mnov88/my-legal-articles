# Legal Research Project: Phase 0 Folder Reorganization

## Universal Folder Structure for Legal Research Projects

```
/[Your Project Name]/
├── 00-Project-Meta/
│   ├── README.md (project overview, research questions, goals)
│   ├── DOCUMENT-TYPE-GUIDE.md (definitions - see template below)
│   ├── style.md (citation style, writing guidelines)
│   └── Outline/ (argument structure, article outline)
│
├── 01-Primary-Sources/
│   ├── Case-Law/
│   │   ├── [Jurisdiction-A]/ (e.g., CJEU, SCOTUS, National)
│   │   ├── [Jurisdiction-B]/
│   │   └── Case-Index.md (quick reference table)
│   ├── Legislation/
│   │   ├── [Type-A]/ (e.g., Directives, Statutes, Regulations)
│   │   └── [Type-B]/
│   ├── Regulatory-Materials/
│   │   └── (Guidance, enforcement decisions, agency documents)
│   └── Academic-Sources/
│       └── (Scholarship you're analyzing as sources)
│
├── 02-Analysis-Legal/
│   ├── Doctrinal-Analysis/
│   ├── Framework-Mapping/
│   ├── Comparative-Analysis/ (if applicable)
│   └── Enforcement-Evidence/ (if applicable)
│
├── 03-Analysis-[Secondary-Domain]/ (if applicable)
│   ├── Economic/ (for law & economics projects)
│   ├── Empirical/ (for empirical legal studies)
│   ├── Historical/ (for legal history)
│   └── Cross-Cutting/
│
├── 04-Empirical-Data/ (if applicable)
│   ├── Datasets/
│   ├── Survey-Results/
│   └── Statistical-Analyses/
│
├── 05-Drafts/
│   └── [main-article].md
│
└── 06-Index-Files/ (leave as is or empty - for later phases)
```

---

## Phase 0 Instructions

### Task Overview

Reorganize a legal research project folder to separate primary legal sources from analytical work, organize by document type, and prepare for systematic indexing.

**This is a mechanical sorting task.** You do NOT need to:
- Read documents deeply
- Understand the research argument
- Map documents to research questions
- Create detailed summaries

You only need to:
- Identify document types based on filenames and quick scans
- Move files to appropriate folders
- Create basic catalogs

---

### Step 1: Analyze Current Structure

**Task 1.1: Examine what exists**
- List all current folders and files
- Identify patterns in naming conventions
- Note file types (.md, .pdf, .html, .csv, etc.)

**Task 1.2: Identify primary source types**
Look for files that are:
- Case names or numbers (e.g., "C-92-11", "Brown v Board", "Smith v Jones")
- Legislation names or numbers (e.g., "Directive 93/13", "15 USC 1", "Section 230")
- Regulatory materials (e.g., "FTC Guidance", "Commission Notice")
- Internal drafts, reports, AI deep research summaries
- Unmodified source documents

**Task 1.3: Identify analysis document types**
Look for files with keywords like:
- "analysis", "review", "assessment", "examination"
- "framework", "mapping", "comprehensive"
- "comparative", "enforcement", "case study"
- Multiple author-generated documents discussing sources

**Output:** Report on current structure and proposed subfolders

---

### Step 2: Create Folder Structure

Based on your analysis, create the folder structure above with these adaptations:

**For 01-Primary-Sources:**
- Customize jurisdiction folders based on what you find (e.g., CJEU, National Courts, Data Protection Authorities)
- Customize legislation folders by type (Directives, Statutes, Constitutional Provisions)
- Include Regulatory-Materials only if such documents exist

**For 02-Analysis-Legal:**
- Always include: Doctrinal-Analysis, Framework-Mapping
- Include Comparative-Analysis if multiple jurisdictions compared
- Include Enforcement-Evidence if regulatory/enforcement documents exist

**For 03-Analysis-[Secondary-Domain]:**
- Only create if project has significant interdisciplinary component
- Name based on actual secondary domain (Economic, Empirical, Historical, etc.)
- Omit entirely if project is purely doctrinal

**For 04-Empirical-Data:**
- Only create if CSV, dataset, or statistical files exist
- Omit if project is purely doctrinal/theoretical

---

### Step 3: Sorting Rules

<sorting_rules>

#### Primary Sources (→ 01-Primary-Sources/)

**Case-Law/[Jurisdiction name, CJEU, ECtHR]/:**
Include:
- Files with case names or numbers in filename
- Court decision documents
- HTML or PDF files from court databases
- Individual case markdown files

Exclude:
- Documents analyzing cases (those are analysis)
- Documents that cite many cases (those are your work)

**Legislation/[Type]/:**
Include:
- Files with legislation numbers (e.g., "93-13-EEC", "Title-VII", "Section-230")
- Statutory text files
- Directive/regulation text files
- Constitutional provisions

Exclude:
- Documents analyzing legislation
- Legislative history analysis (unless you're studying it as a source)

**Regulatory-Materials/:**
Include if any:
- Agency guidance documents
- Commission notices
- Enforcement decisions/actions
- Administrative rulings
- Official interpretive materials

Exclude:
- Your analysis of regulatory materials

**Academic-Sources/:**
Include:
- Academic papers/books you're analyzing AS sources (rare)
- Only if you're doing meta-analysis of scholarship

Exclude:
- Your own literature reviews
- Your analysis citing multiple academic sources

#### Analysis Documents (→ 02-Analysis-Legal/)

**Doctrinal-Analysis/:**
Include files that:
- Apply legal frameworks to specific scenarios
- Argue how law should be interpreted
- Synthesize multiple sources to make arguments
- Have conclusions about legality/interpretation
- Cite multiple cases and statutes together

Keywords: "analysis", "application", "argument", "doctrinal"

**Framework-Mapping/:**
Include files that:
- Systematically present legal frameworks
- Organize by source (article-by-article, section-by-section)
- Describe law comprehensively without applying to specific facts
- Serve as reference documents

Keywords: "framework", "mapping", "comprehensive", "systematic"

**Comparative-Analysis/:**
Include files that:
- Compare legal approaches across jurisdictions
- Analyze convergence/divergence of legal systems
- Contrast statutory/case law frameworks

Keywords: "comparative", "jurisdictions", "cross-border"


#### Secondary Domain Analysis (→ 03-Analysis-[Domain]/)

**Only create this folder if project has significant interdisciplinary component.**

Include files focused on:
- Economic analysis (law & economics)
- Empirical studies (empirical legal studies)
- Historical analysis (legal history)
- Sociological analysis (law & society)
- Other interdisciplinary approaches

**Cross-Cutting/:**
- Analysis spanning multiple categories
- Hypothesis testing across domains
- Integrative syntheses

#### Source Reference Documents (→ 01-Primary-Sources/)

**What:** Tables, lists, indexes, or catalogs OF primary sources

**Include:**
- Case law tables/indexes
- Legislation lists
- Source bibliographies
- Annotated source catalogs
- "Articles interpreted" lists

**Place in the relevant subfolder:**
- Case-related → Case-Law/Case-Index.md // example, retain OG filename
- Legislation-related → Legislation/Legislation-Index.md
- General source lists → Source-Bibliography.md

**How to identify:**
- Titles: "table", "list", "index", "catalog", "bibliography"
- Format: Tables or structured lists
- Content: Metadata about sources (not analysis of them)

**Not the same as:**
- The sources themselves (those go in jurisdiction/type subfolders)
- Your analysis of sources (those go in 02-Analysis-Legal/)

</sorting_rules>


---

### Step 4: Execute Reorganization

**Before moving anything:**
1. Create complete backup of current folder structure
2. Document current state for reference

**While moving files:**
1. Preserve all original filenames
2. Move entire subfolders as units when logical
3. For ambiguous files, make best judgment and flag for review
4. Do NOT delete anything
5. Do NOT rename files
6. Do NOT merge or split documents

**After moving files:**
Create verification list of any ambiguous placements

---

### Step 5: Create Folder Catalogs

In each major folder, create `_CONTENTS.md`:

**Template:**

```markdown
# Contents: [Folder Name]

**Purpose:** [1 sentence: what this folder contains]

**Total files:** [N]

---

## Files

### [Filename or subfolder name]
- **Type:** [case / statute / analysis / etc.]
- **Note:** [Any placement ambiguities or special notes, leave out if none truly present]

[Repeat for each file/subfolder]

---

```

Create catalogs for:
- Each subfolder in `/01-Primary-Sources/`
- Each subfolder in `/02-Analysis-Legal/`


---

### Decision Rules for Ambiguous Cases

**When uncertain where a file belongs:**

1. **Primary source vs analysis?**
   - Is it an original legal text → Primary
   - Does it cite/analyze multiple sources → Analysis

2. **Which analysis subfolder?**
   - Does it argue/apply law → Doctrinal-Analysis
   - Does it systematically describe law → Framework-Mapping
   - Does it compare jurisdictions → Comparative-Analysis


3. **Still uncertain?**
   - Make best-guess placement
   - Document decision in catalog's "Organization Notes"
   - Flag for human review

**Principles:**
- When in doubt, choose the more specific folder
- If file serves multiple purposes, choose its PRIMARY purpose
- Consistency matters more than perfection

---

### Quality Checklist

Before marking Phase 0 complete:

- [ ] All files from original location are accounted for
- [ ] No files deleted or renamed
- [ ] Every major folder has `_CONTENTS.md`
- [ ] Ambiguous placements are documented
- [ ] Backup of original structure exists
- [ ] Primary sources clearly separated from analysis
- [ ] Analysis documents logically categorized

---

### Output Deliverables

1. **Reorganized folder structure** following template above
2. **`_CONTENTS.md` files** in each major folder
3. **Phase 0 completion report:** `/06-Index-Files/PHASE0-REORGANIZATION-REPORT.md`

**Report template:**
```markdown
# Phase 0: Folder Reorganization Report

**Completed:** [Date]

## Summary
- Total files processed: [N]
- Primary sources identified: [N]
- Analysis documents identified: [N]
- Data files identified: [N]

## Folder Structure Created
[List of folders created]

## Files Moved
- To 01-Primary-Sources: [N] files
- To 02-Analysis-Legal: [N] files
- To 03-Analysis-[Domain]: [N] files (if applicable)
- To 04-Empirical-Data: [N] files (if applicable)

## Ambiguous Placements
[List any files whose placement was unclear, with explanation of decision made, only in cases of genuine and high doubt, otherwise leave out]

## Recommendations for alternative structure
[If there is a very strong case to be made that several files would benefit from the project files being structured differently, and that would enhance workflow significantly, note here why, 1-2 sentences max per proposal, otherwise. leve out]

```

---

## What NOT to Do in Phase 0

**Do NOT:**
- Read documents in detail (just scan for categorization)
- Understand the research argument (that's Phase 1)
- Map documents to research questions (that's Phase 1)
- Create detailed summaries (that's Phase 1)
- Add metadata or YAML (that's Phase 2+)
- Attempt any analysis of content
- Delete or rename any files
- Create complex nested hierarchies (keep it 2-3 levels)

**This is mechanical sorting only.** When in doubt about classification: consult [[/00-Project-Meta/DOCUMENT-TYPE-GUIDE.md]]

---
