# CJEU Case Table: Research Question Relevance Map

**Project:** Automated Decision-Making in Administrative Public Participation
**Created:** 2025-11-22
**Purpose:** Map CJEU case law to research questions with relevance assessments

---

## Case Inventory

| Case Name | Citation | Date | Project File |
|-----------|----------|------|--------------|
| OQ v SCHUFA Holding AG | C-634/21, ECLI:EU:C:2023:957 | 7 Dec 2023 | [[C-634-21 OQ v SCHUFA Holding AG]] |
| AG Pikamäe Opinion (SCHUFA) | C-634/21, ECLI:EU:C:2023:220 | 16 March 2023 | [[C-634-21 SCHUFA Advocate General Opinion]] |
| CK v Magistrat der Stadt Wien (Dun & Bradstreet Austria) | C-203/22, ECLI:EU:C:2025:131 | 27 Feb 2025 | [[C-203-22 CK v Magistrat der Stadt Wien]] |
| OT v Vyriausioji tarnybinės etikos komisija | C-184/20, ECLI:EU:C:2022:601 | 1 Aug 2022 | [[C-184-20 OT v Vyriausioji tarnybines etikos komisija]] |

---

## Case Summaries

### 1. C-634/21: OQ v SCHUFA Holding AG (SCHUFA Judgment)

**File:** `/01-Primary-Sources/Case-Law/CJEU/C-634-21 OQ v SCHUFA Holding AG.md`
**Type:** CJEU Preliminary Ruling (First Chamber)
**Decision Date:** 7 December 2023

**Short Summary:**
Landmark ruling on Article 22 GDPR scope. A credit scoring agency (SCHUFA) generated automated probability values that banks used to make credit decisions. The Court held that establishing such probability values constitutes "automated individual decision-making" under Article 22(1) when third parties "draw strongly on" that value to make their own decisions. Key holding: **preparatory acts can be Article 22 "decisions"** if they play a "determining role" in downstream outcomes. Introduced the quantitative benchmark (~80% correlation) for assessing determinative influence.

**Key Paragraphs:**
- ¶46: Broad interpretation of "decision"
- ¶50: "Determining role" test established
- ¶¶56-65: Third-party reliance triggers Article 22 for score provider
- ¶¶61-63: Anti-circumvention principle (preventing "lacuna in legal protection")
- ¶73: Quantitative threshold (~80% correlation between insufficient score and denial)

---

### 2. C-634/21: AG Pikamäe Opinion (SCHUFA)

**File:** `/01-Primary-Sources/Case-Law/CJEU/C-634-21 SCHUFA Advocate General Opinion.md`
**Type:** Advocate General Opinion
**Opinion Date:** 16 March 2023

**Short Summary:**
AG Pikamäe provided the analytical foundation adopted by the Court. Advocated for broad interpretation of "decision" under Article 22(1), reasoning that narrow interpretation would create circumvention loopholes. Distinguished between automated outputs that merely affect data subjects and those that constitute decisions. Emphasized purposive interpretation protecting individuals from risks of solely automated processing.

**Key Paragraphs:**
- ¶83: "Concept of 'decision' must be construed broadly"
- ¶89: "Not every automated processing producing an output which may affect a data subject constitutes a 'decision'" (limits to broad interpretation)

---

### 3. C-203/22: CK v Magistrat der Stadt Wien (Dun & Bradstreet Austria)

**File:** `/01-Primary-Sources/Case-Law/CJEU/C-203-22 CK v Magistrat der Stadt Wien.md`
**Type:** CJEU Preliminary Ruling (First Chamber)
**Decision Date:** 27 February 2025

**Short Summary:**
Critical ruling on the right to explanation under Article 15(1)(h) GDPR. A data subject (CK) was refused a mobile phone contract based on Dun & Bradstreet Austria's automated creditworthiness assessment. The Court held that "meaningful information about the logic involved" requires the controller to explain, **by means of relevant information and in a concise, transparent, intelligible and easily accessible form**, the **procedure and principles actually applied** in automated decision-making. Neither complex mathematical formulas nor full algorithm disclosure satisfies this requirement—explanations must enable data subjects to understand which personal data were used and how. Trade secrets cannot defeat disclosure to DPA/courts for balancing.

**Key Paragraphs:**
- ¶¶47-52: "Meaningful information about the logic" requires explanation of "procedure and principles actually applied"
- ¶50: Information must be individual-specific, not generic algorithm descriptions
- ¶¶51-52: Information must be comprehensible to ordinary person and sufficient for effective challenge
- ¶57: Genuine "right to explanation" recognized
- ¶¶74-76: Trade secrets must be balanced; cannot categorically exclude disclosure

---

### 4. C-184/20: OT v Vyriausioji tarnybinės etikos komisija

