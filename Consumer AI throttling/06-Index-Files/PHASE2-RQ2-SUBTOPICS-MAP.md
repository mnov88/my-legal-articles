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
- Main argument: The Annex to UCTD provides an indicative list of presumptively unfair terms. AI service pricing practices trigger three specific Annex provisions: Point 1(i) identifies as unfair terms "irrevocably binding the consumer to terms with which he had no real opportunity of becoming acquainted before the conclusion of the contract"—terms defining usage limits by reference to undefined baselines bind consumers to obligations they cannot know pre-contractually. Point 1(j) identifies as unfair terms "enabling the seller or supplier to alter the terms of the contract unilaterally without a valid reason which is specified in the contract"—OpenAI's "dynamically adjusting usage caps" and statements that "limits may vary based on system conditions" constitute unilateral alteration power without pre-specified criteria. Point 1(l) identifies as unfair terms "providing for the price of goods to be determined at the time of delivery" without corresponding consumer rights—usage limits determined dynamically or "at time of use" without advance specification create similar unfairness where effective price per unit is "determined at time of delivery" when trader unilaterally sets or modifies limits.
- Evidence:
  - UCTD Annex Point 1(i): "irrevocably binding the consumer to terms with which he had no real opportunity of becoming acquainted before the conclusion of the contract"
  - C-453/10 Pereničová ¶41: "failure to indicate essential terms of the agreement can be decisive in [the transparency] assessment"
  - Application to Point 1(i): Even if trader internally knows actual limits, when not disclosed to consumers pre-contractually, consumers have "no real opportunity of becoming acquainted"
  - UCTD Annex Point 1(j): "enabling the seller or supplier to alter the terms of the contract unilaterally without a valid reason which is specified in the contract"
  - OpenAI statements: "currently dynamically adjusting usage caps" and "these limits may vary based on system conditions"
  - C-472/10 Invitel ¶28: variation mechanisms must be set out transparently so consumers can evaluate amendments based on clear, intelligible criteria
  - C-92/11 RWE Vertrieb ¶51: post-contractual notification cannot cure pre-contractual information deficits
  - UCTD Annex Point 1(l): "providing for the price of goods to be determined at the time of delivery" without corresponding consumer rights
  - Parallel: Usage limits determined dynamically without advance specification means effective price per unit is "determined at time of delivery"

**7. CRD Art 6 - Pre-Contractual Information Duties**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: Article 6(1)(e) CRD mandates disclosure of "the total price" or, where this cannot be reasonably calculated in advance, "the manner in which the price is to be calculated." For subscription services, the provision specifies "the total price shall include the total costs per billing period" and "where the total costs cannot be reasonably calculated in advance, the manner in which the price is to be calculated shall be provided." AI service subscriptions typically charge fixed monthly fees (€20, €100, €200), making nominal price calculable. However, economic substance involves purchasing usage up to specified limits, with potential additional charges, service degradation (throttling), or termination upon exceeding limits. Effective price per unit cannot be calculated without knowing usage limits. When providers claim "5x more usage" without defining baseline, they fail to provide either: (1) total price (because quantity purchased is undefined); or (2) manner of price calculation (because formula for determining limits is undisclosed). Usage limits triggering additional charges or service modifications are part of pricing structure that must be disclosed. Recital 19 CRD provision that traders should inform about "functionality and relevant interoperability" including "absence or presence of any technical restrictions" supports interpretation that usage limits are technical restrictions affecting functionality requiring pre-contractual disclosure.
- Evidence:
  - Article 6(1)(e) CRD text: requires "the total price... or where the nature of the goods or services is such that the price cannot reasonably be calculated in advance, the manner in which the price is to be calculated"
  - Article 6(1)(e) CRD for subscriptions: "the total price shall include the total costs per billing period. Where such contracts are charged at a fixed rate, the total price shall also mean the total monthly costs. **Where the total costs cannot be reasonably calculated in advance, the manner in which the price is to be calculated shall be provided**"
  - Commission Guidance on CRD: for contracts of indeterminate duration or subscriptions, traders must provide "total costs per billing period" or, if costs cannot be calculated, "the manner in which the price is to be calculated"
  - Recital 19 CRD: traders should inform consumers about "the functionality and the relevant interoperability of digital content" including "the absence or presence of any technical restrictions"
  - Application: Usage limits are technical restrictions affecting functionality that must be disclosed pre-contractually
  - Economic substance: Consumer purchases usage up to limits, not just monthly access—effective price per unit depends on limits
  - Violation: Claims of "5x more" without baseline definition fail to provide either total price (undefined quantity) or manner of calculation (undisclosed formula)

