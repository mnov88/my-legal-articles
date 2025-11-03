# AI Service Contracts: Performance Guarantees and Disclaimers

Major AI service providers universally disclaim warranties for model performance, accuracy, and output quality while limiting remedies to service credits for uptime failures. These contracts reveal a striking pattern: extensive "as-is" disclaimers paired with narrow availability SLAs that explicitly exclude the performance characteristics customers care most about.

The contractual landscape establishes that **availability ≠ performance**. Providers guarantee systems will be reachable 99.9% of the time but make no commitments that outputs will be accurate, useful, or consistent. This fundamental asymmetry places all model performance risk squarely on customers. Across every major provider examined—OpenAI, Microsoft, Google, AWS, Anthropic, Cohere, Hugging Face, and Stability AI—the warranty structure follows this pattern: robust infrastructure SLAs paired with comprehensive quality disclaimers. Understanding these terms is critical for organizations deploying AI systems, as standard contracts offer essentially no recourse for model degradation, hallucinations, or output quality issues.

## Performance guarantees across major providers

### OpenAI: Minimal warranties and no public SLA

OpenAI provides the most limited performance commitments among major providers. The company offers no publicly available SLA for standard API services, making it the only major cloud AI provider without uptime guarantees in standard terms.

**Limited warranty scope (OpenAI Business Terms, Section 9.1):**

> "We warrant that, during the Term, when used in accordance with this Agreement, the Services will conform in all material respects with the documentation we provide to you or otherwise make publicly available."

This narrow warranty simply promises the service will work as described in documentation—not that it will work well, accurately, or consistently. **The warranty contains no performance metrics, accuracy thresholds, or quality standards.**

**Customer responsibility for output accuracy (Services Agreement, Section 3.3):**

> "You are solely responsible for all use of the Outputs and evaluating the Output for accuracy and appropriateness for your use case, including by utilizing human review as appropriate."

OpenAI explicitly transfers all accuracy evaluation responsibility to customers. The company makes no representations about whether outputs are correct, appropriate, or fit for any particular purpose. This provision appears in both business and consumer terms, establishing that human review is the customer's obligation, not OpenAI's guarantee.

**Output similarity acknowledgment (Services Agreement, Section 3.4):**

> "You acknowledge that due to the nature of our Services and artificial intelligence generally, Output may not be unique and other users may receive similar content from our services."

This clause acknowledges the non-deterministic nature of AI systems while disclaiming any uniqueness guarantees. Customers accept that identical queries may produce identical or similar outputs across different users—a reality of the technology that nonetheless eliminates any warranty of customized or unique results.

**Beta services treatment (Service Terms):**

> "Beta Services are offered 'as-is' to allow testing and evaluation and are excluded from any indemnification obligations OpenAI may have to you. OpenAI makes no representations or warranties for Beta Services, including any warranty that Beta Services will be generally available, uninterrupted or error-free, or that Content will be secure or not lost or damaged."

Beta features receive even broader disclaimers. OpenAI explicitly disclaims **all** warranties—express, implied, or statutory—for beta offerings, including merchantability, fitness for particular purpose, and non-infringement. Customers using beta features accept they may never become generally available and could be discontinued without notice.

### Microsoft Azure OpenAI: Infrastructure SLAs without model performance guarantees

Microsoft distinguishes itself by offering the most comprehensive infrastructure SLAs while still disclaiming model accuracy warranties. Azure's approach recognizes enterprise customers demand predictability—but only for availability, not quality.

**Availability guarantees (Azure OpenAI Service):**

> "We guarantee that Azure OpenAI will be available at least 99.9% of the time."

This represents a **99.9% uptime SLA**—the highest level commitment among AI providers. Microsoft calculates availability using 5-minute intervals across each monthly billing cycle.

**Latency SLA for provisioned throughput (Microsoft Azure Blog, October 2024):**

> "Enterprises depend on predictability, especially when deploying mission-critical applications. That's why we're introducing a 99% latency service level agreement for token generation. This latency SLA ensures that tokens are generated at faster and more consistent speeds, especially at high volumes."

Microsoft's latency SLA represents the **most specific performance guarantee in the industry**, but applies only to Provisioned Throughput Units (PTU)—a premium tier requiring substantial minimum commitments. The standard pay-per-token model has no latency guarantees.

**Service credit remedy (SLA for Cognitive Services):**

> "We provide financial backing to our commitment to achieve and maintain Service Levels for our Services. If we do not achieve and maintain the Service Levels for each Service as described in this SLA, then you may be eligible for a credit towards a portion of your monthly service fees."

Service credits are calculated as follows:
- **99% to <99.9% uptime**: 10% credit
- **95% to <99% uptime**: 25% credit  
- **<95% uptime**: 50% credit

Critically, these credits constitute the **sole contractual remedy**. Customers cannot pursue additional damages or refunds regardless of business impact.

**Preview services disclaimer (Product Terms):**

> "PREVIEWS ARE PROVIDED 'AS-IS,' 'WITH ALL FAULTS,' AND 'AS AVAILABLE,' as described herein. Unless otherwise noted in a separate agreement, Previews are not included in the SLA for the corresponding Online Service, and may not be covered by customer support."

Preview features explicitly fall outside SLA coverage. Microsoft reserves the right to change or discontinue previews "at any time without notice" and may choose never to make them generally available.

**Azure Direct Models in Preview warning (Preview Supplemental Terms):**

> "Models in Preview may exhibit unexpected behavior, which may include higher risks of producing potentially harmful content and/or greater susceptibility to jailbreaking. Customers should exercise due caution in using Preview models, and are responsible for reviewing model descriptions in Azure AI Foundry, model cards made available by the model provider, and documentation for Preview models."

This provision acknowledges that preview models carry elevated risks but places responsibility for appropriate safeguards on customers.

**High-risk use disclaimer (Product Terms):**

> "WARNING: Modern technologies, and especially platform technologies, may be used in new and innovative ways, and Customer must consider whether its specific use of these technologies is safe. The Online Services are not designed or intended to support any use in which a service interruption, defect, error, or other failure of an Online Service could result in the death or serious bodily injury of any person or in physical or environmental damage (collectively, 'High-Risk Use')."

Microsoft explicitly disclaims suitability for high-risk applications. Customers deploying in safety-critical contexts do so "at their own risk" with no warranty that services are appropriate for such use. The contract continues:

> "Customer must design and implement every application such that, in the event of any interruption, defect, error, or other failure of the Online Service, the safety of people, property, and the environment are not reduced below a level that is reasonable, appropriate, and legal."

