## The inadequacy of alternative pricing models

The legal deficiencies identified in tiered subscription pricing for AI services  — vague capacity commitments, unilateral modification rights, and inadequate pre-contractual disclosure  —  invite an obvious remedial question: would consumers fare better under alternative pricing structures? If opacity is the problem, then transparent, metered billing would appear to be the solution. If unpredictable throttling violates reasonable expectations, then pay-per-use models that charge for precisely what is consumed would seem to eliminate the source of unfairness.

This intuition, however, does not survive scrutiny. The alternative pricing models available to AI service providers  —  token-based pricing, credit-based pricing, flat-rate unlimited subscriptions, and hybrid arrangements  —  each introduce distinct consumer protection problems that are, in many respects, more severe than those created by the current regime. The choice facing consumers and regulators is not between a defective model and sound alternatives, but between different configurations of risk, opacity, and potential harm.

### Measured pricing: tokens, credits, and the consumer-risk transfer

The most frequently proposed alternative to subscription-based AI pricing is measured consumption billing. In its purest form, measured pricing charges consumers for the precise computational resources consumed  —  typically denominated in tokens, which represent the fundamental units of text processed by large language models.[^1] A token corresponds roughly to four characters or three-quarters of a word in English, though the mapping varies across languages and model architectures.[^2] Input tokens (the user's query) and output tokens (the model's response) are metered separately, often at different rates.

[^1]: S Bommasani and others, 'On the Opportunities and Risks of Foundation Models' (2022) arXiv:2108.07258, 101–103.

[^2]: The variability in tokenization across languages creates additional transparency problems: a query in German may consume substantially more tokens than an equivalent query in English due to compound word structures, yet providers rarely disclose language-specific consumption metrics.

This granularity creates an appearance of perfect cost alignment. Consumers pay only for what they use; there is no risk of overpaying for unused capacity; costs scale predictably with consumption.[^3] The model appears to satisfy the price indication requirements of Directive 98/6/EC, which mandates that the selling price and unit price be unambiguous, easily identifiable, and clearly legible.[^4]

[^3]: OpenAI, 'Pricing' (2024) <https://openai.com/pricing> accessed 15 November 2025.

[^4]: Directive 98/6/EC of the European Parliament and of the Council of 16 February 1998 on consumer protection in the indication of the prices of products offered to consumers [1998] OJ L80/27, art 4(1).

The appearance is misleading.

Token-based pricing fundamentally transfers demand uncertainty risk from provider to consumer.[^5] Under subscription models, the provider bears the risk that some consumers will use more than their proportionate share of computational resources while others will use less. The provider prices the subscription to achieve profitability across the aggregate user base, accepting variance in individual consumption. Under token-based pricing, each consumer bears the full risk of their own consumption uncertainty. A consumer who cannot accurately forecast their usage  —  which describes virtually all consumers interacting with generative AI, given the novelty of the technology and the variability of query complexity  —  faces unpredictable bills that may substantially exceed their initial estimates.[^6]

[^5]: J Farrell and C Shapiro, 'Dynamic Competition with Switching Costs' (1988) 19 RAND J Econ 123, 130–132 (analysing risk allocation in metered versus flat-rate pricing).

[^6]: McKinsey Global Institute, 'The Economic Potential of Generative AI' (McKinsey, June 2023) 62 (reporting that 62% of organisations using token-based AI services experienced unexpected cost overruns in the first year of deployment).

This risk transfer has concrete consequences. Research on telecommunications billing demonstrates that consumers systematically underestimate their future usage when selecting among tariff options, a phenomenon termed the 'flat-rate bias'.[^7] Consumers prefer flat-rate plans even when their revealed usage patterns indicate that pay-per-use would be cheaper, in part because they overvalue the psychological comfort of predictable bills.[^8] When consumers are forced into usage-based billing, many respond with 'usage suppression'  —  reducing consumption below the level that would maximise their utility to avoid the anxiety of accumulating charges.[^9]

[^7]: N Grubb, 'Failing to Choose the Best Price: Theory, Evidence, and Policy' (2015) 82 Rev Econ Stud 278, 282–284.

[^8]: M Lambrecht and B Skiera, 'Paying Too Much and Being Happy About It: Existence, Causes, and Consequences of Tariff-Choice Biases' (2006) 43 J Mkt Res 212, 218–220.

