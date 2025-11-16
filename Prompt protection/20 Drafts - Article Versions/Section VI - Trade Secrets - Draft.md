# VI. Trade Secrets

## A. The Directive 2016/943 Framework

Copyright, software, database, and patent protections all fail to accommodate prompts' functional character and instructional nature. Trade secrets offer a fundamentally different protection mechanism – one based on secrecy rather than creativity or technical innovation. Directive (EU) 2016/943 on the protection of undisclosed know-how and business information, adopted 8 June 2016 with Member State transposition required by 9 June 2018, harmonizes trade secret protection across the European Union by establishing minimum standards for civil remedies against unlawful acquisition, use, and disclosure.[^109]

[^109]: Directive (EU) 2016/943 of the European Parliament and of the Council of 8 June 2016 on the protection of undisclosed know-how and business information (trade secrets) against their unlawful acquisition, use and disclosure [2016] OJ L157/1 ('Trade Secrets Directive').

The Directive implements the EU's obligations under Article 39 of the TRIPS Agreement, which requires WTO members to protect undisclosed information that is secret, has commercial value because it is secret, and has been subject to reasonable steps to maintain secrecy.[^110] Article 2(1) of Directive 2016/943 defines "trade secret" through a three-part cumulative test requiring that information: "(a) it is secret in the sense that it is not, as a body or in the precise configuration and assembly of its components, generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question; (b) it has commercial value because it is secret; (c) it has been subject to reasonable steps under the circumstances, by the person lawfully in control of the information, to keep it secret."[^111]

[^110]: TRIPS Agreement (n 14) art 39(2).

[^111]: Trade Secrets Directive (n 109) art 2(1).

The three requirements are cumulative – failure to satisfy any single element defeats trade secret status entirely.

The Directive balances protection against competing policy objectives. Article 1(3) excludes "employees' use of experience and skills honestly acquired in the normal course of their employment."[^112] Article 3 establishes that acquisition is lawful when obtained by "independent discovery or creation," "observation, study, disassembly or testing of a product or object that has been made available to the public," or reverse engineering.[^113]

[^112]: ibid art 1(3).

[^113]: ibid art 3(1).

These exclusions prove critical for prompts. Reverse engineering from AI outputs constitutes lawful acquisition. Independent discovery through parallel prompt engineering experimentation is protected. The policy framework permits competitors to reach similar prompts through their own efforts while prohibiting misappropriation through unlawful means such as breach of confidentiality agreements or hacking.

## B. The Secrecy Requirement and the Cloud Disclosure Paradox

The first element – that information be "secret in the sense that it is not, as a body or in the precise configuration and assembly of its components, generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question" – establishes an objective standard based on accessibility within relevant professional circles.[^116] This requirement confronts AI prompts with a fundamental obstacle: cloud-based AI services require transmitting prompts to third-party providers with each API call or chat interface interaction.

[^116]: ibid art 2(1)(a).

OpenAI's GPT-4, Anthropic's Claude, Google's Gemini, and similar commercial offerings process prompts on the provider's infrastructure. Prompts necessarily travel across networks and reside, at least temporarily, on systems controlled by the AI provider rather than the user. This creates a doctrinal tension: does third-party disclosure destroy the secrecy required for trade secret protection, or can contractual confidentiality provisions with service providers sufficiently preserve secrecy despite physical disclosure?

Academic scholarship demonstrates that third-party disclosure destroys trade secret status absent confidentiality agreements.[^117] National courts across Member States apply this principle strictly. The German Higher Regional Court of Düsseldorf held that disclosure to third parties without executed confidential disclosure agreements defeats trade secret protection.[^118] The Dutch District Court Middle Netherlands and Paris Court of Appeal reached identical conclusions: unprotected third-party disclosure fails the secrecy requirement regardless of other protective measures.[^119]

[^117]: Sharon K. Sandeen and Elizabeth A. Rowe, *Trade Secrecy and International Transactions: Law and Practice* (Edward Elgar 2015) 42–47.

[^118]: OLG Düsseldorf 4 November 2021, I-20 U 16/20, ECLI:DE:OLGD:2021:1104.I20U16.20.00, para 47.

[^119]: Rechtbank Midden-Nederland 15 August 2018, ECLI:NL:RBMNE:2018:3992; CA Paris 9 June 2022, RG n° 19/08167.

Applied to AI prompts, this creates a critical distinction between service tiers. Consumer-tier AI services – including free ChatGPT, Claude.ai, and similar offerings – include terms permitting the provider to use inputs for model training and service improvement.[^120] These terms grant providers rights to use prompts, defeating secrecy. Information disclosed to a party with contractual authorization to use it cannot be "secret" within Article 2(1)(a). The provider's engineers and data scientists constitute "persons within the circles that normally deal with the kind of information in question."