**Medical device disclaimer (Product Terms):**

> "Customer acknowledges that the Online Services (1) are not designed, intended or made available as a medical device(s), and (2) are not designed or intended to be a substitute for professional medical advice, diagnosis, treatment, or judgment and should not be used to replace or as a substitute for professional medical advice, diagnosis, treatment, or judgment."

Healthcare applications receive specific disclaimers establishing services are not medical devices and cannot substitute for professional medical judgment.

**No model accuracy guarantees:**

Microsoft's terms notably contain **no explicit warranties regarding AI model accuracy, output quality, or performance consistency**. Third-party analysis confirms: "Microsoft's terms include disclaimers that the service is provided 'as-is' and that they do not guarantee the AI's output accuracy."

**Model update rights (Product Terms):**

> "Microsoft may make commercially reasonable changes to each Online Service from time to time. Microsoft may modify or terminate an Online Service in any country where Microsoft is subject to a government regulation, obligation or other requirement that (1) is not generally applicable to businesses operating there, (2) presents a hardship for Microsoft to continue operating the Online Service without modification, and/or (3) causes Microsoft to believe these terms or the Online Service may conflict with any such requirement or obligation."

Microsoft reserves broad rights to modify or terminate services, particularly in response to regulatory requirements. Customers have no contractual guarantee of specific model versions remaining available.

**Capacity limitations (Product Terms):**

> "Excessive use of a Microsoft Generative AI Service may result in temporary throttling of Customer's access to the Microsoft Generative AI Service."

Usage may be throttled without constituting an SLA breach—availability guarantees don't prevent Microsoft from limiting access based on consumption patterns.

### Google Cloud Vertex AI: Tiered SLAs with extensive exclusions

Google offers the most granular SLA structure, with different guarantees for different service types. However, like all providers, these commitments cover only availability, not model performance.

**Service level objectives (Vertex AI SLA):**

> "During the Term of the agreement under which Google has agreed to provide Google Cloud Platform to Customer (as applicable, the 'Agreement'), the Covered Service will provide a Monthly Uptime Percentage to Customer as follows (the 'Service Level Objective' or 'SLO'):
>
> Covered Service | Monthly Uptime Percentage
> Training, Deployment, and Batch Prediction | >= 99.9%
> AutoML Tabular and AutoML Image Online Prediction for models deployed on 2 or more nodes | >= 99.9%
> AutoML Text Language Online Prediction | >= 99.9%
> Custom Model Online Prediction for models deployed on 2 or more nodes | >= 99.5%
> Vertex Pipelines | >= 99.5%"

Google's SLA structure creates performance tiers based on deployment architecture. **Single-node deployments receive no SLA coverage**, incentivizing customers to architect for redundancy.

**Financial credit schedule (Vertex AI SLA):**

> "Financial Credit' means the following for Training, Deployment, and Batch Prediction; AutoML Tabular and AutoML Image Online Prediction for models deployed on 2 or more nodes; or AutoML Text Language Online Prediction:
>
> Monthly Uptime Percentage | Percentage of monthly bill that will be credited
> 99% to <99.9% | 10%
> 95% to <99% | 25%
> <95% | 50%"

Credit percentages match Microsoft's structure but apply only to affected service components.

**Sole remedy clause (Vertex AI SLA):**

> "This SLA states Customer's sole and exclusive remedy for any failure by Google to meet the SLO."

Like all major providers, Google limits remedies to service credits with no additional liability.

**SLA exclusions (Vertex AI SLA):**

> "The SLA does not apply to any (a) features designated pre-general availability (unless otherwise stated in the associated Documentation); (b) features excluded from the SLA (in the associated Documentation); or (c) errors (i) caused by factors outside of Google's reasonable control; (ii) that resulted from Customer's software or hardware or third party software or hardware, or both; (iii) that resulted from abuses or other behaviors that violate the Agreement; (iv) that resulted from quotas applied by the system or listed in the Admin Console; or **(v) that resulted from Customer use of the Covered Service inconsistent with the Documentation, including but not limited to invalid request fields, unauthorized users, inaccessible data, or use of a model that is beyond the recommended model lifespan described in the applicable Documentation.**"

The emphasized provision creates a critical loophole: **Google can effectively disclaim SLA coverage if customers use models beyond their "recommended model lifespan."** This means model degradation over time may not constitute an SLA breach if Google has documented a recommended refresh schedule.

### Google Gemini API: Experimental technology disclaimers

Google's consumer-facing Gemini API contains the most explicit experimental technology warnings.

**Experimental technology disclaimer (Gemini API Additional Terms, May 20, 2025):**

> "Disclaimers. The Services include experimental technology and may sometimes provide inaccurate or offensive content that doesn't represent Google's views. Use discretion before relying on, publishing, or otherwise using content provided by the Services. Don't rely on the Services for medical, legal, financial, or other professional advice. Any content regarding those topics is provided for informational purposes only and is not a substitute for advice from a qualified professional."

Google explicitly characterizes Gemini as "experimental technology" that "may sometimes provide inaccurate or offensive content." Users are warned not to rely on outputs for professional advice in any regulated domain.

**Data use for unpaid services (Gemini API Additional Terms):**

> "When you use Unpaid Services, including, for example, Google AI Studio and the unpaid quota on Gemini API, Google uses the content you submit to the Services and any generated responses to provide, improve, and develop Google products and services and machine learning technologies, including Google's enterprise features, products, and services, consistent with our Privacy Policy."

**Human review of content (Gemini API Additional Terms):**

> "To help with quality and improve our products, human reviewers may read, annotate, and process your API input and output. Google takes steps to protect your privacy as part of this process. This includes disconnecting this data from your Google Account, API key, and Cloud project before reviewers see or annotate it. **Do not submit sensitive, confidential, or personal information to the Unpaid Services.**"

Free tier users must accept that human reviewers will examine their inputs and outputs. Google explicitly warns against submitting confidential information to unpaid tiers.

**Data use for paid services (Gemini API Additional Terms):**

> "When you use Paid Services, including, for example, the paid quota of the Gemini API, Google doesn't use your prompts (including associated system instructions, cached content, and files such as images, videos, or documents) or responses to improve our products, and will process your prompts and responses in accordance with the Data Processing Addendum for Products Where Google is a Data Processor."

Paid tiers receive stronger data protections—Google commits not to use customer data for model improvement. This represents a **critical distinction between free and enterprise tiers**.

### AWS Bedrock and SageMaker: Comprehensive SLA framework

