<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# AI Pricing Models in 2025: A Comprehensive Analysis

Based on extensive research into current AI-assisted services, I've identified the pricing landscape, cost management strategies, and optimal approaches for determining API pricing. Here's a detailed report on the findings.

## Executive Summary

The AI services market is experiencing explosive growth (from \$273.6B in 2025 to \$5.26T by 2035), with pricing models evolving rapidly to address the unique challenges of AI cost structures. **Hybrid pricing models combining subscription and usage-based elements have emerged as the dominant approach**, adopted by 46-55% of companies, as they balance revenue predictability with fair cost allocation.[^1][^2][^3]

## Current Pricing Models for AI Services

### 1. Token-Based (Consumption) Pricing

Token-based pricing is the **industry standard for LLM APIs**, where customers pay per token processed (typically per 1,000 tokens). This model directly correlates with computational costs.[^4][^5][^6]

**Typical Pricing (2025):**

- OpenAI GPT-4o: \$0.005 per 1K input tokens, \$0.015 per 1K output tokens[^7]
- Anthropic Claude 3.5 Sonnet: \$20-200/month with usage limits[^7]
- Competitive range: \$0.005-0.06 per 1K tokens[^8]

**Advantages:** Fair cost allocation, transparent, scales with usage, low entry barrier[^2][^9]

**Disadvantages:** Unpredictable costs for customers, difficult forecasting, can become expensive at scale[^10][^11]

### 2. Subscription-Based (Tiered) Pricing

Fixed monthly or annual fees with multiple tiers (typically 3-4 levels: Basic/Professional/Enterprise). This remains popular for general SaaS products with clear feature differentiation.[^12][^13][^14]

**Examples:**

- GitHub Copilot Pro: \$10/month (unlimited completions)[^15][^16]
- Midjourney Standard: \$30/month (~900 images)[^17]

**Advantages:** Predictable revenue, clear upgrade paths, easy for customers to understand[^18][^2]

**Disadvantages:** May not capture heavy usage value, risk of "shelfware" (unused seats), doesn't reflect usage intensity[^13][^18]

### 3. Hybrid Pricing (Subscription + Usage)

**The fastest-growing model**, combining a base subscription fee with usage-based charges for consumption beyond included allowances. This addresses both vendor and customer needs for predictability and fairness.[^19][^20][^21][^2]

**Implementation Structure:**

- Base monthly fee covers 60-80% of typical usage
- Graduated overage pricing (not punitive)
- Usage alerts at 50%, 80%, 100% thresholds[^20][^22]

**Advantages:** Revenue predictability plus flexibility, captures heavy users, aligns with customer success[^3][^23][^20]

**Disadvantages:** More complex to implement, requires sophisticated billing infrastructure[^2][^20]

### 4. Freemium Model

Free tier with limited features plus paid premium tiers. Effective for product-led growth strategies, though conversion rates are typically low (1-5%).[^24][^25][^26][^12]

**Best Practices:**

- Implement usage limits rather than removing features entirely
- Provide clear upgrade triggers
- Offer full-feature trials during onboarding[^25][^27]

**Challenges:** High COGS for free users, low conversion rates, risk of cannibalizing paid tiers[^26][^25]

### 5. Value-Based Pricing

Price determined by customer-perceived value and business outcomes rather than production costs. This approach can maximize revenue but requires deep customer understanding.[^28][^29][^2]

**Formula:** Price = Customer Annual Value × (10-20% capture rate)[^28][^2]

**Example:** If an AI tool saves a customer \$100K annually, pricing at \$10-20K aligns with delivered value.

**Advantages:** Maximizes revenue potential, aligns with customer ROI, enables premium positioning[^29][^2][^28]

**Disadvantages:** Difficult to measure accurately, requires extensive customer research, may be hard to justify initially[^30][^28]

### 6. Outcome-Based Pricing (Emerging)

Payment tied to measurable business results such as resolved support tickets, prevented cancellations, or completed transactions. This model is gaining traction despite representing only 10-15% current adoption.[^31][^32][^33][^34]

**Examples:**

