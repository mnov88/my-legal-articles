# Phase 2: Source & Argument Extraction by RQ
**Completed:** 2025-11-20 (RQ1)

---

## RQ1: Major AI services are marketed and sold under conditions which make it impossible to determine how much usage is included

### Overview

RQ1 is fundamentally an **empirical claim** requiring documentation that AI service providers systematically use vague, undefined, or mathematically impossible terms when describing usage limits. The research demonstrates this through: (1) systematic documentation of actual provider pricing pages and terms; (2) identification of linguistic patterns (undefined baselines, comparative claims without references, multipliers of undefined quantities); (3) behavioral evidence from users; (4) technical analysis showing this is business choice not technical necessity.

---

## Sub-Topics & Arguments Discovered

### 1. Systematic Use of Undefined Baselines Across All Major Providers

**Main Argument:** All major AI service providers (OpenAI, Anthropic, Microsoft, Google) systematically employ undefined baselines when describing usage limits, making it impossible for consumers to determine what they are purchasing. The pattern is not accidental but systematic across the industry.

**Evidence Type:** Direct documentation from provider pricing pages and terms of service

**Found in:**
- [[EU consumer protection law and vague AI service pricing - Claude.md]] - Section II "Documented pricing practices of major AI service providers"
- [[LLM Services Pricing Practices and Consumer Protection Law - Claude.md]] - Research Question 2 "Comprehensive Provider Mapping"

**Specific Provider Evidence Documented:**

| Provider | Pricing Tier | Vague Language Used | What's Undefined | Date Accessed |
|----------|-------------|---------------------|------------------|---------------|
| **OpenAI ChatGPT** | Free | "Limited access to GPT-5 (with limits)" | No numerical limits specified | Oct 21, 2025 |
| OpenAI ChatGPT Plus | $20/month | "Access to higher GPT-5 limits" | What "higher" means; baseline not defined | Oct 21, 2025 |
| OpenAI ChatGPT Go | ₹399/month | "Extended access" / "Enjoy more usage" / "Create more images" | No specific numbers; "more" undefined | Oct 21, 2025 |
| OpenAI (Help Center) | Plus subscriptions | "Limits may vary based on system conditions" | What conditions; how they affect limits | Oct 21, 2025 |
| OpenAI (Help Center) | Plus subscriptions | "Currently dynamically adjusting usage caps" | Dynamic adjustment formula not disclosed | Oct 21, 2025 |
| **Anthropic Claude Pro** | $20/month | "Additional usage limits apply" | No further specification provided | Oct 21, 2025 |
| Anthropic Claude Max 5x | $100/month | "5x higher usage limits" | Base unit (1x) never defined | Oct 21, 2025 |
| Anthropic Claude Max 20x | $200/month | "20x higher usage limits" | Base unit (1x) never defined | Oct 21, 2025 |
| Anthropic (Retroactive) | Pro/Max (Aug 2025) | "New weekly rate limits" imposed | Introduced without prior disclosure | Aug 2025 |
| **Microsoft Copilot** | Free | "Can only be used during non-peak times" | "Non-peak times" undefined | Oct 21, 2025 |
| Microsoft Copilot | Free | "Paid users have priority...you might not be able to use it every time" | Creates complete service uncertainty | Oct 21, 2025 |
| Microsoft Copilot Pro | $20/month | "Priority access" / "More usage" / "Faster response speeds" | "More usage" undefined; no baseline | Oct 21, 2025 |
| Microsoft (Official Response) | Copilot Voice | "Unable to view differences between free and paid versions" | Admitted inability to specify usage differences | Oct 21, 2025 |
| **Google Gemini Advanced** | $19.99/month | "Higher-quality outputs" / "longer prompts" | Usage limits not prominently displayed | Oct 21, 2025 |
| **Perplexity AI** (Exception) | Free | "5 Pro searches per day" | **Specific number provided** | Oct 21, 2025 |
| Perplexity AI Pro | $20/month | "300+ Pro Searches Daily" | **Specific minimum provided** | Oct 21, 2025 |
| Perplexity AI Max | $200/month | "Unlimited Access" | Claims unlimited | Oct 21, 2025 |

**Key Pattern Identified:** Community-reported limits for OpenAI (approximately 80 messages/3 hours for GPT-4o, 40 messages/3 hours for GPT-4) exist but are **NOT disclosed on pricing pages**, demonstrating intentional opacity despite internal knowledge of limits.