[^9]: K Train, 'Self-Selecting Tariffs under Pure Preferences among Tariffs' (1991) 9 J Reg Econ 247, 253–255.

The behavioral economics literature confirms that token-based pricing triggers loss aversion with particular intensity. Each query submitted under a metered model requires the consumer to incur a visible expenditure  —  a 'micro-loss' that generates cognitive disutility disproportionate to its magnitude.[^10] Prospect theory predicts that consumers will experience greater disutility from small repeated losses than from a single larger loss of equivalent total value.[^11] The cumulative psychological burden of evaluating the cost-benefit ratio of each interaction transforms the experience of using the service from exploration to accounting. This phenomenon  —  sometimes termed the 'taxi meter effect'  —  manifests prominently in AI interfaces: consumers watching token counts accumulate in real-time experience psychological stress that inhibits natural interaction with the service.[^12] Stanford researchers have documented that users on token-based AI plans invest substantial effort in 'prompt engineering' to minimise consumption, reducing queries in ways that compromise output quality to save expenditure.[^13]

[^12]: The taxi meter metaphor captures the cognitive burden of visible, accumulating costs. See J Soman, 'The Mental Accounting of Sunk Time Costs: Why Time Is Not Like Money' (2001) 14 J Behav Dec Making 169, 175–177.

There is a further problem with token-based pricing that derives from the nature of AI services as credence goods  —  goods whose quality consumers cannot fully evaluate even after consumption.[^14] A consumer who receives an AI-generated response cannot readily determine whether the response is accurate, whether it represents the optimal use of computational resources, or whether a different query formulation would have produced better results at lower cost. The information asymmetry inherent in credence goods creates moral hazard: providers may have incentives to inflate consumption through verbose responses or unnecessary reasoning chains, analogous to the documented tendency of automobile mechanics to recommend unnecessary repairs.[^15] Token-based pricing, by making each unit of consumption visible, does not resolve this problem; it merely shifts the locus of exploitation from hidden throttling to potentially inflated consumption.

[^10]: A Tversky and D Kahneman, 'Loss Aversion in Riskless Choice: A Reference-Dependent Model' (1991) 106 Q J Econ 1039, 1046–1049.

[^11]: D Kahneman and A Tversky, 'Prospect Theory: An Analysis of Decision under Risk' (1979) 47 Econometrica 263, 279.

[^13]: Y Liu and others, 'Cost-Aware Prompting: How Token Pricing Shapes User Behavior in Large Language Model Interactions' (Stanford HAI Working Paper, October 2024) 14–18.

[^14]: On credence goods generally, see M Darby and E Karni, 'Free Competition and the Optimal Amount of Fraud' (1973) 16 JL & Econ 67, 70–72.

[^15]: See U Schneider, 'Physician Behavior in Response to Incentives: Evidence from Germany' (2004) 23 J Health Econ 1091, 1103–1105 (documenting overtreatment in fee-for-service medical contexts).

The most severe consumer harm from token-based pricing is 'bill shock'  —  the discovery at the end of a billing period that charges dramatically exceed expectations.[^13] In generative AI, bill shock arises from two sources. First, the relationship between query complexity and token consumption is non-linear and largely opaque to consumers. A simple factual question might consume a few hundred tokens; a request for extended analysis of a complex document might consume tens of thousands.[^14] Second, the computational cost of an AI query depends not merely on the length of the prompt and response but on the cognitive load imposed by the task  —  whether the query requires reasoning, retrieval, or creative generation.[^15] Providers increasingly deploy 'reasoning models' that consume substantially more tokens through chain-of-thought processing, sometimes an order of magnitude more than standard inference.[^16] A consumer who asks an advanced model to 'think carefully' before answering may inadvertently trigger reasoning chains that multiply the token cost beyond any reasonable expectation.

[^13]: See generally Federal Communications Commission, 'Bill Shock Report and Order' (2012) 27 FCC Rcd 4436 (documenting consumer harm from unexpected mobile telephone bills and mandating usage alerts).

[^14]: Anthropic, 'Context Window and Token Usage' (Anthropic Documentation, 2024) (explaining that responses to complex analytical queries may consume 10,000–50,000 output tokens depending on instruction framing).

[^15]: OpenAI, 'o1 System Card' (2024) 8–12 (describing the extended token consumption of reasoning models compared to standard inference).

[^16]: The OpenAI o1 model, released in late 2024, incurs inference costs approximately six times higher than GPT-4o for comparable tasks due to its reasoning architecture. See OpenAI (n 3).