- Sierra AI: Pay per resolved customer conversation[^33][^34]
- Zendesk: Charges for automated resolutions[^35]
- Salesforce Agentforce: \$2 per conversation[^31]

**Advantages:** Perfect incentive alignment, customers pay only for results, vendor motivated to optimize performance[^32][^34][^33]

**Disadvantages:** Complex outcome definition, measurement challenges, requires contractual clarity on attribution[^36][^32]

### 7. Agent-Based Pricing (New in 2025)

AI agents priced as "digital workers" with seat-based pricing similar to human employees. Pricing ranges from \$20 to \$2,000 per agent per month depending on capabilities.[^37][^38][^32][^31]

**Rationale:** Easy to understand (like hiring decisions), provides cost predictability, aligns with human labor replacement narrative[^32][^31]

**Considerations:** Actual AI costs can vary significantly, may not reflect work complexity, requires clear agent role definitions[^37][^36]

### 8. Per-User/Per-Seat Pricing

Traditional SaaS model charging per active user or seat. Common in collaborative tools but less suitable for AI services with variable computational costs.[^13][^18]

**Advantages:** Simple billing, scales with team size, predictable costs[^13]

**Disadvantages:** Doesn't reflect usage intensity, can limit collaboration, misses heavy individual users[^18][^13]

## Cost Management and COGS Challenges

### The AI Margin Paradox

AI services face **significantly lower gross margins** compared to traditional SaaS:[^39][^40][^41]

- **Traditional SaaS:** 75-90% gross margin
- **AI-Native SaaS:** 50-60% gross margin (↓20-30 points)
- **LLM Infrastructure Providers:** 40-55% gross margin

**Primary Cost Drivers:**

1. **Inference costs:** 5-10x higher than traditional compute[^42][^39]
2. **GPU infrastructure:** Capital-intensive and expensive to operate[^40][^41]
3. **Token consumption unpredictability:** Variable costs scale with usage[^39][^40]
4. **Model training:** Can exceed \$100M per model[^40]
5. **Data center costs:** Electricity and cooling for GPU clusters[^41]

### Cost Forecasting Challenges

Research reveals significant forecasting difficulties:[^43]

- **85%** of companies miss AI infrastructure forecasts by >25%
- **84%** report 6%+ gross margin erosion due to AI costs
- **26%** experience margin impact of 16% or higher

**Root Causes:**

- Unpredictable token consumption patterns[^39][^40]
- Variable LLM API costs from providers
- Difficulty attributing costs to specific customers or features[^44]
- Hidden costs in prompt engineering and fine-tuning[^39]


## Determining Optimal API Pricing

### Three Primary Approaches

**1. Cost-Plus Pricing**

Formula: `Price = (COGS + Operating Costs) × Markup`

For AI services, typical markup is **3-5x COGS**. This ensures cost recovery but ignores customer value perception.[^45][^29]

**Pros:** Simple to calculate, ensures profitability, transparent cost basis[^45][^30]

**Cons:** May underprice high-value services, ignores competitive positioning, doesn't reflect customer ROI[^30][^28]

**2. Value-Based Pricing (Recommended)**

Formula: `Price = Customer Annual Value × (10-20% capture rate)`[^29][^2][^28]

This approach aligns pricing with business outcomes and maximizes revenue potential when the value proposition is clear.

**Implementation Requirements:**

- Deep customer understanding through interviews and usage analysis
- Quantifiable metrics linking product use to business outcomes
- Case studies demonstrating ROI[^28][^45]

**Pros:** Maximizes revenue, aligns with customer success, enables premium positioning[^29][^28]

**Cons:** Requires significant customer research, hard to measure initially, needs proven ROI[^30][^28]

**3. Competitive Pricing**

Formula: `Price = Market Average × (0.8-1.2 differentiation factor)`

Research 5-10 competitors to establish market benchmarks, then adjust based on feature differentiation.[^46][^45]

**Pros:** Market validation, easier customer comparison, faster go-to-market[^45]

**Cons:** Risk of commoditization, race to bottom, limits differentiation[^45][^30]

