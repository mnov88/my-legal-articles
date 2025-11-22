# Algorithmic gatekeeping in the administrative state: AI-assisted processing of public consultation submissions under GDPR Article 22

## Abstract

The digitisation of public administration has precipitated a shift in the mechanics of participatory democracy. Confronting an unprecedented volume of digital feedback, public authorities deploy artificial intelligence — particularly large language models and natural language processing tools — to aggregate, summarise, and filter public consultation submissions. This technological transition introduces algorithmic gatekeeping into democratic deliberation.

This article provides a doctrinal analysis of whether such upstream AI filtering constitutes automated decision-making prohibited under Article 22 GDPR. The analysis demonstrates that consultation filtering represents a paradigm case exposing unresolved questions in Article 22 interpretation: whether democratic participation effects constitute "similarly significant effects," whether content evaluation constitutes profiling of personal aspects, and whether procedural determinations qualify as Article 22 "decisions." Drawing on the Court of Justice's *SCHUFA* judgment (C-634/21) and *Dun & Bradstreet Austria* ruling (C-203/22), alongside national enforcement decisions, the article argues these doctrinal gaps should be resolved in favour of protection. The "determining role" doctrine, the fundamental rights purpose of Article 22, and the access-to-opportunity framework developed in employment and credit contexts support bringing consultation filtering within the prohibition's scope. Even where doctrinal uncertainty persists, complementary frameworks — the AI Act, administrative procedure law, and the Aarhus Convention — establish accountability obligations that cannot be satisfied through opacity and unreviewable algorithmic gatekeeping.

---

## I. Introduction

A citizen submits a detailed objection to a proposed power plant, documenting environmental concerns that — if considered — might have led the authority to deny the concession. The submission is received by a server, processed by an algorithm that classifies it as "not sufficiently substantive," and archived without human review. The authority grants the concession. The citizen never learns that their submission was filtered.

This scenario is not hypothetical. Administrative authorities across the European Union deploy artificial intelligence to manage the volume of public consultation responses.[^1] The efficiency imperative is understandable: major infrastructure consultations can generate tens of thousands of submissions, exceeding the processing capacity of civil servants. AI tools promise to synthesise this input into actionable summaries.

[^1]: See generally U.S. Federal Government, 'Implementing Federal-Wide Comment Analysis Tool' (Project Open Data 2024); S. Whitehead, 'From Noise to Insight: Using AI to Rethink Public Comment Analysis' (2025) Medium.

The legal question is whether such filtering constitutes automated decision-making prohibited under GDPR Article 22.

This article argues that consultation filtering represents a paradigm case for doctrinal development — neither clearly within nor clearly outside Article 22's scope, but precisely the kind of case that exposes unresolved interpretive questions. Three doctrinal gaps require resolution: whether exclusion from democratic participation produces "similarly significant effects" on data subjects; whether AI evaluation of submission content constitutes profiling of "personal aspects"; and whether procedural filtering determinations qualify as Article 22 "decisions" when they play a determining role in who is heard.

The Court of Justice's recent jurisprudence — particularly *SCHUFA* (C-634/21) and *Dun & Bradstreet Austria* (C-203/22) — provides interpretive tools for resolving these gaps.[^2] The *SCHUFA* judgment established that preparatory automated outputs constitute "decisions" when they play a determining role in downstream outcomes, rejecting formalist arguments that would enable circumvention through nominal human involvement.[^3] This reasoning, combined with Article 22's fundamental rights purpose and the access-to-opportunity framework developed in employment and credit contexts, supports extending protection to democratic participation.

[^2]: Case C-634/21 *SCHUFA Holding and Others (Scoring)* ECLI:EU:C:2023:957; Case C-203/22 *CK v Magistrat der Stadt Wien* ECLI:EU:C:2025:131.

[^3]: *SCHUFA* (n 2) paras 56–65.

The article proceeds as follows. Part II analyses the technical mechanisms of AI filtering and situates consultation filtering within the broader landscape of administrative AI use. Part III addresses the threshold question of what constitutes "solely automated" processing, examining the collapse of the human-in-the-loop defence after *SCHUFA*. Part IV considers whether information gatekeeping constitutes a justiciable "decision" and addresses the challenge of procedural determinations. Part V examines the "similarly significant effects" threshold, developing an access-to-opportunity framework for democratic participation. Part VI analyses whether content evaluation constitutes prohibited profiling, with particular attention to the "about whom" problem. Part VII assesses the adequacy of existing safeguards under Article 22(2)(b). Part VIII considers the interplay with the AI Act. The article concludes with the argument that, even where Article 22's application remains doctrinally uncertain, the analysis reveals requirements for algorithmic accountability in democratic administration that cannot be satisfied through opacity and unreviewable gatekeeping.

---

## II. The technical and legal anatomy of AI filtering

Understanding the legal implications requires first dissecting the technical mechanisms of AI filtering and their correspondence to legal concepts.

### A. Taxonomy of AI interventions

Public authorities utilise various AI techniques to manage submission volumes. Deduplication employs similarity pipelines to identify identical or near-identical text, grouping mass campaigns into single entries.[^4] Where limited to exact matches with human review of the consolidated entry, such processing likely falls outside Article 22's scope.

[^4]: See 'Summarizing Public Comments on Policy Proposals Using Large Language Models' (IPPA Proceedings 2024).

Spam and toxicity filtering deploys classifiers trained on datasets of harmful speech to block submissions deemed irrelevant or abusive.[^5] This processing carries significant Article 22 risk: rejection of input constitutes a determination on admissibility, with direct effects on the data subject's participatory access.

[^5]: Microsoft Azure, 'Azure OpenAI in Azure AI Foundry Models content filtering' (2025).

Sentiment analysis uses natural language processing models to score text polarity.[^6] This processing evaluates the data subject's attitudes and opinions — personal aspects within Article 4(4) GDPR's definition of profiling. Where submissions concern matters of public policy, sentiment analysis risks processing special category data revealing political opinions under Article 9.

[^6]: GDPR Advisor, 'How GDPR Affects AI-Powered Social Listening and Sentiment Analysis' (2024).

Stance detection employs supervised learning models to classify positions toward specific policy proposals.[^7] This constitutes profiling of political opinions with heightened risk where used to filter outliers or minority views.

[^7]: On stance detection methodologies, see MedRxiv, 'Artificial intelligence-enabled analysis of UK and US public attitudes on Facebook and Twitter towards COVID-19 vaccinations' (2020).

