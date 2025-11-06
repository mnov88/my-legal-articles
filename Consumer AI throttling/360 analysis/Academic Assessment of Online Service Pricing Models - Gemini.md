  
# **An Academic Assessment of Online Service Pricing Models: Economic, Competitive, and Social Implications**

## **Executive Summary**

This report provides a doctoral-level analysis of five primary pricing models for online services: tier-based, credit-based, measured, call-based, and flat-rate. The objective is to determine their effects on consumers, businesses, and market structures, assessing which, if any, is "better" in both the immediate and long term. The analysis is conducted through the discrete lenses of microeconomic theory, behavioral economics, competition policy, development economics, and commons management.  
The central finding of this report is that no single pricing model is universally superior. Instead, each model represents a distinct and unavoidable bundle of trade-offs, particularly between economic efficiency, psychological manipulation, market competition, and social equity.  
A cross-cutting analytical framework, developed in Chapter 8, synthesizes these trade-offs. Key findings include:

* **Tier-Based (Good-Better-Best) Pricing:** This is a form of second-degree price discrimination that maximizes surplus extraction. Behaviorally, it relies on the "decoy effect" to manipulate choice. In its "freemium" variant, it can act as a powerful anti-competitive barrier to entry, and it systemically creates a "Second Digital Divide" by placing efficacy-enhancing tools behind paywalls.  
* **Credit-Based Pricing:** This model is a tool for cost abstraction and revenue pre-recognition, primarily chosen to solve a *provider's* internal cash flow and technical metering problems. It operates by exploiting the "sunk cost fallacy" and "gamification" while creating consumer-facing opacity.  
* **Measured (Pay-as-you-Go) Pricing:** This is the most economically efficient model, aligning price with marginal cost and solving the "Tragedy of the Digital Commons." However, it is behaviorally toxic, inducing "meter-running anxiety" and "bill shock," which stifles use. It transfers 100% of demand volatility risk to the consumer.  
* **Flat-Rate ("All-you-can-Eat") Pricing:** This model is the behavioral inverse of measured pricing. It is economically *inefficient* (creating cross-subsidies) and *unsustainable* (driving the "Tragedy of the Digital Commons"). However, it is preferred by consumers as an "insurance" policy against anxiety, and it uniquely promotes digital *efficacy* by removing the cost of experimentation.

The report identifies three fundamental, unresolved conflicts in the digital economy:

1. **The Predictability-Efficiency-Anxiety Trilemma:** Stakeholders must choose between the *efficiency* of Measured pricing, the *predictability* of Flat-Rate pricing, and the avoidance of *anxiety*. No model can deliver all three.  
2. **The Competition-Manipulation Paradox:** In digital markets, firms increasingly compete not on price, but on their *efficacy in exploiting the behavioral biases* of consumers (e.g., decoys, sunk costs). This undermines the rational-actor assumptions of traditional competition policy.  
3. **The Equity-Sustainability Conflict:** The model that best promotes *equity* (Flat-Rate, by encouraging use) is the same model that ensures the *unsustainability* of the shared resource. Conversely, the model that *sustains* the resource (Measured) *stifles* equitable access to efficacy.

The analysis concludes by examining these tensions in two case studies: the emerging AI LLM market, which uses a complex hybrid of all models, and the mature Cloud IaaS market, which is defined by the core conflict between measured (On-Demand) and committed flat-rate (Reserved) pricing. Ultimately, the choice of a pricing model is a policy-laden decision that pre-determines which stakeholders—consumers, producers, or the public commons—will bear the greatest cost.  
---

## **Part I: Analysis of Pricing Models**

### **Chapter 1: Tier-Based and "Good-Better-Best" Pricing**

Tier-based pricing, often manifested as a "Good-Better-Best" (G-B-B) structure, is one of the most common and effective strategies for pricing digital services. It involves offering a menu of options at different price points, with each successive tier providing additional features, higher usage limits, or greater quality. This model is not merely a simple menu; it is a sophisticated mechanism for market segmentation, psychological direction, and, in some cases, anti-competitive strategy.

#### **1.1 Microeconomic Foundations: Second-Degree Price Discrimination**

From a microeconomic perspective, tier-based pricing is a classic implementation of second-degree price discrimination.1 This form of price discrimination is employed when a firm faces a heterogeneous consumer base but cannot distinguish *a priori* between different consumer types or their specific willingness-to-pay (WTP).2 If the firm set a single, uniform price, it would face a trade-off: a high price would capture surplus from high-WTP users but exclude low-WTP users, while a low price would capture the mass market but leave significant consumer surplus on the table from high-WTP users.3  
The tiered model (G-B-B) solves this problem by inducing *consumer self-selection*.4 The firm designs a menu of price-quality combinations that are structured to make each consumer group choose the tier intended for them:

* **The "Good" Tier:** This is the basic, often stripped-down, offering. It is targeted at price-sensitive customers with a low WTP.5 Its purpose is to broaden the market base and capture consumers who would otherwise be priced out.  
* **The "Better" Tier:** This is typically the firm's core product, positioned as the standard or most popular option. It offers a balance of features and price, targeting the median consumer.  
* **The "Best" Tier:** This is the premium, feature-laden package, priced to extract the maximum possible consumer surplus from high-WTP users (e.g., "power users" or enterprises) who seek the best available option.7

By segmenting the market in this way, the firm can capture a far greater portion of the total consumer surplus than a single-price monopolist could.4

#### **1.2 Strategic Implementation: The Centrality of "Fence Attributes"**

The structural integrity of this discriminatory model depends entirely on a concept known as "fence attributes".4 A fence is a specific feature, or set of features, that is included in a higher-cost tier (or, more critically, *excluded* from a lower-cost tier) to prevent high-WTP consumers from "trading down" to the cheaper option.7  
To be effective, a fence attribute must be highly valued by the high-WTP segment but of little value to the low-WTP segment. If the fence is poorly designed, high-WTP users will simply purchase the "Good" option, and the price discrimination scheme will collapse. The "fence" inflicts a cost—of inconvenience, lost time, or missing functionality—on the high-WTP user who attempts to trade down. For instance, a SaaS platform might place critical "workflow automation" or "advanced analytics" features exclusively in the "Best" tier.7 A "Good" tier user does not miss this feature, but an enterprise user (the "Best" target) finds the "Good" tier unusable without it, forcing them to select the higher-priced option.  
A special and highly potent case of tiered pricing is the "Freemium" model.8 Here, the "Good" tier is priced at $0. This acts as a powerful marketing and customer acquisition tool, attracting a massive user base by eliminating the cost barrier to entry.1 The "fence" in a freemium model is typically severe: restrictive usage caps, the inclusion of disruptive advertising, or the withholding of all but the most basic features.9 These "fences" are designed to be sufficiently painful that a subset of the free user base, having already invested time and data into the service, will convert to a paid tier to remove the friction.9

#### **1.3 Behavioral Architecture: Choice, Manipulation, and the Decoy**