Credit-based pricing attempts to mediate between subscription predictability and usage-based granularity. Consumers pre-purchase bundles of credits that are subsequently consumed per use.[^17] The model introduces upfront cost visibility  —  the consumer knows at the moment of purchase exactly how much they are spending  —  while maintaining the usage-proportionality of metered billing.

[^17]: See eg Jasper AI, 'Plans and Pricing' (2024) (offering credit bundles for AI writing assistance); Adobe, 'Firefly Generative Credits' (2024) (credit system for AI image generation).

Credit-based pricing, however, creates a distinct set of consumer protection problems.

The pre-purchase structure exploits hyperbolic discounting  —  the tendency to heavily discount future costs while overweighting immediate benefits.[^18] At the moment of credit purchase, the consumer experiences the benefit of acquiring consumption capacity. At the moment of consumption, the expenditure feels 'free' because the credits represent a sunk cost.[^19] This decoupling of payment from consumption encourages over-purchase. Consumers anchor to volume discounts offered on larger credit bundles and routinely buy more credits than they will use, a pattern well documented in analogous contexts such as gym memberships and prepaid mobile minutes.[^20]

[^18]: D Laibson, 'Golden Eggs and Hyperbolic Discounting' (1997) 112 Q J Econ 443, 447–450.

[^19]: R Thaler, 'Mental Accounting and Consumer Choice' (1985) 4 Mkt Sci 199, 203–206.

[^20]: S DellaVigna and U Malmendier, 'Paying Not to Go to the Gym' (2006) 96 Am Econ Rev 694, 707–710.

Credit expiration intensifies these dynamics. Many credit-based AI services impose temporal limits on credit validity  —  unused credits forfeit after a period ranging from thirty days to one year.[^21] Expiration creates pure deadweight loss: the consumer has paid for consumption capacity they will not receive. The loss triggers anxiety as expiration approaches, often leading to rushed, low-utility consumption undertaken to avoid 'wasting' the purchased credits rather than to achieve any genuine purpose.[^22]

[^21]: Adobe Firefly credits, for example, expire monthly on subscription plans. See Adobe (n 17).

[^22]: H Arkes and C Blumer, 'The Psychology of Sunk Cost' (1985) 35 Org Behav & Hum Dec Proc 124, 131–133.

Credit-based pricing also creates significant switching costs. A consumer who has pre-purchased credits on Platform A faces a substantial barrier to migrating to Platform B, regardless of whether B offers superior service or lower prices.[^23] The unconsumed credit balance represents a sunk investment that the consumer is reluctant to abandon. Providers can strategically exploit this lock-in by offering bonus credits on large purchases, ensuring that consumers maintain credit balances that deter switching.[^24] The competitive harm from this lock-in mechanism may offset any transparency benefits that credit systems provide over subscriptions.

[^23]: P Klemperer, 'Competition when Consumers have Switching Costs: An Overview with Applications to Industrial Organization, Macroeconomics, and International Trade' (1995) 62 Rev Econ Stud 515, 525–528.

[^24]: This strategy mirrors the loyalty programme lock-in documented in airline frequent flyer research. See MN Borenstein, 'The Evolution of U.S. Airline Competition' (1992) 6 J Econ Persp 45, 62–64.

Credit-based and token-based pricing models also raise equity concerns that extend beyond individual consumer welfare to broader questions of access and development. Prepayment requirements act as capital barriers: consumers in developing economies or those with limited financial resources must accumulate funds before accessing services, whereas subscription models distribute costs over time.[^25] The requirement for international payment infrastructure  —  typically credit cards with cross-border transaction capabilities  —  excludes populations without access to such financial instruments.[^26] Students and early-career professionals, who might derive substantial human capital benefits from AI tools, face particular disadvantages under consumption-based pricing, as their limited budgets create anxiety that inhibits the exploratory use most conducive to learning.[^27] These distributional effects are not incidental market outcomes; they represent systematic exclusion of economically vulnerable populations from technologies that may reshape educational and professional opportunity structures.

[^25]: On financial access barriers in digital services, see P Aker and I Mbiti, 'Mobile Phones and Economic Development in Africa' (2010) 24 J Econ Persp 207, 218–221.

[^26]: World Bank, Global Findex Database 2021: Financial Inclusion, Digital Payments, and Resilience in the Age of COVID-19 (World Bank 2022) 24–28 (documenting global disparities in access to digital payment infrastructure).