**8. CRD Art 8 - Plain Intelligible Language**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: Article 8(1) CRD requires information be provided "in plain and intelligible language." Article 8(2) requires that for electronic contracts placing consumers under payment obligations, information must be presented "in a clear and prominent manner, and directly before the consumer places his order." Burying vague references to usage limits in lengthy terms of service while prominently advertising subscription prices violates the "clear and prominent manner" requirement. The Canal Digital principle that emphasizing some price components while hiding others is misleading applies equally under CRD. The requirement that information be provided "directly before the consumer places his order" means usage limit information must be accessible at point of purchase, not buried in linked documents or communicated only after subscription. The "plain and intelligible language" standard incorporates substantive transparency requirements established by CJEU jurisprudence—information must enable consumers to understand economic consequences, not merely be grammatically comprehensible.
- Evidence:
  - Article 8(1) CRD text: information must be provided "in a way appropriate to the means of distance communication used in plain and intelligible language"
  - Article 8(2) CRD: for electronic contracts placing consumers under payment obligations, traders must make consumers aware "in a clear and prominent manner, and directly before the consumer places his order" of specified information including price
  - C-611/14 Canal Digital ¶45-46: emphasizing some price components while hiding others constitutes misleading practice—principle applies to CRD information requirements
  - Application: Prominently displaying subscription prices while burying vague usage limit references in terms of service violates "clear and prominent manner" requirement
  - "Directly before the consumer places his order": usage limit information must be accessible at point of purchase, not only in post-purchase communications
  - Plain intelligible language standard: incorporates CJEU substantive transparency jurisprudence (Kásler, RWE Vertrieb)—must enable understanding of economic consequences
  - Violation: Undefined baseline claims cannot satisfy plain intelligible language standard because consumers cannot understand what they are purchasing

**9. Comparative Advertising Directive Art 4(c) - Non-Verifiable Comparisons**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: Directive 2006/114/EC Article 4(c) requires comparative advertising "objectively compares one or more material, relevant, **verifiable and representative** features of those goods and services, which may include price." The verifiability requirement is central—comparison claiming "5x more" cannot be verified without: (1) specification of what is being measured; (2) specification of baseline quantity; (3) specification of comparison quantity; (4) methodology for measurement; (5) evidence supporting claimed ratio. Claims of "5x your free tier usage" or "20x higher usage limits" fail verifiability because baseline is undefined. Even if trader internally calculates a ratio, consumers and enforcement authorities cannot verify claim without knowing what "1x" represents. This differs from verifiable comparative claims such as "5x faster processing speed" (speed measurable against specified benchmarks) or "contains 5x more vitamin C than product X" (content chemically analyzable against specified comparator). Comparison is also not "objective"—when baseline varies dynamically, is determined by unspecified "system conditions," or remains entirely unpublished, comparison lacks objectivity because different consumers at different times may experience different ratios, and no consumer can determine whether they received claimed multiple.
- Evidence:
  - Directive 2006/114/EC Article 4(c) text: comparative advertising must "objectively compares one or more material, relevant, **verifiable and representative** features... which may include price"
  - Verifiability requirements: comparison must specify (a) what is measured; (b) baseline quantity; (c) comparison quantity; (d) measurement methodology; (e) supporting evidence
  - Failure of "5x more" claims: baseline undefined, making verification mathematically impossible
  - Contrast with verifiable claims: "5x faster processing" (measurable benchmarks), "5x more vitamin C than X" (chemical analysis against comparator)
  - Objectivity requirement failure: when baseline varies dynamically or depends on "system conditions," comparison lacks objective criteria
  - Consequence: Different consumers at different times may experience different ratios—no consumer can determine if received claimed multiple
  - Enforcement implication: Even if trader has internal ratio calculations, verification requires baseline disclosure to consumers and authorities