Tier-based pricing is a potent application of "choice architecture".10 The way options are presented is not neutral; it is explicitly designed to influence consumer decisions, often by exploiting cognitive biases.  
The G-B-B structure, in particular, leverages the "decoy effect," also known as the "asymmetric dominance effect".11 This effect occurs when a consumer's preference between two options (a "competitor" and a "target") is altered by the introduction of a third, asymmetrically dominated option (the "decoy").  
A famous example illustrates this: a movie theater offers a Small popcorn for $3 (the competitor) and a Large popcorn for $7 (the target). Many consumers, finding $7 too expensive, will opt for the $3 Small. However, if the theater introduces a Medium popcorn for $6.50 (the decoy), the consumer's calculus changes.13 The Medium option is clearly a "terrible deal" compared to the Large—for only $0.50 more, one gets much more popcorn. The decoy's presence makes the Large option suddenly seem like a rational "no-brainer".13 The decoy is not meant to be sold; it is meant to *make the target option look more appealing in comparison*.14  
This same logic applies to digital subscription tiers. A "Better" (middle) tier can be priced to make the "Best" (premium) tier seem like a better value. Conversely, the "Best" tier can be priced exorbitantly to make the "Better" tier (the firm's actual target) seem like a reasonable compromise. This architecture can *manipulate* consumers into purchases that are more profitable for the firm, rather than truly optimal for the user's needs.15 While this is manipulative, it also helps consumers overcome the "paradox of choice" 16, where an overabundance of options leads to decision paralysis. The G-B-B model simplifies the decision landscape to three, making a choice feel less overwhelming.17

#### **1.4 Competition and Market Structure Implications**

The "Freemium" model, in particular, has profound implications for market structure and competition policy. While it can be a pro-competitive strategy for new entrants to gain traction against incumbents 18, it can also be a powerful *anti-competitive weapon* for a dominant firm.  
When a dominant incumbent offers a "free" tier, it can create an insurmountable *barrier to entry*.20 A new entrant, which must charge a price to cover its costs and fund operations, finds it impossible to compete with the incumbent's $0 price. The incumbent can subsidize its free tier with revenue from its "Best" tier (enterprise customers) or, more insidiously, with monopoly profits from an entirely different market (e.g., advertising).  
This strategy raises significant antitrust concerns.20 It functions as a form of "behavioral predatory pricing." Traditional predatory pricing is defined as pricing below-cost to drive rivals from the market, followed by a "recoupment" phase of monopoly pricing.21 This strategy often evades traditional antitrust tests, like the Areeda-Turner test, which looks for pricing below average variable cost.23 For a digital good with a marginal cost of zero, "freemium" is not technically "below-cost." However, its *strategic function and anti-competitive effect* are identical: it forces rivals to exit the market. The "recoupment" phase is then achieved not just through future price hikes, but through the *behavioral lock-in* of the massive, captured user base and the valuable data extracted from them.9 This discrepancy between anti-competitive *effect* and the *legal definition* of predation poses a major challenge for modern competition policy.

#### **1.5 Development, Equity, and the "Digital Poverty Trap"**

The implications of tiered pricing are perhaps most critical in the context of development economics and the "digital divide".24 This divide is no longer just about *access* to technology (the First Digital Divide, or FDD) but about the *efficacy* and *skills* to use that technology for socioeconomic gain (the Second Digital Divide, or SDD).25  
Tier-based pricing models systemically create and reinforce the Second Digital Divide. They function as a "digital poverty trap." While a "Freemium" or "Good" tier may give *access* to all, thereby appearing to bridge the FDD, it simultaneously widens the SDD. By design, all efficacy-enhancing features—the advanced tools, AI assistants, API access, and higher processing limits that are required for professional, educational, and economic advancement—are locked behind the "Best" tier's paywall.27  
This structure directly mirrors and exacerbates offline socioeconomic inequalities.26 High-income, high-literacy users can afford the "Best" tier, unlocking tools that further amplify their productivity and earning potential. Low-income users, while "connected," are perpetually relegated to the "Good" tier, limiting their ability to develop digital skills and achieve upward mobility. The pricing model, therefore, does not just segment a market; it actively segments society into "can-use" and "cannot-use-effectively," reinforcing existing disparities in wealth and opportunity.25

### **Chapter 2: Credit-Based Pricing**

Credit-based pricing models represent a sophisticated hybrid, blending the predictability of subscription models with the granularity of measured usage. In this system, a consumer typically pays a recurring subscription fee (e.g., $50 per month) which grants them a fixed allowance of "credits" or "tokens." These credits are then "spent" to consume various services offered by the platform. This model has become particularly prevalent in complex, multi-product digital ecosystems, such as AI platforms, where it serves critical economic and behavioral functions.

#### **2.1 Microeconomic Function: Cost Abstraction and Revenue Pre-recognition**

The primary microeconomic function of a credit-based model is *cost abstraction*. In a platform offering disparate services—such as API calls, data storage, AI image generation, and text analysis—a credit becomes a single, unifying unit of account.28 For example, the platform can set 1 AI-generated image to cost 10 credits, while 1,000 API calls cost 1 credit.  
This abstraction is especially useful for pricing "general purpose technologies" 30, like AI, where the provider's underlying costs (e.g., variable GPU time, model inference costs) are known, but the *value* of the service to the end-user is not yet clear. In this scenario, firms often default to a *cost-plus* model, where they price to cover their variable costs plus a margin. Credits are a "bridge" to implement this: they provide a simple, customer-facing unit while allowing the firm to map those units back to their complex internal costs.28  
For the business, the credit model's most attractive feature is its impact on cash flow and revenue predictability. Because the credits are *prepaid* at the start of the billing period, the firm receives its revenue *before* the service is consumed.29 This de-risks the transaction for the seller, improves cash flow, and provides more predictable revenue than a pure pay-as-you-go model, which is billed in arrears.29

#### **2.2 Behavioral Psychology: Sunk Costs, Gamification, and "Breakage"**

While the microeconomic function is rooted in abstraction and cash flow, the model's *power* is rooted in behavioral psychology. By converting real currency (e.g., US Dollars) into an intermediate, abstract currency (e.g., "AI Credits"), the model *severs the immediate "pain of paying"*.33 When a user "spends" 10 credits, it does not trigger the same psychological pain as seeing a $1.00 charge.  
Once the credits are purchased, their monetary value becomes a *sunk cost*. This activates the "sunk cost fallacy" 34, a cognitive bias where individuals feel compelled to follow through on an endeavor because they have already invested time, effort, or money. Consumers with a non-zero credit balance feel a psychological need to "use them up" or "get their money's worth" before they expire, which in turn increases their engagement and lock-in with the platform.36  
The entire system is inherently "gamified".35 The act of "spending" credits from a "balance" feels less like a financial transaction and more like spending in-game currency. This psychological detachment from the real-world cost encourages higher consumption.  
Furthermore, a significant, non-obvious profit center for the firm is **"breakage."** This is the industry term for the value of credits that are purchased by consumers but *never redeemed*. Whether due to complex expiration policies, user forgetfulness, or a balance too small to be useful, breakage represents a 100% margin for the firm—it has received revenue for a service it never had to deliver.

#### **2.3 The Consumer Trade-off: Opacity vs. Simplicity**

The credit-based model presents a deep tension for the consumer. On one hand, the model is frequently criticized for its *opacity*.28 As one industry lead noted, "Our finance team likes it. Our customers don't know what a credit does".28 A consumer intuitively understands the value of $10, but they have no innate understanding of the value of "100 credits." This abstraction makes it difficult to compare value across competitors and can lead to frustration, especially if the "price" of services (in credits) is changed by the firm.  
On the other hand, this same abstraction is the model's primary *benefit* to the consumer. In a complex system like an AI platform, a bill based on pure measured usage (Chapter 3\) would be an incomprehensible ledger of GPU-seconds, model types, and token counts. The credit model, while opaque in its *value*, is simple in its *mechanics*. The consumer has a single, predictable unit of account.28 They have traded *price-value transparency* for *billing simplicity* and *cost-predictability* (within their prepaid amount).  
This reveals a fundamental disconnect in the model's design. It is not chosen because it is inherently superior for the consumer. Rather, it is often chosen as a *path of least resistance* that resolves the provider's internal agency problems. The firm's Finance department gets its predictable, upfront cash flow 31, and its Engineering department gets a simple metering system, as they "don't yet have the metering sophistication to track usage across multiple AI features".28 The customer, in turn, is forced to bear the *cognitive cost of opacity* so that the firm can solve its own internal constraints.

### **Chapter 3: Measured Pricing (Usage-Based, Pay-as-you-Go)**

Measured pricing, also known as "Pay-as-you-Go" (PAYG) or "consumption-based" pricing, is a model where the consumer is billed in direct proportion to their actual usage of a service. This is the model of a utility, charging for kilowatts of electricity, and it has been adopted as the default for many foundational digital services, most notably cloud computing (IaaS) and AI APIs. Unlike tiered or flat-rate models, it offers no fixed fee or allowance; price is perfectly variable with consumption.

#### **3.1 Microeconomic Rationale: The Pursuit of Allocative Efficiency**

From a microeconomic standpoint, measured pricing is the "purest" and most *efficient* model. Its rationale is to align the price a consumer pays directly with the *marginal cost* of the service they are consuming.38  
While many digital goods (like a streaming video) have a marginal cost of zero, foundational services like cloud computing and AI do not. Each API call, database query, or AI inference task consumes real, non-zero variable costs in the form of electricity, CPU/GPU cycles, and bandwidth.40  
Measured pricing is the *only* model that forces the consumer to internalize these costs. This leads to *allocative efficiency*: a consumer will (in theory) continue to consume the service until the marginal utility they receive from the next unit is equal to the marginal price. This prevents the wasteful overuse and cross-subsidization (where light users subsidize heavy users) that is endemic to flat-rate models.42 For the firm, this model is also highly scalable, as it creates higher "net dollar retention"; as a customer's business succeeds and grows, their usage (and payments) naturally increase, aligning the vendor's success with the customer's.39

#### **3.2 Behavioral Hurdles: The "Pain of Paying" and Bill Shock**

While PAYG is economically efficient, it is often *behaviorally toxic*. This model maximally activates the "pain of paying" 33, a psychological phenomenon where parting with money, especially when the transaction is salient and repeated, inflicts a small amount of "pain."  
This leads to two major behavioral problems for the consumer:

1. **"Meter-Running Anxiety":** Also known as the "taximeter effect".44 When a user is conscious that every second, every click, or every query is actively adding to their bill, they experience a low-level anxiety. This "meter running" in the back of their mind causes them to be reluctant to use the service, to experiment, or to explore new features for fear of incurring costs.45 This can lead to a state of *under-consumption*, where the user fails to extract the full value of the service.  
2. **"Bill Shock":** This is the primary risk and most-cited drawback of PAYG.46 Because usage is variable and billing is in arrears, a consumer can inadvertently rack up a massive bill. A runaway script, a misconfigured application, or a simple underestimation of demand can lead to a "shock bill" that is orders of magnitude higher than expected. This *lack of predictability* is a critical flaw, making budgeting impossible for both individuals and large enterprises.38

#### **3.3 Risk Allocation: Shifting Demand Risk to the Consumer**

The PAYG model and the flat-rate model (Chapter 5\) represent two extremes of *risk allocation*. A flat-rate model forces the *producer* to bear 100% of the demand risk; if a consumer's usage is unexpectedly high, the producer's costs increase but their revenue does not.  
The measured model does the precise opposite: it *transfers 100% of the demand risk to the consumer*.49 If the consumer's demand is volatile or unexpectedly high, they bear the full financial cost of that volatility. While this is highly attractive to suppliers, it creates the financial uncertainty that consumers, particularly enterprise-level procurement officers, are strongly motivated to avoid.44  
This "flaw" in the PAYG model—its inherent anxiety and unpredictability—has not gone un-monetized. It has spawned an entire, multi-billion dollar "FinOps" (Cloud Financial Operations) industry.46 The *sole purpose* of this meta-market is to sell software and services that help companies *manage* the complexity and *prevent* the "bill shock" that the cloud providers' own pricing models create.47 This ecosystem of monitoring, budgeting, and alert tools 50 is a market for *mitigating the anxiety* of the primary service. In effect, the service provider (like AWS) not only creates the complex PAYG model but also sells the tools (like AWS Cost Explorer) to manage it, thus capturing value at both ends of the problem.52

#### **3.4 Development & Equity: The Affordability Paradox**

In the context of development economics, measured pricing presents an "affordability paradox." On one hand, it is highly inclusive. The barrier to entry is effectively zero.33 A user in a developing nation does not need to pay a $50 upfront subscription; they can purchase a few cents' worth of compute time or a few dozen AI tokens.  
However, this low entry point masks a higher-level barrier. The "meter-running anxiety" and "bill shock" risk are *magnified* for low-income users, for whom a $10 billing error is a financial crisis, not an inconvenience. This fear can prevent the very experimentation and "efficacy-building" use that the technology is supposed to enable.26 While PAYG solves the *First* Digital Divide (access), it can exacerbate the *Second* Digital Divide (efficacy) by making *effective* or *experimental* use seem too financially dangerous.42  
Furthermore, PAYG is the *only* model that directly addresses the "Tragedy of the Digital Commons" (Chapter 5). By imposing a non-zero marginal cost on consumption, it forces users to internalize the cost of their actions, preventing the wasteful overuse that degrades a shared resource.53

### **Chapter 4: Call-Based Pricing (Fixed API Calls/Messages)**

Call-based pricing, such as a plan offering "10,000 API calls per month for $20," was a dominant model in the early "Web 2.0" API economy. It represents a functional hybrid, taking the *unit* of a measured service ("one API call") and packaging it into the *structure* of a tiered model. While it has been largely superseded in advanced services, its analysis reveals a critical evolution in how digital value is metered.

#### **4.1 Economic Distinction: A Hybrid of Tiered and Measured**

This model is not a pure PAYG system, nor is it a pure flat rate. It is best described by the economic theory of the *three-part tariff*.54 A three-part tariff (3PT) consists of:

1. A fixed *access fee* (e.g., $20/month)  
2. A bundled *allowance* of usage (e.g., 10,000 API calls)  
3. A *marginal price* for usage *beyond* the allowance (e.g., $0.01 per additional call)

Academic research has shown that this 3PT structure, under conditions of high value heterogeneity and low usage heterogeneity, can be *profit-maximizing* for the firm, outperforming both pure PAYG and pure flat-rate plans.55 It captures the predictable, recurring revenue of a subscription while also extracting additional surplus from high-use customers via overage fees.

#### **4.2 Value Alignment and its Discontents**

The central, and ultimately fatal, flaw of the call-based model is the *misalignment of "API calls" as a value metric*.56 The model operates on the assumption that all API calls are created equal, yet this is fundamentally untrue.  
A developer can make 1,000 "worthless" calls that return an error or no data. Conversely, a developer can make *one* "high-value" call that (for example) qualifies a sales lead, processes a payment, or returns a critical piece of data. The call-based model charges the developer for the 1,000 worthless calls while capturing almost no value from the single, highly profitable call.56  
This failure to align price with *value* is driving a market-wide shift *away* from "usage-based" pricing (which meters *activity*, like calls) and *toward* "outcome-based" pricing (which meters *results*, like a converted sale or a qualified lead).56  
The inadequacy of this model was most starkly exposed by the rise of AI LLMs. In the "Web 2.0" economy (e.g., a weather API), the marginal *cost* of an API call was effectively zero for the provider.56 The only cost was *access*. However, in the "AI economy," the *cost* of a single API call is *highly variable*.41 One "call" to an LLM might process a 1-token query, while the next "call" processes a 100,000-token document.58 Because the provider's *cost* is variable (based on compute), they can no longer *price* on a fixed-per-call basis; they would lose money on every complex call. This forced the shift from *call-based* pricing to *token-based* (measured) pricing, as the latter realigns price with the new locus of variable cost: compute.59

#### **4.3 Consumer Risk: Overage and "Underage"**

Like the tiered model, this structure forces consumers into a difficult optimization problem. They must select a plan (e.g., the 10,000-call tier) in *advance* of their actual usage. This creates two distinct risks:

1. **"Underage" Risk:** If the consumer's usage is *less* than 10,000 calls, they have overpaid for capacity they did not need.  
2. **"Overage" Risk:** If their usage *exceeds* 10,000 calls, they are hit with penalty pricing, which is often far more expensive than the "in-plan" rate.

This structure creates significant consumer anxiety, particularly in a dynamic context. Research on broadband plans with data caps—a functional equivalent—shows that consumers actively *throttle* their own usage as they get close to their allowance limit, for fear of incurring overage fees.60 This stifles consumption and prevents users from extracting the full value of the service, punishing them for exploration.

### **Chapter 5: Flat-Rate Pricing ("All-you-can-Eat")**

Flat-rate pricing, also known as "all-you-can-eat" (AYCE) or subscription pricing, is a model where consumers pay a single, fixed, recurring fee for theoretically unlimited access to a digital service (e.g., Netflix, Spotify). This model's profound market effects are best understood as a direct-but-opposing reaction to the anxieties of measured pricing, creating a central dilemma between psychological comfort and economic efficiency.

#### **5.1 Microeconomic & Behavioral Synthesis: The "Flat-Rate Paradox"**

In classical microeconomics, the AYCE model for digital goods (where the marginal cost of production is zero) is straightforward: the consumer pays the fixed fee and continues to consume units (e.g., watch movies) until their marginal utility from the next unit is zero.61 The price of the service should not affect the *quantity* consumed.  
However, behavioral economics reveals a far more complex reality, encapsulated in the "Flat-Rate Paradox".61 Field experiments have shown that a consumer's consumption is *not* independent of the price. In one study at an AYCE pizza restaurant, customers who were given a 50% discount *ate 27.9% less pizza* than those who paid full price.61 This is non-rational behavior; the price is a *sunk cost* and should not influence consumption. The finding suggests that consumers are actively trying to "get their money's worth" 63, consuming more when they pay more to justify the expenditure.  
This model is immensely popular with consumers, especially at the enterprise level.44 The reasons are entirely behavioral:

* **The "Insurance Effect":** Consumers, and especially enterprise CIOs, are willing to pay a *premium* for the "peace of mind" and *cost certainty* that a flat rate provides.44 The flat rate acts as an *insurance policy* against the "bill shock" 47 and "taximeter anxiety" 33 inherent in measured models.44  
* **Mental Accounting:** Flat rates eliminate the "hassle of tracking use" and the cognitive burden of "mental accounting".44

#### **5.2 Market Structure: Price Wars and Cross-Subsidization**

While behaviorally attractive, the flat-rate model has two major economic flaws. First, its simplicity makes it a ripe target for *commoditization* and *price wars*.48 When competitors all offer "unlimited" access, the only remaining vector for competition is the fixed price, leading to a race to the bottom that can erode industry profits.  
Second, the model is built on a foundation of *cross-subsidization*.42 By charging all users the same fixed fee, "light users" (who consume little) are forced to overpay, while "heavy users" (who consume a lot) are allowed to underpay. This is both *allocatively inefficient* (as the heavy users' consumption is not checked by price) and *inequitable* (as the light users are subsidizing them).42 Tiered pricing (Chapter 1\) and measured pricing (Chapter 3\) are, in effect, direct economic *solutions* to this cross-subsidization problem.

#### **5.3 Commons Management: The "Tragedy of the Digital Commons"**

The most significant, long-term macro effect of flat-rate pricing is that it is the primary *economic driver* of the "Tragedy of the Digital Commons" (TDC).65  
The "tragedy," as first described by Garrett Hardin, occurs when multiple individuals, acting independently in their own rational self-interest, deplete or destroy a shared, finite resource (a "commons"), even when it is clear that doing so is not in anyone's long-term interest.66 The tragedy occurs because each individual user receives the full benefit of their own consumption, but the *cost* of that consumption (e.g., a slightly more depleted pasture) is distributed across *all* users.  
In the digital realm, the "commons" is not a pasture, but a set of finite resources: network bandwidth, server compute capacity, human support staff, and even the "Infosphere" (the shared environment of high-quality, non-spam information).65 A flat-rate pricing model *sets the marginal price of consumption to zero*. It economically *incentivizes* each user to consume as much as possible, as there is no individual cost to doing so. This rational, individual behavior leads to the collective-action failure of the TDC: network congestion, server degradation, and information pollution.65 The "free-riding" problem that threatens the sustainability of the open-source software "commons" 67 is a direct consequence of this zero-price (flat-rate) dynamic.  
This analysis reveals the central, unresolved dilemma of the digital economy. Measured pricing (Chapter 3\) is the *economic solution* to the *Tragedy of the Commons*, as it imposes a marginal cost and forces users to internalize the cost of their consumption.53 However, flat-rate pricing is the *behavioral solution* to the *anxiety* of measured pricing.44 Therefore, the market is locked in a direct conflict: the model that *solves* the sustainability problem (Measured) is the one that is *psychologically painful*, while the model that *solves* the psychological problem (Flat-Rate) is the one that is *economically unsustainable*.  
---

## **Part II: Case Studies in Practice**

### **Chapter 6: Case Study I: AI LLMs (The Measured, Tiered, and Credit Model Nexus)**

The nascent, hyper-competitive market for Large Language Model (LLM) APIs provides a near-perfect "natural experiment" to observe these pricing models colliding and hybridizing in real-time.68 Unlike mature markets that have converged on a dominant logic, the AI market (comprising providers like OpenAI, Anthropic, Google, and Mistral) is actively experimenting with a mix of all models, strategically segmenting Business-to-Consumer (B2C) and Business-to-Developer (B2B) customers.70

#### **6.1 Dominant Model Analysis: Multi-Dimensional Measured Pricing**

The core B2B (developer/API) model is *measured*, but with a crucial evolution. The unit of consumption is not the "API call" (Chapter 4), but the **"token"**—a fraction of a word.58 This shift is a direct economic response to the nature of the service. As established, the primary *variable cost* for an LLM provider is not access, but *compute* (GPU time).41 Because the amount of compute required is directly proportional to the *number of tokens* processed (both in the prompt and the response), token-based pricing perfectly aligns the provider's *cost* with the customer's *price*.59  
This model is even more granular: it is a *multi-dimensional measured* model. Providers charge different rates for **input tokens** (the prompt) and **output tokens** (the model's generated response).58 For example, Anthropic's Claude 3.5 Sonnet costs $3 per million input tokens but $15 per million output tokens.71  
This structure is theoretically optimal, as described in recent economic frameworks.59 The lower input price reflects the provider's *operational cost* of processing the prompt ($\\text{c}\_x$). The significantly higher output price reflects both the higher *computational cost* of generation ($\\text{c}\_y$) and, more importantly, the fact that the *economic value* for the user is captured in the *output*.59

#### **6.2 Hybridization in Practice: Layering Models for Market Segmentation**

While the B2B market is built on measured tokens, providers use other models to segment the *entire* market:

* **Tier-Based (G-B-B):** The "Good-Better-Best" structure is used to price *model quality*. The "fence attribute" 7 is the model's intelligence and capability. A developer or business can self-select:  
  * **"Good":** Low-cost, high-speed, but less "smart" models for simple tasks (e.g., Anthropic's Haiku 71, OpenAI's GPT-4o-mini 74).  
  * **"Better":** The mid-tier, balancing cost and performance (e.g., Anthropic's Sonnet 71, Mistral Large 2 72).  
  * **"Best":** The expensive, state-of-the-art "frontier" models for high-stakes tasks (e.g., Anthropic's Opus 71, OpenAI's GPT-5 Pro 76).  
* **Flat-Rate:** This model is used *exclusively* for B2C end-users (e.g., the $20/month ChatGPT Plus or Anthropic Pro).58 This is a direct behavioral strategy. The provider *knows* that B2C users would suffer from the "meter-running anxiety" of token pricing, so they offer a flat-rate "insurance" policy 44 to maximize B2C adoption, while "power users" on the API bear the measured cost.  
* **Credit-Based:** This model is not typically used by the *foundational* providers (like OpenAI) but is the dominant model for the *SaaS intermediaries* who "wrap" their APIs.28 A SaaS company will *buy* measured tokens from OpenAI (a variable cost) but *sell* prepaid, abstract "credits" to their end-users. This solves *their* cash flow problem 31 and simplifies *their* metering challenges.28

#### **6.3 Table 1: Comparative LLM API Pricing (Mid-2025)**

The G-B-B tiers are clearly visible when comparing the token-based API pricing across providers.

| Provider | Model (Tier) | Input ($/Million tokens) | Output ($/Million tokens) | Context Window |
| :---- | :---- | :---- | :---- | :---- |
| OpenAI | GPT-4o-mini (Good) | $0.15 | $0.60 | 128k 74 |
| OpenAI | GPT-5 Pro (Best) | $15.00 | \[N/A\] | \[N/A\]76 |
| Anthropic | Claude 3.5 Haiku (Good) | $0.25 | $1.25 | 200k 71 |
| Anthropic | Claude 3.5 Sonnet (Better) | $3.00 | $15.00 | 200k 71 |
| Anthropic | Claude 3 Opus (Best) | $15.00 | $75.00 | 200k 71 |
| Mistral | Mistral Large 2 (Better) | $3.00 | $9.00 | 128k 72 |
| Google | Gemini Pro (Better) | $0.002/1K ($2.00) | $0.006/1K ($6.00) | \[N/A\]78 |

Note: Prices and models are based on provided research data and reflect the 2024-2025 landscape.58

#### **6.4 Long-Term Implications: Innovation vs. Commons**

This pricing structure creates a new *innovation bottleneck*. The high cost of "Best" models (e.g., Opus at $75/M output tokens) 75 is prohibitive for startups and developers for everyday use. Fearing "bill shock," they will "flight to quality-for-price," defaulting to "Good" or "Better" models (like Haiku or Sonnet) for the bulk of their applications.75 This can stifle experimentation and slow the adoption of the most powerful AI.  
This, in turn, creates a "flight to the commons." To avoid the high, measured costs of private APIs, developers are increasingly turning to open-source models that can be run on their own hardware.67 While this fosters innovation, it places an enormous strain on the open-source "digital commons," which is often maintained by volunteers and non-profits and is already threatened by "free-riding" and under-funding.67

### **Chapter 7: Case Study II: Cloud Infrastructure (The Flat-Rate vs. Measured Dilemma)**

The Infrastructure-as-a-Service (IaaS) cloud market—dominated by the oligopoly of Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP) 79—is a mature, hyper-scale market. Its pricing landscape is a direct manifestation of the core, unresolved conflict identified in Chapter 5: the *dilemma between flexibility and predictability*.80

#### **7.1 The Core Tension: On-Demand vs. Reserved**

The entire, complex catalog of IaaS pricing 83 can be simplified to a strategic choice between two opposing poles, which directly map to the measured vs. flat-rate conflict:

* **Measured (On-Demand):** This is the default PAYG model.52 It offers perfect flexibility: a developer can spin up a server for seconds and terminate it, paying only for what they use.86 However, this flexibility comes at the *highest* unit price.82 Its fundamental flaw is the *anxiety* it produces, manifested in the enterprise-grade problem of "bill shock".46  
* **Flat-Rate (Reserved Instances & Savings Plans):** These are *not* pure flat-rates (like Netflix), but rather *long-term commitments* to a fixed *capacity* (Reserved Instances \- RIs) or a fixed *hourly spend* (Savings Plans \- SPs).52 In exchange for this 1- or 3-year commitment, the customer receives a massive discount (up to 75%) on the On-Demand price.81

This "commitment-for-discount" model is a direct market response to "bill shock." Enterprise buyers, driven by the need for budget predictability, *hate* the volatility of PAYG.44 RIs and SPs are, in effect, *insurance products* that allow a CFO to exchange the *flexibility* (valued by developers) for the *certainty* (valued by the business).44

#### **7.2 Table 2: Cloud Pricing Model Trade-offs**

This table synthesizes the complex trade-offs between the primary IaaS pricing models, highlighting the risk/cost/flexibility matrix for the consumer.

| Model | Description | Cost (Unit) | Flexibility | Commitment | Primary Risk (for Consumer) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **On-Demand (Measured)** | Pay-as-you-go (per second/hour) | Highest | Total | None | **"Bill Shock"** (Unpredictable high costs) 47 |
| **Reserved Instances (Flat-Rate Commitment)** | Commit to a *specific instance* (1-3 yr) | Lowest | Very Low | High (1-3 yr) | **"Overprovisioning" / Lock-in** (Paying for unused capacity) 82 |
| **Savings Plans (Flat-Rate Commitment)** | Commit to a *dollar spend* ($/hr) (1-3 yr) | Low | Medium | High (1-3 yr) | **"Overcommitment"** (Wasted spend if usage drops) 82 |
| **Spot Instances (Market)** | Bid on spare, unused capacity | Near-Zero | None | None | **"Interruption"** (Instance can be terminated by provider) 82 |

#### **7.3 Behavioral & Agency Problems in Procurement**

The IaaS pricing structure creates a significant *principal-agent problem* not between the provider and the buyer, but *within the buying organization itself*.

* **The Agents (Developers):** Their primary incentive is *flexibility* and *speed*. They prefer to use On-Demand instances to experiment and build without constraints. They are often *insensitive* to the cost, as they do not see the final bill.  
* **The Principals (CFOs/FinOps):** Their primary incentive is *cost predictability* and *budget adherence*. They despise On-Demand volatility and strongly prefer to lock in costs with RIs and Savings Plans.44

This internal conflict *is* the modern field of "FinOps".46 The entire discipline exists to create monitoring and governance structures that force the "Agents" (developers) to be accountable for the "Principals'" (CFOs') cost-efficiency goals. The pricing model's complexity necessitates a new organizational function just to manage it.

#### **7.4 Competition and Lock-In**

In this oligopolistic market, the *complexity* of the pricing models is, itself, a powerful anti-competitive tool that creates *customer lock-in*. The various types of RIs (Standard vs. Convertible) 87, Savings Plans (EC2 vs. Compute), and region-specific pricing 40 make a true "apples-to-apples" comparison between providers nearly impossible.  
Migrating a large-scale application from AWS to Azure 89 is not merely a technical challenge; it is a massive *financial* one. It would require the business to liquidate a complex, multi-year portfolio of AWS RIs and SPs (often at a loss) and accurately re-calculate an entirely new, equally complex portfolio for Azure. This financial *switching cost* is a formidable barrier to entry for competitors and a powerful lock-in mechanism for incumbents. Providers even use dominance in one market (like Microsoft's on-premise software) to create pricing advantages in another (the "Azure Hybrid Benefit"), further complicating the competitive landscape.89  
---

## **Part III: Synthesis and Framework**

### **Chapter 8: A Cross-Cutting Framework for Pricing Model Analysis**

The preceding chapters have analyzed five pricing models through five distinct theoretical lenses. This analysis demonstrates that no model is inherently "better"; each is a complex bundle of trade-offs. To synthesize these findings, this chapter develops a single, cross-cutting analytical framework. This "Pricing Model Analysis Matrix" is designed to make these trade-offs explicit, allowing for a comparative assessment of the systemic impact of each model.

#### **8.1 The Pricing Model Analysis Matrix**

The matrix below maps each pricing model (rows) against its primary function and impact across our five analytical lenses (columns).

| Pricing Model | 1\. Primary Microeconomic Function | 2\. Key Behavioral Lever (Consumer) | 3\. Market Structure Impact (Macro) | 4\. Risk Allocation (Who bears volatility?) | 5\. Equity & Commons Impact |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Tier-Based (G-B-B)** | 2nd-Degree Price Discrimination (Self-selection) 4 | **Decoy Effect / Middle-Option Bias** (Manipulates choice to "target") 11 | **Anti-Competitive Barrier** (When "Freemium," blocks new entrants) 20 | **Shared.** Consumer is "locked-in" to tier, but protected from overage *within* it. | **Negative (Equity):** *Creates* the Second Digital Divide (Efficacy Gap) 26 |
| **Credit-Based** | Cost Abstraction & **Revenue Pre-recognition** (Improves provider cash flow) 29 | **Sunk Cost Fallacy / Gamification** (Drives engagement to "use up" credits) 34 | **Enabler for Cost-Plus** (A "bridge" for pricing new tech like AI) 28 | **Consumer.** Pre-pays for credits that can expire, be devalued, or "break" (lost). | **Negative (Commons):** Obscures true cost, preventing efficient resource allocation. |
| **Measured (PAYG)** | 1st-Degree Price Discrimination / **Allocative Efficiency** (Aligns price with MC) 1 | **"Pain of Paying" / "Meter-Running Anxiety"** (Deters usage, causes anxiety) 33 | **Enables Granular Competition;** Creates "FinOps" meta-market 46 | **Consumer.** Bears 100% of demand volatility risk ("Bill Shock") 47 | **Positive (Commons):** *Solves* Tragedy of the Commons. **Negative (Equity):** *Hinders* Efficacy (SDD) via anxiety. |
| **Call-Based (Hybrid)** | **Three-Part Tariff** (Profit maximization via fee \+ allowance \+ overage) 55 | **Overage-Aversion / Allowance Optimization** (Deters usage near cap) 60 | **Obsolete;** Poor value-alignment, encourages shift to outcome-pricing 56 | **Consumer.** Bears both "overage" (penalty) and "underage" (waste) risk. | **Negative (Equity):** Punishes users for exploration, stifling efficacy. |
| **Flat-Rate (AYCE)** | **Market Penetration / Cross-Subsidization** (Light users subsidize heavy) 42 | **"Insurance Effect" / Sunk Cost (Consumption)** (Pay premium for certainty; consume more) 44 | **Drives Commoditization** (Leads to price wars) 48 | **Producer.** Bears 100% of demand volatility risk (costs rise, revenue is fixed). | **Positive (Equity):** *Solves* Efficacy (SDD) by promoting experimentation. **Negative (Commons):** *Drives* Tragedy of the Commons 65 |

#### **8.2 Analysis of the Framework: The Great Trade-offs**

This framework reveals that the choice of a pricing model is not a simple business decision, but a strategic declaration of which stakeholders will be prioritized and which trade-offs are considered acceptable. Three core, unresolved conflicts emerge from this analysis.

##### **8.2.1 The Predictability-Efficiency-Anxiety Trilemma**

The matrix demonstrates a fundamental trilemma between three desirable, but mutually exclusive, states:

1. **Measured (PAYG)** pricing is highly **Efficient** in its allocation of resources 38 but generates maximal **Anxiety** for the consumer 33 and offers zero **Predictability**.47  
2. **Flat-Rate** pricing is highly **Predictable** and has zero **Anxiety** 44, but it is definitionally **Inefficient**, creating cross-subsidies 42 and the Tragedy of the Digital Commons.65  
3. **Tiered and Credit** models are *compromises*. They try to offer *some* predictability (a fixed tier/credit price) while maintaining *some* efficiency (higher tiers cost more). But they achieve this compromise by introducing *behavioral manipulation* and *cognitive costs* (decoys, opacity).13

A firm or regulator cannot optimize for all three virtues. The choice of a pricing model is an explicit statement about which virtue is being sacrificed.

##### **8.2.2 The Competition-Manipulation Paradox**

Traditional competition policy operates on the assumption that competition leads to better outcomes (lower prices, higher quality) for rational consumers.92 This framework shows that in digital markets, this assumption is failing.  
Firms are increasingly competing not just on price, but on their *effectiveness in exploiting the behavioral biases* of consumers. The "decoy effect" 13, the "sunk cost fallacy" 34, and the selling of "anxiety-insurance" 44 are not *bugs* in these pricing models; they are the core *features* on which firms compete.  
This is a "competition-manipulation paradox": the more firms compete, the more sophisticated the psychological manipulation becomes. This is supercharged by *algorithmic pricing*, which can learn, test, and personalize these manipulative tactics at a scale and speed that humans cannot.22 Competition policy, which is designed to police rational-world problems like predatory pricing 21, is almost entirely unequipped to handle a market where the *basis of competition* is the *exploitation of irrationality*.9

##### **8.2.3 The Equity-Sustainability Conflict**

The framework reveals a profound and direct conflict between two major societal goals:

1. **Solving the Equity Problem (The Second Digital Divide):** To close the *efficacy gap* 26, users must be free to experiment, learn, and use advanced tools without fear. The **Flat-Rate** model, by removing marginal cost and anxiety, is by far the best model to promote this.44  
2. **Solving the Sustainability Problem (The Tragedy of the Commons):** To preserve the shared resources (bandwidth, compute, etc.), overuse must be prevented.65 The **Measured** model, by imposing a marginal cost for every unit of consumption, is the *only* model that achieves this.53

These two goals are in direct opposition. The very model that *promotes equity of efficacy* (Flat-Rate) is the one that *destroys the shared resource*. The model that *saves the resource* (Measured) is the one that *stifles equity* by inducing anxiety and penalizing experimentation.

### **Chapter 9: Concluding Analysis**

This report's granular analysis of online pricing models, synthesized through the matrix in Chapter 8, provides a definitive answer to the user's core query: no model is "better" for consumers and businesses. The "best" model is entirely dependent on the stakeholder's perspective and the specific outcome being optimized.

#### **9.1 Answering the Core Question: Which Model is "Better"?**

* **"Better" for an Incumbent Business:** A hybrid **three-part tariff** (like the Call-Based model) 55 or a strategically "fenced" **G-B-B (Tiered)** model.4 These models are superior for profit maximization, as they combine the predictable revenue of subscriptions with the surplus-extraction of price discrimination and overage fees.  
* **"Better" for a Consumer's Psychology:** A **Flat-Rate** model. Despite its inefficiency, it provides an "insurance" value against the anxiety of "bill shock".44 Consumers are demonstrably willing to pay a premium for this "peace of mind."  
* **"Better" for a Consumer's Wallet (Efficiency):** A "pure" **Measured** model. This is the only model that is "fair" in the sense that users pay *only* for what they consume. It ends the *cross-subsidization* 42 where light users are forced to pay for the consumption of heavy users.  
* **"Better" for Market Competition:** A transparent **Measured** model. It aligns price with cost, limiting the opaque, manipulative aspects of credit-based systems 28 and the anti-competitive "freemium" predation of tiered models.20  
* **"Better" for Social Equity (Efficacy):** A **Flat-Rate** model. By removing the marginal cost and the anxiety of experimentation, it is the *only* model that truly encourages users to develop the skills and *efficacy* needed to close the Second Digital Divide.26  
* **"Better" for Social Sustainability (The Commons):** A **Measured** model. It is the *only* model that imposes a marginal cost that forces users to internalize their consumption, thereby preventing the "Tragedy of the Digital Commons".65

#### **9.2 Immediate vs. Long-Term Effects**

The analysis also highlights a sharp conflict between immediate gains and long-term consequences:

* **Freemium:** The *immediate* effect is market inclusion and consumer surplus. The *long-term* effect is market concentration and a powerful barrier to entry.20  
* **Measured (PAYG):** The *immediate* effect is consumer anxiety and "bill shock".33 The *long-term* effect is a sustainable resource (no TDC) 65 and the creation of an entirely new "FinOps" meta-market.46  
* **Flat-Rate (AYCE):** The *immediate* effect is consumer satisfaction and high engagement.44 The *long-term* effect is resource degradation, congestion, and the "Tragedy of the Digital Commons".65

#### **9.3 Future Research Directions**

This report's findings suggest several urgent areas for future doctoral analysis:

1. **Algorithmic Predation:** The concept of "behavioral predatory pricing," where "freemium" tiers function anti-competitively without triggering traditional legal tests, requires urgent empirical study and new legal-economic theory. The work of scholars on algorithmic predation 22 must be expanded to include freemium models.  
2. **Outcome-Based Pricing:** This report notes the *shift* away from usage-based pricing (metering *activity*) and toward outcome-based pricing (metering *results*).56 The microeconomics, behavioral impacts, and potential for manipulation in *this* new, emerging model are almost entirely un-studied.  
3. **Regulating Choice Architecture:** As competition policy is ill-equipped to handle markets based on psychological manipulation 10, new frameworks are needed. Research is required on how to regulate *choice architecture*, *pricing-induced anxiety*, and *data-driven manipulation* 9 without stifling the innovation and investment that UBP models can foster.53

#### **Works cited**

1. Pricing Strategies in a Digital Economy: A Microeconomic Perspective, accessed November 6, 2025, [https://www.abacademies.org/articles/pricing-strategies-in-a-digital-economy-a-microeconomic-perspective-17498.html](https://www.abacademies.org/articles/pricing-strategies-in-a-digital-economy-a-microeconomic-perspective-17498.html)  
2. Unlocking Market Potential: Strategic Consumer Segmentation and Dynamic Pricing for Balancing Loyalty and Deal Seeking \- MDPI, accessed November 6, 2025, [https://www.mdpi.com/2227-7390/12/21/3364](https://www.mdpi.com/2227-7390/12/21/3364)  
3. Understanding the Theory of Price: Supply, Demand, and Market Equilibrium \- Investopedia, accessed November 6, 2025, [https://www.investopedia.com/terms/t/theory-of-price.asp](https://www.investopedia.com/terms/t/theory-of-price.asp)  
4. The Good-Better-Best Approach to Pricing | Harvard Business ..., accessed November 6, 2025, [https://hbsp.harvard.edu/product/R1805H-PDF-ENG](https://hbsp.harvard.edu/product/R1805H-PDF-ENG)  
5. Good-Better-Best pricing strategy: Examples, Main Approaches and Useful Tips | Priceva, accessed November 6, 2025, [https://priceva.com/blog/good-better-best-pricing-strategy](https://priceva.com/blog/good-better-best-pricing-strategy)  
6. Good, Better, Best Pricing Guide \- FieldPulse, accessed November 6, 2025, [https://www.fieldpulse.com/resources/blog/good-better-best-pricing-guide](https://www.fieldpulse.com/resources/blog/good-better-best-pricing-guide)  
7. Architecting Good-Better-Best Pricing \- Revenue Management Labs, accessed November 6, 2025, [https://revenueml.com/insights/articles/architecting-good-better-best-pricing](https://revenueml.com/insights/articles/architecting-good-better-best-pricing)  
8. Mastering tiered pricing: Strategy for revenue maximization \- Simon-Kucher, accessed November 6, 2025, [https://www.simon-kucher.com/en/insights/mastering-tiered-pricing-strategy-revenue-maximization](https://www.simon-kucher.com/en/insights/mastering-tiered-pricing-strategy-revenue-maximization)  
9. (PDF) Behavioral Economics and Pricing Strategy Optimization in the Digital Age---A Case Study of Spotify \- ResearchGate, accessed November 6, 2025, [https://www.researchgate.net/publication/392535489\_Behavioral\_Economics\_and\_Pricing\_Strategy\_Optimization\_in\_the\_Digital\_Age---A\_Case\_Study\_of\_Spotify](https://www.researchgate.net/publication/392535489_Behavioral_Economics_and_Pricing_Strategy_Optimization_in_the_Digital_Age---A_Case_Study_of_Spotify)  
10. Behavioral Economics in The Era of Digital Subscriptions: Choice or ..., accessed November 6, 2025, [https://academicopinion.org/index.php/pub/article/view/68](https://academicopinion.org/index.php/pub/article/view/68)  
11. The Decoy Effect in Marketing: Description, Psychology, and Examples \- Lead Alchemists, accessed November 6, 2025, [https://www.leadalchemists.com/marketing-psychology/cognitive-biases-marketing/decoy-effect/](https://www.leadalchemists.com/marketing-psychology/cognitive-biases-marketing/decoy-effect/)  
12. (PDF) THE INFLUENCE OF DECOY PRICING ON CONSUMER DECISION-MAKING: A COMPREHENSIVE ANALYSIS \- ResearchGate, accessed November 6, 2025, [https://www.researchgate.net/publication/387754684\_THE\_INFLUENCE\_OF\_DECOY\_PRICING\_ON\_CONSUMER\_DECISION-MAKING\_A\_COMPREHENSIVE\_ANALYSIS](https://www.researchgate.net/publication/387754684_THE_INFLUENCE_OF_DECOY_PRICING_ON_CONSUMER_DECISION-MAKING_A_COMPREHENSIVE_ANALYSIS)  
13. Decoy Effect \- The Decision Lab, accessed November 6, 2025, [https://thedecisionlab.com/biases/decoy-effect](https://thedecisionlab.com/biases/decoy-effect)  
14. Positioning decoy pricing to shape how customers perceive value \- Simon-Kucher, accessed November 6, 2025, [https://www.simon-kucher.com/en/insights/positioning-decoy-pricing-shape-how-customers-perceive-value](https://www.simon-kucher.com/en/insights/positioning-decoy-pricing-shape-how-customers-perceive-value)  
15. Impacts of Visualizations on Decoy Effects \- PMC \- PubMed Central, accessed November 6, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8657019/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8657019/)  
16. Behavioral Economics and Consumer Decision-Making in the Digital Age \- International Journal of Social Impact, accessed November 6, 2025, [https://ijsi.in/wp-content/uploads/2025/07/18.02.024.20251003.pdf](https://ijsi.in/wp-content/uploads/2025/07/18.02.024.20251003.pdf)  
17. Behavioural Economics – Good Better Best Pricing \- ECONFIX \- WordPress.com, accessed November 6, 2025, [https://econfix.wordpress.com/2018/10/25/behavioural-economics-good-better-best-pricing/](https://econfix.wordpress.com/2018/10/25/behavioural-economics-good-better-best-pricing/)  
18. Competitors' pricing strategies: How to build a smarter pricing model \- Stripe, accessed November 6, 2025, [https://stripe.com/resources/more/competitors-pricing-strategies](https://stripe.com/resources/more/competitors-pricing-strategies)  
19. Competitive Pricing | Strategy Definition \+ Examples \- Wall Street Prep, accessed November 6, 2025, [https://www.wallstreetprep.com/knowledge/competitive-pricing/](https://www.wallstreetprep.com/knowledge/competitive-pricing/)  
20. Tiered Pricing Models & Their Antitrust Implications \- Attorney Aaron Hall, accessed November 6, 2025, [https://aaronhall.com/tiered-pricing-models-antitrust-implications/](https://aaronhall.com/tiered-pricing-models-antitrust-implications/)  
21. predatory pricing. The recoupment \- COLUMBIA LAW REVIEW, accessed November 6, 2025, [https://columbialawreview.org/wp-content/uploads/2016/04/Leslie.pdf](https://columbialawreview.org/wp-content/uploads/2016/04/Leslie.pdf)  
22. PREDATORY PRICING ALGORITHMS \- NYU Law Review, accessed November 6, 2025, [https://www.nyulawreview.org/wp-content/uploads/2023/04/98NYULRev49.pdf](https://www.nyulawreview.org/wp-content/uploads/2023/04/98NYULRev49.pdf)  
23. Abusive pricing practices by online platforms: a framework review of Article 102 TFEU for future cases | Journal of Antitrust Enforcement | Oxford Academic, accessed November 6, 2025, [https://academic.oup.com/antitrust/article/10/3/469/6523295](https://academic.oup.com/antitrust/article/10/3/469/6523295)  
24. THE DIGITAL DIVIDE AND ECONOMIC BENEFITS OF BROADBAND ACCESS \- Obama White House Archives, accessed November 6, 2025, [https://obamawhitehouse.archives.gov/sites/default/files/page/files/20160308\_broadband\_cea\_issue\_brief.pdf](https://obamawhitehouse.archives.gov/sites/default/files/page/files/20160308_broadband_cea_issue_brief.pdf)  
25. Full article: Two digital divides and income inequality: a global perspective, accessed November 6, 2025, [https://www.tandfonline.com/doi/full/10.1080/15140326.2025.2568247](https://www.tandfonline.com/doi/full/10.1080/15140326.2025.2568247)  
26. Bridging Digital Divides: a Literature Review and Research Agenda ..., accessed November 6, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7786312/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7786312/)  
27. The Anatomy Of Saas Pricing Strategy, accessed November 6, 2025, [https://soporte.ujcv.edu.hn/Resources/OIJ6vh/5S9104/The%20Anatomy%20Of%20Saas%20Pricing%20Strategy.pdf](https://soporte.ujcv.edu.hn/Resources/OIJ6vh/5S9104/The%20Anatomy%20Of%20Saas%20Pricing%20Strategy.pdf)  
28. Using Credit-Based Pricing In AI-Powered SaaS: What Works And ..., accessed November 6, 2025, [https://www.forbes.com/sites/metronome/2025/10/01/using-credit-based-pricing-in-ai-powered-saas-what-works-and-what-doesnt/](https://www.forbes.com/sites/metronome/2025/10/01/using-credit-based-pricing-in-ai-powered-saas-what-works-and-what-doesnt/)  
29. What are credit-based pricing models and how do they work? \- Lago Blog, accessed November 6, 2025, [https://www.getlago.com/blog/credit-based-pricing](https://www.getlago.com/blog/credit-based-pricing)  
30. Why tokens and credits are becoming a standard approach to pricing AI solutions \- Ibbaka, accessed November 6, 2025, [https://www.ibbaka.com/ibbaka-market-blog/why-tokens-and-credits-are-becoming-a-standard-approach-to-pricing-ai-solutions](https://www.ibbaka.com/ibbaka-market-blog/why-tokens-and-credits-are-becoming-a-standard-approach-to-pricing-ai-solutions)  
31. What is a credits-based subscription model and how does it work? \- Stripe, accessed November 6, 2025, [https://stripe.com/en-jp/resources/more/what-is-a-credits-based-subscription-model-and-how-does-it-work](https://stripe.com/en-jp/resources/more/what-is-a-credits-based-subscription-model-and-how-does-it-work)  
32. Subscription vs. Credit-Based System? : r/SaaS \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/SaaS/comments/1gh0n4q/subscription\_vs\_creditbased\_system/](https://www.reddit.com/r/SaaS/comments/1gh0n4q/subscription_vs_creditbased_system/)  
33. A Behavioral Economist Breaks Down The Pain of Paying \- Blog, accessed November 6, 2025, [https://blog.acumenacademy.org/pain-paying/](https://blog.acumenacademy.org/pain-paying/)  
34. The Sunk Cost Fallacy \- The Decision Lab, accessed November 6, 2025, [https://thedecisionlab.com/biases/the-sunk-cost-fallacy](https://thedecisionlab.com/biases/the-sunk-cost-fallacy)  
35. How the Sunk Cost Fallacy Keeps You Playing Games, accessed November 6, 2025, [https://gamequitters.com/how-the-sunk-cost-fallacy-keeps-you-playing-games/](https://gamequitters.com/how-the-sunk-cost-fallacy-keeps-you-playing-games/)  
36. "Mobile Games and the Sunk Cost Fallacy" by Sadie L. Phillips \- Open Works, accessed November 6, 2025, [https://openworks.wooster.edu/independentstudy/9276/](https://openworks.wooster.edu/independentstudy/9276/)  
37. Product design and psychology: The Exploitation of the Sunk Cost Fallacy in Video Game Design | by Milijana Komad | Medium, accessed November 6, 2025, [https://medium.com/@milijanakomad/product-design-and-psychology-the-exploitation-of-the-sunk-cost-fallacy-in-video-game-design-d60385e39fec](https://medium.com/@milijanakomad/product-design-and-psychology-the-exploitation-of-the-sunk-cost-fallacy-in-video-game-design-d60385e39fec)  
38. Usage-Based Pricing (UBP) | Strategy Definition \+ Examples \- Wall Street Prep, accessed November 6, 2025, [https://www.wallstreetprep.com/knowledge/usage-based-pricing-ubp/](https://www.wallstreetprep.com/knowledge/usage-based-pricing-ubp/)  
39. Usage-Based Pricing vs Subscription Models \- RightRev, accessed November 6, 2025, [https://www.rightrev.com/usage-based-pricing-vs-subscription/](https://www.rightrev.com/usage-based-pricing-vs-subscription/)  
40. Key principles \- How AWS Pricing Works, accessed November 6, 2025, [https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/key-principles.html](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/key-principles.html)  
41. The New Economics of AI Pricing: Models That Actually Work | Pilot Blog, accessed November 6, 2025, [https://pilot.com/blog/ai-pricing-economics-2025](https://pilot.com/blog/ai-pricing-economics-2025)  
42. The Economics of Broadband Data Caps and Usage-Based Pricing, accessed November 6, 2025, [https://laweconcenter.org/resources/the-economics-of-broadband-data-caps-and-usage-based-pricing/](https://laweconcenter.org/resources/the-economics-of-broadband-data-caps-and-usage-based-pricing/)  
43. A Primer: Subscription vs Usage Based Pricing Models \- Mostly metrics, accessed November 6, 2025, [https://www.mostlymetrics.com/p/usage-based-is-best-if-you-are-already](https://www.mostlymetrics.com/p/usage-based-is-best-if-you-are-already)  
44. Flat-rate pricing isn't rational but psychological—that's why it wins ..., accessed November 6, 2025, [https://www.hfsresearch.com/research/pricing-rational-psychological-wins/](https://www.hfsresearch.com/research/pricing-rational-psychological-wins/)  
45. Quantifying the subjective cost of self-control in humans \- PMC \- PubMed Central, accessed November 6, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8536396/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8536396/)  
46. Avoid Cloud Bill Shock: Cost Optimization Tips Every Small Business Should Know, accessed November 6, 2025, [https://velocitytech.com/blog/avoid-cloud-bill-shock-cost-optimization-tips-every-small-business-should-know/](https://velocitytech.com/blog/avoid-cloud-bill-shock-cost-optimization-tips-every-small-business-should-know/)  
47. Why Cloud Analytics May Create a Bill Shock and How to Avoid It, accessed November 6, 2025, [https://sqream.com/blog/why-cloud-analytics-may-create-a-bill-shock-and-how-to-avoid-it/](https://sqream.com/blog/why-cloud-analytics-may-create-a-bill-shock-and-how-to-avoid-it/)  
48. Cloud computing pricing: Beware the bill shock \- ZDNET, accessed November 6, 2025, [https://www.zdnet.com/article/cloud-computing-pricing-beware-the-bill-shock/](https://www.zdnet.com/article/cloud-computing-pricing-beware-the-bill-shock/)  
49. An Analysis of Usage-Based Pricing Policies for Smart Products \- ResearchGate, accessed November 6, 2025, [https://www.researchgate.net/publication/220505613\_An\_Analysis\_of\_Usage-Based\_Pricing\_Policies\_for\_Smart\_Products](https://www.researchgate.net/publication/220505613_An_Analysis_of_Usage-Based_Pricing_Policies_for_Smart_Products)  
50. Pricing Overview | Google Cloud, accessed November 6, 2025, [https://cloud.google.com/pricing](https://cloud.google.com/pricing)  
51. Analyze billing data and cost trends with Reports \- Google Cloud Documentation, accessed November 6, 2025, [https://docs.cloud.google.com/billing/docs/how-to/reports](https://docs.cloud.google.com/billing/docs/how-to/reports)  
52. Select the best pricing model \- Cost Optimization Pillar \- AWS Documentation, accessed November 6, 2025, [https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/select-the-best-pricing-model.html](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/select-the-best-pricing-model.html)  
53. Data Caps and Usage-Based Pricing \- International Center for Law & Economics, accessed November 6, 2025, [https://laweconcenter.org/resources/data-caps-and-usage-based-pricing/](https://laweconcenter.org/resources/data-caps-and-usage-based-pricing/)  
54. Usage based pricing or subscriptions? What's better? : r/startups \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/startups/comments/1aoba6t/usage\_based\_pricing\_or\_subscriptions\_whats\_better/](https://www.reddit.com/r/startups/comments/1aoba6t/usage_based_pricing_or_subscriptions_whats_better/)  
55. "Pay as You Go" or "All You Can Eat"? Pricing Methods ... \- SciSpace, accessed November 6, 2025, [https://scispace.com/pdf/pay-as-you-go-or-all-you-can-eat-pricing-methods-for-56kq9cys8y.pdf](https://scispace.com/pdf/pay-as-you-go-or-all-you-can-eat-pricing-methods-for-56kq9cys8y.pdf)  
56. Usage-Based vs. Outcome-Based Pricing for APIs | Moesif Blog, accessed November 6, 2025, [https://www.moesif.com/blog/api-monetization/api-strategy/Usage-Based-vs-Outcome-Based-Pricing-For-APIs/](https://www.moesif.com/blog/api-monetization/api-strategy/Usage-Based-vs-Outcome-Based-Pricing-For-APIs/)  
57. API Pricing Strategies: Segmentation and Personalized Models | Zuplo Learning Center, accessed November 6, 2025, [https://zuplo.com/learning-center/api-pricing-strategies](https://zuplo.com/learning-center/api-pricing-strategies)  
58. What is the pricing model for OpenAI? \- Milvus, accessed November 6, 2025, [https://milvus.io/ai-quick-reference/what-is-the-pricing-model-for-openai](https://milvus.io/ai-quick-reference/what-is-the-pricing-model-for-openai)  
59. The Economics of Large Language Models: Token Allocation ... \- arXiv, accessed November 6, 2025, [https://arxiv.org/pdf/2502.07736](https://arxiv.org/pdf/2502.07736)  
60. Usage-Based Pricing and Demand for Residential Broadband, accessed November 6, 2025, [https://cris.web.unc.edu/wp-content/uploads/sites/16302/2018/12/Nevo\_et\_al-2016-Econometrica.pdf](https://cris.web.unc.edu/wp-content/uploads/sites/16302/2018/12/Nevo_et_al-2016-Econometrica.pdf)  
61. The Flat-Rate Pricing Paradox: Conflicting Effects of “All-You-Can-Eat” Buffet Pricing, accessed November 6, 2025, [https://www.semanticscholar.org/paper/The-Flat-Rate-Pricing-Paradox%3A-Conflicting-Effects-Just-Wansink/e76280199afa63eca4ed177192c76d425d90e402](https://www.semanticscholar.org/paper/The-Flat-Rate-Pricing-Paradox%3A-Conflicting-Effects-Just-Wansink/e76280199afa63eca4ed177192c76d425d90e402)  
62. The Flat-Rate Pricing Paradox: Conflicting Effects of "“All-You-Can-Eat"” Buffet Pricing, accessed November 6, 2025, [https://ideas.repec.org/a/tpr/restat/v93y2011i1p193-200.html](https://ideas.repec.org/a/tpr/restat/v93y2011i1p193-200.html)  
63. (PDF) The fixed price paradox: Conflicting effects of “all-you-can-eat” pricing \- ResearchGate, accessed November 6, 2025, [https://www.researchgate.net/publication/228775952\_The\_fixed\_price\_paradox\_Conflicting\_effects\_of\_all-you-can-eat\_pricing](https://www.researchgate.net/publication/228775952_The_fixed_price_paradox_Conflicting_effects_of_all-you-can-eat_pricing)  
64. Nonlinear Pricing with Under-Utilization: A Theory of Multi-Part Tariffs \- MIT Economics, accessed November 6, 2025, [https://economics.mit.edu/sites/default/files/inline-files/NLPU\_web.pdf](https://economics.mit.edu/sites/default/files/inline-files/NLPU_web.pdf)  
65. (PDF) The Tragedy of the Digital Commons \- ResearchGate, accessed November 6, 2025, [https://www.researchgate.net/publication/2908264\_The\_Tragedy\_of\_the\_Digital\_Commons](https://www.researchgate.net/publication/2908264_The_Tragedy_of_the_Digital_Commons)  
66. Tragedy of the commons \- Wikipedia, accessed November 6, 2025, [https://en.wikipedia.org/wiki/Tragedy\_of\_the\_commons](https://en.wikipedia.org/wiki/Tragedy_of_the_commons)  
67. TRAGEDY OF THE DIGITAL COMMONS\* \- North Carolina Law Review, accessed November 6, 2025, [https://northcarolinalawreview.org/wp-content/uploads/sites/5/2023/06/Sharma\_FinalforPrint.pdf](https://northcarolinalawreview.org/wp-content/uploads/sites/5/2023/06/Sharma_FinalforPrint.pdf)  
68. OpenAI vs. Mistral \- Solvimon | All-in-one billing and monetization platform, accessed November 6, 2025, [https://www.solvimon.com/pricing-guides/openai-vs-mistral](https://www.solvimon.com/pricing-guides/openai-vs-mistral)  
69. The Great AI Price War: Navigating the LLM API Landscape in 2025 \- Skywork.ai, accessed November 6, 2025, [https://skywork.ai/skypage/en/The-Great-AI-Price-War-Navigating-the-LLM-API-Landscape-in-2025/1948645270783127552](https://skywork.ai/skypage/en/The-Great-AI-Price-War-Navigating-the-LLM-API-Landscape-in-2025/1948645270783127552)  
70. LLM API Pricing Comparison 2025: Complete Cost Analysis Guide \- Binadox, accessed November 6, 2025, [https://www.binadox.com/blog/llm-api-pricing-comparison-2025-complete-cost-analysis-guide/](https://www.binadox.com/blog/llm-api-pricing-comparison-2025-complete-cost-analysis-guide/)  
71. Anthropic API Pricing: Complete Guide and Cost Optimization ..., accessed November 6, 2025, [https://www.finout.io/blog/anthropic-api-pricing](https://www.finout.io/blog/anthropic-api-pricing)  
72. Mistral AI Solution Overview: Models, Pricing, and API \- Obot AI, accessed November 6, 2025, [https://obot.ai/resources/learning-center/mistral-ai/](https://obot.ai/resources/learning-center/mistral-ai/)  
73. Introducing Claude 3.5 Sonnet \- Anthropic, accessed November 6, 2025, [https://www.anthropic.com/news/claude-3-5-sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)  
74. GPT-4o mini: advancing cost-efficient intelligence \- OpenAI, accessed November 6, 2025, [https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/)  
75. LLM API Pricing Comparison (2025): OpenAI, Gemini, Claude | IntuitionLabs, accessed November 6, 2025, [https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025](https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025)  
76. API Pricing \- OpenAI, accessed November 6, 2025, [https://openai.com/api/pricing/](https://openai.com/api/pricing/)  
77. Mistral AI models | Generative AI on Vertex AI \- Google Cloud, accessed November 6, 2025, [https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/mistral](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/mistral)  
78. Google Gemini Pricing Guide: What You Need to Know, accessed November 6, 2025, [https://www.cloudeagle.ai/blogs/blogs-google-gemini-pricing-guide](https://www.cloudeagle.ai/blogs/blogs-google-gemini-pricing-guide)  
79. Comparative Evaluation of Cloud Pricing Models: Insights from Aws, Microsoft Azure, and GCP \- ResearchGate, accessed November 6, 2025, [https://www.researchgate.net/publication/392176452\_Comparative\_Evaluation\_of\_Cloud\_Pricing\_Models\_Insights\_from\_Aws\_Microsoft\_Azure\_and\_GCP](https://www.researchgate.net/publication/392176452_Comparative_Evaluation_of_Cloud_Pricing_Models_Insights_from_Aws_Microsoft_Azure_and_GCP)  
80. accessed November 6, 2025, [https://fiveable.me/cloud-computing-architecture/unit-9/cloud-pricing-models-pay-as-you-go-reserved-instances/study-guide/fMQkqgWtXs02iJbj\#:\~:text=Cloud%20pricing%20models%20are%20essential,commitments%2C%20ideal%20for%20stable%20workloads.](https://fiveable.me/cloud-computing-architecture/unit-9/cloud-pricing-models-pay-as-you-go-reserved-instances/study-guide/fMQkqgWtXs02iJbj#:~:text=Cloud%20pricing%20models%20are%20essential,commitments%2C%20ideal%20for%20stable%20workloads.)  
81. 9.1 Cloud pricing models (pay-as-you-go, reserved instances) \- Fiveable, accessed November 6, 2025, [https://fiveable.me/cloud-computing-architecture/unit-9/cloud-pricing-models-pay-as-you-go-reserved-instances/study-guide/fMQkqgWtXs02iJbj](https://fiveable.me/cloud-computing-architecture/unit-9/cloud-pricing-models-pay-as-you-go-reserved-instances/study-guide/fMQkqgWtXs02iJbj)  
82. What Is the Best Cloud Pricing Model? 2025 Guide \- Finout, accessed November 6, 2025, [https://www.finout.io/blog/what-is-the-best-cloud-pricing-model-2025-guide](https://www.finout.io/blog/what-is-the-best-cloud-pricing-model-2025-guide)  
83. AWS EC2 Instances Explained: Pricing, Types, Features, & Best Practices | CloudKeeper, accessed November 6, 2025, [https://www.cloudkeeper.com/insights/blog/aws-ec2-instances-explained-pricing-types-features-best-practices](https://www.cloudkeeper.com/insights/blog/aws-ec2-instances-explained-pricing-types-features-best-practices)  
84. Amazon EC2 Pricing, accessed November 6, 2025, [https://aws.amazon.com/ec2/pricing/](https://aws.amazon.com/ec2/pricing/)  
85. Best Cloud Pricing Models: Complete Guide \- Pelanor, accessed November 6, 2025, [https://www.pelanor.io/learning-center/learn-best-cloud-pricing-models-guide](https://www.pelanor.io/learning-center/learn-best-cloud-pricing-models-guide)  
86. Google Cloud Pricing: The Complete Guide \- NetApp, accessed November 6, 2025, [https://www.netapp.com/blog/gcp-cvo-blg-google-cloud-pricing-the-complete-guide/](https://www.netapp.com/blog/gcp-cvo-blg-google-cloud-pricing-the-complete-guide/)  
87. AWS EC2 Pricing Explained: How It Works and Optimization Tips ..., accessed November 6, 2025, [https://www.prosperops.com/blog/ec2-instances-cost/](https://www.prosperops.com/blog/ec2-instances-cost/)  
88. Cloud Cost: 4 Cost Models and 6 Cost Management Strategies \- Spot.io, accessed November 6, 2025, [https://spot.io/resources/cloud-cost/cloud-cost-models-management-strategies/](https://spot.io/resources/cloud-cost/cloud-cost-models-management-strategies/)  
89. Pricing Overview—How Azure Pricing Works | Microsoft Azure, accessed November 6, 2025, [https://azure.microsoft.com/en-us/pricing/details/defender-easm/](https://azure.microsoft.com/en-us/pricing/details/defender-easm/)  
90. Making Sense of Azure Costs: A Clear Pricing Explanation \- HAKIA.com, accessed November 6, 2025, [https://www.hakia.com/posts/making-sense-of-azure-costs-a-clear-pricing-explanation](https://www.hakia.com/posts/making-sense-of-azure-costs-a-clear-pricing-explanation)  
91. Pricing Strategies – Intermediate Microeconomics \- Oregon State University, accessed November 6, 2025, [https://open.oregonstate.education/intermediatemicroeconomics/chapter/module-16/](https://open.oregonstate.education/intermediatemicroeconomics/chapter/module-16/)  
92. Consumers' Insights into How Marketing Strategies Influence OTT Platform Preferences \- International Journal of Social Science Research and Review, accessed November 6, 2025, [https://ijssrr.com/journal/article/download/2801/1974/](https://ijssrr.com/journal/article/download/2801/1974/)  
93. Algorithmic Price Discrimination When Demand Is a Function of Both Preferences and (Mis)perceptions, accessed November 6, 2025, [https://lawreview.uchicago.edu/print-archive/algorithmic-price-discrimination-when-demand-function-both-preferences-and](https://lawreview.uchicago.edu/print-archive/algorithmic-price-discrimination-when-demand-function-both-preferences-and)  
94. (PDF) Digital Platforms and Algorithmic Pricing: Investigating Market Efficiency and Consumer Welfare in The Age of Big Data \- ResearchGate, accessed November 6, 2025, [https://www.researchgate.net/publication/393775463\_Digital\_Platforms\_and\_Algorithmic\_Pricing\_Investigating\_Market\_Efficiency\_and\_Consumer\_Welfare\_in\_The\_Age\_of\_Big\_Data](https://www.researchgate.net/publication/393775463_Digital_Platforms_and_Algorithmic_Pricing_Investigating_Market_Efficiency_and_Consumer_Welfare_in_The_Age_of_Big_Data)