[^27]: See generally A Sen, Development as Freedom (OUP 1999) 87–110 (analysing how financial constraints reduce capability and opportunity).

From a consumer protection standpoint, neither token-based nor credit-based pricing resolves the fundamental opacity problems of AI service contracts. Both models denominate costs in provider-centric units  —  tokens or credits  —  that do not correspond to the consumer's value proposition.[^25] A consumer does not want '100,000 tokens'; they want 'a tool that helps me draft documents' or 'a service that answers my questions'. The translation from provider-centric units to consumer-centric value requires knowledge that the consumer does not possess and often cannot acquire: how many tokens does a typical document require? How does query complexity affect consumption? What is the variance around expected usage?[^26]

[^25]: Ibbaka, 'Four Perspectives on Credit-Based Pricing for AI Agents' (2024) (observing that consumers prefer outcome-based units such as 'images generated' or 'documents processed' over raw consumption metrics like tokens).

[^26]: The unit of account problem in AI pricing mirrors longstanding concerns about electricity tariff comprehensibility. See J Defeuilley, 'Retail Competition in Electricity Markets' (2009) 37 Energy Pol'y 377, 383–384.

### Flat-rate unlimited pricing: the tragedy of the commons

If measured pricing transfers too much risk to consumers, flat-rate unlimited pricing would appear to resolve the problem by transferring all consumption risk to providers. Under a flat-rate model, consumers pay a fixed periodic fee for unrestricted access  —  no caps, no throttling, no metering.[^27]

[^27]: The 'flat-rate bias' documented in telecommunications research demonstrates strong consumer preference for unlimited pricing, suggesting that such models would attract substantial demand. See Lambrecht and Skiera (n 8) 222.

Flat-rate pricing has theoretical appeal from a consumer welfare perspective. It eliminates usage anxiety entirely. The consumer need never calculate whether a particular query is 'worth' its incremental cost, because the marginal cost of each query is zero.[^28] Mental accounting is simplified to a single, predictable expense. The model appears to satisfy transparency requirements completely: the price is fixed, unambiguous, and unrelated to any variable the consumer cannot observe.

[^28]: This zero marginal cost perception is behaviourally powerful even when economically irrational. See J Shampanier, N Mazar and D Ariely, 'Zero as a Special Price: The True Value of Free Products' (2007) 26 Mkt Sci 742, 748–752.

The problem is that flat-rate unlimited pricing for AI services is economically unsustainable absent substantial constraints that reintroduce the very opacity problems it purports to solve.

The computational costs of generative AI are substantial and scale with usage.[^29] Each inference operation consumes GPU cycles, electricity, and cooling resources that represent real marginal costs to the provider.[^30] Unlike purely digital goods where marginal cost approaches zero  —  streaming a song costs effectively nothing once the recording exists  —  AI inference has non-trivial marginal costs that vary with query complexity, model sophistication, and system load.[^31] A provider offering genuinely unlimited access at a fixed price must set that price to cover the expected consumption of heavy users, which necessarily means that light users substantially overpay relative to their usage.[^32]

[^29]: Patterson and others, 'Carbon Emissions and Large Neural Network Training' (2021) arXiv:2104.10350, 3–7 (documenting computational and energy costs of AI model inference).

[^30]: Andreessen Horowitz, 'Navigating the High Cost of AI Compute' (a16z, 2024) (analysing inference cost structures across major cloud providers).

[^31]: The contrast with streaming media is instructive: Netflix's marginal cost per stream is effectively zero, whereas OpenAI's marginal cost per inference is measurably positive and increases with query complexity.

[^32]: This cross-subsidisation structure is economically analogous to the 'gym membership effect' documented in fitness industry pricing. See DellaVigna and Malmendier (n 20) 709–711.

The structural incentive for providers under flat-rate models is therefore to constrain consumption in ways that are not visible at the point of contract formation. This is precisely the phenomenon observed in current AI subscription pricing: 'unlimited' access that is in practice limited by 'fair use' policies, rate limits, throttling during peak periods, and degraded service quality for heavy users.[^33] The flat-rate pricing creates the illusion of unrestricted access while the operational reality introduces restrictions that the consumer cannot observe, evaluate, or compare across providers.

[^33]: See Part II above (documenting vague capacity terms in major AI provider agreements).