AWS offers the most mature SLA infrastructure with separate agreements for different AI services.

**Amazon Bedrock service commitment (Amazon Bedrock SLA, October 4, 2023):**

> "AWS will use commercially reasonable efforts to make Amazon Bedrock available with the Monthly Uptime Percentages set forth in the table below, for each AWS region, during any monthly billing cycle (the 'Service Commitment'). In the event Amazon Bedrock does not meet the Service Commitment, you will be eligible to receive a Service Credit as described below."

**Service credit schedule (Amazon Bedrock SLA):**

> "Service Credits are calculated as a percentage of the total charges paid by you for Amazon Bedrock in the affected AWS region for the monthly billing cycle in which the Service Commitment was not met, in accordance with the schedule below:
>
> Monthly Uptime Percentage | Service Credit Percentage
> Less than 99.9% but >= 99.0% | 10%
> Less than 99.0% but >= 95.0% | 25%
> Less than 95.0% | 100%"

AWS offers the most generous credit structure, with **100% credit (full refund) for availability below 95%**—higher than Google's 50% maximum.

**Sole remedy clause (Amazon Bedrock SLA):**

> "Unless otherwise provided in the Agreement, your sole and exclusive remedy for any unavailability, non-performance, or other failure by us to provide Amazon Bedrock is the receipt of a Service Credit (if eligible) in accordance with the terms of this SLA."

**SLA exclusions (Amazon Bedrock SLA):**

> "The Service Commitment does not apply to any unavailability, suspension, or termination of Amazon Bedrock, or any other Amazon Bedrock performance issues: (i) caused by factors outside of our reasonable control, including any force majeure event or Internet access or related problems beyond the demarcation point of Amazon Bedrock; (ii) that result from any actions or inactions by you (e.g. scaling of provisioned throughput, VPC configurations or credential settings, disabling encryption keys or making the encryption keys inaccessible, etc.); (iii) that result from you not following the guidelines and best practices described in the Amazon Bedrock technical documentation on the AWS Site; (iv) that result from your equipment, software or other technology; (v) arising from our suspension or termination of your right to use Amazon Bedrock in accordance with the Agreement; or **(vi) caused by underlying software that leads to repeated model crashes or an inoperable model**."

The emphasized exclusion is critical: **AWS explicitly excludes from SLA coverage scenarios where underlying model software causes crashes or becomes inoperable.** This means model-level failures may not trigger SLA credits even if the infrastructure remains available.

**Amazon SageMaker differentiated SLAs (Amazon SageMaker SLA, May 4, 2022):**

SageMaker offers distinct guarantees based on workload type:

> "For Online Inference:
> Monthly Uptime Percentage | Service Credit Percentage
> Less than 99.95% but >= 99% | 10%
> Less than 99% | 25%
> Less than 95% | 100%
>
> For Batch Transform:
> Monthly Uptime Percentage | Service Credit Percentage
> Less than 99.9% but >= 99% | 10%
> Less than 99% | 25%
> Less than 95% | 100%"

Online inference receives AWS's highest SLA at **99.95% uptime**—the strongest availability commitment in the industry.

**AI Services output ownership (AWS Service Terms, Section 50.2):**

> "The output that you generate using AI Services is Your Content. Due to the nature of machine learning, output may not be unique across customers and the Services may generate the same or similar results across customers."

AWS clearly establishes customer ownership of outputs while disclaiming uniqueness—identical prompts may produce identical results across different customers.

**Hazardous use disclaimer (AWS Service Terms, Section 50.6):**

> "AI Services are not intended for use in, or in association with, the operation of any hazardous environments or critical systems that may lead to serious bodily injury or death or cause environmental or property damage. AI Services may be used in connection with supporting healthcare services but are not medical devices and are not intended to be used by themselves for any clinical decision-making or other clinical use."

AWS explicitly excludes safety-critical applications and medical decision-making from intended use cases.

### Anthropic (Claude): Strong disclaimers with customer notification requirements

Anthropic's terms emphasize customer responsibility to notify end users about output limitations.

**Output evaluation responsibility (Anthropic Commercial Terms):**

> "It is Customer's responsibility to evaluate whether Outputs are appropriate for Customer's use case, including where human review is appropriate, before using or sharing Outputs. Customer acknowledges, and must notify its Users, that factual assertions in Outputs should not be relied upon without independently verifying their accuracy."

Anthropic uniquely requires customers to **notify their end users** that outputs shouldn't be relied upon without verification. This creates a contractual obligation to warn downstream users—a provision not found in most competitor agreements.

**Comprehensive warranty disclaimer (Anthropic Commercial Terms, Section K.2):**

> "EXCEPT TO THE EXTENT EXPRESSLY PROVIDED FOR IN THESE TERMS, TO THE MAXIMUM EXTENT PERMITTED UNDER LAW (A) THE SERVICES AND OUTPUTS ARE PROVIDED 'AS IS' AND 'AS AVAILABLE' WITHOUT WARRANTY OF ANY KIND; AND (B) ANTHROPIC MAKES NO WARRANTIES, EXPRESS OR IMPLIED, RELATING TO THIRD-PARTY PRODUCTS OR SERVICES, INCLUDING THIRD-PARTY INTERFACES. ANTHROPIC EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES, INCLUDING WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE, AS WELL AS ANY IMPLIED WARRANTY ARISING FROM STATUTE, COURSE OF DEALING OR PERFORMANCE, OR TRADE USE. **ANTHROPIC DOES NOT WARRANT, AND DISCLAIMS THAT, THE SERVICES OR OUTPUTS ARE ACCURATE, COMPLETE OR ERROR-FREE OR THAT THEIR USE WILL BE UNINTERRUPTED.**"

The bolded language explicitly disclaims accuracy, completeness, and error-free operation—the exact qualities most customers need.

**Limitation of liability (Anthropic Commercial Terms, Section K.3):**

> "Except as stated in Section K.3.b, the liability of each Party, and its affiliates and licensors, for any damages arising out of or related to these Terms (i) excludes damages that are consequential, incidental, special, indirect, or exemplary damages, including lost profits, business, contracts, revenue, goodwill, production, anticipated savings, or data, and costs of procurement of substitute goods or services and (ii) is limited to Fees actually paid by Customer for the Services in the previous 12 months."

Liability caps at **12 months of fees paid**, excluding all consequential damages including lost profits, business, and data.

**Service suspension rights:**