**10. DSA Art 14 & 25 - Terms Transparency & Dark Patterns**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[EU-Enforcement-Actions-Step3.md]]
- Main argument: Article 14(1) DSA requires providers "include information on any restrictions that they impose in relation to the use of their service" in terms and conditions, which must be "set out in clear, plain, intelligible, user-friendly and unambiguous language." Usage limits constitute restrictions on service use requiring clear specification. Terms stating "additional usage limits apply" (Anthropic) or "limits may vary based on system conditions" (OpenAI) without further specification fail the "clear, plain, intelligible, user-friendly and unambiguous language" standard. The "user-friendly" language requirement suggests consumer-oriented presentation, not merely legal compliance—average consumers must understand and apply restrictions to their usage patterns. Article 25(1) DSA prohibits designing, organizing or operating online interfaces "in a way that deceives or manipulates... or otherwise materially distorts or impairs the ability... to make free and informed decisions." Recital 67 specifies this includes "giving more prominence to certain choices" and "making certain choices more difficult or time-consuming." Pricing pages prominently displaying monthly costs while omitting/minimizing usage limit information constitute "giving more prominence" that distorts decision-making. Burying vague usage limit references in lengthy terms accessed through small-print links while subscription button is prominent constitutes making "certain choices more difficult" (accessing limit information) while facilitating others (subscribing without full information).
- Evidence:
  - DSA Article 14(1) text: providers must "include information on any restrictions that they impose in relation to the use of their service" in terms that "shall be set out in clear, plain, intelligible, user-friendly and unambiguous language"
  - Usage limits = restrictions on service use requiring clear specification
  - "User-friendly" language: consumer-oriented presentation standard—average consumers must be able to understand and apply restrictions
  - Article 14(1) algorithmic disclosure: "policies, procedures, measures and tools used for the purpose of content moderation, including algorithmic decision-making"—extends to algorithmic rate-limiting enforcement
  - DSA Article 25(1) text: prohibits online interfaces that "deceive or manipulate... or otherwise materially distort or impair the ability... to make free and informed decisions"
  - Recital 67 DSA: includes "giving more prominence to certain choices through visual, auditory, or other components... making certain choices more difficult or time-consuming... and deceiving the recipients of the service"
  - Dark pattern identified: Pricing pages prominently display monthly costs (large, bold, highlighted) while omitting/minimizing usage limits
  - Dark pattern identified: Vague limit references buried in lengthy terms accessed via small-print links, while subscription purchase button prominent/accessible
  - Commission 2023 CPC Network sweep: 97% of popular websites/apps in EU employed at least one dark pattern
  - Commission behavioral studies: "interfaces designed to manipulate purchases" through "hidden information" constitute common dark pattern violations

**11. AI Act Art 13 - Performance Limitations Disclosure**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: [PLACEHOLDER]
- Evidence: [PLACEHOLDER]

### **CJEU Case Law Standards**

**12. C-92/11 RWE Vertrieb - Foreseeability Standard**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[NotebookLM CJEU excerpts.md]], [[Doctrinal analysis Perplexity.md]], [[Case C-92-11 RWE Vertrieb (primary source)]]
- Main argument: The RWE Vertrieb judgment establishes the foundational "foreseeability standard" for price variation clauses and contract terms affecting economic consequences. Paragraph 49 holds that "it is of fundamental importance... whether the contract sets out in transparent fashion the reason for and method of the variation of the charges for the service to be provided, so that **the consumer can foresee, on the basis of clear, intelligible criteria, the alterations that may be made to those charges**." This foreseeability requirement has two components: (1) substantive foreseeability—consumers must be able to predict economic consequences; (2) transparency of mechanism—the formula/method for calculating variations must be disclosed. Paragraph 50 establishes that "mere reference... to a legislative or regulatory act... is not satisfied... It is essential that the consumer is informed... of the content" of the provisions. Paragraph 51 clarifies that "the lack of information on the point before the contract is concluded cannot, in principle, be compensated for by the mere fact that consumers will, during the performance of the contract, be informed in good time of a variation." Applied to AI services: when providers claim "5x more usage" without defining the baseline, consumers cannot foresee economic consequences based on clear criteria—the multiplier is applied to an undefined variable, making foreseeability mathematically impossible. Post-contractual notification when limits are exceeded cannot cure pre-contractual information deficit.
- Evidence:
  - C-92/11 RWE Vertrieb ¶49 (full text): "it is of fundamental importance... whether the contract sets out in transparent fashion the reason for and method of the variation of the charges for the service to be provided, so that **the consumer can foresee, on the basis of clear, intelligible criteria, the alterations that may be made to those charges**"
  - C-92/11 RWE Vertrieb ¶50: "that obligation to make the consumer aware of the reason for and method of the variation of those charges... is not satisfied by the mere reference... to a legislative or regulatory act... It is essential that the consumer is informed... of the content of the provisions concerned"
  - C-92/11 RWE Vertrieb ¶51: "the lack of information on the point before the contract is concluded cannot, in principle, be compensated for by the mere fact that consumers will, during the performance of the contract, be informed in good time of a variation of the charges and of their right to terminate the contract"
  - Two-component test: (1) transparent reason for variation; (2) transparent method of variation
  - "Clear, intelligible criteria" standard—consumers must be able to forecast
  - Prohibition on post-contractual cure of pre-contractual information deficits
  - Application to AI services: "5x more usage" provides neither transparent reason (why baseline undefined?) nor transparent method (how is baseline calculated?)—foreseeability impossible when multiplying undefined variable
  - Mathematical parallel: Attempting to foresee "5x" of unknown baseline = attempting to calculate value of undefined expression