[^120]: OpenAI, 'Terms of Use' (14 November 2023) <https://openai.com/policies/terms-of-use> accessed 10 November 2025; Google, 'Google Terms of Service' (5 January 2024) <https://policies.google.com/terms> accessed 10 November 2025; Anthropic, 'Consumer Terms of Service' (22 July 2024) <https://www.anthropic.com/legal/consumer-terms> accessed 10 November 2025.

Enterprise-tier AI services present a different picture. Microsoft Azure OpenAI Service, Anthropic's Enterprise plan, and Google Cloud's Vertex AI contractually provide that customer data will not be used for training or improving models.[^121] These contractual provisions prohibit the provider from using prompts beyond processing the specific customer's requests. The prompts remain disclosed to the provider – they must be, to function – but the disclosure occurs under confidentiality obligations analogous to disclosure to employees under NDAs.

[^121]: Microsoft, 'Azure OpenAI Service Data, Privacy, and Security' (1 March 2024) <https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy> accessed 10 November 2025; Anthropic, 'Enterprise Features' <https://www.anthropic.com/enterprise> accessed 10 November 2025; Google Cloud, 'Data Usage FAQ' <https://cloud.google.com/vertex-ai/docs/generative-ai/data-governance> accessed 10 November 2025.

The German courts' framework supports this distinction. The Higher Regional Court of Düsseldorf's requirement of "executed confidential disclosure agreements" with third parties implies that properly documented contractual protections satisfy the secrecy requirement even where service providers necessarily access the information.[^122]

[^122]: OLG Düsseldorf (n 118) para 47.

The third-party disclosure framework yields a bright-line rule: only prompts used exclusively through enterprise AI services with robust contractual confidentiality provisions can potentially satisfy the secrecy requirement. Prompts submitted through consumer-tier services fail Article 2(1)(a) and cannot qualify as trade secrets under EU law.

## C. Commercial Value Derived from Secrecy

The second element – that information "has commercial value because it is secret" – requires both that information possess commercial value and that this value derive causally from secrecy rather than from other characteristics.[^130] The Commission's Impact Assessment explained that information has commercial value "whether actual or potential" when "its unauthorized acquisition, use or disclosure is likely to harm the interests of the person lawfully controlling it."[^131] The causal link – "because it is secret" – distinguishes trade secrets from other valuable information; information retaining value even if publicly disclosed does not meet this requirement.[^132]

[^130]: Trade Secrets Directive (n 109) art 2(1)(b).

[^131]: European Commission, 'Impact Assessment accompanying the Proposal for a Directive on the protection of undisclosed know-how and business information (trade secrets)' SWD(2013) 471 final, 19.

[^132]: ibid.

AI prompts present a challenge because their utility depends on the underlying AI model. A prompt engineered for ChatGPT produces value only when processed by GPT-4 or similar models. This raises whether prompts possess independent commercial value or merely derivative value from model access.

The argument against independent commercial value proceeds from model dependency. If a prompt's value derives primarily from the model rather than the prompt itself, and disclosure would not harm the holder's competitive position because competitors lack the same model access, the commercial value element fails.[^123]

