# Phase 2: Source & Argument Extraction by RQ

**Project:** Automated Decision-Making in Administrative Public Participation
**Extraction Date:** 2025-11-22
**RQs Completed:** RQ1
**Total RQs:** 5

---

## RQ1: Automated Decision Threshold

**Full Statement:** Does algorithmic filtering of consultation submissions constitute a "decision based solely on automated processing" under GDPR Article 22 when human officials make the final administrative decision, but only review algorithmically-selected inputs? How should "solely automated" be interpreted in multi-stage administrative processes where AI determines which information reaches human decision-makers?

### Documents Analyzed for RQ1
**Primary documents:** [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]], [[Article 22 GDPR Automated Decision-Making]], [[Algorithmic Gatekeeping in Administrative Consultations]], [[Unresolved issues to research]]
**Supporting documents:** [[Hypotheticals case matrix]], [[Algorithmic Gatekeeping in the Public Sphere (Draft)]]

---

### Sub-Topics & Arguments

**Sub-Topic 1: Definition of "Solely Automated" Processing**
- **Main argument:** "Solely automated" means the decision is made entirely by machine with no substantive human review capable of altering the outcome. The key distinction is between form (human review exists) and substance (human review is effective). Post-SCHUFA, the fact that human review exists does not automatically remove Article 22 applicability—the focus shifts to whether human review is genuinely meaningful.
- **Found in:** [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]], [[Algorithmic Gatekeeping in Administrative Consultations]]
- **Evidence used:** WP251rev.01 p. 10-11 definition, SCHUFA C-634/21 ¶¶56-65, four-element meaningful intervention test
- **Relationship to other sub-topics:** Foundation for Sub-Topic 2 (Meaningful Human Intervention Test) and Sub-Topic 3 (Rubber-Stamping Phenomenon)

**Sub-Topic 2: Meaningful Human Intervention Test (Four Cumulative Elements)**
- **Main argument:** Human involvement satisfies the "not solely automated" requirement only when four cumulative elements are present: (1) authority and empowerment to alter outcome, (2) information access to same or better data than algorithm, (3) competence and training to evaluate decision, and (4) genuine exercise of review (not formality). Failure of any element means processing remains "solely automated" despite nominal human involvement.
- **Found in:** [[Evaluation-Synthesis]], [[ADM-Taxonomy-Elements]], [[Article 22 GDPR Automated Decision-Making]]
- **Evidence used:** WP251rev.01 p. 10 definition, Spanish AEPD four-factor framework, Portuguese DPA university proctoring case (FPF Report Case 26), Austrian jobseekers case (FPF Report Case 9)
- **Relationship to other sub-topics:** Operationalizes Sub-Topic 1; provides practical criteria for Sub-Topic 3 and Sub-Topic 4

**Sub-Topic 3: The "Rubber-Stamping" Phenomenon and Automation Bias**
- **Main argument:** When humans nominally review AI outputs but approve 99%+ of recommendations without genuine assessment, the process is de facto solely automated. Research on automation bias confirms humans are cognitively predisposed to trust automated outputs, especially under time pressure or with massive datasets. The EDPB has clarified that controllers cannot fabricate human involvement to avoid Article 22 provisions.
- **Found in:** [[Article 22 GDPR Automated Decision-Making]], [[Algorithmic Gatekeeping in Administrative Consultations]], [[Algorithmic Gatekeeping in the Public Sphere (Draft)]]
- **Evidence used:** WP251rev.01 p. 10 (meaningful intervention definition), research on automation bias, red flag indicators (<1% rejection rate), FPF Report analysis of 70+ cases
- **Relationship to other sub-topics:** Practical application of Sub-Topic 2; core problem in Sub-Topic 5 (high-volume filtering)

