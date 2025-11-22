## Compliance with EU consumer protection laws

The practice of offering AI services under pricing structures that reference undefined usage limits – claims of "5x more usage" where the baseline remains unpublished, or subscriptions providing "extended access" without quantification – implicates multiple overlapping EU consumer protection instruments. These instruments operate independently; a practice may violate one, several, or all simultaneously. The analysis that follows examines each in turn.

### The transparency requirement under the Unfair Contract Terms Directive

Directive 93/13/EEC on unfair terms in consumer contracts imposes two distinct but related transparency obligations.[^1] Article 5 mandates that "in the case of contracts where all or certain terms offered to the consumer are in writing, these terms must always be drafted in plain, intelligible language."[^2] Article 4(2) provides that assessment of unfairness shall not relate to the definition of the main subject matter or the adequacy of price "in so far as these terms are in plain intelligible language."[^3]

[^1]: Council Directive 93/13/EEC of 5 April 1993 on unfair terms in consumer contracts [1993] OJ L95/29.

[^2]: ibid art 5.

[^3]: ibid art 4(2).

The Court of Justice has developed a substantial body of jurisprudence interpreting what "plain intelligible language" requires. The formulation that has become canonical appears in *Kásler*: the transparency requirement "cannot be reduced merely to [terms] being formally and grammatically intelligible."[^4] Rather, "the requirement of transparency ... must be understood as requiring also that the contract set out transparently the specific functioning of the mechanism to which the relevant term refers ... so that the consumer is in a position to evaluate, on the basis of clear, intelligible criteria, the economic consequences for him which derive from it."[^5]

[^4]: Case C-26/13 Kásler and Káslerné Rábai v OTP Jelzálogbank Zrt EU:C:2014:282, para 71.

[^5]: ibid para 72.

This standard – that consumers must be able to evaluate economic consequences on the basis of clear, intelligible criteria – recurs throughout the Court's case law. In *RWE Vertrieb*, the Court held that "it is of fundamental importance ... whether the contract sets out in transparent fashion the reason for and method of the variation of the charges for the service to be provided, so that the consumer can foresee, on the basis of clear, intelligible criteria, the alterations that may be made to those charges."[^6] In *Invitel*, addressing unilateral fee variation in telecommunications contracts, the Court applied the same formulation: transparency requires that the consumer "is in a position to evaluate, on the basis of clear, intelligible criteria, the amendments ... with regard to the fees connected to the service to be provided."[^7] In *Andriciuc*, concerning foreign currency loan terms, the Court reiterated that transparency requires substantive intelligibility enabling consumers to evaluate economic consequences – and added that the seller or supplier "must provide the consumer with sufficient information to enable the latter to take prudent and well-informed decisions."[^8]

[^6]: Case C-92/11 RWE Vertrieb AG v Verbraucherzentrale Nordrhein-Westfalen eV EU:C:2013:180, para 49.

[^7]: Case C-472/10 Nemzeti Fogyasztóvédelmi Hatóság v Invitel Távközlési Zrt EU:C:2012:242, para 28.

[^8]: Case C-186/16 Andriciuc and Others v Banca Românească SA EU:C:2017:703, paras 50–51.

The Commission's 2019 Guidance on the UCTD synthesises this jurisprudence: "transparency requires more than contract terms being formally and grammatically intelligible and implies that consumers must be able to evaluate the economic consequences of a contract term or contract."[^9] The guidance specifies a two-part test: first, whether the terms "are drafted in plain intelligible language enabling an average consumer ... to estimate such a cost"; and second, whether "the failure to mention in the [contract] the information regarded as being essential with regard to the nature of the goods or services ... play[s] a decisive role in that assessment."[^10]

[^9]: Commission Notice – Guidance on the interpretation and application of Council Directive 93/13/EEC on unfair terms in consumer contracts [2019] OJ C323/4, para 70.

[^10]: ibid.

Applied to AI service pricing, the question is whether terms offering "5x more usage" or "20x higher limits" – where no quantified baseline is provided – satisfy this standard. The answer is straightforward: they do not.