### Recommended Hybrid Formula

```
Target Price = MAX(
    Cost-Plus Minimum (COGS × 3),
    Value-Based Optimum (Customer Value × 15%),
    Competitive Floor (Market Average × 0.9)
)
```

This ensures profitability while capturing value and remaining competitive.[^46][^45]

## Eight-Step Pricing Determination Process

**Step 1: Calculate Unit Economics**

- Determine COGS per API call, token, or user
- Include infrastructure, compute, support, and overhead
- Target gross margin: 60-70%+ for AI services[^47][^41]

**Step 2: Understand Your Value Metric**

- Identify what customers value: API calls, tokens, outcomes, time saved
- Ensure metrics are understandable and measurable
- Avoid technical metrics customers don't understand[^2][^46][^45]

**Step 3: Analyze Customer Segments**

- Create 3-4 personas: startups, SMBs, enterprises
- Different segments have varying willingness to pay
- Track usage patterns by segment[^46][^45]

**Step 4: Benchmark Competitive Pricing**

- Research 5-10 competitors thoroughly
- Analyze pricing models and positioning
- Identify gaps and differentiation opportunities[^46][^45]

**Step 5: Choose Pricing Architecture**

- **Hybrid recommended** for most AI services (subscription + usage)
- Consider freemium for product-led growth
- Ensure clear upgrade paths between tiers[^3][^20][^2]

**Step 6: Set Initial Price Points**

- Start higher than minimum—easier to reduce than increase
- Cost-plus: COGS × 3-5x
- Value-based: Customer ROI × 10-20%
- Competitive: ±20% of market rate[^46][^45]

**Step 7: Implement Usage Tracking**

- Real-time metering system for accurate billing
- Customer usage dashboards for transparency
- Automated alerts at usage thresholds (50%, 80%, 100%)[^48][^49][^46]

**Step 8: Test and Iterate**

- A/B test pricing with customer cohorts
- Monitor conversion rates, churn, CAC payback
- Adjust every 3-6 months based on data
- Grandfather existing customers when raising prices[^48][^46]


## Which Pricing Models Work Best?

### By Use Case:

**Early-stage Startups (PLG):** Freemium model

- Low-friction adoption, viral growth potential
- Typical conversion: 1-5% free-to-paid[^24][^26]

**Established SaaS Adding AI:** Hybrid (Subscription + Usage)

- Maintains predictable revenue while capturing variable AI costs
- 15-30% of revenue from usage-based component[^20][^3]

**Pure LLM API Providers:** Token-based (Consumption)

- Industry standard, transparent cost pass-through
- Pricing: \$0.005-0.06 per 1K tokens[^5][^8]

**Enterprise-Focused Solutions:** Subscription (Tiered)

- Predictable budgets, clear feature differentiation
- 40-60% logo retention typical[^18]

**Developer Tools/APIs:** Hybrid (Base + Overages)

- Developers want flexibility with cost control
- 20-40% expansion revenue potential[^20][^46]

**AI Agents Replacing Human Work:** Agent-based or Outcome-based

- Clear value proposition vs. hiring costs
- Easy ROI calculation[^36][^31][^32]

**Image/Video Generation:** Tiered Subscription

- GPU costs make pure metered pricing risky
- Unlimited tiers encourage experimentation[^50][^17]


### Success Factors by Model

**Hybrid Pricing:**

- Shows **highest customer satisfaction** and predictable revenue
- Requires transparent usage tracking and reasonable base allowances[^3][^2][^20]

**Usage-Based:**

- Drives 20-40% expansion revenue when implemented correctly
- Needs excellent usage analytics and forecasting tools[^51][^48]

**Freemium:**

- Converts at only 1-5% but builds massive user bases
- Success requires clear upgrade triggers and low COGS for free users[^26][^24]

**Value-Based:**

- Commands premium pricing but requires deep customer understanding
- Must demonstrate quantifiable 10x+ value[^28][^29]

**Outcome-Based:**

- Perfect incentive alignment but complex to implement
- Requires measurable outcomes and clear attribution[^34][^33][^32]


