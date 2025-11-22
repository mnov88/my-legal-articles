# Algorithmic Gatekeeping in the Administrative State: AI-Assisted Processing of Public Consultation Submissions Under GDPR Article 22

## Abstract

The digitisation of public administration has precipitated a fundamental shift in the mechanics of participatory democracy. Confronting an unprecedented volume of digital feedback, public authorities increasingly deploy artificial intelligence—particularly Large Language Models and natural language processing tools—to aggregate, summarise, and filter public consultation submissions. This technological transition introduces algorithmic gatekeeping into the heart of democratic deliberation, raising urgent questions under the General Data Protection Regulation. This article provides a comprehensive doctrinal analysis of whether such "upstream" AI filtering constitutes automated decision-making prohibited under Article 22 GDPR. Drawing on the Court of Justice's landmark *SCHUFA* judgment (C-634/21) and its recent *Dun & Bradstreet Austria* ruling (C-203/22), alongside national enforcement decisions from Berlin, Austria, and France, the analysis demonstrates that the "determining role" doctrine has substantially expanded the legal definition of automated decision-making. The conventional administrative defence—that AI tools merely serve as preparatory aids for human decision-makers—is no longer legally robust. When AI systems filter, prioritise, or suppress submissions based on sentiment, stance, or quality metrics, they function as *de facto* decision-makers regarding the admissibility of citizen input. This article argues that without rigorous "human-in-the-loop" architectures and specific legislative authorisation, the deployment of AI filtering in public consultations presents significant risk of infringing Article 22, Article 9 (special category data), and the fundamental right to good administration enshrined in the Charter of Fundamental Rights.

---

## I. Introduction

The contemporary administrative state faces a dual crisis of capacity and legitimacy. The ease of digital communication has enabled mass participation in public consultations, generating volumes of submissions that frequently exceed the cognitive processing capacity of civil servants. Yet the imperative to maintain democratic responsiveness demands that these submissions receive meaningful consideration. To bridge this gap, public authorities have become early adopters of artificial intelligence technologies, deploying systems ranging from basic spam filters to advanced generative AI summarisers.[^1] These tools promise to synthesise millions of disparate citizen inputs into actionable policy insights, ostensibly enhancing the efficiency of notice-and-comment procedures.

However, the deployment of such technologies introduces opacity into democratic deliberation. When an algorithm determines which comments are "substantive" and which constitute "noise," it exercises a form of power distinct from traditional bureaucratic discretion. This power operates invisibly, upstream of final policy decisions, and often without the procedural safeguards characteristic of administrative law.[^2] The legal framework governing this technological shift is anchored in the General Data Protection Regulation,[^3] specifically Article 22, which grants data subjects the right not to be subject to decisions based solely on automated processing, including profiling, which produce legal effects or similarly significantly affect them.

While Article 22 was drafted primarily with private sector applications in mind—credit scoring and e-recruiting figure prominently in Recital 71—its application to public administration creates complex interpretive challenges.[^4] The core tension lies between administrative necessity and the prohibition of automated decisions affecting fundamental rights. Recent jurisprudence from the Court of Justice, particularly the *SCHUFA* judgment,[^5] has significantly altered the landscape of automated decision-making law. By establishing that a preparatory automated score can constitute a "decision" if it plays a determining role in the final outcome, the Court has cast doubt on the legality of many "human-in-the-loop" systems deployed in public administration.

This article examines the legality of AI filtering through the lens of this evolving jurisprudence. The analysis proceeds both descriptively—mapping current legal requirements onto consultation filtering practices—and normatively, arguing that algorithmic gatekeeping in democratic deliberation engages fundamental rights protections that cannot be subordinated to administrative convenience.

The methodological approach combines doctrinal analysis of primary sources (GDPR text, CJEU case law, national DPA decisions, EDPB guidance) with functional analysis of AI systems' actual operation. Legal conclusions depend on factual predicates about how AI filtering works in practice. Scholars and practitioners have sometimes discussed Article 22 in abstracted terms divorced from technological reality; this article grounds legal analysis in technical understanding of natural language processing, sentiment analysis, and large language model operation.

Part II analyses the technical mechanisms of AI filtering and their mapping onto legal concepts. Part III addresses the threshold question of what constitutes "solely automated" processing, examining the collapse of the human-in-the-loop defence after *SCHUFA*. Part IV considers whether information gatekeeping constitutes a justiciable "decision" under Article 22. Part V examines the "legal effects" and "similarly significant effects" thresholds in administrative contexts, with particular attention to participatory rights under the Aarhus Convention. Part VI analyses whether sentiment analysis and stance detection constitute prohibited profiling of special category data. Part VII assesses the adequacy of existing administrative law frameworks as safeguards under Article 22(2)(b). Part VIII considers the interplay with the AI Act. The article concludes with recommendations for compliant deployment of AI in public consultations.

A preliminary note on scope is warranted. This article focuses on EU law, specifically GDPR and the AI Act, with reference to Member State administrative law frameworks where relevant. Consultation filtering raises analogous issues under other legal frameworks—the US Administrative Procedure Act's notice-and-comment requirements, constitutional free speech protections, and emerging AI governance frameworks globally. While comparative analysis exceeds this article's scope, the EU framework's influence on global data protection norms suggests that conclusions reached here may have broader implications for democratic governance in an algorithmic age.

---

## II. The Technical and Legal Anatomy of AI Filtering

Understanding the legal implications requires first dissecting the technical mechanisms of AI filtering and their correspondence to legal concepts. The use of AI in public consultations spans a spectrum of automated processing activities, each carrying distinct legal risks.

### A. Taxonomy of AI Interventions

Public authorities utilise various AI techniques to manage submission volumes. These can be categorised by function and potential impact on data subjects.

**Deduplication** employs similarity pipelines to identify identical or near-identical text, grouping mass campaigns or petitions into single entries.[^6] Where limited to exact matches with human review of the consolidated entry, such processing likely falls outside Article 22's scope. The processing does not constitute profiling if it evaluates textual similarity rather than personal aspects of the submitter.

**Spam and toxicity filtering** deploys classifiers trained on datasets of spam or harmful speech to block or hide submissions deemed irrelevant or abusive.[^7] This processing carries significant Article 22 risk: rejection of input constitutes a determination on admissibility, with direct effects on the data subject's participatory rights.

**Sentiment analysis** uses natural language processing models to score text polarity.[^8] This processing evaluates the data subject's attitudes and opinions—"personal aspects" within Article 4(4) GDPR's definition of profiling. Where submissions concern matters of public policy, sentiment analysis risks processing special category data revealing political opinions under Article 9.

**Stance detection** employs supervised learning models to classify positions toward specific policy proposals.[^9] This constitutes profiling of political opinions with heightened risk where used to filter "outliers" or minority views.

**Summarisation** through generative models compresses large text volumes into executive summaries, necessarily involving editorial decisions about inclusion and exclusion.[^10] The omission of nuances or minority viewpoints from summaries presented to human decision-makers constitutes an automated determination of relevance with indirect but potentially decisive effects. This risk is particularly acute with large language models, which may exhibit statistical biases favouring dominant viewpoints or mainstream expression while marginalising unconventional perspectives. Where summarisation shapes the "reality" presented to policymakers, its editorial function cannot be dismissed as merely technical.

**Prioritisation and ranking** through relevance scoring orders submissions for human review, with those ranked lower receiving less attention or none at all.[^10a] Even without outright exclusion, deprioritisation can effectively silence voices: if reviewers examine only the top-ranked 10% of submissions, those in the bottom ranks are functionally excluded. The criteria determining rank—often opaque combinations of multiple signals—determine whose voices are amplified and whose are muted.

### B. The Upstream Character of Filtering