> "Anthropic will use reasonable efforts to provide written notice of any Service Suspension to Customer, and resume providing access to the Services, as soon as reasonably possible after the event giving rise to the Service Suspension is cured, where curable. Anthropic will have no liability for any damage, liabilities, losses (including any loss of data or profits), or any other consequences that Customer may incur because of a Service Suspension."

Anthropic can suspend services with "reasonable efforts" to notify, accepting **no liability for consequences** including data loss or business interruption.

### Cohere: Model deprecation and lifecycle management

Cohere provides the most explicit model lifecycle documentation.

**Model deprecation policy (Cohere Deprecations Documentation):**

> "As Cohere launches safer and more capable models, we will regularly retire old models. Applications relying on Cohere's models may need occasional updates to keep working. Impacted customers will always be notified via email and in our documentation along with blog posts. Once a model is deprecated, it is imperative to migrate all usage to a suitable replacement before the shutdown date. Requests to models and endpoints past the shutdown date will fail."

Cohere explicitly warns that **model deprecation is regular practice**. Customers must actively migrate to new models or face service failures. This represents the most transparent deprecation communication among providers, though still without performance guarantees for replacement models.

**Data handling (Cohere Enterprise Data Commitments):**

> "Enterprise customers can access opt out flags in the Cohere dashboard settings. If you are opted out, prompts and generations are not used to train Cohere models. We automatically delete logged prompts and generations after 30 days, unless we need it to comply with a legal requirement or customer contract, or unless your usage is flagged as potentially violating our terms, including our Usage Policy (e.g. abuse or misuse of our services)."

Cohere provides clear data retention policies with opt-out capabilities for enterprise customers, distinguishing it from some competitors' less explicit policies.

### Hugging Face: Comprehensive disclaimers for open ecosystem

Hugging Face's terms address both hosted services and models from third-party contributors.

**Disclaimer of warranties (Hugging Face Terms of Service, September 15, 2022):**

> "We provide Services that you may or may not decide to access, use or purchase. In this regard, we make no warranties or representations about these Services. In other words, except as expressly provided otherwise herein, and to the fullest extent permitted by law, the Services and Content are provided 'as is' and 'as available'. We disclaim all warranties or guarantees of any kind, express or implied, whether arising under any law or from any usage in trade, or otherwise, including but not limited to the implied warranties of merchantability, non-infringement, quiet enjoyment, fitness for a particular purpose, or otherwise. **We further disclaim all warranties or guarantees about the accuracy, reliability or benefits of any Services, artificial intelligence, Models or any other technology or Content, or that the Services or Content will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise.**"

The emphasized language disclaims accuracy and reliability warranties for "artificial intelligence, Models or any other technology"—directly addressing AI-specific concerns.

**Customer sole responsibility:**

> "You will be solely responsible for any damage resulting from your use of or access to the Services, your downloading of Content or data, or use of any other material provided by or through the Services."

Hugging Face places complete responsibility for outputs on users, consistent with its open model repository approach.

**Limitation of liability (Hugging Face Terms):**

> "Neither of us (or any of our affiliates, subsidiaries, contractors, licensors, officers, directors, agents, or employees ('Related Parties')) will be liable for any indirect, incidental, consequential, punitive, special, or other similar damages, including loss of revenue, profits, data, benefits, or savings, whether or not due to the fault or negligence of the company or related parties, and regardless of whether either of us or our related parties have been advised of the possibility of such damages or losses. Either Party's (and each Related Party's) aggregate liability to the other Party or any third party in any circumstance will not exceed the amount that you paid us during the 12-month period immediately preceding the last claim **(or $50 if relating to a free service)**."

The $50 minimum liability cap for free services effectively eliminates meaningful recourse for users of Hugging Face's free tier.

**Service modification rights:**

> "We may at any time modify, suspend, or discontinue, temporarily or permanently, the Services (or any part thereof) with or without notice. You agree that we will not be liable to you or to any third party for any modification, suspension or discontinuance of the Services."

Hugging Face retains absolute discretion to modify or discontinue services without notice or liability.

### Stability AI: Strongest warnings about critical decision-making

Stability AI includes the most explicit warnings against relying on outputs for important decisions.

**Reliance on outputs warning (Stability AI Terms, Section 4.b):**

> "Generative artificial intelligence is technology that is still developing and Outputs may not always contain accurate information or be as you intended. **You are solely responsible for verifying the accuracy, legality, and appropriateness of any Outputs before using or sharing them. Outputs should not be used for any critical decisions without independent human review.** Please also note that Outputs are not created by Stability and do not reflect Stability's views."

The emphasized language explicitly prohibits using outputs "for any critical decisions without independent human review"—the strongest cautionary language among major providers.

**Disclaimer of warranties (Stability AI Terms, Section 11):**

> "OUR SERVICES ARE PROVIDED 'AS IS' AND, TO THE EXTENT PERMISSIBLE UNDER APPLICABLE LAW, WITHOUT WARRANTIES, (WHETHER EXPRESS, IMPLIED, OR STATUTORY). WE AND OUR PROVIDERS EXPRESSLY DISCLAIM ALL WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, TITLE, MERCHANTABILITY, ACCURACY, SATISFACTORY QUALITY, AVAILABILITY, RELIABILITY, QUIET ENJOYMENT, SECURITY, PRIVACY, COMPATIBILITY, NON-INFRINGEMENT, AND ANY WARRANTY IMPLIED BY COURSE OF DEALING, COURSE OF PERFORMANCE, OR TRADE USAGE. **WE DO NOT WARRANT THAT ANY INPUT OR OUTPUT WILL BE SECURE OR NOT LOST OR ALTERED. YOUR USE OF OUR SERVICES AND INPUTS / OUTPUTS IS SOLELY AT YOUR OWN RISK.**"

**Limitations of liability (Stability AI Terms, Section 11):**

> "TO THE EXTENT PERMISSIBLE UNDER APPLICABLE LAW, THE STABILITY PARTIES' TOTAL AGGREGATE LIABILITY TO YOU FOR ALL DAMAGES, LOSSES AND CAUSES OF ACTION ARISING OUT OF OR RELATED TO OUR SERVICES, THE INPUTS / OUTPUTS, OR THESE TERMS, WHETHER IN CONTRACT, TORT, NEGLIGENCE, OR OTHER, WILL NOT EXCEED THE GREATER OF $100 OR THE AMOUNT YOU PAID FOR ACCESSING OUR SERVICES IN THE SIX MONTHS BEFORE THE DATE SUCH DAMAGES, LOSSES, AND CAUSES OF ACTION FIRST AROSE."