**Counter-Example:** Google Gemini API provides transparent free tier limits ("15 requests/minute, 1M tokens/minute, 1,500 requests/day") and Perplexity specifies actual numbers, proving **technical feasibility of transparency**.

---

### 2. Systematic Use of Comparative Language Without Reference Points

**Main Argument:** Providers systematically use comparative terms ("more," "higher," "extended") without specifying the baseline for comparison, rendering the comparisons meaningless for consumer decision-making.

**Found in:** Both main RQ1 documents

**Linguistic Patterns Identified:**

| Comparative Term | Providers Using It | Logical Problem |
|-----------------|-------------------|-----------------|
| "Higher limits" | OpenAI, Anthropic | Higher than what? Baseline not disclosed |
| "More usage" | OpenAI, Microsoft | More than what quantity? |
| "Extended access" | OpenAI | Extended beyond what duration/amount? |
| "5x higher" | Anthropic | 5× what baseline? Base unit undefined |
| "20x higher" | Anthropic | 20× what baseline? Base unit undefined |
| "Priority access" | Microsoft | Priority over whom under what conditions? |

**Mathematical Impossibility Argument:** The documents establish that these are not mere transparency failures but mathematical impossibilities:
- **Multiplying an undefined variable produces undefined result**: "5x" × (undefined baseline) = undefined outcome
- **Consumers cannot calculate what they're purchasing**: If 1x is unknown, 5x is equally unknown
- **Differs from calculable comparisons**: Unlike "5x faster processing" (measurable benchmarks exist) or "5x more vitamin C than product X" (chemical analysis possible)

**Found in:**
- [[EU consumer protection law and vague AI service pricing - Claude.md]] - Section "The mathematical impossibility argument"
- [[EU consumer protection law and vague AI service pricing - Claude.md]] - Section "Specific issues with quantifying '5x' an undefined baseline"

---

### 3. Dynamic/Variable Limits Disclosed Only After Purchase

**Main Argument:** Even when providers acknowledge limits exist, they describe them as "dynamic," "variable," or "based on system conditions" without disclosing the factors, formula, or typical ranges affecting these limits.

**Evidence:**

**OpenAI Statements:**
- "Limits may vary based on system conditions" - conditions not specified
- "Currently dynamically adjusting usage caps for GPT-4 as we learn more about demand and system performance" - adjustment criteria not disclosed
- "Plus subscriptions may include usage limits such as message caps, especially during high demand" - "high demand" threshold undefined

**Anthropic Actions:**
- August 2025: Retroactively introduced "new weekly rate limits" for Claude Pro and Max
- Justification: Curb "power users running Claude Code continuously in the background, 24/7"
- **Critical flaw**: Limits imposed on paying customers without prior disclosure at contract conclusion

**Microsoft Admission:**
- Official customer service response: "Since this feature is a new feature information that has just been launched recently... we are temporarily unable to view the differences between the free and paid versions and the corresponding usage"
- **Significance**: Provider admits inability to specify what consumers are purchasing

---

### 4. Mathematical Impossibility: Three Scenarios

**Main Argument:** Undefined baseline multiplier claims present unique problems beyond conventional transparency violations - they may involve information that doesn't exist in determinable form even for the trader.

**Found in:** [[EU consumer protection law and vague AI service pricing - Claude.md]] - Section "The mathematical impossibility argument"

**Three Impossibility Scenarios Identified:**

**Scenario 1: No Defined Baseline Exists**
- Free tier operates on undefined "fair use" policy or "system availability" basis
- "5x free tier" cannot be calculated if free tier has no specified limit
- This is **mathematical indeterminacy**, not transparency failure
- No determinate value exists to disclose

**Scenario 2: Baseline Varies Per User or Time Period**
- Free tier usage varies based on undisclosed "system conditions," "demand," or individualized factors
- Baseline is not constant but variable
- "5x" of variable baseline produces variable result
- Requires disclosure of: (a) all factors affecting baseline; (b) formula for calculating baseline; (c) method for consumers to determine their individual baseline
- None of these disclosures are provided