Summarisation through generative models compresses large text volumes into executive summaries, necessarily involving editorial decisions about inclusion and exclusion.[^8] The omission of nuances or minority viewpoints from summaries presented to human decision-makers constitutes an automated determination of relevance with potentially decisive effects. This risk is particularly acute with large language models, which may exhibit statistical biases favouring dominant viewpoints while marginalising unconventional perspectives.

[^8]: On LLM summarisation in legislative contexts, see 'Large Language Models in Legislative Content Analysis: A Dataset from the Polish Parliament' (2025) arXiv.

Prioritisation and ranking through relevance scoring orders submissions for human review, with those ranked lower receiving less attention or none at all.[^9] Even without outright exclusion, deprioritisation can effectively silence voices: if reviewers examine only the top-ranked portion of submissions, those in lower ranks are functionally excluded.

[^9]: On relevance ranking in information retrieval contexts, see generally C. Manning and others, *Introduction to Information Retrieval* (CUP 2008).

### B. Consultation filtering in the administrative AI landscape

Consultation filtering does not exist in isolation. AI deployment in administrative contexts spans a spectrum of applications with varying Article 22 risk profiles.

At one end of the spectrum, predictive scoring for benefit eligibility screening presents the clearest Article 22 case. An algorithm that assigns fraud probability scores to benefit applicants, with human reviewers deferring to high scores to deny or investigate, exhibits every characteristic the *SCHUFA* doctrine targets: profiling of personal aspects, determining role in outcomes affecting legal rights, and nominal human involvement that rubber-stamps algorithmic outputs.[^10] National DPA enforcement consistently treats such processing as falling within Article 22.[^11]

[^10]: See generally Article 29 Working Party, 'Guidelines on Automated individual decision-making and Profiling for the purposes of Regulation 2016/679' (WP251rev.01, adopted 3 October 2017, revised 6 February 2018) 20–21.

[^11]: Italian Garante decisions on algorithmic management in gig economy contexts demonstrate this approach: Garante per la protezione dei dati personali (Italy), Decision 9685994 of 22 July 2021 (Deliveroo Italy), imposing €2,500,000 fine.

Similarly, regulatory inspection selection based on algorithmic risk scoring — where anomaly detection flags entities for enforcement attention — creates direct legal consequences through investigative obligations, reputational harm, and potential sanctions.[^12] This constitutes paradigmatic Article 22 territory.

[^12]: The Belgian APD's approach to government algorithmic processing in the SyRI case demonstrates regulatory attention to discriminatory algorithmic selection in enforcement contexts.

At the other end, pure organisational categorisation — routing freedom of information requests to appropriate departments based on topic classification — produces minimal Article 22 risk where categorisation does not determine substantive outcomes and all requests receive equivalent treatment regardless of category.

Consultation filtering occupies an intermediate position. The processing evaluates submission content rather than personal characteristics in the manner of credit scoring. The effects on data subjects are indirect — affecting a third party's concession rather than the submitter's legal status directly. Human decision-makers retain formal authority over the ultimate administrative determination.

These features create doctrinal uncertainty. The uncertainty is not a defect in the analysis; it reflects genuine interpretive questions that Article 22's text and existing case law do not definitively resolve.

The strategic value of examining consultation filtering lies precisely in this uncertainty. Cases at the spectrum's extremes — benefit eligibility scoring at one end, organisational categorisation at the other — do not expose the interpretive gaps that require judicial or regulatory resolution. Consultation filtering exposes three such gaps: whether democratic participation effects qualify as "similarly significant"; whether content evaluation constitutes profiling; and whether procedural gatekeeping constitutes a "decision."

### C. The upstream character of filtering

The legal significance of upstream filtering lies in its invisibility. Unlike a rejected credit application where the applicant receives notification, a filtered consultation submission simply disappears from the administrative record. The submitter receives no rejection notice; the submission is technically received by the server but procedurally ineffective upon arrival.

Consider the contrast with traditional administrative refusals. When a planning application is rejected, the applicant receives a decision letter explaining grounds for refusal and avenues of appeal. When a benefits claim is denied, the claimant receives notice and reasons. These procedural protections — fundamental to administrative law across jurisdictions — are entirely absent where AI filtering operates upstream.

The citizen's submission vanishes into digital silence, generating neither acknowledgment nor explanation. The "decision" to exclude the citizen is made solely by software, frequently without the knowledge of the human authority nominally responsible for the consultation.

The European Data Protection Board's guidance on automated decision-making emphasises that the right under Article 22 exists precisely because of the risks inherent in allowing machines to make significant decisions about individuals without human oversight.[^13] Where the human decision-maker operates on a dataset already curated by AI — never seeing filtered submissions — the protective purpose of Article 22 is directly implicated.

[^13]: WP251 (n 10) 20–21.

---

## III. The "solely automated" threshold and meaningful human intervention

The first critical question concerns when processing is "solely automated" under Article 22(1). Administrative bodies routinely defend AI deployment by citing human involvement: because human officials ultimately approve policy documents or review aggregated reports, they argue the process is not solely automated.[^14] Rigorous analysis of CJEU jurisprudence reveals this defence as increasingly porous.

[^14]: See Centre for Information Policy Leadership, 'Automated Decisionmaking and Profiling (ADM) Requirements in U.S. State Privacy Laws' (2024) 8–10.

### A. The rubber-stamping phenomenon

Article 22(1) applies only where there is no human involvement in decision-making. However, regulatory guidance consistently holds that such involvement must be meaningful rather than a token gesture.[^15] The Article 29 Working Party, in its guidelines on automated decision-making now endorsed by the EDPB, specified that meaningful human intervention requires the human actor to have both the authority and competence to change the decision, and to actually exercise this authority.[^16]

[^15]: WP251 (n 10) 10.

[^16]: ibid 10–11.

In high-volume filtering contexts, the rubber-stamping phenomenon is acute. If an AI system flags 10,000 submissions as non-substantive, and a human officer approves this classification in bulk without reviewing individual contents, human involvement is merely nominal. Research into automation bias confirms that humans are cognitively predisposed to trust automated outputs, particularly under time pressure or when dealing with massive datasets.[^17]

[^17]: See JuLIA Project, 'Handbook: AI and Public Administration: The (legal) limits of algorithmic governance' (2025) 24–26.

The Berlin Data Protection Authority's 2023 enforcement action against a bank illustrates this principle in practice. The authority imposed a €300,000 fine where automated credit card rejection occurred without meaningful explanation, notwithstanding nominal human involvement.[^18] The authority emphasised that when controllers employ automated decision-making tools, they bear specific transparency obligations under Article 22(3) requiring concrete information about the database used, the factors and the criteria influencing the decision.

