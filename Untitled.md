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
└── 06-Index-Files/ (leave empty - for later phases)
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
[List any files whose placement was unclear, with explanation of decision made]

## Recommendations for Human Review
[Specific files or decisions that should be verified]

## Ready for Next Phase
Phase 0 complete. Project is ready for Phase 1 (Document Inventory & RQ Mapping).
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

**This is mechanical sorting only.**

---

# Generic Document Type Guide for Legal Research Projects

Save as: `/00-Project-Meta/DOCUMENT-TYPE-GUIDE.md`

---

```markdown
# Document Type Guide for Legal Research

**Purpose:** Defines categories of documents in this project to ensure consistent organization and reference.

---

## 1. PRIMARY SOURCES

Documents that ARE the law or official legal materials, not your analysis of them.

### 1.1 Case Law
**What it is:** Court decisions, judicial opinions, case reports

**Characteristics:**
- Has case name/number (e.g., "C-92/11 RWE", "Brown v. Board", "R v. Smith")
- Contains judge's/court's reasoning
- Official court document or database export
- Numbered paragraphs or page numbers from reports

**Examples:**
- CJEU judgments
- Supreme Court opinions
- Circuit court decisions
- National court judgments

**What does NOT belong here:**
- Your case notes
- Your case briefs
- Analysis of multiple cases together

---

### 1.2 Legislation
**What it is:** Enacted laws, statutes, directives, regulations, constitutional provisions

**Characteristics:**
- Has official citation number
- Organized by articles/sections
- Official text from legislature/regulatory body
- May include explanatory memoranda or official notes

**Examples:**
- EU Directives (93/13/EEC)
- Statutes (Title VII, ADA)
- Regulations (CFR sections)
- Constitutional articles

**What does NOT belong here:**
- Legislative history analysis (unless you're studying it AS a source)
- Your commentary on legislation

---

### 1.3 Regulatory Materials
**What it is:** Official guidance, agency decisions, enforcement actions, administrative materials

**Characteristics:**
- Issued by regulatory/administrative bodies
- Official interpretive guidance
- Enforcement decisions/orders
- Agency policy statements

**Examples:**
- FTC guidance documents
- Commission interpretive communications
- Agency enforcement decisions
- Regulatory notices

**What does NOT belong here:**
- Your analysis of regulatory patterns
- Compilations of enforcement data (that's analysis)

---

### 1.4 Academic Sources (as primary sources)
**What it is:** Scholarship you're analyzing AS a source (rare in most legal research)

**When to use this category:**
- You're doing meta-analysis of legal scholarship
- You're studying doctrinal development through academic writing
- Specific articles are objects of study, not tools for study

**Most of the time:** Academic sources you cite belong in your analysis documents, not here.

---

## 2. LEGAL ANALYSIS DOCUMENTS

Your analytical work applying, interpreting, synthesizing, or arguing about legal sources.

### 2.1 Doctrinal Analysis
**What it is:** Application of legal frameworks to specific scenarios; argumentation about how law should be interpreted; synthesis of multiple sources to make legal claims

**Characteristics:**
- **Applies** law to facts or scenarios
- **Argues** for particular interpretations
- **Synthesizes** multiple cases and statutes
- **Concludes** about legality or proper interpretation
- Organized around legal arguments or claims
- Cites extensively across sources

**Structure often includes:**
- Statement of legal issue
- Relevant legal framework
- Application of framework
- Analysis of how cases/statutes interact
- Conclusions about legal outcomes

**Examples:**
- "Analysis of AI Pricing Under EU Consumer Law"
- "Application of First Amendment to Social Media"
- "Doctrinal Examination of Negligence Standards"

**Keywords in titles:** "analysis", "application", "examination", "argument", "doctrinal"

---

### 2.2 Framework Mapping
**What it is:** Systematic, comprehensive presentation of legal frameworks; reference-style organization of legal sources; descriptive rather than argumentative

**Characteristics:**
- **Describes** rather than applies
- Organized by **source** (directive-by-directive, section-by-section)
- **Comprehensive** coverage of legal area
- **Encyclopedia-style** presentation
- Minimal argument; maximum description
- Serves as reference document

**Structure often includes:**
- Article-by-article breakdown
- Provision-by-provision analysis
- Systematic presentation of requirements
- Summaries of key interpretive cases for each provision

**Examples:**
- "EU Consumer Protection Framework: Article-by-Article Analysis"
- "Complete Guide to Title VII Requirements"
- "Systematic Mapping of GDPR Provisions"

**Keywords in titles:** "framework", "mapping", "systematic", "comprehensive", "guide"

**How to distinguish from Doctrinal Analysis:**
- Framework Mapping: "Here's what Article 5 says and means"
- Doctrinal Analysis: "Here's why this practice violates Article 5"

---

### 2.3 Comparative Analysis
**What it is:** Comparison of legal approaches across jurisdictions, systems, or time periods

**Characteristics:**
- Analyzes **multiple jurisdictions**
- Compares legal approaches, interpretations, or outcomes
- Identifies convergence/divergence
- Contrasts different legal systems' treatment of similar issues

**Examples:**
- "US and EU Approaches to Privacy Regulation"
- "Comparative Analysis of Unfair Terms Directives"
- "Convergence in Competition Law Across Jurisdictions"

**Keywords in titles:** "comparative", "cross-border", "jurisdictions", "convergence"

---

### 2.4 Enforcement Evidence
**What it is:** Documentation and analysis of how law is actually enforced; patterns in regulatory action; evidence of legal risk

**Characteristics:**
- Documents **regulatory activities**
- Analyzes **enforcement patterns**
- Compiles **penalty/sanction data**
- Reports on agency actions
- Evidence of practical application

**Examples:**
- "FTC Enforcement Actions on Dark Patterns"
- "DGCCRF Prosecutions of Vague Claims"
- "Survey of Consumer Protection Enforcement 2020-2024"

**Keywords in titles:** "enforcement", "regulatory action", "prosecutions", "penalties"

**How to distinguish from other types:**
- This is about ACTUAL enforcement, not theoretical liability
- Documents what regulators HAVE done, not what law REQUIRES

---

## 3. SECONDARY DOMAIN ANALYSIS

For interdisciplinary legal research projects.

### 3.1 Economic Analysis
**For:** Law & economics projects

**What it is:** Economic theory applied to legal questions; efficiency analysis; market structure implications; behavioral economics

**Examples:**
- Analysis of pricing models
- Efficiency of legal rules
- Market impacts of regulation
- Behavioral effects of legal requirements

---

### 3.2 Empirical Analysis
**For:** Empirical legal studies

**What it is:** Quantitative/qualitative study of legal phenomena; statistical analysis; surveys; data-driven research

**Examples:**
- Statistical analysis of case outcomes
- Survey of compliance rates
- Regression analysis of legal variables

---

### 3.3 Historical Analysis
**For:** Legal history projects

**What it is:** Development of legal doctrine over time; historical context of legal rules; evolution of interpretation

---

### 3.4 Comparative Industry/Sector Analysis
**For:** Projects examining regulatory approaches in other sectors

**What it is:** How other industries handle similar regulatory challenges; lessons from adjacent regulatory regimes

**Examples:**
- "Telecommunications Pricing Transparency Approaches"
- "Utilities Regulation Comparison"
- "Lessons from Financial Services Disclosure"

---

### 3.5 Cross-Cutting/Integrative Analysis
**What it is:** Analysis spanning multiple secondary domains or integrating multiple analytical approaches

**Examples:**
- Interdisciplinary hypothesis testing
- Analyses combining economic, behavioral, and legal perspectives
- Comprehensive assessments across methodologies

---

## 4. CLASSIFICATION GUIDELINES

### How to Determine Document Type

**Step 1: Is it a primary source or your analysis?**
- If it's an original legal text/document → Primary Source (Section 1)
- If you created it by analyzing sources → Analysis (Section 2 or 3)

**Step 2: If analysis, what kind?**

Ask these questions:

**Does it APPLY law to specific facts/scenarios?**
→ Doctrinal Analysis (2.1)

**Does it DESCRIBE legal framework systematically?**
→ Framework Mapping (2.2)

**Does it COMPARE multiple jurisdictions?**
→ Comparative Analysis (2.3)

**Does it DOCUMENT enforcement patterns?**
→ Enforcement Evidence (2.4)

**Does it use non-legal methodologies primarily?**
→ Secondary Domain Analysis (Section 3)

**Step 3: Still uncertain?**
- Choose based on PRIMARY purpose
- A document may do multiple things—categorize by what it does MOST
- Document ambiguity in notes

---

## 5. EXAMPLES BY PROJECT TYPE

### Constitutional Law Project
- Primary Sources: Constitutional text, Supreme Court opinions, legislative history
- Doctrinal Analysis: Application of constitutional tests to new scenarios
- Framework Mapping: Systematic presentation of First Amendment doctrine
- Historical Analysis: Development of due process jurisprudence

### Comparative Law Project
- Primary Sources: Statutes/cases from multiple jurisdictions
- Comparative Analysis: How different systems handle contract formation
- Framework Mapping: Separate framework maps for each jurisdiction
- Doctrinal Analysis: Argument for convergence or divergence

### Regulatory Law Project
- Primary Sources: Statutes, agency regulations, guidance documents
- Doctrinal Analysis: How regulations apply to specific industries
- Enforcement Evidence: Pattern of agency enforcement actions
- Framework Mapping: Comprehensive guide to regulatory requirements

### Law & Economics Project
- Primary Sources: Relevant statutes and cases
- Doctrinal Analysis: Legal framework for regulation
- Economic Analysis: Efficiency implications of legal rules
- Cross-Cutting: Integration of legal and economic perspectives

---

## 6. DISTINGUISHING PRIMARY vs SUPPORTING DOCUMENTS

Within each document type, assess whether a document is PRIMARY or SUPPORTING for a given research question:

**Primary Document:**
- Extensively addresses the research question (50%+ of content)
- Contains core arguments you'll rely on
- Would be heavily cited in that section of your article
- Removing it would create a gap in your argument

**Supporting Document:**
- Partially addresses the research question
- Provides context, background, or supplementary evidence
- Useful but not essential
- Adds nuance or additional perspectives

*Note: A single document may be PRIMARY for one research question and SUPPORTING for another.*

---

## 7. WHEN IN DOUBT

**Guiding Principles:**
1. **Choose the more specific category** when uncertain
2. **Consistency matters more than perfection**—if similar documents exist, categorize similarly
3. **Document your reasoning** in notes when uncertain
4. **Primary purpose rules**—if a document does multiple things, categorize by its main purpose
5. **Flag for human review** if genuinely ambiguous

---

This guide is a living document. Update it as you discover new document types or need to refine definitions based on your project's specific needs.
```

---

## How to Customize for Your Project

**Before using these templates:**

1. **Review the folder structure** - Remove inapplicable folders (e.g., 03-Analysis-Economic if purely doctrinal)

2. **Customize jurisdiction names** - Replace generic [Jurisdiction-A] with actual jurisdictions in your project

3. **Add project-specific notes** - In the Document Type Guide, add examples from YOUR project

4. **Adjust subfolder depth** - Add or remove subfolder levels based on volume of documents

5. **Create `/00-Project-Meta/README.md`** with your specific research questions and goals

These templates should work for most legal research projects with minimal customization!