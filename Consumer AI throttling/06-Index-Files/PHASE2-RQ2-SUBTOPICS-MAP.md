# Phase 2: RQ2 Sub-Topics Map
**RQ2 Claim:** "This is a clear violation of EU consumer protection laws"

**Status:** Mapping complete, filling in arguments and evidence in progress

---

## RQ2 Sub-Topics Map

### **Legal Violations Framework**

**1. UCPD Art 6 - Misleading Actions on Price Advantages**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: Claims of "5x more usage" or "higher limits" constitute misleading actions under Article 6(1)(d) UCPD regarding "the price or the manner in which the price is calculated, or the existence of a specific price advantage." When traders claim subscriptions provide "5x" a baseline that is itself undefined and unpublished, consumers cannot evaluate economic consequences. This violates the RWE Vertrieb standard requiring consumers can "foresee, on the basis of clear, intelligible criteria" what they are purchasing. A multiplier applied to an undefined variable produces an undefined result—this is mathematical impossibility, not merely poor transparency.
- Evidence:
  - Article 6(1)(d) UCPD text: practices misleading regarding "the price or the manner in which the price is calculated, or the existence of a specific price advantage"
  - C-611/14 Canal Digital ¶45: "one component of the price is given particular prominence... whereas another component... is completely omitted or presented in a much less conspicuous manner" constitutes misleading action
  - Provider examples: AI services prominently advertise monthly prices (€20, €100, €200) while completely omitting usage limits determining effective per-unit costs
  - Commission UCTD Guidance (2019): consumers must "evaluate the economic consequences" of contract terms
  - Application: When baseline is undefined, "5x" multiplier creates misleading impression of specific, defined service level when boundaries remain undefined and subject to unilateral trader determination

**2. UCPD Art 7 - Misleading Omissions of Material Information**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: Article 7(1) UCPD prohibits omitting "material information that the average consumer needs, according to the context, to take an informed transactional decision." Usage limits constitute material information for three reasons: (1) they determine effective price per unit of service—without knowing limits, consumers cannot calculate cost per message/query; (2) they determine whether service meets consumer's anticipated needs—professional user needing 500 queries daily cannot assess if undefined "5x free tier usage" suffices; (3) they enable comparison shopping—without published limits, consumers cannot compare offerings across providers. Article 7(2) specifies misleading omissions include providing information "in an unclear, unintelligible, ambiguous or untimely manner." Terms stating "limits may vary based on system conditions" (OpenAI) or "additional usage limits apply" (Anthropic) without specification exemplify unclear/ambiguous presentation. Communicating limits only after consumers exceed them constitutes untimely manner—information arrives after transactional decision made.
- Evidence:
  - Article 7(1) UCPD text: prohibits omitting "material information that the average consumer needs"
  - Article 7(2) UCPD: includes information provided "in an unclear, unintelligible, ambiguous or untimely manner"
  - Article 7(4)(c) UCPD: for invitations to purchase, material information includes "the price... or where the nature of the product means that the price cannot reasonably be calculated in advance, the manner in which the price is calculated"
  - C-518/23 NEW Niederrhein ¶52 (2025): even where exact amounts cannot be pre-specified, traders must "indicate[] the applicability in principle" of variable charges "together with a possible scale and the components having an impact"
  - Provider practices documented: OpenAI "limits may vary based on system conditions" (no formula/criteria/ranges), Anthropic "additional usage limits apply" (no further specification)
  - Violation: Claims of "5x more" without defining 1x, providing scale (e.g., "typically 100-500 queries/day"), or identifying determinative factors violates NEW Niederrhein standard