[^18]: BlnBDI (Berlin) Decision of 31 May 2023, imposing €300,000 fine for Article 15(1)(h) and Article 22(3) violations.

Where standard administrative procedure involves trusting AI filter classifications, the process is de facto solely automated. The EDPB has clarified that controllers cannot fabricate human involvement to avoid Article 22 provisions.[^19]

[^19]: WP251 (n 10) 10: 'The controller cannot avoid the Article 22 provisions by fabricating human involvement.'

### B. The SCHUFA doctrine: the determining role test

The CJEU's *SCHUFA* ruling provides the decisive analytical framework.[^20] The case concerned credit scoring algorithms used by SCHUFA, a credit reference agency. Banks argued that SCHUFA did not make automated decisions because human employees made final lending determinations. The Court rejected this characterisation.

[^20]: *SCHUFA* (n 2).

The Court held that automated score generation constitutes a "decision" under Article 22 where it plays a determining role in downstream decisions. Three cumulative conditions must be met for Article 22(1) to apply: a decision must exist; that decision must be based solely on automated processing; and it must produce legal effects or similarly significantly affect the data subject.[^21]

[^21]: ibid paras 47–48.

The Court reasoned purposively: interpreting Article 22 to require the final formal act to be automated would enable controllers to circumvent GDPR protections by inserting a human intermediary.[^22] If circumvention through a human straw man were permitted, Article 22 would be deprived of practical effect.

[^22]: ibid paras 56–65; see also AG Pikamäe Opinion in C-634/21 ECLI:EU:C:2023:220 paras 35–42.

Applying the *SCHUFA* framework to public consultations: where an AI filter's classification of a submission as irrelevant leads to its exclusion from policy deliberation in essentially all cases, the AI has played a determining role. The filter is the decision-maker regarding that citizen's participatory access.

### C. The upstream trap

The *SCHUFA* doctrine is even more potent where rejected content is never presented to humans. In *SCHUFA*, bank employees at least saw scores and applications. In AI-moderated consultations, if systems auto-archive comments flagged as non-substantive without human queue review, the determining role is absolute. Human policymakers remain unaware that decisions have been made to exclude specific feedback.

This creates what might be termed the upstream trap: administration claims a human made the decision (the policy), but the dataset underlying that decision was curated solely by AI. The upstream decision to exclude specific citizens from the dataset was solely automated, and under *SCHUFA*, this upstream determination is justiciable under Article 22.

The Austrian Data Protection Authority's decision in *DSB 2020-0.436.002* reinforces this analysis.[^23] Addressing marketing score calculation, the authority held that Article 15(1)(h)'s right to meaningful information applies to all profiling activities, not merely those falling within Article 22(1) and (4). The authority specified that information must include: parameters and input variables; their effect on scoring; explanation of why the data subject received particular results; and possible profile categories. The authority rejected trade secret arguments, holding that rights under Articles 8 ECHR and 8 CFR cannot be subordinated to commercial confidentiality.

[^23]: DSB (Austria) Decision 2020-0.436.002 of 8 September 2020, ECLI:AT:DSB:2020:2020.0.436.002.

The Finnish Data Protection Authority's decision in case 6482/186/2020 provides the most direct support for this analysis in the administrative context.[^23a] The authority examined a health benefit assessment tool that used algorithms to identify patients for proactive healthcare measures. The authority drew a critical distinction between two categories: patients selected by the algorithm for human review, and patients not selected. For the former, the authority found no solely automated decision because healthcare professionals made final assessments considering other factors. For the latter, however, the authority held that the result of the profiling remains final and the person no longer re-evaluates the evaluation produced by the tool. The non-selection by the algorithm constituted a solely automated decision because no human subsequently reconsidered the algorithmic determination.

[^23a]: Tietosuojavaltuutetun toimisto (Finland) Decision 6482/186/2020 of 2 June 2021.

Applied to consultation filtering, this reasoning is directly on point. When AI filtering excludes submissions from human review, the exclusion is the solely automated decision. Humans only review the selected submissions; those not selected never receive human consideration. The algorithmic determination that a submission is not sufficiently substantive for human attention remains final — precisely the situation the Finnish authority identified as triggering Article 22.

### D. The physical impossibility of meaningful review

The Spanish AEPD developed the most sophisticated framework for assessing meaningful human involvement in March 2024 guidance responding to *SCHUFA*.[^24] The four-factor test requires: competence (authority to alter outcomes); preparation and training (ability to critically evaluate); independence and diligence (freedom from authority bias); and means to exercise competence (procedural ability, informational access, resources, and sufficient time).

[^24]: Autoriteit Persoonsgegevens (Netherlands), 'Consultation on automated decision-making guidelines' (2025), developing similar framework.

The Spanish framework includes practical feasibility calculations. If a human reviews 100 automated reports of 100 pages daily, this yields only 21 pages per minute — physically impossible to conduct meaningful assessment. Similarly, decisions about flight boarding or event access occurring in seconds lack procedural feasibility for human intervention.

Applied to consultation filtering, these criteria expose structural impossibility. Where an authority receives 50,000 consultation submissions and AI filters 30% as non-substantive, meaningful human review of 15,000 filtered submissions is practically impossible within administrative timelines. The human involvement that would defeat "solely automated" classification simply cannot occur at scale.

This structural impossibility distinguishes consultation filtering from cases where meaningful human intervention is merely absent (the rubber-stamping phenomenon) and cases where it is affirmatively impossible (the physical impossibility problem). The latter strengthens the Article 22 analysis because the authority cannot credibly claim that human review could have occurred but did not.

---

## IV. Information gatekeeping as justiciable "decision"

The second unresolved question concerns the ontology of "decision" itself. Public authorities typically characterise filtering as preparatory — a processing step rather than a decision with legal standing. This distinction, rooted in traditional administrative law, faces significant challenge under GDPR's broader definitions.

### A. The invisible rejection and preparatory acts

In traditional administrative law, judicial review is often limited to final decisions definitively determining individuals' legal positions.[^25] Intermediate measures — internal memoranda, preparatory reports — are generally unreviewable unless they produce independent legal effects. Public bodies argue that AI summaries or filtered datasets constitute intermediate measures preparing for final regulation.

[^25]: See generally ReNEUAL, 'The Pan-European General Principles on Digitalisation of Public Administration' (2024).

