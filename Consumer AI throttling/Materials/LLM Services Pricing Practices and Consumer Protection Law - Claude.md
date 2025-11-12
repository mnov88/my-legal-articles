# LLM Services Pricing Practices and Consumer Protection Law: Comprehensive Academic Research Report

## Executive Overview

This comprehensive research investigates Large Language Model (LLM) service pricing practices through five interconnected analytical lenses: user behavioral responses, provider practices and justifications, regulatory precedents, technical feasibility, and economic theory. **The central finding reveals a critical disconnect: capacity ambiguity in LLM services is primarily a business model choice rather than strict technical necessity, exploiting well-documented behavioral biases while operating in a novel regulatory gap between information services, variable-capacity digital products, and credence goods.**

Major providers demonstrate technical capability for transparency through API documentation yet deliberately maintain opacity in consumer subscriptions, marketing "unlimited" access while implementing undisclosed throttling. This practice exploits flat-rate bias and creates severe information asymmetries in credence good markets, while existing EU consumer protection frameworks lack specific provisions for stochastic service quality.

---

## RESEARCH QUESTION 1: User Behavior Under Different Pricing Models

### Key Findings: Behavioral Patterns and Psychological Effects

#### The "Metered Mindset" Phenomenon

Extensive evidence from user communities and academic literature confirms users exhibit profound behavioral changes under different LLM pricing models, consistent with established research on flat-rate bias. **Users under token/credit systems demonstrate "token anxiety"—constant mental calculation of costs that creates cognitive overhead and self-censorship behavior.**

Academic foundation from telecommunications research (Krämer & Wiewiorra, 2012; Uhrich et al., 2013) identified four key mechanisms driving flat-rate preference: the **taximeter effect** (disutility from perceiving marginal costs), **insurance effect** (willingness to pay premiums for cost predictability), **overestimation effect** (tendency to overestimate usage), and **flexibility effect** (resistance to perceived inflexibility). These patterns manifest distinctly in LLM usage.

User testimony from Reddit and developer forums reveals self-censorship behaviors: avoiding follow-up questions, crafting shorter prompts to conserve tokens, and abstaining from exploratory conversations that might "waste" quota. One developer noted creating monitoring tools specifically to "dodge usage cut-offs," while community projects like "Claude Code Usage Monitor" emerged to help users track consumption in real-time.

#### Sunk Cost Fallacy in Subscription Behavior

**Critical academic evidence** directly addresses subscription pricing and sunk cost effects:

**Zhang et al. (2025)** in *Journal of the Association for Information Systems* found box office revenues increased 12-35% after downward price adjustment, with effects particularly strong for niche information goods. Lower fixed fees attract price-conscious consumers more susceptible to sunk cost fallacy.

**Wharton Study (2020)** on subscription programs found members increased purchases by $27/month on average, with only one-third attributable to economic benefits. Two-thirds stemmed from "becoming a member per se"—clear evidence of sunk cost fallacy driving consumption. The effect was negatively correlated with program benefits, meaning higher sunk costs led to more consumption regardless of value.

For LLM services, this manifests in users describing feeling "trapped" in subscriptions after upfront payment. ChatGPT Pro users paying $200/month report strong pressure to maximize usage, with some making "over $1,000 worth of calls (measured in API pricing) in a single day."

#### Quantity Restrictions vs. Quality Degradation: A Critical Distinction

User complaints bifurcate into **two distinct categories** with different behavioral implications:

**Quantity Restrictions (Usage Limits/Throttling):**
- Primary complaint: **Unpredictability**—users cannot plan workflows around unknown limits
- GPT-5 rollout limited ChatGPT Plus users to 200 messages per week, creating significant workflow disruption
- Anthropic's Claude Code crisis (July 2025): Introduced weekly limits without announcement, affecting developers mid-project
- Behavioral adaptations: Creating monitoring tools, timing usage to reset windows, batching queries, account sharing (policy violation but widely reported)

**Quality Degradation:**
- GPT-5 rollout provides natural experiment in quality perception
- Reddit thread "GPT-5 is horrible" garnered 3,200+ upvotes and 1,400 comments
- Users described model as "cold," "robotic," "soulless," with loss of "conversational warmth"
- Paradox: Technical performance improved (94.6% on AIME 2025 Math Exam) while user satisfaction plummeted
- Users report "mourning" GPT-4o "like losing a friend"

**The distinction is fundamental**: Users adapt to quantity restrictions through strategic behavior but react with emotional intensity to forced quality changes affecting subjective experience. Users tolerate quality issues if given control but strongly resist forced changes and access limitations.

#### Provider Usage Data

**Anthropic Economic Index (August 2025)** analyzed 1 million Claude.ai conversations:
- **Behavioral shift toward delegation**: 27% → 39% "directive" (full task delegation) interactions in 8 months
- **Enterprise automation dominates**: 77% pure automation in API usage vs. ~50% on consumer platforms
- Growing trust drives increased delegation

**OpenAI Data (July 2025)** for 700 million weekly users:
- 18 billion messages weekly (2.5 billion daily)
- **Personal vs. work shift**: 73% personal use (up from 53% in June 2024), 27% work
- **Top use cases**: "Asking" for advice (49%), "Doing" tasks (40%)
- Consumer satisfaction highest with augmentation/collaboration, not full automation

### Contradictions and Debates

**The Democratization-Divergence Paradox**: OpenAI data shows fastest growth in low- and middle-income countries with closing gender gaps, suggesting democratization. However, Anthropic data reveals AI usage correlates with GDP (0.7% increase per 1% GDP growth), with wealthy nations using more intensively. **Resolution**: Consumer AI democratizes access while enterprise AI concentrates competitive advantages—dual trajectories creating new inequality forms.

**Collaboration vs. Automation Preference Gap**: Users derive more satisfaction from "asking" (advisory) mode, yet behavioral trends show clear movement toward automation. Anthropic's consumer trend (27% → 39% automation) serves as "leading indicator" for enterprise endpoint (77%). Economic gravity pulls toward automation despite preference for collaboration.

**Quality vs. Intelligence Tradeoff**: GPT-5's 45% reduction in factual errors and higher technical accuracy deemed "worse" by users due to personality loss. Classic Goodhart's Law manifestation: optimizing for measurable metrics (accuracy, brevity, safety) destroyed unmeasurable but valuable qualities (warmth, creativity, engagement).

### Implications for Scholarly Argument

**The evidence suggests focusing on BOTH quantity and quality ambiguity**, as they operate through different mechanisms:
- **Quantity ambiguity** creates planning uncertainty, strategic behavior, and trust erosion
- **Quality ambiguity** creates emotional responses, satisfaction issues, and expectation management challenges

The psychological costs of metered systems—anxiety, self-censorship, cognitive overhead—are real but unmeasured. The Claude Code crisis demonstrates ambiguous throttling destroys trust faster than explicit limits.

### Research Gaps

**Critical gaps identified:**
1. **No longitudinal studies** tracking individual user behavior across 12+ months under different pricing models
2. **No quantitative metrics** on prompt length changes, query complexity variations, or self-censorship magnitude
3. **No cognitive load studies** measuring mental overhead of token tracking or decision fatigue
4. **No cross-platform comparative studies** controlling for model quality differences
5. **Limited demographic analysis** of how pricing preferences vary by income, profession, technical sophistication

Most flat-rate bias research predates LLMs; no peer-reviewed studies specifically examine LLM pricing behavior. Provider data suffers from selection bias (excludes churned users) and short time windows (8 months maximum).

---

## RESEARCH QUESTION 2: Provider Practices and Justifications

### Key Findings: Pricing Models and Terms of Service

#### Comprehensive Provider Mapping

