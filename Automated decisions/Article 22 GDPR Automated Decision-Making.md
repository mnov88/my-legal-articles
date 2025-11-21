# Article 22 GDPR: Automated Decision-Making and the Right Not to Be Subject to Automated Decisions

The right not to be subject to automated decisions under Article 22 GDPR represents a cornerstone of data protection law in the age of algorithmic governance. Following the landmark CJEU judgments in SCHUFA Holding (C-634/21, December 2023) and Dun & Bradstreet Austria (C-203/22, February 2025), this provision has evolved from an ambiguous safeguard into a robust prohibition with far-reaching implications for AI systems, profiling, and automated processing across all sectors. This comprehensive synthesis examines how courts, regulators, and scholars interpret each doctrinal element of Article 22, revealing both consensus and persistent tensions in the law's application.

## Understanding the core prohibition and its architecture

Article 22(1) GDPR establishes that **data subjects have the right not to be subject to decisions based solely on automated processing, including profiling, which produce legal effects or similarly significantly affect them**. The CJEU in SCHUFA conclusively settled a fundamental interpretative debate: this is a general prohibition requiring one of three narrow exceptions, not merely a right requiring individual invocation. As the Court stated, "Article 22(1) establishes a prohibition in principle, the infringement of which does not need to be invoked individually by the data subject." This interpretation, endorsed by EDPB guidelines and academic consensus, transforms Article 22 from a passive right into an active constraint on automated decision-making systems.

The provision contains four paragraphs creating a comprehensive regulatory framework. Article 22(2) establishes three exceptions: contractual necessity, authorization by law with suitable safeguards, or explicit consent. Article 22(3) mandates minimum safeguards including rights to human intervention, expressing views, and contesting decisions. Article 22(4) imposes enhanced restrictions when special category data is processed. This architecture reflects legislative intent to balance innovation with fundamental rights protection, requiring meaningful human oversight of significant automated decisions while enabling beneficial automation under controlled conditions.

## What constitutes an "automated decision" under Article 22

### CJEU's expansive interpretation in SCHUFA

The SCHUFA judgment revolutionized understanding of what constitutes a "decision" for Article 22 purposes. SCHUFA Holding AG, a German credit reference agency, argued that its credit scoring activities were merely "preparatory acts" since third-party banks made the ultimate lending decisions. The CJEU rejected this narrow interpretation, holding that **the concept of "decision" is "broad enough to encompass the result of calculating a person's creditworthiness in the form of a probability value"** when that value significantly influences downstream decisions.

The Court established a crucial test: where personal data is transmitted to a third-party controller and "the latter, in accordance with consistent practice, draws strongly on that value for its decision on the establishment, implementation or termination of a contractual relationship," Article 22 applies to the score generator, not just the final decision-maker. This reasoning expands Article 22's scope dramatically—automated outputs that substantially influence decisions, even when technically advisory, can constitute Article 22 decisions if they determinatively shape outcomes. The Court noted that where insufficient credit scores lead "in almost all cases" to loan refusal, the scoring mechanism itself becomes the operative decision.

### EDPB framework for decisions

EDPB guidelines define automated decision-making as "the ability to make decisions by technological means without human involvement." Decisions encompass measures, evaluations, and determinations that produce effects on individuals. The guidelines emphasize three ways profiling may be used: general profiling, decision-making based on profiling, and solely automated decision-making including profiling (Article 22[1] cases). Crucially, **automated decisions can be made with or without profiling; profiling can take place without making automated decisions**—they are related but distinct concepts.

EDPB provides concrete examples of Article 22 decisions: automatic refusal of online credit applications, e-recruiting without human intervention, automated benefit eligibility determinations, algorithmic fraud detection affecting service access, and automated insurance pricing. The guidance emphasizes that decisions can be based on data provided directly by individuals, observed about them, or derived through profiling.

### Academic debates on "decision" scope

Academic literature reveals a fundamental split on how broadly "decision" should be construed. **Broad interpretation advocates** (Bygrave, Davis & Schwemer, Brkan, Malgieri) argue that restrictive readings would enable circumvention through human "rubber-stamping" and that Article 22 must capture recommendations, scores, and assessments that effectively determine outcomes. Bygrave warns against "all dressed up but nowhere to go" syndrome where overly narrow interpretation renders the provision ineffective.

**Narrow interpretation proponents** (Hintze, Wong) contend scope should be "quite narrow, limited to those solely automated decisions where a legal or similarly significant effect is an inherent and direct result." They argue broad readings impose inefficiency and reduce accuracy by forcing unnecessary human review of beneficial automation. Wong specifically argues most personalized pricing and marketing decisions lack sufficient directness to qualify.

The SCHUFA judgment largely validates the broad interpretation school, though questions remain about multi-stage decision-making, selective automation, and preparatory analytics that inform but don't determine decisions. Binns and Veale identify five complications: selective automation (some users get human review), staged significance (different stages have different effects), compound effects (multiple small decisions aggregate), contingent automation (automation contingent on screening), and outcome selectivity (human review only for certain outcomes).

### National DPA applications

National DPAs have applied expansive "decision" interpretations in enforcement. The Italian Garante in Deliveroo (€2.5M fine) found that **automated rider ranking determining shift access constituted Article 22 decisions** because the algorithm controlled work opportunities and income potential. The ranking wasn't merely advisory—it operationally determined which riders received booking priority, making it the substantive decision about access to work.

Similarly, Spanish AEPD enforcement established that automated profiling for marketing or service allocation can constitute decisions when they materially affect individuals' access to services or opportunities. German DPAs have emphasized that algorithmic models producing outputs that decisively influence contractual relationships fall within Article 22 even when labeled "recommendations."

The Hamburg DPA explicitly stated post-SCHUFA that **AI systems creating a basis for preliminary decisions can qualify as Article 22 decision-making if they play a decisive role**, particularly when outputs rest on barely comprehensible AI-developed criteria. This interpretation signals that sophisticated machine learning systems generating influential predictions or classifications will increasingly be scrutinized under Article 22.