*SCHUFA* explicitly dismantled this preparatory act defence in automated processing contexts. The Court held that classifying automated scores as merely preparatory would create a lacuna in legal protection.[^26] If data subjects cannot challenge automated scores because they are preparatory and cannot challenge final decisions on grounds of scoring because final decision-makers lack algorithmic logic, rights under Article 22 and Article 15(1)(h) are nullified.

[^26]: *SCHUFA* (n 2) para 58.

Applying this to consultations, the structural parallels are striking.

The act of exclusion operates as follows: when an AI tool marks a submission "do not process," that is a final determination regarding that data packet. For the citizen, the process has ended; their input will not be heard. The algorithmic classification represents the terminus of that citizen's participatory effort.

The lack of remedy compounds the problem: if exclusion is treated as merely preparatory, citizens have no recourse. They cannot challenge final policy on grounds that their specific comment was auto-deleted, because policymakers are likely unaware of the deletion.

To ensure effective legal protection, information gatekeeping — the filtering itself — must qualify as a "decision" within Article 22(1).

### B. When procedural determinations become substantive decisions

A counterargument presents itself: that filtering constitutes administrative housekeeping rather than a substantive decision. Routing, sequencing, and categorisation decisions that do not directly determine outcomes but affect their likelihood arguably fall outside Article 22's scope.

This counterargument fails when examined functionally.

The *SCHUFA* Court's focus on "determining role" requires examining whether the algorithmic classification predetermines the outcome for the individual, not whether the classification formally constitutes the final administrative act. A routing decision that directs complaints to departments with dramatically different dismissal rates is functionally determinative. A categorisation decision that assigns benefit applications to frameworks with different eligibility criteria determines applicable law. A prioritisation decision that creates delays effectively denying time-sensitive rights produces substantive consequences.

Consultation filtering exhibits this functional determinativeness. The question is not whether filtering formally constitutes the concession decision — it does not. The question is whether filtering determines, for the excluded submitter, whether their participatory effort will be considered. When the answer is yes in essentially all cases, the filtering plays a determining role.

The EDPB's guidance supports this functional analysis. Automated decisions can be made with or without profiling; profiling can take place without making automated decisions.[^27] The key is whether automated processing produces determinations affecting individuals. A determination that a citizen's submission will not be considered is precisely such a determination.

[^27]: WP251 (n 10) 10.

### C. Summarisation as decision-making

The issue extends beyond binary acceptance/rejection to summarisation nuance. Generative AI models synthesise thousands of comments into key themes reports, involving editorial decisions: selecting which points are key and which peripheral.[^28]

[^28]: Whitehead (n 1).

If an LLM tasked with summarising 50,000 comments on controversial legislation hallucinates or statistically marginalises valid minority objections, that objection is effectively excised from the record.[^29] The decision is the determination of relevance.

[^29]: On LLM hallucination risks, see D. Magesh and others, 'Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models' (2024) 16 Journal of Legal Analysis 64.

Legal scholarship recognises that AI summarisation is not neutral data compression but normative content evaluation.[^30] When this evaluation determines whether citizens' arguments reach human decision-makers, it constitutes a decision affecting participation rights. The non-deterministic, opaque nature of LLMs — where inclusion/exclusion logic cannot be verified — exacerbates legal risk, preventing administration from confirming whether summarisation was fair or arbitrary.

[^30]: MDPI, 'GDPR and Large Language Models: Technical and Legal Obstacles' (2025) Future Internet 151.

The February 2025 *Dun & Bradstreet Austria* judgment significantly strengthens this analysis.[^31] The Court clarified that meaningful information about the logic involved under Article 15(1)(h) requires explanation of the procedure and principles actually applied — not merely technical descriptions or statistical abstractions, but practical explanation of how the algorithm functions relative to the specific data subject. Information must facilitate comprehension of decision-making rationale and enable effective exercise of data subject rights, including the ability to contest decisions knowledgeably.

[^31]: *Dun & Bradstreet Austria* (n 2) paras 47–52.

The Court held that trade secrets do not excuse transparency obligations. Controllers must find means to explain logic while protecting legitimate business interests; judicial authorities and DPAs can access algorithmic information for enforcement purposes. Applied to consultation summarisation, authorities cannot simply claim that LLM reasoning is proprietary or too complex to explain.

---

## V. Legal and similarly significant effects in administrative contexts

A pivotal defence for public authorities is that consultation responses are merely consultative. Unlike credit denial or employment termination, ignoring comments arguably produces neither legal effects nor similarly significant effects required by Article 22.

This defence requires examination.

### A. Legal effects: the Aarhus Convention and statutory participation rights

The legal effect threshold is met when decisions impact legal status or rights under contract or law.[^32] In environmental governance, the Aarhus Convention and implementing EU Directive (2011/92/EU) grant explicit legal rights to participate in decision-making.

[^32]: WP251 (n 10) 11–12.

Article 6 of the Aarhus Convention requires that due account be taken of public participation outcomes.[^33] If AI filtering systematically excludes relevant submissions — flagging environmental concerns as off-topic in planning consultations, for instance — the authority fails to take due account. In EU administrative law, breach of essential procedural requirements — including failure to consider mandatory public input — can lead to annulment of final decisions.[^34]

[^33]: Convention on Access to Information, Public Participation in Decision-Making and Access to Justice in Environmental Matters (adopted 25 June 1998, entered into force 30 October 2001) 2161 UNTS 447 (Aarhus Convention) art 6.

[^34]: See Case C-72/12 *Gemeinde Altrip* ECLI:EU:C:2013:712; EIA Directive 2011/92/EU.

Automated filtering produces legal effect: it violates statutory rights to be heard and potentially renders entire administrative proceedings unlawful. The decision to exclude comments is a decision to deny exercise of statutory rights.

The CJEU's judgment in *OT v Vyriausioji tarnybinės etikos komisija* (C-184/20) reinforces necessity and proportionality requirements for processing affecting fundamental rights.[^35] Indirect revelation of sensitive data still counts as special category processing. Where consultation filtering reveals or infers political opinions, these enhanced protections apply.

[^35]: Case C-184/20 *OT v Vyriausioji tarnybinės etikos komisija* ECLI:EU:C:2022:601.

### B. Similarly significant effects: the access-to-opportunity framework

Beyond strict statutory rights, Article 22 covers similarly significant effects. The EDPB interprets this to include decisions affecting behaviour, choices, access to services, or resulting in discrimination.[^36]

[^36]: WP251 (n 10) 21–22.