In network engineering, "upstream filtering" refers to blocking traffic before it reaches end-users. In administrative contexts, AI operates as an upstream filter for policymakers: submissions constitute "traffic," and civil servants the "end-users."[^11]

The legal significance of upstream filtering lies in its invisibility. Unlike a rejected credit application where the applicant receives notification, a filtered consultation submission simply disappears from the administrative record. The submitter receives no rejection notice; the submission is technically "received" by the server but procedurally ineffective upon arrival. This structural opacity distinguishes consultation filtering from more visible forms of automated decision-making.

Consider the contrast with traditional administrative refusals. When a planning application is rejected, the applicant receives a decision letter explaining grounds for refusal and avenues of appeal. When a benefits claim is denied, the claimant receives notice and reasons. These procedural protections—fundamental to administrative law across jurisdictions—are entirely absent where AI filtering operates upstream. The citizen's submission vanishes into digital silence, generating neither acknowledgment nor explanation. This creates circumstances where the "decision" to exclude the citizen is made solely by software, frequently without the knowledge of the human authority nominally responsible for the consultation. This structural opacity directly engages the "solely automated" prong of Article 22.

The European Data Protection Board's guidance on automated decision-making emphasises that the right under Article 22 exists precisely because of the risks inherent in allowing machines to make significant decisions about individuals without human oversight.[^12] Where the human decision-maker operates on a dataset already curated by AI—never seeing filtered submissions—the protective purpose of Article 22 is directly implicated.

---

## III. The "Solely Automated" Threshold and Meaningful Human Intervention

The first critical question concerns when processing is "solely automated" under Article 22(1). Administrative bodies routinely defend AI deployment by citing human involvement: because human officials ultimately approve policy documents or review aggregated reports, they argue the process is not *solely* automated.[^13] Rigorous analysis of CJEU jurisprudence and EDPB guidelines reveals this defence as increasingly porous.

### A. The Rubber-Stamping Phenomenon

Article 22(1) applies only where there is no human involvement in decision-making. However, regulatory guidance consistently holds that such involvement must be "meaningful" rather than a "token gesture."[^14] The Article 29 Working Party, in its guidelines on automated decision-making (now endorsed by the EDPB), specified that meaningful human intervention requires the human actor to have both the *authority* and *competence* to change the decision, and to actually exercise this authority.[^15]

In high-volume filtering contexts, the rubber-stamping phenomenon is acute. If an AI system flags 10,000 submissions as "spam" or "non-substantive," and a human officer approves this classification in bulk without reviewing individual contents, human involvement is merely nominal. Research into automation bias confirms that humans are cognitively predisposed to trust automated outputs, particularly under time pressure or when dealing with massive datasets.[^16]

The Berlin Data Protection Authority's 2023 enforcement action against a bank illustrates this principle in practice. The authority imposed a €300,000 fine where automated credit card rejection occurred without meaningful explanation, notwithstanding nominal human involvement.[^17] The authority emphasised that when controllers employ automated decision-making tools, they bear specific transparency obligations under Article 22(3) requiring "concrete information about the database used, the factors and the criteria influencing the decision."

Where standard administrative procedure involves trusting AI filter classifications, the process is *de facto* solely automated. The EDPB has clarified that controllers cannot fabricate human involvement to avoid Article 22 provisions.[^18] If human review merely validates algorithmic output in "almost all cases," the decision remains solely automated in the eyes of the law.

### B. The SCHUFA Doctrine: The Determining Role Test

The CJEU's *SCHUFA* ruling provides the decisive analytical framework.[^19] The case concerned credit scoring algorithms used by SCHUFA, a credit reference agency. Banks argued that SCHUFA did not make automated decisions because human employees made final lending determinations. The Court rejected this characterisation.

The Court held that automated score generation constitutes a "decision" under Article 22 where it plays a "determining role" in downstream decisions. Three cumulative conditions must be met for Article 22(1) to apply: a decision must exist; that decision must be based solely on automated processing; and it must produce legal effects or similarly significantly affect the data subject.[^20]

Crucially, the Court reasoned purposively: interpreting Article 22 to require the final formal act to be automated would enable controllers to circumvent GDPR protections by inserting a human intermediary.[^21] If circumvention through a "human straw man" were permitted, Article 22 would be deprived of practical effect. This reasoning has direct implications for consultation filtering.

Applying the *SCHUFA* framework to public consultations:

| Element | SCHUFA Case | Public Consultation | Legal Consequence |
|---------|-------------|---------------------|-------------------|
| Automated Input | Probability score generated by SCHUFA | Relevance/Toxicity score generated by AI filter | Both serve as primary heuristics for human decision-makers |
| Human Actor | Bank employee granting loan | Civil servant drafting policy summary | Human actor relies on automated input to manage complexity |
| Process Logic | Low score → rejection in almost all cases | "Toxic" tag → exclusion in almost all cases | Automated classification predetermines outcome |
| Information Gap | Bank cannot explain score; SCHUFA claims trade secrets | Civil servant cannot explain LLM reasoning; vendor claims IP | "Lacuna in legal protection" if Article 22 doesn't apply |

Where an AI filter's classification of a submission as "irrelevant" leads to its exclusion from policy deliberation in essentially all cases, the AI has played a determining role. The filter *is* the decision-maker regarding that citizen's participatory access.

### C. The Upstream Trap

The *SCHUFA* doctrine is even more potent where rejected content is never presented to humans. In *SCHUFA*, bank employees at least saw scores and applications. In AI-moderated consultations, if systems auto-archive comments flagged as "abusive" without human queue review, the determining role is absolute. Human policymakers remain unaware that decisions have been made to exclude specific feedback.

This creates a paradox: administration claims a human made the decision (the policy), but the dataset underlying that decision was curated solely by AI. The upstream decision to exclude specific citizens from the dataset was solely automated, and under *SCHUFA*, this upstream determination is justiciable under Article 22.

The Austrian Data Protection Authority's decision in *DSB 2020-0.436.002* reinforces this analysis.[^22] Addressing marketing score calculation, the authority held that Article 15(1)(h)'s right to meaningful information applies to "all profiling activities," not merely those falling within Article 22(1) and (4). The authority specified that information must include: parameters and input variables; their effect on scoring; explanation of why the data subject received particular results; and possible profile categories—or equivalent information enabling exercise of rectification and erasure rights. Critically, the authority rejected trade secret arguments, holding that rights under Articles 8 ECHR and 8 CFR cannot be subordinated to commercial confidentiality.

### D. The Dutch Authority's Perspective on Meaningful Intervention

The Dutch Data Protection Authority (Autoriteit Persoonsgegevens) has provided particularly detailed guidance on what constitutes "meaningful human intervention."[^22a] In its 2025 consultation document, the authority identified several "red flags" indicating that nominal human involvement fails the meaningful intervention standard:

- The human reviewer merely clicks "approve" on algorithmically-generated outputs;
- Review occurs but the reviewer "can only reject in exceptional cases";
- The reviewer lacks access to input data or decision logic;
- The reviewer is trained to default to algorithmic recommendations;
- Rejection rates fall below 1%, suggesting no genuine override capacity;
- Time constraints prevent careful review of individual cases.

Conversely, the authority identified "green flags" suggesting potentially meaningful intervention:

- Real-time access to algorithm inputs and outputs;
- Authority to request additional information before deciding;
- Genuine authority to reject a significant proportion of recommendations;
- Training on decision criteria with actual discretion;
- Override rates between 5-20% depending on context;
- Accountability for decisions made.

Applied to consultation filtering, these criteria suggest that meaningful human intervention requires not merely reviewing accepted submissions, but actively engaging with the exclusion determinations—precisely the review that high-volume processing renders practically impossible. Where an authority cannot demonstrate that human reviewers examined rejected submissions with genuine authority to reinstate them, the filtering process fails the meaningful intervention standard.