A consumer purchasing a subscription described as providing "5x free tier usage" cannot evaluate the economic consequences of that term because the term references a quantity (free tier usage) that is itself undefined and unpublished. The free tier usage limit is not disclosed on pricing pages, not specified in terms of service, and not communicated to consumers before or after contract conclusion. Anthropic's help documentation, for instance, does not provide numerical limits for the free tier; it states only that "additional usage limits apply" without further specification.[^11] OpenAI's help centre states that "Plus subscriptions may include usage limits such as message caps, especially during high demand. These limits may vary based on system conditions."[^12]

[^11]: Anthropic, 'Subscription plan details' (Help Center, accessed 21 October 2025).

[^12]: OpenAI, 'ChatGPT subscription limits' (Help Center, accessed 21 October 2025).

The mathematical consequence is inescapable. A multiplier applied to an undefined variable produces an undefined result. A consumer cannot "foresee, on the basis of clear, intelligible criteria" what quantity of service a "5x" subscription will provide when "1x" has no determinate value. The consumer cannot evaluate whether the subscription will meet their anticipated usage needs. The consumer cannot compare offerings across providers – if Provider A claims "5x more" and Provider B claims "10x more," but neither defines its baseline, the consumer cannot determine which offers greater usage. The effective price per unit of service cannot be calculated.

This is not a marginal transparency failure remediable by clearer drafting. It is a fundamental indeterminacy in the definition of what the consumer is purchasing.

The *RWE Vertrieb* judgment is directly applicable. There, the Court addressed gas supply contracts with clauses permitting unilateral price variation. The Court held that "the lack of information on the point before the contract is concluded cannot, in principle, be compensated for by the mere fact that consumers will, during the performance of the contract, be informed in good time of a variation of the charges."[^13] The same reasoning applies to usage limits: the fact that a consumer discovers the actual limit only upon exceeding it – when the system throttles or blocks further usage – does not cure the pre-contractual information deficit.

[^13]: RWE Vertrieb (n 6) para 51.

The consequences of non-transparent terms under the UCTD are significant. Article 4(2)'s exemption from unfairness review applies only to core terms drafted in plain intelligible language. The Court confirmed in *Pohotovosť* that even terms relating to price or main subject matter "escape the assessment as to whether they are unfair only in so far as the national court ... should form the view ... that they were drafted ... in plain, intelligible language."[^14] Non-transparent core terms lose the Article 4(2) exemption and become subject to the unfairness assessment under Article 3(1).

[^14]: Case C-76/10 Pohotovosť s.r.o. v Iveta Korčkovská EU:C:2010:685, para 71.

Usage limit terms in AI service contracts constitute either part of the price structure (determining effective cost per unit of service) or part of the main subject matter (defining the scope of service provided). Under either characterisation, they would normally fall within Article 4(2)'s exclusion from unfairness review. Because they fail the transparency requirement, they do not.

The Court's judgment in *Pereničová* confirms the analytical consequences: "failure to indicate essential terms of the agreement can be decisive in [the transparency] assessment."[^15] Usage limits that determine service availability and additional charges constitute essential terms. Their omission is not a peripheral drafting deficiency but a decisive failure.

[^15]: Case C-453/10 Pereničová and Perenič v SOS financ spol. s r.o. EU:C:2012:144, para 41.

The Grand Chamber's judgment in *Gutiérrez Naranjo* establishes the remedial implications of non-transparent terms.[^16] Where terms fail the transparency requirement and are declared unfair, invalidity operates *ex tunc* – retroactively from the moment of contract conclusion. The consumer is entitled to restitution of all amounts paid under the unfair term. The Court emphasised that temporal limitation of nullity effects would be incompatible with the Directive: "The protection that the Directive grants to consumers extends to cases in which a consumer who has concluded with a seller or supplier a contract containing an unfair term has failed to raise the unfair nature of the term."[^17] National courts cannot limit restitution to future payments; consumers who have paid for undefined service scopes may seek return of subscription fees for the entire contract period.

[^16]: Joined Cases C-154/15, C-307/15 and C-308/15 Gutiérrez Naranjo and Others EU:C:2016:980.

[^17]: ibid para 62.

### The unfairness assessment

Once the Article 4(2) exemption is lost, the term must be assessed under the general unfairness test in Article 3(1): a term is unfair if "contrary to the requirement of good faith, it causes a significant imbalance in the parties' rights and obligations arising under the contract, to the detriment of the consumer."[^18]

