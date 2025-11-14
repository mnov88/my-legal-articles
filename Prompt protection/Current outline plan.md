Detailed Section Plan
I. Introduction [800 words]
Three prompt examples (simple/intermediate/complex)
Research question: Does EU IP law protect prompts?
Why it matters: PromptBase market data, prompt engineering salaries
Scope: EU IP frameworks (copyright, software/database, patents, trade secrets)
Methodology: Doctrinal analysis, CJEU case law
Roadmap
Links: [[00 Prompt protection questions]], [[README 1]]
II. Economic Foundation [1,000 words - TIGHTENED]
Keep essential justifications only:

Investment & skill (300 words)
Non-intuitive skill (Oppenlaender study)
Training costs, iterative development
Commercial value (300 words)
PromptBase: 370k users, 220k prompts
Labor market: $100k-$335k salaries
Enterprise competitive advantage
Appropriability concerns (200 words)
Zero marginal cost copying
Free-riding problem
Countervailing concerns (200 words)
Monopolization risks
Complexity spectrum matters
Links: [[Economic value of prompts#Marketplace evidence]], [[Economic value of prompts#Labor market signals]], [[Economic value of prompts#Conspicuous absences]]
III. Copyright Protection [3,000 words - EXPANDED]
A. The Harmonized Originality Standard [800 words]
Article 1(3) Software Directive, InfoSoc Directive 2001/29
Five cumulative requirements:
Author's own intellectual creation
Reflects author's personality (Painer)
Free and creative choices (Painer)
Technical constraints defeat originality (BSA, Brompton)
Expression not ideas (Infopaq, SAS Institute)
Cofemel consolidation
Links: [[Copyright - Claude#The harmonized originality test]]
B. Application to Simple Prompts [500 words]
Examples: "Summarize," "Create cat image"
Fails multiple elements:
No free/creative choices beyond necessary words
Doesn't reflect personality
Is the idea not expression
Infopaq principle: "words as such" not protected
Links: [[Copyright - Claude#Application of the originality test to AI prompts]]
C. Application to Complex Prompts [700 words]
Example: 400-word system prompt with parameters
Greater labor investment BUT faces three obstacles:
Instructions problem: Describes what to create (idea), not expression itself
Functional constraints: Purpose dictates form (BSA principle applies)
Merger concerns: Limited ways to express instructions
Detailed analysis of each obstacle
Links: [[Copyright - Claude#Application of the originality test to AI prompts]]
D. The Idea-Expression Dichotomy [600 words]
Core copyright principle: ideas never protected
Prompts specify ideas about desired outputs
Protecting prompts = protecting ideas
CJEU emphasis: BSA §49, Software Directive Art 1(2)
Distinguishing expression vs instruction
Links: [[Copyright - Claude#The harmonized originality test]]
E. Scholarly Consensus [300 words]
Professor He (GRUR International): "merely unprotectable ideas"
Gervais & Hugenholtz (Kluwer Copyright Blog): "dangerously close to owning the underlying idea"
Quintais & Hugenholtz: technical constraints leave no creative freedom
Sampaio: prompts not code (non-deterministic)
Links: [[Copyright - Claude#Scholarly consensus]]
F. Exceptional Cases [100 words]
Very rare: Prompts as independent literary works
Protection of text itself, not functional use
Embedded in software as component
Does not disturb general conclusion
Links: [[Copyright - Claude#Potential exceptions]]
IV. Software & Database Protection [1,200 words]
A. Software Directive 2009/24/EC [700 words]
Definition: "computer programs" includes preparatory design
CJEU interpretation:
BSA: GUIs not programs (user-facing elements)
SAS Institute: functionality, programming language not protected
Sony: RAM data not program expression
Application to prompts:
Not source/object code
Input to programs, not programs themselves
Describe functionality (what), not implementation (how)
Preparatory design material:
Requires "quasi-coding" specificity
Must lead to program at later stage
Prompts lack technical specificity
Non-deterministic (Sampaio argument)
Links: [[Copyright - Claude#Protection under the Software Directive]]
B. Database Directive 96/9/EC [500 words]
Two protections: copyright (selection/arrangement), sui generis (investment)
Copyright for databases:
Requires originality in selection/arrangement
Individual prompts: too minimal
Prompt libraries: possible but protection limited
Sui generis right:
Substantial investment in obtaining/verifying/presenting
Protects against extraction/reutilization
Doesn't prevent independent creation
BHB v William Hill: no protection for created data
Conclusion: Individual prompts unprotected; collections might qualify with limited scope
Links: Synthesize from copyright analysis
V. Patents [600 words - MINIMAL]
A. Patentability Requirements
EPC Article 52: inventions in all fields of technology
Technical character requirement
Excluded: programs as such, presentation of information, mental acts
B. Why Prompts Don't Qualify
Abstract ideas, not technical implementations
Linguistic formulations, not technological solutions
No technical effect beyond normal computer operation
Analogy: Business methods unpatentable unless technical contribution
T 0258/03 Hitachi: further technical effect required
C. Brief Conclusion
Patents not viable protection route
Academic consensus: prompts lack technical character
Move to trade secrets as potential avenue
Links: Brief synthesis, no detailed link needed
VI. Trade Secrets [3,000 words - STREAMLINED BUT COMPREHENSIVE]
A. Directive 2016/943 Framework [400 words]
Article 2(1) three-part cumulative test
TRIPS Art 39 implementation
Legislative history: Commission 2013 proposal → 2016 adoption
Policy balance: protection vs. mobility/innovation/competition
Article 3: lawful acquisition (independent discovery, reverse engineering)
Links: [[Trade secrets - Claude#The three-part test]]
B. Element 1: Secrecy + Cloud Disclosure Paradox [900 words]
The problem: Cloud AI requires transmitting prompts to providers
Doctrinal issue: Third-party disclosure = "readily accessible"?
National court guidance:
Germany: NDAs essential (Higher Regional Court Düsseldorf 2021)
Netherlands: Sharing without NDAs fails (District Court 2018)
France: Third-party disclosure defeats protection (Paris CA 2022)
Application to prompts:
Consumer-tier: OpenAI free, Google free tier = training use = fails secrecy
Enterprise-tier: Azure, AWS Bedrock, Anthropic = contractual confidentiality = may preserve secrecy
Bright-line rule: Only enterprise services with NDAs can potentially satisfy
Links: [[Trade secrets - Claude#Secrecy defeated by disclosure]], [[Trade secrets Perplexity]]
C. Element 2: Commercial Value [600 words]
The challenge: Value from AI model or prompt itself?
Arguments against: Model dependency (prompt worthless without GPT-4 access)
Arguments for:
Marketplace evidence (PromptBase prices)
Quantified benefits (60% faster drug identification)
Investment costs (€2.3M documented)
Compilation analogy (customer lists)
Causal test: Would disclosure harm competitive position?
Distinction: Simple prompts fail; sophisticated prompts with documented investment pass
Links: [[Trade secrets - Claude#The puzzle of commercial value]], [[Economic value of prompts]]
D. Element 3: Reasonable Steps [700 words]
National frameworks:
Germany: Legal + organizational + technical measures; nine-factor proportionality
France: Specific identification required, documented measures
Netherlands: "Policy without practice fails"
The structural challenge: Cloud requires disclosure to function
Comprehensive protection framework required:
Legal: Enterprise services + NDAs + contractor agreements
Organizational: Access controls + classification + training + monitoring
Technical: Encryption + sanitization + authentication
Proportionality analysis: If use requires third-party processing, assess relative to that constraint
Conclusion: Contractual protections + internal controls can satisfy reasonable steps
Links: [[Trade secrets - Claude#Reasonable steps in tension]]
E. Counterarguments [500 words]
Reverse engineering: 5-output reconstruction techniques (2024 research)
Structural impossibility: Cloud architecture incompatible with exclusive control
Independent discovery: Low barriers, high probability
Each counterargument assessed
Links: [[Trade secrets - Claude#Counterarguments]]
F. CJEU Guidance: Dun & Bradstreet [300 words]
Case C-203/22 (27 Feb 2025)
GDPR transparency vs trade secret for algorithms
Holding: Algorithmic info can be trade secrets, case-by-case balancing
Application to prompts: In principle protectable, subject to transparency obligations
Links: [[Trade secrets - Claude#Resolution]]
G. Trade Secrets Synthesis [600 words]
Three categories:
Simple prompts: Fail all elements
Intermediate prompts: Likely fail proportionality
Sophisticated prompts: Can potentially qualify IF comprehensive measures
Conditions for protection:
Enterprise services exclusively
Documented investment
Comprehensive legal/organizational/technical program
Quantified competitive advantages
Unresolved tensions:
No CJEU interpretation yet
Cross-border uncertainty (German vs Dutch vs French approaches)
AI Act transparency intersection unclear
Conclusion: Theoretically possible, demanding in practice, provisional pending CJEU
Links: [[Trade secrets - Claude#Resolution]], [[Trade secret Gemini]], [[Trade secrets Perplexity]]
VII. Conclusion [800 words]
A. Synthesis by Regime [300 words]
Copyright: Generally fails (instructions/ideas, not expression)
Software/Database: Not programs; collections potentially protected with limits
Patents: Lacks technical character
Trade secrets: Narrow conditional protection possible for sophisticated prompts
B. The Core Doctrinal Problem [200 words]
Prompts = instructions about what to create (ideas)
IP law protects expression/implementation, not ideas
Fundamental tension across all regimes
C. Practical Guidance [200 words]
For businesses: Trade secret route only viable option
Requires enterprise services + comprehensive measures
Simple/intermediate prompts: Accept no protection
Focus protection efforts on sophisticated prompts with documented value
D. Open Questions [100 words]
CJEU interpretation needed (Directive 2016/943)
AI Act transparency vs trade secrets
Cross-border harmonization
Reform considerations
Implementation Notes
Obsidian linking syntax: [[filename#Heading]] for each key point
Preserve CJEU case analysis from v1.1 in copyright section
Trade secrets: Use comprehensive analysis from Trade secrets - Claude.md but streamline
Economic foundation: Extract tight version from Economic value of prompts.md
OSCOLA footnoting: Maintain throughout
Word count flexibility: Copyright can breathe to 3200-3500 if material justifies