**Scenario 3: Claimed Multiplier is Average/Approximation, Not Guarantee**
- "5x" may represent average, approximation, or maximum rather than guaranteed minimum
- Consumer law interprets claims in favor of consumers - "5x more" understood as guarantee
- If actual usage is less than 5x, constitutes misleading action
- Providers don't disclose whether multiplier is guarantee, average, or maximum

---

### 5. Disconnect Between API Transparency and Consumer Subscription Opacity

**Main Argument:** The same providers who offer transparent, detailed rate limits for API/developer products maintain systematic opacity for consumer subscriptions, demonstrating this is **business model choice**, not technical necessity.

**Evidence:**

**Google Gemini API** (Developer Product):
- **Free tier**: "15 requests per minute, 1 million tokens per minute, and 1,500 requests per day"
- **Specific rate limits published for each model**
- Complete transparency for developers

**Google Gemini Advanced** (Consumer Product):
- Uses vague language: "higher-quality outputs, access to better models, or longer prompts"
- Usage limits not prominently displayed
- Same company, different transparency standards

**OpenAI API** (Developer Product):
- Token-based pricing: $2.50-$10.00 per million tokens for GPT-5
- Clear, calculable costs

**OpenAI ChatGPT** (Consumer Product):
- "Higher limits" - undefined
- "Extended access" - unspecified
- Community-reported limits exist but not disclosed

**Significance:** This disconnect proves:
1. **Technical capability exists**: Providers CAN specify limits precisely (they do for APIs)
2. **Choice of opacity**: Consumer subscription opacity is deliberate business decision
3. **Different treatment**: Sophisticated developer customers get transparency; mass consumers get vagueness

**Found in:** [[LLM Services Pricing Practices and Consumer Protection Law - Claude.md]] - Research Question 4 "Technical Necessity vs. Business Choice"

---

### 6. Behavioral Evidence: User Reactions and Information Asymmetry

**Main Argument:** User testimony and behavioral evidence demonstrate that vague usage limits create anxiety, self-censorship, monitoring burdens, and inability to plan workflows.

**Found in:** [[LLM Services Pricing Practices and Consumer Protection Law - Claude.md]] - Research Question 1 "User Behavior Under Different Pricing Models"

**Documented User Behaviors:**

**"Token Anxiety" / "Metered Mindset" Phenomenon:**
- Constant mental calculation of costs creating cognitive overhead
- Self-censorship: avoiding follow-up questions, crafting shorter prompts
- Abstaining from exploratory conversations that might "waste" quota
- Developer testimony: Creating monitoring tools to "dodge usage cut-offs"
- Community projects: "Claude Code Usage Monitor" emerged to track consumption in real-time

**Evidence Source:** Academic foundation from telecommunications research (Krämer & Wiewiorra, 2012; Uhrich et al., 2013) identifying four mechanisms:
1. **Taximeter effect**: Disutility from perceiving marginal costs
2. **Insurance effect**: Willingness to pay premiums for cost predictability
3. **Overestimation effect**: Tendency to overestimate usage
4. **Flexibility effect**: Resistance to perceived inflexibility

**Sunk Cost Fallacy in Subscription Behavior:**
- **Zhang et al. (2025)** in *Journal of the Association for Information Systems*: Box office revenues increased 12-35% after downward price adjustment
- **Wharton Study (2020)**: Members increased purchases by $27/month on average; only one-third attributable to economic benefits; two-thirds from "becoming a member per se" (sunk cost fallacy)
- Effect negatively correlated with program benefits - higher sunk costs led to more consumption regardless of value
- ChatGPT Pro users ($200/month) report pressure to maximize usage
- Users report making "over $1,000 worth of calls (measured in API pricing) in a single day" to justify expense

**Case Study: Anthropic Claude Code Crisis (July 2025):**
- Introduced weekly limits without announcement
- Affected developers mid-project
- Created workflow disruption for paying customers
- Demonstrates: "Ambiguous throttling destroys trust faster than explicit limits"

**Case Study: GPT-5 Rollout Quality vs. Quantity Distinction:**
- Limited ChatGPT Plus users to 200 messages per week (quantity restriction)
- Reddit thread "GPT-5 is horrible" - 3,200+ upvotes, 1,400 comments (quality degradation)
- Paradox: Technical performance improved (94.6% on AIME 2025 Math Exam) while user satisfaction plummeted
- Users described model as "cold," "robotic," "soulless" - loss of "conversational warmth"
- Users report "mourning" GPT-4o "like losing a friend"
- **Finding**: Users adapt to quantity restrictions but emotionally resist forced quality changes