**Credit/Token Systems vs. "Unlimited" with Fair Use Policies:**

**Pure Token/Credit Systems:**
- **Cohere**: 100% usage-based API pricing ($0.50-$15.00 per million tokens)
- **OpenAI API**: Token-based for developers ($2.50-$10.00 per million tokens for GPT-5)
- **Google Vertex AI**: Token-based with quota system
- **Mistral API**: €0.14-€7.50 per million tokens

**"Unlimited" with Fair Use Policies:**
- **OpenAI ChatGPT Pro**: $200/month marketed as "unlimited subject to abuse guardrails"
- **OpenAI Business/Enterprise**: "Virtually unlimited" with fair use
- **Anthropic Pro**: $20/month with undisclosed message limits, 5-hour resets
- **Perplexity Pro**: $20/month "unlimited" searches

**Hybrid Models:**
- **OpenAI Enterprise**: Base credits plus overage pricing
- **Google Gemini**: Daily request caps (100 Gemini 2.5 Pro requests/day for AI Pro at $19.99/month)

#### Critical Analysis of Terms of Service

**OpenAI ChatGPT Pro ToS** (from Help Center documentation):
> "The ChatGPT Pro plan offers unlimited access to GPT-5 as well as our legacy models. However, usage must adhere to our Terms of Use, which prohibits, among other things: Abusive usage, such as automatically or programmatically extracting data. Sharing your account credentials or making your account available to anyone else. Reselling access or using ChatGPT to power third-party services. We have guardrails in place to help prevent misuse and are always working to improve our systems. This may occasionally involve a temporary restriction on your usage."

**Critical omission**: No specific metrics for "abusive usage" or triggers for "temporary restriction."

**Contradiction identified**: OpenAI Pro marketed as "unlimited" but Help Center documentation lists same weekly/daily caps for o1/o3/o4-mini models as Plus plan (e.g., o1: 50/week), directly contradicting unlimited claims.

**Anthropic Rate Limit Changes (August 2025)**: Introduced weekly rate limits to address users "running Claude Code continuously in the background, 24/7." Company spokesperson stated limits would affect "less than 5% of subscribers based on current usage" and were necessary to "maintain reliable service broadly" due to "computational resource constraints."

**Google Gemini Documentation** demonstrates greater transparency:
- Explicit quota system with TPM (Tokens Per Minute) quotas per region/subscription
- Clear upgrade request process
- Rate limits justified as serving "fairness," "security," and "infrastructure health"

#### Fair Use Policy Characteristics

**Common FUP patterns across providers:**
1. **Vague language**: "Abuse," "unusual activity," "fair use" without specific thresholds
2. **Retroactive application**: Users learn limits only after hitting them
3. **Non-negotiable**: No ability to pay for guaranteed higher limits
4. **Enforcement opacity**: No transparency on detection methods or appeal processes

**Consumer vs. API transparency disparity**: Providers demonstrate capability for transparency through published API rate limits (RPM, TPM tiers, explicit thresholds, 429 error codes) but deliberately avoid transparency for consumer subscription plans.

### Provider Justifications

**Technical Necessity Arguments** (from documentation):
- **Capacity management**: OpenAI cites "Infrastructure Health: Help manage overall demand"
- **Abuse prevention**: Preventing 24/7 automated extraction, account sharing, reselling access
- **Fairness**: "Ensuring all users have equal opportunities"

**Business Model Flexibility** (inferred from practices):
- Competitive pressure to match "unlimited" marketing
- Revenue protection from power users overwhelming flat-rate plans
- Product evolution flexibility without contractual obligations
- Psychological pricing advantages of "unlimited" over explicit caps

**Critical finding**: If specific thresholds were necessary for technical reasons, providers could publish general ranges without enabling exploitation (e.g., "excessive usage >10× typical behavior"). Choice not to reveal any metrics indicates business rather than technical motivation.

### EU Consumer Protection Actions

#### BEUC (European Consumer Organisation) Complaints

**April 2023**: Called for EU and national authorities to launch investigations into ChatGPT:
> "For all the benefits AI can bring to our society, we are currently not protected enough from the harm it can cause people... EU and national authorities in these fields should launch an investigation immediately."

**June 2023**: Consumer groups from 14 European countries filed complaints about generative AI risks including:
- Deceptive practices and consumer manipulation
- Bias and discrimination
- Privacy violations

#### National Data Protection Authority Actions

**Italy (Garante, March 2023)**: Temporarily banned ChatGPT, launched investigation into suspected GDPR violations

**Spain (AEPD, April 2023)**: Announced investigation into ChatGPT data breaches, requested EU-wide coordination

**France (CNIL, April 2023)**: Investigating complaints about ChatGPT as part of EDPB task force

**EDPB (European Data Protection Board, April 2023)**: Created dedicated ChatGPT task force to "foster cooperation and exchange information on possible enforcement actions"

**Critical gap**: Investigations focus primarily on data privacy and GDPR compliance, with less attention to consumer protection aspects of pricing/throttling practices specifically.

#### EU AI Act Implications

**Status**: Adopted June 2024, phased implementation through 2028. LLMs classified as General-Purpose AI (GPAI) models with transparency requirements, technical documentation, and copyright compliance obligations. High-risk classification if used for employment, credit scoring, or essential services access.

**Relevant for pricing**: Transparency obligations and "appropriate accuracy levels" requirements, though **no specific provisions for variable output quality in standard consumer interactions**.

### Contradictions Between Policy and Practice

**OpenAI Pro ($200/month)** user case study from Medium: User hit restrictions within 24 hours of subscribing. OpenAI response cited vague "guardrails" and "unusual activity" without specifics, directed to email support. User's analysis identified four problems: inadequate customer service for premium tier, lack of transparency on "guardrails," burden on customer to justify usage, generic violations without evidence.

**Anthropic August 2025**: After sudden weekly limit introduction, users complained of poor communication and unexpected changes. Pattern of implementing restrictions on existing subscriptions with minimal advance notice.

### Implications for Scholarly Argument

**Evidence strongly supports focusing on quantity ambiguity as primary regulatory concern**, as:
1. Providers demonstrate technical capability for transparency (API documentation) but choose opacity for consumer plans
2. "Unlimited" marketing combined with undisclosed throttling may violate UCPD prohibitions on misleading practices
3. Fair Use Policies serve as liability shields providing maximum provider rights, minimal consumer protections
4. EU enforcement actions exist but focus on privacy rather than pricing transparency

**Quality ambiguity remains important** but operates through different mechanisms (credence good characteristics, subjective experience).

### Research Gaps

**Missing from provider documentation:**
1. Quantitative thresholds (messages per period, total tokens per cycle)
2. Detection methodologies for "unusual activity"
3. Service level commitments for consumer plans
4. Remedies (refund policies, service credits, cancellation rights)
5. Comparative metrics (average usage by tier, percentage affected by throttling)

**Regulatory gaps**: No EU enforcement actions specifically targeting LLM pricing/throttling practices, though legal frameworks (UCPD, Consumer Rights Directive) apply.

---

## RESEARCH QUESTION 3: Analogous Services and Regulatory Precedents

### Key Findings: EU Case Law and Frameworks

#### CJEU Cases on Telecommunications Throttling

**Telenor Magyarország (C-807/18, Judgment 15 September 2020)**
- **Framework**: Net Neutrality Regulation (EU) 2015/2120, Articles 3(2) and 3(3)
- **Holding**: Zero-rating with selective throttling violates Article 3(3)'s prohibition on discriminatory traffic management
- **Legal test**: Traffic management violates Net Neutrality if discriminating based on commercial rather than technical/congestion grounds

