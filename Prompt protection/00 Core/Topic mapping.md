# Topic Mapping: Prompt Protection Article

*Last updated: 2025-11-12*

This document maps the main topics and themes across all research materials, identifying coverage, connections, and gaps.

---

## I. FOUNDATIONAL QUESTIONS

### 1. Why Protect Prompts? (Economic Foundation)
**Coverage:**
- **Primary:** `01 Research - Economic Foundation/Economic value of prompts.md`
- **Supporting:** Drafts v1.0-v1.1 (rationale sections)

**Key Points:**
- Market evidence: PromptBase (370k+ users, 220k+ prompts)
- Labor market: Prompt engineer salaries ($100k-$335k)
- Productivity gains: McKinsey studies (1.5-2.5x improvements)
- Investment costs: €2.3M cited in trade secrets analysis
- Conspicuous absences: No licensing markets, no litigation, no regulatory recognition

**Gaps:**
- Need update on 2025 market data
- Limited empirical data on European markets specifically
- No analysis of SME vs enterprise perspective

---

## II. INTELLECTUAL PROPERTY PROTECTION REGIMES

### 2. Copyright Protection
**Coverage:**
- **Primary:** `02 Research - IP Protection Regimes/A - Copyright/Copyright - Claude.md`
- **Supporting:** Drafts v1.0-v1.1 (copyright sections)