The EDPB's guidelines identify automated decisions affecting access to services as producing similarly significant effects.[^37] Credit scoring that determines borrowing access, employment screening that gates job opportunities, and tenant scoring that affects housing availability all fall within Article 22's scope precisely because they control access to important life resources.

[^37]: ibid.

Public consultation participation operates analogously.

Citizens engage in consultations to influence policy outcomes affecting their lives, communities, and interests. The opportunity to participate — to have one's views considered in governmental deliberation — constitutes access to a democratic service fundamental to citizenship. When AI filtering determines which citizens gain this access and which do not, it produces effects similar to those recognised in commercial contexts.

The Italian Garante's 2021 decision against Deliveroo Italy provides instructive analogy.[^38] The authority imposed a €2,500,000 fine for inadequate transparency about algorithms managing riders' work shifts. The shift booking system allocated work opportunities based on automated scoring of rider reliability and availability. The Garante emphasised that profiling carried out by the company produces a significant effect on the rider concerned, consisting in the possibility of allowing or denying access to job opportunities.

[^38]: Deliveroo (n 11).

The parallel to consultation filtering is direct. Like the Deliveroo shift booking system, AI filtering of consultation submissions determines access to a valuable opportunity — the opportunity to have one's voice considered in democratic deliberation. Like riders denied shifts, citizens whose submissions are filtered never receive notification of the algorithmic determination affecting them.

The Finnish Data Protection Authority's reasoning on significant effects merits particular attention.[^38a] The authority rejected the controller's argument that no services were denied by the algorithm. Instead, the authority held that it is sufficient that the profiling actually affects the patient's chances of receiving healthcare services. Being excluded from proactive healthcare measures — not receiving an invitation for preventive care that others received based on algorithmic selection — constituted significant effects. The authority emphasised that in terms of significant effects, it is not necessary for the patient to be actively denied access to the treatment; it is sufficient that the profiling actually affects the patient's chances of receiving healthcare services.

[^38a]: Tietosuojavaltuutetun toimisto (Finland) Decision 6482/186/2020 (n 23a).

Applied to consultation filtering, this reasoning supports recognising exclusion from consideration as producing significant effects. The submitter's chances of having their voice considered are affected by the algorithmic determination, even without formal denial of participation rights. The citizen is not told they cannot submit — they submit, and the submission is received. But the algorithmic classification affects their chances of having that submission reach human consideration, just as algorithmic classification affected patients' chances of receiving proactive healthcare. The Finnish authority's rejection of the "active denial" requirement provides direct precedent for treating algorithmic exclusion from opportunity as producing significant effects under Article 22.

### C. Democratic participation as similarly significant: the argument

No CJEU case law addresses whether exclusion from democratic participation constitutes similarly significant effects under Article 22. This is a gap in the doctrine, not a settled answer.

The argument that such exclusion should qualify proceeds on three grounds.

First, Article 22's fundamental rights purpose supports extension to democratic participation. The provision exists to protect individuals from algorithmic determinations of significant outcomes without human oversight. Democratic participation — the opportunity to influence governmental decisions affecting one's life — is significant. Where algorithms determine who participates and who does not, the protective purpose is engaged regardless of whether the effects are commercial or civic.

Second, the Charter of Fundamental Rights integrates democratic participation into the fundamental rights framework. Article 11 protects freedom of expression, including the right to receive and impart information without interference.[^39] Article 41 establishes the right to good administration, including the right to be heard before any adverse measure is taken.[^40] Article 47 guarantees effective remedy.[^41] Algorithmic filtering that prevents submissions from reaching decision-makers interferes with these rights. Interpreting Article 22 to exclude democratic participation effects would create incoherence within the Charter framework.

[^39]: Charter of Fundamental Rights of the European Union [2012] OJ C326/391 art 11.

[^40]: ibid art 41.

[^41]: ibid art 47.

Third, the *SCHUFA* Court's anti-formalist reasoning supports functional analysis. The Court rejected the argument that Article 22 applies only to formal final decisions, emphasising that such interpretation would enable circumvention.[^42] The same reasoning applies to the indirect effects objection. If Article 22 does not apply because the filtered citizen's submission concerned a third party's concession rather than their own legal rights, controllers could systematically exclude citizens from participation by characterising all consultations as affecting third-party interests.

[^42]: *SCHUFA* (n 2) paras 56–65.

The relevant effect is not on the concession decision but on the data subject's participatory rights. The submitter's right to have their submission considered — a right grounded in the Aarhus Convention, EU administrative law principles, and the Charter — was algorithmically denied. That denial produces effects on the data subject regardless of whose concession is at stake.

### D. Counterarguments addressed

Two counterarguments require response.

The first contends that participation effects are too indirect or speculative to qualify. The submission might not have changed the outcome; the concern might have been addressed through other channels; the individual retains other avenues for political engagement.

This argument proves too much. Credit scoring affects probability of loan approval, not certainty. Employment screening affects likelihood of consideration, not guarantee of hire. Article 22 applies to these contexts because algorithmic determination of opportunity access is significant, not because outcomes are certain. The same logic applies to consultation filtering: algorithmic exclusion from consideration is significant regardless of whether inclusion would have changed the result.

The second counterargument asserts that extending Article 22 to democratic participation would impose unworkable burdens on public administration. Authorities would need to ensure human review of all submissions or face Article 22 liability, eliminating the efficiency benefits AI provides.

This argument conflates the scope question with the compliance question. If Article 22 applies to consultation filtering, authorities must comply with its requirements — providing safeguards under Article 22(3), obtaining legal authorisation under Article 22(2)(b), or restructuring AI deployment to ensure meaningful human involvement. These requirements impose costs. But the argument that compliance is burdensome does not establish that the provision should not apply. Credit scoring, employment screening, and benefit eligibility determinations all impose compliance costs. The question is whether the protective purpose of Article 22 extends to democratic participation, not whether compliance is convenient.

---

## VI. Profiling, content evaluation, and the "about whom" problem

A common technical defence asserts that NLP tools analyse content (text), not people (data subjects), therefore processing is not profiling under Article 4(4). This distinction is both ontologically and legally precarious.

### A. Inferring personal aspects from text

Article 4(4) defines profiling as automated processing to evaluate personal aspects, including personal preferences, interests, reliability, behaviour.[^43] Modern NLP techniques — sentiment analysis and stance detection — are designed precisely to evaluate these aspects.

[^43]: GDPR, art 4(4).

Sentiment as preference: when AI analyses submissions to determine if authors are angry, satisfied, or neutral, it evaluates personal preferences and emotional states.