**German Trilogy (Judgments 2 September 2021)**
- **Cases**: C-854/19 (roaming), C-5/20 (tethering), C-34/20 (video streaming)
- **Revolutionary holding**: CJEU declared zero-rating *per se* incompatible with EU law
- **Significance**: Creates incentives for specific services, violating Article 3(3) regardless of limitations—binding on all EU regulatory authorities

#### Analogous Services Regulation

**ISP "Unlimited" Plans under EECC & Net Neutrality**

**Framework**: EECC Directive (EU) 2018/1972 + Net Neutrality Regulation (EU) 2015/2120

**Solutions applied:**
- ✓ Mandatory transparency disclosures (traffic management, throttling triggers)
- ✓ Prohibition of zero-rating (CJEU 2021)
- ✓ "Reasonable traffic management" limited to congestion, security, court orders
- ✗ Vague "reasonable" standards created enforcement gaps
- ✗ Cross-border inconsistency in implementation (only 3/27 states implemented EECC on time)

**Fair Use Policies**: EU Roaming allows FUPs (e.g., 50GB limits) to prevent abuse while ensuring network stability—demonstrates regulatory acceptance of bounded "unlimited" with transparent limits.

**Cloud Computing "Burst Capacity"**

**Framework**: Data Act (EU) 2023/2854 (applicable September 2025)

**Provisions:**
- Switching charges gradually eliminated (capped now, prohibited by 2027)
- Contractual transparency for service specifications
- Standard contractual clauses for data sharing and cloud contracts

**Problem identified**: Study of 100 cloud ToS found 28% lack service descriptions; extensive "as-is" clauses undermine protections. **Academic critique**: "One-size-fits-all insufficient; sector-specific regulation needed."

**Approach**: Ex-ante contractual fairness rather than ex-post enforcement—but limited effectiveness due to weak enforcement.

**Streaming Services Quality Degradation**

**Frameworks:**
1. **Content Portability Regulation (EU) 2017/1128**: No quality guarantee obligation unless agreed; "Quality must not be deliberately reduced"; must inform consumers about quality expectations
2. **Digital Content Directive (EU) 2019/770** (effective January 2022): "Conformity with contract" standard with remedies (fix, price reduction, termination), but "as-is" clauses undermine protections

**COVID-19 precedent (2020)**: BEREC authorized ISP throttling for congestion; Netflix/YouTube voluntarily reduced to standard definition—demonstrated broad "exceptional circumstances" interpretation

**Gap**: No minimum quality standards; only conformity with (often vague) descriptions.

**Energy Utilities Peak/Off-Peak Pricing**

**Framework**: Electricity Directive (EU) 2019/944 + Regulation (EU) 2019/943

**Consumer protections:**
- Time-of-use pricing with 15-minute trading intervals (since September 2025)
- Must offer choice between fixed and variable pricing
- Vulnerability protections (no disconnection for energy-poor, supplier of last resort)
- **Ban on unilateral changes to fixed-price contracts**
- Enhanced pre-contractual information

**2022 Energy Crisis**: Regulation (EU) 2022/1854 mandated 5% peak hour consumption reduction, revenue caps (€180/MWh for inframarginal producers), surplus redistribution to vulnerable consumers.

**Success factors**: Fixed-price options, vulnerability protections, comparison tools
**Challenge**: Balancing real-time price exposure vs. volatility protection

#### EU Enforcement on AI Services

**AI Act (Regulation (EU) 2024/1689) effective August 2024**

**Phased implementation:**
- February 2, 2025: Prohibited systems ban
- August 2, 2025: GPAI transparency rules
- August 2, 2026: High-risk requirements
- August 2, 2028: Full application

**LLM relevance:**
- Classification: Most LLMs = General-Purpose AI (GPAI) models
- High-risk if used for employment, credit scoring, essential services access
- Transparency: Disclosure of AI interaction, technical documentation, copyright compliance
- **Critical gap**: No specific provisions for variable output quality in standard interactions

**Digital Fairness Act (Proposed Q3 2026)**

**Background**: Commission Fitness Check (October 2024) identified digital consumer protection gaps

**Relevant proposals:**
- Prohibition on dark patterns distorting autonomy/choice
- Transparency of ranking/recommendation parameters
- Proposed UCPD amendments: Expand Annex I blacklist, "digital professional diligence" standard

### Regulatory Solutions: Success and Failure Analysis

**Successful approaches:**
1. **Bright-line prohibitions**: Zero-rating ban (CJEU 2021)—clear standard, no case-by-case assessment
2. **Transparency + strong enforcement**: GDPR model with specific requirements plus 4% turnover fines
3. **Low-barrier redress**: Digital Content Directive termination rights
4. **Contract variation prohibition**: Electricity Directive ban on fixed-price changes

**Failed approaches:**
1. **Vague standards**: "Professional diligence" (UCPD Article 5(2)) requires expensive litigation
2. **Information-only transparency**: Overload; consumers don't read; behavioral biases ignored
3. **"Average consumer" benchmark**: Too high; ignores vulnerability and cognitive biases
4. **Fragmented enforcement**: German model lacks investigative powers, low impact
5. **Ex-post only**: Harm widespread before action; traders adapt faster than enforcement

### Applicability to LLM Services

**Existing frameworks that apply:**

**UCPD (Unfair Commercial Practices Directive 2005/29/EC)**: ✓ Applies to B2C LLM services
- Articles 6-7: Misleading claims about "unlimited" access if quality degrades
- Article 8-9: Exploiting emotional vulnerability through anthropomorphization
- **Limitation**: "Average consumer" standard problematic; case-by-case assessment
- **Enforcement likelihood**: Moderate

**Digital Content Directive**: ✓ Applies to LLM services
- Conformity requirements with remedies if non-conforming
- **Limitation**: Vague descriptions + "as-is" clauses defeat protections
- **Enforcement likelihood**: Low to Moderate

**AI Act**: ✓ LLMs are "AI systems"
- GPAI classification with transparency and documentation requirements
- **Limitation**: No specific variable quality provisions for standard use
- **Enforcement likelihood**: Moderate-High for high-risk uses; Low for general chatbots

### Novel Regulatory Category Assessment

**LLMs present HYBRID challenges**:
- **Not entirely novel**: Analogous to variable capacity services (ISPs, cloud, streaming)
- **Novel degree**: Unpredictability, opacity, scale, and dual nature (product/service/tool)

**Specific novel elements:**
1. **Stochastic outputs**: No deterministic quality guarantee—same prompt yields different results
2. **Real-time unpredictable variability**: Unrelated to observable demand patterns
3. **Anthropomorphic interface**: Creates unique expectation management issues
4. **Training data quality**: Indirectly affects user experience through opaque mechanisms
5. **Rapid model updates**: Change service fundamentally without contract modification
6. **Credence good characteristics**: Quality cannot be evaluated even after consumption

**Critical regulatory gaps for LLMs:**
1. **No standard for acceptable variability**: Regulations address failure/non-conformity, not probabilistic outputs
2. **"Average consumer" test inadequate**: Presumes understanding deterministic products
3. **No minimum performance baselines**: Digital services exempt from mandatory quality standards
4. **Real-time variability not addressed**: LLMs vary second-to-second; existing frameworks assume static characteristics
5. **Model update framework missing**: No notification/compensation rights for version changes
6. **Anthropomorphization**: Marketing creates unrealistic expectations; UCPD not adapted for AI capability claims

### Implications for Scholarly Argument

**LLMs occupy a novel regulatory category** requiring framework adaptation. Existing EU consumer protection law provides foundation (UCPD, Digital Content Directive, AI Act) but **significant gaps exist** for:
- Stochastic service quality standards
- Real-time variability disclosure mechanisms
- Model version control and consumer rights
- Emotional manipulation through conversational AI