If providers were genuinely to offer unlimited AI access without hidden constraints, two outcomes would follow. First, prices would rise substantially to cover heavy-user consumption, pricing out casual users who cannot justify the expense.[^34] Second, providers would face adverse selection: the unlimited plan would disproportionately attract heavy users whose consumption exceeds the average, while light users would migrate to cheaper alternatives, raising the average cost per remaining subscriber in a cycle that can destabilise the pricing structure entirely.[^35]

[^34]: The gaming industry provides an illustrative example: subscription services offering unlimited access to games typically price at levels that assume moderate consumption, then implement soft limits through download speeds, device restrictions, or library rotation.

[^35]: On adverse selection spirals in insurance-style pricing models, see M Rothschild and J Stiglitz, 'Equilibrium in Competitive Insurance Markets: An Essay on the Economics of Imperfect Information' (1976) 90 Q J Econ 629, 638–640.

The adverse selection dynamic operates through a predictable four-stage mechanism.[^36] First, unraveling: if a cheaper metered alternative becomes available, low-cost 'light' users  —  those whose actual usage is well below the subscription price  —  leave the flat-rate pool for the cheaper option. Second, adverse selection intensifies: the remaining subscriber base now consists disproportionately of high-cost 'heavy' users. Third, repricing: the provider must raise subscription prices to cover the actual costs of this heavier-usage pool. Fourth, further exodus: the price increase drives out the next tranche of relatively lighter users, who now find metered pricing more attractive, until the subscription becomes unviably expensive for all but the most extreme power users.[^37] This 'death spiral' dynamic explains why providers cannot sustain transparent flat-rate pricing without hidden constraints: the constraints are not merely profit-maximising mechanisms but structural requirements to prevent adverse selection from collapsing the pricing model entirely.

[^36]: This mechanism is formalised in the insurance economics literature. See generally D Cutler and R Zeckhauser, 'Adverse Selection in Health Insurance' (2000) 1 Forum for Health Economics & Policy Article 1.

[^37]: The dynamics have been documented in health insurance markets. See M Pauly and others, 'What Death Spirals? Managed Care in California Employer-Sponsored Coverage' (2002) 21 Health Aff 79, 82–85.

The tragedy of the commons framework illuminates the fundamental problem.[^36] Computational capacity in an AI service is a rivalrous resource  —  one user's consumption of GPU cycles reduces availability for others.[^37] Under flat-rate pricing with genuine unlimited access, each consumer is incentivised to maximise their own consumption because the marginal cost to them is zero, even though the marginal cost to the system is positive. The aggregate effect of individually rational overconsumption is system degradation, service quality reduction, or economic unsustainability.[^38]

[^36]: G Hardin, 'The Tragedy of the Commons' (1968) 162 Science 1243.

[^37]: Researchers have empirically demonstrated tragedy-of-the-commons dynamics in multi-tenant AI systems where shared computational resources degrade under heavy load. See eg L Chen and others, 'Noisy Neighbors: GPU Contention in Multi-Tenant AI Inference' (2024) Proceedings of MLSys 287, 293–295.

[^38]: The dynamics mirror electricity grid management during peak demand, where flat-rate pricing encourages consumption patterns that strain infrastructure. See Defeuilley (n 26) 381–382.

Providers manage this commons problem through precisely the mechanisms that create transparency and contractual certainty deficits: vague terms that reserve discretion to constrain access, rate limits that are not disclosed at contract formation, quality degradation during high-demand periods, and fair use policies that are undefined or defined in ways the consumer cannot operationalise.[^39] The flat-rate model does not eliminate opacity; it makes opacity structurally necessary.

[^39]: This governance-through-opacity pattern is documented in commons management literature. See E Ostrom, Governing the Commons: The Evolution of Institutions for Collective Action (CUP 1990) 88–92 (describing how resource managers employ ambiguous rules to retain adaptive flexibility).

### Tiered pricing: segmentation and structural inequity

Tiered pricing  —  the dominant model in current AI service markets  —  attempts to balance these competing concerns by offering multiple service levels at different price points.[^40] Consumers self-select into tiers based on their anticipated needs: a free tier for casual exploration, a 'Pro' tier for regular individual use, a 'Teams' tier for collaborative work, an 'Enterprise' tier for organisational deployment.[^41]

[^40]: See OpenAI, Anthropic, and Google pricing pages (n 3 and accompanying text).

