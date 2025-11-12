# Legal Protection for AI Prompts in the European Union: An Analysis of Intellectual Property and Contract Law Frameworks

**Article Outline for IIC Journal**

*Target: 10,000-12,000 words | OSCOLA citations*

---

## I. INTRODUCTION [1,200 words]

### A. The Prompt Protection Problem
- **Opening vignette:** Three scenarios illustrating the prompt protection dilemma
  - Legal analytics firm: €2.3M prompt engineering investment, daily cloud API use
  - Pharmaceutical company: 60% faster drug candidate identification, consumer ChatGPT usage
  - Automotive manufacturer: Proprietary system prompts, encrypted storage, but third-party processing
- **Research question:** Do EU legal frameworks provide meaningful protection for AI prompts?
- **Significance:** Commercial prompt markets (370k+ users, 220k+ prompts), professional prompt engineering salaries ($100k-$335k), productivity gains (1.5-2.5x improvements)

### B. Methodology and Scope
- **Approach:** Doctrinal analysis of EU IP law, contract law, and choice of law frameworks
- **Materials analyzed:** Directive 2016/943 (trade secrets), InfoSoc Directive, CJEU case law, major AI provider contracts
- **Geographical scope:** EU law focus with comparative analysis of California/Irish law (chosen governing law in major contracts)
- **Limitations:** Focus on B2B contexts; consumer protection separately analyzed

### C. Roadmap
- Part II: Economic foundation establishing protection rationale
- Part III: Copyright protection analysis
- Part IV: Trade secrets protection analysis
- Part V: Contract law and warranty frameworks
- Part VI: EU choice of law and mandatory provisions
- Part VII: Conclusions and recommendations

---

## II. THE ECONOMIC CASE FOR PROMPT PROTECTION [1,500 words]

### A. Market Evidence of Commercial Value

#### 1. Prompt Marketplaces
- **PromptBase:** 370,000+ users, 220,000+ prompts, €1.99-€4.99 price points
- **Other platforms:** ChatX (39 CAD per prompt), PromptHero, PromptScoop
- **Analysis:** Functioning markets demonstrate non-trivial economic value
- **Limitation:** Low unit prices suggest commodification pressure

#### 2. Labor Market Valuation
- **Salary data:** $100k-$200k typical range (US data)
- **Outliers:** Anthropic $335k "Prompt Engineer and Librarian" (San Francisco)
- **Interpretation:** Values human skill, not prompt outputs as IP assets
- **Distinction:** Labor capital vs. intellectual property

#### 3. Productivity Measurements
- **McKinsey studies:** 1.5-2.5x faster task completion with effective prompts
- **Software development:** 56% faster (GitHub Copilot study)
- **Economic impact:** $2.6-4.4 trillion annual potential (generative AI overall)
- **Attribution challenge:** Productivity gains reflect AI + prompts, not prompts alone

### B. Investment and Skill Acquisition
- **Non-intuitive skill:** Empirical research (Oppenlaender) shows prompt engineering must be learned
- **Investment forms:** Iterative testing costs, technical knowledge acquisition, formal training (€500-€2,000 courses)
- **Time horizon:** Weeks to months for sophisticated prompt development

### C. Appropriability and Free-Riding Concerns
- **Zero marginal cost copying:** Pure information goods
- **Disclosure destroys advantage:** Temporal asymmetry between investment and returns
- **Reverse engineering risk:** 5-output reconstruction techniques documented
- **Trade secret limitations:** Difficult to maintain secrecy in customer-facing applications

### D. Conspicuous Absences in Economic Evidence
- **No licensing markets:** Despite 3+ years of commercial AI adoption
- **No acquisition transactions:** Prompt libraries not valued in M&A
- **No litigation:** Zero reported cases of prompt misappropriation
- **No regulatory recognition:** EU AI Act silent on prompt IP
- **Interpretation:** Market participants don't treat prompts as high-value IP assets

### E. Economic Foundation Synthesis
- **Conclusion:** Evidence supports protection consideration but reveals significant limitations
- **Distinction:** Simple prompts (minimal investment) vs. sophisticated prompts (substantial investment)
- **Transition:** Does EU legal framework accommodate this intermediate category?

---

## III. COPYRIGHT PROTECTION: THE INSTRUCTIONS PROBLEM [2,000 words]

### A. Legal Framework: EU Copyright Harmonization