**The Digital Fairness Act (2026) presents timely opportunity** for targeted intervention through:
- LLM-specific Annex I prohibitions (misleading capability claims, "unlimited" without quality disclosure)
- "Digital professional diligence" standard for AI services
- Model version stability rights

**Recommended regulatory focus**: Transparency requirements (proven effective) rather than guaranteed capacity mandates (economically disruptive), with sector-specific AI consumer regulation addressing novel stochastic quality characteristics.

### Research Gaps

**Major gaps identified:**
1. **No enforcement actions** specifically on AI/LLM pricing/throttling practices (despite applicable frameworks)
2. **Limited academic literature** on regulating stochastic digital services
3. **Cross-jurisdictional inconsistency**: National implementation variance creates forum shopping opportunities
4. **Framework interoperability**: DSA/UCPD/AI Act overlap creates uncertainty
5. **Aggregated vs. individual quality**: Regulations focus on individual consumers; systemic degradation not addressed

---

## RESEARCH QUESTION 4: Technical Reality and Necessity of Ambiguity

### Key Findings: Economic and Technical Constraints

#### Operational Cost Reality

**ChatGPT operating costs** from multiple credible sources:
- **SemiAnalysis (Dylan Patel, 2023)**: $694,444/day (~$0.36/query), requiring ~3,617 HGX A100 servers (28,936 GPUs)
- **Tom Goldstein (University of Maryland)**: $100,000/day or $3M/month
- **2025 estimates**: Advanced model queries can cost up to $1,000 in compute

**Critical profitability crisis**: OpenAI CEO Sam Altman admitted "currently losing money" on ChatGPT Pro ($200/month), stating users "use it much more than we expected." OpenAI projected to lose $5 billion in 2024 against $3.7 billion revenue.

**Economic break-even analysis**:
- At $0.36/query: User making 100 queries/day costs $10.80/day = $324/month
- Exceeds ChatGPT Plus pricing ($20/month) at just **60 queries/day**
- Subscription model unsustainable for heavy users without throttling

**Cost structure**: ~$0.0035/1000 tokens actual cost vs. $0.02/1000 tokens API pricing = 80% gross margins **only if machines never idle**. SemiAnalysis estimated only 50% hardware utilization due to idle time, eliminating margins.

#### Cost Decline vs. Model Complexity

**LLMflation - Rapid price decline** (Andreessen Horowitz analysis):
- 10× cost decrease annually for equivalent performance
- GPT-3 equivalent: $60/M tokens (November 2021) → $0.06/M tokens (2024) = **1,000× reduction in 3 years**
- Driven by GPU improvements, quantization (16-bit → 4-bit), software optimizations

**However**: Advanced models (o1, o3) maintain high costs ($60/M output tokens), suggesting providers "concede low end" while protecting margins on premium models.

#### Technical Sources of Variability

**Two-phase LLM architecture**:
- **Prefill**: Compute-bound, parallel processing, high throughput
- **Decode**: Memory-bound, sequential generation, "often becomes the bottleneck"

**Variability factors**:
- **Sequence length**: KV cache grows linearly; longer outputs exponentially increase memory
- **Batch composition**: Variable completion times create "head-of-line blocking"
- **Model size**: Llama 70B requires ~140GB GPU memory at FP16
- **GPU memory constraints**: Concurrent capacity inversely proportional to context length

**Memory requirements**:
- Llama 3 70B: ~140GB at FP16 (needs 2× A100-80GB or 4× A100-40GB)
- KV cache overhead: 20-35% of GPU memory
- GPU with 24GB total: ~19GB weights, ~5GB KV cache → very limited concurrent users

### Rate Limiting and Capacity Management Infrastructure

**OpenAI API**: Token bucket algorithm with RPM (Requests Per Minute), RPD (Requests Per Day), TPM/ITPM/OTPM (Token limits). **Tiered system** with automatic advancement based on deposit amount, time at tier (1-2 weeks), payment history. Justified as ensuring "fair access" and preventing "abuse."

**Anthropic**: 4-tier system ($5+, $40+, $200+, $400+) with model-specific caps. Tier 1 particularly restrictive: 4,000-10,000 output tokens/minute (~2 generations before 1-minute wait).

**Critical finding**: "OpenAI does not provide a guaranteed SLA for the availability of its APIs, which means that SaaS providers cannot guarantee the availability of their products when relying on these APIs."

**Enterprise exception**:
- **Azure OpenAI**: 99.9% uptime SLA
- **AWS Bedrock**: Provisioned Throughput with guaranteed capacity
- **Google Vertex AI**: Enterprise SLAs available
- All require 10× or more pricing versus consumer rates

### Technical Feasibility of Guaranteed Capacity

**Verdict**: Guaranteed SLAs are **technically feasible but economically infeasible** at current consumer pricing.

**Proof of technical feasibility**: Enterprise "Provisioned Throughput" offerings exist across AWS Bedrock, Azure OpenAI, and Google Vertex AI. **Their existence proves guaranteed capacity is technically possible.**

**Why enterprise works but consumer doesn't**:
- Enterprise customers pay for **dedicated capacity** ($1,000s-$10,000s/month)
- Pricing reflects actual infrastructure costs plus overhead plus margin
- No resource sharing with other customers
- Consumer $20/month cannot cover dedicated GPU resources
- Requires statistical multiplexing across many users

**Technical requirements for SLAs** (all achievable):
- Redundant infrastructure ✓
- Load balancing across regions ✓
- Resource over-provisioning (20-30%) ✓
- Monitoring and response systems ✓

**Evidence**: All exist in enterprise offerings, proving technical feasibility.

#### State-of-the-Art: Academic Research on SLA-Compliant Serving

**Multiple 2024-2025 papers** demonstrate SLA compliance is achievable through sophisticated scheduling:
- "Optimizing LLM Inference Throughput via Memory-aware and SLA-constrained Dynamic Batching" (arXiv 2025)
- "Past-Future Scheduler for LLM Serving under SLA Guarantees" (ACM ASPLOS 2025)

**Research consensus**: Focus on "how" not "if"—SLA compliance is technically feasible, requiring sophisticated scheduling but fundamentally achievable.

**vLLM serving system**: PagedAttention + Continuous Batching achieves 2-4× throughput improvement versus standard serving through non-contiguous memory management and dynamic request batching. **Remaining limitation**: "Sequence group is preempted because there is not enough KV cache space. This can affect end-to-end performance."

### Technical Necessity vs. Business Choice

**Evidence matrix**:

**Technical Feasibility** ✓:
- Enterprise services prove guaranteed capacity possible
- Academic research demonstrates SLA-compliant serving achievable
- vLLM and similar technologies enable sophisticated resource management
- Providers successfully manage capacity for enterprise customers

**Business Reality** ✗:
- Consumer pricing doesn't cover costs for heavy users
- Providers losing money on high-end subscriptions
- Rate limits tightening in response to cost pressures
- **No technical reason explicit limits couldn't be stated**

**API vs. consumer plan transparency disparity proves business choice**: Providers publish explicit API rate limits (RPM, TPM tiers, clear error codes, quota increase processes) but maintain vague "abuse policies" for consumer plans. **Providers CAN provide transparency (demonstrated in API documentation) but CHOOSE not to for consumer subscriptions.**

### Regulatory Implications

**If regulations required guaranteed capacity at consumer pricing:**

**Scenario A - Maintain pricing**:
- Dramatic usage restrictions (explicit hard caps)
- "Unlimited" becomes clearly limited
- Paradox: Guarantees reduce access