## The "solely automated" processing requirement

### EDPB's meaningful human involvement standard

The "solely" qualifier creates Article 22's most contested boundary. EDPB guidelines establish that "based solely on automated processing" means **"no human involvement in the decision process."** However, the guidelines immediately qualify this: controllers cannot avoid Article 22 by "fabricating human involvement." Token gestures, routine application of automated profiles without actual influence, and rubber-stamping do not constitute meaningful involvement.

EDPB specifies that **meaningful human involvement requires:** (1) authority and competence to change the decision; (2) thorough assessment of all relevant data; (3) consideration of additional information provided by the data subject; and (4) genuine discretion, not mere parameter-setting or system oversight. The guidelines provide a key example: if an automated process produces a recommendation and a human reviews and takes account of other factors in making the final decision, that decision is not "based solely" on automated processing.

The guidance warns against automation bias—the demonstrated human tendency to defer uncritically to algorithmic outputs. Bygrave identifies this as a foundational concern: "one of the 'fears' that underpinned drafting of Article 15(1) DPD [Article 22's predecessor] was that increasing automatization propagates automatic acceptance of validity and concomitant reduction in human decisional responsibilities."

### Spanish AEPD's four-factor framework

Spanish AEPD developed the most sophisticated framework for assessing meaningful human involvement in March 2024 guidance responding to SCHUFA. The **four-factor test** requires:

**1. Competence**: The human reviewer must have authority/task enabling alteration of the algorithmic outcome, not merely power to execute or communicate it.

**2. Preparation/Training**: Ability to critically evaluate the decision requires understanding system capabilities, limitations, potential biases, and relevant domain knowledge.

**3. Independence/Diligence**: Freedom from organizational pressures to accept automated outputs; absence of "authority bias" where humans defer to perceived algorithmic expertise.

**4. Means to Exercise Competence**: This encompasses procedural ability (timing to intervene at appropriate stage), informational access (database, factors, criteria, contextual data), resources (analytical tools, support team), and sufficient time per decision.

The Spanish framework includes practical feasibility calculations. For instance, if a human reviews 100 automated reports of 100 pages daily, this yields only 21 pages per minute—physically impossible to conduct meaningful assessment. Similarly, decisions about flight boarding or event access occurring in seconds lack procedural feasibility for human intervention.

### Academic consensus and outliers

Scholarly consensus strongly endorses the meaningful involvement standard. Brkan advocates a "non-strict concept of 'solely' automated decisions"—the provision applies even with nominal human involvement lacking real discretion. The Future of Privacy Forum's empirical analysis of 70+ court and DPA decisions found that **enforcement authorities examine the entire organizational environment**: structure, reporting lines, training programs, actual discretion exercised, quality and timing of human involvement, and whether humans can only rubber-stamp or can meaningfully intervene.

Malgieri emphasizes controllers cannot avoid Article 22 by having humans "merely rubber-stamp machine-based decisions, without actual authority or competence to alter their outcome." Kaminski and Malgieri propose multi-layered accountability frameworks linking individual rights to systemic governance through Data Protection Impact Assessments.

Outliers exist in some Member State interpretations. Sweden historically treated Article 22 as requiring active data subject invocation rather than automatic application. Belgian law imposes an absolute prohibition on discriminatory profiling based on special categories, stricter than GDPR's Article 22(4) permission with safeguards.

### Enforcement examples illuminating the boundary

The German Berlin DPA's €300,000 fine against a bank provides concrete guidance. The bank's algorithm rejected a credit card application despite a good credit score. When the applicant requested explanation, the bank refused to disclose decision-making factors. The DPA found violations of Articles 5(1)(a), 15(1)(h), and 22(3), establishing that **meaningful human involvement requires documented consideration of individual circumstances beyond algorithmic outputs**.

Italian Garante enforcement against Deliveroo and Foodinho/Glovo (€2.5M+ fines) found that automated rider ranking systems without human override constituted solely automated processing. The algorithms tracked location every 12 seconds, processed availability and reliability data, and determined booking priority—all without human review of individual rider circumstances or ability to contest algorithmic determinations.

ICO provides practical examples distinguishing sufficient human involvement: a factory worker's pay linked to automatically monitored productivity without human assessment is solely automated; an HR manager reviewing automated attendance data alongside other factors before issuing warnings is not. The key distinction is whether humans exercise genuine discretion or merely communicate algorithmic determinations.

## "Legal effects" and "similarly significant effects" thresholds

### EDPB's two-tier framework

EDPB guidance establishes a **two-tier analysis** for Article 22's effects requirement. **Legal effects** present a clearer standard—processing affecting legal rights, status, or contractual entitlements. Examples include contract cancellation, denial of statutory social benefits (child or housing benefit), refused country admission or citizenship denial, and subjection to increased security measures by authorities.

**Similarly significant effects** require contextual, case-by-case assessment. EDPB defines the threshold: "effects of the processing must be sufficiently great or important to be worthy of attention." The decision must have potential to (1) significantly influence circumstances, behavior, or choices; (2) have prolonged or permanent impact; or (3) lead to exclusion or discrimination. Recital 71 provides paradigmatic examples: automatic online credit refusal and e-recruiting without human intervention.

EDPB emphasizes effects must be **more than trivial** but need not be catastrophic. The guidance examines targeted advertising with nuance. Most targeted advertising—"women in Brussels aged 25-35 interested in fashion"—does not significantly affect individuals. However, factors can elevate advertising to significance: intrusiveness of profiling (tracking across sites/devices), exploitation of known vulnerabilities (targeting financially distressed individuals with high-interest loans), and differential pricing that effectively bars access to goods or services.

### CJEU's broad interpretation in SCHUFA

