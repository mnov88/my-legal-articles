# VI. Trade Secrets

## A. The Directive 2016/943 Framework

Copyright, software, database, and patent protections all fail to accommodate prompts' functional character and instructional nature. Trade secrets offer a fundamentally different protection mechanism – one based on secrecy rather than creativity or technical innovation. Directive (EU) 2016/943 on the protection of undisclosed know-how and business information, adopted 8 June 2016 with Member State transposition required by 9 June 2018, harmonizes trade secret protection across the European Union by establishing minimum standards for civil remedies against unlawful acquisition, use, and disclosure.[^109]

[^109]: Directive (EU) 2016/943 of the European Parliament and of the Council of 8 June 2016 on the protection of undisclosed know-how and business information (trade secrets) against their unlawful acquisition, use and disclosure [2016] OJ L157/1 ('Trade Secrets Directive').

The Directive implements the EU's obligations under Article 39 of the TRIPS Agreement, which requires WTO members to protect undisclosed information that is secret, has commercial value because it is secret, and has been subject to reasonable steps to maintain secrecy.[^110] Article 2(1) of Directive 2016/943 defines "trade secret" through a three-part cumulative test requiring that information: "(a) it is secret in the sense that it is not, as a body or in the precise configuration and assembly of its components, generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question; (b) it has commercial value because it is secret; (c) it has been subject to reasonable steps under the circumstances, by the person lawfully in control of the information, to keep it secret."[^111]

[^110]: TRIPS Agreement (n 14) art 39(2).

[^111]: Trade Secrets Directive (n 109) art 2(1).

The definition remained essentially unchanged from the European Commission's November 2013 proposal through final adoption in June 2016, demonstrating consensus that the TRIPS Article 39 formulation provides an appropriate international standard.[^112] The three requirements are cumulative – failure to satisfy any single element defeats trade secret status entirely. Recital 14 emphasizes that the definition "should cover know-how, business information and technological information where there is both a legitimate interest in keeping them confidential and a legitimate expectation that such confidentiality will be preserved."[^113]

[^112]: European Commission, 'Proposal for a Directive on the protection of undisclosed know-how and business information (trade secrets) against their unlawful acquisition, use and disclosure' COM(2013) 813 final.

[^113]: Trade Secrets Directive (n 109) recital 14.

The Directive balances protection against competing policy objectives. Article 1(3) provides that "nothing in this Directive shall be understood to offer any ground for restricting the mobility of employees" and specifically excludes "employees' use of experience and skills honestly acquired in the normal course of their employment."[^114] Article 3 establishes that acquisition of a trade secret is lawful when obtained by "independent discovery or creation," "observation, study, disassembly or testing of a product or object that has been made available to the public or that is lawfully in the possession of the acquirer," reverse engineering, or "any other practice which, under the circumstances, is in conformity with honest commercial practices."[^115]

[^114]: ibid art 1(3).

[^115]: ibid art 3(1).

These exclusions prove critical for prompts. Reverse engineering from AI outputs – reconstructing effective prompts by analyzing generated content – constitutes lawful acquisition under Article 3(1)(b). Independent discovery through parallel prompt engineering experimentation is protected under Article 3(1)(a). The policy framework thus permits competitors to reach similar prompts through their own efforts while prohibiting misappropriation of prompts through unlawful means such as breach of confidentiality agreements, hacking, or inducement of breach of contract.

## B. The Secrecy Requirement and the Cloud Disclosure Paradox

The first element – that information be "secret in the sense that it is not, as a body or in the precise configuration and assembly of its components, generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question" – establishes an objective standard based on accessibility within relevant professional circles.[^116] This requirement confronts AI prompts with a fundamental obstacle: cloud-based AI services require transmitting prompts to third-party providers with each API call or chat interface interaction.

[^116]: ibid art 2(1)(a).

OpenAI's GPT-4, Anthropic's Claude, Google's Gemini, and similar commercial offerings process prompts on the provider's infrastructure. Prompts necessarily travel across networks and reside, at least temporarily, on systems controlled by the AI provider rather than the user. This creates a doctrinal tension: does third-party disclosure destroy the secrecy required for trade secret protection, or can contractual confidentiality provisions with service providers sufficiently preserve secrecy despite physical disclosure?

Academic scholarship examining information flows in cloud computing contexts demonstrates that third-party disclosure potentially destroys trade secret status absent express or implied confidentiality agreements establishing duties not to use or disclose the information.[^117] Sharon K. Sandeen's analysis emphasizes that without contractual protections, information "known outside" the company by a service provider may lack the required secrecy, and the information becomes "readily ascertainable" by the provider who possesses it.[^118]

[^117]: Sharon K. Sandeen and Elizabeth A. Rowe, *Trade Secrecy and International Transactions: Law and Practice* (Edward Elgar 2015) 42–47.