Liability caps at the **greater of $100 or 6 months of fees**—the lowest among major providers (most use 12 months).

**Service modification rights (Stability AI Terms, Section 12.a):**

> "We may periodically update our Services, including add or remove features or Services, without advance notice. Unless we specifically agree otherwise in a separate agreement, we reserve the right to modify or discontinue our Services in our discretion and without advance notice. We will not be liable for any changes to our Services."

Stability AI reserves the right to modify or discontinue services "without advance notice" and accepts no liability for such changes.

**Termination rights (Stability AI Terms, Section 12.e):**

> "We may also suspend or terminate your access to our Services (including any subscriptions) at any time without advance notice, particularly if we believe that you have breached these Terms or if we must do so to comply with applicable law... If we terminate your access to our Services due to a violation of these Terms and you have a subscription, you will not be entitled to any refund (unless required by applicable law)."

Stability AI can terminate access without notice and without refund for terms violations.

## Comprehensive warranty disclaimer language

Every major AI provider employs extensive "as-is" disclaimer language to eliminate implied warranties and limit liability. These provisions follow remarkably similar patterns across vendors, suggesting industry-wide legal strategy.

### Universal "as-is" provisions

**OpenAI (Terms of Use):**

> "OUR SERVICES ARE PROVIDED 'AS IS.' EXCEPT TO THE EXTENT PROHIBITED BY LAW, WE AND OUR AFFILIATES AND LICENSORS MAKE NO WARRANTIES (EXPRESS, IMPLIED, STATUTORY OR OTHERWISE) WITH RESPECT TO THE SERVICES, AND DISCLAIM ALL WARRANTIES INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, SATISFACTORY QUALITY, NON-INFRINGEMENT, AND QUIET ENJOYMENT, AND ANY WARRANTIES ARISING OUT OF ANY COURSE OF DEALING OR TRADE USAGE. **WE DO NOT WARRANT THAT THE SERVICES WILL BE UNINTERRUPTED, ACCURATE OR ERROR FREE, OR THAT ANY CONTENT WILL BE SECURE OR NOT LOST OR ALTERED.**"

**Microsoft Azure (Product Terms - Previews):**

> "PREVIEWS ARE PROVIDED 'AS-IS,' 'WITH ALL FAULTS,' AND 'AS AVAILABLE,' as described herein."

**Google Vertex AI (Service Specific Terms - Pre-GA Offerings, Section 5.b):**

> "Disclaimer. PRE-GA OFFERINGS ARE PROVIDED 'AS IS' WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES OR REPRESENTATIONS OF ANY KIND. Pre-GA Offerings (i) may be changed, suspended or discontinued at any time without prior notice to Customer and (ii) are not covered by any SLA or Google indemnity."

**AWS (Service Terms - Beta Services, Section 2.6):**

> "WITHOUT LIMITING ANY DISCLAIMERS IN THE AGREEMENT OR THE SERVICE TERMS, BETA SERVICES AND BETA REGIONS ARE NOT READY FOR GENERAL COMMERCIAL RELEASE AND MAY CONTAIN BUGS, ERRORS, DEFECTS, OR HARMFUL COMPONENTS. ACCORDINGLY, AND NOTWITHSTANDING ANYTHING TO THE CONTRARY IN THE AGREEMENT OR THESE SERVICES TERMS, AWS IS PROVIDING BETA SERVICES AND BETA REGIONS TO YOU 'AS IS.' AWS AND ITS AFFILIATES AND LICENSORS MAKE NO REPRESENTATIONS OR WARRANTIES OF ANY KIND, WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE REGARDING BETA SERVICES AND BETA REGIONS, INCLUDING ANY WARRANTY THAT THE BETA SERVICES AND BETA REGIONS WILL BECOME GENERALLY AVAILABLE, BE UNINTERRUPTED, ERROR FREE, OR FREE OF HARMFUL COMPONENTS, OR THAT ANY CONTENT, INCLUDING YOUR CONTENT, WILL BE SECURE OR NOT OTHERWISE LOST OR DAMAGED."

**Anthropic (Commercial Terms):**

> "THE SERVICES AND OUTPUTS ARE PROVIDED 'AS IS' AND 'AS AVAILABLE' WITHOUT WARRANTY OF ANY KIND."

**Hugging Face (Terms of Service):**

> "the Services and Content are provided 'as is' and 'as available'"

**Stability AI (Terms, Section 11):**

> "OUR SERVICES ARE PROVIDED 'AS IS' AND, TO THE EXTENT PERMISSIBLE UNDER APPLICABLE LAW, WITHOUT WARRANTIES, (WHETHER EXPRESS, IMPLIED, OR STATUTORY)."

### Disclaimer of implied warranties

All providers explicitly disclaim the implied warranties that would otherwise apply to commercial transactions under the Uniform Commercial Code or common law.

**Disclaimers of merchantability:**

This warranty normally guarantees products are fit for ordinary purposes and of fair average quality. Every AI provider disclaims it:

- **OpenAI**: "disclaim all warranties including all implied warranties of merchantability"
- **Microsoft**: disclaims "implied warranties of merchantability"
- **Google**: "PRE-GA OFFERINGS ARE PROVIDED 'AS IS' WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES"
- **AWS**: "DISCLAIM ALL WARRANTIES, INCLUDING ANY IMPLIED WARRANTIES OF MERCHANTABILITY"
- **Anthropic**: "EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES, INCLUDING WARRANTIES OF MERCHANTABILITY"
- **Hugging Face**: "implied warranties of merchantability"
- **Stability AI**: "DISCLAIM ALL WARRANTIES OF... MERCHANTABILITY"

**Disclaimers of fitness for particular purpose:**

This warranty normally guarantees products are suitable for the specific purpose the buyer communicated to the seller. All providers disclaim:

- **OpenAI**: "fitness for a particular purpose"
- **Microsoft**: "fitness for a particular purpose"
- **Google**: disclaims all warranties for Pre-GA offerings
- **AWS**: "FITNESS FOR A PARTICULAR PURPOSE"
- **Anthropic**: "FITNESS FOR A PARTICULAR PURPOSE"
- **Hugging Face**: "fitness for a particular purpose"
- **Stability AI**: "FITNESS FOR A PARTICULAR PURPOSE"

**Disclaimers of non-infringement:**

Providers disclaim warranties that services won't infringe third-party intellectual property rights:

- **OpenAI**: "noninfringement"
- **Microsoft**: implied through "as-is" language
- **AWS**: "NON-INFRINGEMENT"
- **Anthropic**: "NON-INFRINGEMENT"
- **Hugging Face**: "non-infringement"
- **Stability AI**: "NON-INFRINGEMENT"

### No guarantee of uninterrupted or error-free service

Beyond disclaiming specific warranties, providers explicitly state they don't guarantee services will work continuously or correctly.

**OpenAI (Business Terms, Section 9.2):**

> "Despite anything to the contrary, we make no representations or warranties (a) that use of the Services will be uninterrupted, error free, or secure, (b) that defects will be corrected, (c) that Customer Content will be accurate, or (d) with respect to Third Party Offerings."

**Microsoft** does not explicitly warrant uninterrupted service in Product Terms beyond "as-is" language.

**Google (Gemini API Terms):**

Disclaimers indicate services "may sometimes provide inaccurate or offensive content."

**AWS (Beta Services):**

> "MAKE NO REPRESENTATIONS OR WARRANTIES... REGARDING BETA SERVICES AND BETA REGIONS, INCLUDING ANY WARRANTY THAT THE BETA SERVICES AND BETA REGIONS WILL BECOME GENERALLY AVAILABLE, BE UNINTERRUPTED, ERROR FREE, OR FREE OF HARMFUL COMPONENTS"

**Anthropic:**

> "ANTHROPIC DOES NOT WARRANT, AND DISCLAIMS THAT, THE SERVICES OR OUTPUTS ARE ACCURATE, COMPLETE OR ERROR-FREE OR THAT THEIR USE WILL BE UNINTERRUPTED."

**Hugging Face:**

> "the Services or Content will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected"

**Stability AI:**

> "WE DO NOT WARRANT THAT ANY INPUT OR OUTPUT WILL BE SECURE OR NOT LOST OR ALTERED."

### Model updates and performance degradation disclaimers

Providers reserve broad rights to modify services, including underlying models, without guaranteeing consistent performance.

**Microsoft Azure (AI Foundry Models documentation):**

> "AI models evolve fast, and when a new version or a new model with updated capabilities in the same model family become available, older models may be retired in the AI Foundry model catalog. To allow for a smooth transition to a newer model version, some models provide users with the option to enable automatic updates."

Models may be "retired" forcing customers to migrate. "Automatic updates" may change behavior without explicit approval.

**Google Vertex AI (Service Specific Terms, Section 19.n):**

> "Notwithstanding any other provision of the Agreement related to product discontinuation, Google may discontinue Provisioned Throughput for any model available through Generative AI on Vertex AI by providing Customer at least 6 months' prior notice, with no notice required if Google replaces such functionality with materially similar functionality."

Google reserves the right to discontinue specific models with only 6 months' notice—or **no notice if replacing with "materially similar functionality."** The provider determines what qualifies as "materially similar," not the customer.

**Cohere (Deprecations Documentation):**

> "As Cohere launches safer and more capable models, we will regularly retire old models. Applications relying on Cohere's models may need occasional updates to keep working."

Regular model retirement is explicit policy. Customer applications must be updated or will fail.

**Stability AI (Terms, Section 12.a):**

> "We may periodically update our Services, including add or remove features or Services, without advance notice."

No advance notice required for changes.

### Beta/Preview feature disclaimers

Pre-release features receive even broader disclaimers, often excluding SLA coverage entirely.

**OpenAI (Service Terms):**

> "Beta Services are offered 'as-is' to allow testing and evaluation and are excluded from any indemnification obligations OpenAI may have to you... Except to the extent prohibited by law, OpenAI expressly disclaims all warranties for Beta Services, including any implied warranties of merchantability, satisfactory quality, fitness for a particular purpose, non-infringement, or quiet enjoyment, and any warranties arising out of any course of dealing or usage of trade."

Beta features are explicitly excluded from indemnification—OpenAI won't defend customers against third-party claims arising from beta feature use.

**Microsoft (Product Terms):**

> "PREVIEWS ARE PROVIDED 'AS-IS,' 'WITH ALL FAULTS,' AND 'AS AVAILABLE,' as described herein. Unless otherwise noted in a separate agreement, Previews are not included in the SLA for the corresponding Online Service, and may not be covered by customer support. We may change or discontinue Previews at any time without notice."

**Microsoft (Azure Preview Supplemental Terms - Azure Direct Models):**

> "Models in Preview may exhibit unexpected behavior, which may include higher risks of producing potentially harmful content and/or greater susceptibility to jailbreaking."

Preview models explicitly carry "higher risks of producing potentially harmful content"—yet customers deploying them bear responsibility for implementing safeguards.

**Google (Service Specific Terms, Section 5.b):**

> "PRE-GA OFFERINGS ARE PROVIDED 'AS IS' WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES OR REPRESENTATIONS OF ANY KIND. Pre-GA Offerings (i) may be changed, suspended or discontinued at any time without prior notice to Customer and (ii) are not covered by any SLA or Google indemnity."

**Google (Service Specific Terms, Section 5.c - Liability):**

> "Notwithstanding anything to the contrary in any other limitation of liability Section in the Agreement, with respect to Pre-GA Offerings, Google will not be liable for any amounts in excess of the lesser of (i) the limitation on the amount of liability stated in the Agreement or (ii) **$25,000.**"

Google caps pre-GA feature liability at just **$25,000 maximum**—potentially far below normal contract liability limits.

**AWS (Service Terms, Section 2.6):**

> "AWS'S AND ITS AFFILIATES' AND LICENSORS' AGGREGATE LIABILITY FOR ANY BETA SERVICES AND BETA REGIONS WILL BE LIMITED TO THE AMOUNT YOU ACTUALLY PAY US UNDER THIS AGREEMENT FOR THE BETA SERVICES OR BETA REGIONS THAT GAVE RISE TO THE CLAIM DURING THE 12 MONTHS PRECEDING THE CLAIM."

For beta services, AWS caps liability at fees actually paid for those specific beta features—often $0 if offered for free during beta.

### Data accuracy and content responsibility disclaimers

Providers universally disclaim responsibility for output accuracy, placing verification obligations on customers.

**OpenAI (Services Agreement, Section 3.3):**

> "You are solely responsible for all use of the Outputs and evaluating the Output for accuracy and appropriateness for your use case, including by utilizing human review as appropriate."

**OpenAI (Business Terms, Section 3.3):**

> "You are responsible for all Input and represent and warrant that you have all rights, licenses, and permissions required to provide Input to the Services. You are solely responsible for all use of the Outputs and evaluating the Output for accuracy and appropriateness for your use case, including by utilizing human review as appropriate."