The SCHUFA judgment adopted an expansive view of significant effects. The Court held that credit scores affect data subjects "at the very least significantly" because insufficient scores lead "in almost all cases" to loan refusal. This **probabilistic causation standard**—where automated outputs highly correlate with but don't absolutely determine outcomes—suffices for Article 22 application.

The judgment's significance extends beyond credit scoring. As the Hamburg DPA noted, the reasoning applies to **any AI-based decision-making system producing outputs that substantially influence access to contracts, services, employment, or benefits**. The Court's focus on practical effects rather than formal decision-making authority expands Article 22's protective reach.

### Academic frameworks for threshold assessment

The Future of Privacy Forum synthesized enforcement patterns into a **multi-dimensional test** for similarly significant effects:

**Categories of personal data**: Decisions based on behavioral inferences, sensitive inferences, or special category data more likely to have significant effects than those based on factual transactional data.

**Immediate consequences**: Direct, tangible impacts (denied credit, refused employment) weigh more heavily than speculative future effects.

**Temporal dimension**: Permanent or prolonged effects (blacklisting, long-term reputational damage) exceed temporary impacts (single ad exposure).

**Impact on conduct/choices**: Decisions substantially constraining options or forcing behavioral changes (inability to access essential services) carry greater significance.

**Financial impact**: Quantifiable monetary loss or income opportunity deprivation (reduced work allocation in gig economy).

**Limitation of opportunities**: Systematic disadvantage in accessing employment, credit, education, or housing.

**Vulnerable populations**: Children, workers, benefit recipients, and other power-imbalanced groups receive enhanced protection; lower thresholds apply.

Malgieri and Comandé argue significant effects "can encompass marketing manipulation, price discrimination" even absent formal legal effects. Brkan emphasizes that **decisions affecting vulnerable groups warrant heightened scrutiny**—employment algorithmic management, benefit allocation, and educational opportunities present inherently significant contexts.

Conversely, skeptics like Hintze and Wong contend most marketing and pricing decisions lack sufficient significance. Wong argues personalized pricing should require "substantial, demonstrable impact" rather than speculative harm. Hintze advocates for "inherent and direct" effects, excluding attenuated or cumulative impacts.

### National DPA threshold variations

National DPA enforcement reveals **inconsistent thresholds**, particularly for marketing and advertising. Italian Garante applies a relatively low threshold in employment contexts—algorithmic ranking determining work access constitutes significant effects given economic dependence. The Deliveroo decision found that automated allocation affecting riders' ability to "book" shifts and earn income met the threshold, even though riders retained theoretical autonomy to reject assignments.

ICO guidance emphasizes financial circumstances, health, reputation, and employment opportunities as core significant effect categories. ICO examples clarify boundaries: **automatic credit refusal and e-recruiting decisions clearly qualify; TV program recommendations clearly do not**. The middle ground—targeted advertising, personalized pricing, content moderation—requires contextual analysis.

Spanish AEPD found in one case that energy company marketing profiling did **not** reach Article 22 thresholds, while in others, automated service access decisions and employment-related processing did. French CNIL emphasizes that significant effects "influence environment, behavior, choices" or "result in discrimination."

Irish DPC's Meta decisions sidestepped the significant effects question for behavioral advertising, focusing instead on the lawful basis issue. This leaves unresolved whether personalized ad delivery based on extensive profiling produces "similarly significant effects"—a critical question given online advertising's ubiquity.

Dutch AP's approach to government algorithmic processing (SyRI case) found discrimination based on dual nationality violated fairness principles even without established Article 22 violation, demonstrating that **Article 5(1)(a) fairness provides protection when Article 22 thresholds aren't met**.

## Article 22(2) exceptions: contract necessity, legal authorization, and explicit consent

### Narrow interpretation imperative

EDPB guidance and scholarly consensus converge: **Article 22(2) exceptions must be interpreted strictly** to preserve the prohibition's protective effect. Brkan memorably characterizes the provision as "Swiss cheese with giant holes"—the exceptions risk swallowing the prohibition if construed broadly.

### Exception 1: Contractual necessity [Article 22(2)(a)]

EDPB establishes a **necessity test**: "the controller must be able to show that this type of processing is necessary, taking into account whether a less privacy-intrusive method could be adopted." Controllers must demonstrate that "the main subject-matter of the specific contract cannot, as a matter of fact, be performed if the specific processing does not occur."

The guidelines provide contrasting examples. **Permitted**: A business receiving tens of thousands of job applications may use fully automated screening to create a shortlist where it's "not practically possible" to manually review all applications. **Prohibited**: An online retailer completing a sale requires processing payment and delivery information, but profiling the user's lifestyle choices based on website visits is not "necessary" for contract performance, even if mentioned in fine print.

This narrow standard received reinforcement from **Irish DPC's Meta decisions** (€390M combined fines). The DPC held that **behavioral advertising cannot rely on contractual necessity**—personalized ad delivery is not objectively necessary for social media contract performance. This interpretation substantially restricts Article 22(2)(a) for online platforms, requiring reliance on consent or legal authorization instead.

German DPAs apply particularly strict standards in employment contexts, with some indicating that automated recruiting requires **consent** rather than contractual necessity. The rationale: power imbalances in employment relationships make contractual necessity claims suspect; job applicants and workers cannot meaningfully refuse automated processing if it's framed as contractually necessary.

### Exception 2: Legal authorization [Article 22(2)(b)]

Union or Member State law may authorize Article 22 processing, but such law must "lay down suitable measures to safeguard the data subject's rights and freedoms and legitimate interests." EDPB guidance specifies this requires legislative acts specifically contemplating automated decision-making, not general grants of administrative authority.

Recital 71 provides examples: monitoring and preventing fraud and tax evasion, and ensuring security and reliability of controller-provided services. **Required safeguards in authorizing law** must include rights to human intervention, expressing views, and contesting decisions.

