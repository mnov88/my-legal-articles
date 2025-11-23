# National DPA decisions: relevance mapping for EDPL paper

This document maps national DPA enforcement decisions to the paper's arguments, identifying which decisions add new arguments or nuance beyond what is currently cited.

---

## Decisions currently used in V2 draft

### Berlin DPA (BlnBDI) - 31.05.2023

**Context**: €300,000 fine against bank for refusing to explain automated credit card rejection.

**Currently used for**: Article 22(3) safeguards; requirement for individualized explanation.

**Key holdings**:
- Automated decision-making requires "concrete information about the database used, the factors and the criteria influencing the decision"
- Generic descriptions insufficient; must explain "criteria for rejection in individual cases"
- Violation found despite nominal human involvement available

**Assessment**: Adequately integrated into current draft. No additional material needed.

---

### Austrian DSB - 2020-0.436.002

**Context**: Marketing scores classifying individuals into categories (conservatives, traditionalists, hedonists, etc.).

**Currently used for**: Article 15(1)(h) scope; trade secrets not overriding transparency.

**Key holdings**:
- Article 15(1)(h) applies to "all" profiling activities, not merely Article 22(1) and (4) cases
- Trade secrets cannot be blanket justification for non-disclosure
- Required information includes: parameters/input variables; their effect on scoring; explanation of classification result; possible profile categories
- Fundamental rights (Art. 8 ECHR, Art. 8 CFR) weigh against restricting access rights

**Assessment**: Adequately integrated. The "all profiling" point could be emphasised more in the context of consultation filtering even where Article 22 applicability is uncertain.

**Potential enhancement**: Strengthen argument that even if Article 22 doesn't clearly apply, Article 15(1)(h) transparency rights apply to consultation filtering as profiling under Article 4(4).

---

### Italian Garante - Deliveroo (9685994) - July 2021

**Context**: €2,500,000 fine for inadequate transparency about rider management algorithms.

**Currently used for**: Access-to-opportunity framework; algorithmic gatekeeping of work opportunities.

**Key holdings**:
- Algorithmic scoring determining shift access constitutes profiling with "significant effect" because it "allows (or denies) access to job opportunities"
- Location tracking every 12 seconds without adequate disclosure violates transparency
- System that "penalizes riders with a lower score, even though a score can be lowered by simply not logging into the app" requires transparency about assignment algorithms
- Controllers cannot claim statistical information about system satisfies transparency requirements

**Assessment**: Well integrated for access-to-opportunity analogy. The "penalisation for non-engagement" point could be developed further.

**Potential enhancement**: Develop parallel between riders penalised for not logging in and consultation submitters whose non-standard expression may be algorithmically deprioritised.

---

## Decisions requiring deeper integration

### Finnish DPA (Tietosuojavaltuutettu) - 6482/186/2020 (**HIGH RELEVANCE**)

**Context**: Warning issued regarding health benefit assessment tool that uses algorithms to identify patients for proactive healthcare.

**Key holdings - critical for paper**:

1. **The "negative selection" problem**: The DPA distinguished between:
   - Patients SELECTED by the algorithm for human review: NOT solely automated (human makes final assessment)
   - Patients NOT SELECTED by the algorithm: IS solely automated decision because "the result of the profiling remains final" and "the person no longer re-evaluates the evaluation produced by the tool"

2. **Significant effects from exclusion**: "It is sufficient that the profiling actually affects the patient's chances of receiving healthcare services." Being excluded from special preventive measures = significant effect.

3. **Access denial vs. opportunity exclusion**: "In terms of significant effects, it is not necessary for the patient to be actively denied access to the treatment. It is sufficient that the profiling actually affects the patient's chances of receiving healthcare services."

**Relevance to paper**: This decision directly supports the paper's "upstream trap" argument. When AI filtering excludes consultation submissions:
- The exclusion IS the solely automated decision (humans only review "selected" submissions)
- Effects are significant because submitters are excluded from opportunity to influence policy
- No need to show active "denial" - exclusion from consideration suffices

**Recommendation**: ADD to Part III (solely automated) and Part V (similarly significant effects). This is the strongest national DPA support for the paper's central argument.

**Suggested citation point**: Part III.C ("The upstream trap") - the Finnish case provides direct precedent that non-selection by algorithm constitutes solely automated decision.

---

### Finnish DPA - 3895/83/22 (companion case)

**Context**: Same health benefit assessment tool; identical holding on negative selection.

**Assessment**: Reinforces 6482/186/2020. Cite if wanting to emphasise consistency of approach.

---

## Decisions with potential nuance