**Sub-Topic 4: Preparatory Acts as "Decisions" (SCHUFA Doctrine)**
- **Main argument:** The CJEU established in SCHUFA that preparatory acts can constitute "decisions" within Article 22(1) if they play a "determining role" in downstream outcomes. When third parties "draw strongly" on automated assessments to make their own decisions, the generation of that assessment constitutes an Article 22 decision—even if a separate entity makes the final formal decision. This prevents circumvention by inserting a human "straw man."
- **Found in:** [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]], [[Algorithmic Gatekeeping in Administrative Consultations]], [[Algorithmic Gatekeeping in the Public Sphere (Draft)]]
- **Evidence used:** SCHUFA C-634/21 ¶¶46, 50, 56-65, 73 (approximately 80% correlation between score and denial), AG Pikamäe Opinion ¶¶83, 89
- **Relationship to other sub-topics:** Extends Sub-Topic 1 to multi-stage processing; foundation for Sub-Topic 6 (upstream filtering)

**Sub-Topic 5: The "Upstream Foreclosure" Problem in Multi-Stage Processing**
- **Main argument:** Veale & Binns identify "upstream foreclosure" where automated steps foreclose downstream outcomes despite nominal human involvement. Article 22's focus on "final decisions" ignores how prior automated processing constrains choice architecture. If algorithm produces predetermined outcome that human review rubber-stamps, Article 22 applies to the algorithm itself.
- **Found in:** [[Algorithmic Gatekeeping in Administrative Consultations]], [[Article 22 GDPR Automated Decision-Making]]
- **Evidence used:** Veale & Binns (2021) at 319, 327-328 identifying five complications in multi-stage profiling; Kaminski (2019) at 197-198 on meaningful oversight
- **Relationship to other sub-topics:** Academic framework supporting Sub-Topic 3 and Sub-Topic 4; directly relevant to Sub-Topic 6

**Sub-Topic 6: Information Gatekeeping as Decision-Making**
- **Main argument:** If AI filtering controls what information reaches human decision-makers (who never see filtered submissions), the filtering constitutes a "solely automated" decision on admissibility despite humans making the final substantive decision. The "decision" to exclude specific citizen input is made solely by software, often without knowledge of the human nominally responsible. Under SCHUFA logic, if generating information that determines outcomes constitutes a "decision," then omitting information that would determine outcomes should equally qualify.
- **Found in:** [[Algorithmic Gatekeeping in Administrative Consultations]], [[Unresolved issues to research]], [[Algorithmic Gatekeeping in the Public Sphere (Draft)]]
- **Evidence used:** SCHUFA anti-circumvention reasoning ¶¶61-63, ICO guidance on content moderation (March 2024), the "upstream trap" where humans never see filtered data
- **Relationship to other sub-topics:** Core application of Sub-Topics 3-5 to consultation filtering scenario; central to RQ1 resolution

**Sub-Topic 7: Doctrinal Tension Between WP251 and SCHUFA**
- **Main argument:** WP251 Guidelines (p. 20-21) distinguish between decisions and recommendations, suggesting that human review taking account of other factors means the decision is not "based solely" on automated processing. SCHUFA's "determining role" test appears to conflict with this—the resolution lies in whether the filtering so constrains options that the human decision-maker effectively rubber-stamps the algorithmic output.
- **Found in:** [[Algorithmic Gatekeeping in Administrative Consultations]], [[Article 22 GDPR Automated Decision-Making]]
- **Evidence used:** WP251rev.01 p. 20-21, SCHUFA C-634/21 ¶50 ("determining role"), ¶73 (80% correlation threshold)
- **Relationship to other sub-topics:** Explains doctrinal uncertainty in Sub-Topics 1-6; key to understanding why RQ1 remains contested

**Sub-Topic 8: Unresolved Threshold for "Determining Role"**
- **Main argument:** No clear CJEU guidance exists on the precise threshold for when preparatory processing "plays a determining role." SCHUFA involved approximately 80% correlation between automated score and final outcome, but it remains unclear whether 70% would suffice, or whether the test is qualitative rather than quantitative. The boundary between preprocessing and decision-making turns on two factors: determinative effect and evaluation of personal aspects.
- **Found in:** [[Algorithmic Gatekeeping in Administrative Consultations]], [[Unresolved issues to research]], [[Evaluation-Synthesis]]
- **Evidence used:** SCHUFA C-634/21 ¶73 (80% correlation), ICO content moderation guidance (sophistication distinction), academic consensus (Binns & Veale, Kaminski, Malgieri)
- **Relationship to other sub-topics:** Key unresolved question affecting all prior sub-topics; identifies gap in current jurisprudence

