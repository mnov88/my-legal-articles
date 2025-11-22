# Algorithmic Gatekeeping in Administrative Consultations: A Doctrinal Analysis of Article 22 GDPR

## Introduction: The gatekeeping problem in automated governance

An awarding authority uses AI to summarize public consultation submissions on a power plant concession. The algorithm omits a submission that "may have led to refusal" of the concession. This hypothetical crystallizes fundamental tensions in GDPR Article 22's applicability: Does algorithmic information filtering constitute a "decision"? Must effects be direct rather than mediated through subsequent human judgment? When does content processing become evaluation of "personal aspects"? These questions reveal Article 22's contested boundaries in multi-stage governmental decision-making.

The CJEU's recent SCHUFA decision (C-634/21, 7 December 2023) provides crucial interpretive guidance, establishing that Article 22 receives broad purposive interpretation to prevent circumvention. Yet significant doctrinal uncertainties remain regarding algorithmic gatekeeping functions, indirect effects, and the boundaries between content analysis and profiling. This analysis examines these questions through systematic engagement with CJEU jurisprudence, EDPB guidance, ECtHR case law, and scholarly debates, revealing both the potential applicability of Article 22 and significant gaps that other legal frameworks must fill.

---

## 1. What Constitutes a "Decision" Under Article 22: The Boundaries of Algorithmic Gatekeeping

### 1.1 CJEU's Expansive "Decision" Definition in SCHUFA

The CJEU established in **SCHUFA Holding (C-634/21)** that "decision" receives broad interpretation. At **paragraph 46**, the Court held that a decision is "capable of including a number of acts which may affect the data subject in many ways," explicitly encompassing probability values and credit scores. This breadth was intentional—the Court at **paragraph 61-63** rejected narrow interpretation that would create a "lacuna in legal protection."

Critically, **paragraph 50** established the "determining role" test: where an automated probability value "plays a determining role" in subsequent decisions, establishment of that value constitutes a decision under Article 22(1). The Court at **paragraph 73** applied this to credit scoring where third parties "draw strongly on" the score—in the factual circumstances, insufficient scores led to denial "in almost all cases" (approximately 80%).

**Ratio decidendi**: A preparatory automated act constitutes an Article 22 "decision" when it plays a determining role in outcomes affecting data subjects, even if a separate entity makes the formal final decision.

### 1.2 Does Algorithmic Omission/Filtering Constitute a "Decision"?

The SCHUFA logic extends naturally to information filtering. If generating information that determines outcomes constitutes a "decision," then **omitting information that would determine outcomes** should equally qualify. The Court's anti-circumvention reasoning at paragraphs 61-63 supports this: controllers cannot avoid Article 22 by structuring processing as "mere information provision" when that information determines results.

However, the **WP251 Guidelines** (Article 29 Working Party, revised 6 February 2018) at **page 20-21** distinguish between decisions and recommendations: "An automated process produces what is in effect a recommendation concerning a data subject. If a human being reviews and takes account of other factors in making the final decision, that decision would not be 'based solely' on automated processing."

The tension is evident: SCHUFA suggests preparatory acts can be "decisions," while WP251 indicates human involvement breaks Article 22 applicability. The resolution lies in the **"draws strongly on"/"determining role" test**—if the filtering so constrains options that the human decision-maker effectively rubber-stamps the algorithmic output, it remains within Article 22 scope.

### 1.3 Multi-Stage Decision-Making and the "Solely Automated" Requirement

