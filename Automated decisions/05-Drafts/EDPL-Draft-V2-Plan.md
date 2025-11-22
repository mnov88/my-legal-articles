# EDPL Draft V2 Plan: Enhanced Thesis and Structural Revisions

## Executive Summary

Analysis of the Hypotheticals Case Matrix reveals that the current draft, while doctrinally rigorous, can be substantially strengthened by:
1. Reframing the thesis to acknowledge doctrinal uncertainty while making a stronger normative argument
2. Situating consultation filtering within the broader administrative AI landscape
3. Developing three under-explored arguments: "about whom," procedural-as-substantive, and access-to-opportunity
4. Making the paper's original contribution more explicit: arguing that democratic participation effects should be recognized as "similarly significant"

---

## I. THESIS RESTATEMENT

### Current Implied Thesis (V1)
"AI filtering of consultation submissions likely violates Article 22 GDPR because it plays a 'determining role' in excluding citizen voices from democratic deliberation."

### Proposed Revised Thesis (V2)
"AI filtering of public consultation submissions represents a paradigm case exposing critical unresolved questions in Article 22 GDPR interpretation. This article argues that three doctrinal gaps—regarding democratic participation as 'similarly significant effect,' content evaluation as profiling, and procedural determinations as decisions—should be resolved in favor of protection. The SCHUFA 'determining role' doctrine, properly applied alongside Article 22's fundamental rights purpose, supports bringing consultation filtering within the prohibition's scope. Even where doctrinal uncertainty persists, complementary frameworks (AI Act, administrative law, Aarhus Convention) establish robust accountability obligations."

### Why This Is Stronger
- **Intellectually honest**: Acknowledges this is novel territory rather than settled law
- **Makes original contribution explicit**: Arguing how gaps *should* be filled, not merely describing them
- **Strategic positioning**: Places paper at cutting edge of Article 22 development
- **Broader applicability**: Framework developed applies beyond consultation filtering

---

## II. KEY STRUCTURAL CHANGES

### A. New Material: Situating the Case (Insert after current Part II or as new II.C)

**Proposed Title**: "The Administrative AI Landscape: Where Consultation Filtering Sits"

**Content**:
- Brief taxonomy of AI uses in administration (5 types × 5 contexts from matrix)
- Position consultation filtering in the risk spectrum:
  - Higher risk than: complaint routing, FOI categorization, organizational clustering
  - Lower risk than: benefit eligibility scoring, regulatory inspection selection, procurement fraud flagging
  - Similar risk to: complaint sentiment analysis, FOI prioritization
- Explain why this positioning matters: paradigm case for doctrinal development because neither clearly within nor clearly outside Article 22
- Frame the doctrinal questions the paper will address

**Purpose**: Gives readers analytical framework for assessing relative risk; positions paper as providing tools beyond the specific case

### B. Strengthened Part V: Legal and Similarly Significant Effects

**Current gap**: The "democratic participation effects" argument is powerful but under-developed given that the matrix confirms "No case law on democratic participation effects"

**Additions**:

1. **New subsection V.C-bis: "The Access-to-Opportunity Framework"**
   - Draw explicit analogy: consultation participation is access to opportunity like employment screening or credit access
   - Develop parallel: EDPB recognizes "access to services" as similarly significant; participation in democratic processes is "access to" a democratic "service"
   - Cite Deliveroo analogy more prominently: algorithmic control over work opportunities parallels algorithmic control over participatory opportunities

2. **New subsection V.D-bis: "Democratic Participation as 'Similarly Significant': A Novel Argument"**
   - Explicitly acknowledge this is novel extension
   - Argue for recognition based on:
     - Article 22's fundamental rights purpose (preventing algorithmic determination of significant outcomes)
     - Charter Article 41 (good administration) integration
     - Aarhus Convention's recognition of participation as legally protected interest
     - EU law's general recognition of democratic participation as fundamental value
   - Engage with counterarguments:
     - "Effects are indirect" → Response: SCHUFA rejected formalism; functional effects matter
     - "Participation is political, not personal" → Response: Exclusion affects individual's civic status and dignity
     - "This extends Article 22 too far" → Response: Purpose-based interpretation requires protection where algorithms determine significant outcomes