---

### Legal Sources for RQ1

**EU Regulations & Directives**

| Source | Article/Section | Specific Provision | Used For | Found In |
|--------|-----------------|-------------------|----------|----------|
| GDPR (Regulation 2016/679) | Article 22(1) | "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her" | Core prohibition—defining scope of "solely automated" | All RQ1 documents |
| GDPR | Article 22(2)(a)-(c) | Three exceptions: (a) contract necessity, (b) legal authorization, (c) explicit consent | Exceptions analysis for when prohibition doesn't apply | [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]] |
| GDPR | Article 22(3) | Right to obtain human intervention, express point of view, contest decision | Safeguards when exceptions apply | [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]] |
| GDPR | Article 22(4) | "Suitable measures to safeguard data subject's rights and freedoms and legitimate interests" | Mandatory safeguards for exceptions (a) and (c) | [[ADM-Taxonomy-Elements]] |
| GDPR | Article 4(4) | Definition of "profiling" as "automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects" | Distinguishing profiling from other processing | [[ADM-Taxonomy-Elements]], [[Algorithmic Gatekeeping in Administrative Consultations]] |
| GDPR | Article 5(1)(a) | Lawfulness, fairness, transparency principles | Fairness requirement for automated processing | [[ADM-Taxonomy-Elements]] |
| GDPR | Articles 13(2)(f), 14(2)(g) | Information about "existence of automated decision-making" and "meaningful information about the logic involved" | Transparency obligations | [[ADM-Taxonomy-Elements]] |
| GDPR | Article 15(1)(h) | Right of access to "meaningful information about the logic involved" | Data subject access rights | [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]] |

**CJEU Case Law**

| Case | Citation | Paragraph(s) | Principle/Holding | Used For | Found In |
|------|----------|--------------|-------------------|----------|----------|
| SCHUFA Holding AG | C-634/21, ECLI:EU:C:2023:957 (7 Dec 2023) | ¶46 | "Decision" is "capable of including a number of acts which may affect the data subject in many ways" | Broad interpretation of "decision" | [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]], [[Algorithmic Gatekeeping in Administrative Consultations]] |
| SCHUFA Holding AG | C-634/21 | ¶50 | "Determining role" test: where automated probability value "plays a determining role" in subsequent decisions, its establishment constitutes an Article 22 decision | Core test for preparatory acts | [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]], [[Algorithmic Gatekeeping in Administrative Consultations]], [[Article 22 GDPR ADM]] |
| SCHUFA Holding AG | C-634/21 | ¶¶56-65 | Third-party reliance on automated scores triggers Article 22 for score provider | Service provider liability | [[Evaluation-Synthesis]] |
| SCHUFA Holding AG | C-634/21 | ¶¶61-63 | Narrow interpretation would create "lacuna in legal protection"—anti-circumvention principle | Prevents evasion through multi-stage processing | [[ADM-Taxonomy-Elements]], [[Algorithmic Gatekeeping in Administrative Consultations]] |
| SCHUFA Holding AG | C-634/21 | ¶73 | Third parties "draw strongly on" score; insufficient scores led to denial "in almost all cases" (approximately 80%) | Quantitative threshold for "determining role" | [[Evaluation-Synthesis]], [[Algorithmic Gatekeeping in Administrative Consultations]] |
| AG Pikamäe Opinion (SCHUFA) | C-634/21, ECLI:EU:C:2023:220 (16 March 2023) | ¶83 | "Concept of 'decision' within the meaning of that provision must be construed broadly" | Supporting broad interpretation | [[Algorithmic Gatekeeping in Administrative Consultations]] |
| AG Pikamäe Opinion | C-634/21 | ¶89 | "Not every automated processing of personal data producing an output which may affect a data subject constitutes a 'decision'" | Limits to broad interpretation | [[Algorithmic Gatekeeping in Administrative Consultations]] |
| Dun & Bradstreet Austria | C-203/22, ECLI:EU:C:2025:131 (26 Feb 2025) | ¶¶47-52 | "Meaningful information about the logic" requires explanation of "procedure and principles actually applied" | Transparency standard post-SCHUFA | [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]] |
| Dun & Bradstreet Austria | C-203/22 | ¶50 | Information must be individual-specific, not generic algorithm descriptions | Concrete application requirement | [[Evaluation-Synthesis]] |
| Dun & Bradstreet Austria | C-203/22 | ¶¶51-52 | Information must be comprehensible to ordinary person and sufficient for effective challenge | Comprehensibility and utility standards | [[Evaluation-Synthesis]] |
| OT v Vyriausioji | C-184/20 (1 Aug 2022) | General | Background case on automated processing | Context for GDPR ADM jurisprudence | [[ADM-Taxonomy-Elements]] |