### E. The Italian Garante's Deliveroo Decision: Algorithmic Opportunity Gatekeeping

The Italian Garante's 2021 decision against Deliveroo Italy (Case 9685994) provides instructive analogy for consultation filtering.[^22b] The authority imposed a €2,500,000 fine for inadequate transparency about algorithms managing riders' work shifts. The case establishes several principles directly applicable to public consultation contexts.

First, the Garante emphasised that algorithmic systems determining access to opportunities constitute profiling requiring enhanced disclosure. The shift booking system allocated work opportunities based on automated scoring of rider reliability and availability. This "profiling carried out by the company certainly produces a significant effect on the rider concerned, consisting in the possibility of allowing (or denying) access to job opportunities."

Second, the authority rejected the argument that statistical information about algorithmic operation satisfied transparency requirements. Mere availability of aggregate statistics about the booking system was insufficient; riders required information about "the logic used, as well as the importance and expected consequences of such profiling" as it applied to them individually.

Third, the Garante found that algorithmic opacity violated fundamental fairness principles. The system penalised riders with lower scores—even where scores decreased due to circumstances beyond their control such as not logging into the application at designated times—without adequate explanation of how penalties were calculated or how rehabilitation was possible.

The parallel to consultation filtering is direct. Like the Deliveroo shift booking system, AI filtering of consultation submissions determines access to a valuable opportunity—the opportunity to have one's voice considered in democratic deliberation. Like riders denied shifts, citizens whose submissions are filtered never receive notification of the algorithmic determination affecting them. And like the Deliveroo system, consultation filtering typically operates through opaque criteria that cannot be explained or contested.

---

## IV. Information Gatekeeping as Justiciable "Decision"

The second unresolved question concerns the ontology of "decision" itself. Public authorities typically characterise filtering as preparatory—a processing step rather than a decision with legal standing. This distinction, rooted in traditional administrative law, faces significant challenge under GDPR's broader definitions.

### A. The "Invisible Rejection" and Preparatory Acts

In traditional administrative law, judicial review is often limited to final decisions definitively determining individuals' legal positions.[^23] Intermediate measures—internal memoranda, preparatory reports—are generally unreviewable unless they produce independent legal effects. Public bodies argue that AI summaries or filtered datasets constitute "intermediate measures" preparing for final regulation.

However, *SCHUFA* explicitly dismantled this preparatory act defence in automated processing contexts. The Court held that classifying automated scores as merely preparatory would create a "lacuna in legal protection."[^24] If data subjects cannot challenge automated scores (because "preparatory") and cannot challenge final decisions on grounds of scoring (because final decision-makers lack algorithmic logic), rights under Article 22 and Article 15(1)(h) are nullified.

Applying this to consultations, the structural parallels with *SCHUFA* are striking and legally consequential:

First, the **act of exclusion** operates as follows: when an AI tool marks a submission "Do Not Process," that is a final determination regarding that data packet. For the citizen, the process has ended; their input will not be heard. The algorithmic classification represents the end of the road for that citizen's participatory effort.

Second, the **lack of remedy** compounds the problem: if exclusion is treated as merely preparatory, citizens have no recourse. They cannot challenge final policy on grounds that their specific comment was auto-deleted, because policymakers are likely unaware of the deletion.

Third, therefore, to ensure **effective legal protection**, information gatekeeping—the filtering itself—must qualify as a "decision" within Article 22(1).

### B. Summarisation as Decision-Making

The issue extends beyond binary acceptance/rejection to summarisation nuance. Generative AI models synthesise thousands of comments into "key themes" reports,[^25] involving editorial decisions: selecting which points are "key" and which "peripheral."

If an LLM tasked with summarising 50,000 comments on controversial legislation hallucinates or statistically marginalises valid minority objections, that objection is effectively excised from the record.[^26] The "decision" is the determination of relevance.

Legal scholarship recognises that AI summarisation is not neutral data compression but normative content evaluation.[^27] When this evaluation determines whether citizens' arguments reach human decision-makers, it constitutes a decision affecting participation rights. The non-deterministic, opaque nature of LLMs—where inclusion/exclusion logic cannot be verified—exacerbates legal risk, preventing administration from confirming whether summarisation was fair or arbitrary.

The February 2025 *Dun & Bradstreet Austria* judgment (C-203/22) significantly strengthens this analysis.[^28] The Court clarified that "meaningful information about the logic involved" under Article 15(1)(h) requires explanation of "the procedure and principles actually applied"—not merely technical descriptions or statistical abstractions, but practical explanation of how the algorithm functions relative to the specific data subject. Information must facilitate comprehension of decision-making rationale and enable effective exercise of data subject rights, including the ability to contest decisions knowledgeably.

Importantly, the Court held that trade secrets do not excuse transparency obligations. Controllers must find means to explain logic while protecting legitimate business interests; judicial authorities and DPAs can access algorithmic information for enforcement purposes. Applied to consultation summarisation, authorities cannot simply claim that LLM reasoning is proprietary or too complex to explain.

---

## V. Legal and Similarly Significant Effects in Administrative Contexts

A pivotal defence for public authorities is that consultation responses are merely consultative. Unlike credit denial or employment termination, ignoring comments arguably produces neither "legal effects" nor "similarly significant effects" required by Article 22. Closer examination reveals this to be misconception.

### A. Legal Effects: The Aarhus Convention and Statutory Participation Rights

The "legal effect" threshold is met when decisions impact legal status or rights under contract or law.[^29] In environmental governance, the Aarhus Convention and implementing EU Directive (2011/92/EU) grant explicit legal rights to participate in decision-making.

Article 6 of the Aarhus Convention requires that "due account" be taken of public participation outcomes.[^30] If AI filtering systematically excludes relevant submissions—flagging "climate change" as political keyword in planning consultations, for instance—the authority fails to take "due account." In EU administrative law, breach of essential procedural requirements—including failure to consider mandatory public input—can lead to annulment of final decisions.[^31]

Therefore, automated filtering produces "legal effect": it violates statutory rights to be heard and potentially renders entire administrative proceedings unlawful. The "decision" to exclude comments is a decision to deny exercise of statutory rights.

The CJEU's judgment in *OT v Vyriausioji tarnybinės etikos komisija* (C-184/20) reinforces necessity and proportionality requirements for processing affecting fundamental rights.[^32] Publication of personal data must meet objectives of public interest through data minimisation principles. Indirect revelation of sensitive data still counts as special category processing. Where consultation filtering reveals or infers political opinions, these enhanced protections apply.

### B. Similarly Significant Effects: Democratic Exclusion

Beyond strict statutory rights, Article 22 covers "similarly significant effects." The EDPB interprets this to include decisions affecting behaviour, choices, access to services, or resulting in discrimination.[^33]

**Exclusion from the polity** operates as significant effect. Systemic exclusion of citizens' voices from democratic processes is significant. If algorithms bias against non-standard dialects, minority languages, or specific socio-economic phrasing, they effectively disenfranchise those groups from feedback loops.[^34] Research demonstrates that natural language processing models exhibit systematic biases correlated with socioeconomic indicators, potentially amplifying existing inequalities in political participation.

**Cumulative impact** matters: while single rejected comments might seem trivial, *SCHUFA* and DPA authorities examine processing scale and nature. Automated mass-screening of public opinion shapes the "reality" perceived by government. If that reality is distorted by algorithmic bias, the effect on citizenry is significant—it erodes democratic legitimacy. The Court of Justice's reasoning in *SCHUFA* emphasises that where automated processing affects a large number of individuals, its aggregate effects on fundamental rights must be considered even where individual impacts might appear modest.