3. **Strengthen engagement with "indirect effects" counterargument**
   - The matrix identifies this as key vulnerability: "effects on third-party applications...constitute 'similarly significant effects' on the data subject?"
   - Develop argument: the relevant effect is not on the concession decision but on the data subject's participatory rights—their right to be heard was algorithmically denied

### C. Expanded Part VI: Profiling and the "About Whom" Problem

**Current gap**: Section treats profiling analysis somewhat separately from the central question: when does evaluating submission content become evaluating the person?

**Additions**:

1. **New subsection VI.D: "The 'About Whom' Problem: Content Evaluation as Personal Evaluation"**
   - Develop matrix insight: "Article 22 protects data subjects from automated decisions 'about' them. When does processing of submissions/applications become evaluation of submitters/applicants?"
   - Argue: Submission evaluation inherently evaluates personal aspects because:
     - Arguments, reasoning, expression are personal aspects (interests, reliability as participants)
     - Sentiment analysis evaluates emotional state (clearly personal)
     - Relevance scoring evaluates perceived value of person's contribution
     - Quality assessment evaluates communicative competence
   - Draw on Deliveroo: Garante found algorithm evaluated "riders" not just "shifts" because work allocation evaluated rider characteristics
   - Proposed test: If AI classification determines how a person is treated based on evaluation of their communicative acts, this constitutes profiling of "personal aspects"

2. **Strengthen sentiment analysis argument**
   - Matrix identifies: "Sentiment analysis and anomaly detection inherently evaluate personal aspects (emotional state, behavioral patterns) even when ostensibly evaluating submission content"
   - Develop: This is profiling even if not explicitly person-focused
   - Special category data risk more prominent: Any political consultation involves political opinions

### D. New Subsection: Procedural Determinations as Decisions (Insert in Part IV)

**Proposed Title**: "IV.C: When Procedural Determinations Become Substantive Decisions"

**Content**:
- Engage with counterargument: "Filtering is administrative housekeeping, not Article 22 decision"
- Develop functional test based on matrix insights:
  - Procedural determination becomes decision when it has "determining role" in outcome
  - Examples from matrix: routing to dismissive vs. receptive department; categorization determining applicable legal framework; prioritization creating effective denial through delay
- Apply to consultation: filtering that excludes submissions plays determining role in those submissions' fate
- Key argument: Following SCHUFA's purposive reasoning, focusing on procedural vs. substantive characterization would enable circumvention—insert "human housekeeping step" between algorithm and outcome

### E. Reframed Conclusion

**Current conclusion**: Synthesizes findings and provides recommendations

**Enhanced conclusion** should:

1. **Explicitly frame the paper's original contribution**:
   - Novel argument that democratic participation effects should be recognized
   - Analytical framework for assessing administrative AI (applicable beyond consultation)
   - Integration of Article 22 with administrative law and democratic theory

2. **Position the paper in doctrinal development**:
   - Acknowledge this is edge-of-doctrine territory
   - Argue courts should extend Article 22 to consultation filtering based on:
     - Purpose of provision (preventing algorithmic determination of significant outcomes)
     - SCHUFA's anti-formalist reasoning
     - Fundamental rights context (Charter Articles 11, 41, 47)
   - Note that even if Article 22 doesn't clearly apply, analysis reveals need for algorithmic accountability in democratic administration

3. **Stronger normative closing**:
   - Current closing is good but could be more forceful
   - Add: The question is not merely whether Article 22 technically applies, but whether EU law can tolerate algorithmic gatekeeping of democratic participation without meaningful safeguards. The answer should be no.

---

## III. MINOR ADDITIONS AND REFINEMENTS

### A. Comparative Risk Table (New, Part II or Appendix)

Add a simplified version of the matrix showing where consultation filtering sits:

| Context | AI Use | Article 22 Risk | Why |
|---------|--------|-----------------|-----|
| Benefit Eligibility | Predictive Scoring | CRITICAL | Direct profiling + legal effects |
| Regulatory Inspection | Anomaly Detection | CRITICAL | Enforcement consequences + profiling |
| Public Procurement | Predictive Scoring | VERY HIGH | Economic stakes + "about whom" |
| **Public Consultation** | **Filtering/Summarization** | **HIGH (UNCERTAIN)** | **Paradigm case for doctrinal development** |
| Complaint Triage | Routing | LOW | Procedural without significant effects |
| FOI Requests | Categorization | LOW | Organizational efficiency |