[^18]: UCTD (n 1) art 3(1).

The Court's guidance on good faith appears in *Aziz*: the good faith requirement "requires the seller or supplier to deal fairly and equitably with the consumer whose legitimate interests he has to take into account," asking "whether the seller or supplier, dealing fairly and equitably with the consumer, could reasonably assume that the consumer would have agreed to such a term in individual contract negotiations."[^19]

[^19]: Case C-415/11 Aziz v Caixa d'Estalvis de Catalunya EU:C:2013:164, para 69.

It is difficult to conceive that a consumer, negotiating individually, would agree to pay a fixed monthly fee for an undefined quantity of service. The asymmetry is stark: the trader knows or can determine actual usage limits; the consumer cannot. The trader drafted the terms; the consumer had no opportunity to negotiate them. The trader retains discretion to interpret – and modify – vague promises; the consumer is bound to pay regardless of what those promises turn out to mean.

On significant imbalance, *Aziz* directs comparison with "the legal situation that would prevail in the absence of the contract term at issue."[^20] The question is whether the contract places the consumer in a less favourable position than applicable law would otherwise provide.

[^20]: ibid para 68.

Undefined usage terms create multiple imbalances. First, they prevent the consumer from ascertaining when non-conformity has occurred. If the contract does not specify what quantity the trader must provide, the consumer cannot determine whether the quantity actually provided falls short. Second, they shift the interpretive burden to the consumer: where the contract is ambiguous about the trader's obligations, the consumer must prove what those obligations should have been. Third, they enable the trader to determine unilaterally the scope of its own obligations by leaving them unspecified at contract conclusion and interpreting them during performance. Fourth, they obstruct remedy access: under Directive 2019/770, consumers may seek remedies for lack of conformity – but establishing lack of conformity requires a baseline of what conformity would entail.[^21]

[^21]: Directive (EU) 2019/770 of the European Parliament and of the Council of 20 May 2019 on certain aspects concerning contracts for the supply of digital content and digital services [2019] OJ L136/1, art 14.

The Annex to the UCTD provides an indicative list of terms that may be regarded as unfair. Point 1(i) identifies terms "irrevocably binding the consumer to terms with which he had no real opportunity of becoming acquainted before the conclusion of the contract."[^22] Undefined usage limits satisfy this criterion: even reading the contract in full, the consumer cannot become acquainted with the actual limits. Point 1(j) identifies terms "enabling the seller or supplier to alter the terms of the contract unilaterally without a valid reason which is specified in the contract."[^23] OpenAI's statement that it "dynamically adjust[s] usage caps as we learn more about demand and system performance" constitutes precisely such a unilateral alteration power without pre-specified valid reasons.[^24] Point 1(l) identifies terms "providing for the price of goods to be determined at the time of delivery" without corresponding consumer rights.[^25] Where usage limits – which determine effective per-unit price – are determined at time of use rather than at contract conclusion, the same concern arises.

[^22]: UCTD (n 1) annex, point 1(i).

[^23]: ibid point 1(j).

[^24]: OpenAI (n 12).

[^25]: UCTD (n 1) annex, point 1(l).

### Misleading practices under the Unfair Commercial Practices Directive

Directive 2005/29/EC prohibits unfair commercial practices, including misleading actions and misleading omissions.[^26] Article 6(1)(d) specifically addresses practices that deceive or are likely to deceive consumers regarding "the price or the manner in which the price is calculated, or the existence of a specific price advantage."[^27]

[^26]: Directive 2005/29/EC of the European Parliament and of the Council of 11 May 2005 concerning unfair business-to-consumer commercial practices in the internal market [2005] OJ L149/22.

[^27]: ibid art 6(1)(d).

Claims of "5x more usage" or "20x higher limits" assert a specific price advantage: the consumer receives more for their money than under the free or lower tier. But the claim cannot be verified, substantiated, or even understood without knowing the baseline. It asserts a ratio without disclosing either term of the ratio. This is not merely incomplete information – it is a statement structured to appear informative while conveying no determinate content.