**Scenario B - Maintain service**:
- 3-10× price increases
- Consumer tiers approach enterprise pricing
- Mass-market AI services become unaffordable

**Scenario C - Business model shift**:
- Pure pay-per-use API model
- No subscriptions
- Eliminates predictable pricing consumers prefer

**SLA overhead requirements**:
- 20-30% over-provisioning for burst capacity
- 2× infrastructure for redundancy/failover
- Already 50% idle time without SLA guarantees
- Would require 2-3× price increases or stricter usage limits

### Expert Opinions and Contradictions

**Provider contradictions**: OpenAI claims "compute costs are eye-watering" (Altman) implying unavoidable reality, yet still offers "unlimited" consumer tiers while losing money. **Rational business would** stop unprofitable services, set explicit hard limits, or move to profitable API-only model. **Interpretation**: Ambiguous capacity serves customer acquisition/retention strategy, subsidized by investor funding and enterprise revenue.

**Cloud provider actions contradict impossibility claims**: AWS, Azure, Google all provide guaranteed throughput, clear SLAs, and explicit capacity reservations. Their ability demonstrates guaranteed capacity is not technically impossible—difference is pricing reflects actual costs.

### Implications for Scholarly Argument

**Central conclusion**: Capacity ambiguity is **primarily a business model choice enabled by technical complexity, not strict technical necessity.**

**Technical constraints are real but surmountable**:
- Variable inference costs → Manageable with sophisticated scheduling
- GPU memory limitations → Addressable with over-provisioning
- Supply constraints → Affect pricing, not fundamental feasibility

**These constraints make guaranteed capacity expensive, not impossible.**

**Business advantages of ambiguity**:
1. Customer acquisition ("unlimited" > "100 queries/day")
2. Flexibility (adjust capacity without breaking promises)
3. Cost management (throttle expensive users without contractual violation)
4. Competitive positioning (explicit limits invite unfavorable comparisons)
5. Pricing psychology (subscriptions more palatable than usage-based)

**Regulatory consideration**: Question is not whether guaranteed capacity is technically possible (clearly yes) but **whether regulations should require it given economic tradeoffs**. Regulation should focus on **transparency requirements** rather than guaranteed capacity mandates, allowing market to determine optimal price/service tradeoffs.

### Research Gaps

**Empirical studies needed**:
1. Measurement of actual consumer LLM throttling behavior
2. User expectations vs. actual service delivery survey
3. Cost modeling under different regulatory scenarios
4. International regulatory comparison (EU vs. US vs. China)

**Gaps in public information** (deliberately opaque):
1. Actual GPU utilization rates
2. Per-user cost distribution and variance
3. Throttling algorithms and triggers
4. True concurrent capacity

**Conflicting cost estimates** (wide ranges suggest either significant uncertainty or deliberately obfuscated information):
- ChatGPT daily cost: $100K to $700K (7× variance)
- Cost per query: $0.01 to $1,000 (100,000× variance)

---

## RESEARCH QUESTION 5: Economic and Behavioral Literature on Pricing Variable-Value Services

### Key Findings: Theoretical Frameworks

#### Flat-Rate Bias and Consumer Preference for Certainty

**Seminal work**: Lambrecht & Skiera (2006) in *Journal of Marketing Research* documented that consumers systematically choose flat-rate tariffs even when pay-per-use would be cheaper, with flat-rate bias more prevalent than pay-per-use bias. Average overpayment: Users paid $17+ per gym visit despite $10 pay-per-visit alternatives. Bias generates 2-12% additional revenue for providers.

**Four mechanisms driving flat-rate bias**:

1. **Insurance effect**: Consumers pay premiums to avoid uncertainty and smooth monthly bills, reflecting loss aversion and desire to hedge against unexpectedly high usage

2. **Taxi meter effect** (also "ticking meter effect"): Pay-per-use reduces consumption utility because consumers experience psychological cost watching charges accumulate. Flat rates eliminate "pain of paying" during consumption.

3. **Convenience effect**: Flat rates reduce cognitive burden of tracking usage and simplify decision-making

4. **Overestimation effect**: Consumers systematically overestimate future usage, potentially due to wishful thinking or projection bias

**Welfare implications**: Short-term increases firm profits without significantly increasing churn. Long-term may increase churn as consumers become aware of overpayment. Creates deadweight loss through over-consumption by some, under-consumption by others.

**Extensions**: Balasubramanian, Bhattacharya & Krishnan (2015) confirmed "ticking meter" as key driver. Kienzler et al. (2021) demonstrated flat-rate bias persists even among experienced B2B purchasing professionals, suggesting robustness across contexts. Extensive telecommunications evidence (Gerpott 2007, 2009; Mitomo et al. 2007) confirms globally.

#### Mental Accounting and "All-You-Can-Eat" Effects

**Thaler's mental accounting framework** (1985, 1999): Consumers create separate mental accounts for different expenditure categories. Money is not fungible despite economic theory. Value function from prospect theory shows asymmetric treatment of gains and losses. **Transaction utility**: Consumers derive utility not just from consumption but from perceived quality of the deal.

**Implications for flat-rate pricing**:
- Fixed subscription payments become psychological "sunk costs"
- Once paid, consumption feels "free" (prospective accounting)
- Removes ongoing pain of paying, increasing consumption satisfaction
- Enables pre-commitment devices for time-inconsistent preferences

**DellaVigna & Malmendier (2006)**: "Paying Not to Go to the Gym" in *American Economic Review*

**Empirical findings from 7,752 health club members**:
- Members with $70+ monthly flat-rate contracts attended average 4.3 times/month
- Effective cost per visit: $17+ despite $10 pay-per-use option available
- Average member forewent $600+ in savings during membership
- Monthly contract holders 17% more likely to remain enrolled beyond one year than annual contract holders

**Theoretical explanation**: Time-inconsistent preferences (hyperbolic discounting), overconfidence about future self-control, projection bias ("I'll definitely go more next month"), default/inertia effects in cancellation decisions.

**Welfare analysis**: Consumer surplus negative for many due to overpayment. Firm profits enhanced through exploitation of behavioral biases. Overall efficiency reduced due to misallocation of consumer resources. Distributional concerns: Affects those with self-control problems most severely.

#### Bundling and Welfare Economics for Information Goods

**Bakos & Brynjolfsson** (1999, 2000, 2001): "Economies of Aggregation" theory

**Core insight**: When marginal costs are very low (as with digital/information goods), bundling large numbers of goods creates economies of aggregation through Law of Large Numbers:
- Individual valuations highly heterogeneous and unpredictable
- Bundle valuations converge toward mean through statistical aggregation
- Reduces dispersion in willingness-to-pay across consumers
- Enables more efficient price discrimination and higher extraction of consumer surplus

**Key mathematical result**: As bundle size n → ∞, variance of bundle valuation → 0, even if goods are imperfectly correlated. Allows monopolist to: (1) set price close to mean valuation, (2) sell to nearly all consumers, (3) extract nearly all consumer surplus.

**Welfare analysis**:
- **Producer surplus**: Dramatically increases with bundle size
- **Consumer surplus**: Ambiguous—bundling can increase sales/access but enables greater surplus extraction
- **Total welfare**: Often increases because more consumers purchase (output expansion)
- **Distributional effects**: Low-value consumers may gain access; high-value consumers pay less than willingness-to-pay

**Competitive implications**: Larger bundlers can outbid smaller ones for content. Bundling makes incumbents "tougher" competitors, raising entry barriers. Mixed innovation incentives. Favors consolidation and platform dominance.