[^41]: This tiered structure mirrors the 'versioning' strategies documented in information goods literature. See C Shapiro and HR Varian, Information Rules: A Strategic Guide to the Network Economy (HBS Press 1999) 53–81.

Tiered pricing has apparent virtues. It accommodates heterogeneous consumer needs without forcing everyone into a single pricing structure. It enables market segmentation that can improve allocative efficiency by matching consumers to service levels appropriate to their valuation.[^42] It provides price competition across tiers, creating pressure for providers to offer genuine value at each level. Empirical research on digital platform pricing provides qualified support for this proposition: a study of the Xbox video game platform found that multi-tiered subscription bundles increased consumer surplus by sixteen per cent compared to a-la-carte metered pricing, suggesting that well-designed tier structures can generate welfare gains by enabling consumers to access more content at predictable prices.[^43]

[^42]: On second-degree price discrimination and efficiency, see JA Tirole, The Theory of Industrial Organization (MIT Press 1988) 134–141.

[^43]: L Derdenger and V Kumar, 'The Dynamic Effects of Bundling as a Product Strategy' (2013) 32 Mkt Sci 827, 841–844. The study found that single-tier bundling reduced consumer surplus below the a-la-carte baseline, but multiple tiers restored and improved surplus.

The problems with tiered pricing are more subtle but no less significant.

First, tiered pricing is a mechanism for price discrimination  —  specifically, second-degree price discrimination through self-selection.[^43] Providers design tiers not to maximise consumer welfare but to maximise revenue extraction by inducing consumers to reveal their willingness to pay through tier choice.[^44] The free tier is calibrated to be useful enough to attract users but limited enough to frustrate them into upgrading. The mid-tier is priced to extract maximum surplus from individual professional users. The enterprise tier captures organisational budgets at price points untethered from marginal cost.[^45]

[^43]: Tirole (n 42) 136–138.

[^44]: This is the 'damaged goods' strategy documented in versioning literature, where providers deliberately degrade lower-tier offerings to preserve price differentiation. See R Deneckere and P McAfee, 'Damaged Goods' (1996) 5 J Econ & Mgmt Strategy 149, 152–155.

[^45]: Revenue maximisation through tier design is explicit in industry pricing guidance. See Simon-Kucher, 'AI Pricing Strategy: How to Monetize Your AI Product' (2024) (advising providers to design tiers that 'encourage upgrade behavior').

Second, tiered pricing creates choice complexity that can reduce rather than enhance consumer welfare. Behavioural research documents 'choice overload'  —  the phenomenon whereby increasing the number of options leads to decision paralysis, reduced satisfaction, and suboptimal selection.[^46] When consumers face three or more tiers with different feature bundles, usage limits, and price points, many lack the information or cognitive resources to identify the option that maximises their surplus.[^47] The complexity is compounded when tier features are described in technical terms the consumer cannot evaluate  —  'priority access', 'enhanced context window', 'advanced reasoning capabilities'  —  without clear benchmarks for what these features mean in practice.[^48]

[^46]: S Iyengar and MR Lepper, 'When Choice is Demotivating: Can One Desire Too Much of a Good Thing?' (2000) 79 J Pers & Soc Psychol 995, 999–1002.

[^47]: B Schwartz, The Paradox of Choice: Why More is Less (ECCO 2004) 117–132.

[^48]: The opacity of feature descriptions in AI service tiers creates the information asymmetry conditions associated with market failure in credence goods. See M Darby and E Karni, 'Free Competition and the Optimal Amount of Fraud' (1973) 16 JL & Econ 67, 70–72.

Third, tiered pricing with usage caps reintroduces the core contractual certainty problem in a different form. When the Pro tier offers '5x the capacity of Free', the consumer has no means of determining what absolute quantity of service that represents.[^49] The tier boundary becomes a threshold of uncertainty: consumers cannot predict when they will hit the limit, what happens when they do, and whether upgrading to the next tier represents value proportionate to the price increase.[^50] Research on subscription consumption demonstrates that uncertainty about tier boundaries generates anxiety that reduces service enjoyment even before any limit is reached.[^51]

[^49]: See Part II above (documenting the vagueness of tier differentiation language).

[^50]: This is the 'allowance trap' documented in mobile data pricing: consumers who cannot predict their consumption relative to plan limits either substantially underuse their allocation or pay overage charges. See K Seim, 'Spatial Differentiation and Firm Entry: The Video Retail Industry' (PhD thesis, Yale University 2001) 45–48.