**Behavioral Adaptations to Uncertainty:**
- Creating monitoring tools
- Timing usage to reset windows
- Batching queries
- Account sharing (policy violation but widely reported)
- Strategic behavior that wouldn't be necessary with transparent limits

---

### 7. Provider Usage Data Revealing Usage Patterns

**Main Argument:** Limited provider-disclosed usage data shows behavioral shifts and actual usage patterns that contradict marketing claims.

**Found in:** [[LLM Services Pricing Practices and Consumer Protection Law - Claude.md]] - Research Question 1, subsection "Provider Usage Data"

**Anthropic Economic Index (August 2025)** - Analysis of 1 million Claude.ai conversations:
- **Behavioral shift toward delegation**: 27% → 39% "directive" (full task delegation) interactions in 8 months
- **Enterprise automation dominates**: 77% pure automation in API usage vs. ~50% on consumer platforms
- Growing trust drives increased delegation

**OpenAI Data (July 2025)** - 700 million weekly users:
- 18 billion messages weekly (2.5 billion daily)
- **Personal vs. work shift**: 73% personal use (up from 53% in June 2024), 27% work
- **Top use cases**: "Asking" for advice (49%), "Doing" tasks (40%)
- Consumer satisfaction highest with augmentation/collaboration, not full automation

**Democratization-Divergence Paradox:**
- OpenAI data shows fastest growth in low- and middle-income countries with closing gender gaps (democratization)
- Anthropic data reveals AI usage correlates with GDP (0.7% increase per 1% GDP growth) - wealthy nations use more intensively (concentration)
- **Resolution**: Consumer AI democratizes access while enterprise AI concentrates competitive advantages - dual trajectories creating new inequality

---

### 8. Technical Analysis: Capacity Ambiguity as Business Choice, Not Technical Necessity

**Main Argument:** Comprehensive technical analysis demonstrates that capacity ambiguity in LLM services is primarily a business model choice rather than strict technical necessity.

**Found in:** [[LLM Services Pricing Practices and Consumer Protection Law - Claude.md]] - Research Question 4 "Technical Reality and Necessity of Ambiguity"

**Technical Capability Evidence:**

**SLA-Compliant Serving Research:**
- Academic research demonstrates **technical feasibility** of providing guaranteed capacity with Service Level Agreements (SLAs)
- State-of-the-art research shows LLM serving can be made SLA-compliant
- Conclusion: "Capacity ambiguity is primarily a business model choice rather than strict technical necessity"

**Cost Structure Reality:**
- **Operational Cost Reality**: Real, non-zero variable costs (electricity, GPU cycles, bandwidth)
- **Cost Decline**: Inference costs declining rapidly due to optimization
- **Model Complexity**: Variable costs depend on model size, query complexity, output tokens

**Technical Sources of Variability:**
- Agentic workflows creating unpredictable multi-stage costs
- Dynamic batching and KV caching affecting per-user attribution
- Hardware variability (CPU vs. GPU performance differences)
- Workload co-location impacts

**Critical Finding:** Despite these sources of variability, technical solutions exist for providing guarantees. The choice NOT to provide guarantees is business decision, not technical limitation.

**Rate Limiting Infrastructure:**
- Providers demonstrably have sophisticated rate limiting and capacity management infrastructure
- They use it to enforce (undisclosed) limits
- Same infrastructure could provide transparent guarantees
- **Conclusion**: Technical capability exists; transparency is policy choice

---

### 9. Information Asymmetry Across Pricing Models

**Main Argument:** Different pricing models create distinct types and severities of information asymmetry, all documented across economic analysis documents.

**Found in:**
- [[RQ1-Information-Asymmetry.md]] (Tier-Based)
- [[RQ1-Information-Asymmetry.md]] (Call-Based)
- [[information-asymmetry-decision-making.md]] (Credit-Based)
- [[RQ1-Information-Asymmetry-Decision-Making.pdf]] (Token-Based)

**Information Asymmetry Mechanisms by Pricing Model:**