### Italian Garante - Foodinho/Glovo (9675440) - June 2021

**Context**: €2,600,000 fine against Foodinho (Glovo) for rider management algorithms.

**Key holdings beyond Deliveroo**:
- Algorithmic management without transparency about logic violates Article 22
- Booking systems determining work access constitute profiling affecting employment opportunities
- Controller must verify "algorithm correctness and accuracy"
- Must implement measures to "prevent errors and discrimination"

**Assessment**: Reinforces Deliveroo analysis. The "prevent errors and discrimination" point could strengthen safeguards discussion.

**Potential enhancement**: Add to Part VII (safeguards) - requirement to verify algorithm accuracy and prevent discrimination maps to consultation filtering context.

---

### Spanish AEPD decisions (PS/00037/2020 and others)

**Context**: Multiple decisions on automated decision-making in commercial contexts.

**Key holdings**:
- Four-factor test for meaningful human involvement (already referenced via guidance)
- Physical impossibility calculations for human review
- Explanations must include "importance and consequences with examples"

**Assessment**: The four-factor test is already integrated. The physical impossibility calculations could be more prominent.

**Potential enhancement**: Add specific AEPD calculation example to Part III.D (100 reports × 100 pages = 21 pages/minute = impossible meaningful review).

---

### Greek HDPA - 30/2024 and 51/2021

**Context**: Access rights enforcement; algorithmic processing transparency.

**Key holdings**:
- Controllers cannot ignore data subject requests for information about algorithmic processing
- Fines for failure to respond to access requests AND failure to cooperate with supervisory authority

**Assessment**: Reinforces enforcement seriousness but doesn't add new doctrinal arguments. Lower priority.

---

### Portuguese CNPD - 2024/279 (Worldcoin)

**Context**: Jurisdictional determination re biometric data collection.

**Assessment**: Primarily addresses one-stop-shop mechanism and establishment questions. Not directly relevant to Article 22 analysis. Low priority.

---

### Danish Datatilsynet - 2019-421-0028

**Context**: Early Article 22 enforcement.

**Assessment**: Would need further review. Lower priority given stronger precedents available.

---

## Summary: recommended additions to V2 draft

### High priority (new arguments)

1. **Finnish DPA 6482/186/2020**: Add to Parts III and V. Critical support for "negative selection = solely automated decision" argument. This is the missing piece that directly addresses the paper's central claim about upstream filtering.

### Medium priority (additional nuance)

2. **Italian Garante Foodinho**: Add to Part VII safeguards discussion - requirement to verify algorithm accuracy and prevent discrimination.

3. **Spanish AEPD physical impossibility calculation**: Make more prominent in Part III.D.

4. **Austrian DSB "all profiling" point**: Strengthen argument that Article 15(1)(h) applies regardless of Article 22 uncertainty.

### Low priority (reinforcement only)

5. Greek HDPA decisions: Already adequately represented in enforcement seriousness.
6. Portuguese CNPD Worldcoin: Not relevant to Article 22 analysis.
7. Danish Datatilsynet: Superseded by more recent precedents.

---

## Suggested integration for Finnish DPA decision

**Part III.C (The upstream trap)** - add after current paragraph on SCHUFA:

> The Finnish Data Protection Authority's decision in case 6482/186/2020 provides direct support for this analysis in the administrative context. The authority examined a health benefit assessment tool that used algorithms to identify patients for proactive healthcare measures. The authority distinguished between two categories of patients: those selected by the algorithm for human review, and those not selected. For the former, the authority found no solely automated decision because healthcare professionals made final assessments considering other factors. For the latter, however, the authority held that "the result of the profiling remains final" and "the person no longer re-evaluates the evaluation produced by the tool." The non-selection by the algorithm constituted a solely automated decision because no human subsequently reconsidered the algorithmic determination.

**Part V.B (Similarly significant effects)** - add to access-to-opportunity discussion:

> The Finnish DPA's reasoning on significant effects merits attention. The authority rejected the controller's argument that no services were denied by the algorithm. Instead, the authority held that "it is sufficient that the profiling actually affects the patient's chances of receiving healthcare services." Being excluded from proactive healthcare measures - not receiving an invitation for preventive care that others received based on algorithmic selection - constituted significant effects. Applied to consultation filtering, this reasoning supports recognising exclusion from consideration as producing significant effects: the submitter's chances of having their voice considered are affected by the algorithmic determination, even without formal denial.

---

*Document created: 2025-11-22*
*Purpose: Assess whether additional DPA decisions should be integrated into EDPL V2 draft*
