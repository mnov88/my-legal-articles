# Automated Decision-Making and Profiling: Doctrinal Taxonomy and Constitutive Elements

## I. FOUNDATIONAL FRAMEWORK

### A. Definition and Scope of Profiling

**Doctrinal Element 1: Automated Processing of Personal Data**

**Statutory Definition (Article 4(4) GDPR):**
Profiling is defined as "any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning that natural person's performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements."

**Key Components (WP251rev.01, p. 7):**
- Must involve automated form of processing (human involvement does not necessarily negate profiling classification)
- Applied to personal data
- Objective: evaluate personal aspects about a natural person

**Three-Stage Model (WP251rev.01, p. 8):**
1. Data collection
2. Automated analysis to identify correlations
3. Applying the correlation to an individual to identify characteristics of present or future behavior

**Data Categories in Profiling (WP251rev.01, p. 8):**
- Directly provided by individuals (questionnaires, applications)
- Observed data (location via application, behavioral tracking)
- Derived or inferred data (existing credit scores, previously created profiles)

**Doctrinal Element 2: Legal Distinctions Between Profiling Categories**

The GDPR addresses profiling through three distinct mechanisms (WP251rev.01, p. 9):

1. **General Profiling (Chapter IV of WP251rev.01)**
   - No specific prohibition
   - Subject to general GDPR principles (lawfulness, fairness, transparency)
   - Requires transparency and fairness safeguards

2. **Decision-Making Based on Profiling (Mixed Regime)**
   - Involves profiling plus a decision affecting the individual
   - Not purely automated (human element involved)
   - Subject to transparency, accountability, and fairness requirements

3. **Solely Automated Individual Decision-Making Including Profiling (Article 22)**
   - Subject to general prohibition with three specific exceptions
   - Requires explicit safeguards and data subject rights
   - Focus of WP251rev.01 Chapter III and CJEU jurisprudence

---

## II. ARTICLE 22 PROHIBITION: THREE CONSTITUTIVE CONDITIONS

### A. Condition One: Existence of a "Decision"

**Statutory Requirement (Article 22(1) GDPR):**
"The data subject shall have the right not to be subject to a decision based solely on automated processing..."

**Definition from WP251rev.01 (p. 9-10):**
A "decision" in this context means:
- An assessment or evaluation of a person
- That has a legal or similarly significant effect on that person
- Produces a particular outcome (approval/denial, grant/refusal)
- Not merely preliminary or advisory

**Preparatory Acts as Decisions (SCHUFA C-634/21, Dec. 2023):**
The CJEU established that preparatory acts can constitute "decisions" within Article 22(1) if they:
- Constitute a decisive step in a decision-making process
- Play a significant role in determining the final outcome
- Are actively relied upon by third parties in their own decision-making

**SCHUFA Application:** Automated credit scoring by SCHUFA Holding constituted a "decision" because lenders "drew strongly" on these scores to establish, implement, or terminate contracts. The score was not merely informational but determinative of lending decisions.

**Practical Implication:**
- Service providers creating profiles, scores, or algorithmic outputs used by third parties in decision-making may themselves be subject to Article 22 obligations
- Not just the entity making the final decision, but providers of algorithmic inputs bear responsibility

### B. Condition Two: Processing Must Be "Solely" Automated

**Statutory Language (Article 22(1) GDPR):**
"...based solely on automated processing, including profiling..."

**WP251rev.01 Interpretation (p. 10-11):**

**Meaning of "Solely":**
- Processing must be entirely automated
- No meaningful human involvement in the decision-making process
- Human involvement must be genuine and substantive, not merely ceremonial

**Definition of Meaningful Human Intervention (WP251rev.01, p. 10):**
Human involvement satisfies this requirement only when:
1. The person performing the human review has the authority and competence to change the decision
2. The person actually engages with the decision, considering all available inputs and outputs
3. The intervention goes beyond perfunctory rubber-stamping
4. The person involved possesses decision-making authority