**EDPB/WP29 Guidance**

| Source | Type | Page/Section | Key Point | Used For | Found In |
|--------|------|--------------|-----------|----------|----------|
| WP251rev.01 | Guidelines on Automated individual decision-making and Profiling (Adopted 3 Oct 2017; revised 6 Feb 2018) | p. 7 | Three key components of profiling: automated processing, personal data, evaluate personal aspects | Profiling definition | [[ADM-Taxonomy-Elements]] |
| WP251rev.01 | Guidelines | p. 8 | Three-stage profiling model: data collection, automated analysis, applying correlation | Processing stages | [[ADM-Taxonomy-Elements]] |
| WP251rev.01 | Guidelines | p. 9-10 | "Decision" means assessment producing particular outcome with legal/significant effects | Decision definition | [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]] |
| WP251rev.01 | Guidelines | p. 10-11 | **Meaningful human intervention definition:** (1) authority to change decision, (2) competence to assess, (3) goes beyond rubber-stamping, (4) possesses decision-making authority | Core test for "solely automated" | [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]], [[Article 22 GDPR ADM]] |
| WP251rev.01 | Guidelines | p. 11-12 | "Legal effects" and "similarly significant effects" definitions | Effects threshold | [[ADM-Taxonomy-Elements]] |
| WP251rev.01 | Guidelines | p. 12-14 | Three exceptions and consent requirements | Exceptions analysis | [[ADM-Taxonomy-Elements]] |
| WP251rev.01 | Guidelines | p. 14-15 | Article 22(3) rights: human intervention, express views, explanation, challenge | Safeguards | [[ADM-Taxonomy-Elements]] |
| WP251rev.01 | Guidelines | p. 20-21 | Distinction between decisions and recommendations: "If a human being reviews and takes account of other factors in making the final decision, that decision would not be 'based solely' on automated processing" | Tension with SCHUFA doctrine | [[Algorithmic Gatekeeping in Administrative Consultations]] |

**National DPA Enforcement & Guidance**

| Source | Type | Key Point | Used For | Found In |
|--------|------|-----------|----------|----------|
| Portuguese DPA - University Proctoring | Enforcement (FPF Report Case 26) | Found violation where humans could make final decisions but lacked "clear instructions about when to follow AI system's recommendations" | Meaningful intervention requires guidance | [[Algorithmic Gatekeeping in Administrative Consultations]], [[Article 22 GDPR ADM]] |
| Austrian DPA - Jobseekers Case | Enforcement (FPF Report Case 9) | Required "clear instructions and training for human decision-makers" | Training element of meaningful intervention | [[Algorithmic Gatekeeping in Administrative Consultations]] |
| Spanish AEPD | Four-factor framework | Four elements for meaningful human involvement assessment | National operationalization | [[Article 22 GDPR ADM]] |
| ICO (UK) - Content Moderation Guidance | Guidance (March 2024) | Distinguishes: simple matching to human-set lists (likely not Art. 22) vs. "sophisticated systems making predictions based on context" (likely Art. 22) | Sophistication threshold | [[Algorithmic Gatekeeping in Administrative Consultations]] |
| Future of Privacy Forum Report | Analysis of 70+ cases (May 2022) | Systems where humans "nominally" make final decisions but lack effective capacity to diverge may still be "solely automated" | Pattern across jurisdictions | [[Article 22 GDPR ADM]], [[Algorithmic Gatekeeping in Administrative Consultations]] |