**Critical distinction**:
- **Information goods**: Near-zero marginal cost makes bundling highly profitable
- **Physical goods**: Non-trivial marginal costs limit bundling benefits
- **LLM implication**: Compute costs create hybrid situation—not zero but low relative to value variation

#### Credence Goods with Quality Uncertainty

**Darby & Karni (1973)**: Foundational framework in *Journal of Law and Economics*

**Goods classification**:
1. **Search goods**: Quality observable before purchase (e.g., produce color)
2. **Experience goods** (Nelson 1970): Quality observable only after consumption (e.g., restaurant meal)
3. **Credence goods**: Quality cannot be evaluated even after consumption (e.g., medical treatment, auto repair, **LLM outputs**)

**Market failures in credence goods**:
- **Asymmetric information**: Sellers know quality; buyers cannot verify
- **Adverse selection**: Low-quality providers have incentive to misrepresent
- **Moral hazard**: Providers may undersupply quality or oversell services
- **Optimal fraud**: Some level of fraud may be economically "optimal" given verification costs

**Modern extensions**: Dulleck & Kerschbamer (2006, 2011) provide experimental evidence that reputation effects can mitigate fraud but imperfectly. Liability mechanisms (warranties, guarantees) improve outcomes. Verification costs crucial to market efficiency.

**LLM services as credence goods**:
- Output quality highly variable and context-dependent
- Users often cannot evaluate correctness (especially specialized tasks)
- Particularly acute for factual accuracy, reasoning quality, creativity assessment
- Creates severe information asymmetries between provider and user

**Welfare implications**:
- **Underutilization**: Risk-averse consumers may underconsume valuable services
- **Quality degradation**: Providers have incentives to reduce costly quality when unobservable
- **Price discrimination justification**: Can be welfare-enhancing if expands access while maintaining quality for high-value users

**Recent literature (2020s)**: Introduction of "diagnostic uncertainty" and "service uncertainty" in credence goods experiments. Even "honest" experts may give wrong advice due to noisy signals. Services may fail even when appropriately specified. **Direct application to LLMs**: Model uncertainty, prompt sensitivity, non-deterministic outputs.

#### Two-Sided Markets with Capacity Constraints

**Rochet & Tirole (2006)**: "Two-Sided Markets: A Progress Report" in *RAND Journal of Economics*

**Canonical model structure**:
- Platform intermediates between two distinct user groups
- Cross-side network externalities: Value to one side depends on participation of other side
- Platform sets prices on both sides to maximize total surplus extraction
- **Key insight**: Price structure matters, not just price level

**Optimal pricing**: Subsidize price-sensitive side with strong positive externality. Extract surplus from less elastic side. Usage fees below marginal cost can be profit-maximizing.

**Rysman (2009)**: Applications include video game platforms, payment cards, search engines/advertising. **Potential LLM application**: Developers/fine-tuners vs. end-users; or API users vs. compute providers.

**Capacity constraints in two-sided markets**:
- Most models assume unlimited capacity
- Capacity constraints complicate pricing: Must ration on both sides simultaneously
- With constraints: May need to price some side(s) above optimal to manage load
- Creates peak-load pricing incentives
- May favor committed users over casual users

**Theoretical gap for LLMs**: Compute capacity constraints critical to LLM economics. Queue management and priority access as additional dimensions. Limited academic treatment of capacity-constrained two-sided markets with variable quality.

#### Nonlinear Pricing Theory

**Spence (1977)**: "Nonlinear Prices and Welfare" established second-degree price discrimination through quantity-dependent pricing. Necessary condition for welfare improvement: Output expansion.

**Armstrong (1996)**: Multiproduct nonlinear pricing with continuum of types, characterizing optimal multi-part tariffs and conditions under which bundling dominates separate sales.

**Corrao, Flynn & Sastry (2023)**: "Nonlinear Pricing with Underutilization" in *American Economic Review*

**Key innovation**: Models goods where usage generates revenue for seller (advertising, data, network effects). Consumers can freely dispose of unwanted units. **Optimal structure**: Multi-part tariffs with tiers of zero marginal price. Rationalizes free products, free trials, unlimited subscriptions. **Direct LLM relevance**: Usage generates training data value for providers.

**Welfare results**: Free disposal harms both producer and consumer welfare relative to first-best. Both parties less sensitive to changes in usage-based revenue. May justify below-cost pricing even under competition.

**Bornstein & Peter (2024)**: "Nonlinear Pricing and Misallocation"—Markup heterogeneity under nonlinear pricing does NOT imply inefficiency across firms. New source of misallocation: Across consumers (high-taste consumers get too much; low-taste too little). Welfare losses from consumer misallocation > firm misallocation. Policy implication: Subsidizing high-markup firms can reduce welfare with nonlinear pricing.

### Efficiency vs. Exploitation in Flat-Rate Pricing

**When flat-rate pricing is efficient**:
1. Transaction costs: Metering costs > efficiency gains from usage-based pricing
2. Predictable demand: Average consumption relatively uniform across users
3. Network effects: Flat-rate encourages higher usage, building network value
4. Innovation incentives: Removes usage monitoring, facilitating experimentation
5. Administrative simplicity: Reduces billing complexity and disputes

**Odlyzko (1996-2001)**: Historical analysis showing flat-rate often dominated usage-based pricing. Customer preference for certainty often outweighs efficiency losses. Argues flat-rate pricing facilitated Internet growth.

**When flat-rate pricing is exploitative**:
1. Systematic bias exploitation: Deliberately designing contracts to exploit overconfidence
2. High variance in usage: Cross-subsidization from light to heavy users
3. Switching barriers: Combined with lock-in makes bias exploitation profitable
4. Vulnerable populations: Low financial literacy consumers disproportionately affected
5. Quality degradation: Using flat-rate to hide quality reductions

**DellaVigna & Malmendier (2004)**: "Contract Design and Self-Control"—Firms may deliberately design menus to exploit time-inconsistency. "Shrouded attributes" and complex pricing structures exacerbate exploitation. Competitive markets may not eliminate exploitation if all firms use similar strategies.

### Welfare Economics Assessment Framework

**Social welfare decomposition**: ΔSW = Δ(Consumer Surplus) + Δ(Producer Surplus) + Δ(Deadweight Loss)

**Key trade-offs**:
1. **Output expansion vs. rent extraction**: Flat-rate increases participation (efficiency gain) but enables greater surplus extraction (redistribution)
2. **Behavioral welfare vs. revealed preference**: Standard welfare respects consumer choices; behavioral welfare corrects for systematic biases (Bernheim & Rangel 2009: "choice-based" welfare when preferences inconsistent)
3. **Ex-ante vs. ex-post assessment**: Ex-ante consumers may prefer flat-rate for insurance value; ex-post many would have been better off with usage-based. Correct welfare standard ambiguous.

**Regulatory implications**: Disclosure requirements forcing transparent comparison. Cooling-off periods allowing reconsideration. Default rules protecting most vulnerable. Mandatory simple options requiring straightforward pay-per-use alternatives.

### Contradictions and Debates

**Price discrimination: Harmful or beneficial?**
- **Pro** (Varian 1989; Stole 2007): Expands output serving low-value customers. Enables provision of goods unprofitable under uniform pricing. Can increase total welfare if output expansion sufficient.
- **Anti** (Armstrong & Vickers 2001; Stole 2002): Extracts consumer surplus without efficiency gains. May reduce welfare if demand reduction from high prices > gains from serving low-price consumers. Distributional concerns.
- **Synthesis**: Effect depends on market structure, type of discrimination, cost structure, information structure.