## Industry-Specific Pricing Considerations

**LLM APIs:** Token-based is industry standard; competitive pricing critical[^4][^5]

**Coding Assistants:** Subscription \$10-40/month with unlimited use winning over usage-based[^52][^53][^15]

**Image Generation:** Tiered subscriptions (\$10-30/month) preferred over per-image[^54][^50][^17]

**Customer Service AI:** Outcome-based (per resolved conversation) gaining traction[^33][^34][^35]

**Analytics Platforms:** Value-based pricing tied to business insights value[^29][^45]

**Developer Tools:** Hybrid models with base + overages align with developer preferences[^20][^46]

**Enterprise AI:** Custom/negotiated pricing typical, 20-40% discounts common[^55][^56]

## Common Pricing Mistakes to Avoid

1. **Underpricing initially** - Much harder to raise prices later than to lower them[^45][^46]
2. **Too many tiers** - 3-4 tiers optimal; more creates confusion[^14][^13][^18]
3. **Opaque pricing** - Lack of transparency destroys customer trust[^57][^48]
4. **No volume discounts** - Essential for winning enterprise deals[^55][^46]
5. **Ignoring unit economics** - Must track COGS per customer religiously[^41][^47][^44]
6. **Copying competitors blindly** - Loses differentiation opportunity[^46][^45]
7. **Never experimenting** - Should test pricing adjustments every 3-6 months[^48][^46]
8. **Complex billing** - Simplicity and clarity trump optimization[^2][^20]

## Future Pricing Trends (2025-2027)

**Predicted Developments:**

1. **Outcome-based pricing** adoption will grow from 10% to 30%[^31][^32]
2. **Hybrid models** will dominate 60-70% of AI companies[^21][^3][^20]
3. **Token prices** will continue declining as model efficiency improves[^42]
4. **Agentic pricing** will standardize around "digital worker" concepts[^38][^32][^31]
5. **Consumption models** will add more predictability features[^51][^48]
6. **Value-based pricing** will become table stakes for premium positioning[^28][^29]

**Technology Enablers:**

- Real-time metering APIs (Stripe, Orb, Metronome)[^20][^46]
- AI cost optimization tools (Mavvrik, CloudZero)[^44][^39]
- Automated billing platforms (Chargebee, Zuora)[^58][^20]
- Usage analytics dashboards and forecasting tools[^49][^48]


## Key Recommendations

### For API Providers:

1. **Start with hybrid pricing** (subscription + usage) for balance of predictability and fairness[^3][^2][^20]
2. **Invest in usage tracking infrastructure early** - Critical for any consumption-based model[^49][^48][^46]
3. **Provide transparent dashboards** showing real-time usage and costs[^57][^48]
4. **Implement graduated pricing tiers** with clear differentiation (3-5x between levels)[^13][^18]
5. **Offer volume discounts** at meaningful thresholds (10K, 100K, 1M+ units)[^46]
6. **Test pricing regularly** (every 3-6 months) based on data, not intuition[^48][^46]
7. **Align pricing with customer value realization**, not just costs[^29][^28]
8. **Consider freemium** only if COGS manageable and PLG strategy viable[^25][^24]

### For Optimal Price Determination:

1. **Calculate true unit economics** including all COGS components[^47][^41]
2. **Target 60-70%+ gross margins** for AI services (vs. 75-90% traditional SaaS)[^40][^41]
3. **Use MAX formula** combining cost-plus, value-based, and competitive approaches[^45][^46]
4. **Start higher** - easier to decrease than increase prices[^45][^46]
5. **Grandfather existing customers** when raising prices to maintain trust[^48][^46]
6. **Monitor competitor pricing** continuously (5-10 companies)[^46][^45]
7. **Quantify customer ROI** to justify value-based pricing premiums[^28][^29]
8. **Build flexible billing systems** that can adapt as pricing evolves[^58][^20]

## Conclusion