---

### Secondary Sources for RQ1

**Academic Scholarship**

| Source | Author(s) | Key Concept | Used For | Found In |
|--------|-----------|-------------|----------|----------|
| "Is That Your Final Decision?" 11 Int'l Data Privacy L. 319 (2021) | Veale & Binns | "Upstream foreclosure" problem: automated steps foreclose downstream outcomes despite nominal human involvement; five complications in multi-stage profiling | Multi-stage processing analysis | [[Algorithmic Gatekeeping in Administrative Consultations]] |
| "The Right to Explanation, Explained" 34 Berkeley Tech. L.J. 189 (2019) | Kaminski | WP251 clarifies human involvement must be "meaningful"—"authority and competence to change the decision" with "thorough assessment" | Meaningful oversight standard | [[Algorithmic Gatekeeping in Administrative Consultations]], [[Article 22 GDPR ADM]] |
| "Automated Decision-Making in the EU Member States" 35 Computer L. & Security Rev. (2019) | Malgieri | Two-step approach: distinguish profiling (generating information) from decision-making (using information) | Profiling vs. decision distinction | [[Algorithmic Gatekeeping in Administrative Consultations]] |
| "Why a Right to Legibility...Exists" 7 Int'l Data Privacy L. 243 (2017) | Malgieri & Comandé | Profiling involves "gathering information about an individual...and evaluating their characteristics or behaviour patterns in order to place them into a certain category" | Profiling definition | [[Algorithmic Gatekeeping in Administrative Consultations]] |
| "Profiling and the Rule of Law" 1 Identity Info. Soc. 55 (2008) | Hildebrandt | Advanced profiling "answer[s] questions we did not raise" and "generate[s] knowledge we did not anticipate" | Scope of profiling | [[Algorithmic Gatekeeping in Administrative Consultations]] |
| "Why a Right to Explanation...Does Not Exist" 7 Int'l Data Privacy L. 76 (2017) | Wachter, Mittelstadt & Floridi | Profiling focused on generating predictions/inferences about individuals beyond data explicitly provided | Inference-based profiling | [[Algorithmic Gatekeeping in Administrative Consultations]] |
| "Counterfactual Explanations Without Opening the Black Box" 31 Harvard J.L. & Tech. 841 (2018) | Wachter, Mittelstadt & Russell | Counterfactual explanations distinguishing probabilistic from deterministic thresholds | Materiality threshold | [[Algorithmic Gatekeeping in Administrative Consultations]] |

---

### Empirical Evidence & Data for RQ1

**Datasets/Surveys:**
- Future of Privacy Forum analysis of 70+ automated decision-making cases across EU Member States (May 2022) - Found in: [[Article 22 GDPR ADM]], [[Algorithmic Gatekeeping in Administrative Consultations]]

**Quantitative Thresholds:**
- SCHUFA: Approximately 80% correlation between insufficient credit score and loan denial ("in almost all cases") - Source: [[Evaluation-Synthesis]], [[Algorithmic Gatekeeping in Administrative Consultations]]
- Red flag indicator: <1% rejection/override rate suggests no genuine human intervention - Source: [[Evaluation-Synthesis]]
- Green flag indicator: 5-20% override rate (context-dependent) may indicate meaningful intervention - Source: [[Evaluation-Synthesis]]

**Practical Indicators (Red Flags for Non-Meaningful Intervention):**
- Human clicks "approve" button without substantive review - Source: [[Evaluation-Synthesis]]
- Reviewer "can reject in exceptional cases" only - Source: [[Evaluation-Synthesis]]
- Reviewer lacks access to input data or decision logic - Source: [[Evaluation-Synthesis]]
- Reviewer trained to default to algorithm recommendation - Source: [[Evaluation-Synthesis]]
- Time constraints preventing careful review - Source: [[Evaluation-Synthesis]]