**Chilling effect** on speech constitutes recognised harm in fundamental rights jurisprudence.[^35] Knowledge that submissions are AI-filtered may deter participation, particularly from those uncertain whether their contributions will be characterised as "relevant" or "constructive" by opaque algorithmic criteria. This concern is particularly acute where public authorities deploy AI without disclosing its use, leaving citizens unaware that their submissions may be subject to algorithmic evaluation.

### C. The Access-to-Opportunity Framework

A useful conceptual framework for analysing effects in consultation contexts emerges from employment and financial services precedents. The EDPB's guidelines identify automated decisions affecting "access to services" as producing similarly significant effects.[^35a] Credit scoring that determines borrowing access, employment screening that gates job opportunities, and tenant scoring that affects housing availability all fall within Article 22's scope precisely because they control access to important life resources.

Public consultation participation operates analogously. Citizens engage in consultations to influence policy outcomes affecting their lives, communities, and interests. The opportunity to participate—to have one's views considered in governmental deliberation—constitutes access to a democratic "service" fundamental to citizenship. When AI filtering determines which citizens gain this access and which do not, it produces effects similarly significant to those recognised in commercial contexts.

The Greek Hellenic Data Protection Authority's Decision 30/2024 reinforces this framework.[^35b] While addressing access rights rather than automated decision-making directly, the authority emphasised that controllers cannot simply ignore data subjects' requests for information about how their data is processed. The decision imposed fines for both failure to respond to access requests and failure to cooperate with supervisory authority investigations—demonstrating regulatory willingness to enforce transparency obligations rigorously.

### D. The Administrative Law Dimension: Good Administration Requirements

Beyond GDPR, the fundamental right to good administration under Article 41 of the Charter of Fundamental Rights imposes independent obligations on public authorities.[^35c] This right includes the obligation of administration to give reasons for its decisions. Where AI filtering determines consultation outcomes without explanation, it arguably violates this fundamental administrative law requirement.

The European Ombudsman's investigations into EU institutions' AI use underscore this dimension.[^35d] The Ombudsman has emphasised that administrative decisions must be explicable and contestable. Algorithmic determinations that cannot be explained—because the AI system's reasoning is opaque or non-deterministic—fail to satisfy the duty to give reasons that administrative law requires.

This creates a potentially broader obligation than GDPR alone imposes. Even where Article 22 might not apply (perhaps because filtering does not cross the "similarly significant effects" threshold), the administrative law duty to provide reasons would still require authorities to be able to explain why particular submissions were excluded. Where explanation is impossible due to algorithmic opacity, deployment of the AI system itself may constitute maladministration.

The CNIL's 2023 deliberation on algorithmic video surveillance for the Paris Olympics (SAN-2023-076) provides instructive analogy.[^36] Approving the system, CNIL emphasised that safeguards under Article 22(3) required "human intervention in the systematic identification of alerts." The authority stressed transparency as "essential to allow deployment in a climate of confidence." Applied to consultation filtering, similar requirements for human review of algorithmic determinations and disclosure of AI use would apply.

---

## VI. Profiling, Sentiment Analysis, and Special Category Data

A common technical defence asserts that NLP tools analyse *content* (text), not *people* (data subjects), therefore processing is not "profiling" under Article 4(4). This distinction is both ontologically and legally precarious.

### A. Inferring Personal Aspects from Text

Article 4(4) defines profiling as automated processing to evaluate "personal aspects," including "personal preferences, interests, reliability, behaviour."[^37] Modern NLP techniques—sentiment analysis and stance detection—are designed precisely to evaluate these aspects.

**Sentiment as preference**: when AI analyses submissions to determine if authors are "Angry," "Satisfied," or "Neutral," it evaluates personal preferences and emotional states.

**Stance as interest**: classifying submissions as "Pro-Policy" or "Anti-Policy" evaluates data subjects' interests and reliability regarding proposed measures.

**Linkage to identity**: even where text is anonymised, modern practices often link submissions to IP addresses or user accounts to detect "bot" activity. Once this link exists, text analysis becomes profiling of identifiable natural persons.

The Austrian DSB's *2020-0.436.002* decision directly addressed this issue.[^38] Marketing scores calculating probability percentages for classification into categories such as "conservatives," "traditionalists," or "digital individualists" constituted profiling under Article 4(4). The authority emphasised that processing need not be *solely* automated to constitute profiling—any automated evaluation of personal aspects suffices. The same reasoning applies to sentiment and stance analysis in consultations.

### B. Sentiment Analysis as Special Category Data Processing

Legal stakes escalate dramatically where inferred "personal aspects" include political opinions. Under Article 9, data revealing political opinions constitutes special category data; processing is generally prohibited.[^39]

**Inference of politics**: in consultations regarding controversial legislation (migration, tax reform), submissions expressing strong opposition inherently reveal political opinions. If NLP models categorise submissions as "Opposed/Negative Sentiment," they process special category data.

**Article 22(4) prohibition**: Article 22(4) explicitly prohibits automated decisions based on special category data unless the subject has given explicit consent, or processing is necessary for substantial public interest with suitable measures in place.[^40]

Public authorities rarely obtain explicit consent to profile political sentiment for filtering purposes. The "substantial public interest" defence is weak for mere administrative efficiency. Therefore, using sentiment analysis to deprioritise "negative" feedback constitutes *prima facie* violation of Article 22(4).

The EDPB's WP251 guidelines acknowledge that profiling can create special category data by inference from data not itself special category but becoming so when combined.[^41] Records of food shopping combined with nutritional data might infer health status; consultation comments combined with stance detection infer political convictions. Controllers must ensure they have lawful basis for special category processing and inform data subjects of such processing.

### C. The Ontological Problem: Text Analysis as Personal Evaluation

The argument that NLP analyses *content* rather than *people* faces a deeper conceptual challenge. Text analysis in consultation contexts necessarily evaluates what the author has written—their arguments, their reasoning, their expression. This is not content-neutral deduplication but evaluation of the communicative act the person has performed.

Article 4(4) defines profiling as evaluating "personal aspects" including "interests," "reliability," and "behaviour." When AI classifies a submission as "off-topic," "low-quality," or "non-constructive," it evaluates the submitter's *behaviour* (the act of making a particular type of submission) and implicitly their *reliability* as a participant in democratic deliberation. The output—inclusion or exclusion—determines how the person is treated based on this evaluation.

This analysis finds support in the Court of Justice's approach to algorithmic processing more generally. In *SCHUFA*, the Court emphasised that automated processing affecting individuals must be subject to safeguards regardless of technical characterisation. The protective purpose of Article 22 applies wherever algorithms make determinations that affect how individuals are treated, not merely where processing fits neatly into predefined technical categories.

### D. Comparative Approaches: The UK Perspective

The United Kingdom's approach to automated decision-making post-Brexit provides instructive contrast. Under the Data (Use and Access) Bill, reforms to Article 22 equivalent provisions have been proposed that would permit solely automated decision-making more readily while strengthening safeguards requirements.[^41a]

However, even under proposed UK reforms, meaningful safeguards remain mandatory. The Information Commissioner's Office has emphasised that automated decision-making affecting individuals requires: transparency about AI use; explanation of decision logic; opportunity to contest decisions; and genuine human review mechanisms.[^41b] These requirements would apply equally to public authority deployment of consultation filtering systems.

The convergence between EU and UK approaches on safeguards—despite divergence on the general prohibition—suggests that the transparency and contestability requirements analysed in this article represent minimum standards that public authorities cannot avoid regardless of jurisdiction. The specific question of whether filtering constitutes prohibited ADM may vary by jurisdiction, but obligations to explain, to enable challenge, and to ensure meaningful oversight apply universally.

---

## VII. Safeguards and the Article 22(2)(b) Exception