**Tier-Based Pricing:**
- **Temporal information gap**: Providers know typical usage trajectories; consumers cannot predict
- **Platform uncertainty**: Difficulty evaluating reliability, pricing stability, long-term value
- **Seller uncertainty**: In two-sided markets, uncertainty about service quality
- **Product uncertainty**: Cannot assess whether capabilities match needs before extended use
- **Bounded rationality**: Consumers cannot accurately assess congestion levels, usage requirements, or optimal tier selection
- **Feature bundling complexity**: Tiers combine usage limits with feature access, making direct price comparison difficult
- **Hidden threshold effects**: Transition points between tiers create non-obvious cost implications
- **Temporal pricing variations**: "Value migration" where features shift to higher tiers over time

**Credit-Based Pricing:**
- **Decoupling purchase from consumption**: Mental accounting manipulation
- **Opaque credit-to-service value ratios**: Consumers don't understand what credit purchases
- **Sunk cost exploitation**: Already-purchased credits create pressure to consume
- **Breakage profit**: Unused credits that expire represent pure profit

**Call-Based/API Pricing:**
- **Variable complexity per call**: Cannot predict costs when call complexity varies
- **Hidden backend optimization**: Dynamic batching, KV caching affect costs but invisible to user
- **Cross-user cost dependencies**: User A's cost depends on User B's concurrent queries

**Token-Based Pricing:**
- **Token as non-intuitive unit**: Consumers lack innate understanding of token value
- **Model-specific variability**: Same task uses different tokens across models (GPT-5 uses 90% fewer tokens than Claude Opus 4.1 for same task)
- **Hardware variability**: Cost per token varies 9x-24x depending on CPU/GPU/workload co-location

---

## Empirical Data Sources Referenced

### Provider Pricing Pages (Primary Sources)

| Provider | Source Type | Access Date | What Was Documented |
|----------|------------|-------------|---------------------|
| OpenAI ChatGPT pricing page | Public pricing page | Oct 21, 2025 | Free, Plus, Go tier descriptions |
| OpenAI Help Center | Public support documentation | Oct 21, 2025 | Usage limit policies, dynamic adjustment statements |
| Anthropic Claude pricing page | Public pricing page | Oct 21, 2025 | Pro, Max 5x, Max 20x tier descriptions |
| Anthropic Blog | Public blog post | Aug 2025 | Announcement of retroactive weekly rate limits |
| Microsoft Copilot pricing | Public pricing page | Oct 21, 2025 | Free and Pro tier descriptions |
| Microsoft Official Response | Customer service communication | Oct 21, 2025 | Admission of inability to specify usage differences |
| Google Gemini Advanced | Public pricing page | Oct 21, 2025 | Advanced tier description |
| Google Gemini API docs | Public API documentation | Oct 21, 2025 | Transparent free tier rate limits |
| Perplexity AI pricing | Public pricing page | Oct 21, 2025 | Free, Pro, Max tier specifications |

### Community-Reported Data

| Source | Type | What It Provides |
|--------|------|------------------|
| Reddit discussions | User testimony | Reported limits: ~80 messages/3 hours GPT-4o, ~40 messages/3 hours GPT-4 |
| Developer forums | User testimony | Self-censorship behaviors, token anxiety, monitoring tool creation |
| Claude Code Usage Monitor | Community project | Evidence of user-created tools to track undisclosed limits |

### Academic Research Cited

| Source | Finding | Application to RQ1 |
|--------|---------|-------------------|
| Krämer & Wiewiorra (2012) | Flat-rate bias mechanisms (taximeter, insurance, overestimation, flexibility effects) | Explains user preference for subscription despite potential irrationality |
| Uhrich et al. (2013) | Flat-rate preference research | Behavioral foundation for understanding pricing model reactions |
| Zhang et al. (2025), *Journal of the Association for Information Systems* | Box office revenues increased 12-35% after price reduction; sunk cost effect | Demonstrates sunk cost fallacy in subscription behavior |
| Wharton Study (2020) | Members increased purchases $27/month; 2/3 from membership itself | Evidence of sunk cost driving consumption |

### Provider-Disclosed Usage Data

| Source | Sample Size | Key Finding |
|--------|------------|-------------|
| Anthropic Economic Index | 1 million Claude.ai conversations | 27% → 39% directive interactions (8-month period); 77% API automation |
| OpenAI Usage Data | 700 million weekly users, 18 billion weekly messages | 73% personal use, 49% "asking" use case, satisfaction with collaboration |

---

## Academic/Research Frameworks Establishing Information Asymmetry

### Credence Goods Framework