**Provider Examples/Case Studies:**
- SCHUFA credit scoring system: Third-party lenders relied on scores as primary basis for credit decisions - Analyzed in: [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]]
- University proctoring software (Portugal): Humans nominally reviewed but lacked guidance on when to diverge - Analyzed in: [[Algorithmic Gatekeeping in Administrative Consultations]]
- Austrian employment service algorithmic categorization: Determined service levels for jobseekers - Analyzed in: [[Algorithmic Gatekeeping in Administrative Consultations]]

---

### Key Tests, Frameworks & Standards for RQ1

**1. Meaningful Human Intervention Test (Four Cumulative Elements)**
- **Established by:** WP251rev.01 p. 10, elaborated in [[Evaluation-Synthesis]]
- **Definition:** Human involvement satisfies "not solely automated" requirement only when genuinely meaningful
- **Elements/Criteria:**
  1. **Authority & Empowerment:** Formal authority to alter outcome; not constrained by predetermined instructions; can genuinely reject machine recommendation
  2. **Information Access:** Receives same or better information as algorithm; understands decision logic and factors; has context about individual affected
  3. **Competence & Training:** Skills/expertise to evaluate decision; time to conduct meaningful assessment; accountable for decision alteration
  4. **Genuine Exercise:** Intervention not mere formality; actually engages with decision; can and does make different decisions when warranted
- **Applied in:** [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]], [[Article 22 GDPR ADM]]
- **Application & Conclusion:** Documents apply this test to consultation filtering and conclude that if authority's decision-makers receive only AI-generated summary without access to filtered submissions, and lack clear instructions on when to seek additional input, the filtering may constitute "solely automated" decision despite human making final concession determination.

**2. "Determining Role" Test (SCHUFA Doctrine)**
- **Established by:** SCHUFA C-634/21 ¶50
- **Definition:** Where automated probability value "plays a determining role" in subsequent decisions, establishment of that value constitutes a decision under Article 22(1)
- **Elements/Criteria:**
  1. Automated processing produces assessment/score/output
  2. Third parties rely on ("draw strongly on") this output
  3. Output correlates highly with final outcomes (approximately 80% in SCHUFA)
  4. Third parties cannot or do not meaningfully diverge from algorithmic recommendation
- **Applied in:** [[ADM-Taxonomy-Elements]], [[Evaluation-Synthesis]], [[Algorithmic Gatekeeping in Administrative Consultations]], [[Algorithmic Gatekeeping in the Public Sphere (Draft)]]
- **Application & Conclusion:** Documents argue this logic extends to information filtering—if generating information that determines outcomes constitutes a "decision," then omitting information that would determine outcomes should equally qualify. Applied to consultation filtering: if filtered inputs would have influenced outcomes, omission plays a determining role.

**3. Anti-Circumvention Principle**
- **Established by:** SCHUFA C-634/21 ¶¶61-63
- **Definition:** Article 22 must be interpreted to prevent controllers from avoiding its protections by structuring processing as "mere information provision" when that information determines results
- **Elements/Criteria:**
  1. Controller characterizes processing as preparatory/informational
  2. Processing actually constrains or determines downstream decisions
  3. Narrow interpretation would create "lacuna in legal protection"
- **Applied in:** [[ADM-Taxonomy-Elements]], [[Algorithmic Gatekeeping in Administrative Consultations]]
- **Application & Conclusion:** Prevents authorities from evading Article 22 by characterizing algorithmic filtering as "consultation management" when filtering functionally determines which voices are heard.

**4. Three-Part Decision Existence Test**
- **Established by:** WP251rev.01 p. 9-10, synthesized in [[Evaluation-Synthesis]]
- **Definition:** Test for whether processing constitutes a "decision" under Article 22
- **Elements/Criteria:**
  1. **Assessment Requirement:** Processing constitutes evaluation of personal aspects with determination
  2. **Output Requirement:** Process produces determinate outcome (approval/denial, accept/reject)
  3. **Third-Party Reliance (Post-SCHUFA):** Does act play decisive role in downstream decisions?