**Veale & Binns** ("Is That Your Final Decision?" 11 Int'l Data Privacy L. 319, 2021) identify five complications in multi-stage profiling, most relevantly the "upstream foreclosure" problem: automated steps that foreclose downstream outcomes despite nominal human involvement. They argue Article 22's focus on "final decisions" ignores how prior automated processing constrains choice architecture.

**Kaminski** ("The Right to Explanation, Explained," 34 Berkeley Tech. L.J. 189, 2019, at 197-198) emphasizes that WP251 clarifies human involvement must be **"meaningful"**—performed by someone with "authority and competence to change the decision" who conducts "thorough assessment." Merely having humans in the process does not defeat Article 22 if they lack effective power to diverge from algorithmic recommendations.

**National court precedent** reinforces this. The **Portuguese DPA** found university proctoring software violated GDPR principles where humans could make final decisions but lacked "clear instructions about when to follow the AI system's recommendations or not" (FPF Report, "Automated Decision-Making Under the GDPR," May 2022, Case 26). The **Austrian jobseekers case** (Case 9) similarly required clear instructions and training for human decision-makers.

**Application to consultation filtering**: If the authority's decision-makers receive only the AI-generated summary without access to filtered-out submissions, and lack clear instructions on when to seek additional input, the filtering may constitute a "solely automated" decision despite the human making the final concession determination.

### 1.4 The Boundary Problem: When Does Preprocessing Become Decision-Making?

No clear CJEU guidance exists on when information filtering crosses from preprocessing to decision-making. **ICO guidance on content moderation** (March 2024) suggests sophistication matters: simple matching to prohibited material lists determined by humans likely doesn't qualify, while "sophisticated systems making predictions based on context" that significantly affect outcomes does qualify.

The doctrinal boundary appears to turn on **two factors**:

**First, determinative effect**: Does the filtering functionally determine outcomes, or merely organize information for human judgment? SCHUFA's 80% correlation suggests a high but not absolute threshold.

**Second, evaluation of personal aspects**: Does the system evaluate characteristics of the submitter (profiling) or merely analyze content? WP251 at page 7 distinguishes classification based on known characteristics without evaluation from genuine profiling involving assessment of personal aspects.

**Academic consensus** (Binns & Veale, Kaminski, Malgieri) suggests Article 22 should extend to upstream filtering that substantially constrains downstream choices, but acknowledges current jurisprudence leaves this uncertain.

---

## 2. Direct vs. Indirect Effects: Must Decisions Be "About" or Can They Merely "Affect"?

### 2.1 CJEU's Textual Focus on Data Subjects Being "Subject To" Decisions

Article 22(1) protects the right "not to be **subject to** a decision based solely on automated processing." This language suggests the data subject must be the **object** of the decision, not merely affected by it. SCHUFA's facts involved decisions directly about the applicant—her creditworthiness was being assessed.

Yet the Court's broad interpretation at paragraph 46 ("capable of including a number of acts which may affect the data subject **in many ways**") emphasizes effects rather than formal subject matter. The language "affect the data subject" appears more expansive than "decisions about the data subject."

### 2.2 Third-Party Decision Scenarios: WP251's Explicit Recognition

**WP251 at page 22** explicitly addresses third-party scenarios: "Similarly significant effects could also be triggered by the actions of individuals other than the one to which the automated decision relates."

The Guidelines provide a striking example: "A credit card company might reduce a customer's card limit, based not on that customer's own repayment history, but on non-traditional credit criteria, such as an analysis of other customers living in the same area who shop at the same stores. This could mean that someone is deprived of opportunities based on the actions of others."

This example demonstrates EDPB recognition that Article 22 extends beyond decisions formally "about" the data subject to decisions that **significantly affect** them based on algorithmic processing. The formal subject matter (other customers' behavior) differs from the affected party (the specific customer), yet Article 22 applies.

### 2.3 Application to Consultation Scenarios: The Attenuation Problem

The hypothetical presents **two-degree attenuation**:
- **First degree**: The AI decision is about consultation inputs (which to include/omit)
- **Second degree**: The consultation summary informs the concession decision about the company
- **Effect on individual**: The citizen who submitted input has reduced influence on a decision affecting their interests

**Argument for applicability** (broad interpretation):
Following WP251's logic, the citizen is "deprived of opportunities based on the actions of others" (the algorithm's filtering decision). The formal subject matter (which inputs to summarize) differs from the affected party (citizens seeking to influence environmental decisions), but effects may be similarly significant.

**Argument against applicability** (narrow interpretation):
The decision is not "about" the citizen at all—it concerns the company's concession application. The citizen is a **third party** to the actual decision. Article 22 protects those "subject to" decisions, requiring them to be decision objects, not merely affected bystanders.

**Scholarly perspectives diverge**:

**Veale & Binns** (at 327-328) identify this as the "indirect effects" problem: "If 'automated' steps which indirectly produce qualifying effects are within scope when the further step is also automated, why would they not also be in scope when the further step is taken by a human?" They leave this tension unresolved.

**Malgieri** ("Automated Decision-Making in the EU Member States," 35 Computer L. & Security Rev. 2019) suggests a **two-step approach**: distinguish profiling (generating information) from decision-making (using information). This would classify consultation filtering as profiling subject to general GDPR obligations but not necessarily Article 22 unless it produces legal/similarly significant effects on the filtered individuals themselves.

### 2.4 Directness of Causal Chain: How Attenuated Is Too Attenuated?

No CJEU case law establishes causation thresholds for Article 22. SCHUFA involved direct causation—the automated score directly influenced decisions about the applicant. The consultation scenario involves **mediated causation**—the filtering influences the summary which influences the concession decision which affects citizens.

**Administrative law analogues** may inform interpretation. In **EU standing jurisprudence** for judicial review (Article 263 TFEU), the CJEU requires challengers to be "directly and individually concerned." The test is strict—regulatory acts affecting broad classes don't confer individual standing without showing direct effect on the particular applicant.

By analogy, Article 22 may require **direct effects** on the data subject, not effects mediated through multiple decision stages. The citizen's harm is contingent on: (1) what the omitted input would have said, (2) whether the authority would have been persuaded, (3) whether this would have changed the concession decision. This contingency chain may be too attenuated.

**Counter-argument**: Article 22 serves **different purposes** than standing requirements. Standing doctrine gatekeeps access to courts; Article 22 protects fundamental rights to avoid automated subordination. Purposive interpretation (SCHUFA paragraphs 61-63) supports broader applicability despite attenuation.

---

## 3. Profiling vs. Content Processing: Evaluating "Personal Aspects"

### 3.1 Article 4(4) Definition and the Personal Aspects Requirement

Article 4(4) defines profiling as "automated processing of personal data consisting of the use of personal data to **evaluate certain personal aspects** relating to a natural person, in particular to analyse or predict aspects concerning that natural person's performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements."

**WP251 at pages 6-7** establishes three elements:
1. Automated processing
2. Of personal data  
3. To **evaluate personal aspects** about a natural person

The Guidelines at page 7 emphasize: "The use of the word 'evaluating' suggests **assessment or judgement about a person**." They distinguish classification based on known characteristics for statistical purposes (not profiling) from using data to evaluate behavior, preferences, reliability (profiling).

### 3.2 The WHAT vs. WHO Distinction: Does Content Analysis Evaluate Personal Aspects?

**Critical question**: If AI analyzes **what was said** (content relevance, salience, technical merit) rather than **who said it** (submitter credibility, reliability, demographic characteristics), does this constitute "evaluation of personal aspects"?

**Argument that content analysis is NOT profiling**:

WP251's examples focus on evaluating characteristics **of the person**—creditworthiness, job performance, health, preferences. Analyzing argument quality, technical merit, or logical coherence evaluates **the communication**, not the communicator. The AI need not infer anything about the submitter's personal characteristics to determine content salience.

**ICO guidance on content moderation** (2024) suggests content matching determined by humans (e.g., matching posts to prohibited material databases) does not evaluate personal aspects, thus not profiling.

**Argument that content analysis DOES evaluate personal aspects**:

**Hildebrandt** ("Profiling and the Rule of Law," 1 Identity Info. Soc. 55, 2008) argues advanced profiling "answer[s] questions we did not raise" and "generate[s] knowledge we did not anticipate." Even ostensibly content-based analysis may implicitly evaluate submitter characteristics.

If the AI assesses submission **"quality," "thoroughness," or "technical sophistication,"** these inherently evaluate the submitter's capabilities, expertise, or diligence—personal aspects per Article 4(4). The listed examples include "performance at work" and "reliability," which could encompass quality of intellectual work products.

### 3.3 Edge Cases: Credibility, Weighting, Salience Based on Submitter Type

**Scenario 1: Credibility assessment**. If the AI weights submissions differently based on whether the submitter is a scientist, industry representative, or ordinary citizen, this explicitly evaluates personal aspects (credentials, role, authority). WP251 at page 15 warns that profiling may infer sensitive characteristics including "political convictions, religious beliefs." Weighting environmental concerns based on submitter type likely evaluates "personal preferences" and "interests" per Article 4(4).

**Scenario 2: Historical patterns**. If the AI considers whether this submitter previously filed relevant comments, or whether similar submitters' concerns proved valid, this evaluates "behaviour" and "reliability"—explicitly listed in Article 4(4).

**Scenario 3: Pure content salience**. If the AI evaluates only whether the content addresses relevant legal criteria (environmental impact, technical feasibility, public interest) without reference to submitter characteristics, the strongest argument exists that this does NOT evaluate "personal aspects relating to a natural person."

### 3.4 Academic Debates on Profiling Boundaries

**Malgieri & Comandé** ("Why a Right to Legibility...Exists," 7 Int'l Data Privacy L. 243, 2017, at 255) emphasize profiling involves "gathering information about an individual...and evaluating their characteristics or behaviour patterns in order to place them into a certain category or group."

**Wachter, Mittelstadt & Floridi** ("Why a Right to Explanation...Does Not Exist," 7 Int'l Data Privacy L. 76, 2017) focus on profiling as generating **predictions or inferences** about individuals beyond data explicitly provided.

**Synthesis**: The academic consensus suggests profiling requires **evaluation of the person** rather than mere **classification of their data**. Content analysis that infers submitter characteristics (expertise, reliability, bias) constitutes profiling; pure content relevance assessment without such inferences does not.

**Application to hypothetical**: Whether Article 4(4) profiling occurred depends on system design. If the AI evaluates submission content against legal criteria without assessing submitter characteristics, likely not profiling. If it weights inputs based on submitter credibility, type, or inferred expertise, profiling occurs.

---

## 4. The Relevance/Weight Problem: Non-Decisive Inputs and Materiality

### 4.1 The Hypothetical's Specification: Inputs "Could Be Meaningless"

The hypothetical states consultation inputs are "principally broadly assessed...without [any input] being a decisive factor" and "any input could be meaningless." This raises whether Article 22 applies when inputs are **explicitly advisory** and **non-determinative**.

Yet the hypothetical also states the omitted input "may have led to a refusal to grant" the concession. This creates tension: inputs are generally non-decisive, but this specific input might have been consequential.

### 4.2 SCHUFA's Reasoning on Probabilistic vs. Deterministic Influence

SCHUFA did not require the automated processing **deterministically** control outcomes. At **paragraph 73**, the Court found Article 22 applies where third parties "draw strongly on" the probability value—which in practice meant insufficient scores led to denial "in almost all cases" but not absolutely all.

The **"determining role" standard** (paragraph 50) suggests **high correlation** suffices; **absolute determination** is not required. The approximately 80% correlation in SCHUFA satisfied this threshold.

**Application**: If consultation inputs are "generally meaningless," they likely don't play a "determining role" in most cases. But if evidence showed that consultation opposition led to concession refusal in 70-80% of cases, SCHUFA's logic would suggest the inputs do play a determining role, even if not absolutely decisive.

### 4.3 Counterfactual Analysis: "May Have Led To" Different Outcome

The hypothetical specifies the omitted input "may have led to refusal." This probabilistic formulation—**may have** rather than **would have**—raises the materiality threshold question.

**Wachter, Mittelstadt & Russell** ("Counterfactual Explanations Without Opening the Black Box," 31 Harvard J.L. & Tech. 841, 2018) propose counterfactual explanations focusing on what would need to change to alter outcomes. They distinguish **probabilistic** (changes that increase likelihood of different outcome) from **deterministic** (changes that certainly alter outcome) thresholds.

No CJEU guidance establishes which standard applies. **Two interpretive approaches**:

**Narrow approach**: Article 22 requires showing the automated processing **did** produce legal/significant effects, not that it **might have** under different circumstances. "May have led to refusal" is too speculative—the input was omitted, the concession was granted, no actual effect materialized.

**Broad approach**: The **potential** for significant effects suffices when assessing whether processing falls within Article 22 scope. If an omitted input had substantial probability of changing outcomes, the algorithmic omission "produced" significant effects by denying that probability.

WP251 at page 21 states effects must "**significantly affect** the circumstances, behavior, or choices of individuals" (emphasis added). The use of "affect" rather than "would affect" or "might affect" suggests **actual** effects are required, supporting the narrow approach.

### 4.4 The Tension: Advisory Systems vs. Effective Influence

**Real-world consultation processes** typically involve advisory input that authorities "take into account" without being bound by. This is intentional—administrative discretion requires freedom to weigh multiple factors.

If Article 22 applies to filtering of such advisory inputs, it would subject **vast categories of government information processing** to its requirements. Every algorithmic triage of citizen communications—emails, petitions, consultations, complaints—could trigger Article 22 if those communications might influence outcomes.

**Counter-argument**: The **public participation context** distinguishes advisory consultation from mere correspondence. The **Aarhus Convention** (discussed in Section 7) requires authorities to "take due account" of public participation outcomes in environmental decisions. If participation rights have legal force, filtering that denies effective participation may produce "legal effects" within Article 22's meaning.

---

## 5. Directness and Causation: When Ultimate Effect Is on Third Party's Application

### 5.1 The Three-Party Structure

The hypothetical presents:
- **Party A**: Individual Y submitting consultation response
- **Party B**: Company X applying for power plant concession  
- **Decision-maker**: Awarding authority using AI to filter consultation inputs
- **Automated processing**: Omits Y's input from summary provided to authority
- **Final decision**: Grant or deny X's concession application

The formal Article 22 "decision" would be about X's application. But Y claims protection based on algorithmic filtering of Y's input affecting that decision.

### 5.2 Does Y Have "Legal Effects or Similarly Significant Effects"?

**WP251 at pages 21-23** defines these terms:

**Legal effects**: Affect legal rights such as "freedom to associate with others, vote, take legal action" or "legal status or rights under a contract." Examples include contract cancellation, denial of statutory benefits, refused admission to a country.

**Similarly significant effects**: Must be "sufficiently great or important to be worthy of attention." Test includes whether effects:
- Significantly affect circumstances, behavior, or choices
- Have prolonged or permanent impact
- At most extreme, lead to exclusion or discrimination

**Application to Y**: Y has no direct legal rights regarding X's concession application. Y is not party to any contract with the authority. Y has no statutory entitlement to have concession denied.

**Argument for significance**: Y has **participation rights** under administrative law and potentially Aarhus Convention. If these rights are **legally enforceable** (not merely political), then denial of effective participation through algorithmic filtering affects Y's legal rights—specifically, the right to meaningful participation in environmental decision-making.

**ECtHR case law** (discussed in Section 7) establishes **procedural rights** that may be legally enforceable. The **Yüksel Yalçınkaya** case (ECtHR Grand Chamber, 26 September 2023) found violations of Article 6 ECHR where algorithmic evidence affected outcomes without adequate opportunity to challenge methodology. By analogy, algorithmic filtering of consultation inputs without opportunity for challenge could violate procedural rights.

**Argument against significance**: Y's interest is in **influencing a decision about someone else** (X's application). This is too attenuated to constitute "legal or similarly significant effects" on Y. Y's position is that of an **interested third party**, not a rights-holder in the decision.

### 5.3 Standing and Causation Requirements

**No CJEU case law directly addresses** third-party standing to invoke Article 22. SCHUFA involved the data subject whose creditworthiness was assessed. No precedent extends Article 22 to parties affected by decisions about others.

**Administrative law standing** (Article 263 TFEU) requires being "directly and individually concerned." Applying this standard, Y would need to show:
- **Direct concern**: The omission directly affected Y (met—Y's input was omitted)
- **Individual concern**: Y is affected in a way distinguishing Y from all other citizens (harder—many citizens can file consultation responses)

The **directness** of Y's concern is questionable. Y is affected only **if**: (1) Y's submission would have been persuasive, (2) the authority would have been influenced, (3) this influence would have changed the decision, (4) the changed decision would have affected Y's interests.

Each contingency attenuates causation. **SCHUFA's causation** was direct: low score → denial of credit to that person. Here: filtered input → summary excludes it → decision-maker unaware → decision possibly different → citizen's environmental interests possibly affected.

### 5.4 Analogues in Case Law: Access to Process vs. Control of Outcome

**Dutch SyRI case** (District Court of The Hague, 5 February 2020) found Article 8 ECHR violations where algorithmic welfare fraud detection system lacked transparency. Importantly, **the decision was not "about" the data subjects** in the sense of determining their benefits—it flagged them for investigation. The effect was **denial of equal treatment** and **exposure to suspicion**.

By analogy, Y's harm is not control over the decision outcome (whether X receives concession) but rather **denial of procedural equality**—Y's input was algorithmically excluded while others' inputs were considered.

**Austrian jobseekers case** involved algorithmic categorization of jobseekers determining which services they received. The categorization didn't directly grant/deny employment, but **structured access** to opportunities. Courts found this sufficiently significant.

These cases suggest **procedural harms** and **gatekeeping effects** may constitute significant effects even when the formal decision is about a third party.

---

## 6. Most Similar Scenarios in Literature and Case Law

### 6.1 Algorithmic Content Moderation

**ICO Guidance** (March 2024) addresses whether content moderation constitutes Article 22 decisions. Key findings:

- **Article 22 applies** when sophisticated AI makes predictions based on context that can block content or ban users **without human review**
- **Article 22 does NOT apply** when content is matched to prohibited material databases with parameters set by humans
- The distinction turns on whether **the AI exercises judgment** or merely **applies human-set rules**

**Relevance**: Content moderation filtering determines what speech reaches audiences; consultation filtering determines what input reaches decision-makers. Both involve algorithmic gatekeeping affecting access and influence.

**Digital Services Act** (Articles 27, 50) imposes transparency requirements on recommender systems and content moderation, operating **alongside** GDPR Article 22. This suggests recognition that **not all algorithmic filtering** triggers Article 22, but **supplementary protections** are needed.

### 6.2 Government AI Processing Citizen Inputs

**Limited direct precedent** exists. The **Future of Privacy Forum Report** (May 2022) analyzing 70+ cases found:

- **Dutch SyRI welfare fraud detection**: Article 8 ECHR violation for opacity, but system flagged people for investigation rather than making final decisions
- **Italian DPA - Deliveroo rider management**: Fined for not verifying accuracy of automated work allocation decisions  
- **Portuguese DPA - University proctoring**: Found unlawful where humans lacked meaningful oversight despite having final decision authority

**Common theme**: Systems where humans **nominally** make final decisions but lack effective capacity to diverge from algorithmic outputs may still be "solely automated."

**Application**: If authority decision-makers receive only AI summaries without awareness of filtered inputs or ability to access omitted submissions, the filtering may be "solely automated" despite human final decision.

### 6.3 Automated Triaging of Applications/Submissions

**Veale & Binns** (at 323-324) identify **"triaging systems"** where "automated categorization determines the future decision pathway that the case continues along." Examples:
- Visa applications routed to different review tracks
- Asylum screening determining expedited vs. full review
- Benefit fraud cases flagged for investigation

**Critical insight**: Triaging doesn't formally decide applications, but **structurally constrains** downstream options. If high-priority cases receive thorough review while low-priority cases receive cursory review, the triaging algorithm effectively determines outcomes through **choice architecture**.

**Application**: Consultation filtering operates as triaging—determining which inputs receive full consideration vs. omission. If this categorization "plays a determining role" (SCHUFA paragraph 50) in what information decision-makers consider, it may constitute an Article 22 decision.

### 6.4 Information Retrieval and Ranking Systems

**No CJEU case law** addresses whether search ranking or information retrieval systems constitute Article 22 decisions. The **Digital Services Act Article 27** requires transparency about "main parameters" of recommender systems, suggesting these are **distinct from** Article 22 ADM.

**Scholarly debate**: If search engines rank results based on predicted relevance to users, does this "evaluate personal aspects" (user preferences, interests) constituting profiling? Or does it evaluate content relevance independent of user characteristics?

**Consensus appears to be**: General ranking for all users based on content attributes likely does not profile individual users. Personalized ranking based on individual user history does profile.

**Application**: If consultation filtering uses identical criteria for all submissions (relevance to legal criteria), less likely to be profiling. If it weights submissions based on submitter characteristics or past behavior patterns, more likely profiling.

---

## 7. ECtHR Case Law Informing Article 22 Interpretation

### 7.1 Article 8 ECHR and Algorithmic Decision-Making: The SyRI Precedent

**NJCM et al. v. The Netherlands (SyRI Case)**, District Court of The Hague, 5 February 2020, applied Article 8 ECHR to algorithmic welfare fraud detection.

**Key holdings**:
- Processing personal data for risk scoring engaged Article 8 rights
- Article 8(2) requirements—legality, necessity, proportionality—apply to algorithms
- **Opacity shifts burden**: Government's refusal to disclose algorithm methodology transferred burden to government to prove compliance
- Risk of discriminatory effects required safeguards (none present)
- Interference "extensive and serious" despite no direct legal consequences

**Relevance to Article 22**: Court interpreted Article 8 **"in light of GDPR principles"** including transparency, purpose limitation, data minimization. This demonstrates **complementary application** of ECHR and GDPR standards.

**Application**: Even if consultation filtering falls outside Article 22's technical scope, Article 8 ECHR requires proportionality and transparency. Algorithmic omission of citizen input without disclosure violates Article 8(2).

### 7.2 Article 6 ECHR and Automated Evidence: Yüksel Yalçınkaya

**Yüksel Yalçınkaya v. Türkiye**, ECtHR Grand Chamber, 26 September 2023, addressed algorithmic evidence in criminal proceedings.

**Article 6 violations** (16-1 vote):
- Inadequate access to algorithmic evidence concerning applicant  
- Unable to challenge methodology identifying him as app user
- Courts failed to provide safeguards for effective challenge
- Shortcomings "incompatible with **very essence**" of procedural rights
- Uniform approach to digital evidence violated individual assessment requirement

**Key principle**: Algorithmic evidence cannot be dispositive without: (1) disclosure of methodology, (2) opportunity to challenge, (3) individual assessment beyond system output, (4) reasoned judicial decisions.

**Relevance**: If environmental decisions engage "civil rights" under Article 6, procedural requirements apply. Citizens must be able to: understand what evidence decision-makers considered, challenge algorithmic filtering methodology, receive reasoned decisions explaining how participation was considered.

### 7.3 Procedural Rights: Right to Be Heard (Audi Alteram Partem)

**General EU administrative law principle**: Person whose interests affected by public authority decision must have opportunity to state views. This predates GDPR and applies independently.

**National court applications to algorithms**:
- **Slovak Constitutional Court (eKasa, §133)**: Individual must have "knowledge about existence, scope and impact of automated assessment" to "effectively defend against possible errors"
- **Italian Higher Administrative Court (Altomare/C.P.)**: Required "full upstream knowability" of algorithm and criteria
- **Dutch Council of State (SyRI)**: System must be "transparent and verifiable"

**Application**: These principles apply **even without Article 22**. If citizens lack awareness their submissions were algorithmically filtered, they cannot effectively exercise right to be heard.

### 7.4 Aarhus Convention: Environmental Participation Rights

**UNECE Aarhus Convention** (1998), ratified by EU and all Member States, establishes three pillars:
1. Access to environmental information
2. **Public participation in environmental decision-making**
3. Access to justice in environmental matters

**Article 6 requirements** for decisions on specific activities (including power plants):
- Public must be informed **"early in decision-making when all options are open"**
- Must have **"genuine opportunity to participate effectively"**  
- Authorities must **"take due account of the outcome"**
- Public must be informed of decisions and **"how participation was taken into consideration"**

**Critical for hypothetical**: Algorithmic filtering of consultation inputs potentially violates multiple Aarhus requirements:
- If filtering not disclosed, public lacks information about process
- If filtering removes substantive input, participation not "effective"
- If authority unaware of filtered submissions, cannot "take due account"
- If decisions don't explain filtering's role, explanation requirement violated

**Regulatory hierarchy**: Aarhus obligations are **legally binding** treaty requirements, independently enforceable. Even if Article 22 doesn't apply, Aarhus provides **alternative protection** for environmental consultations.

---

## 8. Doctrinal Synthesis: Article 22's Boundaries and Gap Analysis

### 8.1 What This Reveals About Article 22's Boundaries

**If consultation filtering is NOT an Article 22 decision**, this reveals:

**First, Article 22 may require the data subject be the formal decision object**, not merely affected by decisions about third parties. The "subject to a decision" language emphasizes direct rather than indirect effects.

**Second, Article 22 may exclude preparatory information processing** that influences but doesn't determine outcomes. The "based solely" requirement may draw a boundary at information provision vs. decision-making.

**Third, Article 22 may apply only to decisions about individuals' rights/status**, not their participation in processes about others' rights. Gatekeeping functions that structure access may fall outside scope.

**Fourth, advisory inputs with uncertain influence** may not "produce" effects sufficiently to trigger Article 22. The SCHUFA "determining role" test requires high correlation between processing and outcomes.

**If consultation filtering IS an Article 22 decision**, this reveals:

**First, Article 22 extends to algorithmic gatekeeping** that structures what information reaches decision-makers, not just direct decisions about individuals.

**Second, multi-stage processing where upstream automation constrains downstream choices** remains within scope despite human involvement.

**Third, procedural rights violations** (denial of meaningful participation) may constitute "similarly significant effects" even when substantive outcome rights belong to third parties.

**Fourth, SCHUFA's anti-circumvention logic** prevents controllers from evading Article 22 by characterizing determinative processing as "mere information provision."

### 8.2 What Government AI Uses Fall Within vs. Outside Article 22?

**Likely within Article 22 scope**:
- Automated benefit eligibility determination producing legal entitlement/denial
- Algorithmic risk scoring that determines investigation/enforcement actions
- Automated triaging that categorically determines service levels (if correlation with outcomes is high)
- Content moderation causing account suspension/bans with significant economic effects

**Uncertain boundary cases** (consultation filtering exemplifies):
- Information filtering influencing but not determining decisions
- Advisory recommendations human decision-makers "draw strongly on"
- Procedural gatekeeping affecting access to decision-makers
- Multi-stage systems with meaningful but constrained human oversight

**Likely outside Article 22 scope**:
- General information categorization not linked to decisions about individuals
- Statistical analysis producing aggregate insights
- Recommendation systems where humans make independent judgments
- Technical processing (spam filtering, format conversion) not affecting substantive rights

The **determinative factor** appears to be whether the automated processing **functionally determines outcomes** affecting the data subject's legal rights or similarly significant interests, regardless of formal decision structure.

### 8.3 Gaps in Protection That Other Frameworks Must Fill

**Multiple gaps** emerge where Article 22 doesn't clearly apply:

**Gap 1: Meaningful human involvement** - When humans nominally make decisions but lack effective capacity to diverge from algorithmic recommendations, Article 22 may not apply (due to "solely" requirement) yet automated subordination occurs.

**Fill**: **Article 41 EU Charter** (right to good administration), national administrative procedure law, and **Article 6 ECHR** (fair hearing) require meaningful human decision-making with adequate information and reasoning.

**Gap 2: Advisory systems** - When algorithmic processing influences but doesn't determine outcomes, effects may be too uncertain/attenuated for Article 22.

**Fill**: **GDPR general principles** (Articles 5, 13-15) require transparency and fairness even without Article 22. **Article 8 ECHR** requires proportionality for any data processing. **Aarhus Convention** specifically addresses consultation processes.

**Gap 3: Indirect/third-party effects** - When individuals are affected by decisions formally about others, they may lack standing under Article 22's "subject to" language.

**Fill**: **Administrative law standing** and **Aarhus access to justice** provide routes to challenge decisions affecting environmental interests. **ECtHR procedural rights** apply where "civil rights" are engaged.

**Gap 4: Collective harms** - Article 22 protects individuals; systemic discrimination affecting groups may not be adequately addressed.

**Fill**: **Article 21 GDPR** (right to object to profiling), **non-discrimination law**, and **data protection impact assessments** (Article 35) address systemic risks. **EU AI Act** (forthcoming) will regulate high-risk systems creating collective harms.

### 8.4 How Administrative Law, Aarhus, and AI Act Interact with GDPR

**Cumulative application** characterizes the regulatory landscape:

**Layer 1 - Constitutional/Human Rights**: ECHR Articles 6 & 8, EU Charter Articles 7-8 & 41 provide baseline rights applying to all government processing. These are **interpretive frameworks** for more specific laws.

**Layer 2 - Data Protection**: GDPR Articles 5 (principles), 13-15 (information rights), 22 (ADM prohibition) apply to personal data processing. GDPR is **lex specialis** within broader human rights framework.

**Layer 3 - Sectoral Regulation**: Aarhus Convention applies specifically to environmental decisions, requiring participation rights **exceeding** general data protection. Digital Services Act applies to platforms. These are **additional** to GDPR.

**Layer 4 - Future AI Regulation**: EU AI Act will classify government use of AI in areas affecting fundamental rights as "high-risk," requiring conformity assessments, transparency, human oversight, and accuracy standards. This operates **alongside** GDPR.

**Interaction principle**: The **most protective standard** applies where frameworks overlap. **Cumulative compliance** is required—satisfying one framework doesn't exempt from others.

**Application to hypothetical**: The awarding authority must comply with:
- **GDPR**: Transparency, fairness, accuracy (general principles) plus Article 22 if applicable
- **Aarhus**: Public participation rights including information about consultation processing
- **ECHR/Charter**: Proportionality, procedural fairness, non-discrimination
- **National administrative law**: Right to be heard, duty to give reasons
- **AI Act** (when applicable): High-risk system requirements if AI affects fundamental rights

These obligations are **cumulative**. Even if Article 22 doesn't apply, other frameworks comprehensively protect against algorithmic consultation filtering without transparency and accountability.

---

## 9. Methodological Conclusions and Unresolved Questions

### 9.1 What SCHUFA Establishes (Ratio Decidendi)

**Binding precedent** from SCHUFA Holding (C-634/21):

**First, broad purposive interpretation**: Article 22 encompasses "a number of acts which may affect the data subject in many ways" (para. 46). Narrow interpretation creating "lacuna in protection" is rejected (para. 61-63).

**Second, preparatory acts can be decisions**: Generating probability values that "play a determining role" in subsequent decisions constitutes Article 22 decision-making (para. 50), even when separate entities make final decisions (para. 73).

**Third, "draws strongly on" test**: When third parties rely on automated processing such that it correlates highly with outcomes (approximately 80% in SCHUFA), Article 22 applies to the generation of that information.

**Fourth, prohibition in principle**: Article 22(1) is a prohibition whose "infringement does not need to be invoked individually" (para. 52), distinguishing it from rights requiring individual assertion.

### 9.2 What Remains Unresolved After SCHUFA

**First, precise "determining role" threshold**: Is 80% correlation required? 70%? 90%? Does correlation suffice or must causation be more direct?

**Second, "solely" with rubber-stamping**: When humans nominally make decisions but lack effective independence from algorithmic recommendations, is processing still "solely" automated? SCHUFA didn't address this.

**Third, indirect effects**: Can individuals invoke Article 22 for decisions formally about third parties but affecting them? SCHUFA involved direct decisions about the applicant.

**Fourth, information gatekeeping**: Does algorithmic filtering of information that reaches decision-makers constitute a "decision," or is it preprocessing outside Article 22 scope?

**Fifth, public sector specificities**: SCHUFA involved private credit scoring. Do different standards apply to government use of AI in administrative processes?

**Sixth, intersection with profiling**: Must Article 22 decisions involve Article 4(4) profiling, or can non-profiling automated processing qualify if it produces significant effects?

### 9.3 Advocate General Reasoning and Alternative Interpretations

**AG Pikamäe Opinion** (C-634/21, 16 March 2023, ECLI:EU:C:2023:220) provided reasoning the Court largely adopted but with nuances:

The AG emphasized at paragraph 83 that "the concept of 'decision' within the meaning of that provision must be construed broadly" but also noted at paragraph 89 that "not every automated processing of personal data producing an output which may affect a data subject constitutes a 'decision' within the meaning of Article 22(1)."

The AG's reasoning suggests a **functional test**: processing constitutes a "decision" when it **determines outcomes** rather than merely providing information. The boundary lies in **substitution of judgment**—has the algorithm replaced human evaluation, or merely informed it?

**Alternative interpretations** left open:

**Narrow view**: Article 22 applies only to fully automated final decisions with minimal human involvement, directly determining legal/significant effects on the data subject who is the formal decision object.

**Broad view**: Article 22 applies to any automated processing that substantially constrains human decision-makers' choices, even in multi-stage systems where effects are indirect or mediated through decisions about third parties.

The Court in SCHUFA moved toward the broader view but did not fully resolve these tensions.

### 9.4 Academic Consensus vs. Unresolved Scholarly Debates

**Areas of scholarly consensus**:

**First, inadequacy of current framework**: Nearly all scholars (Veale & Binns, Kaminski, Edwards & Veale, Wachter et al.) agree Article 22 in its current form inadequately addresses modern multi-stage algorithmic systems.

**Second, meaningful human oversight requirement**: Consensus exists that nominal human involvement shouldn't defeat Article 22 if humans lack genuine capacity for independent judgment (Kaminski, FPF Report, national court decisions).

**Third, need for systemic governance**: Individual rights alone insufficient; require impact assessments, auditing, and systemic oversight (Kaminski, Edwards & Veale, Selbst & Powles).

**Areas of fundamental disagreement**:

**First, existence of explanation right**: Wachter et al. deny general right to explanation exists; Malgieri & Comandé and Selbst & Powles argue it does through combined reading of provisions. **Unresolved**.

**Second, scope of profiling**: Whether evaluation of content becomes evaluation of "personal aspects" remains contested. Hildebrandt argues broader interpretation; others limit to explicit personal characteristics.

**Third, indirect effects**: Veale & Binns identify but don't resolve whether Article 22 should extend to indirect effects through multi-stage processing. No scholarly consensus.

**Fourth, normative goals**: Disagreement whether Article 22 primarily protects **dignity/autonomy** (supporting broad interpretation) or **prevents specific discriminatory harms** (supporting narrow interpretation focused on high-impact decisions).

### 9.5 How Courts Might Resolve Tensions in Future Cases

**Likely approaches**:

**First, functional analysis**: Courts will likely adopt **functional tests** examining whether automated processing **effectively determines outcomes** regardless of formal decision structure. SCHUFA's "plays a determining role" language supports this.

**Second, contextual assessment**: Rather than categorical rules, courts will likely assess Article 22 applicability **context-specifically**, considering: nature of rights affected, degree of automation, meaningfulness of human oversight, and availability of alternative protections.

**Third, harmonized interpretation**: Courts will likely interpret Article 22 **in light of** Charter Articles 7-8, 41, and ECHR Articles 6, 8, ensuring consistent protection of fundamental rights across frameworks.

**Fourth, gap-filling through principles**: Where Article 22's technical requirements aren't met, courts will likely apply **GDPR general principles** (fairness, transparency, accountability) to prevent algorithmic harms, as Dutch courts did in SyRI.

**Fifth, sectoral differentiation**: Courts may develop **different standards** for public sector algorithmic decision-making versus private sector, given distinct constitutional constraints on government action and procedural rights in administrative law.

---

## Final Assessment: Application to the Hypothetical

### The algorithmic consultation filtering presents a **boundary case** that reveals Article 22's contested scope:

**Arguments Article 22 APPLIES**:

**First, SCHUFA's broad interpretation**: The "determining role" logic extends to information filtering that constrains what decision-makers consider. If filtered inputs would have influenced outcomes, omission plays a determining role.

**Second, anti-circumvention principle**: Allowing controllers to evade Article 22 by filtering information rather than making formal decisions would create exactly the "lacuna in protection" CJEU rejected at paragraphs 61-63.

**Third, WP251 third-party effects**: The Guidelines recognize significant effects can arise from decisions affecting individuals based on others' characteristics. Algorithmic filtering denies participation opportunities based on automated assessment.

**Fourth, profiling if submitter evaluation**: If the AI weighs submissions based on submitter characteristics (credentials, past behavior, submitter type), Article 4(4) profiling occurs, strengthening Article 22 applicability.

**Fifth, Aarhus legal effects**: In environmental contexts, participation rights have legal force. Denying effective participation may constitute "legal effects" triggering Article 22.

**Arguments Article 22 DOES NOT APPLY**:

**First, no decision "about" the data subject**: The formal decision concerns the company's concession application, not the citizen's rights. Article 22's "subject to" language requires the data subject be the decision object.

**Second, indirect/attenuated effects**: The causal chain—filtering → summary → concession decision → environmental effects on citizen—is too attenuated. Effects are contingent on multiple intervening decisions.

**Third, advisory nature**: Consultation inputs are explicitly non-decisive. SCHUFA's "determining role" test requires high correlation; advisory inputs with uncertain influence don't meet this threshold.

**Fourth, not "solely" automated**: Humans make the final concession decision with discretion to weigh multiple factors. The filtering is preprocessing, not the decision itself.

**Fifth, no profiling if pure content analysis**: If the AI evaluates submission relevance to legal criteria without assessing submitter characteristics, no "evaluation of personal aspects" occurs, thus no Article 4(4) profiling.

### Methodological conclusion on likelihood of Article 22 application:

**Article 22 application is POSSIBLE but UNCERTAIN** based on current jurisprudence. The outcome depends heavily on factual specifics:

**Higher likelihood if**:
- Evidence shows consultation opposition correlates highly with concession refusal (SCHUFA "determining role")
- The AI evaluates submitter characteristics not just content (Article 4(4) profiling)
- Decision-makers lack access to filtered submissions (more "solely" automated)
- Aarhus Convention applies, giving participation legal status ("legal effects")
- The omitted input demonstrably would have changed the decision (direct causation)

**Lower likelihood if**:
- Consultation inputs have low correlation with outcomes (not "determining")
- The AI performs pure content relevance analysis (not profiling)
- Decision-makers retain meaningful discretion and access to original submissions
- Effects on citizen are speculative/contingent (insufficient causation)
- The citizen is third party to decision about company's application (insufficient directness)

**Most probable outcome**: **Article 22 does not apply** to this specific scenario under current narrow interpretation, but **alternative protections** comprehensively address the harms through **Aarhus Convention** (environmental participation rights), **Article 8 ECHR** (proportionality of processing), **Article 41 EU Charter** (right to good administration), **GDPR general principles** (transparency, fairness), and **national administrative law** (right to be heard, duty to give reasons).

### The gap Article 22 leaves is filled by complementary frameworks creating **cumulative protection exceeding** what Article 22 alone provides:

**Protection 1 - Aarhus**: Right to know consultation processing methods, effective participation, decisions explaining how input was considered

**Protection 2 - Article 8 ECHR**: Proportionality requirement for algorithmic processing, burden-shifting where opacity exists

**Protection 3 - Article 41 EU Charter**: Right to be heard, access to file, reasoned decisions when implementing EU law

**Protection 4 - GDPR Articles 5, 13-15**: Transparency about automated processing logic, fairness, right to access information

**Protection 5 - National administrative law**: Right to be heard, non-discrimination, procedural fairness

**This reveals Article 22's role** in the broader data protection ecosystem: not a comprehensive prohibition on algorithmic government, but a **specific protection against fully automated decisions with significant effects**, operating within a **multi-layered framework** where constitutional principles, administrative law, sector-specific regulations, and general data protection obligations create comprehensive accountability for algorithmic governance.

**The hypothetical illuminates** that Article 22's boundaries remain contested, particularly regarding multi-stage processing, indirect effects, and information gatekeeping functions. Future CJEU jurisprudence must clarify whether SCHUFA's logic extends to these contexts or whether Article 22's technical scope remains narrower, relying on alternative frameworks to fill protection gaps.