Academic debate centers on what constitutes sufficient legislative authorization. Swedish scholars question whether general administrative procedure laws suffice or whether specific ADM-contemplating provisions are required. The SCHUFA judgment deferred to national courts to determine whether German Federal Data Protection Act Section 31 (governing credit scoring) constitutes compatible legal authorization under Article 22(2)(b).

**National legislative supplements** demonstrate varied approaches. Spanish Royal Decree Law 9/2021 creates specific obligations for gig economy algorithmic management, requiring worker representatives to be informed about algorithms and AI use. French law (Article L. 311-3-1 Code on Relations between Public and Administration) establishes a specific regime for administrative automated decisions, requiring controllers to ensure algorithmic processing is under control and to provide detailed, intelligible explanations. German BDSG Section 37 contains specific provisions for automated decisions in employment and insurance. Belgian law imposes an **absolute prohibition** on profiling leading to discrimination based on special categories, exceeding GDPR minimum standards.

These national elaborations reflect recognition that Article 22(2)(b)'s "legal authorization" exception requires **sector-specific legislative consideration** of automated decision-making risks and appropriate safeguards, not blanket administrative authority.

### Exception 3: Explicit consent [Article 22(2)(c)]

Article 22 requires **explicit consent**, a higher standard than Article 6(1)(a)'s general consent. EDPB explains: "The term explicit refers to the way consent is expressed by the data subject. It means the data subject must give an express statement of consent." Written statements or express electronic confirmation (clicking "I consent to automated credit decisions") meet this standard; pre-ticked boxes and inferred consent do not.

**Consent must be informed**, meaning "data subjects should have enough relevant information about the envisaged use and consequences to ensure consent represents an informed choice." Controllers must explain exactly what automated decision-making will occur, what data will be used, what effects may result, and what safeguards apply.

Italian Supreme Court case law establishes that **consent is invalid if the individual is subjected to an ADM system influencing rights when inadequately informed about the logic behind it**. This creates a potential circularity: meaningful consent requires understanding the system, but understanding requires information often claimed as trade secrets.

Critical scholarly perspectives emphasize that **consent in power-imbalanced contexts is problematic**. Aza (2024) argues "given the imbalance of power in the employment relationship, consent is not a suitable legal ground for automated decision-making in algorithmic management." Similarly, benefit recipients, tenants, and other vulnerable populations cannot "freely" consent when alternatives are unavailable.

CNIL clarifies that while "explicit consent" need not be "in writing," controllers bear the burden of proving consent was freely given, specific, informed, and unambiguous. Irish DPC guidance emphasizes consent for Article 22 processing must be **granular**—distinct from general terms of service acceptance—and not bundled with acceptance of essential services.

## Article 22(3) safeguards: human intervention, expressing views, and contesting decisions

### Minimum mandatory safeguards

Article 22(3) establishes that when Article 22(2) exceptions permit automated decision-making, controllers "shall implement suitable measures to safeguard the data subject's rights and freedoms and legitimate interests, **at least** the right to: (1) obtain human intervention on the part of the controller; (2) express his or her point of view; and (3) contest the decision."

EDPB emphasizes these are **minimum safeguards**—the "at least" language indicates controllers must implement additional measures appropriate to processing risks. The guidelines specify that human intervention review "must be carried out by someone who has the appropriate authority and capability to change the decision. The reviewer should undertake a thorough assessment of all relevant data, including any additional information provided by the data subject."

### The "right to explanation" controversy

The existence and scope of a **right to explanation** represents Article 22's most contested doctrinal question. The CJEU in Dun & Bradstreet Austria (C-203/22, February 2025) provided definitive clarification. The Court held that **Article 15(1)(h) GDPR affords data subjects a right to explanation of automated decision-making** sufficient to enable them to understand and challenge decisions.

The Court established that **if individuals affected by automated decisions cannot understand the reasons leading to decisions before expressing views or contesting them, Article 22(3) rights would not satisfy their protective purpose**. The judgment links Articles 15(1)(h) and 22(3) functionally: access to meaningful information about logic is instrumental to effectively exercising contestation rights.

Recital 71 provides textual support: "data subjects should have a right to obtain an explanation of the decision reached after such assessment." The CJEU confirmed this creates an obligation, not merely an aspiration. Controllers must describe **procedures and principles actually applied** such that data subjects understand which personal data were used and how they were used in automated decision-making.

The Court specified that **"meaningful information" requires**:
- Categories of data used in the decision-making process
- Why these categories are considered pertinent
- How profiles are built (including statistical methods)
- Why profiles are relevant to automated decision-making
- How they are used for decisions concerning the data subject
- Extent to which variations in personal data would lead to different results

Critically, the CJEU held that **meaningful information does not require disclosure of complex algorithms, mathematical formulas, or source code**. The Advocate General in Dun & Bradstreet reasoned that such technical disclosures would be "hardly understandable to the average data subject" and thus wouldn't satisfy transparency objectives. Instead, controllers must provide high-level, individualized explanations of factors affecting specific decisions.

The judgment resolves a longstanding academic debate. **Pro-explanation scholars** (Malgieri & Comandé, Brkan, Selbst & Powles, Kaminski) argued that systemic interpretation of Articles 13-15, 22, and Recital 71 supports a robust right to explanation necessary for meaningful contestation and preventing discrimination. **Anti-explanation scholars** (Wachter, Mittelstadt & Floridi) contended recitals aren't legally binding and only limited informational rights exist, with full explanations technically infeasible and not textually required.

The CJEU synthesis adopts a middle position: explanations are required, but must be **intelligible and useful for contestation** rather than technically exhaustive. Malgieri and Comandé's "legibility test" aligns with this approach—focusing on understanding architecture and implementation rather than mathematical precision.

### Additional safeguards beyond Article 22(3) minima

EDPB guidelines detail additional safeguards controllers should implement:

**Regular quality assurance**: "Controllers should carry out frequent assessments on data sets to check for bias, and develop ways to address prejudicial elements, including over-reliance on correlations."

**Algorithmic auditing**: "Testing algorithms and ML systems to prove they perform as intended, not producing discriminatory, erroneous, or unjustified results."

**Data minimization**: Clear retention periods for profiles and personal data; using anonymization or pseudonymization.

**Error prevention**: "Appropriate procedures and measures to prevent errors, inaccuracies, or discrimination on the basis of special category data, used cyclically throughout the profiling lifecycle."

**Transparency**: Data subjects must fully understand how decisions are made to challenge them effectively. Complexity is no excuse—Recital 58 states transparency is "of particular relevance where proliferation of actors and technological complexity makes it difficult for data subjects to know whether, by whom, and for what purpose data is collected."

ICO provides implementation details: controllers should establish simple ways to request human intervention, explain review processes at the point of decision, maintain audit trails showing key decision points, explain why alternatives weren't preferred, provide clear appeals processes with stated grounds, and conduct regular checks that systems work as intended.

### National DPA enforcement of safeguards

The **German Berlin DPA €300k case** (May 2023) represents rare Article 22(3)-specific enforcement. The bank was required to provide: specific information on the database used, decision-making factors, criteria for rejection in individual cases, and meaningful explanation about logic. The decision establishes that **general, boilerplate explanations are insufficient**—individualized information explaining the specific rejection is required.

Italian Garante's **Deliveroo enforcement** (€2.5M) included Article 22 violations for failing to implement measures to verify algorithm correctness and accuracy, prevent errors and discrimination, and provide meaningful information on logic, importance, and expected consequences. The decision emphasized that **algorithmic systems affecting work access require robust safeguards including transparency, accuracy verification, and contestability mechanisms**.

Spanish AEPD requires that explanations include not just logic but also **importance and consequences with examples**. Abstract statements about scoring methodology are inadequate; controllers must provide tangible examples of how factors influence decisions and what consequences result.

Belgian DPA's **IAB Europe decision** (€250k) included findings that failure to conduct Data Protection Impact Assessments for profiling/automated decision-making frameworks violates accountability obligations. This establishes **DPIAs as essential safeguards** for Article 22 processing, not merely recommended best practices.

## Relationship between Article 22, profiling (Article 4(4)), and AI systems

### Conceptual distinctions and overlaps

Article 4(4) GDPR defines **profiling** as "any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements."

EDPB emphasizes that **profiling and automated decision-making are related but distinct**. Three elements define profiling: (1) automated processing, (2) of personal data, (3) to evaluate personal aspects of natural persons. Profiling can create profiles used later for decisions (sequential) or directly feed into decision-making (integrated).

The guidelines establish **three regulatory frameworks**:

**1. Solely automated decision-making with legal/similarly significant effects** (Article 22): Subject to prohibition with three narrow exceptions; requires specific safeguards including human intervention rights.

**2. Decision-making based on profiling (not solely automated)**: Subject to general GDPR provisions (lawfulness, fairness, transparency, purpose limitation, data minimization); right to object under Article 21 may apply; no Article 22 prohibition but enhanced transparency required.

**3. General profiling**: All GDPR principles apply; specific transparency requirements under Articles 13(2)(f) and 14(2)(g); data minimization and purpose limitation particularly important.

This taxonomy matters because **not all profiling triggers Article 22**. A retailer profiling customers to predict purchasing preferences for inventory management engages in profiling but may not make decisions that legally or significantly affect individuals. Conversely, automated decisions can occur without profiling—a speed camera issuing tickets performs automated decision-making without evaluating personal aspects beyond violation occurrence.

### AI and machine learning systems

EDPB acknowledges that "advances in technology and capabilities of big data analytics, artificial intelligence and machine learning have made it easier to create profiles and make automated decisions with potential to significantly impact rights and freedoms." The guidance recognizes AI presents unique challenges: "growth and complexity of machine-learning can make it challenging to understand how automated decision-making or profiling works."

**Inference of special category data** represents a critical AI-specific concern. EDPB warns: "profiling can create special category data by inference from data which is not special category in its own right but becomes so when combined. For example, food shopping records combined with nutritional data can infer health status." The guidance cites research showing Facebook "likes" plus limited survey information predicted male sexual orientation 88% accurately, ethnic origin 95%, and religious affiliation 82%.

When AI systems infer sensitive attributes, controllers face compounded obligations: they must identify lawful basis for processing special category data under Article 9, ensure processing remains compatible with original purpose, inform data subjects about processing, and comply with Article 22(4)'s enhanced restrictions.

**Requirements for AI/ML systems under GDPR**:
- All general GDPR principles apply (lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity/confidentiality, accountability)
- **Accuracy concerns are heightened** due to predictive elements and potential training data bias
- Regular testing and auditing required to verify systems perform as intended
- Cannot invoke trade secrets as blanket excuse to deny transparency
- Must conduct DPIAs for systematic and extensive profiling (Article 35(3)(a))
- Must implement data protection by design and by default (Article 25)

National DPA guidance emphasizes AI-specific requirements. German DPAs mandate **"intervenability"**—user-accessible options to question or override AI results. Spanish AEPD focuses on ensuring humans reviewing AI outputs have sufficient training to understand capabilities, limitations, and potential biases—not merely technical operation but substantive domain knowledge enabling critical assessment.

### Multi-stage and selective automation challenges

Binns and Veale identify five complications Article 22 faces with complex AI systems:

**Selective automation**: Some users receive human review while others receive fully automated decisions. Does Article 22 apply to the subset receiving automated treatment, even if the system could provide human review?

**Staged significance**: Different processing stages have different effects. Initial automated screening may lack significant effects, but aggregate processing produces them. When does Article 22 obligation arise?