AI pricing is fundamentally different from traditional SaaS due to high variable costs and margin compression. **Hybrid pricing models have emerged as the optimal approach** for most AI services, combining subscription predictability with usage-based fairness. The key to success is balancing cost recovery (maintaining 60-70% gross margins) with customer value perception, implementing transparent usage tracking, and iterating based on data rather than assumptions.

As the market matures, we're seeing a shift from pure consumption models toward more sophisticated hybrid and outcome-based approaches that better align vendor and customer incentives. The winners will be those who invest in billing infrastructure, deeply understand customer value drivers, and maintain pricing flexibility as the AI landscape continues to evolve rapidly.
<span style="display:none">[^100][^101][^102][^103][^104][^105][^106][^107][^108][^109][^110][^111][^112][^113][^114][^115][^116][^117][^118][^119][^120][^121][^122][^123][^124][^125][^126][^127][^128][^129][^130][^131][^132][^133][^134][^135][^136][^137][^138][^139][^140][^141][^142][^143][^144][^145][^146][^147][^148][^149][^150][^151][^152][^153][^154][^155][^156][^157][^158][^159][^160][^161][^162][^163][^164][^165][^166][^167][^168][^169][^170][^171][^172][^173][^59][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^70][^71][^72][^73][^74][^75][^76][^77][^78][^79][^80][^81][^82][^83][^84][^85][^86][^87][^88][^89][^90][^91][^92][^93][^94][^95][^96][^97][^98][^99]</span>

<div align="center">⁂</div>

[^1]: https://www.sidetool.co/post/ai-pricing-trends-what-the-market-looks-like-in-2025/

[^2]: https://www.withorb.com/blog/ai-pricing-models

[^3]: https://www.valueships.com/post/ai-pricing-8-biggest-saas-trends-in-2025

[^4]: https://www.iguazio.com/questions/what-is-a-llm-pricing-strategy/

[^5]: https://www.byteplus.com/en/topic/380417

[^6]: https://blogs.novita.ai/comprehensive-guide-to-llm-api-pricing-choose-the-best-for-your-needs/

[^7]: https://bitskingdom.com/blog/ai-pricing-2025-costs-openai-claude-gemini/

[^8]: https://research.aimultiple.com/llm-pricing/

[^9]: https://blog.alguna.com/ai-pricing-models/

[^10]: https://www.reddit.com/r/SaaS/comments/1da25he/help_needed_choosing_the_right_pricing_model_for/

[^11]: https://www.getmonetizely.com/articles/should-your-ai-agent-use-token-based-or-subscription-pricing

[^12]: https://www.revenera.com/blog/software-monetization/saas-pricing-models-guide/

[^13]: https://userpilot.com/blog/saas-pricing-models/

[^14]: https://www.ai-bees.io/post/saas-pricing-models

[^15]: https://www.reddit.com/r/GithubCopilot/comments/1jnboan/github_copilot_vs_cursor_in_2025_why_im_paying/?tl=ms

[^16]: https://github.com/features/copilot/plans

[^17]: https://www.imagineapi.dev/midjourney-pricing-plans

[^18]: https://www.cloudzero.com/blog/saas-pricing/

[^19]: https://www.webapper.com/saas-ai-pricing-models/

[^20]: https://kinde.com/learn/billing/pricing/the-rise-of-hybrid-pricing-how-to-combine-subscription-and-usage-based-models/

[^21]: https://www.pacepricing.com/blog/saas-pricing-evolution-from-subscriptions-to-hybrid-pricing-models

[^22]: https://www.forbes.com/sites/metronome/2025/10/01/hybrid-pricing-in-saas-a-strategic-guide-for-ai-products/

[^23]: https://www.solvimon.com/glossary/hybrid-pricing-models

[^24]: https://www.getmonetizely.com/articles/should-you-adopt-a-freemium-model-for-your-ai-agent-weighing-the-pros-and-cons

[^25]: https://www.maxio.com/blog/freemium-model

[^26]: https://www.fincome.co/blog/freemium-business-model-benefits-drawbacks-best-practices

[^27]: https://userpilot.com/blog/freemium-strategy/

[^28]: https://www.withvayu.com/blog/cost-based-vs-value-based-pricing-why-b2b-companies-shift-to-value-driven-models

