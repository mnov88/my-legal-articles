
# **An Economic Analysis of Per-Unit Pricing for Digital Services: Theory, Behavior, and Market Structure**

## **I. Introduction: The Economic Logic of Per-Unit Digital Pricing**

### **The Fundamental Problem: Pricing Information Goods**

The pricing of digital services represents a fundamental challenge to traditional microeconomic theory. The cost structure of "information goods"—a category that includes software, digital media, network bandwidth, and Application Programming Interfaces (APIs)—is characterized by an unusual and paradoxical combination: extremely high fixed costs of production and near-zero marginal variable costs of reproduction.1  
For example, developing a large-scale cloud infrastructure or training a foundational large language model (LLM) can require billions of dollars in research, development, and capital expenditure. This represents the "first unit" cost.1 Once that "first unit" (the software, the trained model) exists, the cost of replicating and delivering it to an additional user is "virtually nothing".2 This cost structure defies classic marginal-cost pricing. If competition were to drive prices down to the marginal cost of production (near-zero), firms would never be able to recover their immense fixed costs, obviating the incentive for innovation. This creates an "extremely challenging" pricing task for firms, necessitating creative strategies to recover high fixed costs without triggering destructive price wars.2

### **Usage-Based Pricing as a Resource Allocation Mechanism**

Per-unit pricing—often termed usage-based, metered, or pay-as-you-go—emerges as a primary strategic solution to this paradox. Beyond simple cost recovery, it functions as a powerful mechanism for managing scarce, *congestible resources*. Online services, from broadband networks 3 to cloud computing platforms 4 and the GPU clusters that power AI, are not infinite. They are prone to congestion and overload, where consumption by one user can degrade the service quality for others.  
In a flat-rate system, users have no incentive to moderate their consumption, leading to a "tragedy of the commons" dynamic. Usage-based pricing directly addresses this by forcing users to internalize the cost of their consumption. Economic models demonstrate that in "overload" regimes, usage-based pricing leads to a *reduction in aggregate overloads* and simultaneously results in *higher individual user utilities* compared to a flat-rate model.5 This positions per-unit pricing not merely as a billing method, but as an active and efficient resource management strategy.

### **The "Pay-for-Value" Proposition and Case Study Introduction**

Providers have framed this model as a transparent and equitable "pay-for-value" proposition. The narrative is that it "aligns pricing with value delivered" 6, "lowers the barrier to entry" for new users 6, and offers superior "transparency".8  
This report will conduct a granular analysis of these claims by focusing on two archetypal case studies of modern per-unit pricing:

1. **Case 1: Serverless Computing (Function-as-a-Service, or FaaS):** This model abstracts away servers, charging for compute in fine-grained units of the "GB-second"—a composite metric of memory allocated and code execution time.10 This model is designed to eliminate the cost of idle servers, a significant source of waste.12  
2. **Case 2: Large Language Model (LLM) APIs:** This model charges per "token," a unit of text (roughly 4 characters), and often prices input tokens (the prompt) differently from output tokens (the model's response).13

While per-unit pricing appears to be a transparent, efficient, and fair mechanism, its implementation in these complex digital ecosystems creates significant, non-obvious information asymmetries, perverse behavioral incentives, and market-consolidating dynamics that challenge the simple "pay-for-value" narrative.

## **II. Information Asymmetry and Decision-Making Quality**

This section addresses how pricing model transparency affects users' ability to make optimal consumption decisions and the welfare implications of information gaps between providers and consumers.

### **The Illusion of Transparency: Simple Units vs. Complex Digital Metrics**

The primary benefit of unit pricing in traditional retail is its role as a "shopping superpower," allowing consumers to easily compare products of different sizes—such as price per ounce for groceries—and make optimal value-based decisions.15 This transparency, however, is largely illusory when applied to complex digital services.  
A "price per ounce" is static, tangible, and easily comparable. In contrast, a "price per GB-second" 10 or "price per token" 13 is dynamic and cognitively opaque. A consumer (in this case, a developer or business) cannot easily or accurately estimate *ex ante* how many "tokens" a complex query will require, or how many "GB-seconds" a function will consume under variable data loads. This creates a fundamental disconnect: the *price* for the unit is transparent, but the *quantity* of units a given action will consume is unknowable. This opacity undermines the model's core claim of empowering informed decision-making.

### **Bounded Rationality and the Inevitability of "Bill Shock"**

The cognitive opacity of digital units means that "bill shock" is not an edge case but a structural feature of the per-unit pricing model. Developers, operating under conditions of bounded rationality, are systemically unable to predict the cost implications of their actions in a complex, automated environment.  
This is extensively documented in developer complaints:

* **FaaS/Cloud:** The canonical "bill shock" event is the "Lambda/S3 loop," where a simple code misconfiguration creates an infinite recursive trigger. One event (e.g., a file write to S3) triggers a Lambda function, which in turn writes a file to S3, triggering itself again. This simple error can create an exponential cost cascade in minutes, resulting in catastrophic, unforeseen bills ranging from $3,200 to $12,000 or more.16  
* **LLMs:** Developers express similar surprise and frustration upon discovering that the cost of a chat application grows linearly with the length of the conversation, as the entire chat history (context) must be re-submitted and re-processed with every new turn.19

These events are a direct consequence of an information gap. The problem is exacerbated by the provider's *choice* not to implement hard spending caps by default, a failure that users describe as a "trap" and "scam," especially for hobbyists and students who face significant financial risk.18 The fact that providers *could* offer real-time billing and hard caps but often choose not to suggests this information asymmetry may be strategically maintained.

### **Deconstructing Opacity: "Hidden" and "Unknown" Costs**

The information gap extends beyond cognitive load; it is structurally embedded in the pricing model through "hidden" and "unknown" costs that are not captured by the advertised per-unit metric.  
In the **Serverless (FaaS) case**, the "price per GB-second" masks a host of other cost drivers:

* **Cold Starts:** The latency spike that occurs when a new "container" must be initialized to serve a request.22 This is a "hidden" performance cost, not a direct monetary one. However, it *induces* a monetary cost, as developers are forced to *over-provision memory* (which increases the "GB" half of the "GB-second" metric) to reduce this latency, thereby overpaying for compute they do not need.24  
* **Data Egress:** Developers are frequently surprised by high data transfer costs, which are billed separately and can, in some architectures, outpace the cost of compute itself.26  
* **Associated Services:** The FaaS function is merely "glue".27 The true cost is often hidden in the services the function calls, such as databases (which have their own metered billing), storage, and NAT gateways.26

In the **LLM case**, the "price per token" is similarly misleading:

* **Context Window Inflation:** As noted, the cost of a single marginal query is not fixed; it dynamically increases as the conversation history grows.19  
* **Tokenization Discrepancies:** The process of "tokenization" (how the provider counts tokens) is an opaque black box. Developers report "inflationary" token counts, particularly with real-time audio streaming, where silence or background noise can be tokenized and billed.30  
* **Asymmetric Pricing:** The distinction between input and output token pricing 13 further complicates any *ex ante* cost calculation, as the user cannot know the *length* of the model's response in advance.

### **Dynamic Choice Models and Suboptimal Welfare Outcomes**

This analysis is supported by dynamic models of consumer choice. Research on usage-based broadband plans found that consumers are *not* myopic; they behave rationally and dynamically, altering their consumption in response to the "shadow price" of data as they approach their monthly cap.32 In fact, static models that ignore this behavior *underestimate* consumer price sensitivity by as much as 38.6%.32  
This finding is critical: users *are* trying to be rational, dynamic optimizers, but in the FaaS/LLM cases, they are optimizing with intractably poor information. A broadband user has one simple "cap" to monitor. A developer's "cap" is a complex, multi-dimensional, and unknowable vector (CPU, memory, input tokens, output tokens, egress, storage) that changes with every line of code. The "shadow price" is effectively un-calculable.  
This information asymmetry leads to systemic suboptimal welfare outcomes:

1. **Over-consumption:** Accidental and catastrophic, as seen in the S3 loops.18 This represents a pure, unplanned transfer of consumer surplus to the provider.  
2. **Under-consumption:** Users, particularly those fearing "bill shock" 21, may self-censor, avoiding beneficial experimentation or usage, thus stifling the very innovation the model claims to promote.  
3. **Deadweight Loss:** Users are forced to invest their own time and engineering resources to mitigate the provider's opaque pricing. This includes building custom cost-monitoring dashboards or "routers" to direct queries to cheaper models.33 This effort is a deadweight loss, as it creates no new value but merely mitigates a risk imposed by the pricing model.

### **Table 1: Comparative Analysis of Information Gaps in Per-Unit Models**

| Metric | Case Study 1: FaaS (Serverless) | Case Study 2: LLM APIs |
| :---- | :---- | :---- |
| **Advertised Per-Unit Metric** | GB-second (Composite of Memory x Time) 10 | Per-Token (Split by Input/Output) 13 |
| **Primary "Hidden Cost"** | Cold Start latency 22, Data Egress fees 26, Associated service costs (e.g., NAT Gateway, DB calls) 29 | Context Window inflation 19, Opaque/inflationary tokenization 30 |
| **Source of Cognitive Opacity** | User cannot predict function *duration* or *memory* required for variable loads. | User cannot predict *token count* of input or *length/cost* of output *ex ante*. |
| **Catastrophic User Error** | Recursive "event loops" (e.g., S3-Lambda) leading to exponential cost.16 | Submitting long conversations/documents repeatedly, unaware of context cost.20 |
| **Typical Behavioral Response** | "Architecting around" cold starts 25; Over-provisioning memory.24 | "Prompt Engineering" for cost 34; Building model-routing logic.33 |

## **III. Value-Cost Alignment and Perceived Fairness**

This section assesses the extent to which the per-unit structure aligns the value delivered to users with the costs they incur, and the resulting impact on perceived fairness.

### **The Core Claim: "Pay for What You Use" as "Pay for What You Value"**

The model's central marketing claim is that it perfectly aligns cost with value. Providers argue it is a "fairer and more transparent" model 8 that offers a "clear value for cost" 7 and "directly correlates with customer needs and usage".35 This section critically evaluates this claim by deconstructing the "unit" being sold.

### **The Value-Cost Disconnect: Metering Provider Cost vs. Consumer Value**

A granular analysis reveals that the "unit of consumption" (the token, the GB-second) is fundamentally a *provider-centric metric*, not a consumer-centric one. It is a proxy for the provider's *cost of goods sold (COGS)*—specifically, the cost of GPU or CPU cycles—not a measure of the *value* the consumer receives (the outcome).  
This misalignment is the source of the model's core tension. For example, a developer's confusion about being charged for *input* tokens 20 stems from this disconnect. The developer's *perceived value* is in the *output* (the "completion"). The provider, however, incurs compute cost for processing *both* the input and output. The per-token model 13 meters the provider's cost, not the user's value.  
This disconnect manifests clearly in both case studies:

* **FaaS Case:** The "memory-CPU coupling" in many serverless offerings 24 is a prime example. A developer with a memory-hungry but compute-light task is forced to pay for a high-performance vCPU they do not need, simply because the pricing unit bundles them. The cost is high, but it is not aligned with the specific value the user requires.  
* **LLM Case:** The misalignment is starker. A model that is more "helpful" by providing a more detailed and verbose (i.e., higher token count) response is *penalized* with a higher cost, even if a user might assign equal or greater value to a brief, concise answer.36 Furthermore, as the conversation context grows, the *cost* of asking the *same* marginal query increases over time.19 The value of the query is static, but its cost is dynamic and rising. This is exacerbated by the provider's incentive to (mis)report longer tokenizations 37, which would sever the link between price and value.

### **Cross-Subsidization and Market Segmentation**

The per-unit model is often praised for *eliminating* the cross-subsidization inherent in flat-rate plans, where casual users inevitably subsidize power users. In a usage-based system, each user "pays their own way".38  
However, this analysis obscures a different, more significant form of subsidization: a *temporal* and *market-level* subsidy. Developer forums and market analyses allege that current low per-token prices are not sustainable, but rather a "subsidized... wonnabe monopolistic play".39 In this view, the profits from incumbent firms' core businesses (e.g., Google's advertising, Microsoft's enterprise software) are cross-subsidizing below-cost AI token prices. This is not a subsidy *between* users, but a subsidy from the corporation's present-day profits to *all* users, with the goal of capturing future market share.  
This dynamic creates a "Prisoner's Dilemma" for the entire market.36 A sustainable, cost-plus usage-based model is the rational *collective* choice for industry health. But the dominant *individual* strategy for any single, VC-funded competitor is to defect, offering a flat-rate "unlimited" plan to rapidly acquire users. This leads to a "race to the bottom" that threatens the viability of the very model itself.36

### **Perceived Fairness and Distributive Justice**

The fairness of the model is paradoxical. It is perceived as highly fair at the point of *entry* 61 but can be perceived as deeply *unfair* at the point of *billing*.21  
This suggests "fairness" has two components:

1. **Distributive Fairness:** Is the *price* for the unit fair? Initially, users believe so.  
2. **Procedural Fairness:** Is the *process* of arriving at the total bill fair? The lack of predictability, opaque units, and hidden costs makes the process feel unjust.

One mechanism for achieving *both* forms of fairness is "Paris Metro Pricing" (PMP). PMP is an economic model for managing congestion by partitioning a resource (like a network, or the Paris Metro) into different service classes with different price points.3 This allows users to *self-select* into a tier that matches their willingness-to-pay and their sensitivity to "congestion" (or in this case, model quality).3  
Modern LLM pricing is a clear implementation of PMP. A provider offering a spectrum of models—such as Anthropic's "Haiku," "Sonnet," and "Opus," or OpenAI's "mini," "pro," and "ultra" tiers—is creating different "metro cars".13 This is a rational and arguably fair strategy. It allows the provider to capture the high surplus from enterprise users (who will pay for the premium "Opus" car) while still serving the mass market with the "Haiku" car, aligning price with *perceived value* and willingness-to-pay.

## **IV. Dynamic Behavioral Effects and Usage Patterns**

This section analyzes how per-unit pricing structures influence user behavior, experimentation, lock-in, and the development of complementary ecosystems.

### **Positive Behavioral Effect: Lowering Barriers to Experimentation**

The most significant and positive behavioral impact of the per-unit model is the "freedom to experiment" it affords developers.43 By eliminating "upfront commitment" 45 and high fixed costs, the pay-as-you-go model dramatically "lowers the barrier to entry".6  
This is a primary driver of adoption. A developer can start using a powerful API, like those from Google 43, Twilio 46, or OpenAI 46, with minimal friction. They can test new use cases 43, try new features 48, and onboard their first customers without a large capital outlay.35 This "try-before-you-commit" dynamic, which has been shown to increase market participation 49, is essential to the rapid growth of the entire API and serverless ecosystem.

### **Second-Order Effect: The Externalization of Cost Optimization**

While experimentation is the *intended* effect, the model produces a critical, *unintended* second-order effect: it externalizes the provider's cost-optimization burden onto the consumer.  
The provider's COGS is the GPU/CPU-second. The "token" 13 or "GB-second" 10 is the billing *proxy* for that COGS. By charging the user per-unit, the provider directly exposes its COGS-proxy to the user. This forces the user (the developer) to share the provider's optimization burden. The developer must now expend their *own* time and cognitive resources—a new, un-metered cost—on behaviors designed explicitly to minimize the provider's metered unit.  
This "work" is not optional; it is a required discipline for any user who wishes to avoid "bill shock." It manifests in specific, observable behaviors:

* LLM Case: "Prompt Engineering as Cost Engineering".34 The entire discipline of prompt engineering, ostensibly about improving *quality*, becomes a *cost-control* discipline in practice.  
  * Developers build complex "routers" to "automatically route prompts to cheaper models" based on perceived task difficulty.33  
  * They explicitly instruct models to be "concise".33  
  * They implement hard "token budget constraints" and "response length limits".34  
  * They must "choose cost-effective models for simpler tasks" 50, creating a new layer of application logic.  
* **FaaS Case: "Architecting Around the Meter."**  
  * Developers must actively mitigate "cold starts" 25—a problem that only exists because of the provider's specific implementation of the FaaS model.  
  * They must optimize application architecture to avoid S3/Lambda loops.18  
  * They must analyze utilization patterns to choose between FaaS (cheaper for low, spiky utilization) and containers (cheaper for high, steady utilization).24

This externalization of cost optimization represents a significant, hidden deadweight loss to the economy, as developer time is diverted from creating new value to simply managing the billing meter.

### **Lock-In Effects and Switching Costs**

The pay-as-you-go model appears to be the epitome of flexibility, with "no lock-ins".44 However, this contractual flexibility masks a deep and subtle *ecosystem lock-in*.  
A developer rarely uses a single metered service in isolation. As noted, FaaS functions are "glue" 27 that connect an entire ecosystem of other metered services: serverless databases (like DynamoDB), storage (like S3), messaging queues, and more.29 A developer who builds an application on AWS is not just using Lambda 10; they are building on top of a deeply integrated, proprietary stack.  
To switch to a competitor (e.g., Google Cloud Functions 53), the developer cannot simply port their function. They must re-architect their entire data, storage, and eventing logic. The "open technology" promise 54 is often an illusion. The lock-in comes not from the *compute* service, but from the proprietary, metered *integrations* between services, which create powerful switching costs.

### **Table 2: Second-Order Behavioral Incentives of Per-Unit Pricing**

| Pricing Feature / Mechanism | Induced User Behavior (Cost-Mitigation "Work") |
| :---- | :---- |
| **Pay-per-Token (Input)** | Prompt shortening; Context truncation; Developing "context caching" strategies.50 |
| **Pay-per-Token (Output)** | Requesting "concise" answers or JSON formats 33; Implementing "response length limits".34 |
| **Tiered Models (PMP)** | Building "model routers" to send simple queries to cheap models (e.g., "Haiku") and complex queries to expensive ones (e.g., "Opus").33 |
| **FaaS "GB-second"** | Code optimization to reduce *execution time*; Choosing lower-memory functions to reduce *memory* cost. |
| **FaaS "Cold Start"** | Implementing "warming" services to ping functions and keep them active; Over-provisioning memory (a *cost-increasing* behavior) to reduce latency.24 |
| **Data Egress Fees** | Architecting applications to keep all services within a single cloud region/zone to avoid cross-zone data transfer charges.26 |

## **V. Market Structure and Competitive Dynamics**

This section analyzes the impact of per-unit pricing on market concentration, barriers to entry, and the distribution of value among stakeholders.

### **The Incumbent's Advantage: High Fixed Costs and Natural Oligopoly**

The analysis of market structure must begin with the cost structure of information goods.1 The markets for foundational LLMs and global cloud infrastructure are *not* perfectly competitive. They are defined by *astronomical* fixed costs. Training a "frontier" model and building the global data center network to serve it requires capital, specialized hardware, and data at a scale accessible to only a handful of firms.  
This structure inherently leads to a natural monopoly or, more accurately, a tight *oligopoly*.55 Per-unit pricing is the competitive *tool* these oligopolists use to acquire users and capture surplus within this market structure.

### **Pricing as a Barrier to Entry and Consolidation Tool**

The observed "price war" in LLM tokens—with prices reportedly falling by "40x per year" 56—is not, as it might appear, evidence of a healthy, hyper-competitive market. It is a *consolidation play*.  
This dynamic is rooted in cross-subsidization. Large, vertically integrated incumbents like Google (with revenues from Search and Ads) or Microsoft (with revenues from Azure and Office) can sustain negative or near-zero margins on their per-token inference costs.39 Their goal is not immediate profit from tokens, but long-term *market saturation* and *ecosystem lock-in* (see Section IV). They can afford to lose money on every token to ensure that developers build the next generation of applications on *their* platform.  
A pure-play AI startup, with no massive, separate profit center, *cannot* compete in this price war. Therefore, the per-unit price, when set at a "subsidized" 39 and artificially low level, becomes a powerful *barrier to entry*. It functions as a form of predatory pricing.55 Antitrust doctrine holds that predatory pricing is plausible only when the firm can later "reap a monopoly profit".58 Given the high barriers to entry (capital, data), this condition is met. The per-token model is the mechanism by which incumbents can eliminate competition and consolidate the market.  
This bifurcates the market:

1. **Foundational Model Market:** An oligopoly of incumbents (OpenAI/Microsoft, Google, Anthropic, xAI) competing via subsidized per-token prices.31  
2. **Hosting Market:** A highly competitive, commoditized market of "low-cost cloud providers" hosting open-source models.59 This competition is illusory, however, as it simply commoditizes the "complement" (the model) while strengthening the "platform" (the incumbent's underlying cloud infrastructure, e.g., AWS, on which the hosting provider runs).59

### **Distribution of Value: Platforms vs. Complementors**

In this ecosystem, the per-unit model ensures that value flows from the edges to the center.60

* **Provider (Platform):** The provider "controls the meter" and captures value from *every* action taken in the ecosystem. They are insulated from risk; they get paid whether the complementor's business succeeds or fails.  
* **Complementor (Developer/Business):** The complementor bears *all* the risk. They build an application, and if it becomes successful, their costs scale linearly with usage.61 Their profit margin is permanently squeezed between what they can charge their end-users (a market-based price) and the metered bill they must pay the platform (a provider-set price). They are entirely dependent on the platform's pricing, which can be changed at any time.62  
* **End-Users:** In the short term, users benefit from subsidized low prices 56 and a Cambrian explosion of innovative apps. In the long term, they face a consolidated market with fewer choices and the risk of price hikes once competition has been disciplined.39

## **VI. Long-term Sustainability and Systemic Risks**

This final section evaluates the long-term implications of the per-unit model for provider viability, resource efficiency, and systemic risks such as access inequality.

### **Positive: Resource Allocation and Infrastructure Efficiency**

From a pure systems-thinking and operational perspective, per-unit pricing is a massive leap forward in efficiency. Its primary long-term benefit is the rational allocation of scarce resources.

* **Provider Viability:** The model ensures that providers can manage "overload" 5 and "congestion-prone" networks.3 This gives them the confidence to make the massive capital investments in infrastructure, knowing they have a mechanism to monetize it efficiently.  
* **Resource Efficiency:** At a systemic level, the model's greatest virtue is that it "eliminates idle and underutilized servers" 12, which are a major source of wasted capital and energy. The provider's core economic incentive is to maximize their *internal utilization* ($c$) 63, which aligns their private interest with the public good of computational efficiency.

### **Provider Viability and the "Price per Answer" Paradox**

The sustainability of the model, however, is threatened by the "race to the bottom" 36 described in Section V. If per-token prices are truly "subsidized" and falling "40x per year" 56, how can the model be viable?  
The solution to this paradox is a crucial, hidden trend: **the "price per token" is falling, but the "price per answer" is rising.**  
Market analysis indicates that while the *unit price* of a token is decreasing, the *complexity of tasks* is increasing.64 A "meaningful answer" no longer involves a single model call. Modern applications use complex chains, agents, and Retrieval-Augmented Generation (RAG) systems that may involve dozens of model calls to produce a single outcome. As one analyst notes, "Token usage per task is skyrocketing".36  
This means provider viability is likely secure. They can publicly advertise "cheaper" models and falling *unit prices* 56—a public relations victory—while privately enjoying *exploding volume* of units sold. The growing complexity of the ecosystem ensures that total revenue per user will continue to rise, even as the price per token falls.

### **Systemic Risk: Volatility and Capacity Constraints**

The "bill shock" 16 experienced by individuals scales up to a systemic risk for providers. The model's "frictionless" nature, which drives adoption, also invites extreme demand volatility. A single application going viral could create a demand spike that overwhelms the provider's capacity, leading to cascading failures or brownouts. The provider's primary defense against this is the price itself: as demand spikes, the "shadow price" 32 of scarce capacity rises, which (in a functioning market) should dampen demand.

### **Systemic Risk: Inequality of Access and the "Frontier Divide"**

The most significant long-term societal risk of the per-token model is the creation of a new, persistent form of inequality: the **"Frontier Divide."**  
Market behavior shows that "Demand follows the frontier, not the cheap".36 Users and businesses consistently flock to the *best, most powerful* models (e.g., "GPT-5 pro," "Opus 4.1" 31), even when "26x cheaper alternatives" exist.36  
These "frontier" models remain—and will likely always remain—prohibitively expensive for a large class of users. The per-token model thus bifurcates the market:

1. **The "Commodity" Tier:** "Good-enough" open-source models 59 become cheap or free, handling simple, commoditized tasks.  
2. **The "Frontier" Tier:** The best, most powerful models that drive true innovation and competitive advantage remain locked behind a high per-token paywall.13

This creates a new digital divide. Large enterprises can afford to use frontier models at scale, giving them a compounding advantage in research, productivity, and innovation. Meanwhile, public-good actors—academics, non-profits, students 21, and public-sector researchers—are priced out. The per-token pricing model, therefore, ceases to be a simple billing mechanism. It becomes a potent *instrument of industrial policy*, allocating the most powerful technology to those with the greatest ability to pay, entrenching corporate advantage and widening the gap between the technological haves and have-nots.

## **VII. Executive Summary: Evaluation Matrix**

The following matrix synthesizes the micro-level (individual decision-making) and macro-level (market structure) implications of the per-token pricing model across immediate, medium-term, and long-term horizons.

### **Table 3: Micro- and Macro-Level Evaluation of Per-Token Pricing**

| Time Horizon | Stakeholder | Micro-Level Implications (Individual Decision-Making & UX) | Macro-Level Implications (Market Structure & Society) |
| :---- | :---- | :---- | :---- |
| **Immediate Effects** | **Consumers (Developers / Users)** | **(+)** Lowers barrier to entry, fostering experimentation and adoption.43 **(-)** High cognitive load; "illusory transparency" leads to suboptimal consumption and "bill shock".18 | **(+)** Rapid market penetration and service discovery. **(-)** High "anxiety" and risk aversion for non-corporate users (e.g., students, hobbyists).21 |
|  | **Businesses (Providers / Complementors)** | **(+)** Captures revenue from all usage levels; "pay-for-value" narrative.6 **(-)** Difficult revenue prediction; risk of "noisy neighbors" 65 and customer churn from "bill shock".65 | **(+)** Efficiently manages congestible resources 5 and eliminates cost of idle servers.12 **(+)** Enables effective price-based market segmentation (Paris Metro Pricing).3 |
|  | **Society / Policy** | **(+)** "Freedom to experiment" may democratize access to powerful tools *initially*.66 | **(+)** Drives highly efficient allocation of scarce computational resources (e.g., GPUs, energy). |
| **Medium-Term Effects** | **Consumers (Developers / Users)** | **(-) Perverse Incentives:** Forces users to perform "cost-engineering work" (e.g., prompt engineering 34) and "architect around the meter" 25, a deadweight loss of developer time and resources. | **(-) Ecosystem Lock-In:** While contractually flexible, the model creates deep switching costs via integration with proprietary platform services (e.g., AWS Lambda+S3+DynamoDB).27 |
|  | **Businesses (Providers / Complementors)** | **(+) Provider:** Aligns user financial incentives with provider COGS. **(-) Complementor:** Margins are squeezed between end-user price and the platform's metered bill. Business model is high-risk. | **(-) Competitive Dynamics:** Can be used as a predatory pricing tool in a "race to the bottom" 36, driving price wars 56 and destabilizing the market for pure-play competitors. |
|  | **Society / Policy** | **(+)** A new "discipline" of computational efficiency emerges.34 **(-)** User "work" (e.g., prompt optimization) is a hidden, unmeasured drag on innovation. | **(-) Market Destabilization:** The "Prisoner's Dilemma" 36 between usage-based and flat-rate models creates market volatility. |
| **Long-Term Effects** | **Consumers (Developers / Users)** | **(-)** Risk of being locked into a consolidated market with few providers, leading to future price hikes or reduced innovation. | **(-) Consolidated Market:** End-users face higher prices and less choice as "subsidized" 39 price wars eliminate competitors. |
|  | **Businesses (Providers / Complementors)** | **(+) Provider:** Successful "consolidation play" leads to durable oligopoly with high market power and ability to raise prices. **(-) Complementor:** Total dependence on the platform's pricing strategy. | **(-) Market Concentration:** High-fixed-cost nature 1 combined with predatory pricing 57 leads to a natural oligopoly. |
|  | **Society / Policy** | **(-) "Frontier Divide":** A new form of digital divide emerges. The most powerful AI models remain prohibitively expensive for public-good actors (academia, non-profits), entrenching corporate advantage.36 | **(-) Systemic Risk:** Market consolidation reduces innovation. Access inequality for frontier models 21 becomes a structural barrier to social and scientific progress. |

#### **Works cited**

1. Pricing Information Goods, Price Discrimination, Pricing Digital ..., accessed November 6, 2025, [https://oz.stern.nyu.edu/io/pricing.html](https://oz.stern.nyu.edu/io/pricing.html)  
2. Understanding unit economics & why it matters | Definitions & formulae \- Mercury, accessed November 6, 2025, [https://mercury.com/blog/understanding-unit-economics](https://mercury.com/blog/understanding-unit-economics)  
3. Usage-Based Pricing and Competition in Congestible Network ..., accessed November 6, 2025, [https://www.researchgate.net/publication/285629945\_Usage-Based\_Pricing\_and\_Competition\_in\_Congestible\_Network\_Service\_Markets](https://www.researchgate.net/publication/285629945_Usage-Based_Pricing_and_Competition_in_Congestible_Network_Service_Markets)  
4. Cloud Computing Costs in 2024 \- Oracle, accessed November 6, 2025, [https://www.oracle.com/cloud/cloud-computing-cost/](https://www.oracle.com/cloud/cloud-computing-cost/)  
5. On Flat-Rate And Usage-Based Pricing for Tiered Commodity ..., accessed November 6, 2025, [https://www.princeton.edu/optnet/CISS/kesidis.pdf](https://www.princeton.edu/optnet/CISS/kesidis.pdf)  
6. Usage-Based Pricing Model: Definition, Benefits, and Implementation \- Maxio, accessed November 6, 2025, [https://www.maxio.com/blog/benefits-of-a-usage-based-pricing-model](https://www.maxio.com/blog/benefits-of-a-usage-based-pricing-model)  
7. Pay-as-you-go pricing model: What businesses should know \- Stripe, accessed November 6, 2025, [https://stripe.com/resources/more/pay-as-you-go-pricing-model-what-businesses-should-know](https://stripe.com/resources/more/pay-as-you-go-pricing-model-what-businesses-should-know)  
8. The Power of Usage-Based Pricing in SaaS \- Gilion, accessed November 6, 2025, [https://www.gilion.com/basics/usage-based-pricing](https://www.gilion.com/basics/usage-based-pricing)  
9. How to Implement Scalable Usage-Based Billing for AI Workloads \- CloudRaft, accessed November 6, 2025, [https://www.cloudraft.io/blog/usage-based-billing-for-ai-workloads](https://www.cloudraft.io/blog/usage-based-billing-for-ai-workloads)  
10. AWS Lambda Pricing, accessed November 6, 2025, [https://aws.amazon.com/lambda/pricing/](https://aws.amazon.com/lambda/pricing/)  
11. Azure Functions pricing, accessed November 6, 2025, [https://azure.microsoft.com/en-us/pricing/details/functions/](https://azure.microsoft.com/en-us/pricing/details/functions/)  
12. Optimizing Enterprise Economics with Serverless Architectures ..., accessed November 6, 2025, [https://docs.aws.amazon.com/pdfs/whitepapers/latest/optimizing-enterprise-economics-with-serverless/optimizing-enterprise-economics-with-serverless.pdf](https://docs.aws.amazon.com/pdfs/whitepapers/latest/optimizing-enterprise-economics-with-serverless/optimizing-enterprise-economics-with-serverless.pdf)  
13. LLM Pricing: Top 15+ Providers Compared \- Research AIMultiple, accessed November 6, 2025, [https://research.aimultiple.com/llm-pricing/](https://research.aimultiple.com/llm-pricing/)  
14. Compare LLM API Prices For Over 300 Models, accessed November 6, 2025, [https://pricepertoken.com/](https://pricepertoken.com/)  
15. The Role of Unit Pricing in Consumer Decision-Making \- B.Com Institute, accessed November 6, 2025, [https://bcom.institute/principles-of-marketing/unit-pricing-consumer-decision-making/](https://bcom.institute/principles-of-marketing/unit-pricing-consumer-decision-making/)  
16. I got slammed with a $3200 AWS bill because of a misconfigured Lambda, how are you all catching these before they hit? \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/devops/comments/1ltdt4q/i\_got\_slammed\_with\_a\_3200\_aws\_bill\_because\_of\_a/](https://www.reddit.com/r/devops/comments/1ltdt4q/i_got_slammed_with_a_3200_aws_bill_because_of_a/)  
17. I got hit with a $3200 AWS bill from a misconfigured Lambda. I just wish something had told me earlier. \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/aws/comments/1ltdshc/i\_got\_hit\_with\_a\_3200\_aws\_bill\_from\_a/](https://www.reddit.com/r/aws/comments/1ltdshc/i_got_hit_with_a_3200_aws_bill_from_a/)  
18. How Realistic is the Risk of an Astronomical AWS Bill for Hobby Developers? \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/aws/comments/1daq04x/how\_realistic\_is\_the\_risk\_of\_an\_astronomical\_aws/](https://www.reddit.com/r/aws/comments/1daq04x/how_realistic_is_the_risk_of_an_astronomical_aws/)  
19. Building Cost-Aware AI Systems: Strategies for Managing LLM Expenses, accessed November 6, 2025, [https://www.cloudgeometry.com/blog/building-cost-aware-ai-systems-a-guide-for-both-technical-and-non-technical-decisions](https://www.cloudgeometry.com/blog/building-cost-aware-ai-systems-a-guide-for-both-technical-and-non-technical-decisions)  
20. The Great Deception of "Low Prices" in LLM APIs : r/LocalLLaMA \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/LocalLLaMA/comments/1meep6o/the\_great\_deception\_of\_low\_prices\_in\_llm\_apis/](https://www.reddit.com/r/LocalLLaMA/comments/1meep6o/the_great_deception_of_low_prices_in_llm_apis/)  
21. Warning: $14k BigQuery charge in 2 hours \- Hacker News, accessed November 6, 2025, [https://news.ycombinator.com/item?id=39446789](https://news.ycombinator.com/item?id=39446789)  
22. Understanding and Remediating Cold Starts: An AWS Lambda Perspective, accessed November 6, 2025, [https://aws.amazon.com/blogs/compute/understanding-and-remediating-cold-starts-an-aws-lambda-perspective/](https://aws.amazon.com/blogs/compute/understanding-and-remediating-cold-starts-an-aws-lambda-perspective/)  
23. Understand serverless function performance with Cold Start Tracing \- Datadog, accessed November 6, 2025, [https://www.datadoghq.com/blog/serverless-cold-start-traces/](https://www.datadoghq.com/blog/serverless-cold-start-traces/)  
24. Serverless vs Containers: Which Is More Cost‑Effective? \- Binadox, accessed November 6, 2025, [https://www.binadox.com/blog/serverless-vs-containers-which-is-more-cost%E2%80%91effective-in-the-cloud/](https://www.binadox.com/blog/serverless-vs-containers-which-is-more-cost%E2%80%91effective-in-the-cloud/)  
25. Let's Stop Talking About Serverless Cold Starts | Ready, Set, Cloud\!, accessed November 6, 2025, [https://www.readysetcloud.io/blog/allen.helton/lets-stop-talking-about-serverless-cold-starts/](https://www.readysetcloud.io/blog/allen.helton/lets-stop-talking-about-serverless-cold-starts/)  
26. Senior Developers I know are always hating on serverless \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/serverless/comments/1b8zc51/senior\_developers\_i\_know\_are\_always\_hating\_on/](https://www.reddit.com/r/serverless/comments/1b8zc51/senior_developers_i_know_are_always_hating_on/)  
27. Is Serverless expensive at scale? Only if you are using it wrong \- DEV Community, accessed November 6, 2025, [https://dev.to/aws-heroes/is-serverless-expensive-at-scale-only-if-you-are-using-it-wrong-19pa](https://dev.to/aws-heroes/is-serverless-expensive-at-scale-only-if-you-are-using-it-wrong-19pa)  
28. Exploring the Economics of Serverless: An Analysis of ... \- DiVA portal, accessed November 6, 2025, [http://www.diva-portal.org/smash/get/diva2:1943579/FULLTEXT01.pdf](http://www.diva-portal.org/smash/get/diva2:1943579/FULLTEXT01.pdf)  
29. Analysis of cost-efficiency of serverless approaches \- arXiv, accessed November 6, 2025, [https://arxiv.org/html/2506.05836v1](https://arxiv.org/html/2506.05836v1)  
30. Realtime API Pricing: VAD and Token Accumulation \- A KILLER \- Community, accessed November 6, 2025, [https://community.openai.com/t/realtime-api-pricing-vad-and-token-accumulation-a-killer/979545](https://community.openai.com/t/realtime-api-pricing-vad-and-token-accumulation-a-killer/979545)  
31. LLM API Pricing Comparison (2025): OpenAI, Gemini, Claude | IntuitionLabs, accessed November 6, 2025, [https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025](https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025)  
32. usage-based pricing and demand for residential broadband by aviv ..., accessed November 6, 2025, [https://cris.web.unc.edu/wp-content/uploads/sites/16302/2018/12/Nevo\_et\_al-2016-Econometrica.pdf](https://cris.web.unc.edu/wp-content/uploads/sites/16302/2018/12/Nevo_et_al-2016-Econometrica.pdf)  
33. What do you do about LLM token costs? : r/LLMDevs \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/LLMDevs/comments/1njmjsn/what\_do\_you\_do\_about\_llm\_token\_costs/](https://www.reddit.com/r/LLMDevs/comments/1njmjsn/what_do_you_do_about_llm_token_costs/)  
34. The Hidden “Verbosity Tax” in AI: Why Per-Token Pricing Isn't What It Seems \- DevOps.dev, accessed November 6, 2025, [https://blog.devops.dev/the-hidden-verbosity-tax-in-ai-why-per-token-pricing-isnt-what-it-seems-a3d446499102](https://blog.devops.dev/the-hidden-verbosity-tax-in-ai-why-per-token-pricing-isnt-what-it-seems-a3d446499102)  
35. Usage-Based Pricing: Models, Benefits & Implementation \- Zuora, accessed November 6, 2025, [https://www.zuora.com/guides/ultimate-guide-to-usage-based-pricing/](https://www.zuora.com/guides/ultimate-guide-to-usage-based-pricing/)  
36. The LLM Cost Paradox: How "Cheaper" AI Models Are Breaking Budgets \- IKANGAI, accessed November 6, 2025, [https://www.ikangai.com/the-llm-cost-paradox-how-cheaper-ai-models-are-breaking-budgets/](https://www.ikangai.com/the-llm-cost-paradox-how-cheaper-ai-models-are-breaking-budgets/)  
37. Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives \- arXiv, accessed November 6, 2025, [https://arxiv.org/html/2505.21627v2](https://arxiv.org/html/2505.21627v2)  
38. Consumption-Based Pricing Model: How to Make It Work for You \- Thales, accessed November 6, 2025, [https://cpl.thalesgroup.com/software-monetization/make-consumption-based-pricing-work](https://cpl.thalesgroup.com/software-monetization/make-consumption-based-pricing-work)  
39. Isn't price per token of LLMs too low? : r/LocalLLaMA \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/LocalLLaMA/comments/1mjud6n/isnt\_price\_per\_token\_of\_llms\_too\_low/](https://www.reddit.com/r/LocalLLaMA/comments/1mjud6n/isnt_price_per_token_of_llms_too_low/)  
40. Paris Metro Pricing: The minimalist differentiated services solution Andrew Odlyzko AT\&T Labs, accessed November 6, 2025, [https://www-users.cse.umn.edu/\~odlyzko/doc/paris.metro.minimal.pdf](https://www-users.cse.umn.edu/~odlyzko/doc/paris.metro.minimal.pdf)  
41. Paris Metro Pricing for the Internet \- ResearchGate, accessed November 6, 2025, [https://www.researchgate.net/publication/2318076\_Paris\_Metro\_Pricing\_for\_the\_Internet](https://www.researchgate.net/publication/2318076_Paris_Metro_Pricing_for_the_Internet)  
42. LLM Cost Calculator: Compare OpenAI, Claude2, PaLM, Cohere & More \- YourGPT, accessed November 6, 2025, [https://yourgpt.ai/tools/openai-and-other-llm-api-pricing-calculator](https://yourgpt.ai/tools/openai-and-other-llm-api-pricing-calculator)  
43. Introducing Pay-as-you-go pricing for Apigee API Management | Google Cloud Blog, accessed November 6, 2025, [https://cloud.google.com/blog/products/api-management/introducing-pay-as-you-go-pricing-for-apigee-api-management](https://cloud.google.com/blog/products/api-management/introducing-pay-as-you-go-pricing-for-apigee-api-management)  
44. What is the pay-as-you-go (PAYG) Model? Guide for SaaS Businesses \- Flexprice, accessed November 6, 2025, [https://flexprice.io/blog/pay-as-you-go-model](https://flexprice.io/blog/pay-as-you-go-model)  
45. Amazon Bedrock pricing, accessed November 6, 2025, [https://aws.amazon.com/bedrock/pricing/](https://aws.amazon.com/bedrock/pricing/)  
46. Usage-based vs Outcome-based: API Monetization Pricing Strategy | by Bharath Kumar, accessed November 6, 2025, [https://digitalapiai.medium.com/usage-based-vs-outcome-based-api-monetization-pricing-strategy-2c3e931c8192](https://digitalapiai.medium.com/usage-based-vs-outcome-based-api-monetization-pricing-strategy-2c3e931c8192)  
47. The Unit Economics of Different Pricing Models: A Strategic Guide for SaaS Executives, accessed November 6, 2025, [https://www.getmonetizely.com/articles/the-unit-economics-of-different-pricing-models-a-strategic-guide-for-saas-executives](https://www.getmonetizely.com/articles/the-unit-economics-of-different-pricing-models-a-strategic-guide-for-saas-executives)  
48. What is usage-based billing? \- Stripe, accessed November 6, 2025, [https://stripe.com/resources/more/usage-based-billing-explained-how-it-works-and-how-to-optimize-its-benefits](https://stripe.com/resources/more/usage-based-billing-explained-how-it-works-and-how-to-optimize-its-benefits)  
49. Pay-As-You-Go Insurance: Experimental Evidence on Consumer Demand and Behavior, accessed November 6, 2025, [https://www.hbs.edu/ris/Publication%20Files/23-030\_73d0c3d1-fb78-40f2-b151-741ba02340e4.pdf](https://www.hbs.edu/ris/Publication%20Files/23-030_73d0c3d1-fb78-40f2-b151-741ba02340e4.pdf)  
50. Optimize LLM API Costs: Token Strategies for 2025 \- Sparkco AI, accessed November 6, 2025, [https://sparkco.ai/blog/optimize-llm-api-costs-token-strategies-for-2025](https://sparkco.ai/blog/optimize-llm-api-costs-token-strategies-for-2025)  
51. Lambda warmness vs cost tradeoff : r/aws \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/aws/comments/rdp0bz/lambda\_warmness\_vs\_cost\_tradeoff/](https://www.reddit.com/r/aws/comments/rdp0bz/lambda_warmness_vs_cost_tradeoff/)  
52. S3 Pricing \- Amazon AWS, accessed November 6, 2025, [https://aws.amazon.com/s3/pricing/](https://aws.amazon.com/s3/pricing/)  
53. Cloud Run pricing | Google Cloud, accessed November 6, 2025, [https://cloud.google.com/run/pricing](https://cloud.google.com/run/pricing)  
54. Cloud Run functions, accessed November 6, 2025, [https://cloud.google.com/functions](https://cloud.google.com/functions)  
55. Retooling Federal Antitrust Laws to Address Modern Pricing Solutions: Pricing Algorithms and Dynamic Pricing \- Penn Carey Law: Legal Scholarship Repository, accessed November 6, 2025, [https://scholarship.law.upenn.edu/context/jli/article/1037/viewcontent/Choi\_Retooling\_Federal\_Antitrust\_Laws\_to\_Fit\_Emerging\_Technologies\_\_Dynamic\_Pricing\_Publication\_Draft\_FINAL.pdf](https://scholarship.law.upenn.edu/context/jli/article/1037/viewcontent/Choi_Retooling_Federal_Antitrust_Laws_to_Fit_Emerging_Technologies__Dynamic_Pricing_Publication_Draft_FINAL.pdf)  
56. LLM inference prices have fallen rapidly but unequally across tasks \- Epoch AI, accessed November 6, 2025, [https://epoch.ai/data-insights/llm-inference-price-trends](https://epoch.ai/data-insights/llm-inference-price-trends)  
57. The Paradox of Predatory Pricing \- Scholarship@Cornell Law: A Digital Repository, accessed November 6, 2025, [https://scholarship.law.cornell.edu/cgi/viewcontent.cgi?referer=\&httpsredir=1\&article=3010\&context=clr](https://scholarship.law.cornell.edu/cgi/viewcontent.cgi?referer&httpsredir=1&article=3010&context=clr)  
58. Entry Barriers and Contemporary Antitrust Litigation | UC Davis Business Law Journal, accessed November 6, 2025, [https://blj.ucdavis.edu/archives/7/1/entry-barriers-and-contemporary-antitrust-litigation](https://blj.ucdavis.edu/archives/7/1/entry-barriers-and-contemporary-antitrust-litigation)  
59. Token growth indicates future AI spend per dev \- Hacker News, accessed November 6, 2025, [https://news.ycombinator.com/item?id=44867312](https://news.ycombinator.com/item?id=44867312)  
60. Digital Economy / Industrial Organization \- BBVA Research, accessed November 6, 2025, [https://www.bbvaresearch.com/wp-content/uploads/2019/03/mar19\_watch\_TSE\_conference.pdf](https://www.bbvaresearch.com/wp-content/uploads/2019/03/mar19_watch_TSE_conference.pdf)  
61. Can we please talk about llm costs : r/ycombinator \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/ycombinator/comments/1nqappq/can\_we\_please\_talk\_about\_llm\_costs/](https://www.reddit.com/r/ycombinator/comments/1nqappq/can_we_please_talk_about_llm_costs/)  
62. Updates to Google Cloud's infrastructure capabilities and pricing | Hacker News, accessed November 6, 2025, [https://news.ycombinator.com/item?id=30671997](https://news.ycombinator.com/item?id=30671997)  
63. Serverless Boom or Bust? An Analysis of Economic ... \- USENIX, accessed November 6, 2025, [https://www.usenix.org/system/files/hotcloud20\_paper\_lin.pdf](https://www.usenix.org/system/files/hotcloud20_paper_lin.pdf)  
64. Price per token is going down. Price per answer is going up. \- Blog | MLOps Community, accessed November 6, 2025, [https://home.mlops.community/public/blogs/price-per-token-is-going-down-price-per-answer-is-going-up](https://home.mlops.community/public/blogs/price-per-token-is-going-down-price-per-answer-is-going-up)  
65. Billing for AI and LLM-Based APIs: Cost Control Strategies \- Kinde, accessed November 6, 2025, [https://kinde.com/learn/billing/pricing/billing-for-ai-and-llm-based-apis-cost-control-strategies/](https://kinde.com/learn/billing/pricing/billing-for-ai-and-llm-based-apis-cost-control-strategies/)  
66. How Metered Billing Benefits Your Business | BillingPlatform, accessed November 6, 2025, [https://billingplatform.com/blog/how-metered-billing-benefits-your-business](https://billingplatform.com/blog/how-metered-billing-benefits-your-business)