**What Does NOT Constitute Meaningful Human Involvement:**
- Token human review that cannot alter the outcome
- Cursory examination of automated decision
- Review by individuals lacking authority to change results
- Human confirmation of an essentially predetermined outcome

**Practical Threshold:**
The human element must be capable of altering the decision and exercised with genuine authority and competence. Procedural compliance without substantive decision-making power is insufficient.

### C. Condition Three: Production of "Legal Effects" or "Similarly Significant Effects"

**Statutory Language (Article 22(1) GDPR):**
"...which produces legal effects concerning him or her or similarly significantly affects him or her"

**Legal Effects (WP251rev.01, p. 11-12):**
Include decisions that:
- Have legal consequences for the data subject
- Alter the legal rights/obligations of the individual
- Produce binding legal implications
- Examples: contract conclusion/rejection, credit approval/denial, employment decisions

**Similarly Significant Effects (WP251rev.01, p. 11-12):**
Extend beyond narrow legal effects to include:
- Denial or granting of services or goods
- Discriminatory treatment
- Exclusion from opportunities
- Significantly altered circumstances or life chances
- Impact on professional opportunities or personal dignity

**Key Interpretive Principle (WP251rev.01, p. 11):**
The GDPR recognizes that automated decision-making can have serious consequences even without formal legal effects. The threshold is effects that are "similarly significant" to legal effects—i.e., substantively important to the individual's circumstances.

**SCHUFA C-634/21 Application:**
The CJEU confirmed that credit scoring producing "legal or similarly significant effects" includes:
- Decisions about credit access (legal effect)
- Determinations affecting financial accessibility to credit (similarly significant effect)
- Third-party reliance on scores in making contractual decisions

**Test for "Significant Effect" (Inferred from WP251rev.01 and CJEU jurisprudence):**
An effect is "similarly significant" if it:
1. Substantially impacts the data subject's interests or opportunities
2. Affects fundamental rights or freedoms
3. Determines access to important goods or services
4. Influences professional or personal circumstances materially

---

## III. EXCEPTIONS TO THE GENERAL PROHIBITION

### A. Three Statutory Exceptions (Article 22(2) GDPR)

The general prohibition in Article 22(1) does not apply if the decision is:

**Exception 1: Necessary for Performance of a Contract (Article 22(2)(a))**

**Scope (WP251rev.01, p. 12-13):**
- Automated decision-making necessary to enter into or perform a contract with data subject
- Limited to decisions integral to contract execution
- Cannot be used for purposes beyond contract performance

**Conditions:**
- Decision must be necessary (not merely convenient)
- Must relate to contract between controller and data subject
- Must fall within reasonable expectations of contracting parties

**Example:** Automated order processing for e-commerce transactions

**Exception 2: Authorization by Law (Article 22(2)(b))**

**Scope (WP251rev.01, p. 13):**
- Automated decision-making authorized by Union or Member State law
- Law must specify the automated processing
- Law must lay down suitable safeguards for data subject rights and freedoms

**Double Requirements:**
1. Legal authorization for automated processing
2. Legal protection of safeguards (not discretionary)

**Practical Application:**
Requires explicit legislative basis in national/EU law, not merely permissive silence

**Exception 3: Based on Explicit Consent (Article 22(2)(c))**

**Scope (WP251rev.01, p. 13-14):**
- Data subject must provide explicit, informed consent
- Consent must be specific to automated decision-making
- Governed by Article 7 GDPR consent requirements

**Requirements for Valid Consent (WP251rev.01, p. 13):**
- Freely given (not coerced)
- Specific (not blanket)
- Informed (understanding of consequences)
- Unambiguous affirmative action required
- Cannot be precondition for service unless processing is necessary

**Key Limitation:**
Consent cannot override legal prohibitions or fundamentally unfair processing. Even with consent, data subject retains certain rights (Article 22(3)).