[^123]: OLG Düsseldorf (n 118) para 52 (requiring that unauthorized use harm holder's competitive position).

Three considerations support finding independent commercial value for sophisticated prompts.

First, commercial prompt marketplaces demonstrate market recognition of prompts as valuable assets. PromptBase reports over 370,000 users and more than 220,000 prompts available for purchase.[^124] Prompts sold on these platforms derive value from their effectiveness across multiple users, each with independent model access. The prompt's value resides in the optimized formulation itself.

[^124]: PromptBase, 'About PromptBase' <https://promptbase.com/about> accessed 10 November 2025.

Second, specialized prompts provide measurable economic benefits. Prompts enabling 60% faster drug candidate identification represent quantifiable time savings worth potentially millions of euros. Documented investment – €2.3 million in eighteen months of prompt engineering – creates economic value competitors could misappropriate by copying rather than independently investing.[^125] German courts require objective proof of economic value through documented development costs and quantified performance improvements.[^126]

[^125]: Sharon K. Sandeen, 'The Reasonable Secrecy Requirement' in Rochelle C. Dreyfuss and Katherine J. Strandburg (eds), *The Law and Theory of Trade Secrecy: A Handbook of Contemporary Research* (Edward Elgar 2011) 105, 115–118.

[^126]: OLG Düsseldorf (n 118) para 49.

Third, system prompts embedded in proprietary AI applications can represent substantial engineering investment and provide differentiation among competing products using the same underlying AI model.

The distinction parallels established trade secret doctrine protecting customer lists: publicly available contact information does not qualify, but a curated compilation derived from substantial effort qualifies as a protectable compilation.[^127] Similarly, a refined prompt representing months of optimization constitutes a valuable compilation whose "precise configuration and assembly" – Article 2(1)(a)'s language – has commercial value because competitors lack this optimized formulation.

[^127]: Case C-30/14 *Ryanair Ltd v PR Aviation BV* EU:C:2015:10, para 29 (applied by analogy to trade secret compilations).

The causal link – "because it is secret" – requires that disclosure would harm the holder's competitive advantage. Prompts that codify novel applications, combine techniques in non-obvious ways, or represent substantial optimization work satisfy this requirement. Prompts implementing widely known techniques fail this test – value does not derive from secrecy.

## D. Reasonable Steps under the Circumstances

The third element – that information "has been subject to reasonable steps under the circumstances, by the person lawfully in control of the information, to keep it secret" – requires trade secret holders to exercise what Recital 13 characterizes as a "duty of care as regards the preservation of the confidentiality of their valuable trade secrets."[^140] The "under the circumstances" qualifier establishes that the requirement is context-specific and proportionate, not absolute.[^141]

[^140]: Trade Secrets Directive (n 109) recital 13.

[^141]: European Commission, 'Impact Assessment' (n 131) 21–22.

National courts have developed detailed frameworks for assessing reasonable steps. German courts require measures at legal, organizational, and technical levels.[^128] The Higher Regional Court of Düsseldorf established nine factors for proportionality assessment including type of trade secret, value, circumstances of use, and contractual provisions.[^129] This framework emphasizes proportionality – measures must be reasonable given the information's value and circumstances of use.

[^128]: OLG Düsseldorf (n 118) paras 45–50.

[^129]: ibid para 49.

French courts require specific and targeted measures rather than blanket confidentiality designations.[^130] Dutch courts apply particular strictness: "policy without practice fails the reasonable steps test."[^131] Stated policies that employees routinely violate demonstrate that reasonable steps have not been taken in practice.

[^130]: CA Paris (n 119).

[^131]: Rechtbank Midden-Nederland (n 119).

Cloud AI architecture creates significant challenges because prompts must be transmitted to third-party providers. The decisive question is whether use of enterprise AI services with contractual confidentiality provisions, combined with internal controls, constitutes "reasonable steps under the circumstances." National court guidance suggests contractual protections can suffice. The German courts' emphasis on "executed confidential disclosure agreements" implies that properly documented contractual protections with service providers satisfy reasonable steps even though the provider necessarily accesses the information.[^132]

[^132]: OLG Düsseldorf (n 118) para 47.

Trade secret law developed assuming holders could maintain exclusive physical or digital control. Cloud AI inverts this by requiring disclosure to third parties as a condition of use. German courts' proportionality framework suggests contractual protections can substitute for exclusive control: the nine-factor test includes "specific circumstances of use," indicating that if information's use necessarily requires third-party involvement, reasonable steps must be assessed relative to that constraint.[^133]

[^133]: ibid para 49.

For AI prompts, reasonable steps require comprehensive protection programs: legal measures (enterprise services with documented contractual confidentiality protections, NDAs with employees); organizational measures (access controls, classification systems, employee training, monitoring, enforcement); technical measures (encryption, authentication, sanitization, audit logging, controls preventing consumer service use). The Dutch principle – "policy without practice fails" – requires demonstrating that stated protections are implemented and enforced in reality.[^134]

[^134]: Rechtbank Midden-Nederland (n 119).

## E. Counterarguments: structural vulnerabilities

Three structural vulnerabilities limit trade secret protection's effectiveness for prompts despite formal compliance with Directive 2016/943's requirements.

Article 3(1)(b) explicitly permits acquisition through "observation, study, disassembly or testing of a product or object that has been made available to the public."[^151] Academic research demonstrates that prompts can be reconstructed from analyzing AI outputs, and this reconstruction constitutes lawful acquisition that trade secret law cannot prevent. Businesses relying on trade secret protection must accept that competitors engaging in systematic reverse engineering commit no violation.

[^151]: Trade Secrets Directive (n 109) art 3(1)(b).

Article 3(1)(a) protects "independent discovery or creation" as lawful acquisition.[^152] Prompt engineering requires no specialized equipment, substantial capital investment, or rare expertise. The barrier to independent discovery is relatively low compared to paradigmatic trade secrets like chemical formulas or manufacturing processes. Competitors may independently develop similar or functionally equivalent prompts through parallel experimentation, and such independent development defeats any trade secret claim regardless of the holder's investment.

[^152]: ibid art 3(1)(a).

Article 1(3) emphasizes that trade secret protection "should not offer any ground for restricting the mobility of employees" and explicitly protects "employees' use of experience and skills honestly acquired in the normal course of their employment."[^153] When employees develop prompt engineering expertise while working for one company, they retain the right to use that general skill at subsequent employers. The boundary between protectable specific prompts and unprotectable general prompt engineering skills remains unclear and fact-intensive.

[^153]: ibid art 1(3); recital 13.

These three vulnerabilities mean that trade secret protection for prompts provides weaker and more contingent protection than for traditional trade secrets. The protection is real but limited – it prevents misappropriation through unlawful means (breach of confidentiality agreements, hacking, inducement of breach) but cannot prevent acquisition through lawful means (reverse engineering, independent discovery, employee mobility with general skills).

## F. CJEU guidance: algorithmic information as trade secrets

The CJEU's decision in *Dun & Bradstreet Austria GmbH v Bundeswettbewerbsbehörde* provides authoritative guidance on whether algorithmic information can qualify for trade secret protection under Directive 2016/943.[^154] The Court addressed whether trade secret claims can justify withholding information about automated decision-making logic from data subjects under GDPR transparency obligations. The Court held that controllers must provide "meaningful information about the logic involved" to data subjects, but need not disclose algorithms themselves where doing so would reveal trade secrets.[^155] Austrian law creating a blanket exemption for trade secrets was impermissible; instead, controllers claiming trade secret protection must provide allegedly protected information to supervisory authorities or courts for case-by-case proportionality assessment balancing commercial confidentiality against transparency rights.[^156]

[^154]: Case C-203/22 *Dun & Bradstreet Austria GmbH v Bundeswettbewerbsbehörde* EU:C:2025:144.

[^155]: ibid para 53.

[^156]: ibid paras 58–60.

*Dun & Bradstreet* confirms two principles relevant to prompts. First, algorithmic information – including logical instructions controlling AI system behavior – can in principle qualify as trade secrets; the Court did not categorically exclude computational instructions from protection. Second, trade secret protection is not absolute and must yield to competing fundamental rights and regulatory transparency where proportionality requires. Businesses cannot invoke trade secrecy to avoid disclosure obligations under the GDPR, the AI Act, or sector-specific regulations where transparency outweighs commercial confidentiality.[^157]

[^157]: EUIPO, 'Trade Secrets Litigation Trends in the European Union' (2023) 47–49 (noting developments needed to clarify trade secrets role in data economy and algorithmic transparency contexts).

## G. Synthesis: conditional protection under enterprise frameworks

AI prompts can qualify as trade secrets under current EU law. The qualification is conditional – requiring sophisticated prompts, enterprise service frameworks, rigorous protective measures, and acceptance that regulatory transparency may require disclosure where fundamental rights or public interest outweigh commercial confidentiality.

The three cumulative requirements create distinct barriers. Under Article 2(1)(a)'s secrecy element, prompts submitted through consumer-tier AI services fail because terms of service authorize provider use for training. Only prompts used exclusively through enterprise AI services with contractual prohibitions on provider use or disclosure can potentially satisfy secrecy. Under Article 2(1)(b)'s commercial value element, simple prompts that any competent user could develop through brief experimentation fail. Sophisticated prompts representing substantial documented investment satisfy this requirement because their disclosure would enable competitors to appropriate development results without incurring equivalent costs. Under Article 2(1)(c)'s reasonable steps element, enterprise service agreements prohibiting provider use or disclosure, combined with comprehensive internal measures, can satisfy this requirement despite cloud AI's distributed architecture.

Simple prompts fail all three elements. Intermediate prompts representing modest optimization face challenges under reasonable steps proportionality. Sophisticated prompts representing substantial investment can qualify if, and only if, used exclusively through enterprise services with documented contractual protections and subject to comprehensive internal controls.

Unresolved tensions require CJEU clarification or legislative guidance. No preliminary ruling has directly interpreted Directive 2016/943's three-part test for algorithmic information. National courts have developed divergent approaches. Cross-border uncertainty will persist until the CJEU addresses whether third-party disclosure with contractual safeguards satisfies secrecy and reasonable steps requirements.[^158]

[^158]: As of November 2025, no CJEU preliminary ruling under TFEU art 267 has addressed core definitional questions under Directive 2016/943 regarding algorithmic or computational information.

The intersection between trade secret protection and AI transparency requirements under the AI Act remains incompletely theorized. The AI Act imposes transparency obligations on high-risk AI systems including technical documentation, training data disclosure, and deployment logs.[^159] Recital 75 acknowledges that trade secret information "should be safeguarded" but provides no detailed operational guidance.[^160] *Dun & Bradstreet* establishes the framework – case-by-case balancing by authorities or courts – but implementing this for AI Act compliance will require either Commission guidance or judicial decisions.

[^159]: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence [2024] OJ L184/1 ('AI Act') arts 11–13, 53.

[^160]: ibid recital 75.

Trade secret protection for prompts exists doctrinally, but it is demanding, contested, and ultimately provisional pending authoritative interpretation.