**13. C-26/13 Kásler - Substantive Transparency (Economic Consequences)**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[NotebookLM CJEU excerpts.md]], [[Doctrinal analysis Perplexity.md]]
- Main argument: The Kásler judgment establishes that the "plain intelligible language" requirement under UCTD Article 5 encompasses substantive, not merely formal, transparency. Paragraph 71 holds that "the requirement that a term must be drafted in plain intelligible language... cannot be reduced merely to it being formally and grammatically intelligible." Paragraph 72 specifies the substantive standard: "the requirement of transparency... must be understood as requiring also that the contract set out transparently the specific functioning of the mechanism [of conversion] to which the relevant term refers and the relationship between that mechanism and that prescribed by other terms, so that **the consumer is in a position to evaluate, on the basis of clear, intelligible criteria, the economic consequences for him which derive from it**." This establishes that transparency is tested by whether consumers can evaluate economic consequences, not just whether words are comprehensible. The "specific functioning of the mechanism" must be explained—mathematical formulas, calculation methods, and determinative factors must be disclosed. Applied to AI services: terms stating "5x your free tier usage" are grammatically intelligible but fail substantive transparency because: (1) they reference a baseline ("free tier usage") that is itself undefined; (2) consumers cannot evaluate economic consequences of purchasing 5x an unknown quantity; (3) the "specific functioning of the mechanism" (how baseline is determined) is not disclosed; (4) evaluating economic consequences requires knowing what quantity is being purchased—mathematically impossible when multiplying undefined variable by 5.
- Evidence:
  - C-26/13 Kásler ¶71 (full text): "the requirement that a term must be drafted in plain intelligible language... cannot be reduced merely to it being formally and grammatically intelligible"
  - C-26/13 Kásler ¶72 (full text): "the requirement of transparency... must be understood as requiring also that the contract set out transparently the specific functioning of the mechanism... so that **the consumer is in a position to evaluate, on the basis of clear, intelligible criteria, the economic consequences for him which derive from it**"
  - Distinction: formal transparency (grammatical intelligibility) vs. substantive transparency (ability to evaluate economic consequences)
  - "Specific functioning of the mechanism" requirement: contract must explain how calculations/determinations are made
  - Economic consequences evaluation test: can average consumer determine what they are getting and what it costs?
  - Commission UCTD Guidance (2019) interpretation: "transparency requires more than contract terms being formally and grammatically intelligible and implies that consumers must be able to evaluate the economic consequences of a contract term"
  - Application to AI services: "5x free tier usage" = grammatically clear but economically opaque—references undefined baseline creating circular definition
  - Evaluation impossibility: Consumer cannot evaluate economic consequences of "5x × (undefined quantity)" = undefined result