**Compound effects**: Multiple small automated decisions (content recommendations, feed curation, notification timing) aggregate to significance. Does Article 22 apply to the system as a whole?

**Contingent automation**: Automation contingent on initial human or automated screening. If only applicants failing automated screening receive human review, is the screening itself an Article 22 decision?

**Outcome selectivity**: Human review only for certain outcomes (e.g., only denials reviewed, not approvals). Does this constitute sufficient human involvement?

These complications remain largely unresolved in CJEU case law. Binns and Veale argue Article 22 requires examining **entire decision-making chains**, not isolated stages, to determine whether individuals are meaningfully protected.

## Special protection for children and vulnerable groups

### Children under Recital 71

Recital 71(5) states: "Such measure should not concern a child." This language creates interpretative tension—it appears in a recital (non-binding) rather than Article 22's operative text, and uses "should not" rather than "shall not."

EDPB position: "Given this wording is not reflected in the Article itself, WP29 does not consider this represents an absolute prohibition on processing in relation to children. However, **in light of this recital, WP29 recommends that, as a rule, controllers should not rely upon Article 22(2) exceptions to justify it**."

The guidance elaborates: "Because children represent a more vulnerable group, organisations should, in general, refrain from profiling them for marketing purposes. Children can be particularly susceptible in the online environment and more easily influenced by behavioural advertising."

EDPB acknowledges exceptional circumstances: "There may be some circumstances in which it is necessary to carry out solely automated decision-making in relation to children, for example to protect their welfare." If permitted, **enhanced safeguards** are mandatory to effectively protect children's rights, freedoms, and legitimate interests.

### Vulnerable groups more broadly

While GDPR doesn't explicitly define "vulnerable groups" beyond children, EDPB guidance and enforcement patterns establish that **power imbalances and susceptibility warrant enhanced protection**:

**Workers and job seekers**: Spanish Rider Law, German DPA positions on automated recruiting, and Italian Garante gig economy enforcement demonstrate that employment-related automated decision-making receives heightened scrutiny. Aza argues that "given imbalance of power in employment relationships, consent is not a suitable legal ground for automated decision-making in algorithmic management."

**Benefit recipients**: Dutch AP and CNIL emphasize that government benefit allocation involves significant power asymmetry. Automated systems determining eligibility for social security, housing assistance, or healthcare access affect individuals with limited alternatives and thus warrant rigorous safeguards.

**Financially vulnerable individuals**: EDPB uses the example of "someone known or likely to be in financial difficulties who is regularly targeted with adverts for high-interest loans" as requiring protection. Targeting vulnerable populations with exploitative products can constitute "similarly significant effects" even where general marketing would not.

**Elderly and disabled persons**: While less developed in enforcement, academic literature and some national guidance suggest these groups warrant enhanced protection given potential susceptibility to manipulation and limited ability to understand or contest algorithmic decisions.

The unifying principle: **where power imbalances exist or individuals have heightened susceptibility, Article 22 thresholds should be lower and safeguards stronger**.

## Comprehensive synthesis: How doctrinal elements are evaluated across sources

### Convergence and consensus

Several doctrinal elements show remarkable convergence across CJEU, EDPB, academics, and national DPAs:

**1. Article 22(1) as prohibition**: Universal agreement post-SCHUFA that Article 22 establishes a general prohibition, not merely a right requiring invocation.

**2. Meaningful human involvement requirement**: Consensus that rubber-stamping is insufficient; humans need authority, competence, training, and genuine discretion.

**3. Narrow interpretation of exceptions**: Contractual necessity and legal authorization should be construed strictly to preserve the prohibition's protective effect.

**4. Trade secrets not absolute**: Trade secret claims cannot be blanket justifications to deny transparency; individualized balancing required.

**5. Multi-layered accountability**: Agreement that Article 22 protection requires combination of individual rights (transparency, contestation) and systemic governance (DPIAs, auditing, bias testing).

**6. Purpose is fundamental rights protection**: Universal recognition that Article 22 aims to protect human dignity, autonomy, and prevent discrimination in an age of algorithmic governance.

### Persistent divergences and unresolved questions

Despite substantial consensus, critical tensions remain:

**"Similarly significant effects" threshold**: National DPAs apply inconsistent standards, particularly for marketing and personalized pricing. Italian Garante applies relatively low thresholds in employment; ICO applies higher thresholds for commercial contexts; Irish DPC left behavioral advertising significance largely unresolved.

**Scope of "decision" in multi-stage systems**: While SCHUFA established that intermediate outputs can be decisions, questions remain about preparatory analytics, recommendations that weakly influence outcomes, and selective/contingent automation.

**Content of "meaningful information"**: Dun & Bradstreet provides guidance but practical implementation remains contested. How detailed must explanations be? What level of individualization is required? Can standardized templates ever suffice?

**Role of legitimate interests balancing**: Tension exists between Article 6(1)(f) legitimate interests assessments and Article 22 protections. Some argue legitimate interests can't authorize Article 22 processing; others contend it provides flexibility for beneficial automation.

**Public sector vs. private sector standards**: Should government algorithmic decision-making face stricter standards given democratic accountability and fundamental rights implications? Some national laws (France, Netherlands) suggest yes; GDPR itself doesn't differentiate.

**Temporal and geographic scope**: When do processing activities occurring partly in third countries fall under Article 22? How does Brexit affect UK-EU coordination? These remain partially resolved.

## Application to hypothetical: AI summarization in public consultation

### Factual scenario analysis

The hypothetical presents: An individual submits input to a public consultation on granting a power plant concession. The input is "principally broadly assessed by the awarding authority without being a decisive factor." The authority uses **AI to summarize stakeholder inputs** and **skips/omits a relevant input** that may have led to refusal to grant the concession.

### Doctrinal analysis by element

#### 1. Is this an "automated decision"?

**Arguments this IS an automated decision (SCHUFA reasoning)**:

**Broad interpretation of "decision"**: Following SCHUFA, the "decision" is not limited to the formal concession award. The AI summarization that **omits the individual's input** constitutes a preparatory decision with downstream effects. CJEU held that automated outputs significantly influencing later decisions can themselves be Article 22 decisions.

**Determinative effect**: If the omitted input "may have led to refusal," the AI's choice to exclude it substantially influenced the concession decision. The authority "draws strongly" on the AI summary in its deliberations, analogous to how banks relied on SCHUFA scores.

**Measure affecting data subject**: Recital 71 states decisions include "measures" affecting individuals. The AI summarization is a measure that evaluates and classifies inputs, determining which receive consideration and which are filtered out.

**Purposive interpretation**: Article 22 aims to protect individuals from algorithmic processes that materially affect them without human oversight. An AI system that gates information reaching decision-makers by selecting which inputs merit inclusion serves this gatekeeping function algorithmically.

**Arguments this is NOT an automated decision (narrow interpretation)**:

**Ultimate human decision-making**: The concession authority makes the final decision after reviewing the summary. Humans consider multiple factors beyond stakeholder input. The AI merely assists information processing.

**Preparatory/advisory nature**: Unlike SCHUFA where scores were nearly determinative, here inputs are "not decisive factors." The AI summarization is genuinely preparatory, with substantial human discretion remaining.

**No profiling of data subject**: Article 22 targets decisions about individuals based on evaluation of their personal aspects. The AI here processes **content of submissions**, not personal characteristics of submitters. The omission stems from content filtering, not personal profiling.

**Indirect effects**: The individual isn't directly subjected to a decision by the AI. The decision is about the concession, not about the individual. Effects on the individual are attenuated—their interest in concession refusal is indirect.

**SYNTHESIS**: Under **SCHUFA's expansive approach**, strong arguments exist that AI summarization omitting material inputs constitutes an automated decision-making process within Article 22's scope, particularly if the omission was based on algorithmic evaluation. However, the **lack of profiling** (evaluating personal characteristics rather than submission content) and the **indirect nature of effects** on the individual create substantial uncertainty.

#### 2. Is it "solely" automated?

**Arguments for solely automated processing**:

**AI performs selection without human review**: If the AI summarizes by selecting representative inputs or filtering "less relevant" submissions without human verification of excluded material, the exclusion decision is wholly automated.

**Automation bias risk**: Even if humans review the summary, they may uncritically accept its completeness without examining omitted inputs, exhibiting the automation bias Article 22 guards against.

**No meaningful human involvement in omission**: While humans make the final concession decision, they don't exercise meaningful discretion about the **omission itself**—they aren't aware the input was excluded or why.

**Arguments against solely automated processing**:

**Human decision-making on concession**: Humans review the summary and make the ultimate decision considering numerous factors. This human involvement in the final decision may be deemed "meaningful."

**Human parameter-setting**: If humans established criteria for summarization, selected relevant topics, or reviewed draft summaries, some human involvement exists in the process.

**Concession as ultimate decision**: Focusing on the concession award as "the decision" rather than the summarization, there is clear human involvement—the authority's deliberations, stakeholder consultations, technical assessments, and policy considerations.

**SYNTHESIS**: Whether processing is "solely automated" depends critically on what constitutes "the decision." If we focus on the **omission of the individual's input**, strong arguments exist that this was solely automated—the AI decided which inputs to include/exclude without meaningful human review of filtered content. However, if we focus on the **concession decision**, human involvement is substantial, making Article 22 inapplicable. Spanish AEPD's framework suggests humans would need **means** to identify omitted inputs (access to raw data), **competence** to evaluate summarization accuracy, and **training** to recognize AI limitations—likely absent in typical scenarios.

#### 3. Does it produce "legal effects" or "similarly significant effects"?

**Arguments for legal/similarly significant effects**:

**Legal effects on concession outcome**: The concession grant/denial creates legal rights and obligations. If the omitted input would have led to refusal, the AI's omission materially affected a legal decision.

**Deprivation of procedural rights**: Public consultations often provide legal or quasi-legal participatory rights. Omitting an input deprives the individual of their right to be heard—itself potentially a legal effect.

**Environmental/health impacts**: If the individual's concern related to environmental harm or health risks from the power plant, their interest in the decision has significant personal implications—health, property values, quality of life.

**Democratic participation rights**: EU law recognizes rights to public participation in environmental decision-making (Aarhus Convention). Algorithmic exclusion from consideration affects these fundamental participatory rights.

**Arguments against legal/similarly significant effects**:

**Effects on third party**: The decision is about the concession holder (electricity company), not the individual consultant. Effects on the individual are indirect—they hoped to influence an outcome but have no legal entitlement to particular decision.

**Inputs not decisive**: The hypothetical states any input "could be meaningless." If consultation inputs are generally non-determinative, the omission lacks significance.

**No personal evaluation**: Article 22 protects against automated personal evaluations. Here, the AI evaluates submission content, not personal aspects of the submitter. The individual isn't profiled, scored, or ranked.

**Diffuse public interest**: Many individuals share interest in concession outcomes. The effect on any single consultant is diffuse and shared among a community rather than individualized.

**Minimal threshold not met**: Under FPF's framework, effects would need to be "more than trivial." Influencing a regulatory decision as one of many consultants may not exceed this threshold.

**SYNTHESIS**: This presents the **most uncertain element**. Arguments exist that **democratic participatory rights** and potential environmental/health impacts create "similarly significant effects," particularly if the individual can demonstrate concrete interests (property ownership near plant, health conditions affected by emissions). However, the **indirect nature** of effects—affecting a third-party decision rather than a direct decision about the individual—and the **lack of personal profiling** create substantial doubt about meeting Article 22 thresholds. The case is **stronger** if: (1) the individual has concrete legal/proprietary interests affected by the concession; (2) the consultation process provides legally protected participatory rights; (3) the omission resulted from algorithmic assessment of the submitter's characteristics (e.g., scoring credibility based on past participation) rather than content assessment.