Article 22(2)(b) provides an exception for automated decisions "authorised by Union or Member State law" to which controllers are subject, provided such law establishes "suitable measures to safeguard the data subject's rights." The question is whether current national administrative laws meet this standard.

### A. The Adequacy of Statutory Authorisation

General administrative laws authorising "data processing" or "digital government" are likely insufficient to authorise *solely automated filtering* under strict GDPR requirements. Recital 71 mandates specific authorisation.[^42]

**German framework**: Section 35a of the Administrative Procedure Act (VwVfG) permits fully automated administrative acts (*Verwaltungsakt*) only where "permitted by a legal provision" and where there is "no discretion" or room for independent appreciation.[^43] Evaluating public comments is inherently discretionary—weighing arguments, assessing relevance. Therefore, fully automated filtering of consultation responses likely falls *outside* § 35a's scope. Without specific legal basis, such filtering is unauthorised and illegal under Article 22(2)(b).

**French framework**: the Code of Relations between the Public and Administration (CRPA Article L311-3-1) permits individual decisions based on algorithmic processing, provided the decision is explicitly mentioned and rules defining processing are communicated upon request.[^44] This framework imposes strict transparency conditions. If authorities use proprietary, opaque LLMs and cannot explain "rules defining the processing" (because models are non-deterministic), they violate Article L311-3-1. Filtering becomes unlawful not because automated, but because failing the explanation safeguard.

The French Défenseur des Droits' 2024 report on algorithms in public services emphasises that algorithmic opacity creates "asymmetry of information that can undermine citizens' capacity to understand and contest decisions affecting them."[^45] The report recommends that public authorities deploying AI must ensure intelligible explanations sufficient for individuals to exercise rights.

### B. The Safeguards Deficit

Even where legally authorised, controllers must implement suitable measures including rights to obtain human intervention, express views, and contest decisions.[^46]

**The notice gap**: in AI filtering, citizens are rarely notified that submissions were filtered. Without notification ("Your submission was flagged as off-topic"), they cannot exercise rights to contest or demand human intervention.

**The black box barrier**: even where citizens contest filtering, authorities may be unable to provide meaningful explanation of *why* LLMs rejected comments, violating the right to good administration.[^47]

**Architectural inadequacy**: current consultation procedures were designed for paper submissions; they lack procedural "hooks"—notification mechanisms, appeal processes—necessary for Article 22 compliance.

The Berlin DPA's enforcement action underscores these requirements.[^48] The authority held that even with automated processes, controllers must provide "comprehensible information about the automated rejection," including "specific information on the database and the decision-making factors as well as the criteria for rejection in individual cases." Generic descriptions of AI systems are insufficient.

### C. The C-203/22 Transparency Standard

The *Dun & Bradstreet Austria* judgment establishes heightened transparency requirements post-February 2025.[^49] "Meaningful information about logic involved" requires substantive explanation—not "algorithm processed your data" or "socio-demographic factors given equal weighting," but explanation of *how specific data inputs produced the decision regarding this individual*.

The Court's holding that trade secrets do not excuse non-disclosure is particularly significant for public authorities using third-party AI systems. Where vendors claim algorithmic opacity as intellectual property, authorities cannot simply defer: they bear responsibility for ensuring systems they deploy permit compliance with transparency obligations. This may require contractual provisions mandating vendor cooperation with explanation requests, or may counsel against deploying truly opaque systems for decisions affecting fundamental rights.

The *Dun & Bradstreet* judgment elaborates specific elements that meaningful information must address.[^49a] First, controllers must explain "the procedure and principles actually applied" to the individual's data—not merely generic descriptions of system capabilities, but account of how the specific decision was reached. Second, information must be presented "in concise, transparent, intelligible and easily accessible form, using clear and plain language"—technical algorithmic specifications that require expertise to interpret do not satisfy this requirement. Third, the purpose of explanation is to enable exercise of data subject rights, particularly the ability to "contest the decision" under Article 22(3)—information is insufficient if it does not enable the data subject to identify potential errors or grounds for challenge.

For consultation filtering, these requirements pose significant practical challenges. Large language models and complex NLP systems often lack deterministic, explicable decision pathways. A sentiment classifier might assign negative polarity to a submission based on distributional patterns across thousands of training examples without identifiable "reasoning" that could be communicated to a layperson. The *Dun & Bradstreet* standard suggests that such systems may be inherently unsuitable for decisions affecting individuals' fundamental rights—if the logic cannot be meaningfully explained, the transparency obligation cannot be satisfied, and deployment is prima facie unlawful.

### D. Procedural Safeguards in Practice

Even where transparency requirements can be satisfied, Article 22(3) mandates specific procedural safeguards: the right to obtain human intervention, to express one's view, and to contest the decision.[^49b] These safeguards require operational implementation that current consultation procedures typically lack.

**Human intervention** requires more than nominal human involvement—it requires intervention that can genuinely affect the outcome. For filtered submissions, this means human review of the filtering determination with authority to reinstate excluded content. Current systems rarely provide this: filtered submissions are typically archived without notification, and human reviewers engage only with accepted content.

**Expression of views** presupposes notification that a decision has been made. Where submissions are filtered without notice, data subjects cannot express views about determinations they are unaware of. Implementing this safeguard requires notification systems informing participants when submissions are classified adversely, together with mechanisms for response.

**Contestation** requires review processes capable of reversing erroneous determinations. This implies both procedural mechanisms (how does one contest a filtering decision?) and substantive standards (what grounds justify reversal?). Neither is typically articulated in current consultation procedures.

The Spanish Data Protection Agency's (AEPD) approach to AI transparency provides useful guidance.[^49c] In decisions concerning algorithmic systems, the authority has emphasised that controllers must be able to "reconstruct" decision-making processes—to identify the inputs, algorithmic operations, and outputs that produced a particular determination. Where such reconstruction is impossible due to system opacity, the controller has failed to implement appropriate safeguards.

### E. The Transparency-Efficiency Trade-off

A fundamental tension emerges from the analysis: the efficiency gains AI promises in consultation processing may be incompatible with the transparency and safeguard obligations GDPR imposes. Systems capable of processing millions of submissions rapidly typically achieve this through complexity that defies simple explanation. Systems simple enough to explain meaningfully may lack the sophistication to handle consultation volumes efficiently.

This trade-off has implications for system design. Authorities should consider "glass box" approaches that prioritise explicability over raw performance—simpler rule-based systems or interpretable machine learning models that sacrifice some accuracy for transparency. Alternatively, hybrid architectures might combine efficient AI preprocessing with human-accessible explanation generation, though such approaches introduce additional complexity and potential points of failure.

The trade-off also has resource implications. Where AI cannot lawfully exclude submissions without human review, the efficiency gains from automation are reduced. Authorities must budget for compliance costs alongside technological deployment costs. The seductive promise of AI—that technology can replace human labor—may prove illusory where GDPR mandates human involvement that AI was intended to displace.

---

## VIII. The Interplay with the AI Act

The regulatory landscape tightens with the AI Act's entry into force. This legislation codifies risks identified in GDPR analysis.

### A. High-Risk Classification

The AI Act classifies AI systems intended for "administration of justice and democratic processes" as High-Risk (Annex III, point 8).[^50] Systems used by public authorities that may influence democratic processes fall within this category.

AI tools filtering or summarising public consultation responses directly impact democratic processes. This classification triggers stringent obligations: high-quality data governance to prevent bias, record-keeping, transparency, and human oversight.[^51] The practical implications for public authorities are substantial.

First, **data governance requirements** under Article 10 mandate that training, validation, and testing datasets be relevant, sufficiently representative, and free of errors.[^51a] For consultation filtering systems, this requires demonstration that training data adequately represents the diversity of legitimate public input—a challenging requirement given the heterogeneity of democratic discourse. Systems trained primarily on formal bureaucratic communication may systematically misclassify informal citizen expression.