**Source:** Referenced in [[RQ1-Information-Asymmetry.md]] (Tier-Based)

**Application:** Online services exhibit credence goods characteristics where consumers cannot easily verify whether service level received matches what was promised. This creates opportunities for:
- **Overprovision incentives**: Encouraging subscription to higher tiers than necessary (analogous to medical overtreatment)
- **Underprovisioning through tier design**: Entry tiers with artificially restrictive limits to force upgrades
- **Quality verification challenges**: Cannot objectively assess whether performance issues stem from tier choice, network conditions, or platform degradation

### Bounded Rationality Theory

**Sources:**
- Telecommunications research on subscription decisions
- Music streaming behavioral studies

**Application:** Consumers cannot consistently evaluate:
- Congestion levels
- Utility of different tiers
- Future usage needs
- Intertemporal optimization

**Finding:** "Consumers exhibit significant bounded rationality in subscription decisions... cannot accurately assess congestion levels or utility, leading to systematic deviations from optimal choices"

### Platform Uncertainty Framework

**Three Dimensions Identified:**
1. **Platform uncertainty**: Difficulty evaluating platform reliability, pricing stability, long-term value proposition
2. **Seller uncertainty**: In two-sided markets, uncertainty about service quality and provider behavior
3. **Product uncertainty**: Inability to assess whether service capabilities match actual needs before extended use

**Source:** Platform market literature on digital services

### Temporal Information Gap

**Concept:** Providers possess superior knowledge about typical usage trajectories, pricing optimization strategies, and statistical distribution of consumer behavior at time of purchase. Consumers lack this information about their own future needs.

**Result:** Creates systematic advantage for providers in tier design and pricing optimization.

---

## Key Tests & Frameworks Established for RQ1

### The "Mathematical Impossibility" Test

**Established in:** [[EU consumer protection law and vague AI service pricing - Claude.md]]

**Description:** Undefined baseline multiplier claims are not merely transparency violations (information exists but poorly communicated) but mathematical impossibilities where information may not exist in determinable form.

**Three-Part Test:**
1. **Does defined baseline exist?** If no → mathematical indeterminacy (5x undefined = undefined)
2. **Is baseline constant or variable?** If variable without disclosed formula → consumers cannot calculate promised usage
3. **Is multiplier guarantee or approximation?** If not disclosed → consumers misled about nature of claim

**Application:** Used to demonstrate that claims like "5x higher usage limits" or "20x more usage" without defining base unit (1x) are categorically different from standard transparency violations. Standard remedy (clearer disclosure) cannot fix mathematical impossibility.

**Significance:** Distinguishes AI service vagueness from other types of consumer information problems.

### The API/Consumer Transparency Disconnect Test

**Established in:** [[LLM Services Pricing Practices and Consumer Protection Law - Claude.md]]

**Description:** Comparing transparency provided to developer/API customers versus consumer subscription customers for same provider.

**Test Elements:**
1. **Does provider offer both API and consumer products?**
2. **What level of specification does API product provide?** (rate limits, token costs, etc.)
3. **What level of specification does consumer product provide?**
4. **If disparity exists**, does it prove technical capability exists for transparency?

**Application to Providers:**
- **Google**: Gemini API (transparent: "15 requests/min, 1M tokens/min, 1,500/day") vs. Gemini Advanced (vague: "higher quality outputs")
- **OpenAI**: API (transparent: "$2.50-$10/M tokens") vs. ChatGPT (vague: "higher limits," "extended access")

**Conclusion:** Disparity proves opacity is business choice, not technical limitation.

### The Quantity vs. Quality Degradation Framework

**Established in:** [[LLM Services Pricing Practices and Consumer Protection Law - Claude.md]] - Research Question 1

**Description:** User complaints and behavioral reactions bifurcate into two distinct categories with different implications.

**Framework:**

| Dimension | Quantity Restrictions | Quality Degradation |
|-----------|---------------------|-------------------|
| **What it is** | Usage limits, throttling, message caps | Model performance changes, personality alterations |
| **Primary complaint** | Unpredictability - cannot plan workflows | Emotional loss - service feels degraded |
| **User adaptation** | Strategic behavior: monitoring tools, timing usage, batching queries | Emotional reaction: dissatisfaction, mourning loss |
| **Example** | GPT-5 rollout: 200 messages/week cap | GPT-5 rollout: Model feels "cold," "robotic," "soulless" |
| **Legal implication** | Violates transparency/foreseeability requirements | May violate conformity/quality expectations |