### B. Article 22(4) Special Safeguards for Exceptions

**Additional Requirement (Article 22(4) GDPR):**
"In the cases referred to in points (a) and (c) of paragraph 2, the controller shall implement suitable measures to safeguard the data subject's rights and freedoms and legitimate interests..."

**Mandatory Safeguards (WP251rev.01, p. 14):**
1. Specific information to data subject
2. Right to obtain human intervention
3. Right to express point of view
4. Right to obtain explanation of decision
5. Right to challenge decision

---

## IV. INFORMATION AND TRANSPARENCY REQUIREMENTS

### A. Rights to Information: Dual Provisions

**Doctrinal Element 3: Transparency in Automated Decision-Making**

**Statutory Basis (Articles 13-14 GDPR):**

**Article 13(2)(f) and 14(2)(g) - Information on Automated Decision-Making:**
Collected/requested from data subject must include information about the "existence of automated decision-making, including profiling" and where applicable "meaningful information about the logic involved, as well as the significance and the envisaged consequences" for the data subject.

**Article 15(1)(h) - Right of Access:**
Data subject has right of access to information confirming whether automated decision-making occurs and "meaningful information about the logic involved, as well as the significance and the envisaged consequences"

### B. The "Meaningful Information About Logic" Standard

**Key Doctrinal Element: Dun & Bradstreet Austria C-203/22 (Feb. 2025)**

**Prior Standard (Limited Interpretation):**
Controllers faced ambiguity about what "meaningful information" required, with some interpreting this narrowly as high-level descriptions of algorithmic categories.

**CJEU Clarification (C-203/22):**
"Meaningful information about the logic" requires controllers to:

1. **Explain the Procedure and Principles Actually Applied:**
   - Not merely technical descriptions
   - Not statistical abstractions
   - Practical explanation of how algorithm functions relative to the specific data subject

2. **Enable Data Subject Understanding:**
   - Information must facilitate comprehension of decision-making rationale
   - Enable effective exercise of data subject rights
   - Allow data subject to contest the decision knowledgeably

3. **Overcome Trade Secret Limitations:**
   - Trade secrets do not excuse obligations under Article 22(3)
   - Controllers must find means to explain logic while protecting legitimate business interests
   - Judicial authorities and DPAs can access algorithmic information to enforce rights

**Practical Standard (from C-203/22):**
Information must progress beyond:
- ❌ "Algorithm processed your data"
- ❌ "Socio-demographic factors given equal weighting"
- ✓ Substantive explanation of how specific data inputs produced the score/decision regarding this individual

---

## V. DATA SUBJECT RIGHTS IN AUTOMATED DECISION-MAKING

### A. Right to Meaningful Explanation (Article 22(3))

**Statutory Requirement:**
Data subject shall have "the right to obtain an explanation of the decision reached after such assessment"

**Interpretation from WP251rev.01 (p. 14):**
- Right to understand why decision was made
- Right to know which factors influenced outcome
- Right to challenge the decision on grounds of error or unfairness

**Application of C-203/22 Standard:**
- Explanation must relate to factors/logic actually applied
- Cannot be generic descriptions of system operation
- Must enable data subject to assess decision's accuracy and fairness

### B. Right to Human Intervention and Contest

**Article 22(3) Rights (WP251rev.01, p. 14-15):**
1. **Right to obtain human intervention:** Data subject can request human review/decision-making
2. **Right to express point of view:** Opportunity to present alternative information or perspective
3. **Right to challenge the decision:** Ability to contest decision's accuracy or appropriateness

**Conditions for Exercising Rights:**
- Applicable when automated decision produces legal/significant effects
- Data subject must exercise right in identifiable manner
- Controller must respond substantively, not ceremonially

### C. Right to Object and Data Subject Protections

**Article 21 Right to Object (WP251rev.01, p. 15):**
- Data subject may object to profiling generally
- Includes objection to profiling for marketing purposes (Article 21(2))
- Controller must cease processing unless legitimate interest override