**3. UCPD Art 12 - Substantiation Failure**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: Article 12 UCPD enables courts and administrative authorities to "require the trader to furnish evidence as to the accuracy of factual claims in relation to a commercial practice." Claims that subscriptions provide "5x" or "20x" more usage than free tier constitute factual claims requiring substantiation. Substantiation would require proving: (1) what quantitative measure constitutes free tier baseline; (2) that paid tier actually provides claimed multiple; (3) that consumers can achieve claimed usage under normal patterns. Given providers refuse to publish specific free tier limits and describe them as "dynamic" and varying, substantiation appears impossible. The practice resembles Danish Consumer Ombudsman precedent requiring "'up to' indication may only be used if most (80%) of customers targeted can obtain the speed indicated"—standard undefined multipliers cannot satisfy.
- Evidence:
  - Article 12 UCPD text: authorities can "require the trader to furnish evidence as to the accuracy of factual claims"
  - Commission UCPD Guidance (SWD(2016)163): traders must have "adequate evidence readily available to substantiate the claim" and demonstrate consumers are "likely to achieve the maximum results promised under normal circumstances"
  - Commission UCPD Guidance: "'up to' claims could be misleading if traders are not in a position to substantiate that consumers are likely to achieve the maximum results promised"
  - Danish Consumer Ombudsman precedent: 80% of customers must be able to obtain claimed results
  - Substantiation requirements for "5x more" claims: (a) data on actual free tier usage allowances; (b) data on actual paid tier usage allowances; (c) evidence ratio equals 5x; (d) evidence consumers actually achieve this usage
  - Provider practices: Refuse to publish specific free tier limits, describe as "dynamic" and varying—makes substantiation impossible
  - Problem: Trader can retroactively define baseline to satisfy ratio, reducing substantiation to tautology rather than empirical measurement against pre-specified criteria

**4. UCTD Art 5 - Transparency Requirement Failure**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]], [[NotebookLM CJEU excerpts.md]]
- Main argument: Article 5 UCTD mandates contract terms "must always be drafted in plain, intelligible language." The Kásler judgment (¶71-73) establishes this "cannot be reduced merely to [terms] being formally and grammatically intelligible" but requires "the contract set out transparently the specific functioning of the mechanism" enabling consumers to "evaluate, on the basis of clear, intelligible criteria, the economic consequences." Terms stating "5x your free tier usage" are grammatically intelligible but fail substantive transparency because consumers cannot evaluate economic consequences. The term refers to a baseline ("free tier usage") itself undefined in contract or publicly available materials—creating circular definition: paid tier limit defined by reference to undefined free tier limit. Commission UCTD Guidance requires consumers "must be able to evaluate the economic consequences of a contract term" and "estimate in particular the total cost." When usage limits defined by reference to undefined baselines, estimation is mathematically impossible—multiplying unknown variable by 5 yields unknown result.
- Evidence:
  - Article 5 UCTD text: terms "must always be drafted in plain, intelligible language"
  - C-26/13 Kásler ¶71: transparency requirement "cannot be reduced merely to it being formally and grammatically intelligible"
  - C-26/13 Kásler ¶72: requires "contract set out transparently the specific functioning of the mechanism... so that **the consumer is in a position to evaluate, on the basis of clear, intelligible criteria, the economic consequences for him which derive from it**"
  - C-92/11 RWE Vertrieb ¶50: "mere reference... to a legislative or regulatory act... is not satisfied... It is essential that the consumer is informed... of the content"
  - Analogy: Just as referring to external legal provisions without explaining content fails transparency, referring to "free tier baseline" without defining baseline fails transparency
  - Commission UCTD Guidance (2019, C(2019) 5325): "consumers must be able to evaluate the economic consequences of a contract term" and "must be able to estimate in particular the total cost"
  - UCTD Annex Point 1(i): terms "irrevocably binding the consumer to terms with which he had no real opportunity of becoming acquainted before the conclusion of the contract"
  - Application: Consumer has "no real opportunity of becoming acquainted" with actual usage obligations before contract conclusion when limits defined by undefined baselines