Article 7 addresses misleading omissions. Article 7(1) provides that a commercial practice is misleading if it "omits material information that the average consumer needs, according to the context, to take an informed transactional decision."[^28] Article 7(2) extends this to information provided "in an unclear, unintelligible, ambiguous or untimely manner."[^29] Article 7(4)(c) specifies that for invitations to purchase, material information includes "the price inclusive of taxes, or where the nature of the product means that the price cannot reasonably be calculated in advance, the manner in which the price is calculated."[^30]

[^28]: ibid art 7(1).

[^29]: ibid art 7(2).

[^30]: ibid art 7(4)(c).

Usage limits are material information. They determine whether the service will meet the consumer's anticipated needs. They determine the effective price per unit of usage. They enable comparison shopping. A professional user needing 500 queries daily cannot assess whether a service providing undefined "5x free tier usage" will suffice without knowing what the free tier provides.

The Court's judgment in *Canal Digital* is instructive. There, the Court held that "a commercial practice ... may be regarded as misleading where ... one component of the price is given particular prominence ... whereas another component of that price is completely omitted or presented in a much less conspicuous manner."[^31] AI service pricing pages prominently display monthly subscription costs while omitting or obscuring usage limit information. The effective price – cost per message, per query, per interaction – depends on the usage limit; presenting the nominal price prominently while hiding the usage limit follows the pattern the Court identified as potentially misleading.

[^31]: Case C-611/14 Canal Digital Danmark A/S EU:C:2016:800, para 45.

The January 2025 judgment in *NEW Niederrhein Energie* provides further guidance.[^32] The Court held that where exact amounts cannot be pre-calculated, traders must nonetheless "indicate[] the applicability in principle of such a percentage, together with a possible scale and the components having an impact on that percentage."[^33] Claims of "5x more" without defining 1x, without providing an indicative scale (eg "typically 100–500 queries per day"), and without identifying factors affecting the variable component fall short of this standard.

[^32]: Case C-518/23 Bundesverband der Verbraucherzentralen und Verbraucherverbände – Verbraucherzentrale Bundesverband eV v NEW Niederrhein Energie und Wasser GmbH EU:C:2025:44.

[^33]: ibid para 52.

Directive 2006/114/EC on misleading and comparative advertising provides an additional basis for challenge.[^34] Article 4(c) requires that comparative advertising "objectively compares one or more material, relevant, verifiable and representative features of those goods and services, which may include price."[^35] Claims of "5x more usage" or "20x higher limits" are comparative: they compare the paid tier to the free tier. But the comparison fails the verifiability requirement because the baseline is undefined. Neither consumers nor enforcement authorities can verify the claimed ratio without knowing what "1x" represents. The comparison also fails objectivity: where the baseline varies dynamically or depends on undisclosed factors, different consumers at different times may experience different ratios. This is not objective comparison but empty assertion dressed in numerical form.

[^34]: Directive 2006/114/EC of the European Parliament and of the Council of 12 December 2006 concerning misleading and comparative advertising [2006] OJ L376/21.

[^35]: ibid art 4(c).

Article 12 UCPD enables courts and administrative authorities to "require the trader to furnish evidence as to the accuracy of factual claims in relation to a commercial practice."[^36] A claim that a subscription provides "5x" more usage is a factual claim requiring substantiation. Substantiation would require demonstrating: what quantitative measure constitutes the free tier baseline; that the paid tier actually provides the claimed multiple; and that consumers can actually achieve the claimed usage under normal usage patterns. Given that providers refuse to publish specific free tier limits and describe them as dynamic, substantiation appears impossible. The claim cannot be proven true because the terms in which it is expressed lack determinate referents.

[^36]: UCPD (n 26) art 12.

### Pre-contractual information duties under the Consumer Rights Directive

Directive 2011/83/EU imposes pre-contractual information requirements for distance and off-premises contracts.[^37] Article 6(1)(a) requires disclosure of "the main characteristics of the goods or services, to the extent appropriate to the medium and to the goods or services."[^38] Article 6(1)(e) requires disclosure of "the total price of the goods or services inclusive of taxes" or, where the price cannot reasonably be calculated in advance, "the manner in which the price is to be calculated."[^39]

[^37]: Directive 2011/83/EU of the European Parliament and of the Council of 25 October 2011 on consumer rights [2011] OJ L304/64.