**Additional Protections (WP251rev.01, p. 15-16):**
- Special protection for children's profiling (Article 8(1))
- Heightened scrutiny for sensitive purposes (health, employment)
- Requirement for DPIA when automated processing involves high risk

---

## VI. SAFEGUARDS AND FAIRNESS REQUIREMENTS

### A. General GDPR Principles Applied to Automated Processing

**Doctrinal Element 4: Lawfulness, Fairness, Transparency (Article 5(1)(a))**

**Lawfulness Requirement (WP251rev.01, p. 16-17):**
- Processing must have lawful basis (Article 6 GDPR)
- Automated processing must be legally permitted
- Cannot circumvent legal restrictions through automation

**Fairness Requirement (WP251rev.01, p. 17):**
- Processing must not be discriminatory or unjustly prejudicial
- Must not perpetuate stereotypes or social segregation
- Cannot lock individuals into categories restricting autonomy
- Must account for accuracy and avoid inaccurate predictions

**Transparency Requirement (WP251rev.01, p. 17-18):**
- Processing operation must be transparent to data subjects
- Information must be clear and accessible
- Rationale for decision must be intelligible

### B. Data Minimization in Automated Processing (Article 5(1)(c))

**Principle (WP251rev.01, p. 18-19):**
- Only necessary data for profiling/decision-making should be processed
- Automated processing should not be pretext for mass data collection
- Controller must limit scope of profiling to its stated purpose

**Application to Profiling:**
- Cannot collect data "just in case" for future profiling
- Categories of data used must be justified by decision-making purpose
- Sensitive categories require heightened justification

### C. Purpose Limitation in Profiling (Article 5(1)(b))

**Principle (WP251rev.01, p. 18):**
- Further processing of profiling data must be compatible with original purpose
- Cannot use profile created for one purpose to make automated decisions for different purpose
- Secondary uses require new legal basis or compatible purpose assessment

---

## VII. SPECIAL CATEGORIES AND SECTOR-SPECIFIC CONSIDERATIONS

### A. Profiling of Children (Article 8)

**Special Protection (WP251rev.01, p. 20-21):**
- Enhanced scrutiny required for automated processing of children's data
- Consent for automated decision-making of children subject to stricter requirements
- Profiling of children for behavioral prediction (particularly for marketing) requires heightened fairness assessment

### B. Sensitive Data and Profiling

**Article 9 Restrictions (WP251rev.01, p. 19-20):**
- Automated processing of special categories (health, race, political opinion) subject to heightened restrictions
- Derogation for explicit consent requires higher standard
- Legal authorization for such processing must be explicit

**Discrimination Risk Assessment (WP251rev.01, p. 20):**
- Automated decision-making involving sensitive categories requires specific attention to discrimination
- Proxy discrimination analysis necessary (inferential data may encode protected characteristics)
- Fairness testing across demographic groups required

---

## VIII. ORGANIZATIONAL ACCOUNTABILITY MECHANISMS

### A. Data Protection Impact Assessment (Article 35)

**Trigger (WP251rev.01, p. 21-22):**
DPIA required when automated processing:
- Is large-scale
- Involves sensitive categories
- Involves systematic monitoring
- Involves profiling or automated decision-making with significant effects

**Content Requirements (WP251rev.01, p. 22):**
- Description of processing operation and its purpose
- Assessment of necessity and proportionality
- Evaluation of risks to data subject rights/freedoms
- Description of safeguards and mitigation measures

### B. Data Protection Officer Role (Article 37-38)

**DPO Responsibilities (WP251rev.01, p. 22-23):**
- Monitor automated processing compliance
- Advise on Article 22 applicability
- Ensure safeguards are implemented
- Review DPIA for automated decision-making

### C. Accountability and Documentation (Article 5(2), Article 30)