[^29]: https://www.zuora.com/glossary/pricing-strategies/

[^30]: https://www.priceagent.com/blog/value-based-pricing-vs-cost-plus-pricing-which-strategy-drives-better-results-

[^31]: https://www.bcg.com/publications/2025/rethinking-b2b-software-pricing-in-the-era-of-ai

[^32]: https://sendbird.com/blog/ai-agent-pricing

[^33]: https://sierra.ai/blog/outcome-based-pricing-for-ai-agents

[^34]: https://sierra.ai/uk/blog/outcome-based-pricing-for-ai-agents

[^35]: https://www.zendesk.co.uk/newsroom/articles/zendesk-outcome-based-pricing/

[^36]: https://www.mavvrik.ai/ai-agent-pricing-models/

[^37]: https://zylo.com/blog/ai-cost/

[^38]: https://research.aimultiple.com/ai-agent-pricing/

[^39]: https://www.getmonetizely.com/articles/the-hidden-cogs-of-ai-why-your-pricing-model-might-be-doomed

[^40]: https://www.getmonetizely.com/blogs/ai-pricing-how-much-does-ai-cost-in-2025

[^41]: https://burklandassociates.com/2025/06/17/financial-kpis-for-ai-startups-to-measure-improve/

[^42]: https://baincapitalventures.com/insight/gross-margin-is-a-bs-metric/

[^43]: https://www.mavvrik.ai/2025-state-of-ai-cost-management-research-finds-85-of-companies-miss-ai-forecasts-by-10/

[^44]: https://www.cloudzero.com/blog/saas-gross-margin-benchmarks/

[^45]: https://www.moesif.com/blog/technical/api-development/SaaS-Pricing-Models/

[^46]: https://zuplo.com/learning-center/api-pricing-strategies

[^47]: https://www.drivetrain.ai/strategic-finance-glossary/saas-gross-margin

[^48]: https://stripe.com/resources/more/usage-based-pricing-101-what-it-is-and-strategies-to-implement-it

[^49]: https://www.hubifi.com/blog/usage-based-pricing-model-guide

[^50]: https://www.eweek.com/artificial-intelligence/midjourney-vs-dalle/

[^51]: https://www.zuora.com/guides/ultimate-guide-to-usage-based-pricing/

[^52]: https://www.reddit.com/r/GithubCopilot/comments/1jnboan/github_copilot_vs_cursor_in_2025_why_im_paying/

[^53]: https://www.builder.io/blog/cursor-vs-github-copilot

[^54]: https://www.lovart.ai/blog/ai-illustration-tools-review

[^55]: https://getdx.com/blog/compare-copilot-cursor-tabnine/

[^56]: https://getdx.com/blog/ai-coding-assistant-pricing/

[^57]: https://www.salesforce.com/blog/usage-based-pricing/

[^58]: https://flexprice.io/blog/best-tools-to-manage-a-hybrid-pricing-model

[^59]: https://ieeexplore.ieee.org/document/11058501/

[^60]: https://linkinghub.elsevier.com/retrieve/pii/S0925527325000908

[^61]: https://arxiv.org/abs/2505.21286

[^62]: https://journalwjaets.com/node/846

[^63]: https://esp.as-pub.com/index.php/esp/article/view/3803

[^64]: https://eajournals.org/ejcsit/vol13-issue-5-2025/the-rise-of-serverless-ai-transforming-machine-learning-deployment/

[^65]: https://jier.org/index.php/journal/article/view/2631

[^66]: https://arxiv.org/abs/2505.18901

[^67]: https://www.academicpublishers.org/journals/index.php/ijdsml/article/view/6217/7267

[^68]: https://chandigarhphilosophers.com/index.php/ijmrp/article/view/273

[^69]: https://arxiv.org/pdf/2311.12485.pdf

[^70]: https://arxiv.org/pdf/2306.04945.pdf

[^71]: http://arxiv.org/pdf/2502.00198.pdf

[^72]: http://arxiv.org/pdf/2310.17843.pdf