Stance as interest: classifying submissions as pro-policy or anti-policy evaluates data subjects' interests and reliability regarding proposed measures.

Linkage to identity: even where text is anonymised, modern practices often link submissions to accounts or identifiers to detect duplicate submissions. Once this link exists, text analysis becomes profiling of identifiable natural persons.

The Austrian DSB's *2020-0.436.002* decision directly addressed this issue.[^44] Marketing scores calculating probability percentages for classification into categories such as conservatives, traditionalists, or digital individualists constituted profiling under Article 4(4). The authority emphasised that processing need not be solely automated to constitute profiling — any automated evaluation of personal aspects suffices.

[^44]: DSB (Austria) 2020-0.436.002 (n 23).

### B. The "about whom" problem: when content evaluation becomes person evaluation

Article 22 protects data subjects from automated decisions "about" them. A critical question arises: when does processing of submissions become evaluation of submitters?

The technical argument that NLP analyses content rather than people collapses upon examination. Submission evaluation inherently evaluates personal aspects because arguments, reasoning, and expression are personal aspects. The submission is the person's communicative act; evaluating the submission evaluates the person's behaviour as a communicator, their interests as revealed through their arguments, and their reliability as a participant in deliberation.

Sentiment analysis evaluates emotional state — clearly personal.

Relevance scoring evaluates the perceived value of the person's contribution — an assessment of their reliability or competence as a participant.

Quality assessment evaluates communicative competence — the person's performance in the act of democratic expression.

The Deliveroo enforcement illustrates this point. The Garante found the algorithm evaluated riders, not just shifts, because work allocation evaluated rider characteristics.[^45] The same reasoning applies: consultation filtering evaluates submitters, not just submissions, because filtering evaluates submitter characteristics as expressed through their submissions.

[^45]: Deliveroo (n 11).

A functional test emerges: if AI classification determines how a person is treated based on evaluation of their communicative acts, this constitutes profiling of personal aspects. The output — inclusion or exclusion — determines how the person is treated. The input — evaluation of their submission's sentiment, stance, quality, or relevance — evaluates personal aspects expressed through communication.

### C. Sentiment analysis as special category data processing

Legal stakes escalate dramatically where inferred personal aspects include political opinions. Under Article 9, data revealing political opinions constitutes special category data; processing is generally prohibited.[^46]

[^46]: GDPR, art 9(1).

In consultations regarding controversial legislation — migration, tax reform, environmental regulation — submissions expressing strong opposition inherently reveal political opinions. If NLP models categorise submissions as opposed with negative sentiment, they process special category data.

Article 22(4) explicitly prohibits automated decisions based on special category data unless the subject has given explicit consent, or processing is necessary for substantial public interest with suitable measures in place.[^47]

[^47]: GDPR, art 22(4).

Public authorities rarely obtain explicit consent to profile political sentiment for filtering purposes. The substantial public interest defence is weak for mere administrative efficiency. Using sentiment analysis to deprioritise negative feedback constitutes prima facie violation of Article 22(4).

The EDPB's WP251 guidelines acknowledge that profiling can create special category data by inference from data not itself special category but becoming so when combined.[^48] Consultation comments combined with stance detection infer political convictions. Controllers must ensure they have lawful basis for special category processing and inform data subjects of such processing.

[^48]: WP251 (n 10) 15.

### D. The content-person distinction reconsidered

The argument that NLP analyses content rather than people faces a deeper conceptual challenge. Text analysis in consultation contexts necessarily evaluates what the author has written — their arguments, their reasoning, their expression. This is not content-neutral deduplication but evaluation of the communicative act the person has performed.

Article 4(4) defines profiling as evaluating personal aspects including interests, reliability, and behaviour. When AI classifies a submission as off-topic, low-quality, or non-constructive, it evaluates the submitter's behaviour (the act of making a particular type of submission) and implicitly their reliability as a participant in democratic deliberation.

This analysis finds support in the Court of Justice's approach to algorithmic processing. In *SCHUFA*, the Court emphasised that automated processing affecting individuals must be subject to safeguards regardless of technical characterisation.[^49] The protective purpose of Article 22 applies wherever algorithms make determinations that affect how individuals are treated, not merely where processing fits neatly into predefined technical categories.

[^49]: *SCHUFA* (n 2) paras 56–65.

---

## VII. Safeguards and the Article 22(2)(b) exception

Article 22(2)(b) provides an exception for automated decisions authorised by Union or Member State law to which controllers are subject, provided such law establishes suitable measures to safeguard the data subject's rights. The question is whether current national administrative laws meet this standard.

### A. The adequacy of statutory authorisation

General administrative laws authorising data processing or digital government are likely insufficient to authorise solely automated filtering under strict GDPR requirements. Recital 71 mandates specific authorisation.[^50]

[^50]: GDPR, Recital 71.

German framework: Section 35a of the Administrative Procedure Act (VwVfG) permits fully automated administrative acts only where permitted by a legal provision and where there is no discretion or room for independent appreciation.[^51] Evaluating public comments is inherently discretionary — weighing arguments, assessing relevance. Fully automated filtering of consultation responses likely falls outside § 35a's scope. Without specific legal basis, such filtering is unauthorised and illegal under Article 22(2)(b).

[^51]: Verwaltungsverfahrensgesetz (VwVfG) § 35a; see CERIDAP, 'Automated Decision-Making Systems in German Administrative Law' (2024).

French framework: the Code of Relations between the Public and Administration (CRPA Article L311-3-1) permits individual decisions based on algorithmic processing, provided the decision is explicitly mentioned and rules defining processing are communicated upon request.[^52] This framework imposes strict transparency conditions. If authorities use proprietary, opaque LLMs and cannot explain rules defining the processing because models are non-deterministic, they violate Article L311-3-1. Filtering becomes unlawful not because automated, but because failing the explanation safeguard.

[^52]: Code des relations entre le public et l'administration, art L311-3-1; see Défenseur des Droits, 'Algorithms, AI systems and public services: what rights do users have?' (2024).

### B. The safeguards deficit

Even where legally authorised, controllers must implement suitable measures including rights to obtain human intervention, express views, and contest decisions.[^53]

[^53]: GDPR, art 22(3).

The notice gap: in AI filtering, citizens are rarely notified that submissions were filtered. Without notification, they cannot exercise rights to contest or demand human intervention.

The black box barrier: even where citizens contest filtering, authorities may be unable to provide meaningful explanation of why LLMs rejected comments, violating the right to good administration.[^54]

[^54]: Charter of Fundamental Rights art 41.