[^51]: S Frederick, G Loewenstein and T O'Donoghue, 'Time Discounting and Time Preference: A Critical Review' (2002) 40 J Econ Lit 351, 378–381.

Fourth, tiered models facilitate tacit coordination among oligopolistic providers. When OpenAI, Anthropic, and Google all offer subscription tiers at similar price points with similar feature differentiations, price competition is constrained by mutual observation and parallel pricing behaviour.[^52] The standardisation of tier structures  —  free, approximately $20/month for individual Pro, approximately $25–30/month for team plans  —  suggests coordination, whether explicit or implicit, that suppresses price competition to the detriment of consumers.[^53]

[^52]: On tacit collusion through price transparency in oligopolistic markets, see J Tirole, The Theory of Industrial Organization (MIT Press 1988) 239–245.

[^53]: The parallel tier structures across major AI providers are documented in Section II above.

The consumer protection problem with tiered pricing is not that price discrimination is inherently harmful  —  under certain conditions, price discrimination can improve total welfare by enabling providers to serve consumers who would otherwise be priced out of the market.[^54] The problem is that tiered pricing for AI services combines discriminatory structures with information asymmetries that prevent consumers from making informed choices. The tiers are designed to extract surplus, not to provide clear value propositions. The boundaries between tiers are opaque. The features distinguishing tiers are described in ways that resist comparison. And the oligopolistic market structure that enables parallel tiered pricing across providers eliminates the competitive pressure that might otherwise discipline these practices.

[^54]: On the welfare economics of price discrimination, see HR Varian, 'Price Discrimination' in R Schmalensee and R Willig (eds), Handbook of Industrial Organization, vol 1 (North-Holland 1989) 597, 618–622.

### The impossibility of a transparent equilibrium

The analysis of alternative pricing models reveals a structural problem that no pricing configuration can fully resolve: the technical characteristics of generative AI create irreducible opacity in the relationship between price and value.

The cost of an AI query is not a stable, observable quantity that can be priced transparently.

AI inference operates under what might be termed an 'impossible trinity' of competing constraints: model quality, inference performance (latency and throughput), and economic cost.[^55] Providers continuously optimise along a cost-quality Pareto frontier, making instantaneous trade-offs that determine the actual cost of each query in ways invisible to consumers and often to the providers' own pricing teams.[^56] The cost of responding to a query depends on the specific model weights loaded in memory at that moment, the current GPU utilisation across the provider's fleet, the queueing delays imposed by concurrent requests, and the caching state of relevant context. These variables fluctuate second by second.

[^55]: The concept of impossible trinities in economic systems originates in international finance. See RA Mundell, 'Capital Mobility and Stabilization Policy under Fixed and Flexible Exchange Rates' (1963) 29 Can J Econ & Pol Sci 475. The application to AI systems reflects analogous structural constraints.

[^56]: On the cost-quality trade-offs inherent in large language model inference, see T Brown and others, 'Language Models are Few-Shot Learners' (2020) 33 NIPS 1877, 1892–1894.

It depends on the model deployed, which providers routinely update without notice.[^57] It depends on query complexity, which neither provider nor consumer can predict with precision before execution.[^58] It depends on system load, which varies moment to moment across provider infrastructure.[^59] It depends on reasoning depth, which is determined by the model's internal processing in ways that are not visible to users.[^60] No pricing model can make transparent a cost function that is inherently stochastic and multi-dimensional.

[^55]: OpenAI, 'Model Updates and Deprecation' (2024) (documenting that model versions may be updated without changelog publication for minor improvements).

[^56]: The non-linear relationship between query characteristics and computational cost is a fundamental property of transformer architecture inference. See A Vaswani and others, 'Attention Is All You Need' (2017) NIPS 5998, 6001.

[^57]: Multi-tenant GPU infrastructure exhibits congestion externalities where one user's heavy workload affects performance for others. See Chen and others (n 37) 289–291.

[^58]: Reasoning models like OpenAI o1 consume tokens through internal chain-of-thought processing that is not visible to users and varies unpredictably with query characteristics. See OpenAI (n 15) 9–11.

This irreducible opacity means that consumers cannot, under any pricing model, fully understand what they are purchasing before they purchase it. Metered pricing makes the cost formula visible but leaves the consumption quantity unpredictable. Flat-rate pricing makes the total cost predictable but hides the quality and capacity constraints that make the price sustainable. Tiered pricing creates an illusion of choice among well-defined options while obscuring both what each tier provides and where its boundaries lie.