Second, **technical documentation** under Article 11 requires detailed records of system design, development, and operation.[^51b] Public authorities deploying third-party AI systems must ensure vendor cooperation in producing such documentation. The common practice of deploying commercial "off-the-shelf" AI tools without detailed technical specifications becomes problematic under these requirements.

Third, **transparency obligations** under Article 13 require that deployers provide sufficient information to enable users to interpret system outputs and use them appropriately.[^51c] For consultation filtering, this means civil servants must understand system limitations, potential biases, and appropriate contexts for reliance on or override of algorithmic recommendations.

Fourth, **human oversight** under Article 14 requires measures enabling humans to understand system capacities and limitations, appropriately monitor operation, and intervene when necessary.[^51d] This reinforces the meaningful intervention requirements discussed above—nominal human involvement that merely ratifies algorithmic outputs does not satisfy Article 14 any more than it satisfies Article 22 GDPR.

### B. Fundamental Rights Impact Assessment

Article 27 requires deployers of high-risk AI systems—specifically public bodies—to conduct Fundamental Rights Impact Assessments (FRIA) prior to deployment.[^52]

The assessment must address specific risks of harm to affected individuals' fundamental rights: freedom of expression, good administration, non-discrimination.[^53] If authorities cannot guarantee that AI filters will not disproportionately silence minority voices or misclassify valid dissent as "toxicity," FRIA should theoretically prevent deployment. A negative assessment would render continued use unlawful, reinforcing Article 22 prohibition.

The FRIA requirement represents a significant procedural safeguard absent from GDPR's Article 22 framework. While GDPR's Data Protection Impact Assessment (DPIA) under Article 35 applies to "systematic and extensive evaluation of personal aspects" including profiling, its focus on data protection risks differs from FRIA's emphasis on fundamental rights more broadly.[^53a]

For consultation filtering, the relevant fundamental rights extend beyond data protection to include:

**Freedom of expression** (Article 11 CFR): AI filtering directly implicates speech rights. Citizens have the right to hold opinions and to express and receive information without interference. Algorithmic suppression of submissions—particularly where based on viewpoint-correlated characteristics—engages this freedom directly.[^53b]

**Freedom of assembly and association** (Article 12 CFR): organised campaigns coordinating submissions may be particularly vulnerable to deduplication algorithms. While eliminating truly identical spam serves legitimate purposes, algorithms that suppress related but distinct submissions from organised groups may interfere with collective political action.[^53c]

**Right to good administration** (Article 41 CFR): this includes the right to be heard before any adverse measure is taken. Where AI filtering prevents submissions from reaching decision-makers, it interferes with this procedural right—the citizen's voice is not heard because it never reaches human ears.[^53d]

**Right to an effective remedy** (Article 47 CFR): where citizens cannot challenge algorithmic filtering—because they are unaware it occurred, because they cannot access explanation of the algorithmic determination, or because no review mechanism exists—this fundamental right is undermined.[^53e]

A comprehensive FRIA for consultation filtering would need to assess risks to each of these rights, propose mitigation measures, and conclude that deployment is justified despite residual risks. Given the analysis in this article, conducting such an assessment honestly might lead many authorities to conclude that current filtering practices cannot be justified.

### C. The European Ombudsman's Stance

The European Ombudsman has investigated AI use in public administration, emphasising that efficiency cannot subordinate accountability.[^54] The Ombudsman recommends that public administrations ensure AI systems remain "tools to support decision-making" rather than delegates of decision-making power.

The Ombudsman's closing note on the Commission's AI use (SI/4/2024/MIK) recommended "compliance checks" and internal guidelines to ensure human oversight remains meaningful.[^55] This soft law reinforces hard law interpretation: black-box filtering without genuine human review constitutes maladministration.

The Ombudsman's broader jurisprudence on good administration provides additional guidance. In decisions concerning procedural fairness, the Ombudsman has consistently held that affected persons must have opportunity to present their views before measures affecting them are taken, must receive reasoned decisions, and must have access to effective review.[^55a] These principles, developed in human decision-making contexts, apply with equal or greater force where decisions are automated—the fundamental requirements of procedural fairness do not diminish merely because the decision-maker is algorithmic.

### D. The AI Act's Interaction with GDPR

The AI Act explicitly preserves GDPR's application. Article 2(7) provides that the Regulation "shall apply without prejudice to" Union law on data protection.[^55b] This means that compliance with AI Act requirements does not excuse GDPR violations—authorities must satisfy both frameworks.

For consultation filtering, this creates layered obligations:

Under **GDPR**, filtering must either not constitute Article 22 ADM (unlikely given *SCHUFA* analysis), fall within Article 22(2) exceptions (requiring specific authorisation and safeguards), or be conducted in compliance with Article 22(3) rights (human intervention, expression of views, contestation).

Under the **AI Act**, high-risk classification requires compliance with data governance, transparency, human oversight, and FRIA requirements.

The cumulative effect is demanding. Authorities cannot argue that AI Act compliance substitutes for GDPR obligations, nor that GDPR compliance excuses AI Act requirements. Both frameworks must be satisfied simultaneously.

### E. Enforcement Implications

The AI Act establishes market surveillance authorities with powers to investigate and sanction AI Act violations.[^55c] These authorities operate alongside data protection authorities with GDPR enforcement powers. The potential for parallel investigations and cumulative sanctions—by both AI Act market surveillance and GDPR data protection authorities—increases compliance pressure on public authorities deploying consultation filtering systems.

The AI Act's penalty provisions (up to €35 million or 7% of turnover for certain violations) significantly exceed those for which public authorities have typically been held liable under GDPR.[^55d] While public authority liability under both frameworks requires clarification through enforcement practice, the regulatory trend clearly favours heightened accountability for algorithmic governance.

---

## IX. Synthesis and Recommendations

The analysis yields several conclusions regarding AI-assisted filtering of public consultation submissions under GDPR Article 22.

### A. Summary of Legal Findings

**On solely automated processing**: where human reviewers do not audit *excluded* submissions, filtering is solely automated. The human-in-the-loop is illusory if they see only the "accepted" pile. The *SCHUFA* doctrine's "determining role" test asks not whether humans formally approve outcomes, but whether algorithmic classification predetermines them in practice. Where AI filtering flags submissions as "non-substantive" and human reviewers never examine them—treating the algorithmic classification as dispositive—the process is *de facto* solely automated.

**On decision status**: under *SCHUFA*, upstream filtering constitutes a justiciable decision because it determines admissibility of citizen input, predetermining final outcomes for those individuals. The Court's purposive reasoning—that excluding preparatory automated processing from Article 22 would create a "lacuna in legal protection"—applies directly. Citizens cannot challenge final policies on grounds that their specific submissions were algorithmically excluded when policymakers were unaware of the exclusion. Therefore, the exclusion itself must be justiciable.

**On effects**: such decisions produce "legal effects" (violation of statutory participation rights under Aarhus and EU administrative law) and "similarly significant effects" (exclusion from democratic processes, chilling effects on civic engagement). The "access-to-opportunity" framework developed in employment and credit contexts applies: participation in public consultation is a valuable opportunity, and algorithmic gatekeeping controlling that access produces effects recognised as significant in comparable private sector contexts.

**On profiling**: sentiment analysis and stance detection constitute profiling of "personal aspects" (political opinions), triggering stricter Article 9 and Article 22(4) prohibitions. The technical argument that NLP analyses text rather than people collapses upon examination—evaluating what someone has written necessarily evaluates their behaviour, interests, and reliability as a communicative actor.