[^38]: ibid art 6(1)(a).

[^39]: ibid art 6(1)(e).

For subscriptions, the provision specifies that "the total price shall include the total costs per billing period" and that "where the total costs cannot be reasonably calculated in advance, the manner in which the price is to be calculated shall be provided."[^40]

[^40]: ibid.

The Commission's Guidance on the CRD interprets "main characteristics" to include "all essential product attributes," specifying for digital content or digital services "examples of main characteristics include its functionality and interoperability."[^41] Usage limits constitute essential attributes: they determine service availability, functionality scope, and effective pricing. The guidance further specifies that functionality information should include "limitations on use whether territorial, time-based or device-based."[^42] Usage limits are such limitations.

[^41]: Commission Notice – Guidance on the interpretation and application of Directive 2011/83/EU [2021] OJ C525/1, para 89.

[^42]: ibid para 108.

Article 6(5) provides that the information referred to in Article 6(1) "shall form an integral part of the distance or off-premises contract and shall not be altered unless the contracting parties expressly agree otherwise."[^43] Vague pre-contractual information thus becomes vague contractual terms. Article 6(9) places the burden of proof regarding compliance with information requirements on the trader.[^44] A trader employing vague language cannot satisfy the burden of proving clear and comprehensible disclosure of main service characteristics.

[^43]: CRD (n 37) art 6(5).

[^44]: ibid art 6(9).

Article 8(2) mandates that for electronic contracts placing consumers under payment obligations, the trader must make the consumer aware "in a clear and prominent manner, and directly before the consumer places his order" of the price and main characteristics.[^45] The Article further provides that "if the trader has not complied with this subparagraph, the consumer shall not be bound by the contract or order."[^46] Burying vague references to usage limits in lengthy terms of service while prominently advertising subscription prices may fail the "clear and prominent manner" requirement.

[^45]: ibid art 8(2).

[^46]: ibid.

### Conformity requirements under the Digital Content Directive

Directive 2019/770 establishes conformity requirements for digital content and digital services.[^47] Article 7 sets out subjective conformity requirements – conformity with the contract – while Article 8 establishes objective conformity requirements.[^48]

[^47]: DCD (n 21).

[^48]: ibid arts 7–8.

Article 7(a) requires that the digital service "be of the description, quantity, quality, and possess the functionality, compatibility, interoperability and other features as required by the contract."[^49] Vague contractual language failing to quantify service parameters undermines this requirement: the contract cannot be said to "require" specific characteristics when language is insufficiently specific to create enforceable obligations.

[^49]: ibid art 7(a).

Article 8(1)(b) requires that the digital service "be of the quantity and possess the qualities and performance features, including in relation to functionality, compatibility, accessibility, continuity and security, normal for digital content or digital services of the same type and which the consumer may reasonably expect."[^50] The reference to "continuity" directly implicates uptime and availability. The reference to "quantity" implicates usage limits. Where traders provide no contractual specification of these parameters, consumers are forced to rely exclusively on what is "normal" for services of the same type – but without published industry norms or trader commitments, determining normality becomes speculative.

[^50]: ibid art 8(1)(b).

Article 19 addresses trader modification of digital services. Article 19(1) permits modification only if: the contract allows it and provides a valid reason; the modification is made without additional cost; the consumer is informed in a clear and comprehensible manner; and, where the modification negatively impacts the consumer's access or use, the consumer is informed reasonably in advance and of their right to terminate.[^51]

[^51]: ibid art 19(1)–(2).

Vague initial service specification undermines Article 19's modification framework. Notification of modification "in a clear and comprehensible manner" presupposes clarity regarding the baseline from which the modification deviates. Where that baseline is undefined, the trader can modify service provision while claiming the modification falls within the original (vague) scope.

Article 19(2) entitles the consumer to terminate "if the modification negatively impacts the consumer's access to or use of the digital content or digital service."[^52] Vague specification of access parameters and usage limitations precludes the consumer from establishing negative impact: if the original entitlement was undefined, any subsequent limitation can be characterised as consistent with it.

[^52]: ibid art 19(2).

### Contra proferentem and burden of proof

Article 5 UCTD provides that "where there is doubt about the meaning of a term, the interpretation most favourable to the consumer shall prevail."[^53] Vague usage specifications necessarily create doubt about meaning.