- **Applied in:** [[Evaluation-Synthesis]]
- **Application & Conclusion:** Applied to consultation filtering—filtering produces determinate outcome (include/exclude) and plays decisive role in what decision-makers consider, satisfying all three elements.

**5. Sophistication Threshold (ICO Content Moderation)**
- **Established by:** ICO Guidance on Content Moderation (March 2024)
- **Definition:** Distinguishes between simple matching and sophisticated predictive systems for Article 22 purposes
- **Elements/Criteria:**
  - Simple matching to prohibited material lists determined by humans → likely NOT Article 22 decision
  - "Sophisticated systems making predictions based on context" that significantly affect outcomes → likely IS Article 22 decision
- **Applied in:** [[Algorithmic Gatekeeping in Administrative Consultations]]
- **Application & Conclusion:** Consultation filtering using NLP/LLMs for relevance assessment likely qualifies as "sophisticated system making predictions"—not simple keyword matching—suggesting Article 22 applies.

**6. Doctrinal Evolution Timeline**
- **Established by:** Synthesis in [[Evaluation-Synthesis]]
- **Definition:** Framework showing how Article 22 interpretation has evolved
- **Periods:**
  1. **Pre-SCHUFA (Pre-Dec 2023):** Narrow scope; "decision" required final determination; service providers not subject to Article 22
  2. **SCHUFA Era (Dec 2023 – Feb 2025):** Broader scope; preparatory acts can be decisions; service providers liable; "determining role" test
  3. **Post-Dun & Bradstreet (Feb 2025 – Current):** Heightened transparency; "meaningful information" requires substantive explanation; trade secrets not defense
- **Applied in:** [[Evaluation-Synthesis]]
- **Application & Conclusion:** Current interpretation (post-Feb 2025) is at its broadest, supporting argument that consultation filtering triggers Article 22.

---

### RQ1 Extraction Summary

**Coverage strength:**
- **Well-developed sub-topics:**
  - Meaningful human intervention test (four cumulative elements with practical indicators)
  - SCHUFA "determining role" doctrine with specific paragraph citations
  - Rubber-stamping phenomenon and automation bias
  - Information gatekeeping as decision-making

- **Under-developed areas:**
  - Precise quantitative threshold for "determining role" (only 80% SCHUFA example)
  - Specific standards for consultation filtering (novel application of doctrine)
  - How to measure "genuine exercise" of human review in practice

- **Source depth:** Heavy reliance on WP251rev.01 (with specific page citations) and SCHUFA C-634/21 (with paragraph-level citations). C-203/22 Dun & Bradstreet adds transparency dimension. Academic scholarship (Veale & Binns, Kaminski, Malgieri) provides theoretical framework. Limited national court precedent directly on point for consultation filtering.

**Key findings:**
- The "solely automated" question is the project's doctrinal centerpiece
- Post-SCHUFA doctrine strongly supports argument that preparatory algorithmic acts constitute "decisions"
- The "determining role" test provides framework but threshold remains uncertain
- Tension exists between WP251's recommendation/decision distinction and SCHUFA's broad interpretation
- Resolution likely depends on factual showing of how much filtering constrains downstream decision-making

**Gaps or questions:**
- **Quantitative threshold:** Is 80% correlation required, or would 60-70% suffice?
- **Override rate benchmarks:** What percentage of human overrides indicates "meaningful" intervention?
- **Information gatekeeping boundary:** At what point does preprocessing become decision-making?
- **Public sector specificity:** Does SCHUFA (private sector credit) translate to government consultations?
- **Novel application:** No direct case law on AI filtering of public consultation submissions

**Estimated readiness:** **Strong foundation** - Comprehensive doctrinal framework with specific citations. Ready for Phase 3 synthesis. Would benefit from additional case law if available on government algorithmic processing of citizen inputs.

---