Architectural inadequacy: current consultation procedures were designed for paper submissions; they lack procedural hooks — notification mechanisms, appeal processes — necessary for Article 22 compliance.

The Berlin DPA's enforcement action underscores these requirements.[^55] The authority held that even with automated processes, controllers must provide comprehensible information about the automated rejection, including specific information on the database and the decision-making factors as well as the criteria for rejection in individual cases. Generic descriptions of AI systems are insufficient.

[^55]: BlnBDI Decision (n 18).

### C. The Dun & Bradstreet transparency standard

The *Dun & Bradstreet Austria* judgment establishes heightened transparency requirements post-February 2025.[^56] Meaningful information about logic involved requires substantive explanation — not "algorithm processed your data" or "socio-demographic factors given equal weighting," but explanation of how specific data inputs produced the decision regarding this individual.

[^56]: *Dun & Bradstreet Austria* (n 2) paras 47–52.

The Court's holding that trade secrets do not excuse non-disclosure is particularly significant for public authorities using third-party AI systems. Where vendors claim algorithmic opacity as intellectual property, authorities cannot simply defer: they bear responsibility for ensuring systems they deploy permit compliance with transparency obligations. This may require contractual provisions mandating vendor cooperation with explanation requests, or may counsel against deploying truly opaque systems for decisions affecting fundamental rights.

For consultation filtering, these requirements pose significant practical challenges. Large language models and complex NLP systems often lack deterministic, explicable decision pathways. A sentiment classifier might assign negative polarity to a submission based on distributional patterns across thousands of training examples without identifiable reasoning that could be communicated to a layperson.

The *Dun & Bradstreet* standard suggests that such systems may be inherently unsuitable for decisions affecting individuals' fundamental rights. If the logic cannot be meaningfully explained, the transparency obligation cannot be satisfied, and deployment is prima facie unlawful.

---

## VIII. The interplay with the AI Act

The regulatory landscape tightens with the AI Act's entry into force. This legislation codifies risks identified in GDPR analysis.

### A. High-risk classification

The AI Act classifies AI systems intended for administration of justice and democratic processes as high-risk (Annex III, point 8).[^57] Systems used by public authorities that may influence democratic processes fall within this category.

[^57]: Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act) Annex III, point 8.

AI tools filtering or summarising public consultation responses directly impact democratic processes. This classification triggers stringent obligations: high-quality data governance to prevent bias, record-keeping, transparency, and human oversight.[^58]

[^58]: ibid arts 9–15.

Data governance requirements under Article 10 mandate that training, validation, and testing datasets be relevant, sufficiently representative, and free of errors.[^59] For consultation filtering systems, this requires demonstration that training data adequately represents the diversity of legitimate public input — a challenging requirement given the heterogeneity of democratic discourse.

[^59]: ibid art 10.

Human oversight under Article 14 requires measures enabling humans to understand system capacities and limitations, appropriately monitor operation, and intervene when necessary.[^60] This reinforces the meaningful intervention requirements discussed above — nominal human involvement that merely ratifies algorithmic outputs does not satisfy Article 14 any more than it satisfies Article 22 GDPR.

[^60]: ibid art 14.

### B. Fundamental rights impact assessment

Article 27 requires deployers of high-risk AI systems — specifically public bodies — to conduct Fundamental Rights Impact Assessments (FRIA) prior to deployment.[^61]

[^61]: ibid art 27.

The assessment must address specific risks of harm to affected individuals' fundamental rights: freedom of expression, good administration, non-discrimination.[^62] If authorities cannot guarantee that AI filters will not disproportionately silence minority voices or misclassify valid dissent as toxicity, FRIA should theoretically prevent deployment.

[^62]: ibid Recital 96.

The FRIA requirement represents a significant procedural safeguard absent from GDPR's Article 22 framework. For consultation filtering, the relevant fundamental rights extend beyond data protection to include freedom of expression (Article 11 CFR), the right to good administration (Article 41 CFR), and the right to effective remedy (Article 47 CFR).

A comprehensive FRIA for consultation filtering would need to assess risks to each of these rights, propose mitigation measures, and conclude that deployment is justified despite residual risks. Given the analysis in this article, conducting such an assessment honestly might lead many authorities to conclude that current filtering practices cannot be justified.

### C. Regulatory convergence

The AI Act explicitly preserves GDPR's application. Article 2(7) provides that the Regulation applies without prejudice to Union law on data protection.[^63] This means that compliance with AI Act requirements does not excuse GDPR violations — authorities must satisfy both frameworks.

[^63]: ibid art 2(7).

The AI Act's high-risk classification for systems affecting democratic processes effectively recognises what Article 22 analysis suggests — that AI in democratic contexts requires enhanced oversight. The regulatory convergence supports interpreting Article 22 to apply to consultation filtering.

---

## IX. Conclusion

This article has argued that AI filtering of public consultation submissions represents a paradigm case exposing unresolved questions in Article 22 GDPR interpretation. Three doctrinal gaps require resolution: whether democratic participation effects constitute similarly significant effects; whether content evaluation constitutes profiling of personal aspects; and whether procedural filtering determinations qualify as decisions.

The analysis demonstrates that these gaps should be resolved in favour of protection.

The *SCHUFA* doctrine's "determining role" test applies when AI classification predetermines whether citizens' participatory efforts will be considered. The fundamental rights purpose of Article 22 extends to democratic participation, where algorithmic gatekeeping determines significant outcomes for individuals. The access-to-opportunity framework developed in employment and credit contexts supports recognising consultation access as analogously significant. Content evaluation inherently evaluates personal aspects because submissions are communicative acts expressing the submitter's interests, behaviour, and reliability as a participant.

Even where doctrinal uncertainty persists, complementary frameworks establish accountability obligations. The AI Act's high-risk classification triggers FRIA, human oversight, and transparency requirements. Administrative law principles of good administration require explicable, contestable decisions. The Aarhus Convention mandates that due account be taken of public participation.

The path forward requires not rejection of technology but its disciplined deployment: systems that tag rather than filter, human review that examines rejections rather than merely ratifying acceptances, transparency that enables citizens to understand how their submissions are processed, and accountability structures ensuring that administrative convenience does not override participatory rights.

The fundamental question is not merely whether Article 22 technically applies to consultation filtering. The question is whether EU law can tolerate algorithmic gatekeeping of democratic participation without meaningful safeguards.

The answer should be no.