[^73]: https://arxiv.org/pdf/2502.07736.pdf

[^74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9364287/

[^75]: http://arxiv.org/pdf/2502.16363.pdf

[^76]: https://arxiv.org/pdf/1805.11450.pdf

[^77]: http://www.scholink.org/ojs/index.php/ibes/article/download/4410/4994

[^78]: https://arxiv.org/pdf/2401.02675.pdf

[^79]: http://arxiv.org/pdf/2402.14844.pdf

[^80]: http://arxiv.org/pdf/2503.21448.pdf

[^81]: http://arxiv.org/pdf/2411.02661.pdf

[^82]: http://arxiv.org/pdf/2404.00311.pdf

[^83]: https://linkinghub.elsevier.com/retrieve/pii/S0148296322005689

[^84]: https://arxiv.org/pdf/2401.10897.pdf

[^85]: https://sparkco.ai/blog/optimize-llm-api-costs-token-strategies-for-2025

[^86]: https://www.maddyness.com/uk/2025/04/14/ai-is-upending-saas-pricing-for-real-this-time/

[^87]: https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/upgrading-software-business-models-to-thrive-in-the-ai-era

[^88]: https://www.reddit.com/r/LLMDevs/comments/1dnb3ob/llm_apis_price_comparison_by_model/

[^89]: https://arxiv.org/abs/2406.17910

[^90]: http://indecs.eu/index.php?s=x\&y=2024\&p=355-359

[^91]: https://ieeexplore.ieee.org/document/10714559/

[^92]: https://www.semanticscholar.org/paper/0a5ca7649ab378cc8c734ddac5bf6c6c00f086c1

[^93]: https://arxiv.org/abs/2403.12671

[^94]: https://ieeexplore.ieee.org/document/10735191/

[^95]: https://dl.acm.org/doi/10.1145/3723178.3723224

[^96]: https://dl.acm.org/doi/10.1145/3545945.3569830

[^97]: https://dl.acm.org/doi/10.1145/3702652.3744219

[^98]: https://ieeexplore.ieee.org/document/11029749/

[^99]: https://arxiv.org/html/2410.07002v1

[^100]: https://arxiv.org/pdf/2403.08299.pdf

[^101]: http://arxiv.org/pdf/2411.09224.pdf

[^102]: http://arxiv.org/pdf/2409.19922.pdf

[^103]: http://arxiv.org/pdf/2503.14724.pdf

[^104]: https://arxiv.org/pdf/2406.17910.pdf

[^105]: https://arxiv.org/pdf/2206.15331.pdf

[^106]: https://arxiv.org/pdf/2403.12671.pdf

[^107]: https://arxiv.org/pdf/2402.08431.pdf

[^108]: https://arxiv.org/pdf/2310.13896.pdf

[^109]: http://arxiv.org/pdf/2210.14306.pdf

[^110]: https://www.mdpi.com/2076-3417/13/24/13061/pdf?version=1701939072

[^111]: https://arxiv.org/html/2412.08063v1

[^112]: https://dl.acm.org/doi/pdf/10.1145/3643916.3644402

[^113]: https://www.reddit.com/r/aiArt/comments/w9pxyp/dalle_vs_midjourney_pricing_comparison/

[^114]: https://www.byteplus.com/en/topic/536644

[^115]: https://www.wingback.com/blog/should-ai-founders-use-the-same-pricing-model-as-openai

[^116]: https://community.latenode.com/t/cursor-vs-github-copilot-2025-same-functionality-but-double-the-cost/20812

[^117]: https://stripe.com/resources/more/token-consumption-101-what-it-is-and-how-businesses-use-it

[^118]: https://stablediffusionapi.com/pricing

[^119]: https://agents24x7.com/blog/ai-services-price-comparison

[^120]: https://freshvanroot.com/blog/ai-image-generators/

[^121]: https://drpress.org/ojs/index.php/HSET/article/view/21600

[^122]: https://ieeexplore.ieee.org/document/10332266/

[^123]: https://ieeexplore.ieee.org/document/10546009/

[^124]: https://econjournals.com/index.php/irmm/article/view/17567

[^125]: https://eipublication.com/index.php/eijmrms/article/view/1787/1688

[^126]: https://afropolitanjournals.com/index.php/ajmbr/article/view/293

[^127]: https://nawalaeducation.com/index.php/MJ/article/view/962

[^128]: https://njaat.com.ng/index.php/njaat/article/view/922

[^129]: https://www.clausiuspress.com/article/10706.html

[^130]: https://journals.lww.com/10.4103/jrpp.jrpp_34_25

[^131]: http://arxiv.org/pdf/1606.09376.pdf

[^132]: http://arxiv.org/pdf/1403.2990.pdf

[^133]: https://journals.sagepub.com/doi/pdf/10.1177/21582440211032168

[^134]: https://arxiv.org/pdf/2305.05176.pdf

[^135]: http://arxiv.org/pdf/2403.14004.pdf

[^136]: http://arxiv.org/pdf/2309.12735.pdf

[^137]: https://pubsonline.informs.org/doi/pdf/10.1287/isre.2019.0882

[^138]: http://arxiv.org/pdf/1506.06648.pdf

[^139]: https://www.mdpi.com/0718-1876/16/4/49/pdf?version=1613812326

[^140]: http://arxiv.org/pdf/2403.14007.pdf

[^141]: https://www.tandfonline.com/doi/pdf/10.1080/09540091.2021.2024146?needAccess=true

[^142]: https://www.younium.com/blog/usage-based-pricing

[^143]: https://www.maxio.com/blog/benefits-of-a-usage-based-pricing-model

[^144]: https://stripe.com/en-gr/resources/more/pricing-strategies-for-new-products?__wpdm_view_count=1052e89f97

[^145]: https://www.convertmate.io/blog/cost-plus-vs-value-based-pricing-ecommerce-showdown

[^146]: https://arxiv.org/abs/2411.12990

[^147]: https://fepbl.com/index.php/csitrj/article/view/1351

[^148]: https://journals.lww.com/10.4103/jehp.jehp_402_23

[^149]: https://ieeexplore.ieee.org/document/11105321/

[^150]: https://arxiv.org/abs/2305.07153

[^151]: https://arxiv.org/abs/2404.07503

[^152]: https://www.ijsat.org/research-paper.php?id=1527

[^153]: https://ieeexplore.ieee.org/document/10698359/

[^154]: https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt.3053

[^155]: https://www.allmultidisciplinaryjournal.com/search?q=F-24-249\&search=search

[^156]: https://arxiv.org/html/2406.16746v4

[^157]: http://arxiv.org/pdf/2405.08597.pdf

[^158]: http://arxiv.org/pdf/2311.12573.pdf

[^159]: http://arxiv.org/pdf/2409.05919.pdf

[^160]: https://arxiv.org/pdf/2501.10383.pdf

[^161]: https://arxiv.org/pdf/2305.02555.pdf

[^162]: https://www.emerald.com/insight/content/doi/10.1108/CEMJ-08-2022-0096/full/pdf?title=platform-based-support-for-ai-uptake-by-smes-guidelines-to-design-service-bundles

[^163]: https://arxiv.org/pdf/2404.17047.pdf

[^164]: https://arxiv.org/pdf/2412.06044.pdf

[^165]: https://www.mdpi.com/2227-7390/9/9/944/pdf?version=1619338570

[^166]: https://arxiv.org/html/2411.03376v1

[^167]: http://arxiv.org/pdf/2406.14114.pdf

[^168]: https://www.arxiv.org/pdf/2402.08938.pdf

[^169]: https://aiboost.co.uk/enhancing-freemium-value-with-ai-driven-content-recommendations/

[^170]: https://www.togai.com/subscription-pricing-vs-pay-as-you-go-vs-hybrid-pricing/

[^171]: https://aiboost.co.uk/ai-for-freemium-service-innovation-staying-ahead-of-the-curve/

[^172]: https://www.zuora.com/glossary/freemium-business-model/

[^173]: https://www.nitrobox.com/wiki/subscriptions/hybrid-pricing-models/