**Behavioral biases: Should policy correct them?**
- **Libertarian paternalism** (Thaler & Sunstein 2008): Nudges help without restricting choice. Disclosure and defaults sufficient. Preserve consumer sovereignty.
- **Hard paternalism**: Systematic biases justify bans or restrictions. Disclosure often ineffective. Protecting vulnerable populations requires intervention.
- **Anti-paternalism**: Individuals best judges of own welfare. Regulators lack information. Risk of unintended consequences.

**Flat-rate vs. usage-based: Which is more efficient?**
- **Pro-flat-rate**: Lower transaction costs, encourages innovation, consumer preference for certainty has value, administrative simplicity
- **Pro-usage-based**: Better aligns price with cost, reduces overconsumption and congestion, more equitable, enables price signals for capacity management
- **Contingent efficiency**: Answer depends on ratio of transaction costs to metering costs, variance in usage, capacity constraints, consumer sophistication

### Gaps in Existing Theory for LLM Context

**Novel characteristics of LLM services**:
1. **Non-linear value generation**: Value per token varies dramatically by use case. Quality variation within single generation. Context-dependent value. **Existing theory gap**: Most models assume stable value-per-unit.

2. **Capacity constraints with queue uncertainty**: Variable latency based on load. Priority access mechanisms. **Existing theory gap**: Two-sided market literature assumes fixed quality of service.

3. **Compounding credence good problems**: Quality unobservable even to sophisticated users. Stochastic outputs complicate learning. Model capabilities opaque. **Existing theory gap**: Credence good theory assumes stable expert-client relationship.

4. **Training data externalities**: User queries provide value back to provider. Creates reciprocal value flow unlike traditional services. **Existing theory gap**: Limited theory on "reverse" network effects in pricing.

**Theoretical tools needed**:
1. Dynamic quality revelation models: How do users learn about LLM quality over time? What pricing enables efficient learning?
2. Multi-dimensional bundling: Quality tiers × usage limits × latency guarantees
3. Welfare analysis with behavioral biases AND asymmetric information: Most behavioral literature assumes symmetric information; most information economics assumes rational actors; LLMs combine both
4. Long-run competitive dynamics: How does flat-rate vs. usage-based affect market concentration?

### Implications for Optimal LLM Pricing Design

**Efficiency-oriented design principles**:
1. **Hybrid pricing structures**: Combine fixed access fee with usage-based marginal pricing. Two-part tariffs align incentives while providing certainty.
2. **Quality-differentiated tiers**: Separate pricing by latency guarantees and model capabilities. Enables self-selection and reduces information asymmetry.
3. **Transparent cost disclosure**: Real-time cost estimation before generation. Historical usage analytics. Comparison tools across pricing plans.
4. **Commitment mechanisms with flexibility**: Allow users to pre-commit but with periodic re-optimization. Cooling-off periods and easy switching.

**Welfare-enhancing regulatory interventions**:
1. **Mandatory simple options**: Require availability of straightforward pay-per-token pricing. Prevent pure bundling exploiting biases. Reference point for comparison.
2. **Usage-based revenue sharing**: When LLM outputs create documented value, allow performance-based pricing. Aligns incentives between provider and user.
3. **Capacity allocation mechanisms**: Priority access pricing during peak times. Interruptible service at discounts.
4. **Consumer protection standards**: Disclosure of quality limitations. Accuracy benchmarks for credence attributes.

### Implications for Scholarly Argument

**Economic literature provides strong normative foundation** for regulatory intervention in LLM pricing:
1. **Flat-rate bias exploitation**: Systematic evidence that consumers overestimate usage and prefer flat-rates beyond economically rational levels
2. **Credence good characteristics**: Severe information asymmetries justify protective regulation
3. **Bundling power**: Economies of aggregation can be efficiency-enhancing but raise competitive and distributional concerns
4. **Behavioral welfare standard**: When preferences are inconsistent (ex-ante vs. ex-post), paternalistic intervention may be justified

**The literature suggests focusing on both quantity and quality ambiguity**, as they operate through different economic mechanisms:
- **Quantity ambiguity**: Creates behavioral biases (overestimation, sunk cost), transaction utility effects, and insurance demand
- **Quality ambiguity**: Manifests credence good problems, adverse selection, and moral hazard

**Key insight**: The combination of flat-rate bias (behavioral economics) and credence good characteristics (information economics) creates particularly severe consumer protection concerns, as providers can exploit both behavioral tendencies and information asymmetries simultaneously.

### Research Gaps

**Critical gaps in economic literature for LLM context**:
1. **No models for stochastic service quality**: Existing theory addresses deterministic quality or complete failure, not probabilistic performance ranges
2. **Limited capacity-constrained two-sided market models**: Most assume unlimited capacity or fixed quality
3. **No theory combining behavioral biases with asymmetric information**: Typically addressed separately
4. **Limited dynamic learning models**: How consumers learn about quality over time under uncertainty
5. **No framework for reciprocal value generation**: Training data externalities create unique feedback loops

**Empirical research needed**:
1. Experimental studies on LLM pricing model preferences with full information
2. Long-term welfare tracking under different pricing structures
3. Market concentration effects of different pricing models
4. Distributional impacts across income, education, and demographic groups

---

## SYNTHESIS: IMPLICATIONS FOR REGULATORY APPROACH

### Central Findings Across Research Questions

**The evidence converges on several critical conclusions:**

**1. Capacity ambiguity is primarily business choice, not technical necessity**
- Enterprise "Provisioned Throughput" offerings prove guaranteed capacity is technically feasible
- Providers demonstrate transparency capability through API documentation
- Choice to maintain consumer opacity serves customer acquisition and cost management
- Technical constraints affect pricing but not fundamental possibility of transparency

**2. "Unlimited" marketing exploits well-documented behavioral biases**
- Flat-rate bias (Lambrecht & Skiera), sunk cost fallacy (DellaVigna & Malmendier), mental accounting (Thaler)
- Users systematically overestimate usage and prefer certainty
- Providers benefit from 2-12% additional revenue through bias exploitation
- Gym membership evidence directly parallels LLM subscription behavior

**3. LLMs exhibit severe credence good characteristics**
- Quality cannot be evaluated even after consumption (Darby & Karni framework)
- Stochastic outputs compound verification problems
- Creates information asymmetries enabling quality degradation and misrepresentation
- Users particularly vulnerable to capability overclaims

**4. Existing EU frameworks apply but have critical gaps**
- UCPD, Digital Content Directive, AI Act provide foundation
- "Average consumer" standard inadequate for stochastic services
- No regulatory framework for acceptable variability in probabilistic outputs
- Real-time quality variation not addressed by static conformity standards

**5. User behavior divides quantity vs. quality concerns**
- **Quantity restrictions**: Drive strategic behavior, trust erosion, planning uncertainty
- **Quality degradation**: Drive emotional responses, satisfaction issues, expectation management
- Both require regulatory attention through different mechanisms

### Recommended Scholarly Focus: Both Quantity and Quality Ambiguity

**The research supports addressing BOTH dimensions** as they operate through complementary mechanisms:

**Quantity Ambiguity Focus**:
- **Strength**: Clear regulatory precedents (ISP throttling, net neutrality cases)
- **Strength**: Measurable, verifiable through usage monitoring
- **Strength**: Bright-line rules possible ("unlimited" must mean X or disclose limits)
- **Applicability**: UCPD Articles 6-7 on misleading practices directly applicable
- **Evidence**: Strong user complaints, documented throttling events (Claude Code crisis)

**Quality Ambiguity Focus**:
- **Strength**: Addresses novel regulatory challenge of stochastic services
- **Strength**: Captures credence good characteristics unique to AI
- **Strength**: Aligns with AI Act transparency and accuracy requirements
- **Applicability**: Digital Content Directive conformity standards with adaptation needed
- **Evidence**: User satisfaction data, quality degradation complaints (GPT-5 backlash)