**Documentation Requirements (WP251rev.01, p. 23):**
- Record processing of automated decision-making
- Document legal basis for each category of automated processing
- Maintain records of testing for bias/fairness
- Document safeguards implemented
- Maintain audit trail for decisions made

---

## IX. SYNTHESIS: DECISION-MAKING FLOWCHART

**Applying Article 22 GDPR:**

**Step 1: Is there automated processing of personal data?**
- YES → Continue to Step 2
- NO → Article 22 does not apply; apply general GDPR principles

**Step 2: Does the processing produce a "decision"?**
- Definition: Assessment/evaluation with legal or similarly significant effects
- Includes preparatory acts that determinatively influence third-party decisions
- YES → Continue to Step 3
- NO → General profiling rules apply; ensure transparency and fairness

**Step 3: Is processing "solely" automated?**
- Test: Is there meaningful human intervention with authority and competence to alter outcome?
- YES (meaningful intervention) → Not solely automated; apply general rules + safeguards
- NO → Continue to Step 4

**Step 4: Does decision produce legal or similarly significant effects?**
- Legal effects: Contract decisions, credit approvals, employment determinations
- Similarly significant effects: Access to services, denial of goods, discrimination, material impact on circumstances
- YES → Continue to Step 5
- NO → General GDPR principles apply

**Step 5: Does an exception apply? (Article 22(2))**
- **Exception A:** Necessary for contract performance?
- **Exception B:** Authorized by law with safeguards?
- **Exception C:** Based on explicit consent?
- NO exceptions apply → Article 22(1) prohibition triggered; processing is unlawful unless one exception applies
- Exception applies → Continue to Step 6

**Step 6: Implement Article 22(4) Safeguards**
- Provide specific information to data subject
- Implement right to human intervention
- Facilitate right to express point of view
- Provide meaningful explanation of decision
- Ensure right to contest decision
- All safeguards must be meaningful and substantive

---

## X. DOCTRINAL GAPS AND EVOLVING INTERPRETATION

### A. Open Questions Post-SCHUFA and C-203/22

1. **Scope of "Preparatory Acts":** How far upstream in decision chain does Article 22 apply to preliminary assessments?
2. **Meaningful Information Adequacy:** What level of algorithmic detail satisfies "meaningful information" without exposing trade secrets?
3. **Human Intervention Benchmarks:** How must human reviewers demonstrate competence and authority in practice?
4. **Significant Effects Threshold:** What quantifiable or qualitative standards determine "similarly significant effects"?

### B. Emerging Issues

1. **AI Systems Opacity:** Deep learning models create challenges for explainability requirements
2. **Service Provider Chain:** Responsibility allocation when multiple entities contribute to algorithmic decision-making
3. **Inference and Proxy Variables:** How to assess discrimination in purely correlational algorithms using non-protected characteristics
4. **Real-Time Decisioning:** Application of human intervention requirement in high-frequency automated systems

---

## BIBLIOGRAPHY OF KEY SOURCES

**EU Legislation:**
- Regulation (EU) 2016/679 (GDPR), Articles 4(4), 5, 6, 8-9, 13-14, 15, 21-23, 30, 35, 37-38
- Charter of Fundamental Rights of the EU, Articles 7-8

**WP29/EDPB Guidance:**
- WP251rev.01: Guidelines on Automated individual decision-making and Profiling for the purposes of Regulation 2016/679 (Adopted 3 Oct 2017; revised 6 Feb 2018; endorsed EDPB 25 May 2018)

**CJEU Jurisprudence:**
- CJEU, C-184/20, OT v Vyriausioji tarnybinės etikos komisija (1 Aug 2022)
- CJEU, C-634/21, SCHUFA Holding v Bundesverwaltungsgericht (7 Dec 2023) - ECLI:EU:C:2023:957
- CJEU, C-203/22, CK v Magistrat der Stadt Wien (26 Feb 2025) - ECLI:EU:C:2025:131