**14. C-472/10 Invitel - Unilateral Variation Transparency**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]], [[NotebookLM CJEU excerpts.md]], [[Doctrinal analysis Perplexity.md]], [[Case C-472-10 Invitel (primary source)]]
- Main argument: The Invitel judgment applies RWE Vertrieb's transparency principles to telecommunications services with unilateral variation clauses, establishing that variation mechanisms must enable consumers to foresee amendments based on clear, intelligible criteria. Paragraph 28 holds: "the requirement of transparency of contractual terms laid down in Article 5 of Directive 93/13 cannot be reduced merely to the terms concerned being formally and grammatically intelligible, but... requires that the contract sets out transparently the specific functioning of the mechanism [for price variation] to which the relevant term refers... so that **the consumer is in a position to evaluate, on the basis of clear, intelligible criteria, the amendments, by a seller or supplier, of the GBC with regard to the fees connected to the service to be provided**." Paragraph 24 establishes that "the reason for and the method of the variation of the aforementioned price must, in particular, be set out, the consumer having the right to terminate the contract." Applied to AI services: OpenAI's statements that it "dynamically adjust[s] usage caps" and that "limits may vary based on system conditions" without specifying criteria, methodology, or determinative factors constitute exactly the type of non-transparent unilateral variation mechanism Invitel condemns. Consumers cannot evaluate amendments to usage limits when: (1) no baseline is defined; (2) variation mechanism not disclosed; (3) "system conditions" not specified; (4) dynamic adjustment methodology opaque.
- Evidence:
  - C-472/10 Invitel ¶28 (full text): "the requirement of transparency... cannot be reduced merely to the terms concerned being formally and grammatically intelligible, but... requires that the contract sets out transparently the specific functioning of the mechanism... so that **the consumer is in a position to evaluate, on the basis of clear, intelligible criteria, the amendments... of the GBC with regard to the fees connected to the service**"
  - C-472/10 Invitel ¶24: "the reason for and the method of the variation of the aforementioned price must, in particular, be set out, the consumer having the right to terminate the contract"
  - Invitel ¶25: annex to UCTD contains "only an indicative and non-exhaustive list" of unfair terms—not limited to enumerated examples
  - Context: Telecommunications provider attempted to introduce "money order fees" post-contractually without specifying calculation method
  - Holding: Unilateral variation without transparent mechanism = unfair
  - Application to AI dynamic limits: OpenAI "dynamically adjusting usage caps" = unilateral variation; "limits may vary based on system conditions" = no disclosed mechanism; failure to specify what "system conditions" means or how they affect limits = non-transparent functioning
  - Anthropic August 2025 retroactive limits: Imposed "new weekly rate limits" on existing paying customers without prior disclosure = paradigmatic unilateral variation condemned by Invitel
  - Termination right insufficiency: Even if consumers can terminate, Invitel requires transparent mechanism disclosure pre-contractually—cannot cure opacity with exit rights alone

**15. C-76/10 Pohotovosť - Core Terms Lose Exemption if Non-Transparent**
- Found in: [[EU consumer protection law and vague AI service pricing - Claude.md]]
- Main argument: The Pohotovosť judgment establishes that even core contractual terms relating to price and main subject matter lose their Article 4(2) UCTD exemption from unfairness review when they fail the "plain intelligible language" requirement. Paragraph 71 holds: "Even if such a term may be assessed as falling within the scope of the exclusion referred to in that article [Article 4(2)], it should be observed that the terms referred to in Article 4(2) of that directive, while they come within the area covered by Directive 93/13, **escape the assessment as to whether they are unfair only in so far as the national court having jurisdiction should form the view, following a case-by-case examination, that they were drafted by the seller or supplier in plain, intelligible language**." This means: (1) Article 4(2) exempts "definition of main subject matter" and "adequacy of price" from unfairness review; (2) BUT exemption only applies if terms are in "plain intelligible language"; (3) non-transparent core terms become subject to Article 3(1) unfairness assessment. Applied to AI services: usage limits constitute either price (determining effective cost per unit) or main subject matter (defining scope of service). Normally Article 4(2) would exempt them from unfairness review. However, because "5x undefined baseline" terms fail plain intelligible language requirement (per Kásler substantive transparency standard), the exemption does not apply. National courts must assess whether such terms cause "significant imbalance" contrary to "good faith"—which undefined limits likely do through information asymmetry, unilateral definition power, and impossibility of informed consent.
- Evidence:
  - C-76/10 Pohotovosť ¶71 (full text): "Even if such a term may be assessed as falling within the scope of the exclusion referred to in that article [Article 4(2)]... the terms referred to in Article 4(2)... **escape the assessment as to whether they are unfair only in so far as the national court having jurisdiction should form the view, following a case-by-case examination, that they were drafted by the seller or supplier in plain, intelligible language**"
  - Article 4(2) UCTD text: "Assessment of the unfair nature of the terms shall relate neither to the definition of the main subject matter of the contract nor to the adequacy of the price and remuneration... **in so far as these terms are in plain intelligible language**" [emphasis added]
  - Two-step analysis: (1) Is term core (price/subject matter)? (2) Is it in plain intelligible language? Only if both = yes does exemption apply
  - Consequence of transparency failure: Core term loses exemption, becomes subject to Article 3(1) unfairness test
  - Article 3(1) UCTD unfairness criteria: "contrary to requirement of good faith" + "causes significant imbalance" + "to detriment of consumer"
  - Application to usage limits: Either price component (cost per unit) OR subject matter (service scope)—qualifies as core term
  - Transparency failure: "5x undefined baseline" fails Kásler substantive transparency—not in "plain intelligible language"
  - Result: Exemption inapplicable, unfairness assessment triggered
  - Likely unfairness: Information asymmetry (trader knows, consumer doesn't), unilateral definition power, no informed consent possible, contrary to good faith (exploits weak consumer position)

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
