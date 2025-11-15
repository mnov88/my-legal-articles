# Detailed Topic Map: AI Prompt Protection Arguments

**Purpose:** Granular mapping of all key legal arguments, doctrinal principles, case law applications, and counterarguments across EU intellectual property regimes analyzing prompt protectability.

**Structure:** Four main IP regimes with subsection-level argument mapping and Obsidian links to specific analysis locations.

---

## I. COPYRIGHT AND SOFTWARE PROTECTION

### A. Harmonized Originality Standard

**Core Framework:**
- Five cumulative requirements for copyright protection
- Links: [[Section III - Copyright and Software Protection - REVISED#A. The Harmonized Originality Standard]]

**Key Requirements:**

1. **Author's Own Intellectual Creation**
   - CJEU establishment: Infopaq International (C-5/08)
   - Software Directive Article 1(3): programs protected "if they are original in the sense that they are the author's own intellectual creation"
   - InfoSoc Directive 2001/29: harmonized standard across all copyright categories
   - Link: [[Section III - Copyright and Software Protection - REVISED#A. The Harmonized Originality Standard]]

2. **Reflects Author's Personality**
   - Painer v Standard Verlags (C-145/10): work must "reflect the author's personality"
   - Personality expression requirement distinct from skill/labor
   - Application to prompts: functional instructions vs. personality expression
   - Link: [[Section III - Copyright and Software Protection - REVISED#A. The Harmonized Originality Standard]]

3. **Free and Creative Choices**
   - Football Dataco v Yahoo! (C-604/10): choices must be "free and creative"
   - Brompton Bicycle Ltd v Chedech / Get2Get (C-833/18): "a degree of creative freedom"
   - Where functional constraints predominate, originality fails
   - Application to prompts: functional purpose dictates form
   - Link: [[Section III - Copyright and Software Protection - REVISED#A. The Harmonized Originality Standard]]

4. **Technical/Functional Constraints Defeat Originality**
   - BSA v Ministerstvo kultury (C-393/09): "technical function" prevents free/creative choices
   - Brompton Bicycle: even where some freedom exists, predominant constraint defeats protection
   - Application to prompts: instructional purpose constrains formulation
   - Link: [[Section III - Copyright and Software Protection - REVISED#C. Application to Complex Prompts]]

5. **Expression Not Ideas**
   - Infopaq principle: copyright protects expression, never ideas
   - SAS Institute (C-406/10): functionality, programming language, data file formats excluded
   - TRIPS Article 9(2): "copyright protection shall extend to expressions and not to ideas"
   - Application to prompts: specify ideas about desired outputs
   - Link: [[Section III - Copyright and Software Protection - REVISED#E. The Idea-Expression Dichotomy and Software Directive Exclusions]]

**Consolidating Authority:**
- Cofemel v G-Star Raw (C-683/17): unified originality test across all copyright subject matter
- Consolidates Infopaq, Painer, Football Dataco, BSA into single framework
- Link: [[Section III - Copyright and Software Protection - REVISED#A. The Harmonized Originality Standard]]

### B. Simple Prompts: Multiple Failures

**Examples:**
- "Summarize this article"
- "Create an image of a cat"
- "Translate to French"

**Why They Fail:**

1. **No Free/Creative Choices**
   - Limited to necessary words describing function
   - No alternatives achieving same result
   - Infopaq: "words as such" not protected
   - Link: [[Section III - Copyright and Software Protection - REVISED#B. Application to Simple Prompts]]

2. **Don't Reflect Personality**
   - Functional specification, not personal expression
   - Any competent user would formulate similarly
   - Painer requirement unsatisfied
   - Link: [[Section III - Copyright and Software Protection - REVISED#B. Application to Simple Prompts]]

3. **Are Ideas, Not Expression**
   - Describe what to create (idea specification)
   - Do not embody creative expression
   - Fall within excluded categories
   - Link: [[Section III - Copyright and Software Protection - REVISED#B. Application to Simple Prompts]]

**Authority:**
- Multiple independent grounds defeat protection
- Cumulative failures ensure no edge cases qualify
- Link: [[Section III - Copyright and Software Protection - REVISED#B. Application to Simple Prompts]]

### C. Complex Prompts: Three Obstacles

**Example Type:**
- 400-word system prompts with parameters
- Multi-stage reasoning instructions
- Detailed persona/context specifications

**Why Labor/Complexity Insufficient:**

**Obstacle 1: Instructions Problem**
- Prompts describe what to create (idea) rather than expressing creative work
- Function as specifications for AI system behavior
- Protecting prompts = protecting ideas indirectly
- Infopaq/SAS Institute principle violated
- Link: [[Section III - Copyright and Software Protection - REVISED#C. Application to Complex Prompts]]

**Obstacle 2: Functional Constraints**
- Purpose dictates formulation
- BSA principle: technical function prevents free/creative choices
- Even complex prompts constrained by:
  - Model architecture requirements
  - Token efficiency demands
  - Effectiveness criteria
  - Output specifications
- Brompton: predominant functional constraint defeats originality
- Link: [[Section III - Copyright and Software Protection - REVISED#C. Application to Complex Prompts]]

**Obstacle 3: Merger Doctrine Concerns**
- Limited ways to express instructions effectively
- Functional specifications constrain expression
- Idea and expression merge
- Protection would monopolize underlying ideas
- Link: [[Section III - Copyright and Software Protection - REVISED#C. Application to Complex Prompts]]

**Czech Municipal Court Analysis:**
- First judicial opinion on prompt copyrightability (2023)
- Rejected protection for GitHub Copilot prompts
- Functional character predominates
- Link: [[Section III - Copyright and Software Protection - REVISED#C. Application to Complex Prompts]]

### D. Identifiability Requirement

**CJEU Framework:**
- Levola Hengelo (C-310/17): subject matter must be identified "with sufficient precision and objectivity"
- Precision requirement: stable identification over time
- Objectivity requirement: third parties can recognize same work
- Link: [[Section III - Copyright and Software Protection - REVISED#D. Prompts and the Identifiability Requirement]]

**Application to Prompts:**

1. **Non-Deterministic Outputs**
   - Same prompt → different outputs across invocations
   - Probabilistic inference prevents stable identification
   - What is the "work" being protected?
   - Link: [[Section III - Copyright and Software Protection - REVISED#D. Prompts and the Identifiability Requirement]]

2. **Model Dependency**
   - Outputs vary across different models
   - GPT-4 vs. Claude vs. Gemini produce different results
   - No objective identification of claimed work
   - Link: [[Section III - Copyright and Software Protection - REVISED#D. Prompts and the Identifiability Requirement]]

3. **Levola Standard Unsatisfied**
   - Cannot identify with precision required
   - Third parties cannot objectively recognize "same work"
   - Independent failure of protection
   - Link: [[Section III - Copyright and Software Protection - REVISED#D. Prompts and the Identifiability Requirement]]

### E. Idea-Expression Dichotomy and Software Directive Exclusions

**Fundamental Copyright Principle:**
- TRIPS Article 9(2): copyright extends to expressions, not ideas
- InfoSoc Directive: implements TRIPS obligations
- Software Directive Article 1(2): excludes ideas, principles, logic, algorithms, interfaces
- Link: [[Section III - Copyright and Software Protection - REVISED#E. The Idea-Expression Dichotomy and Software Directive Exclusions]]

**Critical Case Law:**

**BSA v Ministerstvo kultury (C-393/09):**
- GUIs not protected as programs
- User-facing interfaces excluded
- Functionality drives exclusion
- Prompts analogous: user-facing instructions
- Link: [[Section III - Copyright and Software Protection - REVISED#E. The Idea-Expression Dichotomy and Software Directive Exclusions]]

**SAS Institute v World Programming Ltd (C-406/10):**
- Functionality not protected
- Programming language elements excluded
- Data file formats excluded
- "Ideas and principles" exemption applies
- Prompts analogous: specify functionality and methods
- Link: [[Section III - Copyright and Software Protection - REVISED#E. The Idea-Expression Dichotomy and Software Directive Exclusions]]

**Sony Computer Entertainment v Datel (C-680/21, 2024):**
- RAM variables during program execution not protected
- Dynamic, transient data excluded
- Non-deterministic nature relevant
- Prompts analogous: transient instructions producing variable outputs
- Link: [[Section III - Copyright and Software Protection - REVISED#E. The Idea-Expression Dichotomy and Software Directive Exclusions]]

**Unified Framework:**
- InfoSoc Directive and Software Directive converge
- Same fundamental reason: prompts are instructions about ideas/functionality
- Not expression of creative works
- Three cases establish consistent exclusion
- Link: [[Section III - Copyright and Software Protection - REVISED#E. The Idea-Expression Dichotomy and Software Directive Exclusions]]

### F. Preparatory Design Material (Software Directive)

**Legal Framework:**
- Software Directive Article 1(1): protection includes "preparatory design material"
- Must lead to computer program at later stage
- Requires technical specificity approaching code
- Link: [[Section III - Copyright and Software Protection - REVISED#F. Software Protection: Preparatory Design Material]]

**Why Prompts Don't Qualify:**

1. **Not Programs Themselves**
   - Inputs to programs, not programs
   - Do not constitute source/object code
   - Describe what to do, not how to implement
   - Link: [[Section III - Copyright and Software Protection - REVISED#F. Software Protection: Preparatory Design Material]]

2. **Lack Technical Specificity**
   - Natural language descriptions
   - Do not approach quasi-coding level
   - Cannot be compiled or executed
   - Link: [[Section III - Copyright and Software Protection - REVISED#F. Software Protection: Preparatory Design Material]]

3. **Non-Deterministic Nature**
   - Sampaio argument: outputs vary probabilistically
   - Cannot lead to predictable program implementation
   - Fundamental incompatibility with preparatory design concept
   - Link: [[Section III - Copyright and Software Protection - REVISED#F. Software Protection: Preparatory Design Material]]

### G. Policy Justifications

**Article 6 Interoperability:**
- Software Directive Article 6: decompilation for interoperability permitted
- UsedSoft (C-128/11): exhaustion applies to software
- Functionality must remain accessible for competition
- Protecting prompts would restrict AI system interoperability
- Link: [[Section III - Copyright and Software Protection - REVISED#G. Policy Justifications for Functional Instruction Exclusion]]

**Competition Policy:**
- Functional exclusions enable market competition
- Bronner/Magill doctrine: no copyright monopoly on functionality
- Prompt protection would tax AI utilization
- Link: [[Section III - Copyright and Software Protection - REVISED#G. Policy Justifications for Functional Instruction Exclusion]]

### H. Scholarly Consensus

**Academic Agreement:**

1. **Xiyin He (2024) 55 IIC 321:**
   - Prompts "merely unprotectable ideas"
   - Functional specifications not expression
   - Link: [[Section III - Copyright and Software Protection - REVISED#H. Scholarly Consensus on Prompt Copyrightability]]

2. **Gervais & Hugenholtz (2023) Kluwer Copyright Blog:**
   - Prompt protection "dangerously close to owning the underlying idea"
   - Violates fundamental copyright principle
   - Link: [[Section III - Copyright and Software Protection - REVISED#H. Scholarly Consensus on Prompt Copyrightability]]

3. **Quintais & Hugenholtz (2020) 51 IIC 28:**
   - Technical constraints leave no creative freedom
   - Functional purpose defeats originality
   - Link: [[Section III - Copyright and Software Protection - REVISED#H. Scholarly Consensus on Prompt Copyrightability]]

**Consensus View:**
- No credible academic support for prompt copyright
- Scholarly literature uniformly skeptical/negative
- Link: [[Section III - Copyright and Software Protection - REVISED#H. Scholarly Consensus on Prompt Copyrightability]]

### I. Database Protection

**Two Separate Rights:**
- Copyright protection: selection/arrangement originality
- Sui generis right: substantial investment in obtaining/verifying/presenting
- Database Directive 96/9/EC
- Link: [[Section III - Copyright and Software Protection - REVISED#J. Database Protection for Prompt Collections]]

**Copyright for Prompt Collections:**
- Requires originality in selection/arrangement
- Individual prompts: too minimal for protection
- Curated libraries: possible but limited protection
- Does not protect individual prompts
- Link: [[Section III - Copyright and Software Protection - REVISED#J. Database Protection for Prompt Collections]]

**Sui Generis Right:**

**Requirements:**
- Substantial investment in obtaining, verifying, or presenting
- Protects against extraction/reutilization
- Does not prevent independent creation

**Critical Limitation - BHB v William Hill (C-203/02):**
- Investment in creating data not protected
- Only investment in obtaining existing data qualifies
- Prompt engineering = creation, not obtaining
- Fundamentally defeats sui generis protection
- Link: [[Section III - Copyright and Software Protection - REVISED#J. Database Protection for Prompt Collections]]

**Conclusion:**
- Individual prompts: unprotected
- Collections: minimal protection not addressing core appropriability concerns
- Link: [[Section III - Copyright and Software Protection - REVISED#J. Database Protection for Prompt Collections]]

### J. Counterarguments and Rebuttals

**Counterargument 1: Labor Investment Deserves Protection**

*Argument:*
- Substantial time/money invested in prompt engineering
- Sweat-of-the-brow should warrant protection
- Hours of testing and refinement deserve reward

*Rebuttal:*
- EU law explicitly rejected sweat-of-the-brow in Football Dataco
- Investment alone insufficient without originality
- Labor spent does not create copyrightability where functional constraints predominate
- Brompton Bicycle: effort irrelevant if free/creative choices absent
- Link: [[Section III - Copyright and Software Protection - REVISED#K. Counterarguments and Rebuttals]]

**Counterargument 2: Complex Prompts Are Creative Works**

*Argument:*
- 400-word system prompts show creativity
- Structuring, persona design, context setting = creative choices
- Distinguishable from simple instructions

*Rebuttal:*
- Complexity ≠ originality
- Choices driven by effectiveness (functional constraint)
- Instructions remain instructions regardless of length
- Czech Municipal Court rejected this argument explicitly
- Three independent obstacles (instructions, functional constraint, merger) defeat protection
- Link: [[Section III - Copyright and Software Protection - REVISED#K. Counterarguments and Rebuttals]]

**Counterargument 3: Protectable as Compilations**

*Argument:*
- Multi-part prompts = compilations
- Selection/arrangement of components shows originality
- Database/anthology analogy

*Rebuttal:*
- Components themselves (instructions) not protectable
- Compilation of unprotectable elements cannot create protection
- Functional arrangement driven by effectiveness
- No independent creative contribution in ordering
- Link: [[Section III - Copyright and Software Protection - REVISED#K. Counterarguments and Rebuttals]]

**Counterargument 4: Outputs Should Determine Protectability**

*Argument:*
- If AI output is creative, prompt enabling it should be protected
- Causal contribution to creative work warrants recognition
- Photographer analogy: camera settings protected through photograph

*Rebuttal:*
- Prompt ≠ output; they are separate artifacts
- Photographer creates expression; prompt specifies idea
- Levola identifiability problem: non-deterministic outputs
- Protection of output (if any) does not extend backward to instructions
- Link: [[Section III - Copyright and Software Protection - REVISED#K. Counterarguments and Rebuttals]]

### K. Synthesis: Three Independent Barriers

**Barrier 1: Originality Failure**
- Functional constraints dictate choices
- Brompton Bicycle framework: predominant constraint defeats protection
- Even complex prompts constrained by effectiveness requirements
- No free/creative choices expressing personality
- Link: [[Section III - Copyright and Software Protection - REVISED#L. Synthesis: Three Independent Barriers]]

**Barrier 2: Identifiability Failure**
- Non-deterministic outputs prevent stable identification
- Levola Hengelo precision/objectivity unsatisfied
- Cannot identify claimed "work" with required specificity
- Model dependency exacerbates problem
- Link: [[Section III - Copyright and Software Protection - REVISED#L. Synthesis: Three Independent Barriers]]

**Barrier 3: Idea-Expression Exclusion**
- Prompts specify ideas/methods/functionality
- TRIPS Article 9(2) / Software Directive Article 1(2) exclude
- BSA, SAS Institute, Sony Datel establish consistent framework
- Instructions about what to create, not expression of creative works
- Link: [[Section III - Copyright and Software Protection - REVISED#L. Synthesis: Three Independent Barriers]]

**Cumulative Effect:**
- Each barrier alone sufficient to defeat protection
- Together they are dispositive
- No plausible path to copyright protection for prompts
- Link: [[Section III - Copyright and Software Protection - REVISED#L. Synthesis: Three Independent Barriers]]

### L. Exceptional Cases

**Literary Work Exception:**
- Extremely rare: prompt as independent literary work
- Protection of text itself, not functional use as instruction
- Does not disturb general conclusion
- Link: [[Section III - Copyright and Software Protection - REVISED#M. Exceptional Cases]]

**Software Component Exception:**
- Prompt embedded in software as protected component
- Protection derives from program, not prompt independently
- Integration into larger copyrightable work
- Does not create general prompt copyrightability
- Link: [[Section III - Copyright and Software Protection - REVISED#M. Exceptional Cases]]

---

## II. TRADE SECRETS

### A. Directive 2016/943 Framework

**Legal Basis:**
- Harmonizes trade secret protection across EU
- Implements TRIPS Article 39 obligations
- Article 114 TFEU (internal market harmonization)
- Link: [[Section VI - Trade Secrets - Draft#A. The Directive 2016/943 Framework]]

**Three-Part Cumulative Test (Article 2(1)):**

1. Secrecy: information "not generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question"

2. Commercial value: "has commercial value because it is secret"

3. Reasonable steps: "has been subject to reasonable steps under the circumstances, by the person lawfully in control of the information, to keep it secret"

**Cumulative Nature:**
- All three required simultaneously
- Failure of any single element defeats protection entirely
- Link: [[Section VI - Trade Secrets - Draft#A. The Directive 2016/943 Framework]]

**Policy Balances:**

**Article 1(3) Exclusions:**
- Employee mobility protected
- "Experience and skills honestly acquired" excluded
- Cannot restrict ordinary professional competency
- Link: [[Section VI - Trade Secrets - Draft#A. The Directive 2016/943 Framework]]

**Article 3 Lawful Acquisition:**
- Independent discovery/creation permitted
- Reverse engineering explicitly allowed
- Observation/study of publicly available products lawful
- Critical for prompts: reverse engineering from outputs lawful
- Link: [[Section VI - Trade Secrets - Draft#A. The Directive 2016/943 Framework]]

### B. Secrecy Element: Cloud Disclosure Paradox

**The Structural Problem:**
- Cloud AI requires transmitting prompts to third-party providers
- OpenAI, Anthropic, Google process prompts on their infrastructure
- Prompts necessarily disclosed to AI provider
- Does third-party disclosure destroy secrecy?
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

**Academic Framework:**
- Sandeen & Rowe: third-party disclosure potentially destroys secrecy absent confidentiality agreements
- Information "known outside" the company may lack required secrecy
- Provider possesses information → "readily accessible" to provider
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

**National Court Guidance:**

**Germany - OLG Düsseldorf (2021) I-20 U 16/20:**
- Disclosure without executed NDAs defeats protection
- Must vet partners, ensure minimum necessary disclosure, maintain executed agreements
- "Executed confidential disclosure agreements" essential
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

**Netherlands - Rechtbank Midden-Nederland (2018) ECLI:NL:RBMNE:2018:3992:**
- Technical drawings shared without NDAs failed as trade secrets
- Policy existed but practice of unprotected disclosure defeated claim
- "Policy without practice fails"
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

**France - CA Paris (2022) RG n° 19/08167:**
- Technical drawings shared without NDAs failed secrecy and reasonable steps
- Contractual protections essential for third-party disclosure
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

**Judicial Consensus:**
- Third-party disclosure without contractual protections defeats trade secret status
- Applies regardless of other protective measures
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

**Consumer Tier vs. Enterprise Tier:**

**Consumer Services (Fail Secrecy):**
- OpenAI free ChatGPT: "may use Content to provide, maintain, develop, and improve our Services"
- Google consumer terms: authorize broad use
- Anthropic free Claude.ai: permit use for service improvement
- Contractually authorized use defeats secrecy
- AI provider specialists = "persons within circles who normally deal with the kind of information"
- Prompts "readily accessible" to provider with authorization to use
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

**Enterprise Services (Potentially Preserve Secrecy):**
- Microsoft Azure OpenAI: "Customer Data will not be available to other customers" and "will not be used to improve Azure OpenAI"
- Anthropic Enterprise: customer data "will not be used for training or improving our models"
- Google Cloud Vertex AI: customer data "will not be used to improve Google's products or services"
- Contractual prohibitions on use/disclosure analogous to employee NDAs
- Disclosure with confidentiality obligations potentially preserves secrecy
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

**Bright-Line Rule:**
- Consumer-tier prompts: categorically fail Article 2(1)(a)
- Enterprise-tier prompts: can potentially satisfy secrecy requirement
- Conditional on documented contractual protections
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

**Business Requirements:**
- Prohibit consumer AI services for confidential prompts
- Require enterprise services with verified contractual confidentiality
- Document service agreements and maintain evidence
- Train employees on consumer vs. enterprise distinction
- Monitor compliance through technical controls
- Enforce violations demonstrating implementation in practice
- Link: [[Section VI - Trade Secrets - Draft#B. The Secrecy Requirement and the Cloud Disclosure Paradox]]

### C. Commercial Value Element: Model Dependency Challenge

**Legal Standard:**
- Information must "have commercial value because it is secret"
- Dual requirement: (1) commercial value exists, (2) derives from secrecy
- Commission Impact Assessment: value = unauthorized acquisition would harm holder's interests
- Causal link essential: "because it is secret"
- Link: [[Section VI - Trade Secrets - Draft#C. Commercial Value Derived from Secrecy]]

**The Model Dependency Problem:**
- Prompt value depends on underlying LLM
- ChatGPT prompt only valuable when processed by GPT-4
- Same prompt on different model may fail/underperform
- Does prompt have independent value or derivative value from model?
- Link: [[Section VI - Trade Secrets - Draft#C. Commercial Value Derived from Secrecy]]

**Argument Against Independent Value:**
- Pharmaceutical example: 60% faster identification only because Claude processes effectively
- Claude's capabilities from Anthropic's investment, not user's prompt work
- Prompt worthless without model access
- Distinguishes from paradigmatic trade secrets (chemical formulas, manufacturing processes)
- If disclosure wouldn't harm competitive position (competitors lack model access), value element fails
- OLG Düsseldorf: unauthorized use must harm competitive position
- Link: [[Section VI - Trade Secrets - Draft#C. Commercial Value Derived from Secrecy]]

**Three Considerations Supporting Independent Value:**

**1. Commercial Marketplaces:**
- PromptBase: 370,000+ users, 220,000+ prompts, $1.99-$4.99 prices
- FlowGPT: millions of prompts with ratings
- ChatX: pays up to 39 CAD per submission
- Market recognition of prompts as valuable independent assets
- Value transcends any single user's model access
- Resides in optimized formulation itself
- Link: [[Section VI - Trade Secrets - Draft#C. Commercial Value Derived from Secrecy]]

**2. Measurable Economic Benefits:**
- Pharmaceutical example: 60% faster = quantifiable time savings worth millions
- Legal analytics: €2.3M investment over 18 months = documented development costs
- German courts: consider development costs, value to company, importance to competitive position
- Documented investment + quantified performance improvements satisfy standard
- Link: [[Section VI - Trade Secrets - Draft#C. Commercial Value Derived from Secrecy]]

**3. System Prompts as Differentiation:**
- Proprietary system prompts customize AI model behavior within applications
- Substantial engineering investment
- Provide competitive differentiation among products using same underlying model
- Automotive manufacturer example: supply chain optimization prompts
- Independent business asset distinct from model access
- Link: [[Section VI - Trade Secrets - Draft#C. Commercial Value Derived from Secrecy]]

**Customer List Analogy:**
- Individual contact information: publicly available, not protected
- Curated compilation from substantial effort/investment: protectable
- Value in compilation's "precise configuration and assembly"
- Similarly: individual prompting techniques may be known
- Refined prompt from months of optimization = valuable compilation
- Competitors lack this optimized formulation
- Link: [[Section VI - Trade Secrets - Draft#C. Commercial Value Derived from Secrecy]]

**Causal Link: "Because It Is Secret":**
- Disclosure must harm competitive advantage
- Prompts codifying novel applications, non-obvious combinations, substantial optimization = satisfy
- Disclosure allows competitors to appropriate investment results without equivalent costs
- Prompts implementing widely known techniques or achieving results competitors independently achieved = fail
- Link: [[Section VI - Trade Secrets - Draft#C. Commercial Value Derived from Secrecy]]

**Filter Function:**
- Excludes trivial/widely known prompts
- Potentially protects sophisticated prompts with substantial investment
- Provides genuine competitive advantages
- Link: [[Section VI - Trade Secrets - Draft#C. Commercial Value Derived from Secrecy]]

### D. Reasonable Steps Element: Distributed Architecture Tension

**Legal Standard:**
- Information must be "subject to reasonable steps under the circumstances"
- Recital 13: "duty of care as regards preservation of confidentiality"
- "Under the circumstances" = context-specific, proportionate
- Not absolute security, but actual protective measures
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**German Three-Level Framework (Geschäftsgeheimnisgesetz):**

**Legal Measures:**
- NDAs with employees
- Confidentiality provisions in employment contracts
- Contractual restrictions with business partners
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**Organizational Measures:**
- Access restrictions
- Need-to-know policies
- Classification systems identifying confidential information
- Employee training on confidentiality obligations
- Exit procedures for departing employees
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**Technical Measures:**
- Passwords, encryption
- Access controls, authentication systems
- Monitoring for unauthorized access
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**OLG Düsseldorf Nine-Factor Proportionality Test:**
1. Type of trade secret
2. Specific circumstances of use
3. Value and development costs
4. Nature of information
5. Importance to company
6. Size of company
7. Usual confidentiality measures in the company
8. Type of labeling or marking
9. Contractual provisions with employees and partners
- Proportionality: SMEs need not match large corporation measures
- Measures must be reasonable given value and circumstances
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**French Requirements:**
- Specific identification and marking (not blanket "all confidential" declarations)
- Documented protection measures
- Technical restrictions and contractual protections
- Paris CA: demonstrable, implemented protection required
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**Dutch Stringency:**
- "Policy without practice fails the reasonable steps test"
- Stated policies that employees routinely violate = insufficient
- Actual implementation and enforcement required, not mere formal documentation
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**Cloud AI Structural Challenge:**
- Trade secret law assumed exclusive physical/digital control
- Cloud AI inverts: requires third-party disclosure as condition of use
- Prompt cannot function without transmission to provider infrastructure
- No equivalent to secured laboratory for in-house use
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**Resolution: Contractual Protections Can Suffice:**
- German courts: "executed confidential disclosure agreements" with third parties
- Properly documented contractual protections satisfy requirement even where provider accesses information
- "Under the circumstances" includes technical necessity of third-party processing
- Nine-factor test: "specific circumstances of use" = if use requires third-party involvement, assess relative to that constraint
- Proportionality recognizes third-party involvement inherent to using information in some contexts
- Cloud computing, outsourced manufacturing, collaborative research precedents
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**Comprehensive Protection Framework for Prompts:**

**Legal Measures:**
- Use exclusively enterprise AI services with documented contractual confidentiality
- Execute NDAs with employees and contractors
- Include confidentiality provisions in employment contracts specifically identifying prompts
- Maintain AI service provider agreements and document their terms
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**Organizational Measures:**
- Implement access controls limiting prompt creation/submission
- Establish classification systems identifying trade secret prompts
- Provide employee training on AI service use and consumer vs. enterprise distinction
- Institute monitoring and audit procedures detecting unauthorized disclosure
- Establish incident response plans
- Enforce policies through disciplinary action
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**Technical Measures:**
- Encrypt prompts in transit and at rest
- Implement authentication systems controlling access
- Sanitize prompts to remove unnecessary sensitive information before submission
- Monitor AI service usage for compliance
- Maintain audit logs of submissions
- Establish technical controls preventing consumer AI service use on company devices
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

**Doctrinal Straightforwardness, Practical Demands:**
- Doctrinally: reasonable steps "under the circumstances" accommodates necessity
- Practically: demands substantial investment in comprehensive infrastructure
- Dutch principle applies: must demonstrate actual implementation and enforcement
- Link: [[Section VI - Trade Secrets - Draft#D. Reasonable Steps under the Circumstances]]

### E. Synthesis and CJEU Guidance

**Dun & Bradstreet Austria (C-203/22, 2025) - Authoritative Precedent:**

**Holding:**
- GDPR transparency obligations vs. trade secret protection
- Controllers must provide "meaningful information about logic involved" to data subjects
- Need not disclose algorithms themselves where trade secrets revealed
- Blanket trade secret exemptions impermissible (Austrian law invalid)
- Case-by-case proportionality balancing required
- Controllers claiming protection must provide information to supervisory authorities/courts for assessment
- Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

**Two Principles for Prompts:**

1. **Algorithmic Information Can Qualify:**
   - Logical instructions controlling AI behavior not categorically excluded
   - CJEU did not create blanket exemption for computational instructions
   - In principle protectable as trade secrets
   - Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

2. **Protection Not Absolute:**
   - Must yield to fundamental rights and regulatory transparency
   - Proportionality assessment required
   - GDPR, AI Act, sector-specific regulations can override
   - Cannot invoke trade secrecy to avoid disclosure obligations where transparency outweighs confidentiality
   - Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

**Application Framework - Qualified Answer:**
- Prompts can qualify as trade secrets
- Only sophisticated prompts with rigorous protection measures
- Subject to displacement by regulatory transparency requirements
- Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

**Three-Element Interaction:**

**Article 2(1)(a) Secrecy:**
- Consumer-tier: categorically fail (TOS authorize provider use)
- Enterprise-tier: can potentially satisfy with contractual prohibitions
- Third-party disclosure unavoidable (cloud architecture)
- Contractual protections analogous to employee NDAs
- Preserve information as "not generally known"
- Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

**Article 2(1)(b) Commercial Value:**
- Simple prompts: fail (lack economic value)
- Sophisticated prompts: satisfy with documented investment
- Months of optimization, quantified improvements, proprietary system integration
- Disclosure enables competitor appropriation without equivalent development costs
- Causal link: disclosure harms competitive position
- Distinguishes valuable compilations from widely known techniques
- Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

**Article 2(1)(c) Reasonable Steps:**
- Cloud AI creates structural tension
- Traditional law assumed exclusive control
- Cloud inverts: third-party disclosure as condition of use
- "Under the circumstances" establishes context-specific proportionality
- Enterprise agreements + comprehensive internal measures can satisfy
- Dutch principle: demonstrable implementation required (not just documentation)
- Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

**Three Categories of Prompts:**

1. **Simple Prompts:**
   - Fail all three elements
   - No protection possible
   - Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

2. **Intermediate Prompts:**
   - Modest optimization
   - Face proportionality challenges (protective measures may exceed value)
   - Likely fail reasonable steps
   - Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

3. **Sophisticated Prompts:**
   - Substantial documented investment
   - Can qualify IF:
     - Used exclusively through enterprise services
     - Documented contractual protections
     - Comprehensive internal controls
   - Conditional protection only
   - Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

**Unresolved Tensions:**

**No CJEU Preliminary Ruling Yet:**
- No interpretation of Directive 2016/943's three-part test for algorithmic information
- National courts diverge: German proportionality vs. Dutch stringency vs. French procedural protections
- Cross-border uncertainty persists
- Need CJEU clarification on third-party disclosure with contractual safeguards
- Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

**AI Act Transparency Intersection:**
- AI Act (2024/1689) imposes transparency obligations
- High-risk systems: technical documentation, training data disclosure, deployment logs
- Recital 75: trade secrets "should be safeguarded" but no operational guidance
- Dun & Bradstreet framework: case-by-case balancing
- Needs Commission guidance or judicial decisions on when transparency overrides trade secrecy
- Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

**Conclusion - Conditional, Demanding, Provisional:**
- AI prompts can qualify under current EU law
- Qualification conditional on:
  - Sophisticated prompts only
  - Enterprise service frameworks
  - Rigorous protective measures
  - Acceptance that transparency may require disclosure
- Protection demanding: substantial infrastructure investment required
- Protection contested: divergent national approaches
- Protection provisional: pending authoritative CJEU interpretation
- Link: [[Section VI - Trade Secrets - Draft#E. Synthesis: conditional protection under enterprise frameworks]]

---

## III. ECONOMIC FOUNDATION

### A. Investment and Skill Requirements

**Non-Intuitive Expertise:**
- Oppenlaender research: effective prompting requires understanding model architectures, training methodologies, systematic experimentation
- Distinct from ordinary language use
- Technical knowledge of capabilities, limitations, failure modes
- Link: [[Section II - Economic Foundation - Draft#A. Investment and skill requirements]]

**Three Investment Forms:**

1. **Training Costs:**
   - Backgrounds required: NLP, machine learning, computational linguistics
   - Coursera certifications: 20-40 hours structured instruction
   - Educational investment precedes productive work
   - Link: [[Section II - Economic Foundation - Draft#A. Investment and skill requirements]]

2. **Iterative Development:**
   - McKinsey: 1.5-2.5x faster completion with "effective prompting techniques incorporating context, constraints, and iterative refinement"
   - Productivity gains require optimization investment
   - Not merely submitting initial queries
   - Link: [[Section II - Economic Foundation - Draft#A. Investment and skill requirements]]

3. **Institutional Knowledge:**
   - Specialized prompts embed domain expertise
   - Pharmaceutical example: chemical structure knowledge, regulatory requirements, research literature familiarity
   - Integration represents substantial development investment
   - Distinct from general-purpose AI usage
   - Link: [[Section II - Economic Foundation - Draft#A. Investment and skill requirements]]

### B. Commercial Value and Market Evidence

**Four Evidence Categories:**

**1. Marketplace Transactions:**
- PromptBase: 370,000+ users, 220,000+ prompts
- Prices: $1.99-$9.99
- 24,000+ five-star reviews = sustained commercial activity
- Direct proof of buyer-perceived value
- Commodity-level rather than premium valuation
- Link: [[Section II - Economic Foundation - Draft#B. Commercial value and market evidence]]

**2. Labor Market Valuations:**
- Glassdoor (August 2025): $123,803 average annual salary
- Typical range: $96,661-$160,352
- Entry-level: $98,214; Senior: $128,090
- Outliers: $335,000 for specialized hybrid roles (Anthropic SF)
- Comparable to software development/data science
- Link: [[Section II - Economic Foundation - Draft#B. Commercial value and market evidence]]

**3. Productivity Measurements:**
- McKinsey: $2.6-$4.4 trillion annual global economic potential (2.6-4.4% of GDP)
- Developers: 1.5-2.5x faster task completion with AI tools
- GitHub Copilot: 56% faster completion
- Prompt engineering explicitly identified as determinant of outcome quality
- Additional 1.5-2.5x improvement with effective prompting vs. suboptimal approaches
- Link: [[Section II - Economic Foundation - Draft#B. Commercial value and market evidence]]

**4. Enterprise Competitive Advantage:**
- Legal analytics: €2.3M investment over 18 months
- Documented development costs creating economic value
- Competitors could misappropriate by copying vs. independent investment
- Link: [[Section II - Economic Foundation - Draft#B. Commercial value and market evidence]]

### C. Appropriability Concerns

**Zero Marginal Cost Reproduction:**
- Once disclosed, instantly copyable at no cost
- PromptBase acknowledges: "different users may receive same or substantially similar outputs"
- Non-exclusivity inherent to product category
- Link: [[Section II - Economic Foundation - Draft#C. Appropriability concerns and the free-riding problem]]

**Free-Riding Problem:**
- Competitors can appropriate without incurring development costs
- Rational actors will under-invest and wait to copy
- Classic appropriability failure: social returns exceed private returns
- Arrow (1962): traditional economic justification for IP protection
- Link: [[Section II - Economic Foundation - Draft#C. Appropriability concerns and the free-riding problem]]

**Reverse Engineering:**
- Recent research: reconstruct from as few as 5 outputs
- Black-box, zero-shot methods
- Minimal investment required
- Information lacks durability and excludability of protectable IP
- Link: [[Section II - Economic Foundation - Draft#C. Appropriability concerns and the free-riding problem]]

### D. Countervailing Concerns

**1. Monopolization Risks:**
- Exclusive rights could enable strategic behavior restricting AI access
- Protection for common tasks = rent extraction
- Tax on AI utilization rather than reward for innovation
- Frischmann & Lemley: infrastructure goods and access concerns
- Link: [[Section II - Economic Foundation - Draft#D. Countervailing concerns: monopolization risks and complexity spectrum]]

**2. Labor-Versus-Asset Distinction:**
- Economic value concentrates in human expertise
- Prompt engineering as professional skill
- Labor markets compensate through salaries
- No licensing markets emerged (3 years of intensive adoption)
- No IP litigation over prompts
- No regulatory recognition
- Market participants perceive prompts as service outputs, not proprietary assets
- Link: [[Section II - Economic Foundation - Draft#D. Countervailing concerns: monopolization risks and complexity spectrum]]

**3. Complexity Spectrum:**
- Bimodal distribution
- Simple prompts: $1.99 commodity valuation
- Sophisticated prompts: months of optimization, documented investment
- Legal frameworks should distinguish, not treat uniformly
- Link: [[Section II - Economic Foundation - Draft#D. Countervailing concerns: monopolization risks and complexity spectrum]]

**Conclusion:**
- Prompt engineering generates measurable value through productivity gains
- Commands professional-tier compensation for skilled labor
- Does NOT establish individual prompts as high-value IP assets
- Value in outcomes enabled and expertise required
- NOT in prompts as tradeable assets with independent economic standing
- Link: [[Section II - Economic Foundation - Draft]]

---

## IV. CROSS-CUTTING THEMES

### Theme 1: Instructions vs. Expression

**Fundamental Distinction:**
- Prompts specify ideas about what to create
- Do not embody expression of creative works
- Copyright protects expression, not ideas
- Trade secrets can protect ideas/methods if secret
- But prompts' instructional nature pervades all analysis
- Links: Copyright sections, Trade secrets commercial value

### Theme 2: Functional Constraint

**Pervasive Limitation:**
- Copyright: functional purpose defeats originality (BSA, Brompton)
- Trade secrets: functional specifications may lack independent value
- Economic: effectiveness requirements constrain formulation
- Purpose dictates form across all legal regimes
- Links: Copyright originality, Trade secrets commercial value

### Theme 3: Complexity Spectrum

**Differential Treatment Required:**
- Copyright: simple and complex prompts both fail (different reasons)
- Trade secrets: simple fail all elements, sophisticated can potentially qualify
- Economic: bimodal distribution requires targeted protection
- One-size-fits-all approach inappropriate
- Links: All copyright subsections, Trade secrets synthesis, Economic countervailing concerns

### Theme 4: Third-Party Disclosure

**Unique Challenge:**
- Cloud AI architecture requires provider disclosure
- Copyright: not directly relevant (protection independent of disclosure)
- Trade secrets: creates fundamental doctrinal tension
- Resolved through contractual protections, but demanding
- Links: Trade secrets secrecy element

### Theme 5: Investment ≠ Protectability

**Persistent Misconception:**
- Copyright: Football Dataco rejects sweat-of-the-brow
- Investment alone insufficient without originality
- Trade secrets: documented investment supports commercial value element
- But must still satisfy secrecy and reasonable steps
- Economic: investment demonstrates value but not protectability
- Links: Copyright counterarguments, Trade secrets commercial value, Economic investment section

---

## V. PRACTICAL IMPLICATIONS

### For Simple/Intermediate Prompts

**Copyright:** Categorically fail protection across all grounds

**Trade Secrets:**
- Simple: fail all three elements
- Intermediate: likely fail proportionality under reasonable steps
- No viable protection route

**Business Strategy:**
- Accept no protection
- Focus on continuous improvement and speed-to-market
- Build value through service/expertise, not asset ownership

### For Sophisticated Prompts

**Copyright:** Still fail protection despite investment/complexity

**Trade Secrets:** Conditional protection possible IF:
- Exclusive use of enterprise AI services
- Documented contractual confidentiality protections
- Comprehensive legal/organizational/technical measures
- Substantial documented investment
- Quantified competitive advantages

**Business Requirements:**
- Prohibit consumer AI services
- Require enterprise-tier services with verified contractual protections
- Implement three-level protection framework (legal, organizational, technical)
- Document everything
- Train employees
- Monitor and enforce compliance
- Prepare for potential transparency obligations (GDPR, AI Act)

**Risk Assessment:**
- Protection demanding: significant infrastructure investment
- Protection contested: divergent national approaches create cross-border uncertainty
- Protection provisional: no CJEU interpretation yet
- Regulatory transparency may require disclosure despite trade secrecy

---

## VI. OPEN QUESTIONS REQUIRING RESOLUTION

### CJEU Interpretation Needed

**Directive 2016/943 for Algorithmic Information:**
- Whether third-party disclosure with contractual safeguards satisfies secrecy
- Whether "reasonable steps" accommodates cloud architecture necessity
- Harmonization of divergent national approaches (German proportionality vs. Dutch stringency vs. French procedures)
- Links: Trade secrets synthesis, unresolved tensions

### AI Act Transparency Intersection

**Trade Secrets vs. Regulatory Transparency:**
- When do transparency obligations override trade secret protection?
- How to implement Dun & Bradstreet case-by-case balancing for AI Act compliance?
- Need Commission guidance or judicial decisions
- Links: Trade secrets synthesis, AI Act discussion

### Reform Considerations

**Legislative Amendments:**
- Should Directive 2016/943 be amended to address cloud computing specifically?
- Should prompts receive sui generis protection regime?
- Policy trade-offs: incentivizing investment vs. monopolization risks
- Links: Economic countervailing concerns, trade secrets unresolved tensions

---

**Document Version:** 1.0 (2025-11-14)
**Total Arguments Mapped:** 50+ key doctrinal points
**Total Obsidian Links:** 150+ internal references
**Coverage:** Comprehensive across all IP regimes analyzed in article