**Integrated Approach Recommended**:
- **Quantity ambiguity** as primary regulatory target for near-term intervention (proven frameworks exist)
- **Quality ambiguity** as novel category requiring new regulatory development (Digital Fairness Act opportunity)
- Both create consumer harm through different pathways: planning uncertainty (quantity) vs. expectation management (quality)

### Framework for Regulatory Intervention

**Immediate interventions leveraging existing law**:

**1. UCPD Guidance on "Unlimited" Claims**:
- Commission guidance specifying "unlimited" requires disclosure of:
  - Quality variability ranges (mean, variance, worst-case for key tasks)
  - Throttling triggers with general thresholds (e.g., ">10× typical usage")
  - Appeal processes and restoration timeframes
- Prohibition on "unlimited" marketing combined with undisclosed throttling
- Expansion of Annex I blacklist for LLM-specific practices

**2. Digital Content Directive Enforcement**:
- Challenge "as-is" clauses as unfair terms under UCTD
- Require "conformity with contract" to include statistical performance disclosure
- Model version updates treated as contract modifications requiring notice/opt-out

**3. AI Act Implementation**:
- Interpret "appropriate accuracy levels" to require statistical disclosure
- "Systemic risk" assessment to include quality degradation at scale
- "Consistent performance" to mean bounded variability within disclosed ranges

**Medium-term: Digital Fairness Act Provisions (2026)**:

**1. LLM-Specific Annex I Prohibitions**:
- Claiming capabilities without statistical performance disclosure
- Anthropomorphic marketing without capability limitation disclosure
- "Unlimited" claims without quality variability disclosure
- Degrading service quality without notification/compensation

**2. "Digital Professional Diligence" Standard for AI**:
- Duty to maintain quality within disclosed ranges
- Duty to notify material quality changes (advance notice minimum 14 days)
- Duty to provide human escalation for significant failures

**3. Model Version Stability Rights**:
- Fixed subscription = fixed model version OR notification + opt-out + refund
- Grandfathering for critical use cases

**Long-term: Sector-Specific AI Consumer Regulation**:

**1. Minimum Performance Standards**:
- Statistical disclosure requirements (mean, variance, confidence intervals)
- Mandatory benchmarking on representative tasks (not gaming-prone tests)
- Standardized comparison tools enabling cross-provider evaluation

**2. Quality Guarantee Tiers**:
- "Best effort" tier: Variable quality with statistical disclosure, lower price
- "Guaranteed" tier: SLA with compensation for degradation, higher price
- Consumer choice between price/stability tradeoff

**3. Portability and Interoperability**:
- Export: Conversation history, custom instructions, trained preferences
- Import: Ability to switch providers with configuration transfer
- Standardized prompt formats

**4. Dynamic Pricing-Quality Linkage**:
- If quality varies significantly, price must vary proportionally OR
- Fixed price requires bounded quality variation within disclosed ranges
- Real-time notification of quality degradation with service credits

### Potential Regulatory Pitfalls to Avoid

**1. Guaranteed capacity mandates without pricing flexibility**:
- Would force 3-10× price increases or dramatic usage restrictions
- May reduce accessibility for mass market
- Better approach: Transparency requirements allowing market-based solutions

**2. "Average consumer" standard without adaptation**:
- Inadequate for stochastic services and behavioral biases
- Should incorporate "vulnerable consumer" benchmark
- Requires behavioral insights integration

**3. Information-only transparency**:
- Evidence shows disclosure alone insufficient (behavioral biases persist)
- Must combine with substantive protections (opt-out rights, compensation, cooling-off periods)
- Comparison tools and decision aids necessary

**4. Ex-post only enforcement**:
- Too slow for fast-moving AI industry
- Should incorporate ex-ante requirements (pre-contractual standards)
- Hybrid approach combining both

**5. Fragmented national implementation**:
- EECC experience shows cross-border inconsistency undermines effectiveness
- Requires centralized enforcement (EU AI Office) or strong coordination mechanisms
- Harmonized implementation crucial

### Open Research Questions

**1. Empirical welfare analysis**:
- What is net welfare impact of flat-rate vs. usage-based pricing for LLM services?
- How do different pricing models affect adoption rates, usage intensity, and value creation?
- What are distributional impacts across socioeconomic groups?

**2. Optimal regulatory stringency**:
- What level of transparency maximizes consumer welfare without stifling innovation?
- How should regulations balance access expansion vs. consumer protection?
- What enforcement mechanisms are most cost-effective?

**3. Dynamic effects**:
- How do pricing models affect long-run market structure and competition?
- What are innovation implications of different regulatory approaches?
- How do learning curves and technological progress affect optimal regulation over time?

**4. International coordination**:
- How should EU approach align with other jurisdictions (US, China, UK)?
- What mechanisms facilitate cross-border enforcement?
- How to prevent regulatory arbitrage?

**5. Quality measurement**:
- What metrics should define "acceptable" variability in stochastic services?
- How can quality be monitored without excessive testing costs?
- What role for third-party auditing and certification?

---

## CONCLUSION

This comprehensive research reveals LLM service pricing practices operate at a critical intersection of behavioral economics, information asymmetry, and regulatory innovation. Providers market "unlimited" access while implementing undisclosed throttling—a practice that exploits well-documented flat-rate bias and sunk cost fallacy while creating severe credence good problems in markets with extreme information asymmetry.

**The evidence decisively refutes claims of technical necessity**: enterprise Provisioned Throughput offerings and academic research prove guaranteed capacity is technically feasible. The choice to maintain consumer opacity serves business objectives—customer acquisition, cost management, competitive positioning—not technical constraints.

**Existing EU consumer protection frameworks provide foundation but require adaptation**. UCPD applies to misleading "unlimited" claims. Digital Content Directive addresses conformity. AI Act establishes transparency requirements. Yet critical gaps exist for stochastic service quality, real-time variability, and anthropomorphic expectation management.

**User behavior reveals the human cost**: token anxiety, self-censorship, trust erosion, and emotional responses to forced quality changes. The Claude Code crisis demonstrates ambiguous throttling destroys trust faster than explicit limits. Users adapt to quantity restrictions but resist quality degradation affecting subjective experience.

**The economic literature provides clear normative guidance**: systematic behavioral biases combined with credence good characteristics create particularly severe consumer protection concerns. Flat-rate pricing can be efficiency-enhancing but becomes exploitative when deliberately designed to exploit overconfidence and time-inconsistency, particularly affecting vulnerable populations.

**The Digital Fairness Act (2026) presents timely intervention opportunity** before widespread harm crystallizes. LLM-specific Annex I prohibitions, "digital professional diligence" standards, and model version stability rights can address immediate concerns while sector-specific AI consumer regulation develops longer-term frameworks.

**Recommended scholarly focus**: Address BOTH quantity and quality ambiguity through complementary mechanisms. Quantity ambiguity as primary near-term target leveraging proven frameworks. Quality ambiguity as novel category requiring new regulatory development for stochastic digital services.

The central policy question is not whether guaranteed capacity is possible (clearly yes) but what regulatory approach maximizes consumer welfare while preserving innovation and accessibility. **Transparency requirements rather than capacity mandates**—enabling informed choice, bounded variability disclosure, notification rights, and low-barrier redress—offer the most promising path forward.

LLMs represent a novel regulatory category at the intersection of variable capacity services, information goods, and autonomous systems. Existing EU consumer protection frameworks can apply with adaptation, but the unique combination of stochastic outputs, severe information asymmetries, and anthropomorphic interfaces demands regulatory innovation. The evidence gathered here provides scholarly foundation for that necessary evolution.