**On safeguards**: existing national administrative laws frequently lack specific authorisation and procedural safeguards (notification, contestability) required to legitimise discretionary automated filtering under Article 22(2)(b). General laws permitting digital government or administrative efficiency do not satisfy the specific authorisation Recital 71 requires. Moreover, the Article 22(3) safeguards—human intervention, expression of views, contestation—require procedural mechanisms that current consultation systems typically lack.

### B. Recommendations for Public Authorities

To achieve lawful AI deployment, public authorities should restructure their approaches along the following lines.

**From filtering to tagging**: AI should never unilaterally exclude or delete submissions. It should function only to tag or group comments for human review—"Potential Spam" folders, not automatic deletion. This architectural choice preserves human decision-making authority and creates an audit trail enabling the "meaningful intervention" GDPR requires.

**Human audit of the negative**: meaningful intervention requires auditing the *rejected* pile, not merely the accepted. Human reviewers must have authority, information access, and time to genuinely assess AI classifications. This may require resource allocation acknowledging that AI efficiency gains cannot be fully captured if compliance obligations mandate human review of negative determinations. Authorities should consider whether partial efficiency gains with full compliance are preferable to greater efficiency gains with legal risk.

**Transparency**: AI use in analysing submissions must be publicly disclosed, including filtering logic, to satisfy Articles 13-14 GDPR and principles of good administration. The *Dun & Bradstreet* standard requires explanation of procedures and principles actually applied. Authorities should publish accessible descriptions of AI systems deployed, their functions, limitations, and the criteria they apply. Consultation invitations should explicitly inform participants that AI tools may process their submissions and explain available review mechanisms.

**Avoid sentiment scoring for eligibility**: using sentiment analysis to determine visibility or weight of submissions carries unacceptable legal risk under Article 9. If deployment is necessary, explicit consent or specific legislative authorisation with suitable safeguards is required. More fundamentally, authorities should question whether sentiment scoring serves legitimate purposes in democratic consultation—negative sentiment may reflect legitimate grievance rather than non-substantive input.

**FRIA before deployment**: high-risk classification under the AI Act mandates fundamental rights impact assessment. Authorities should document risks to participation rights, freedom of expression, and non-discrimination, with mitigation measures. Where FRIA reveals unmitigable risks—algorithmic systems that cannot be adequately explained, or that exhibit bias against particular communicative styles or viewpoints—deployment should not proceed regardless of efficiency benefits.

### C. Recommendations for Legislators

The legal uncertainty identified in this article suggests the need for legislative clarification. Member States could address the issues through specific authorising legislation meeting Article 22(2)(b) requirements.

**Clear legal basis**: legislation should explicitly authorise specified categories of automated processing in consultation contexts, identifying permissible functions (deduplication, spam detection) and prohibited ones (viewpoint-based filtering, sentiment scoring for eligibility).

**Mandatory safeguards**: authorising legislation should establish procedural safeguards including: notification when submissions are algorithmically classified; explanation of classification criteria; accessible review mechanisms enabling challenge to adverse classifications; and human review before any submission is excluded from consideration.

**Transparency requirements**: legislation should mandate disclosure of AI system specifications sufficient to enable public scrutiny and accountability, consistent with proportionate protection of legitimate commercial interests in proprietary technology.

**Audit and accountability**: legislation should require periodic independent audit of AI systems' performance, including analysis of false positive rates, bias indicators, and review outcome statistics. Audit results should be publicly disclosed.

### D. Recommendations for Civil Society and Affected Individuals

Individuals whose submissions may be subject to algorithmic processing should consider taking proactive steps to protect their participatory rights.

**Exercise access rights**: data subjects may request information under Article 15 about how their submissions were processed, including whether algorithmic tools were used and how they classified the submission. The *Dun & Bradstreet* standard requires meaningful information about the logic involved.

**Document submissions**: maintaining records of submissions made enables later verification if submissions appear to have been excluded. Where authorities publish summaries of consultation input, participants can compare these against their own submissions to identify potential gaps.

**Collective action**: civil society organisations may coordinate monitoring of algorithmic consultation processing, identifying patterns suggesting bias or malfunction. Complaints to data protection authorities can trigger supervisory investigation.

**Strategic litigation**: test cases challenging algorithmic filtering could establish precedent clarifying legal obligations. The *SCHUFA* judgment demonstrates judicial willingness to interpret Article 22 purposively; litigation concerning public authority ADM could extend this jurisprudence to administrative contexts.

---

## X. Conclusion

The digitisation of public consultation creates both opportunity and risk. AI tools promise to manage unprecedented volumes of citizen feedback, but their deployment introduces algorithmic gatekeeping into democratic deliberation with significant legal implications under GDPR Article 22.

The evolution from *SCHUFA* to *Dun & Bradstreet Austria* demonstrates judicial willingness to interpret Article 22 purposively, preventing circumvention through nominal human involvement or preparatory act characterisation. Where AI determines which citizens are heard and which are silenced—however efficiently—it makes decisions affecting fundamental rights. The transparency, explainability, and safeguard requirements attached to such decisions cannot be satisfied through opacity and automation.

National enforcement by authorities in Berlin, Austria, and France confirms supervisory attention to these issues. The Italian Garante's Deliveroo decision demonstrates that algorithmic opportunity gatekeeping—determining who gains access to valuable opportunities—attracts strict regulatory scrutiny regardless of the nominal characterisation of the processing. The AI Act's high-risk classification for systems affecting democratic processes, and the European Ombudsman's emphasis on accountability over efficiency, signal a regulatory environment increasingly inhospitable to unreviewable algorithmic gatekeeping.

Public authorities deploying AI in consultations must ensure that technology serves rather than supplants human judgment on questions of democratic participation. The right to be heard must include the right not to be silenced by an algorithm. Where AI filtering operates upstream, invisibly curating which voices reach decision-makers, the promise of digital democracy is compromised by the reality of algorithmic exclusion.

The path forward requires not rejection of technology but its disciplined deployment: systems that tag rather than filter, human review that examines rejections rather than merely ratifying acceptances, transparency that enables citizens to understand how their submissions are processed, and accountability structures ensuring that administrative convenience does not override participatory rights. Only through such measures can public authorities reconcile the efficiency benefits of AI with their fundamental obligations under data protection law and the principle of good administration.

The stakes extend beyond legal compliance. Public consultation serves functions beyond efficient policy development—it legitimises governmental action by demonstrating responsiveness to citizen concerns. When algorithmic systems intermediate between citizens and government, they must do so in ways that preserve this legitimating function. Consultation that citizens perceive as genuine—where their voices have realistic possibility of being heard and considered—generates democratic legitimacy that mere box-ticking exercises cannot. AI deployment that undermines this perception, whether through opacity, arbitrary exclusion, or demonstrable bias, damages not merely individual rights but the broader project of democratic governance.

Conversely, appropriately deployed AI could enhance rather than undermine democratic consultation. Systems designed to identify themes, flag potential issues, and organise diverse input for human consideration might enable more effective policy deliberation than manual review of overwhelming submission volumes. The distinction lies in whether AI functions as a decision-maker—determining outcomes for citizens without genuine human review—or as a tool empowering human decision-makers to exercise their judgment more effectively.

This article has argued that current legal frameworks, properly interpreted, require the latter model. Article 22's protection against solely automated decisions, reinforced by *SCHUFA*'s "determining role" doctrine, applies wherever algorithms predetermine individual outcomes regardless of nominal human involvement. The AI Act's high-risk classification and FRIA requirements add layers of obligation. Administrative law principles of good administration require explicable, contestable decisions.

Whether public authorities will comply with these requirements, and whether supervisory authorities and courts will enforce them rigorously, remains to be seen. The coming years will likely see test cases as citizens challenge algorithmic exclusion from public participation. The outcomes of such cases will shape not merely data protection law but the character of democratic governance in an algorithmic age.