**Anthropic (Commercial Terms):**

> "It is Customer's responsibility to evaluate whether Outputs are appropriate for Customer's use case, including where human review is appropriate, before using or sharing Outputs. Customer acknowledges, and must notify its Users, that factual assertions in Outputs should not be relied upon without independently verifying their accuracy."

**Google Gemini (API Terms):**

> "The Services include experimental technology and may sometimes provide inaccurate or offensive content that doesn't represent Google's views. Use discretion before relying on, publishing, or otherwise using content provided by the Services."

**Stability AI (Terms, Section 4.b):**

> "Generative artificial intelligence is technology that is still developing and Outputs may not always contain accurate information or be as you intended. You are solely responsible for verifying the accuracy, legality, and appropriateness of any Outputs before using or sharing them. Outputs should not be used for any critical decisions without independent human review."

**Hugging Face (Terms):**

> "We further disclaim all warranties or guarantees about the accuracy, reliability or benefits of any Services, artificial intelligence, Models or any other technology or Content"

### Liability caps and excluded damages

All providers cap aggregate liability and exclude consequential damages.

**Liability caps:**

- **OpenAI**: "THE GREATER OF THE AMOUNT YOU PAID FOR THE SERVICE THAT GAVE RISE TO THE CLAIM DURING THE 12 MONTHS BEFORE THE LIABILITY AROSE OR ONE HUNDRED DOLLARS ($100)"
- **Microsoft Azure**: Service credits as sole remedy; general liability follows volume licensing terms
- **Google**: Financial credits as sole remedy under SLA
- **AWS**: "THE AMOUNT YOU ACTUALLY PAY US UNDER THIS AGREEMENT FOR THE BETA SERVICES OR BETA REGIONS... DURING THE 12 MONTHS PRECEDING THE CLAIM" (for beta); 100% service credit maximum for SLA breaches
- **Anthropic**: "limited to Fees actually paid by Customer for the Services in the previous 12 months"
- **Hugging Face**: "the amount that you paid us during the 12-month period immediately preceding the last claim (or $50 if relating to a free service)"
- **Stability AI**: "THE GREATER OF $100 OR THE AMOUNT YOU PAID FOR ACCESSING OUR SERVICES IN THE SIX MONTHS BEFORE THE DATE SUCH DAMAGES"

**Excluded consequential damages (all providers exclude):**

- Lost profits
- Business interruption
- Loss of revenue
- Loss of goodwill
- Loss of data
- Cost of procurement of substitute goods
- Indirect, incidental, special, consequential, punitive, or exemplary damages

**OpenAI (Terms of Use):**

> "NEITHER WE NOR ANY OF OUR AFFILIATES OR LICENSORS WILL BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR EXEMPLARY DAMAGES, INCLUDING DAMAGES FOR LOSS OF PROFITS, GOODWILL, USE, OR DATA OR OTHER LOSSES, EVEN IF WE HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES."

**Anthropic (Commercial Terms, Section K.3):**

> "the liability of each Party, and its affiliates and licensors, for any damages arising out of or related to these Terms (i) excludes damages that are consequential, incidental, special, indirect, or exemplary damages, including lost profits, business, contracts, revenue, goodwill, production, anticipated savings, or data, and costs of procurement of substitute goods or services"

**Hugging Face (Terms):**

> "Neither of us (or any of our affiliates, subsidiaries, contractors, licensors, officers, directors, agents, or employees ('Related Parties')) will be liable for any indirect, incidental, consequential, punitive, special, or other similar damages, including loss of revenue, profits, data, benefits, or savings"

**Stability AI (Terms, Section 11):**

> "THE STABILITY PARTIES WILL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, PUNITIVE, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY, OR OTHER DAMAGES ARISING OUT OF OR RELATED TO OUR SERVICES, THE INPUTS / OUTPUTS, OR THESE TERMS... INCLUDING DAMAGES FOR LOSS OF PROFITS, GOODWILL, USE, OR DATA OR OTHER LOSSES, EVEN IF THE DAMAGES ARE FORESEEABLE."

## Comparative analysis: The contractual gap

Examining contracts across all major providers reveals a fundamental gap between what customers need and what vendors commit to providing.

### What providers guarantee vs. what customers need

**Providers guarantee:**
- Infrastructure availability (99.5%-99.95% uptime)
- Service accessibility (APIs responding to requests)
- Infrastructure-level SLAs with service credit remedies

**Customers actually need:**
- Model output accuracy and consistency
- Performance stability over time
- Fitness for specific business use cases
- Advance notice of model changes affecting behavior
- Recourse when outputs become unreliable

**The gap:** SLAs cover "is the service reachable?" not "does the service produce useful outputs?" A model can be 100% available while producing degraded, inaccurate, or hallucinated outputs—and **this triggers no contractual remedy**.

### The "availability vs. performance" distinction

All major provider SLAs measure **availability** (uptime, response rate, error rate) rather than **performance** (accuracy, quality, fitness for purpose). This creates several critical limitations:

1. **Model degradation doesn't breach SLAs**: A model experiencing concept drift, data distribution shifts, or declining accuracy remains "available" in contractual terms. The API returns responses successfully—they're just wrong responses.

2. **Hallucinations don't constitute outages**: Confidently stated but entirely fabricated outputs aren't service failures under any reviewed SLA. They're explicitly disclaimed as customer responsibility to verify.

3. **Model updates preserve "availability" while changing behavior**: Providers can swap underlying models, fundamentally altering output characteristics, without SLA breach as long as the API endpoint remains reachable.

4. **Latency variability often excluded**: Only Microsoft's Provisioned Throughput offers latency SLAs. Standard pay-per-token services may experience significant latency increases without contractual remedy.

### Enterprise vs. consumer tier differences

**Data protections:**
- **Google Gemini**: Paid services don't use data for training; unpaid services do
- **AWS**: Select services use data for improvement; opt-out available via AWS Organizations
- **Cohere**: Enterprise customers can opt out of training data use
- **OpenAI**: Business terms provide stronger data commitments than consumer terms

**Support and escalation:**
- Enterprise tiers typically include dedicated account teams
- Priority support response times
- Access to technical advisors
- Advance notice of deprecations (not always contractual)

**SLA coverage:**
- Consumer/free tiers: **No SLA** (explicitly stated by most providers)
- Standard paid tiers: Basic availability SLA
- Enterprise tiers: May negotiate enhanced SLAs, response time commitments, latency guarantees