[^118]: ibid 45.

National court decisions across Member States demonstrate strict application of the secrecy requirement in contexts involving third-party disclosure. The German Higher Regional Court of Düsseldorf held in 2021 that disclosure to third parties without executed confidential disclosure agreements can result in loss of trade secret protection.[^119] The court emphasized that vetting partners, ensuring minimum necessary disclosure, and maintaining executed non-disclosure agreements constitute essential reasonable steps.[^120]

[^119]: OLG Düsseldorf 4 November 2021, I-20 U 16/20, ECLI:DE:OLGD:2021:1104.I20U16.20.00.

[^120]: ibid para 47.

The Dutch District Court Middle Netherlands held in August 2018 that technical drawings marked as confidential but shared with third parties without NDAs failed to qualify as trade secrets.[^121] The policy of maintaining secrecy existed, but the practice of unprotected disclosure defeated the claim. The Paris Court of Appeal similarly held in 2022 that sharing technical drawings with third parties without non-disclosure agreements failed both the secrecy element and the reasonable steps test.[^122]

[^121]: Rechtbank Midden-Nederland 15 August 2018, ECLI:NL:RBMNE:2018:3992.

[^122]: CA Paris 9 June 2022, RG n° 19/08167.

The judicial consensus across Germany, France, and the Netherlands establishes a clear principle: third-party disclosure without contractual protections defeats trade secret status regardless of other protective measures the holder may have implemented.

Applied to AI prompts, this doctrine creates a critical distinction between service tiers. Consumer-tier AI services – including free ChatGPT, free Claude.ai, and similar offerings – generally include terms of service permitting the provider to use inputs for model training and service improvement. OpenAI's terms of service for the free tier state that "we may use Content to provide, maintain, develop, and improve our Services," representing contractually authorized use that defeats trade secret status.[^123] Google's terms similarly authorize broad use of user content.[^124] Anthropic's terms for free Claude.ai access permit use "to provide, maintain, and improve our Services."[^125]

[^123]: OpenAI, 'Terms of Use' (14 November 2023) <https://openai.com/policies/terms-of-use> accessed 10 November 2025.

[^124]: Google, 'Google Terms of Service' (5 January 2024) <https://policies.google.com/terms> accessed 10 November 2025.

[^125]: Anthropic, 'Consumer Terms of Service' (22 July 2024) <https://www.anthropic.com/legal/consumer-terms> accessed 10 November 2025.

These terms grant the provider rights to use prompts for training, fundamentally defeating secrecy. Information disclosed to a party with contractual authorization to use it cannot be "secret" within the meaning of Article 2(1)(a). The provider's engineers, researchers, and data scientists who have authorized access to user prompts constitute "persons within the circles that normally deal with the kind of information in question" – they are AI specialists to whom the prompts are "readily accessible."

Enterprise-tier AI services present a different picture. Microsoft Azure OpenAI Service contractually provides that "Customer Data" including prompts "will not be available to other customers" and "will not be used to improve Azure OpenAI or any other Microsoft offering."[^126] Anthropic's Enterprise plan provides that customer data "will not be used for training or improving our models."[^127] Google Cloud's Vertex AI terms provide that customer data "will not be used to improve Google's products or services."[^128]

[^126]: Microsoft, 'Azure OpenAI Service Data, Privacy, and Security' (1 March 2024) <https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy> accessed 10 November 2025.

[^127]: Anthropic, 'Enterprise Features' <https://www.anthropic.com/enterprise> accessed 10 November 2025.

[^128]: Google Cloud, 'Data Usage FAQ' <https://cloud.google.com/vertex-ai/docs/generative-ai/data-governance> accessed 10 November 2025.

These contractual provisions prohibit the provider from using prompts for any purpose beyond processing the specific customer's requests. The prompts remain disclosed to the provider – they must be, to function – but the disclosure occurs under confidentiality obligations analogous to disclosure to employees under NDAs. Just as disclosing a trade secret to employees bound by confidentiality agreements does not destroy secrecy, disclosing prompts to AI providers bound by contractual confidentiality provisions potentially preserves secrecy.

The German courts' framework supports this distinction. The Higher Regional Court of Düsseldorf's requirement of "executed confidential disclosure agreements" with third parties implies that properly documented contractual protections satisfy the secrecy requirement even where service providers necessarily access the information.[^129] The emphasis is on contractual controls over use and disclosure, not exclusive physical possession.

[^129]: OLG Düsseldorf (n 119) para 47.

The third-party disclosure framework yields a bright-line rule for prompts: only prompts used exclusively through enterprise AI services with robust contractual confidentiality provisions can potentially satisfy the secrecy requirement. Prompts submitted through consumer-tier services without such protections fail Article 2(1)(a) and cannot qualify as trade secrets under EU law.