### B. Engage with the "Solely Automated" Vulnerability

The matrix notes: "What level of human engagement defeats 'solely automated'?" in mass processing contexts.

**Add to Section III**: Develop the "physical impossibility" argument from Spanish AEPD framework more prominently:
- If authority reviews 10,000 AI-filtered submissions at 30 seconds each = perfunctory
- Cite AEPD's calculation: 100 reports × 100 pages = 21 pages/minute = impossible meaningful review
- Argue: High-volume contexts create structural impossibility of meaningful human intervention

### C. AI Act Integration Strengthening

Current Section VIII is good but could be strengthened:

**Add**: The AI Act's high-risk classification (Annex III, point 8: "administration of justice and democratic processes") effectively recognizes what Article 22 analysis suggests—that AI in democratic contexts requires enhanced oversight. The regulatory convergence supports interpreting Article 22 to apply to consultation filtering.

### D. Title Consideration

**Current**: "Algorithmic Gatekeeping in the Administrative State: AI-Assisted Processing of Public Consultation Submissions Under GDPR Article 22"

**Options for V2**:
- Keep current (strong, descriptive)
- Alternative: "Democratic Participation in the Algorithmic Age: GDPR Article 22 and the Limits of AI-Assisted Public Consultation"
- Alternative: "When Algorithms Filter Democracy: Article 22 GDPR and the Challenge of AI-Assisted Public Consultation"

Recommendation: Current title is effective; no change required unless editor prefers alternative.

---

## IV. WHAT V2 DOES NOT NEED

To maintain focus and appropriate length for EDPL:

1. **Not a full taxonomy paper**: Use matrix insights strategically but don't turn paper into comprehensive administrative AI taxonomy
2. **Not comparative law**: Keep EU focus; comparative analysis (US APA, etc.) remains out of scope
3. **Not empirical**: Don't need to document actual AI deployment (mentioned as potential future work)
4. **Not technical deep-dive**: Maintain current level of technical explanation; don't add ML/NLP detail

---

## V. IMPLEMENTATION APPROACH

### Phase 1: Structural Integration
- Insert new "Situating the Case" material (II.C or new II.A)
- Add "About Whom" subsection (VI.D)
- Add "Procedural Determinations" subsection (IV.C)
- Strengthen "Similarly Significant Effects" with access-to-opportunity framework (V.C-bis, V.D-bis)

### Phase 2: Argument Development
- Revise introduction to signal reframed thesis
- Strengthen engagement with counterarguments throughout
- Make original contribution (democratic participation effects) more explicit

### Phase 3: Conclusion Reframing
- Explicitly position paper's contribution
- Stronger normative closing
- Acknowledge doctrinal uncertainty while arguing for resolution

### Phase 4: Polish
- Add comparative risk table
- Review footnotes for consistency
- Ensure new material integrates smoothly

---

## VI. EXPECTED OUTCOMES

V2 should:
1. **Make a clearer original contribution**: Arguing that democratic participation effects should be recognized as "similarly significant"
2. **Be more intellectually honest**: Acknowledging this is novel territory while arguing for how gaps should be filled
3. **Provide broader analytical tools**: Framework applicable beyond consultation filtering
4. **Be more persuasive**: Engaging counterarguments directly rather than sidestepping
5. **Position the author strategically**: At cutting edge of Article 22 doctrinal development

---

## VII. SUMMARY: KEY CHANGES FROM V1 TO V2

| Element | V1 | V2 |
|---------|----|----|
| **Thesis** | Implied: "Consultation filtering likely violates Art. 22" | Explicit: "Paradigm case exposing gaps that should be resolved in favor of protection" |
| **Comparative context** | Absent | Present: situates case in administrative AI landscape |
| **"Similarly significant effects"** | Argued but under-developed | Developed with access-to-opportunity framework; acknowledged as novel argument |
| **"About whom" problem** | Touched in profiling section | Fully developed subsection |
| **Procedural vs. substantive** | Assumed filtering is "decision" | Engages counterargument; develops functional test |
| **Counterarguments** | Partially addressed | Systematically engaged |
| **Original contribution** | Implicit | Explicit: arguing for recognition of democratic participation effects |
| **Tone** | Confident doctrinal analysis | Intellectually honest about uncertainty while making normative case |

---

*Document created: 2025-11-22*
*Status: V2 Plan for review before implementation*