**File:** `/01-Primary-Sources/Case-Law/CJEU/C-184-20 OT v Vyriausioji tarnybines etikos komisija.md`
**Type:** CJEU Preliminary Ruling (Grand Chamber)
**Decision Date:** 1 August 2022

**Short Summary:**
Lithuanian case on public disclosure of officials' private interest declarations. While not directly addressing automated decision-making, the Court addressed data protection proportionality principles relevant to administrative processing. The Court held that online publication of personal data in interest declarations is lawful only if proportionate to legitimate anti-corruption objectives. Established that publication of spouse/family member data goes beyond what is strictly necessary. Key for **balancing transparency objectives against data protection rights** in administrative contexts and **proportionality analysis** for processing special categories of data.

**Key Holdings:**
- National legislation must meet an objective of public interest and be proportionate
- Lack of administrative resources cannot justify interference with fundamental rights
- Data minimisation principle requires processing limited to what is strictly necessary
- Processing revealing sensitive data indirectly (e.g., sexual orientation) is still special category processing

---

## Research Question Relevance Matrix

| Case | RQ1: Automated Decision Threshold | RQ2: Transparency & Accountability | RQ3: Data Subject Rights* | RQ4: Legal Effects & Significance | RQ5: Comparative Administrative Law |
|------|:---------------------------------:|:----------------------------------:|:------------------------:|:---------------------------------:|:-----------------------------------:|
| **SCHUFA Judgment (C-634/21)** | **HIGH** | MEDIUM | — | **HIGH** | MEDIUM |
| **AG Pikamäe Opinion (C-634/21)** | **HIGH** | LOW | — | MEDIUM | LOW |
| **Dun & Bradstreet (C-203/22)** | MEDIUM | **HIGH** | — | MEDIUM | MEDIUM |
| **OT v Vyriausioji (C-184/20)** | LOW | LOW | — | LOW | LOW |

*RQ3 extraction currently skipped per project plan.

---

## Detailed RQ Relevance Analysis

### RQ1: Automated Decision Threshold

**Does algorithmic filtering constitute a "decision based solely on automated processing" under GDPR Article 22?**

| Case | Relevance | Key Contributions |
|------|-----------|-------------------|
| **SCHUFA Judgment** | **HIGH** | (1) "Determining role" test at ¶50; (2) Preparatory acts can be Article 22 decisions; (3) ~80% correlation threshold at ¶73; (4) Anti-circumvention principle at ¶¶61-63 preventing multi-stage evasion; (5) Broad interpretation of "decision" at ¶46 |
| **AG Pikamäe Opinion** | **HIGH** | (1) Supports broad interpretation at ¶83; (2) Establishes outer limits at ¶89—not every automated output is a decision; (3) Purposive interpretation framework |
| **Dun & Bradstreet** | MEDIUM | (1) Post-SCHUFA confirmation of broad approach; (2) Links transparency to effective Article 22 rights exercise at ¶55 |
| **OT v Vyriausioji** | LOW | Tangential—addresses data processing but not Article 22 specifically |

**RQ1 Citation Priorities:**
1. SCHUFA ¶50, ¶73 (determining role test, threshold)
2. SCHUFA ¶¶61-63 (anti-circumvention)
3. AG Opinion ¶83, ¶89 (broad interpretation with limits)

---

### RQ2: Transparency & Accountability Mechanisms

**What transparency and accountability mechanisms apply to algorithmic filtering in administrative processes?**

| Case | Relevance | Key Contributions |
|------|-----------|-------------------|
| **Dun & Bradstreet** | **HIGH** | (1) "Meaningful information about the logic" standard at ¶¶47-52; (2) Must explain "procedure and principles actually applied"; (3) Individual-specific not generic at ¶50; (4) Comprehensibility standard at ¶¶51-52; (5) Right to explanation recognized at ¶57; (6) Trade secrets balanced at ¶¶74-76 |
| **SCHUFA Judgment** | MEDIUM | (1) Establishes what triggers transparency obligations under Article 22; (2) References Articles 13-15 GDPR information requirements |
| **AG Pikamäe Opinion** | LOW | Limited direct transparency analysis |
| **OT v Vyriausioji** | LOW | Transparency in different context (public disclosure vs. individual explanation) |

**RQ2 Citation Priorities:**
1. Dun & Bradstreet ¶57, ¶¶47-52 (right to explanation, standards)
2. Dun & Bradstreet ¶¶74-76 (trade secrets balancing)
3. SCHUFA ¶¶56-57 (Articles 13-15 obligations triggered)

---

### RQ4: Legal Effects and Significance

**What constitutes "legal effects" or "similarly significant effects" for consultation exclusion?**