The rule reflects the structural reality that cloud AI architecture requires third-party disclosure. Trade secret law accommodates such disclosure where contractual safeguards substitute for exclusive physical control. The accommodation is conditional – the contractual protections must be documented, the enterprise service tier must be deliberately selected rather than defaulting to consumer services, and internal controls must ensure employees comply with the requirement to use only protected services.

Businesses maintaining prompt libraries as trade secrets must therefore implement strict policies: prohibit use of consumer AI services for any prompts containing confidential information; require use only of enterprise services with verified contractual confidentiality provisions; document service agreements and maintain evidence of their terms; train employees on the distinction between consumer and enterprise tiers; monitor compliance through technical controls and audit procedures; and enforce violations through disciplinary measures demonstrating that policies are implemented in practice, not merely stated on paper.

## C. Commercial Value Derived from Secrecy

The second element – that information "has commercial value because it is secret" – requires both that information possess commercial value and that this value derive causally from secrecy rather than from other characteristics.[^130] The Commission's Impact Assessment explained that information has commercial value "whether actual or potential" when "its unauthorized acquisition, use or disclosure is likely to harm the interests of the person lawfully controlling it."[^131] The causal link – "because it is secret" – distinguishes trade secrets from other valuable information; information retaining value even if publicly disclosed does not meet this requirement.[^132]

[^130]: Trade Secrets Directive (n 109) art 2(1)(b).

[^131]: European Commission, 'Impact Assessment accompanying the Proposal for a Directive on the protection of undisclosed know-how and business information (trade secrets)' SWD(2013) 471 final, 19.

[^132]: ibid.

AI prompts present a challenge for the commercial value element because their utility depends fundamentally on the underlying large language model they instruct. A prompt engineered for ChatGPT produces value only when processed by OpenAI's GPT-4 or similar models; the same prompt applied to a different architecture may produce inferior results or fail entirely. The dependency raises whether prompts possess independent commercial value or merely derivative value flowing primarily from access to proprietary AI models.

The argument against independent commercial value proceeds from model dependency. The pharmaceutical company example – prompts enabling 60% faster drug candidate identification – produces value only because Claude processes them effectively; Claude's capabilities derive from Anthropic's investment in model development rather than from the user's prompt engineering work. A prompt for a specific AI model is worthless without access to that model. This distinguishes prompts from paradigmatic trade secrets like chemical formulas or manufacturing processes, which have value independent of any third party's proprietary assets. If a prompt's value derives primarily from the model rather than the prompt itself, and if disclosure would not harm the holder's competitive position because competitors lack access to the same model configuration, the commercial value element might fail.[^133]