**Key Finding:** "Users adapt to quantity restrictions through strategic behavior but react with emotional intensity to forced quality changes affecting subjective experience. Users tolerate quality issues if given control but strongly resist forced changes and access limitations."

**Application:** Demonstrates that RQ1 documentation of usage limit ambiguity affects not just rational economic decision-making but creates psychological costs (anxiety, loss of control, inability to plan).

---

## Research Gaps Identified for RQ1

**From:** [[LLM Services Pricing Practices and Consumer Protection Law - Claude.md]] - Research Question 1, "Research Gaps" section

### Methodological Gaps

1. **No longitudinal studies** tracking individual user behavior across 12+ months under different pricing models
2. **No quantitative metrics** on:
   - Prompt length changes under usage uncertainty
   - Query complexity variations based on pricing model
   - Magnitude of self-censorship behavior
3. **No cognitive load studies** measuring mental overhead of token tracking or decision fatigue
4. **No cross-platform comparative studies** controlling for model quality differences
5. **Limited demographic analysis** of how pricing preferences vary by income, profession, technical sophistication

### Empirical Data Gaps

1. **Provider data suffers from selection bias**: Excludes churned users who left due to dissatisfaction
2. **Short time windows**: Maximum 8 months of data (Anthropic Economic Index)
3. **No peer-reviewed studies** specifically examining LLM pricing behavior
4. **Most flat-rate bias research predates LLMs**: Cannot directly extrapolate to AI services

### Evidence Limitations

1. **Community-reported limits are estimates**: Not officially confirmed by providers
2. **Provider statements captured at single point in time**: May change without documentation
3. **User testimony from Reddit/forums**: Self-selected sample, potential biases
4. **No independent verification** of claimed usage limits through systematic testing

---

## Integration with Other RQs

### Connection to RQ2 (EU Law Violations)

RQ1's empirical documentation provides the **factual predicate** for RQ2's legal analysis:
- RQ1 documents that providers use undefined baselines, vague comparatives, undisclosed dynamic limits
- RQ2 applies legal framework (UCPD, UCTD, CRD) to these documented practices
- RQ1 establishes "mathematical impossibility" → RQ2 uses this to argue transparency cannot be achieved through clearer drafting alone

### Connection to RQ3 (Alternative Models Problematic)

RQ1's behavioral evidence informs RQ3's analysis:
- Token anxiety, metered mindset documented in RQ1 → RQ3 analyzes whether transparent usage-based models solve or worsen problems
- Sunk cost fallacy evidence from RQ1 → RQ3 examines whether subscription models exploit behavioral biases
- User preference for predictability (RQ1) → RQ3 evaluates efficiency costs of flat-rate models

### Connection to RQ4 (Other Industries)

RQ1's technical analysis (business choice vs. necessity) → RQ4 examines whether solutions from telecoms/utilities are transferable or whether AI's technical characteristics create unique constraints

---

## Summary: Core Evidence Establishing RQ1

**Empirical Claim:** Major AI services ARE marketed under conditions making usage determination impossible

**Evidence Strength:** **STRONG**
- Systematic documentation across all major providers (OpenAI, Anthropic, Microsoft, Google)
- Direct quotes from pricing pages and terms of service
- Multiple types of vagueness: undefined baselines, comparative without references, multipliers of unknowns, dynamic limits without formulas
- Provider admissions (Microsoft: "unable to view differences")
- Counter-examples proving feasibility (Perplexity numbers, Google API transparency)
- Behavioral confirmation (user anxiety, monitoring tools, community-reported limits)
- Technical analysis showing choice not necessity

**Key Documents:**
1. **EU consumer protection law and vague AI service pricing - Claude.md** - Most systematic provider documentation
2. **LLM Services Pricing Practices and Consumer Protection Law - Claude.md** - Behavioral evidence and technical analysis
3. **Economic analysis RQ1 files** - Information asymmetry theoretical frameworks

**Strongest Single Piece of Evidence:** Anthropic's "20x higher usage limits" for $200/month tier without ever defining base unit (1x) - represents pure mathematical impossibility of consumer evaluation.

---

*RQ1 Extraction Complete - Ready for User Review*