The right to be heard must include the right not to be silenced by an algorithm. Where AI filtering operates upstream, invisibly curating which voices reach decision-makers, the promise of digital democracy is compromised by the reality of algorithmic exclusion. Only through transparent, explicable, and contestable AI deployment can public authorities reconcile efficiency benefits with their fundamental obligations under data protection law, administrative law, and the principle of democratic governance.

---

## References

[^1]: See generally U.S. Federal Government, 'Implementing Federal-Wide Comment Analysis Tool' (Project Open Data 2024); S. Whitehead, 'From Noise to Insight: Using AI to Rethink Public Comment Analysis' (2025) Medium.

[^2]: Case C-634/21 *SCHUFA Holding and Others (Scoring)* ECLI:EU:C:2023:957; Case C-203/22 *CK v Magistrat der Stadt Wien* ECLI:EU:C:2025:131.

[^3]: *SCHUFA* (n 2) paras 56–65.

[^4]: See 'Summarizing Public Comments on Policy Proposals Using Large Language Models' (IPPA Proceedings 2024).

[^5]: Microsoft Azure, 'Azure OpenAI in Azure AI Foundry Models content filtering' (2025).

[^6]: GDPR Advisor, 'How GDPR Affects AI-Powered Social Listening and Sentiment Analysis' (2024).

[^7]: On stance detection methodologies, see MedRxiv, 'Artificial intelligence-enabled analysis of UK and US public attitudes on Facebook and Twitter towards COVID-19 vaccinations' (2020).

[^8]: On LLM summarisation in legislative contexts, see 'Large Language Models in Legislative Content Analysis: A Dataset from the Polish Parliament' (2025) arXiv.

[^9]: On relevance ranking in information retrieval contexts, see generally C. Manning and others, *Introduction to Information Retrieval* (CUP 2008).

[^10]: See generally Article 29 Working Party, 'Guidelines on Automated individual decision-making and Profiling for the purposes of Regulation 2016/679' (WP251rev.01, adopted 3 October 2017, revised 6 February 2018) 20–21.

[^11]: Italian Garante decisions on algorithmic management in gig economy contexts demonstrate this approach: Garante per la protezione dei dati personali (Italy), Decision 9685994 of 22 July 2021 (Deliveroo Italy), imposing €2,500,000 fine.

[^12]: The Belgian APD's approach to government algorithmic processing in the SyRI case demonstrates regulatory attention to discriminatory algorithmic selection in enforcement contexts.

[^13]: WP251 (n 10) 20–21.

[^14]: See Centre for Information Policy Leadership, 'Automated Decisionmaking and Profiling (ADM) Requirements in U.S. State Privacy Laws' (2024) 8–10.

[^15]: WP251 (n 10) 10.

[^16]: ibid 10–11.

[^17]: See JuLIA Project, 'Handbook: AI and Public Administration: The (legal) limits of algorithmic governance' (2025) 24–26.

[^18]: BlnBDI (Berlin) Decision of 31 May 2023, imposing €300,000 fine for Article 15(1)(h) and Article 22(3) violations.

[^19]: WP251 (n 10) 10: 'The controller cannot avoid the Article 22 provisions by fabricating human involvement.'

[^20]: *SCHUFA* (n 2).

[^21]: ibid paras 47–48.

[^22]: ibid paras 56–65; see also AG Pikamäe Opinion in C-634/21 ECLI:EU:C:2023:220 paras 35–42.

[^23]: DSB (Austria) Decision 2020-0.436.002 of 8 September 2020, ECLI:AT:DSB:2020:2020.0.436.002.

[^23a]: Tietosuojavaltuutetun toimisto (Finland) Decision 6482/186/2020 of 2 June 2021.

[^24]: Autoriteit Persoonsgegevens (Netherlands), 'Consultation on automated decision-making guidelines' (2025), developing similar framework.

[^25]: See generally ReNEUAL, 'The Pan-European General Principles on Digitalisation of Public Administration' (2024).

[^26]: *SCHUFA* (n 2) para 58.

[^27]: WP251 (n 10) 10.

[^28]: Whitehead (n 1).

[^29]: On LLM hallucination risks, see D. Magesh and others, 'Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models' (2024) 16 Journal of Legal Analysis 64.

[^30]: MDPI, 'GDPR and Large Language Models: Technical and Legal Obstacles' (2025) Future Internet 151.

[^31]: *Dun & Bradstreet Austria* (n 2) paras 47–52.

[^32]: WP251 (n 10) 11–12.

[^33]: Convention on Access to Information, Public Participation in Decision-Making and Access to Justice in Environmental Matters (adopted 25 June 1998, entered into force 30 October 2001) 2161 UNTS 447 (Aarhus Convention) art 6.

[^34]: See Case C-72/12 *Gemeinde Altrip* ECLI:EU:C:2013:712; EIA Directive 2011/92/EU.

[^35]: Case C-184/20 *OT v Vyriausioji tarnybinės etikos komisija* ECLI:EU:C:2022:601.

[^36]: WP251 (n 10) 21–22.

[^37]: ibid.

[^38]: Deliveroo (n 11).

[^38a]: Tietosuojavaltuutetun toimisto (Finland) Decision 6482/186/2020 (n 23a).

[^39]: Charter of Fundamental Rights of the European Union [2012] OJ C326/391 art 11.

[^40]: ibid art 41.

[^41]: ibid art 47.

[^42]: *SCHUFA* (n 2) paras 56–65.

[^43]: GDPR, art 4(4).

[^44]: DSB (Austria) 2020-0.436.002 (n 23).

[^45]: Deliveroo (n 11).

[^46]: GDPR, art 9(1).

[^47]: GDPR, art 22(4).

[^48]: WP251 (n 10) 15.

[^49]: *SCHUFA* (n 2) paras 56–65.

[^50]: GDPR, Recital 71.

[^51]: Verwaltungsverfahrensgesetz (VwVfG) § 35a; see CERIDAP, 'Automated Decision-Making Systems in German Administrative Law' (2024).

[^52]: Code des relations entre le public et l'administration, art L311-3-1; see Défenseur des Droits, 'Algorithms, AI systems and public services: what rights do users have?' (2024).

[^53]: GDPR, art 22(3).

[^54]: Charter of Fundamental Rights art 41.

[^55]: BlnBDI Decision (n 18).

[^56]: *Dun & Bradstreet Austria* (n 2) paras 47–52.

[^57]: Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act) Annex III, point 8.

[^58]: ibid arts 9–15.

[^59]: ibid art 10.

[^60]: ibid art 14.

[^61]: ibid art 27.

[^62]: ibid Recital 96.

[^63]: ibid art 2(7).
