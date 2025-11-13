# VI. Trade Secrets

## A. The Directive 2016/943 Framework

Copyright, software, database, and patent protections all fail to accommodate prompts' functional character and instructional nature. Trade secrets offer a fundamentally different protection mechanism – one based on secrecy rather than creativity or technical innovation. Directive (EU) 2016/943 on the protection of undisclosed know-how and business information, adopted 8 June 2016 with Member State transposition required by 9 June 2018, harmonizes trade secret protection across the European Union by establishing minimum standards for civil remedies against unlawful acquisition, use, and disclosure.[^109]

[^109]: Directive (EU) 2016/943 of the European Parliament and of the Council of 8 June 2016 on the protection of undisclosed know-how and business information (trade secrets) against their unlawful acquisition, use and disclosure [2016] OJ L157/1 ('Trade Secrets Directive').

The Directive implements the EU's obligations under Article 39 of the TRIPS Agreement, which requires WTO members to protect undisclosed information that is secret, has commercial value because it is secret, and has been subject to reasonable steps to maintain secrecy.[^110] Article 2(1) of Directive 2016/943 defines "trade secret" through a three-part cumulative test requiring that information: "(a) it is secret in the sense that it is not, as a body or in the precise configuration and assembly of its components, generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question; (b) it has commercial value because it is secret; (c) it has been subject to reasonable steps under the circumstances, by the person lawfully in control of the information, to keep it secret."[^111]

[^110]: TRIPS Agreement (n 14) art 39(2).

[^111]: Trade Secrets Directive (n 109) art 2(1).

This definition remained essentially unchanged from the European Commission's November 2013 proposal through final adoption in June 2016, demonstrating consensus that the TRIPS Article 39 formulation provides an appropriate international standard.[^112] The three requirements are cumulative – failure to satisfy any single element defeats trade secret status entirely. Recital 14 emphasizes that the definition "should cover know-how, business information and technological information where there is both a legitimate interest in keeping them confidential and a legitimate expectation that such confidentiality will be preserved."[^113]

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

This analysis yields a bright-line rule for prompts: only prompts used exclusively through enterprise AI services with robust contractual confidentiality provisions can potentially satisfy the secrecy requirement. Prompts submitted through consumer-tier services without such protections fail Article 2(1)(a) and cannot qualify as trade secrets under EU law.

The rule reflects the structural reality that cloud AI architecture requires third-party disclosure. Trade secret law accommodates such disclosure where contractual safeguards substitute for exclusive physical control. But the accommodation is conditional – the contractual protections must be documented, the enterprise service tier must be deliberately selected rather than defaulting to consumer services, and internal controls must ensure employees comply with the requirement to use only protected services.

Businesses maintaining prompt libraries as trade secrets must therefore implement strict policies: prohibit use of consumer AI services for any prompts containing confidential information; require use only of enterprise services with verified contractual confidentiality provisions; document service agreements and maintain evidence of their terms; train employees on the distinction between consumer and enterprise tiers; monitor compliance through technical controls and audit procedures; and enforce violations through disciplinary measures demonstrating that policies are implemented in practice, not merely stated on paper.