[^133]: OLG Düsseldorf (n 119) para 52 (holding that unauthorized use must harm holder's competitive position for commercial value requirement to be met).

However, three considerations support finding independent commercial value for sophisticated prompts.

First, commercial prompt marketplaces demonstrate market recognition of prompts as valuable assets independent of any particular user's access to AI models. PromptBase, launched June 2022, reports over 370,000 users and more than 220,000 prompts available for purchase at prices ranging from $1.99 to $4.99.[^134] FlowGPT offers millions of prompts with community ratings and verification.[^135] ChatX pays up to 39 CAD per successful prompt submission.[^136] Prompts sold on these platforms derive value from their effectiveness across multiple users, each of whom has independent access to the underlying AI service; the prompt's value thus transcends any single user's model access and resides in the optimized formulation itself.

[^134]: PromptBase, 'About PromptBase' <https://promptbase.com/about> accessed 10 November 2025.

[^135]: FlowGPT, 'Community Prompts' <https://flowgpt.com> accessed 10 November 2025.

[^136]: ChatX, 'Prompt Marketplace' <https://chatx.ai/marketplace> accessed 10 November 2025.

Second, specialized prompts that significantly improve output quality or efficiency provide measurable economic benefits. The pharmaceutical example – 60% faster drug candidate identification – represents quantifiable time savings worth potentially millions of euros in accelerated research. The legal analytics firm example – €2.3 million invested in eighteen months of prompt engineering – demonstrates substantial documented development costs that create economic value competitors could misappropriate by copying rather than independently investing.[^137] German courts require objective proof that information has economic value, considering factors including value to the company, development costs, type of information, and importance to competitive position.[^138] Documented investment in prompt development and quantified performance improvements satisfy this standard.

[^137]: See generally Sharon K. Sandeen, 'The Reasonable Secrecy Requirement' in Rochelle C. Dreyfuss and Katherine J. Strandburg (eds), *The Law and Theory of Trade Secrecy: A Handbook of Contemporary Research* (Edward Elgar 2011) 105, 115–118.

[^138]: OLG Düsseldorf (n 119) para 49.

Third, system prompts embedded in proprietary AI applications – instructions that customize how an AI model behaves within a specific application context – can represent substantial engineering investment and provide differentiation among competing products using the same underlying AI model. The automotive manufacturer example – proprietary system prompts customizing Anthropic's models for supply chain optimization – illustrates prompts as valuable business assets independent of mere model access.

The better view distinguishes between simple prompts that any competent user could develop through brief experimentation and sophisticated prompts representing substantial investment in development, testing, and refinement. The distinction parallels established trade secret doctrine protecting customer lists: publicly available contact information does not qualify as a trade secret, but a curated compilation of customers derived from substantial effort, investment, and analysis qualifies as a protectable compilation with commercial value deriving from the compilation itself rather than individual data points.[^139] Similarly, individual prompting techniques may be publicly known, but a refined prompt representing months of optimization, A/B testing, and fine-tuning constitutes a valuable compilation whose "precise configuration and assembly" – Article 2(1)(a)'s language – has commercial value because competitors lack this optimized formulation.

[^139]: Case C-30/14 *Ryanair Ltd v PR Aviation BV* EU:C:2015:10, para 29 (addressing database compilations); applied by analogy to trade secret compilations.

The causal link – "because it is secret" – requires that disclosure would harm the holder's competitive advantage. For AI prompts, this test distinguishes between prompts whose disclosure would enable competitors to immediately replicate valuable outputs and prompts providing minimal competitive benefit. Prompts that codify novel applications, combine techniques in non-obvious ways, or represent substantial optimization work satisfy this requirement because their disclosure allows competitors to appropriate the results of investment without incurring equivalent development costs. Prompts that merely implement widely known techniques or achieve results competitors have independently achieved fail this test – the value does not derive from secrecy because disclosure provides no competitive advantage.

The commercial value element therefore operates as a filter, excluding trivial or widely known prompts while potentially protecting sophisticated prompts representing substantial investment and providing genuine competitive advantages to their holders.

## D. Reasonable Steps under the Circumstances

The third element – that information "has been subject to reasonable steps under the circumstances, by the person lawfully in control of the information, to keep it secret" – requires trade secret holders to exercise what Recital 13 characterizes as a "duty of care as regards the preservation of the confidentiality of their valuable trade secrets."[^140] The "under the circumstances" qualifier establishes that the requirement is context-specific and proportionate, not absolute.[^141]

[^140]: Trade Secrets Directive (n 109) recital 13.

[^141]: European Commission, 'Impact Assessment' (n 131) 21–22.

National courts have developed detailed frameworks for assessing reasonable steps under their implementations of Directive 2016/943. German courts apply the Geschäftsgeheimnisgesetz through a comprehensive three-level framework requiring measures at legal, organizational, and technical levels.[^142] Legal measures include non-disclosure agreements with employees, confidentiality provisions in employment contracts, and contractual restrictions with business partners. Organizational measures include access restrictions, need-to-know policies, classification systems identifying confidential information, employee training on confidentiality obligations, and exit procedures for departing employees. Technical measures include passwords, encryption, access controls, authentication systems, and monitoring for unauthorized access.[^143]

[^142]: Ansgar Ohly, '"Volenti Non Fit Iniuria": The Lawfulness of the Defendant's Acquisition of a Trade Secret as a Defense in Trade Secret Litigation' in Rochelle C. Dreyfuss and Katherine J. Strandburg (eds), *The Law and Theory of Trade Secrecy* (Edward Elgar 2011) 495, 510–515.

[^143]: OLG Düsseldorf (n 119) paras 45–50.

The Higher Regional Court of Düsseldorf established nine factors for proportionality assessment: type of trade secret, specific circumstances of use, value and development costs, nature of information, importance to company, size of company, usual confidentiality measures in the company, type of labeling or marking, and contractual provisions with employees and partners.[^144] This framework emphasizes proportionality – small and medium enterprises need not implement the same expensive security measures as large corporations, but measures must be reasonable given the information's value and the circumstances of its use.

[^144]: ibid para 49.

French courts applying Code de Commerce provisions implementing the Directive emphasize that measures must be specific and targeted rather than blanket designations.[^145] Generic "all information confidential" declarations in employment contracts are insufficient; holders must specifically identify and mark confidential information, document protection measures taken, and implement both technical restrictions and contractual protections.[^146] The Paris Court of Appeal's decisions require demonstrable, implemented protection rather than merely stated policies.[^147]

[^145]: Pascal Kamina, *Film Copyright in the European Union* (2nd edn, Cambridge University Press 2016) 234–237 (discussing French trade secret framework).

[^146]: CA Paris (n 122).

[^147]: ibid.

Dutch courts apply the Wet bescherming bedrijfsgeheimen with particular strictness, exemplified in the pithy formulation that "policy without practice fails the reasonable steps test."[^148] Stated confidentiality policies that employees routinely violate without consequence demonstrate that reasonable steps have not been taken in practice, regardless of written policies. This approach focuses on actual implementation and enforcement rather than formal documentation.

[^148]: Rechtbank Midden-Nederland (n 121).

Applied to AI prompts, these requirements create significant challenges because the fundamental architecture of cloud AI services requires transmitting prompts across networks to third-party providers. The legal analytics firm maintaining NDAs, restricting internal access, and encrypting its prompt library satisfied legal and organizational measures but necessarily transmitted prompts to OpenAI's servers thousands of times daily. The pharmaceutical company's scientists using consumer ChatGPT accounts clearly failed by disclosing prompts without contractual safeguards. The automotive manufacturer storing prompts in encrypted files accessible to only three senior engineers potentially satisfied reasonable steps if, and only if, using Anthropic's enterprise service with contractual confidentiality protections.

The decisive question is whether use of enterprise AI services with contractual confidentiality provisions, combined with internal controls, constitutes "reasonable steps under the circumstances" or whether transmitting prompts to third-party servers fundamentally defeats the requirement. National court guidance on third-party service providers suggests that contractual confidentiality provisions can suffice. The German courts' emphasis on "executed confidential disclosure agreements" implies that properly documented contractual protections with service providers satisfy reasonable steps even though the provider necessarily accesses the information.[^149]

[^149]: OLG Düsseldorf (n 119) para 47.

However, cloud AI services present a structural challenge distinct from traditional third-party relationships. Trade secret law developed in contexts where holders could maintain physical or exclusive digital control over secret information – formulas in locked laboratories, customer lists on access-controlled servers. Cloud AI inverts this model by requiring disclosure to third parties as a condition of using the information at all. The prompt cannot function without transmission to the AI provider's infrastructure; there is no equivalent to maintaining a chemical formula in a secured laboratory while using it in-house.

The resolution depends on whether contractual protections can substitute for exclusive physical control. German courts' proportionality framework suggests they can: the nine-factor test includes "specific circumstances of use" as a factor, indicating that if information's use necessarily requires third-party involvement, reasonable steps must be assessed relative to that constraint rather than requiring impossible exclusive control.[^150] The approach recognizes that in some contexts – cloud computing, outsourced manufacturing, collaborative research – third-party involvement is inherent to using the information, and contractual protections combined with internal controls can satisfy the reasonable steps requirement.

[^150]: ibid para 49.

For AI prompts, reasonable steps therefore require a comprehensive protection program acknowledging the necessity of third-party disclosure while minimizing associated risks:

Legal measures: use exclusively enterprise AI services with documented contractual confidentiality protections; execute non-disclosure agreements with employees and contractors; include confidentiality provisions in employment contracts specifically identifying prompts as confidential; maintain agreements with AI service providers and document their confidentiality terms.

Organizational measures: implement access controls limiting which employees can create and submit prompts; establish classification systems identifying which prompts contain trade secret information; provide employee training on proper use of AI services and the distinction between consumer and enterprise tiers; institute monitoring and audit procedures detecting unauthorized disclosure; establish incident response plans addressing breaches; enforce policies through disciplinary action demonstrating implementation in practice.

Technical measures: encrypt prompts in transit and at rest; implement authentication systems controlling prompt access; sanitize prompts to remove unnecessary sensitive information before submission; monitor AI service usage for compliance; maintain audit logs of prompt submissions; establish technical controls preventing use of consumer AI services on company devices.

This comprehensive framework parallels protections German courts require for traditional trade secrets but adapted to accommodate cloud AI's distributed architecture. The requirement is straightforward doctrinally – reasonable steps must be "under the circumstances," and the circumstances of AI prompt use include technical necessity of third-party processing – but demanding practically, requiring substantial investment in legal, organizational, and technical infrastructure.

The conclusion is that contractual protections with enterprise AI providers, combined with rigorous internal controls, can satisfy Article 2(1)(c)'s reasonable steps requirement. However, the accommodation is conditional and demanding. Businesses must document enterprise service agreements, implement comprehensive internal protection measures, train employees, monitor compliance, and enforce violations. The Dutch principle – "policy without practice fails" – requires demonstrating that stated protections are implemented and enforced in reality, not merely documented on paper.

## E. Synthesis: conditional protection under enterprise frameworks

The CJEU's decision in *Dun & Bradstreet Austria GmbH v Bundeswettbewerbsbehörde* provides authoritative guidance on whether algorithmic information can qualify for trade secret protection under Directive 2016/943.[^142] The Court addressed whether trade secret claims can justify withholding information about automated decision-making logic from data subjects under GDPR transparency obligations. The Court held that controllers must provide "meaningful information about the logic involved" to data subjects, but need not disclose algorithms themselves where doing so would reveal trade secrets.[^143] Austrian law creating a blanket exemption for trade secrets was impermissible; instead, controllers claiming trade secret protection must provide allegedly protected information to supervisory authorities or courts for case-by-case proportionality assessment balancing commercial confidentiality against transparency rights.[^144]

[^142]: Case C-203/22 *Dun & Bradstreet Austria GmbH v Bundeswettbewerbsbehörde* EU:C:2025:144.

[^143]: ibid para 53.

[^144]: ibid paras 58–60.

*Dun & Bradstreet* confirms two principles relevant to prompts. First, algorithmic information – including logical instructions controlling AI system behavior – can in principle qualify as trade secrets; the Court did not categorically exclude computational instructions from protection. Second, trade secret protection is not absolute and must yield to competing fundamental rights and regulatory transparency where proportionality requires. Businesses cannot invoke trade secrecy to avoid disclosure obligations under the GDPR, the AI Act, or sector-specific regulations where transparency outweighs commercial confidentiality.[^145]

[^145]: EUIPO, 'Trade Secrets Litigation Trends in the European Union' (2023) 47–49 (noting developments needed to clarify trade secrets role in data economy and algorithmic transparency contexts).

Applied to prompts, this framework yields a qualified answer. Prompts can qualify as trade secrets, but only sophisticated prompts subjected to rigorous protection measures, and even then subject to potential displacement by regulatory transparency requirements.

The three cumulative requirements create distinct barriers. Under Article 2(1)(a)'s secrecy element, prompts submitted through consumer-tier AI services fail because terms of service authorize provider use for training, defeating the requirement that information be "not readily accessible" to specialists in the field. Only prompts used exclusively through enterprise AI services with contractual prohibitions on provider use or disclosure can potentially satisfy secrecy – the third-party disclosure is unavoidable given cloud architecture, but contractual protections function analogously to employee NDAs in preserving information as "not generally known."[^146]

[^146]: OLG Düsseldorf (n 119) para 47 (requiring "executed confidential disclosure agreements" with third parties).

Under Article 2(1)(b)'s commercial value element, simple prompts that any competent user could develop through brief experimentation fail because they lack the economic value required for protection. Sophisticated prompts representing substantial documented investment – months of optimization, quantified performance improvements, integration into proprietary systems – satisfy this requirement because their disclosure would enable competitors to appropriate development results without incurring equivalent costs. The causal link – "because it is secret" – requires that disclosure would harm competitive position, distinguishing valuable prompt compilations from widely known techniques.[^147]

[^147]: European Commission, 'Impact Assessment' (n 131) 19 (explaining commercial value requires that unauthorized acquisition, use, or disclosure would harm holder's interests).

Under Article 2(1)(c)'s reasonable steps element, cloud AI's distributed architecture creates structural tension. Trade secret law developed assuming holders could maintain exclusive physical or digital control; cloud AI inverts this by requiring third-party disclosure as a condition of use. However, the "under the circumstances" qualifier establishes context-specific proportionality rather than absolute control. Enterprise service agreements prohibiting provider use or disclosure, combined with comprehensive internal measures – access controls, encryption, classification systems, employee training, monitoring, enforcement – can satisfy this requirement. The Dutch principle that "policy without practice fails" demands demonstrable implementation, not merely formal documentation.[^148]

[^148]: Rechtbank Midden-Nederland (n 121).

These three requirements interact to exclude most prompts while potentially protecting a narrow category. Simple prompts fail all three elements. Intermediate prompts representing modest optimization face challenges under reasonable steps proportionality – protective measures may exceed value. Sophisticated prompts representing substantial investment can qualify if, and only if, used exclusively through enterprise services with documented contractual protections and subject to comprehensive internal controls.

The resolution faces unresolved tensions requiring CJEU clarification or legislative guidance. No preliminary ruling has directly interpreted Directive 2016/943's three-part test for algorithmic information. National courts have developed divergent approaches – Germany's nine-factor proportionality framework differs from the Netherlands' stringent practice requirement and France's procedural protections. Cross-border uncertainty will persist until the CJEU addresses whether third-party disclosure with contractual safeguards satisfies secrecy and reasonable steps requirements.[^149]

[^149]: As of November 2025, no CJEU preliminary ruling under TFEU art 267 has addressed core definitional questions under Directive 2016/943 regarding algorithmic or computational information.

More fundamentally, the intersection between trade secret protection and AI transparency requirements under the AI Act remains incompletely theorized. The AI Act imposes transparency obligations on high-risk AI systems including technical documentation, training data disclosure, and deployment logs.[^150] Recital 75 acknowledges that trade secret information "should be safeguarded" but provides no detailed operational guidance on balancing commercial confidentiality against regulatory transparency.[^151] *Dun & Bradstreet* establishes the framework – case-by-case balancing by authorities or courts – but implementing this for AI Act compliance will require either Commission guidance or judicial decisions establishing when transparency obligations override trade secret protection.

[^150]: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence [2024] OJ L184/1 ('AI Act') arts 11–13, 53.

[^151]: ibid recital 75.

AI prompts can qualify as trade secrets under current EU law. The qualification is conditional – requiring sophisticated prompts, enterprise service frameworks, rigorous protective measures, and acceptance that regulatory transparency may require disclosure where fundamental rights or public interest outweigh commercial confidentiality. Trade secret protection for prompts exists doctrinally, but it is demanding, contested, and ultimately provisional pending authoritative interpretation.
## E. Synthesis: When Prompts Qualify as Trade Secrets

The analysis of Directive 2016/943's three-part cumulative test establishes that AI prompts can potentially qualify as trade secrets under EU law, but only under narrow and demanding conditions. The framework requires satisfying all three elements simultaneously – failure on any single element defeats protection entirely.

**Simple prompts categorically fail trade secret protection.** Basic instructions like "Summarize this text" or "Write a marketing email" do not meet the secrecy requirement because they are generally known among AI users; they lack commercial value because any competent user can develop them through minimal experimentation; and they cannot justify the substantial protective measures required for reasonable steps given their minimal value. These prompts resemble individual publicly available facts – they may have utility, but they do not constitute protectable information under trade secret law.

**Intermediate prompts representing modest optimization face significant obstacles.** Domain-specific queries, tested formulations that improve reliability, or structured templates that standardize outputs might satisfy the commercial value element if they represent genuine efficiency improvements. However, they face challenges under the secrecy element if widely shared within professional communities, and they struggle under the reasonable steps requirement because the investment required to protect them through comprehensive legal, organizational, and technical measures may exceed their value, failing the proportionality test. Moreover, the high probability of independent discovery for intermediate prompts – any competent practitioner working in the same domain will likely develop similar approaches through parallel experimentation – undermines claims that value derives from secrecy rather than from general domain expertise.

**Sophisticated prompts representing substantial investment can potentially qualify as trade secrets if subjected to rigorous protection measures.** These prompts must satisfy four cumulative conditions:

First, **exclusive use through enterprise AI services** with documented contractual confidentiality provisions. Consumer-tier services with terms permitting training use categorically defeat the secrecy requirement. Enterprise agreements must contractually prohibit the provider from using prompts for model training, from disclosing prompts to other customers, and from accessing prompts except as necessary to process the specific user's requests. The agreements must be documented, maintained, and periodically reviewed to ensure continued compliance.

Second, **substantial documented investment** in prompt development creating quantifiable economic benefits. This includes documented development costs (specialist salaries, testing expenses, computational resources), quantified performance improvements (efficiency gains, quality metrics, competitive advantages), and evidence that competitors could misappropriate these benefits by copying rather than independently investing. German courts' emphasis on objective proof of economic value requires documentation beyond mere assertions of worth.

Third, **comprehensive internal protection measures** spanning legal, organizational, and technical domains. Legal measures must include non-disclosure agreements with employees and contractors, employment contract provisions specifically identifying prompts as confidential, and documented agreements with AI service providers. Organizational measures must include access controls limiting who can create and submit prompts, classification systems identifying trade secret prompts, employee training on proper AI service use, monitoring and audit procedures, incident response plans, and enforcement through disciplinary action. Technical measures must include encryption in transit and at rest, authentication systems, prompt sanitization, usage monitoring, audit logging, and controls preventing consumer service use. The Dutch "policy without practice fails" principle requires demonstrating actual implementation and enforcement, not merely written policies.

Fourth, **limited disclosure scope** minimizing the risk that prompts become "readily accessible" through reconstruction or observation. Prompts whose effectiveness can be easily reverse-engineered from publicly available outputs face substantial risk that the secrecy element will fail because competitors can lawfully reconstruct them through observation and testing under Article 3(1)(b). Prompts used in contexts where outputs are publicly visible must be evaluated for whether skilled competitors could reconstruct similar prompts through analysis – if reconstruction is feasible, secrecy may be defeated regardless of internal protective measures.

The practical reality is that **trade secret protection for AI prompts is feasible but fragile**. Protection exists in principle but requires continuous vigilance, substantial investment in protection infrastructure, and acceptance that protection remains provisional. Three structural vulnerabilities limit trade secret protection's effectiveness for prompts.

First, **the reverse engineering vulnerability**. Article 3(1)(b) explicitly permits acquisition through "observation, study, disassembly or testing of a product or object that has been made available to the public."[^151] Academic research demonstrates that prompts can be reconstructed from analyzing AI outputs, and this reconstruction constitutes lawful acquisition that trade secret law cannot prevent. Businesses relying on trade secret protection must accept that competitors engaging in systematic reverse engineering commit no violation.

[^151]: Trade Secrets Directive (n 109) art 3(1)(b).

Second, **the independent discovery vulnerability**. Article 3(1)(a) protects "independent discovery or creation" as lawful acquisition.[^152] Prompt engineering requires no specialized equipment, substantial capital investment, or rare expertise. The barrier to independent discovery is relatively low compared to paradigmatic trade secrets like chemical formulas or manufacturing processes. Businesses must accept that competitors may independently develop similar or functionally equivalent prompts through parallel experimentation, and such independent development defeats any trade secret claim regardless of the holder's investment.

[^152]: ibid art 3(1)(a).

Third, **the employee mobility tension**. Article 1(3) emphasizes that trade secret protection "should not offer any ground for restricting the mobility of employees" and explicitly protects "employees' use of experience and skills honestly acquired in the normal course of their employment."[^153] When employees develop prompt engineering expertise while working for one company, they retain the right to use that general skill at subsequent employers. The boundary between protectable specific prompts and unprotectable general prompt engineering skills remains unclear and fact-intensive. Former employees arguing they merely applied general skills rather than copied specific prompts present difficult cases that may require litigation to resolve.

[^153]: ibid art 1(3); recital 13.

These three vulnerabilities mean that trade secret protection for prompts provides weaker and more contingent protection than for traditional trade secrets like chemical formulas or customer lists. The protection is real but limited – it prevents misappropriation through unlawful means (breach of confidentiality agreements, hacking, inducement of breach) but cannot prevent acquisition through lawful means (reverse engineering, independent discovery, employee mobility with general skills).

**The Court of Justice has not yet addressed these issues.** Directive 2016/943 entered into force in June 2016 with Member State transposition required by June 2018, but as of November 2025, no CJEU preliminary ruling under Article 267 TFEU has interpreted the Directive's core provisions as applied to AI prompts or cloud computing contexts. The analysis above synthesizes national court decisions from Germany, France, and the Netherlands applying their respective implementations, but these decisions may diverge in emphasis and application. Cross-border uncertainty persists until the CJEU provides authoritative interpretation.[^154]

[^154]: EUIPO, 'Trade Secrets Litigation Trends in the EU Member States' (2023) 47–52 (documenting divergent national approaches to reasonable steps assessment).

The regulatory landscape adds further complexity. The AI Act imposes transparency obligations on high-risk AI systems including technical documentation, training data disclosure, and deployment logging.[^155] These transparency requirements may conflict with trade secret confidentiality, requiring case-by-case balancing. The CJEU's decision in *Dun & Bradstreet Austria* established that trade secret protection can justify withholding algorithmic information from data subjects but not from supervisory authorities or courts conducting proportionality assessments.[^156] This framework – acknowledging trade secret protection while requiring disclosure where fundamental rights or regulatory transparency obligations outweigh commercial confidentiality – will likely govern conflicts between prompt trade secrets and AI Act transparency requirements.

[^155]: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence [2024] OJ L184/1 ('AI Act'), arts 11–13, 53.

[^156]: Case C-203/22 *CK and Dun & Bradstreet Austria GmbH* EU:C:2024:173, paras 55–62.

**Practical guidance for businesses** seeking to protect prompt engineering work through trade secrets requires implementing the comprehensive framework described above while accepting its limitations. Use exclusively enterprise AI services with verified contractual confidentiality provisions; prohibit consumer service use for any confidential prompts; document all service agreements and maintain evidence of confidentiality terms; implement access controls, classification systems, employee training, and monitoring procedures; encrypt prompts in transit and at rest; sanitize prompts to remove unnecessary sensitive information; maintain audit logs; enforce violations through disciplinary action demonstrating implementation in practice; accept that reverse engineering and independent discovery remain lawful and cannot be prevented; prepare for potential conflicts with transparency requirements under the GDPR, AI Act, or other regulatory frameworks; and recognize that trade secret protection, while real, provides weaker and more contingent protection than copyright or patent monopolies.

Trade secrets represent the most viable intellectual property protection mechanism for AI prompts under current EU law, but the protection is conditional, demanding, and ultimately provisional. It exists for sophisticated prompts subjected to rigorous protection measures, but even then remains vulnerable to lawful acquisition through reverse engineering, independent discovery, and employee mobility. The legal framework accommodates prompt protection within existing doctrine, but businesses must invest substantially in protection infrastructure and accept substantial residual risk that protection will prove inadequate in contested cases.