#### 4. Does AI summarization constitute the kind of processing Article 22 regulates?

**Core purpose alignment analysis**:

Article 22 aims to protect individuals from automated processing that evaluates their personal characteristics to make decisions significantly affecting them. The paradigmatic cases involve credit scoring, employment screening, benefit eligibility, fraud detection—automated assessments **of individuals** determining their access to opportunities.

The consultation scenario differs: the AI processes **content submissions** to synthesize information for decision-makers. The processing evaluates **what was said**, not **who said it**. This resembles automated content moderation, search engine results, or information retrieval systems more than classical Article 22 scenarios.

**EDPB guidance** emphasizes Article 22 applies to processing that "evaluates personal aspects relating to natural persons." If the AI summarization evaluates **relevance, representativeness, or significance of submissions** based on content rather than author characteristics, it may fall outside Article 22's core concern.

However, if the AI system incorporates **any profiling elements**—weighting inputs based on submitter credibility, past participation, demographic characteristics, or inferred expertise—the processing moves toward Article 22's target. The omission of an input "which may have led to refusal" suggests the AI made a **salience determination** that could implicate Article 22 if that determination involved any assessment of the submitter.

#### 5. Counterarguments and complexities

**The "right to be forgotten" in decision-making**:

An intriguing parallel exists with CJEU's right to be forgotten case law. If individuals have rights to have inaccurate or outdated information excluded from processing, do they have rights to have **relevant** information included? The omission in this scenario creates a completeness problem—the authority's decision rests on incomplete information due to algorithmic filtering.

**Transparency and accountability gaps**:

Even if Article 22 doesn't apply, **fairness and transparency principles** under Article 5(1)(a) may be violated. If the authority uses AI summarization without transparency about filtering methods, accuracy limitations, or omission rates, this may breach general GDPR obligations even absent Article 22 violation.

**Article 21 right to object**:

The individual may have rights under Article 21 to object to processing on grounds of their particular situation, separate from Article 22. If the processing significantly affects their interests, Article 21(1) may provide recourse.

**Procedural due process beyond GDPR**:

Administrative law principles of procedural fairness, right to be heard, and reasoned decision-making may provide **stronger protections** than GDPR in public consultation contexts. The omission may violate administrative procedure requirements regardless of GDPR application.

**Sectoral legislation (Aarhus Convention)**:

The Aarhus Convention and EU implementing legislation (Directive 2003/35/EC, Public Participation Directive) provide specific rights to public participation in environmental decision-making. Algorithmic processing that undermines these rights may violate sectoral law even if GDPR Article 22 doesn't apply.

**Emerging AI Act requirements**:

The EU AI Act classifies systems used in public administration affecting fundamental rights as "high-risk." AI systems used in consultation processes affecting environmental or public health decisions may face **specific requirements** for human oversight, transparency, and accuracy under the AI Act, providing complementary protection to GDPR.

**Cumulative effects and systemic concerns**:

While a single omission may lack significant effects, **systematic algorithmic filtering** of consultation inputs could aggregate to significant democratic participation concerns. If AI summarization routinely omits certain viewpoints, stakeholder categories, or substantive concerns, the cumulative effect becomes significant even if individual omissions don't.

### Conclusion on hypothetical

**Most likely outcome**: This scenario **does not cleanly fit Article 22's scope** under current interpretation, primarily because:

1. **Lack of personal profiling**: The AI processes submission content rather than evaluating personal aspects of the submitter
2. **Indirect effects**: Effects on the individual are mediated through influence on a third-party decision
3. **Significant human involvement**: The concession decision involves substantial human deliberation beyond the AI summary

**However, several factors could bring it within Article 22**:

1. **If the AI incorporated any submitter profiling** (credibility scoring, weighting by demographics/expertise)
2. **If the consultation provides legally protected participatory rights** that the omission violated
3. **If the individual has concrete legal/proprietary interests** in the decision outcome
4. **If CJEU extends SCHUFA reasoning** to encompass information gatekeeping that substantially influences downstream decisions

**Alternative GDPR protections likely apply**:

- **Article 5(1)(a) fairness**: Algorithmic omission of relevant inputs may violate fairness principles
- **Articles 13-14 transparency**: The authority must inform consultants about AI use in processing submissions
- **Article 21 objection rights**: The individual may object to processing on grounds of their particular situation
- **Article 35 DPIA**: AI systems processing consultation inputs affecting public decisions may require DPIAs
- **Accountability (Article 5(2))**: The authority must be able to demonstrate appropriate AI system governance

**Broader legal landscape**:

Even if Article 22 doesn't apply, the scenario raises serious concerns under **administrative law** (procedural fairness, right to be heard), **environmental law** (Aarhus Convention public participation rights), and emerging **AI Act** requirements for high-risk systems in public administration. The most effective legal challenge would likely invoke this **constellation of protections** rather than relying exclusively on GDPR Article 22.

**Practical recommendations**:

Authorities using AI in consultation processes should:

1. **Maintain full transparency** about AI use, methods, and limitations
2. **Implement human verification** that AI summaries accurately represent input diversity
3. **Provide access** to all submissions, not just AI-selected representative samples
4. **Document** that all substantive viewpoints received consideration
5. **Enable challenges** to summary accuracy or completeness
6. **Conduct DPIAs** assessing risks of algorithmic filtering to democratic participation

This case illustrates Article 22's **boundaries**—while not every algorithmic process affecting individuals falls within its scope, the provision's purposive interpretation post-SCHUFA expands protection beyond narrow classical scoring scenarios. The consultation hypothetical sits in the **grey zone** where Article 22 may not directly apply but its principles and complementary GDPR provisions create meaningful obligations for algorithmic transparency and accountability in public decision-making.