| Case | Relevance | Key Contributions |
|------|-----------|-------------------|
| **SCHUFA Judgment** | **HIGH** | (1) Effects analysis at ¶¶56-60: must "significantly affect circumstances, behaviour or choices" or "produce legal effects"; (2) Probabilistic causation standard at ¶73 (~80% correlation); (3) Broad effects interpretation at ¶¶57-62: credit scores affect data subjects "at the very least significantly" |
| **Dun & Bradstreet** | MEDIUM | (1) Connects effects to right to challenge at ¶55; (2) Information must enable effective exercise of rights |
| **AG Pikamäe Opinion** | MEDIUM | Supports broad effects analysis from SCHUFA |
| **OT v Vyriausioji** | LOW | Proportionality framework, but different effects context |

**RQ4 Citation Priorities:**
1. SCHUFA ¶¶56-60 (effects standard)
2. SCHUFA ¶73 (probabilistic causation/~80% threshold)
3. SCHUFA ¶¶57-62 ("at the very least significantly")

---

### RQ5: Comparative Administrative Law Approaches

**How do different EU Member States regulate automated processing in administrative decision-making?**

| Case | Relevance | Key Contributions |
|------|-----------|-------------------|
| **SCHUFA Judgment** | MEDIUM | (1) German national law context (BDSG § 31); (2) Reference to whether national law satisfies Article 22(2)(b) requirements at ¶¶71-72; (3) Framework for assessing national legal bases |
| **Dun & Bradstreet** | MEDIUM | (1) Austrian DSG § 4(6) analysis at ¶75; (2) Held national law cannot categorically exclude access based on trade secrets; (3) Model for evaluating national implementation |
| **OT v Vyriausioji** | LOW | Lithuanian context, but limited ADM relevance |
| **AG Pikamäe Opinion** | LOW | No significant comparative content |

**RQ5 Citation Priorities:**
1. SCHUFA ¶¶71-72 (German national law assessment)
2. Dun & Bradstreet ¶75 (Austrian implementation struck down)

---

## Cross-Case Doctrinal Themes

### Theme 1: Anti-Circumvention Principle
- **Primary source:** SCHUFA ¶¶61-63
- **Principle:** Narrow interpretation of "decision" would create "lacuna in legal protection"
- **Application:** Multi-stage processing cannot evade Article 22 by inserting nominal human intermediary
- **Relevance:** RQ1 (core), RQ4 (effects in chain)

### Theme 2: Probabilistic Causation Standard
- **Primary source:** SCHUFA ¶73
- **Principle:** When automated output leads to adverse outcome "in almost all cases" (~80%), it "plays a determining role"
- **Application:** Threshold for preparatory acts becoming Article 22 decisions
- **Relevance:** RQ1 (threshold), RQ4 (effects measurement)

### Theme 3: Substantive Explanation Requirement
- **Primary source:** Dun & Bradstreet ¶¶47-52, ¶57
- **Principle:** "Meaningful information about the logic" requires explanation of procedure and principles actually applied, individual-specific and comprehensible
- **Application:** Neither algorithm disclosure nor generic descriptions suffice
- **Relevance:** RQ2 (core)

### Theme 4: Proportionality in Administrative Processing
- **Primary source:** OT v Vyriausioji (entire judgment)
- **Secondary:** SCHUFA ¶¶68-70 (Article 6 requirements)
- **Principle:** Processing must be proportionate to legitimate aim; data minimisation applies
- **Application:** Administrative efficiency cannot justify disproportionate interference
- **Relevance:** RQ4 (effects proportionality), RQ5 (national implementation standards)

---

## Official Links

| Case | CURIA | EUR-Lex |
|------|-------|---------|
| SCHUFA Judgment C-634/21 | [CURIA](https://curia.europa.eu/juris/document/document.jsf?docid=282187&doclang=EN) | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0634) |
| AG Opinion C-634/21 | [CURIA](https://curia.europa.eu/juris/document/document.jsf?docid=271443&doclang=EN) | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CC0634) |
| Dun & Bradstreet C-203/22 | [CURIA](https://curia.europa.eu/juris/document/document.jsf?docid=295841&doclang=EN) | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62022CJ0203) |
| OT v Vyriausioji C-184/20 | [CURIA](https://curia.europa.eu/juris/document/document.jsf?docid=263721&doclang=EN) | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62020CJ0184) |

---

## Usage Notes

- **For RQ1 analysis:** Start with SCHUFA ¶50 (determining role test), then ¶73 (threshold), then ¶¶61-63 (anti-circumvention)
- **For RQ2 analysis:** Start with Dun & Bradstreet ¶57 (right to explanation), then ¶¶47-52 (standards)
- **For RQ4 analysis:** Start with SCHUFA ¶¶56-60 (effects), then ¶73 (probabilistic causation)
- **For comparative work:** Use SCHUFA German context and Dun & Bradstreet Austrian context as models

---

*Last updated: 2025-11-22*