The fundamental question is not whether AI can be used in public consultation—clearly it can, within appropriate limits. The question is whether democratic societies will insist on those limits, maintaining human judgment as the ultimate arbiter of citizen participation, or will acquiesce to algorithmic governance that prioritises efficiency over accountability. The legal frameworks analysed in this article provide tools for insisting on the former. Their effective deployment depends on vigilance by citizens, civil society, and supervisory authorities committed to ensuring that technological capability does not outpace constitutional constraint.

---

## References

[^1]: See generally U.S. Federal Government, 'Implementing Federal-Wide Comment Analysis Tool' (Project Open Data 2024); S. Whitehead, 'From Noise to Insight: Using AI to Rethink Public Comment Analysis' (2025) Medium.

[^2]: On upstream filtering in network contexts, see SSAC Advisory on Impacts of Content Blocking via the Domain Name System, SSAC 056 (ICANN 2012). The administrative analogy is developed in the text.

[^3]: Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data [2016] OJ L119/1 (GDPR).

[^4]: GDPR, Recital 71 ('Profiling'); see also Article 29 Working Party, 'Guidelines on Automated individual decision-making and Profiling for the purposes of Regulation 2016/679' (WP251rev.01, adopted 3 October 2017, revised 6 February 2018) (hereinafter 'WP251').

[^5]: Case C-634/21 *SCHUFA Holding and Others (Scoring)* ECLI:EU:C:2023:957.

[^6]: See 'Summarizing Public Comments on Policy Proposals Using Large Language Models' (IPPA Proceedings 2024).

[^7]: Microsoft Azure, 'Azure OpenAI in Azure AI Foundry Models content filtering' (2025).

[^8]: GDPR Advisor, 'How GDPR Affects AI-Powered Social Listening and Sentiment Analysis' (2024).

[^9]: On stance detection methodologies, see MedRxiv, 'Artificial intelligence-enabled analysis of UK and US public attitudes on Facebook and Twitter towards COVID-19 vaccinations' (2020).

[^10]: On LLM summarisation in legislative contexts, see 'Large Language Models in Legislative Content Analysis: A Dataset from the Polish Parliament' (2025) arXiv.

[^11]: The 'upstream' metaphor is developed from network security literature; see CJIS Security Policy v5.9.3 (FBI 2023) at 4.

[^12]: WP251 (n 4) 20-21.

[^13]: See Centre for Information Policy Leadership, 'Automated Decisionmaking and Profiling (ADM) Requirements in U.S. State Privacy Laws' (2024) 8-10.

[^14]: WP251 (n 4) 10.

[^15]: ibid 10-11.

[^16]: See JuLIA Project, 'Handbook: AI and Public Administration: The (legal) limits of algorithmic governance' (2025) 24-26.

[^17]: BlnBDI (Berlin) Decision of 31 May 2023, imposing €300,000 fine for Article 15(1)(h) and Article 22(3) violations.

[^18]: WP251 (n 4) 10: 'The controller cannot avoid the Article 22 provisions by fabricating human involvement.'

[^19]: Case C-634/21 *SCHUFA* (n 5).

[^20]: ibid paras 47-48.

[^21]: ibid paras 56-65; see also AG Pikamäe Opinion in C-634/21 ECLI:EU:C:2023:220 paras 35-42.

[^22]: DSB (Austria) Decision 2020-0.436.002 of 8 September 2020, ECLI:AT:DSB:2020:2020.0.436.002.

[^23]: See generally ReNEUAL, 'The Pan-European General Principles on Digitalisation of Public Administration' (2024).

[^24]: Case C-634/21 *SCHUFA* (n 5) para 58.

[^25]: Whitehead (n 1).

[^26]: On LLM hallucination risks, see D. Magesh and others, 'Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models' (2024) 16 Journal of Legal Analysis 64.

[^27]: MDPI, 'GDPR and Large Language Models: Technical and Legal Obstacles' (2025) Future Internet 151.

[^28]: Case C-203/22 *CK v Magistrat der Stadt Wien* ECLI:EU:C:2025:131.

[^29]: WP251 (n 4) 11-12.

[^30]: Convention on Access to Information, Public Participation in Decision-Making and Access to Justice in Environmental Matters (adopted 25 June 1998, entered into force 30 October 2001) 2161 UNTS 447 (Aarhus Convention) art 6.

[^31]: See Case C-72/12 *Gemeinde Altrip* ECLI:EU:C:2013:712; EIA Directive 2011/92/EU.

[^32]: Case C-184/20 *OT v Vyriausioji tarnybinės etikos komisija* ECLI:EU:C:2022:601.

[^33]: WP251 (n 4) 11-12.

[^34]: Digital Freedom Fund, 'Legal Pathways for Platform Accountability in Europe' (2024).

[^35]: The Constitution Society, 'Data and Democracy in the Digital Age' (2018) 34-36.

[^36]: CNIL (France) Délibération 2023-068 of 15 June 2023.

[^37]: GDPR, art 4(4).

[^38]: DSB (Austria) 2020-0.436.002 (n 22).

[^39]: GDPR, art 9(1).

[^40]: GDPR, art 22(4).

[^41]: WP251 (n 4) 15.

[^42]: GDPR, Recital 71.

[^43]: Verwaltungsverfahrensgesetz (VwVfG) § 35a; see CERIDAP, 'Automated Decision-Making Systems in German Administrative Law' (2024).

[^44]: Code des relations entre le public et l'administration, art L311-3-1; see Défenseur des Droits, 'Algorithms, AI systems and public services: what rights do users have?' (2024).

[^45]: ibid 42-45.

[^46]: GDPR, art 22(3).

[^47]: Charter of Fundamental Rights of the European Union [2012] OJ C326/391 art 41 (right to good administration).

[^48]: BlnBDI Decision (n 17).

[^49]: Case C-203/22 *Dun & Bradstreet Austria* (n 28) paras 47-52.

[^50]: Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act) Annex III, point 8.

[^51]: ibid arts 9-15.

[^52]: ibid art 27.

[^53]: ibid Recital 96.

[^54]: European Ombudsman, Closing Note SI/4/2024/MIK (2025).

[^55]: ibid paras 24-28.

[^22a]: Autoriteit Persoonsgegevens (Netherlands), 'Consultation on automated decision-making guidelines' (2025).

[^22b]: Garante per la protezione dei dati personali (Italy), Decision 9685994 of 22 July 2021 (Deliveroo Italy).

[^35a]: WP251 (n 4) 21-22.

[^35b]: HDPA (Greece) Decision 30/2024.

[^35c]: Charter of Fundamental Rights art 41.

[^35d]: European Ombudsman, Strategic Inquiry OI/4/2024/MHZ on Use of AI by EU Institutions (2024).

[^41a]: Data (Use and Access) Bill 2024 (UK).

[^41b]: Information Commissioner's Office (UK), 'Guidance on AI and data protection' (2024).

[^49a]: Case C-203/22 *Dun & Bradstreet Austria* (n 28) paras 53-58.

[^49b]: GDPR, art 22(3).

[^49c]: AEPD (Spain), Decision PS/00037/2020.

[^51a]: AI Act (n 50) art 10.

[^51b]: ibid art 11.

[^51c]: ibid art 13.

[^51d]: ibid art 14.

[^53a]: GDPR, art 35.

[^53b]: Charter of Fundamental Rights art 11.

[^53c]: ibid art 12.

[^53d]: ibid art 41.

[^53e]: ibid art 47.

[^55a]: European Ombudsman, 'Principles of Good Administration' (2012).

[^55b]: AI Act (n 50) art 2(7).

[^55c]: ibid arts 63-75.

[^55d]: ibid art 99.

[^10a]: On relevance ranking in information retrieval contexts, see generally C. Manning and others, *Introduction to Information Retrieval* (CUP 2008).