**Key Arguments:**
- **Against:** Prompts are instructions (ideas) not expression
- **Against:** Fail originality test (insufficient author's intellectual creation)
- **For:** Complex prompts show creativity, selection, arrangement
- **Analogies:** Technical writing, search queries, SQL commands

**Legal Framework:**
- InfoSoc Directive 2001/29/EC
- Software Directive 2009/24/EC
- Database Directive 96/9/EC
- CJEU cases: Infopaq, Painer, BSA, Cofemel

**Status:** Likely fails protection except perhaps most sophisticated prompts

---

### 3. Trade Secrets
**Coverage:**
- **Primary:** `02 Research - IP Protection Regimes/B - Trade Secrets/Trade secrets - Claude.md`
- **Supporting:** Trade secrets Perplexity.md, Trade secret Gemini.md, Edits from ChatGPT

**Key Three-Part Test (Directive 2016/943):**

#### A. Secrecy Element
- **Challenge:** Cloud AI requires disclosure to third parties
- **Distinction:** Enterprise services with NDAs vs consumer services
- **Case law:** German, Dutch, French courts on third-party disclosure
- **Outcome:** Consumer-tier prompts fail; enterprise-tier may pass

#### B. Commercial Value
- **Challenge:** Value derives from AI model, not prompt itself
- **Counter:** Marketplace evidence, development costs, competitive advantage
- **Test:** Would disclosure harm competitive position?
- **Outcome:** Sophisticated prompts may pass; simple prompts fail

#### C. Reasonable Steps
- **Challenge:** Cloud architecture inherently involves disclosure
- **Requirements:** Legal (NDAs), organizational (access controls), technical (encryption)
- **German framework:** Nine-factor proportionality test
- **Outcome:** Requires comprehensive protection program

**Counterarguments:**
- Reverse engineering from outputs (5-output reconstruction possible)
- High probability of independent discovery
- Structural impossibility of maintaining secrecy in cloud

**CJEU Guidance:**
- Case C-203/22 Dun & Bradstreet (algorithmic info can be trade secret)
- Case-by-case balancing with transparency obligations

**Status:** Limited protection possible for sophisticated prompts with rigorous measures

---

### 4. Patents & Database Rights
**Coverage:**
- Brief mentions across multiple files
- No dedicated analysis file

**Status:** Minimal viable protection pathway
- **Patents:** Abstract ideas, no technical effect
- **Database:** Single prompts don't constitute databases

**Gap:** Needs systematic treatment or can be briefly addressed in article

---

## III. CONTRACT LAW & WARRANTY FRAMEWORKS

### 5. AI Service Contracts: Performance & Disclaimers
**Coverage:**
- **Primary:** `03 Research - Contract Law & Warranties/AI Contracts Performance and Disclaimers.md`
- **Supporting:** Warranty disclaimers files (California, Ireland)

**Provider Analysis (8 major providers):**
- OpenAI, Microsoft Azure, Google (Vertex AI & Gemini), AWS (Bedrock & SageMaker)
- Anthropic, Cohere, Hugging Face, Stability AI

**Key Findings:**

#### What Providers Guarantee:
- Infrastructure availability (99.5%-99.95% uptime)
- Service accessibility (API responds)
- Narrow SLAs with service credit remedies

#### What Providers Disclaim:
- Model accuracy, completeness, reliability
- Output quality and consistency
- Fitness for particular purpose
- Merchantability
- Uninterrupted or error-free performance

**Universal Contract Patterns:**
- "As-is" provisions
- Customer responsibility for output verification
- Liability caps (6-12 months fees or $50-$100 minimum)
- Exclusion of consequential damages
- Service modification rights without notice
- Beta/preview broader disclaimers

**Critical Gap:** Availability ≠ Performance
- Model degradation doesn't breach SLA
- Hallucinations don't constitute outages

---

### 6. Warranty Law: California vs Ireland
**Coverage:**
- `03 Research - Contract Law & Warranties/Warranty disclaimers Perplexity Californian.md`
- `03 Research - Contract Law & Warranties/Warranty disclaimers Irenalnd California google.md`

**California Framework:**
- UCC §2316 (goods) vs common law (services)
- Formalistic approach: conspicuousness requirement
- Unconscionability as backstop (A & M Produce Co v FMC Corp)
- High threshold for challenging disclaimers in B2B

**Irish Framework:**
- Sale of Goods and Supply of Services Act 1980, §39-40
- Implied undertaking: due skill, care, diligence
- Fairness and reasonableness test (supplier bears burden)
- UK precedent: Last Bus Ltd v Dawsongroup (equality of bargaining power)
- No general duty of good faith (Flynn v Breccia)

**Comparative Outcome:** Both permit disclaimers but Irish law more substantive review

---

### 7. Continental European Service Conformity
**Coverage:**
- `03 Research - Contract Law & Warranties/Continental European Service Conformity Standards - Claude.md`

**Key Jurisdictions:**
- Germany: BGB §633 (work free from defects)
- France: Code civil art 1217 (conformity with contract)
- Italy: Codice civile art 1668 (manifest defects)

**Theme:** Stricter consumer protection, but B2B contracts have more flexibility

---

### 8. Guarantees in Generative AI
**Coverage:**
- `03 Research - Contract Law & Warranties/Guarantees in generative AI - google.md`

**Focus:** What constitutes adequate warranty/guarantee framework for AI outputs

---

## IV. EU LAW & CHOICE OF LAW

### 9. Good Faith as Overriding Mandatory Provision
**Coverage:**
- **Primary:** `04 Research - EU Law Frameworks/Good faith as overriding norm.md`

**Framework:** Rome I Regulation (EC) 593/2008

**Analysis:**

#### Article 9 OMPs Structure:
- Art 9(1): Definition ("crucial" public interest)
- Art 9(2): Forum OMPs always apply
- Art 9(3): Performance location OMPs (limited, discretionary)
- Deliberate restriction vs Rome Convention

#### Good Faith Across Jurisdictions:
- **Germany:** §242 BGB (Treu und Glauben) - pervasive standard
- **France:** Art 1104 Code civil - public policy principle
- **Italy:** Arts 1175, 1375 Codice civile
- **Ireland:** No general duty in commercial contracts

**Core Argument:**
Good faith does NOT qualify as OMP because:
1. Not specific "provision" but open-textured standard
2. Regulates private relationships, not public interest
3. Varies dramatically across Member States
4. Not "crucial" in uniform manner

**CJEU:** Nikiforidis (C-135/15) - restrictive interpretation of Article 9

**Outcome:** Choice of California/Irish law likely upheld; good faith cannot override

---

### 10. Legal Certainty in AI Contracts
**Coverage:**
- `04 Research - EU Law Frameworks/Certainty - Google.md`

**Theme:** Tension between AI's inherent uncertainty and legal system's need for predictability

---

## V. TECHNICAL & EMPIRICAL EVIDENCE

### 11. AI Model Performance Degradation
**Coverage:**
- **Primary:** `05 Evidence - Technical & Empirical/Definitive Proof of AI Model Performance Degradation Over Time.md`

**Key Studies:**

#### Stanford-Berkeley Study (2023):
- GPT-4 March to June 2023
- Prime number accuracy: 97.6% → 2.4%
- Code generation: 52.0% → 10.0% executable
- Instruction-following: 99.5% → 0.5%
- 3-month timeframe

#### Nature Study (2022):
- 91% of models show degradation post-deployment
- Gradual vs explosive failure patterns
- Even with minimal concept drift

#### Model Collapse Research (2024):
- Training on AI-generated data causes recursive degradation
- 1% synthetic data can trigger collapse
- Affects quality and diversity

**Legal Implications:**
- Proves non-conformity can occur
- Challenges: task-specific metrics, stochastic outputs, causal attribution
- Benchmarks don't translate to real-world performance

---

## VI. SYNTHESIS & OVERVIEWS

### 12. Integrated Analyses
**Coverage:**
- `10 Synthesis & Overviews/Full overview ChatGPT.md`
- `10 Synthesis & Overviews/Full overview Claude.md`

**Purpose:** Cross-cutting analyses integrating multiple IP regimes, contract law, and EU frameworks

---

## VII. ARTICLE DRAFTS (Evolution Tracking)

**Version History:**
- **v1.0:** Initial Claude draft (combined copyright analysis)
- **v1.1:** Full revision (comprehensive IP regimes analysis)
- **v1.2:** Second revision
- **v1.3:** Iterative update
- **v1.4:** Further update
- **v2.0:** Claude Cursor (major restructure?)
- **Working:** Codex revision

**Observable Evolution:**
- Shift from copyright-only to multi-regime analysis
- Integration of contract law alongside IP
- Addition of technical evidence
- Refinement of trade secrets analysis

---

## THEMATIC CONNECTIONS

### Connection 1: The Secrecy Paradox
**Files:** Trade secrets (all), AI contracts, Model degradation
**Theme:** Cloud AI architecture fundamentally conflicts with trade secret law's assumptions about exclusive control

### Connection 2: The Warranty Gap
**Files:** AI contracts, Warranty disclaimers (all), Continental European standards
**Theme:** SLAs cover availability not performance; model degradation proves non-conformity but contracts disclaim it

### Connection 3: The Instructions Problem
**Files:** Copyright analysis, Trade secrets, Good faith analysis
**Theme:** Prompts are instructions about what to create, not creative expression—places them outside traditional IP frameworks

### Connection 4: The Valuation Asymmetry
**Files:** Economic value, Trade secrets commercial value test, AI contracts
**Theme:** Prompts have market value (labor, productivity) but lack characteristics of protectable IP assets

### Connection 5: The Choice of Law Strategy
**Files:** Good faith as OMP, Warranty disclaimers (CA/Ireland), AI contracts
**Theme:** Provider selection of CA/Ireland law exploits favorable disclaimer regimes; Rome I limits EU good faith override

---

## GAPS & NEEDED ANALYSIS

### 1. European-Specific Empirics
- Most economic data is US-focused
- Need EU market analysis, prompt marketplaces in Europe
- European case law on AI contracts

### 2. AI Act Integration
- Article mentions AI Act but limited analysis
- Transparency obligations vs trade secret protection
- High-risk AI systems classification

### 3. GDPR Intersection
- Data protection vs trade secrets
- Dun & Bradstreet case touched on this
- Transparency rights (Art 13-15) vs commercial confidentiality

### 4. Patent/Database Rights
- Brief mentions only
- Either expand or explicitly limit scope

### 5. Comparative Analysis
- Could strengthen with German/French case law on service contracts
- BGB §633, Code civil analysis

### 6. Practical Recommendations
- What should businesses actually do?
- Model contract clauses?
- Best practices for protection?

---

## ARTICLE SCOPE DECISION POINTS

Based on topic mapping, you need to decide:

### Option A: IP Protection Focus (Current Draft Direction)
- Center on IP regimes (copyright, trade secrets, briefly patents/database)
- Contract law as secondary/contextual
- Target: IP specialists, 8-10k words

### Option B: Comprehensive AI Legal Framework
- IP protection + contract law + EU regulatory frameworks
- Risk: Too broad for 10-12k word limit
- Target: Broader AI law audience

### Option C: Trade Secrets Specialization
- Deep dive on trade secrets only
- Most mature analysis in your materials
- Clear tensions with cloud architecture
- Target: Trade secret specialists, 8-10k words

### Recommended: Modified Option A
- **Part I:** Economic foundation (why protect prompts)
- **Part II:** Copyright protection (likely fails)
- **Part III:** Trade secrets (limited protection possible)
- **Part IV:** Contract law implications (warranty disclaimers in AI services)
- **Part V:** EU law frameworks (choice of law, good faith)
- **Conclusion:** Recommendations and gaps

---

## NEXT STEP: OUTLINE CREATION

With topic mapping complete, ready to create detailed article outline for IIC publication.