#### 1. Originality Standard
- **InfoSoc Directive 2001/29/EC:** Harmonized originality test
- **CJEU case law:** *Infopaq* (author's intellectual creation), *Painer* (creative choices), *Cofemel* (expression of free creative choices)
- **Standard:** Work must reflect author's personality through free and creative choices
- **Threshold:** Low but not absent; sufficient creative freedom required

#### 2. Idea-Expression Dichotomy
- **Principle:** Copyright protects expression, not ideas
- **CJEU:** *BSA* (functionality vs. creativity), *SAS Institute* (programming language principles unprotectable)
- **Application:** Instructions about what to create vs. creative expression itself

### B. Applying Copyright to Prompts

#### 1. The Instructions Argument (Against Protection)
- **Nature of prompts:** Commands describing desired outputs
- **Analogies:** Search queries, SQL commands, programming specifications
- **Doctrinal barrier:** Prompts constitute ideas (what to create) not expression (creative work)
- **Example:** "Write a formal business letter declining a job offer" = instruction, not expression

#### 2. The Creativity Argument (For Protection)
- **Complex prompts:** 400-word system prompts with tone specifications, vocabulary constraints, rhetorical strategies
- **Creative choices:** Selection of precise vocabulary, sequencing of instructions, parameter calibration
- **Analogies:** Technical writing receives copyright despite functional purpose
- **DLA Piper view:** Sophisticated prompts "can be traced back to creativity and personality of author"

#### 3. Selection and Arrangement
- **Compilation theory:** Individual elements public but arrangement protected
- **Database Directive 96/9/EC:** Selection/arrangement of contents may be protected
- **Application to prompts:** Individual techniques known but specific configuration novel?
- **Limitation:** Single prompts typically too minimal for compilation protection

### C. Case Analysis: Simple vs. Sophisticated Prompts

#### 1. Simple Prompts [Unprotectable]
- **Examples:** "Summarize," "Translate to French," "Create image of cat"
- **Analysis:** Minimal creative choices, obvious word selection, functional necessity
- **Outcome:** Below originality threshold

#### 2. Intermediate Prompts [Ambiguous]
- **Examples:** Domain-specific templates, tested formulations improving reliability
- **Analysis:** Some selection/arrangement but limited creative freedom
- **Challenge:** High independent discovery probability

#### 3. Sophisticated Prompts [Potentially Protectable]
- **Examples:** Multi-paragraph system prompts with examples, strategic keyword sequencing, parameter specifications
- **Analysis:** Reflects personality through vocabulary selection, structure, creative judgment
- **Limitation:** Still primarily instructional; expression serves functional purpose

### D. Software and Database Protections

#### 1. Software Directive 2009/24/EC
- **Scope:** Protects computer programs "in any form"
- **Argument:** Prompts function as instructions to AI systems
- **Counterargument:** Prompts are data inputs, not programs; lack algorithmic structure
- **Outcome:** Unlikely to qualify as "software"

#### 2. Database Directive 96/9/EC
- **Sui generis right:** Substantial investment in obtaining, verifying, presenting contents
- **Argument:** Prompt libraries constitute databases
- **Limitation:** Individual prompts don't constitute databases; collections might qualify but protection extends only to extraction/reuse

### E. Copyright Synthesis
- **Conclusion:** Most prompts fail originality test as primarily instructional
- **Exception:** Highly sophisticated prompts with substantial creative elaboration might qualify, but functional nature remains obstacle
- **Primary barrier:** Idea-expression dichotomy places instructions outside copyright's core domain
- **Transition:** If copyright fails, can trade secret law provide protection?

---

## IV. TRADE SECRETS: THE CLOUD DISCLOSURE PARADOX [3,000 words]

### A. Legal Framework: Directive 2016/943

#### 1. Three-Part Cumulative Test
- **Article 2(1):** Information must meet all three requirements
  - (a) Secret (not generally known or readily accessible)
  - (b) Commercial value because secret
  - (c) Reasonable steps to keep secret
- **Legislative history:** TRIPS Art 39 implementation, harmonization across Member States
- **Structure:** Failure of any single element defeats protection entirely

#### 2. Policy Objectives
- **Recital 14:** Homogenous definition, legitimate interest in confidentiality
- **Article 3:** Lawful acquisition includes independent discovery, reverse engineering, observation
- **Balance:** Protection vs. mobility, innovation, competition

### B. The Secrecy Element: Cloud Architecture as Disclosure

#### 1. Third-Party Disclosure Problem
- **Technical reality:** Cloud AI requires transmitting prompts to provider servers
- **Doctrinal issue:** Information disclosed to third parties "readily accessible" to recipients?
- **Key distinction:** Enterprise services with NDAs vs. consumer services without

#### 2. National Court Guidance on Third-Party Disclosure
- **German courts (Geschäftsgeheimnisgesetz):** Executed confidential disclosure agreements essential
- **Dutch case law:** District Court Middle Netherlands (2018) - technical drawings shared without NDAs failed as trade secrets
- **French courts:** Paris Court of Appeal (2022) - third-party sharing without NDAs defeats reasonable steps
- **Synthesis:** Contractual confidentiality protections can preserve secrecy despite disclosure

#### 3. Application to AI Prompts
- **Consumer-tier services:** OpenAI free ChatGPT, Google Gemini free tier use prompts for training
  - **Terms explicitly permit:** Data used for model improvement, human review
  - **Outcome:** Disclosure without confidentiality protection defeats secrecy
- **Enterprise-tier services:** Azure OpenAI, AWS Bedrock, Anthropic enterprise plans
  - **Contractual protections:** No training use, no disclosure to third parties, deletion upon request
  - **Outcome:** May preserve secrecy if robustly implemented
- **Bright-line rule:** Only prompts used through enterprise services with contractual confidentiality protections can potentially satisfy secrecy element

### C. The Commercial Value Element: Model Dependency

#### 1. The Dependency Challenge
- **Observation:** Prompts derive utility from underlying AI models
- **Example:** GPT-4 prompt worthless without OpenAI model access
- **Question:** Does value derive from prompt itself or from model access?
- **Doctrinal requirement:** Value must derive *because* information is secret

#### 2. Arguments Against Independent Value
- **Model access determinative:** Same prompt on different models produces different results
- **High independent discovery:** Low barriers to prompt engineering
- **German case law:** Higher Regional Court Düsseldorf (2021) - if unauthorized use saves time but disclosure doesn't harm competitive position, commercial value element may fail

#### 3. Arguments For Independent Value
- **Marketplace evidence:** PromptBase demonstrates market recognition of prompts as valuable
- **Quantified benefits:** 60% faster drug candidate identification = measurable economic worth
- **Investment costs:** €2.3M spent on prompt engineering represents substantial value
- **Compilation analogy:** Customer lists - individual contacts public but curated compilation protected
- **Distinction:** Simple prompts (trivial independent discovery) vs. sophisticated prompts (substantial optimization investment)

#### 4. Commercial Value Synthesis
- **Test:** Would disclosure harm holder's competitive advantage?
- **Application:** Prompts codifying novel applications, non-obvious combinations, substantial optimization satisfy test
- **Outcome:** Sophisticated prompts representing genuine investment can meet commercial value requirement

### D. The Reasonable Steps Element: Structural Tension with Cloud

#### 1. National Frameworks for "Reasonable Steps"

##### Germany (Geschäftsgeheimnisgesetz):
- **Three-level framework:**
  - Legal: NDAs, employment provisions, contractual restrictions
  - Organizational: Access controls, need-to-know policies, employee training
  - Technical: Encryption, authentication, monitoring
- **Nine-factor proportionality test:** Value, development costs, company size, type of information, circumstances of use
- **Key principle:** Measures must be proportionate to information value

##### France (Code de Commerce):
- **Specific identification required:** Generic "all confidential" clauses insufficient
- **Documented measures:** Must implement and enforce, not merely adopt policies
- **Procedural protections:** Courts require specific marking, targeted restrictions

##### Netherlands:
- **Stringent practice requirement:** "Policy without practice fails"
- **Dutch courts:** Actual implementation essential, stated policies insufficient

#### 2. Applying Reasonable Steps to Cloud AI Prompts

##### The Structural Challenge:
- **Trade secret law assumption:** Holders maintain exclusive physical/digital control
- **Cloud AI reality:** Information must be disclosed to function
- **Historical examples:** Formula in locked vault, customer list on secured server, source code with access controls
- **Prompts differ:** Cannot function without transmission to third party

##### Comprehensive Protection Framework Required:
- **Legal layer:**
  - Exclusive use of enterprise AI services with documented contractual confidentiality
  - Internal NDAs with employees accessing prompts
  - Contractor agreements with IP assignment clauses
- **Organizational layer:**
  - Access controls limiting who can create/submit prompts
  - Classification systems identifying which prompts contain trade secrets
  - Employee training on proper AI service use
  - Monitoring compliance (audit logs, usage reviews)
  - Incident response plans
- **Technical layer:**
  - Encryption in transit and at rest
  - Prompt sanitization procedures (remove unnecessary sensitive info before submission)
  - Separate enterprise vs. non-enterprise tool usage
  - Authentication and authorization systems

#### 3. Proportionality Analysis Under German Framework
- **Factor: Specific circumstances of use:** Technical necessity of third-party processing
- **Factor: Value and development costs:** Documented €2.3M investment justifies substantial measures
- **Conclusion:** If use necessarily requires third-party involvement, reasonable steps must be assessed relative to that constraint
- **Outcome:** Contractual protections + internal controls can satisfy reasonable steps despite third-party disclosure

### E. Counterarguments: Why Trade Secret Protection Likely Fails

#### 1. Reverse Engineering from Outputs
- **Technical research:** 5-output reconstruction techniques (2024 studies)
- **Lawful acquisition:** Article 3(1)(b) explicitly permits reverse engineering
- **Implication:** If prompts readily reconstructible from publicly available outputs, information "readily accessible"

#### 2. Structural Impossibility Argument
- **Core tension:** Trade secrets assume exclusive control; cloud AI requires disclosure
- **Third-party risks:** Provider security breaches, employee misconduct, regulatory disclosure obligations
- **Distinction from other outsourcing:** Payroll processors don't *require* sensitive data; AI models *require* actual prompts
- **Conclusion:** Cloud architecture fundamentally incompatible with trade secret confidentiality expectations

#### 3. Independent Discovery Probability
- **Low barriers:** No specialized equipment, no capital investment, no rare expertise
- **Article 3(1)(a):** Independent discovery explicitly lawful
- **Durability question:** If competitors converge on similar solutions within months, value doesn't truly derive from secrecy

### F. CJEU Guidance: Dun & Bradstreet

#### 1. Case Background (C-203/22, 27 February 2025)
- **Issue:** GDPR transparency vs. trade secret protection for algorithmic decision-making
- **Holding:** Controllers must provide "meaningful information about logic" but need not disclose algorithm itself
- **Balance:** Trade secret protection can justify withholding from data subjects, not from supervisory authorities/courts

#### 2. Implications for AI Prompts
- **Principle:** Algorithmic instructions (including prompts) can in principle qualify as trade secrets
- **Limitation:** Protection not absolute; must yield to transparency obligations where proportionality requires
- **Framework:** Case-by-case balancing rather than categorical rules
- **Nuance:** Distinguishes simple vs. sophisticated prompts based on investment and competitive advantage

### G. Trade Secrets Synthesis

#### 1. The Resolution: Limited Conditional Protection
- **Category 1 - Simple prompts:** Categorically fail all three elements
  - Generally known within professional circles
  - Lack commercial value (trivial independent discovery)
  - Cannot justify substantial protective measures
- **Category 2 - Intermediate prompts:** Ambiguous; likely fail proportionality
  - May have modest value
  - High independent discovery probability undermines "because secret" requirement
  - Investment in protection exceeds value
- **Category 3 - Sophisticated prompts:** Can potentially qualify IF:
  - Used exclusively through enterprise AI services with contractual confidentiality
  - Subject to comprehensive legal + organizational + technical protection measures
  - Represent substantial documented investment
  - Provide quantified competitive advantages

#### 2. Unresolved Tensions
- **No CJEU interpretation:** Directive 2016/943 entered force 2016; no preliminary ruling on core definitional questions
- **Cross-border uncertainty:** German proportionality vs. Dutch stringent practice vs. French procedural requirements
- **AI Act intersection:** Transparency obligations incompletely theorized with trade secret protection
- **Conclusion:** Protection theoretically possible but demanding in practice, provisional pending judicial clarification

---

## V. CONTRACT LAW: THE AVAILABILITY-PERFORMANCE GAP [2,000 words]

### A. AI Service Contract Architecture

#### 1. Universal Contractual Structure
- **SLAs cover:** Infrastructure availability (99.5%-99.95% uptime)
- **SLAs exclude:** Model accuracy, output quality, performance consistency
- **Remedies:** Service credits (10%-100% of monthly fees)
- **Sole remedy clauses:** Credits constitute exclusive contractual remedy

#### 2. Comprehensive Warranty Disclaimers
- **"As-is" provisions:** Services provided without warranties
- **Merchantability disclaimed:** Explicitly excluded across all major providers
- **Fitness for purpose disclaimed:** No guarantee services suit customer's specific needs
- **Accuracy disclaimers:** OpenAI, Anthropic, Google, AWS, Stability AI all disclaim accuracy, completeness, error-free operation

#### 3. Liability Limitations
- **Caps:** 6-12 months of fees paid, or $50-$100 minimum
- **Excluded damages:** Consequential, incidental, special, indirect damages (lost profits, business interruption, data loss)
- **Example scenario:** $1M business losses from model degradation; maximum recovery: $10k service credit (if uptime SLA breached)

### B. The Availability ≠ Performance Problem

#### 1. Technical Evidence: Model Degradation Over Time
- **Stanford-Berkeley study (2023):** GPT-4 March-June 2023
  - Prime number accuracy: 97.6% → 2.4% (3 months)
  - Code generation: 52% → 10% executable
  - Instruction-following: 99.5% → 0.5%
- **Nature study (2022):** 91% of ML models show post-deployment degradation
- **Model collapse research (2024):** Training on AI-generated data causes recursive degradation

#### 2. The Contractual Gap
- **Model degradation doesn't breach SLA:** API remains reachable, responses returned (incorrectly)
- **Hallucinations not service failures:** Confidently stated fabrications are disclaimed as customer's responsibility to verify
- **Model updates preserve availability:** Swapping models changes behavior but doesn't breach uptime guarantees

#### 3. Provider Rights to Modify/Discontinue
- **Microsoft:** "Commercially reasonable changes" permitted
- **Stability AI:** Modify/discontinue "with or without notice"
- **Cohere:** "Regularly retire old models"; customer applications must migrate or fail
- **Google Vertex AI:** 6 months' notice to discontinue, or *no notice* if "materially similar functionality" provided (provider determines similarity)

### C. Legal Analysis Under California and Irish Law

#### 1. California Law Framework

##### Goods vs. Services Classification:
- **Predominant factor test:** Essence of transaction determines UCC applicability
- **AI services:** Likely classified as services (no tangible goods transferred)
- **Consequence:** Common law governs, not UCC detailed warranty provisions

##### Warranty Disclaimer Validity:
- **UCC § 2316 (if goods):** Conspicuousness requirement, must mention "merchantability"
- **Common law (services):** Clear and unambiguous language required
- **Unconscionability doctrine (Cal Civ Code § 1670.5):** Procedural + substantive elements, sliding scale
- **A & M Produce Co v FMC Corp:** B2B disclaimer unconscionable where:
  - Disparity in technical expertise
  - Fine print, no negotiation
  - Disclaimer shifts entire risk + excludes consequential damages = worthless remedy

##### Application to AI Contracts:
- **Procedural unconscionability:** Arguable - standard forms, no negotiation, technical complexity
- **Substantive unconscionability:** Stronger - disclaims core performance characteristics customer needs, remedy caps inadequate for business losses
- **Limitation:** California courts rarely find B2B contracts unconscionable; high bar

#### 2. Irish Law Framework

##### Statutory Implied Undertakings:
- **Sale of Goods and Supply of Services Act 1980, § 39:**
  - (a) Supplier has necessary skill
  - (b) Service provided with due skill, care, diligence
  - (c) Materials sound and reasonably fit for purpose
  - (d) Goods of merchantable quality

##### Fairness and Reasonableness Test (§ 40):
- **Burden on supplier:** Must prove exclusion fair and reasonable
- **Schedule criteria:**
  - Strength of bargaining positions
  - Inducement to agree or alternative options
  - Customer knowledge of term
  - Practicability of compliance
- **UK precedent (highly persuasive):** *Last Bus Ltd v Dawsongroup* (2023) - blanket exclusion "at least arguably unreasonable" where no materially different terms available in market

##### Application to AI Contracts:
- **Undertaking (b):** Due skill, care, diligence arguably breached by model degradation if no advance warning
- **Fairness assessment:**
  - Against supplier: Standard forms, no alternatives (all major providers use similar disclaimers), technical complexity
  - For supplier: Sophisticated commercial parties, could negotiate enterprise terms
- **No general good faith duty:** *Flynn v Breccia* [2017] IECA 74 rejected overarching good faith in Irish commercial contracts

### D. Enterprise vs. Consumer Tier Differences

#### 1. Data Protection Distinctions
- **Consumer tiers:** Inputs used for training (Google, OpenAI free tiers)
- **Enterprise tiers:** No training use, 30-day deletion, opt-out flags (Cohere)
- **Implication:** Consumer-tier use destroys trade secret status

#### 2. Support and Notice
- **Enterprise:** Dedicated account teams, advance deprecation notice (sometimes)
- **Consumer:** No SLA, no support guarantees, changes without notice

#### 3. Negotiation Possibilities
- **Standard terms:** Take-it-or-leave-it, comprehensive disclaimers
- **Custom enterprise agreements:** May secure model version locks, enhanced SLAs, performance baselines
- **Reality:** Only largest customers have leverage to negotiate material changes

### E. Contract Law Synthesis
- **The gap:** Providers guarantee infrastructure (availability) but disclaim what customers need (performance)
- **Legal validity:** Disclaimers likely enforceable under both California and Irish law in B2B contexts
  - California: Unconscionability high bar, rarely applied to sophisticated parties
  - Irish: Fairness test provides more scrutiny but not insurmountable for suppliers
- **Practical outcome:** Customers bear all model performance risk despite limited ability to verify, monitor, or remedy degradation
- **Connection to IP:** Even if prompts qualify as trade secrets, contracts disclaim the service quality that makes prompt investment worthwhile

---

## VI. EU LAW: CHOICE OF LAW AND MANDATORY PROVISIONS [1,500 words]

### A. Rome I Regulation Framework

#### 1. Party Autonomy (Article 3)
- **Regulation (EC) No 593/2008:** Law applicable to contractual obligations
- **Article 3(1):** Contract governed by law chosen by parties
- **Application:** California/Irish law choice in AI contracts falls within party autonomy
- **Policy:** Enhances legal certainty and predictability in international commerce

#### 2. Overriding Mandatory Provisions (Article 9)

##### Article 9(1) Definition:
- "Provisions the respect for which is regarded as **crucial** by a country for safeguarding its **public interests**, such as its political, social or economic organisation, to such an extent that they are applicable to any situation falling within their scope, irrespective of the law otherwise applicable"

##### Three-Part Structure:
- **Article 9(2):** Forum OMPs always apply
- **Article 9(3):** Performance location OMPs may apply (discretionary, if render performance unlawful)
- **Deliberate restriction:** Replaced Rome Convention Art 7(1) "close connection" test with narrow, specific criteria

##### Recital 37:
- OMPs interpreted "more restrictively" than simple non-derogable provisions
- Policy choice: Predictability over judicial flexibility

#### 3. Distinction from Public Policy
- **Article 21:** Public policy (ordre public) operates negatively as corrective
- **Article 9:** OMPs operate positively, displacing lex causae
- **Difference:** Public policy blocks intolerable outcomes; OMPs impose forum rules proactively

### B. Good Faith as Overriding Mandatory Provision?

#### 1. Good Faith Across European Jurisdictions

##### Germany:
- **§ 242 BGB (Treu und Glauben):** Pervasive standard, "king of paragraphs"
- **Functions:** Interpret contracts, supplement with ancillary duties, limit abusive rights exercise
- **Nature:** Structural pillar of German contract law

##### France:
- **Art 1104 Code civil:** Bonne foi required in negotiation, formation, performance
- **Status:** Characterized as public policy principle
- **Scope:** Comprehensive obligation not to act contrary to contract spirit

##### Italy:
- **Arts 1175, 1375 Codice civile:** Buona fede in obligations and performance
- **Integration:** Fundamental principle across contract law

##### Ireland:
- **No general duty:** *Flynn v Breccia* [2017] IECA 74 definitively rejected
- **Limitation:** Outside specific relational contract categories, no good faith implied

#### 2. Why Good Faith Does NOT Qualify as OMP

##### Doctrinal Reasons:
1. **Not specific "provision":** Open-textured legal standard, not identifiable rule
2. **Private not public interest:** Regulates inter partes fairness, not state's political/social/economic organization
3. **Lacks uniformity:** Fundamental in Germany, rejected in Ireland - cannot be "crucial" for EU-wide public interest
4. **Function:** Interpretive/integrative tool within domestic law, not supra-national override

##### CJEU Authority:
- **Nikiforidis (C-135/15, 2016):** Article 9 provides exhaustive list; restrictive interpretation mandatory
- **Policy:** Allowing good faith as OMP would reintroduce unpredictability Rome I was designed to eliminate
- **Outcome:** Good faith principles from third Member States cannot be applied as OMPs

#### 3. Limited Utility Even if Applicable

##### Conceptual Limitations:
- **Good faith concerns manner:** How parties exercise rights, not substantive performance standards
- **Not warranty creator:** Doesn't impose quality standards parties deliberately excluded
- **Function:** Police abusive/opportunistic behavior, not rewrite risk allocation

##### Application to AI Contracts:
- **Supplier accurately discloses:** "As-is," no accuracy warranties - satisfies honesty requirement
- **Performs as specified:** Provides API access per contract - satisfies loyalty requirement
- **Model degradation:** If disclosed that performance may vary, continued use despite degradation doesn't breach good faith absent affirmative misrepresentation

##### Evidentiary Obstacles:
- **Same problems persist:** Must establish baseline performance, measure decline, prove exceeds acceptable variation
- **No objective benchmarks:** Non-deterministic outputs, task-specific metrics, lack of standardization
- **Conclusion:** Good faith doesn't solve evidentiary challenges inherent in proving AI model non-conformity

### C. Alternative Mandatory Provisions

#### 1. Consumer Protection Directives (Not Applicable to B2B)
- **Directive 93/13/EEC (Unfair Terms):** Consumer contracts only
- **Directive 2011/83/EU (Consumer Rights):** Not applicable to B2B
- **Limitation:** Article addresses B2B contexts where consumer protection unavailable

#### 2. Competition Law (Not Relevant to Contract Terms)
- **Articles 101-102 TFEU:** Anticompetitive agreements, abuse of dominance
- **Potential relevance:** If all major providers use identical disclaimer structures, possible coordinated behavior?
- **Unlikely:** Standard industry practice, legitimate business justification (AI uncertainty)

#### 3. AI Act Transparency Requirements
- **Regulation (EU) 2024/1689:** AI Act entered force August 2024
- **High-risk systems:** Technical documentation, transparency obligations
- **Interaction with trade secrets:** Recitals acknowledge trade secrets "should be safeguarded" but no operational guidance
- **Dun & Bradstreet framework:** Case-by-case balancing by authorities
- **Status:** Incompletely theorized; awaits Commission guidance or judicial decisions

### D. EU Law Synthesis
- **Party autonomy upheld:** California/Irish law choice valid under Rome I
- **Good faith cannot override:** Fails Article 9 criteria as OMP; restrictive interpretation per Nikiforidis
- **Consumer protection unavailable:** B2B contexts fall outside Directive 93/13/EEC scope
- **AI Act intersection unresolved:** Transparency vs. trade secrets awaits clarification
- **Practical outcome:** Choice of law strategies by AI providers effectively insulate warranty disclaimers from continental good faith challenges

---

## VII. CONCLUSION [1,000 words]

### A. Synthesis of Findings

#### 1. IP Protection: Narrow and Conditional
- **Copyright:** Most prompts fail as instructions (ideas not expression); possible exception for highly sophisticated prompts but functional nature remains obstacle
- **Trade secrets:** Theoretically possible for sophisticated prompts IF:
  - Enterprise services with contractual confidentiality only
  - Comprehensive legal + organizational + technical measures
  - Documented substantial investment
  - Quantified competitive advantages
- **Reality:** Protection demanding in practice, uncertain in application, provisional pending CJEU clarification

#### 2. Contract Law: The Performance Protection Gap
- **Providers guarantee:** Infrastructure availability (99.5%-99.95%)
- **Providers disclaim:** Model accuracy, output quality, performance consistency
- **Legal validity:** Disclaimers likely enforceable under California and Irish law in B2B contexts
- **Consequence:** All model performance risk allocated to customers

#### 3. EU Law: Limited Override Possibilities
- **Rome I permits:** Party choice of California/Irish law
- **Good faith fails:** As overriding mandatory provision under Article 9
- **Consumer protection inapplicable:** B2B contexts outside Directive 93/13/EEC
- **Outcome:** Choice of law strategies effectively insulate provider disclaimers

### B. The Paradox: Value Without Protection

#### 1. Economic Value Exists But...
- **Market evidence:** Prompt marketplaces, professional salaries, productivity gains
- **Investment real:** Months of development, measurable costs, competitive advantages
- **But:** No licensing markets, no litigation, no M&A valuations, no regulatory recognition

#### 2. Legal Protection Theoretically Available But...
- **Copyright possible:** For most sophisticated prompts
- **Trade secrets possible:** With comprehensive measures
- **But:** High barriers, uncertain application, structural tensions with cloud architecture

#### 3. Contractual Allocation Overrides Both
- **Even if:** Prompts qualify as trade secrets
- **Contract disclaims:** The service quality making prompt investment worthwhile
- **Result:** IP protection pyrrhic victory if underlying service quality unprotected

### C. Unresolved Tensions

#### 1. Doctrinal Gaps
- **No CJEU guidance:** Directive 2016/943 interpretation awaits preliminary ruling
- **Cross-border uncertainty:** Divergent national approaches (German proportionality, Dutch stringency, French procedure)
- **AI Act intersection:** Trade secret vs. transparency incompletely theorized

#### 2. Technical-Legal Mismatch
- **Trade secret law assumes:** Exclusive physical/digital control
- **Cloud AI requires:** Third-party disclosure to function
- **Doctrinal adaptation needed:** Accommodation of distributed architectures

#### 3. Evidence and Metrics
- **Non-conformity proof:** Requires baseline performance, degradation measurement, causal attribution
- **AI characteristics:** Non-deterministic, task-specific, stochastic variation
- **Legal system needs:** Objective standards, quantifiable metrics, predictable outcomes

### D. Recommendations

#### 1. For Businesses Using AI Services

##### Prompt Protection Strategy:
- **Trade secret protection:** Only for sophisticated prompts representing substantial investment
- **Minimum requirements:**
  - Exclusive use of enterprise AI services with documented contractual confidentiality
  - Comprehensive internal protection program (legal + organizational + technical)
  - Documentation of development costs, performance improvements, competitive advantages
- **Acceptance:** Simple/intermediate prompts not protectable; factor into IP strategy

##### Contract Negotiation Priorities:
- **Custom enterprise agreements:** Negotiate model version locks, performance baselines, enhanced SLAs
- **Model lifecycle management:** Advance notice periods for deprecations, migration support commitments
- **Remedy enhancement:** Negotiate liability caps higher than standard terms where AI mission-critical
- **Documentation requirements:** Require provider disclosure of model updates, performance metric changes

##### Risk Mitigation:
- **Human review:** Contract disclaimers allocate verification responsibility to customer; implement review procedures
- **Output validation:** Independent verification systems for critical applications
- **Model monitoring:** Track performance metrics, detect degradation early
- **Contingency planning:** Alternative providers, model switching capabilities, fallback procedures

#### 2. For AI Service Providers

##### Transparency Enhancements:
- **Model lifecycle disclosure:** Clearer communication about expected model lifespans, update frequencies
- **Performance metric publishing:** Benchmark results, confidence intervals, limitations documentation
- **Degradation acknowledgment:** Transparent about known degradation patterns, mitigation strategies

##### Differentiated Service Tiers:
- **Performance SLAs:** Offer optional performance guarantees (beyond availability) at premium pricing
- **Model stability commitments:** Version-lock options for enterprises requiring consistency
- **Balanced risk allocation:** Partial warranties for specific use cases with higher pricing

#### 3. For EU Legislators and Courts

##### CJEU Preliminary Reference Needed:
- **Trade secrets + cloud architecture:** Can contractual confidentiality preserve secrecy despite third-party disclosure?
- **Reasonable steps proportionality:** How to assess when technical necessity requires third-party involvement?
- **Commercial value causation:** When does value derive "because secret" vs. because of underlying technology?

##### Legislative Clarification:
- **AI Act implementation:** Operational guidance on trade secret vs. transparency balancing
- **Service quality standards:** Consider mandatory disclosure requirements for AI service characteristics, limitations
- **B2B contract regulation:** Assess whether complete disclaimer of performance characteristics in AI services should be limited

##### Judicial Development:
- **National courts:** First cases addressing prompt misappropriation will establish precedents
- **Unconscionability application:** AI contract disclaimer challenges will test substantive fairness boundaries
- **Good faith limits:** Define boundaries of good faith's inability to impose quality standards parties excluded

### E. Future Research Directions

#### 1. Empirical Studies Needed
- **European prompt markets:** EU-specific data on valuations, transactions, labor markets
- **Degradation documentation:** Systematic tracking of commercial AI model performance over time
- **Contract negotiation practices:** Survey of enterprise customers on actual negotiated protections

#### 2. Comparative Analysis
- **Other jurisdictions:** US, UK, China approaches to prompt protection
- **Sectoral differences:** Healthcare, financial services, legal practice AI usage patterns
- **SME vs. enterprise:** Protection feasibility and practices vary by company size

#### 3. Regulatory Development Tracking
- **AI Act evolution:** Commission implementing acts, enforcement guidelines
- **Member State implementation:** Divergence in trade secret law application to AI contexts
- **International harmonization:** WIPO, OECD initiatives on AI governance

### F. Concluding Observation

The legal protection of AI prompts in the EU reveals fundamental tensions between traditional intellectual property frameworks developed for tangible innovations and the distributed, cloud-based architecture of modern AI systems. While economic evidence demonstrates that prompts possess commercial value and require substantial investment to develop, existing legal frameworks provide only narrow, conditional, and uncertain protection. Copyright law's idea-expression dichotomy largely excludes instructions; trade secret law struggles to accommodate information that must be disclosed to third parties to function; and contract law permits providers to disclaim the very performance characteristics that make prompt engineering valuable.

This gap between economic reality and legal protection reflects a broader challenge: adapting 20th-century intellectual property regimes to 21st-century AI technologies. Whether the solution lies in judicial interpretation stretching existing doctrines, legislative intervention creating sui generis frameworks, or market mechanisms developing alternative protection models remains an open question for European law and policy.

What is clear is that businesses investing substantial resources in prompt engineering currently operate in a legally uncertain environment where protection, if available at all, requires comprehensive, costly, and still-provisional measures whose effectiveness remains untested in European courts.

---

**WORD COUNT ESTIMATE: ~11,000 words**

**NEXT STEPS:**
1. Drafting sections based on outline
2. Integration of citations (OSCOLA format)
3. Cross-referencing existing research materials
4. Quality assurance review
5. Submission preparation for IIC