**Notably absent even in enterprise tiers:**
- Model accuracy or quality guarantees
- Performance degradation protections
- Guarantees about model version stability
- Contractual commitments about model lifespans

### The sole remedy constraint

Every major provider's SLA contains "sole remedy" language limiting customers to service credits:

- **OpenAI Terms**: "your sole and exclusive remedy"
- **Microsoft Azure SLA**: "This SLA states Customer's sole and exclusive remedy"
- **Google Vertex AI SLA**: "This SLA states Customer's sole and exclusive remedy"
- **AWS Bedrock SLA**: "your sole and exclusive remedy"
- **AWS SageMaker SLA**: "your sole and exclusive remedy"

**Practical implications:**

1. **No right to sue for additional damages**: Service credit is the only contractual remedy even if business impact far exceeds the credit amount
2. **Credits are future-use only**: Not cash refunds; applied only to future invoices
3. **Credit caps**: Typically 10-100% of monthly fees for affected service
4. **No compensation for consequential losses**: Lost business opportunities, reputational harm, or costs of mitigation are unrecoverable

**Example scenario**: Company builds customer-facing application on AI service. Model degradation causes reputational harm and customer churn representing $1M in losses. Monthly AI service fees were $10,000. Maximum recovery under SLA: $10,000 credit toward future service use—not cash, and only if downtime breached availability threshold. Model degradation without downtime triggers no remedy at all.

### Common disclaimer patterns across all providers

**Universal elements in AI service contracts:**

1. **"As-is" provision**: Services provided without warranties
2. **Disclaimer of implied warranties**: Merchantability, fitness for purpose, non-infringement explicitly disclaimed
3. **No accuracy guarantees**: Explicit disclaimer that outputs may be inaccurate
4. **Customer verification responsibility**: Customers must independently verify output accuracy
5. **No uninterrupted service guarantee**: Providers don't warrant continuous availability
6. **Limitation of liability**: Caps at fees paid (typically 6-12 months)
7. **Exclusion of consequential damages**: Lost profits, business, data excluded from liability
8. **Service modification rights**: Providers may change or discontinue services with limited notice
9. **Beta/preview broader disclaimers**: Pre-release features have even more extensive disclaimers
10. **High-risk use disclaimers**: Not suitable for safety-critical applications

**Strongest protections (relative comparison):**
- **Microsoft Azure**: Highest uptime SLA (99.95% for SageMaker online inference), latency SLA for PTU
- **AWS**: 100% service credit for <95% availability (most generous credit tier)
- **Anthropic**: Requires customers to notify end users about output limitations (transparency requirement)
- **Cohere**: Most explicit model deprecation timeline documentation

**Weakest protections:**
- **OpenAI**: No public SLA for standard services
- **Free/unpaid tiers**: Zero SLA coverage across all providers
- **Beta/preview features**: Limited to $0-$25,000 liability caps, no SLA coverage, no support guarantees

## Key findings and implications

**For B2B customers:**

1. **Standard contracts provide essentially no model performance protection**. SLAs cover infrastructure availability only, not AI output quality. The service can be "up" while producing degraded outputs.

2. **All accuracy risk falls on customers**. Every provider disclaims output accuracy and requires customers to verify results. This fundamentally contradicts the value proposition of AI—automating tasks—since verification reintroduces manual review.

3. **Model changes are inevitable and largely at provider discretion**. Deprecation policies exist but with limited notice periods (6 months at Google, regular updates at Cohere, "without notice" at Stability AI). Providers determine what constitutes "materially similar" replacements.

4. **Remedies are strictly limited to service credits**. Sole remedy clauses prevent additional litigation or damages recovery. Credit caps at monthly fees create massive exposure gap when AI systems are mission-critical.

5. **Enterprise negotiations are essential for meaningful protection**. Standard terms are take-it-or-leave-it. Custom enterprise agreements may secure model version locks, enhanced SLAs, advance notice periods, or performance baselines—but only through negotiation.

**For legal review:**

1. **Implied warranty disclaimers are comprehensive and likely enforceable** in commercial contexts under UCC § 2-316 and common law, assuming proper formatting (conspicuous, explicit mention of merchantability/fitness).

2. **Limitation of liability clauses will likely be enforced** for sophisticated commercial parties absent unconscionability, fraud, or gross negligence. Courts rarely find commercial contracts between businesses unconscionable.

3. **"Sole remedy" clauses are generally enforceable** unless the exclusive remedy "fails of its essential purpose" (UCC § 2-719). Burden is on plaintiff to show remedy inadequacy.

4. **Beta/preview disclaimers create substantial risk**. Organizations relying on beta features accept that: (a) features may never reach GA; (b) no SLA applies; (c) liability is capped at minimal amounts; (d) features can be discontinued without notice.

5. **Choice of law and arbitration clauses warrant close review**. Most providers specify jurisdiction (often California, Washington, Delaware) and many include arbitration clauses preventing class actions.

## Methodology and sources

This analysis is based on verbatim extraction from official, publicly available contract documents accessed October 2025:

**OpenAI:**
- Business Terms (November 2023 - Current)
- Services Agreement (Current)
- Service Terms (Current)
- Terms of Use (Current)

**Microsoft Azure:**
- Product Terms - For Online Services (Current)
- Azure Legal Information (Current)
- Azure Preview Supplemental Terms (Current)
- Azure OpenAI Service FAQ (Current)
- SLA for Cognitive Services (Current)

**Google Cloud:**
- Vertex AI Service Level Agreement (Current, October 2025)
- Service Specific Terms (Last Modified: June 9, 2025)
- Gemini API Additional Terms of Service (Effective: May 20, 2025)

**AWS:**
- Amazon Bedrock SLA (Last Updated: October 4, 2023)
- Amazon SageMaker SLA (Last Updated: May 4, 2022)
- AWS Service Terms (Last Updated: July 17, 2025)

**Anthropic:**
- Commercial Terms of Service - Bedrock (Effective: January 2024)
- Commercial Terms of Service - Vertex (Version: March 19, 2024)

**Cohere:**
- Terms of Use (cohere.com/terms-of-use)
- Enterprise Data Commitments
- Deprecations Documentation

**Hugging Face:**
- Terms of Service (Effective: September 15, 2022)

**Stability AI:**
- Terms of Service (stability.ai/terms-of-service)
- Stable Assistant Terms of Service

All quotes are verbatim from official published terms. Enterprise customers may negotiate different terms privately. This analysis is for informational purposes only and does not constitute legal advice. Organizations should consult legal counsel before entering AI service agreements.