**5. UCTD Art 3 - Unfairness Test (Core Terms Lose Exemption)**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: The Pohotovosť judgment (¶71) establishes that even core terms relating to price and main subject matter "escape the assessment as to whether they are unfair only in so far as the national court having jurisdiction should form the view... that they were drafted by the seller or supplier in plain, intelligible language." Non-transparent core terms lose Article 4(2) exemption and become subject to Article 3(1) unfairness assessment. Usage limits constitute either: (1) part of price structure (determining effective cost per unit); or (2) part of main subject matter (defining scope of service provided). Under either characterization, they would normally fall within Article 4(2) exemption. However, because these terms fail "plain intelligible language" requirement, exemption does not apply. National courts must assess whether undefined usage limit terms "cause[] a significant imbalance in the parties' rights and obligations... to the detriment of the consumer" contrary to "good faith." Such terms likely satisfy unfairness test because they: (1) create information asymmetry—trader knows/can determine actual limits while consumer cannot; (2) confer unilateral definition power on trader; (3) prevent informed consent; (4) are "contrary to good faith" because they undermine reasonable consumer expectations who interpret "5x" as specific quantified enhancement rather than empty comparative.
- Evidence:
  - Article 3(1) UCTD text: "A contractual term which has not been individually negotiated shall be regarded as unfair if, contrary to the requirement of good faith, it causes a significant imbalance in the parties' rights and obligations arising under the contract, to the detriment of the consumer"
  - Article 4(2) UCTD: exemption for core terms relating to "definition of the main subject matter of the contract" and "adequacy of the price and remuneration... **in so far as these terms are in plain intelligible language**" [emphasis added]
  - C-76/10 Pohotovosť ¶71: "Even if such a term may be assessed as falling within the scope of the exclusion referred to in that article [Article 4(2)]... the terms referred to in Article 4(2)... **escape the assessment as to whether they are unfair only in so far as the national court having jurisdiction should form the view, following a case-by-case examination, that they were drafted by the seller or supplier in plain, intelligible language**"
  - Consequence: Non-transparent core terms lose exemption, become subject to unfairness review
  - Four reasons satisfy unfairness test: (a) Information asymmetry favoring trader; (b) Unilateral definition power reserved to trader; (c) Informed consent impossible; (d) Contrary to good faith—undermines reasonable expectations
  - Recital 16 UCTD: unfairness assessment involves "taking into account the strength of the bargaining positions of the parties, whether the consumer had an inducement to agree to the term"
  - Good faith requirement: seller/supplier must "deal[] fairly and equitably with the other party whose legitimate interests he has to take into account"

**6. UCTD Annex - Presumptively Unfair Terms**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**7. CRD Art 6 - Pre-Contractual Information Duties**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**8. CRD Art 8 - Plain Intelligible Language**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**9. Comparative Advertising Directive Art 4(c) - Non-Verifiable Comparisons**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**10. DSA Art 14 & 25 - Terms Transparency & Dark Patterns**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**11. AI Act Art 13 - Performance Limitations Disclosure**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

### **CJEU Case Law Standards**

**12. C-92/11 RWE Vertrieb - Foreseeability Standard**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[NotebookLM CJEU excerpts.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**13. C-26/13 Kásler - Substantive Transparency (Economic Consequences)**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[NotebookLM CJEU excerpts.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**14. C-472/10 Invitel - Unilateral Variation Transparency**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[NotebookLM CJEU excerpts.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**15. C-76/10 Pohotovosť - Core Terms Lose Exemption if Non-Transparent**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**16. C-611/14 Canal Digital - Misleading Price Presentation**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**17. C-518/23 NEW Niederrhein (2025) - Variable Components Need Scales**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**18. C-472/23 Lexitor (2025) - Fee Variation Transparency**
- Found in: [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**19. C-39/24 Caixabank (2025) - Fee Must Specify Counter-Performance**
- Found in: [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**20. C-453/10 Pereničová - Failure to Indicate Essential Terms**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**21. Joined Cases C-154/15, C-307/15, C-308/15 Gutiérrez Naranjo - Comprehensibility of Actual Significance**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

### **Unique AI Service Arguments**

**22. Mathematical Impossibility Argument (Three Scenarios)**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**23. Cumulative Violations Framework (Cascading Liability)**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**24. Good Faith Violation (Information Asymmetry Exploitation)**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**25. Four Specific Problems with "5x Undefined Baseline"**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

### **Enforcement Evidence**

**26. German Verbraucherzentralen vs Streaming Services (2022-2025)**
- Found in: [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**27. German Post-RWE Energy Contract Invalidation (~40M Contracts)**
- Found in: [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**28. German Bundeskartellamt Facebook Decision (2019)**
- Found in: [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**29. French DGCCRF Greenwashing Enforcement (2024)**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**30. French DGCCRF Facebook Enforcement (2014-2016)**
- Found in: [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**31. Dutch ACM H&M/Decathlon Actions**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**32. EU Commission Digital Fairness Fitness Check (2024)**
- Found in: [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**33. EU Commission DSA Enforcement (X, TikTok, AliExpress)**
- Found in: [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**34. CPC Network Sweeps (2018, 2023)**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

### **Remedies & Consequences**

**35. Terms Non-Binding (UCTD Art 6)**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**36. Penalties & Fines Framework**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[EU-Enforcement-Actions-Step3.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

**37. Consumer Restitution Rights**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

---

**Total: 37 Sub-Topics Identified**
**Status: Arguments and evidence being filled in progressively**