[^53]: UCTD (n 1) art 5.

The interpretation most favourable to the consumer of a term offering "5x more usage" – where no limit is specified – would be that no limit applies, or that the highest conceivable interpretation governs. The trader bears the consequences of vague drafting. The Commission's Guidance confirms that this rule "aims to offset the informational disadvantage of consumers" and "reflects the underlying rationale that pre-formulated terms are drafted by or on behalf of the seller or supplier, who therefore has to bear the consequences of any ambiguity."[^54]

[^54]: Commission UCTD Guidance (n 9) para 76.

Burden of proof provisions reinforce this allocation of risk. Article 6(9) CRD places the burden of proving compliance with information requirements on the trader.[^55] Article 12(2) of Directive 2019/770 places the burden of proving conformity at the time of supply on the trader for lack of conformity appearing within one year.[^56] Vague service specification disadvantages traders in satisfying these burdens: a trader cannot prove service conformed to vague promises when those promises are insufficiently specific to establish an ascertainable conformity standard.

[^55]: CRD (n 37) art 6(9).

[^56]: DCD (n 21) art 12(2).

### Cumulative effect and enforcement

The violations identified operate independently. Each provides a separate basis for legal challenge; several may apply simultaneously to the same practice.

Non-transparent usage terms violate Article 5 UCTD, rendering them subject to the Article 3(1) unfairness assessment – and likely failing it. The same terms constitute misleading omissions under UCPD Article 7 because they hide material information in ambiguous form. The failure to disclose the manner of price calculation violates CRD Article 6(1)(e). Presenting these terms through interfaces that emphasise nominal prices while obscuring usage limits may engage the UCPD's prohibition on misleading presentation.

Directive 2019/2161 (the "Omnibus Directive") strengthened enforcement, introducing Article 8a to the UCTD requiring Member States to establish penalties that are "effective, proportionate and dissuasive" with maximum fines of "at least 4% of the trader's annual turnover in the Member State or Member States concerned" or EUR 2 million where turnover information is unavailable.[^57]

[^57]: Directive (EU) 2019/2161 of the European Parliament and of the Council of 27 November 2019 as regards the better enforcement and modernisation of Union consumer protection rules [2019] OJ L328/7, art 1.

Consumer protection authorities possess standing under Article 7(2) UCTD to bring actions against continued use of unfair terms. The Court confirmed in *Invitel* that collective proceedings with *erga omnes* effect are permitted: an authority obtaining a finding that a term violates transparency requirements binds the trader for all consumer contracts, not merely identified plaintiffs.[^58]

[^58]: Invitel (n 7) paras 37–42.

National enforcement actions in analogous contexts demonstrate regulatory appetite for addressing vague comparative claims. France's Direction Générale de la Concurrence, de la Consommation et de la Répression des Fraudes sanctioned over one-third of 1,800 businesses inspected in 2024 greenwashing sweeps for "imprecise or ambiguous claims likely to mislead consumers."[^59] The Netherlands' Autoriteit Consument en Markt required H&M and Decathlon to revise marketing practices for "using sustainability-related terms ... without clear definitions or supporting evidence."[^60] The Consumer Protection Cooperation Network's 2023 digital fairness sweep found that 97% of the most popular websites and applications in the EU employed at least one dark pattern, with "hidden information" identified as a common violation type.[^61]

[^59]: Direction Générale de la Concurrence, de la Consommation et de la Répression des Fraudes, 'Bilan 2024 des contrôles sur les allégations environnementales' (4 September 2024).

[^60]: Autoriteit Consument en Markt, 'ACM takes action against H&M and Decathlon for misleading sustainability claims' (press release, 6 July 2022).

[^61]: European Commission, 'Results of 2023 consumer website sweep on dark patterns' (Commission press release, 30 January 2024).

The specific intersection of AI services and usage-based pricing has not yet attracted coordinated EU enforcement action. The Commission's ongoing digital fairness reviews and the Consumer Protection Cooperation Network's attention to dark patterns suggest that coordinated action targeting AI service pricing practices – which exhibit precisely the opacity, vagueness, and information asymmetry that consumer protection frameworks exist to remedy – remains plausible.