The opacity problem is compounded by the failure of familiar pricing analogies to transfer from other industries. Cloud computing's spot instance pricing  —  where users bid for interruptible compute capacity at variable prices  —  does not translate to consumer AI services because AI inference cannot be meaningfully interrupted mid-query; a two-minute termination warning, acceptable for batch processing, is incompatible with conversational interaction.[^61] Airline revenue management, which dynamically prices a fixed inventory of perishable seats, likewise fails as an analogy because AI capacity is generative rather than fixed: providers can scale infrastructure, whereas airlines cannot add seats to an already-manufactured aircraft.[^62] Public utility pricing for electricity provides perhaps the closest structural parallel, but electricity is a fungible commodity  —  one kilowatt-hour is equivalent to another  —  whereas AI queries are non-fungible services whose value depends on content, context, and quality.[^63] The search for 'best practices' from analogous industries is therefore unlikely to yield workable solutions; the technical characteristics of AI inference create pricing challenges that are, to a significant degree, sui generis.

[^61]: Amazon Web Services, 'Spot Instance Interruptions' (AWS Documentation, 2024) (describing the two-minute interruption warning for spot instances).

[^62]: On the economics of airline yield management, see K Talluri and G van Ryzin, The Theory and Practice of Revenue Management (Springer 2004) 156–189.

[^63]: On the commodity versus service distinction in pricing, see C Shapiro and HR Varian, Information Rules: A Strategic Guide to the Network Economy (HBS Press 1999) 20–28.

It must be acknowledged that the analysis presented here does not demonstrate that all alternative pricing models are worse than current tiered subscriptions for all consumers. Consumer heterogeneity complicates any categorical assessment.[^64] Light users  —  those whose consumption falls below the twenty-fifth percentile of the usage distribution  —  may fare better under metered pricing, avoiding the cross-subsidisation that flat rates impose. Heavy users with predictable, sustained consumption patterns may benefit from flat-rate models that bound their costs regardless of usage intensity. Budget-constrained consumers may prefer the pay-as-you-go flexibility of token-based pricing despite its anxiety-inducing characteristics. Variable or 'bursty' users may find hybrid models  —  combining a base subscription with metered overages  —  optimal for their particular consumption patterns.[^65] Welfare analysis that aggregates across these heterogeneous consumer types may obscure distributional effects that favour some groups while harming others.

[^64]: On consumer heterogeneity in optimal tariff design, see R Schmalensee, 'Monopolistic Two-Part Pricing Arrangements' (1981) 12 Bell J Econ 445, 458–462.

[^65]: Hybrid models that combine subscription base access with usage-based marginal pricing have been shown in telecommunications research to achieve higher total welfare under certain demand distributions. See S Sundararajan, 'Nonlinear Pricing of Information Goods' (2004) 50 Mgmt Sci 1660, 1668–1672.

The implication for consumer protection law is significant. If transparency-based remedies cannot fully succeed  —  if the technical characteristics of the service create opacity that no pricing model can eliminate  —  then regulatory intervention must proceed on a different basis. The question is not how to mandate pricing structures that make AI services transparent; it is how to allocate the risks created by irreducible opacity in ways that protect consumers from exploitation while preserving functioning markets for beneficial services.

The answer may lie not in prescribing pricing models but in regulating the practices that exploit opacity: mandatory disclosure of capacity constraints at contract formation, prohibition of unilateral modification of material terms during subscription periods, standardised metrics for service quality that enable cross-provider comparison, and liability rules that allocate the risks of consumption uncertainty to the party best positioned to bear and manage them.[^66] These interventions accept that perfect transparency is impossible and focus instead on preventing the harms that opacity enables. Effective transparency regulation should adopt design principles that account for behavioral realities: graduated complexity that offers simple headline information with optional deeper detail; comparative rather than absolute metrics ('you used eighty per cent of your allocation' rather than raw token counts); predictive rather than real-time disclosure (monthly projections rather than live cost tickers); and mechanisms that enable precommitment through caps and budgets to reduce ongoing monitoring burdens.[^67]

[^66]: See Part V below (proposing regulatory interventions based on this analysis).

[^67]: On optimal transparency design in consumer markets, see OI Bar-Gill and R Warren, 'Making Credit Safer' (2008) 157 U Pa L Rev 1, 65–71 (advocating graduated disclosure approaches).
