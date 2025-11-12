## Don’t shoot the messenger: the (non-)ban on advertising based on special categories of data under the DSA Article 26

## I. Introduction

A person struggling with a gambling addiction is shown ads for instant loans while browsing a used car marketplace website. A teenager is ordering food with their parents and passes them a phone. Mid-order, the phone shows an ad for gay dating apps.

Profiling-based advertising can cause deep, systemic, society-wide harms; but it can cause deep, direct, tangible harm to real people.

Aware of this, the EU legislative has attempted to implement a fix which, in principle, sounds reasonable: Article 26(3) of the Digital Services Act forbids platforms from presenting advertisements based on profiling using special categories of personal data.

This solution works on paper. It does not, however, work in practice – because it is fundamentally misaligned with the technological realities of how the modern advertising ecosystem functions.

The car marketplace, the clothes sale platform, and the food delivery app have no means of knowing why this particular ad was shown – because the ecosystem is not designed, technologically and principally, in such a way. As ad publishers, they automatically display the winning bid based on auction price; they did not choose the target audience, cannot see why the advertiser bid, and have no technical means to verify whether prohibited profiling occurred before the advertisement loads.

The question this Article asks is straightforward: what must a platform do to comply with a prohibition it cannot observe?

Three approaches present themselves.

First, one might read Article 26(3) as imposing liability whenever an individual ad is displayed: platforms must verify the targeting basis of every advertisement before presentation, and any failure to prevent a prohibited advertisement – regardless of the platform’s ability to detect it – constitutes a violation. Second, one might argue that platforms must contractually require, and technically implement, disclosure mechanisms through which upstream actors communicate the targeting rationale for each impression, thereby enabling the platform to conduct per-impression verification and block prohibited advertisements in real time. Third, one might contend that platforms must implement a due diligence regime – obtaining sufficient guarantees from upstream actors, conducting periodic audits, and maintaining documentation – analogous to the standard imposed on data controllers under GDPR Article 28(1) when engaging processors, but adapted to the DSA’s distinct objectives and subject matter.

This Article will establish that the first two interpretations fail. Part III demonstrates why holding platforms liable for displaying individual illegal ads is technically impossible given programmatic advertising architecture. Part IV shows why mandatory disclosure collides with data minimisation principle, creates unwanted (and unenforceable) joint controllership, and collides with the essential principles underlying the GDPR and the DSA.

The third approach – a due diligence standard grounded by analogy in Article 28(1) GDPR – emerges as the only interpretation that aligns the DSA’s protective objective with proportionality and with the structural constraints of advertising technology systems. In direct terms, Part V of this Article argues for a due diligence standard: platforms must obtain guarantees from advertising partners, verify system design prevents special-category targeting, monitor for breach signals, and respond proportionately to violations.

This interpretation faces objections: that it provides insufficient protection, that it enables bad actor exploitation, that it imposes excessive burdens on small platforms, and that the solution lies instead in upstream regulation. They are valid. The Article will discuss them in turn in Part VI.

The main argument is simple: unintuitive as it might sound, the duty not to show advertising based on profiling of special categories of personal data must not be seen as an obligation of result – but as one of effort.

## II. The legal framework: how the DSA and the GDPR interact

Article 26 of the DSA imposes three obligations on providers of online platforms that present advertisements. First, platforms must ensure that recipients of the service can identify, for each advertisement, that it is an advertisement and can identify – in real time and in an easily accessible manner – the natural or legal person on whose behalf the advertisement is presented, as well as the person who paid for it.[^1] Second, platforms must present “meaningful information” about the main parameters used to determine which recipient is shown the advertisement and, where applicable, how to modify those parameters.[^2] Third – and it is this obligation with which this article is concerned – platforms must not present advertisements “based on profiling as defined in Article 4(4) [GDPR] using special categories of personal data referred to in Article 9(1) [GDPR].”[^3]

[^1]: Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 on a Single Market For Digital Services (Digital Services Act) [2022] OJ L277/1, art 26(1)(a)–(b).

[^2]: ibid art 26(1)(d).

[^3]: ibid art 26(3).

The definition of “profiling” is found in GDPR Article 4(4). It encompasses “any form of automated processing of personal data” used to evaluate personal aspects relating to a natural person, “in particular to analyse or predict aspects concerning that natural person’s performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements.”[^4] Special categories of personal data, in turn, are defined in GDPR Article 9(1) to include “personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership,” as well as genetic data, biometric data processed for the purpose of uniquely identifying a natural person, data concerning health, and data concerning a natural person’s sex life or sexual orientation.[^5]

[^4]: Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data (General Data Protection Regulation) [2016] OJ L119/1, art 4(4).

[^5]: ibid art 9(1).

The Court of Justice of the European Union (CJEU) has clarified that Article 9(1)’s scope is broad: in *Meta Platforms*, the Court held that inferences derived from processing can fall within Article 9(1), including when the controller “can, by processing potentially sensitive information, deduce [such] information” even without aiming to do so, and regardless of whether the inference is accurate.[^6] In *OT v. Lithuania*, the Court similarly held that indirect disclosure can engage Article 9(1).[^7] To that extent, targeting predicated on inferences about religion derived from location data – such as visits to places of worship – or about health from browsing behaviour can arguably fall within Article 9(1)’s scope, even if the advertiser did not directly collect those attributes as declared fields.

[^6]: Case C-252/21 Meta Platforms Ireland EU:C:2023:537, paras 75–77.

[^7]: Case C-184/20 OT v Vyriausioji tarnybinės etikos komisija EU:C:2022:601, paras 89–93.

The DSA prohibition, however, operates at the point of presentation.

This is straightforward: Recital 69 clarifies that platforms “should not present advertisements based on profiling … using special categories of personal data … including by using profiling categories based on those special categories.”[^8] This wording establishes that the prohibition extends not only to profiling that directly processes Article 9(1) data, but also to profiling categories that function as proxies for such data – again, unsurprisingly, in light of the CJEU case law.

[^8]: DSA (n 1) recital 69.

Recital 69 also underscores the policy rationale: targeting techniques “optimised to match [users’] interests and potentially appeal to their vulnerabilities … can have particularly serious negative effects,” contribute to the spread of disinformation, and enable discriminatory presentation of advertisements that affect equal treatment. This assessment is aligned with empirical research documenting discriminatory outcomes in advertisement delivery – including studies demonstrating gender and racial skew in housing and employment advertisement delivery even with neutral advertiser settings, as a result of algorithmic optimization for engagement.[^9]

[^9]: M. Ali, P. Sapiezynski, M. Bogen, A. Korolova, A. Mislove, A. Rieke, Discrimination through Optimization: How Facebook's Ad Delivery Can Lead to Biased Outcomes, Proc. ACM Hum. Comput. Interact. 3 (2019) Article 199. https://doi.org/10.1145/3359301; P. Sapiezynski, A. Ghosh, L. Kaplan, A. Rieke, A. Mislove, Algorithms That "Don't See Color": Measuring Biases in Lookalike and Special Ad Audiences, in: Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society, AIES '22, ACM, New York, 2022, pp. 419–427. https://doi.org/10.1145/3514094.3534135.

The DSA prohibition, rather clearly, does not displace the GDPR.

Recital 68 emphasizes that the transparency requirements in Article 26(1) and (2) are “without prejudice” to the GDPR, “in particular” the right to object under Article 21, the provisions on automated decision-making including profiling under Article 22, and the requirement to obtain consent for targeted advertising where applicable.[^10] Recital 69 similarly reaffirms that the prohibition in Article 26(3) is “without prejudice to the obligations under Regulation (EU) 2016/679 that apply to providers of online platforms and any other parties involved in the displaying of advertisements on online platforms.”[^11] Put differently, the GDPR governs whether and under what conditions profiling using special categories of personal data may lawfully occur; the DSA adds a display-layer constraint that applies regardless of whether the upstream processing satisfied GDPR requirements.

[^10]: DSA (n 1) recital 68.

[^11]: ibid recital 69.

The EDPB has embraced this interpretation.

In its draft Guidelines on the interplay between the DSA and the GDPR, the EDPB states that Article 26(3) “prohibits the presentation of any advertising based on profiling using such special categories of personal data by providers of online platforms to recipients of the service, regardless of whether this profiling is carried out by providers of online platforms or by others.”[^12] The EDPB further clarifies that the prohibition applies “even in situations where the provider of an online platform or another entity would rely on an appropriate legal basis under Article 6(1) GDPR and an appropriate derogation under Article 9(2) GDPR.”

[^12]: European Data Protection Board, Guidelines 3/2025 on the interplay between the Digital Services Act and the General Data Protection Regulation (adopted 12 September 2025) para 76.

In other words, a demand-side platform might lawfully process special category data under Article 9(2)(a) GDPR – explicit consent – and still not be permitted to have the resulting targeted advertisement presented on an online platform governed by the DSA. The legality of the processing and the permissibility of the presentation are distinct questions, governed by distinct regimes.

This division of places the platform – the entity that presents the advertisement – in a position where it must prevent presentation of advertisements selected on a prohibited basis, but where the selection itself occurs upstream and outside the platform’s processing operations. The platform’s obligation, therefore, is not to refrain from profiling (it may not be profiling at all), but to structure its advertising systems and relationships in such a way that prohibited advertisements are not presented to users.

The question is what that structuring entails – and it is to this question, through an examination of the technical environment in which platforms operate, that the analysis now turns.

## III. Why strict interpretation fails

A strict liability interpretation of Article 26(3) – under which platforms must verify the targeting basis of every advertisement before presentation, and under which any failure to prevent a prohibited advertisement constitutes a violation regardless of the platform’s ability to detect it – rests on an implicit premise: that platforms can, in fact, observe the targeting rationale applied by upstream actors.

This premise does not hold.

The architecture of programmatic advertising places the locus of targeting decisions outside the publisher’s control and outside the publisher’s observational capacity. To that extent, a strict verification standard demands what is, as a matter of system design, technically impossible.

Simply put: in open programmatic advertising, the decision about which specific creative should be served to which specific user is rarely made by the publisher.

This is a simple reflection of the reality of how a typical real-time bidding workflow on the web functions. When a user visits a publisher’s webpage, the page loads header bidding wrappers or calls a server-side supply-side platform (SSP). The SSP, in turn, sends bid requests to multiple demand-side platforms (DSPs) – often dozens of them, operating simultaneously.[^13] Each bid request contains information about the available advertising slot (its dimensions, its position on the page, contextual signals such as the page URL) and, depending on the parties’ arrangements and the jurisdiction’s consent framework, an identifier associated with the user (a cookie ID, a mobile advertising ID, or a hashed email address).[^14] Each DSP receives this bid request and evaluates it using proprietary data, auction logic, and campaign targeting parameters maintained by the DSP and its advertiser clients. The DSP determines whether any of its active campaigns wish to bid for this impression, applies its targeting rules – which may include matching the user identifier against audience segments, applying frequency caps, evaluating predicted engagement or conversion probability, and calculating bid price – and submits a bid response to the SSP.[^15] The SSP collects the bid responses, applies its own auction rules (which typically prioritize bid price, but may include deals, preferred buyers, or yield optimization algorithms), and returns a winning bid to the publisher’s advertisement server. The publisher’s advertisement server – or, in client-side implementations, a JavaScript tag running in the user’s browser – selects the winning bid and instructs the browser to load the corresponding creative.[^16]

[^13]: IAB Tech Lab, OpenRTB API Specification Version 2.6 (April 2022) https://iabtechlab.com/standards/openrtb/; Google, Authorized Buyers Real-Time Bidding Protocol (Google Developers Documentation, 2023) https://developers.google.com/authorized-buyers/rtb/.

[^14]: ibid; J.R. Mayer, J.C. Mitchell, Third-Party Web Tracking: Policy and Technology, in: Proceedings of the 2012 IEEE Symposium on Security and Privacy, IEEE Computer Society, 2012, pp. 413–427. https://doi.org/10.1109/SP.2012.47.

[^15]: IAB OpenRTB Specification (n 13) ss 3.2.1–3.2.13 (bid request object fields), ss 4.2.1–4.2.8 (bid response object fields).

[^16]: Prebid.org, How Prebid.js Works (Prebid Documentation, 2024) https://docs.prebid.org/; Google Ad Manager, About the Ad Exchange Dynamic Allocation (Google Ad Manager Help Center, 2024) https://support.google.com/admanager/.

The publisher’s selection, however, is based on auction outcomes, not on targeting rationale. The publisher sees which DSP won, the bid price, the advertiser domain, and the creative asset to be displayed; but the publisher does not see the audience segment identifiers, the profiling categories, or the data inputs that led the DSP to bid.[^17]

[^17]: M. Veale, F.J. Zuiderveen Borgesius, Adtech and Real-Time Bidding under European Data Protection Law, Ger. Law J. 23 (2022) 226–256. https://doi.org/10.1017/glj.2022.11.

In other words, the publisher observes the fact that DSP X bid 2.50 EUR for this impression and won the auction, but the publisher does not observe that DSP X bid because the user was classified into segment “likely_gay” derived from their browsing behavior. The targeting decision – the determination that this user should see this advertisement – was made upstream by the DSP. The publisher’s role was to select among competing bids based on price and priority, not to evaluate or approve the targeting basis.

This opacity is not accidental.

The architecture, in its systemic essence, reflects the commercial structure of programmatic advertising, in which DSPs and advertisers regard their targeting logic, their audience data, and their bidding strategies as proprietary and competitively sensitive.[^18] Bid requests and bid responses in the OpenRTB protocol – the dominant technical standard for real-time bidding – do not include a machine-readable “why this ad?” field.[^19] Audience segment identifiers, when included in bid requests, are typically opaque numeric codes whose meaning is known only to the DSP that assigned them; and bid responses specify price, creative URL, and advertiser identity, but not the profiling category or data sources used to select the user.[^20] To that extent, the information asymmetry between publishers and DSPs is structural, not incidental.

[^18]: J.M. Carrascosa, J. Riederer, V. Heorhiadi, S. Güera, S. Dacier, R. Pletka, To the Trash Bin! – On the Privacy Implications of Search Suggestions, in: M.J. Jacobsson, M. Rousseau, F. Cuppens (Eds.), ICT Systems Security and Privacy Protection, Lecture Notes in Computer Science, vol 8340, Springer, Berlin, Heidelberg, 2013, pp. 120–133. https://doi.org/10.1007/978-3-642-55415-5_10; D. Levin, K. Bhagwan, S. Savage, G.M. Voelker, Analyzing the Trade-Offs in Third-Party Data Sharing (Workshop on Technology and Consumer Protection, Washington DC, January 2020).

[^19]: IAB OpenRTB Specification (n 13) s 4.2 (bid response object specification).

[^20]: ibid s 3.2.13 (user.data object specification).

The problem becomes greater in server-side bidding, in-app advertising mediation, and connected television server-side ad insertion. In these environments, the auction occurs entirely on remote servers, outside the publisher’s direct control or observation. The publisher receives only the outcome: a creative URL and instructions to display it.[^21] Identifiers used by different parties may not align – one DSP may use a cookie ID, another a probabilistic device graph, a third a hashed email – making it difficult or impossible to join logs ex post for forensic analysis.[^22] Timestamp skew, differing retention policies, data volume, and confidentiality constraints further impede any attempt at cross-party reconciliation.[^23]

[^21]: Interactive Advertising Bureau, Server-Side Header Bidding: Programmatic Advertising Guide (IAB Tech Lab 2019) https://iabtechlab.com/; A. Soppera, M. Hildebrandt, Tracking and Profiling on the Open Web: A Technical and Legal Analysis, Int. Data Priv. Law 13 (2023) 45–62. https://doi.org/10.1093/idpl/ipac029.

[^22]: S. Englehardt, A. Narayanan, Online Tracking: A 1-Million-Site Measurement and Analysis, in: Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security, CCS '16, ACM, New York, 2016, pp. 1388–1401. https://doi.org/10.1145/2976749.2978313.

[^23]: M. Eslami, A. Rickman, K. Vaccaro, A. Aleyasen, A. Vuong, K. Karahalios, K. Hamilton, C. Sandvig, First I "Like" It, Then I Hide It: Folk Theories of Social Feeds, in: Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, CHI '16, ACM, New York, 2016, pp. 2371–2382. https://doi.org/10.1145/2858036.2858494.

Even if the publisher were contractually entitled to demand logs from every DSP that participated in auctions on its inventory – a significant practical and legal hurdle, as we will see – the publisher would face the task of matching impression-level records across systems that do not share a common identifier schema, that record events at different granularities, and that may retain data for different periods.

This informational asymmetry has been documented in earlier academic analysis of the GDPR’s transparency obligations under Articles 13 and 14. Veale and Zuiderveen Borgesius concluded, in their examination of real-time bidding, that publishers “cannot tell which RTB companies will collect or use data,” that publishers often do not know in advance which companies will receive bid stream data, and that publishers cannot predict auction winners.[^24] That literature addressed the difficulty of identifying data recipients and providing transparency to users, not the specific question of whether publishers can ascertain the targeting basis; but the underlying technical constraint is the same. The publisher is not the locus of decision-making in programmatic advertising; it is, rather, an infrastructure provider that facilitates auctions conducted by independent upstream actors using data and logic to which the publisher has no access.

[^24]: M. Veale, F.J. Zuiderveen Borgesius, Adtech and Real-Time Bidding under European Data Protection Law, Ger. Law J. 23 (2022) 232.

One might object that publishers could, in principle, demand technical changes to the OpenRTB protocol or to contractual arrangements with SSPs and DSPs, such that targeting rationale is disclosed on a per-impression basis. This objection anticipates the second interpretation – mandatory disclosure – which will be addressed in Part IV.

For present purposes, the point is narrower: under the current architecture of programmatic advertising, publishers cannot observe the targeting basis used by upstream actors. A strict liability interpretation of Article 26(3) – one that holds the publisher liable for presenting any advertisement based on profiling using special categories, regardless of the publisher’s ability to detect such profiling – therefore imposes liability for conduct that the publisher cannot observe, cannot prevent, and often cannot even verify *ex post*. Put differently, strict liability would hold publishers responsible for decisions made by independent third parties using proprietary data and systems over which the publisher exercises no control.

This is not a viable interpretation.

The principle of legal certainty, recognized as a general principle of EU law, requires that legal rules be clear, precise, and predictable in their application, such that individuals can foresee the legal consequences of their conduct.[^25] A rule that imposes liability for unobservable upstream conduct does not meet this standard.

[^25]: Case C-345/06 Gottfried Heinrich EU:C:2009:140, para 44; Case C-17/03 VEMW and Others EU:C:2005:362, paras 80–81.

Moreover, proportionality – another general principle of EU law – requires that measures imposed by EU legislation be appropriate and necessary to achieve the legitimate objectives pursued, and that they do not go beyond what is necessary to attain those objectives.[^26] Holding platforms strictly liable for targeting decisions made by independent upstream actors, when those decisions are not observable to the platform, is arguably neither appropriate nor necessary to achieve the DSA’s objective of preventing discriminatory and manipulative advertising.

[^26]: Case C-293/12 Digital Rights Ireland EU:C:2014:238, paras 46–47; Case C-311/18 Schrems II EU:C:2020:559, para 175.

The Court has already held as much under the GDPR: for the purposes of damages claims and administrative sanctions alike, there must be a finding of fault – because the very fundamental balance the GDPR seeks to protect would otherwise collaps.

To that extent, strict liability fails as a matter of both legal principle and technical feasibility.

The first interpretation must therefore be rejected.

## IV. Why mandatory disclosure fails

Having established that strict liability is technically impossible, one might argue for a second interpretation: that platforms must contractually require, and technically implement, disclosure mechanisms through which upstream actors communicate the targeting rationale for each impression.

Under this reading, Article 26(3) would mandate that publishers obtain, in real time or through logged data, information sufficient to verify whether each served advertisement was based on profiling using special categories of personal data. The publisher would then be obliged to block any advertisement for which such verification indicates a violation, or for which verification cannot be completed. This interpretation would, in principle, resolve the observability problem identified in Part III by requiring upstream actors to make their targeting decisions transparent to publishers on a per-impression basis.

This interpretation, however, fails on three grounds: it collides with the fundamental GDPR principles, it would transform publishers into co-controllers of upstream profiling operations in ways the DSA does not contemplate, and it exceeds what the text of Article 26(3) requires or supports.

The first difficulty concerns the GDPR principles – specifically, the one of data minimization and lawfulness of processing.

Article 5(1)(c) GDPR provides that personal data shall be “adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed.”[^27] The principle of data minimisation requires controllers to collect and process only the personal data that is strictly necessary to achieve the specified purpose.[^28] A mandatory disclosure regime, however, would require publishers to receive and process information about the profiling categories applied to individual users, the data sources used to construct those categories, and potentially the inferences drawn about users’ special category attributes. To that extent, the publisher would be processing personal data – and special category personal data or data closely linked to such categories at that – for the purpose of verifying compliance with Article 26(3). The wisdom of such solution is debatable.

[^27]: GDPR (n 4) art 5(1)(c).

[^28]: European Data Protection Board, Guidelines 4/2019 on Article 25 Data Protection by Design and by Default (adopted 20 October 2020) para 35; see also Case C-708/18 TK v Asociaţia de Proprietari bloc M5A-ScaraA EU:C:2019:1064, para 53.

The publisher’s purpose in operating an advertising-supported website is, generally, to display advertisements and generate revenue; it is not to profile users or to make targeting decisions.

Under a mandatory disclosure regime, the publisher would be required to ingest targeting data not because such data is necessary for the publisher’s own processing purposes, but solely to verify the compliance of third parties. Put differently, the publisher would become a joint controller of profiling data – data that it does not need and would not otherwise collect. This arguably conflicts with data minimisation: the publisher is being required to process personal data that is not necessary for its own purposes, but is necessary only to police the conduct of upstream actors.[^29]

[^29]: Article 29 Data Protection Working Party, Opinion 03/2013 on Purpose Limitation (WP 203, 2 April 2013) 24–28 (discussing necessity assessment under data minimisation).

One might respond that the processing is necessary for compliance with a legal obligation under Article 6(1)(c) GDPR – specifically, the obligation under Article 26(3) DSA.

However, this response assumes the very question at issue: whether Article 26(3) in fact requires such disclosure. If Article 26(3) can be interpreted in a manner that does not require ingestion of targeting data, then the processing is not necessary for compliance, and data minimisation principle thus stands against adopting the interpretation that mandates such ingestion. To that extent, the principle of data minimisation operates as an interpretive constraint: between two plausible readings of Article 26(3), one should prefer the reading that minimises the processing of personal data.[^30]

[^30]: cf Case C-293/12 Digital Rights Ireland (n 26) para 52 (proportionality requires that derogations and limitations to data protection "must apply only in so far as is strictly necessary").

The second difficulty concerns issues of controllership.

Under GDPR Article 4(7), a controller is “the natural or legal person … which, alone or jointly with others, determines the purposes and means of the processing of personal data.”[^31] Joint controllers, in turn, are controllers that “jointly determine the purposes and means of the processing.”[^32] The Court of Justice has clarified that joint controllership does not require that parties exercise equal influence over the processing or that they have access to the personal data; it is sufficient that each party determines, even partially, the purposes and means.[^33] In *Fashion ID*, the Court held that a website operator that embedded a Facebook “Like” button was a joint controller with Facebook with respect to the collection and transmission of visitor data to Facebook, even though the website operator did not have access to the data subsequently processed by Facebook.[^34]

[^31]: GDPR (n 4) art 4(7).

[^32]: ibid art 26(1).

[^33]: Case C-40/17 Fashion ID EU:C:2019:629, paras 68–74; Case C-210/16 Wirtschaftsakademie Schleswig-Holstein EU:C:2018:388, paras 28–38.

[^34]: Fashion ID (n 33) paras 74–80.

A mandatory disclosure regime would, arguably, make publishers joint controllers with DSPs for the profiling operations that precede advertisement display. If the publisher is required to receive, verify, and act upon targeting data – blocking advertisements based on profiling using special categories – then the publisher is determining, at least partially, the means by which the profiling is used. The publisher would be making decisions about which profiling-based advertisements may be displayed and which may not, based on criteria specified in Article 26(3). This goes beyond simply receiving the output of a profiling decision (the advertisement creative); it would entail receiving and processing the data inputs or decisional logic underlying that output. To that extent, the publisher would be exercising influence over the purposes and means of the profiling operation, thus engaging the criteria for joint controllership established in *Fashion ID* and *Wirtschaftsakademie*.[^35]

[^35]: Wirtschaftsakademie (n 33) para 38 (joint responsibility exists where multiple actors participate in determination of purposes and means, "even if to different degrees").

This outcome would have consequences beyond Article 26(3) compliance. Joint controllers are required under Article 26 GDPR to “determine their respective responsibilities for compliance with the obligations under this Regulation … in particular as regards the exercising of the rights of the data subject.”[^36] They must make the arrangement available to data subjects and designate a contact point.[^37] If publishers become joint controllers with every DSP whose targeting decisions they verify, the contractual and transparency obligations multiply across the entire supply chain, creating a web of joint controller arrangements that the DSA does not expressly require and that may be impractical to implement at the scale of open programmatic advertising.[^38] Moreover, joint controllership would expose publishers to liability under Article 82 GDPR for infringements of data protection rules committed by DSPs in the profiling operation, unless the publisher can prove that it is “in no way responsible for the event giving rise to the damage.”[^39] A regime that mandates disclosure, and thereby creates joint controllership, thus expands publishers’ legal exposure well beyond the confines of Article 26(3) DSA.

[^36]: GDPR (n 4) art 26(1).

[^37]: ibid art 26(2).

[^38]: European Data Protection Board, Guidelines 07/2020 on the Concepts of Controller and Processor in the GDPR (adopted 7 July 2021) paras 135–148 (discussing documentation and transparency obligations for joint controllers).

[^39]: GDPR (n 4) art 82(3); Case C-300/21 UI v Österreichische Post EU:C:2023:370, paras 39–44 (joint controllers are liable unless they prove lack of responsibility for the event giving rise to damage).

The third difficulty is textual.

Article 26(3) DSA prohibits platforms from presenting advertisements based on profiling using special categories of personal data; it does not explicitly require platforms to verify or obtain disclosure of the targeting basis. The text imposes a result-oriented obligation (do not present such advertisements) without specifying the means by which that obligation is to be achieved. One could read the text as implicitly requiring verification, on the theory that the only way to comply with a prohibition is to verify compliance.

However, this reading is not the only plausible one. The text could just as equally be read as requiring platforms to implement a due diligence regime that reduces the risk of non-compliance to a level that is reasonable and proportionate, without demanding absolute verification of every impression – as we explore further.

Recital 68 lends support to this alternative reading. It provides that the transparency obligations in Article 26(1) and (2) are “without prejudice” to the GDPR.[^40] While Recital 68 does not expressly mention Article 26(3), the same interpretive principle arguably applies: the DSA’s obligations should be construed in a manner that avoids conflict with the GDPR where possible. A mandatory disclosure regime creates tension with data minimisation and potentially transforms controllership roles in ways that generate conflict between the two instruments. An interpretation that avoids such conflict – by reading Article 26(3) as requiring due diligence rather than per-impression verification – is preferable as a matter of harmonious construction.[^41]

[^40]: DSA (n 1) recital 68.

[^41]: cf Case C-131/12 Google Spain EU:C:2014:317, para 81 (directive provisions must be interpreted in light of fundamental rights, avoiding conflict where possible); Case C-682/15 Berlioz Investment Fund EU:C:2017:373, para 50 (principle of consistent interpretation).

To that extent, the mandatory disclosure interpretation fails.

The reasons are straightforward: such disclosure requires publishers to process personal data that is not necessary for their own purposes, thereby arguably violating data minimization; it risks making publishers joint controllers of upstream profiling operations, with attendant legal obligations and liabilities that the DSA does not expressly contemplate; and it imposes a reading of Article 26(3) that, while textually possible, is neither required by the language nor supported by the broader regulatory context.

By elimination, the second interpretation must be rejected.

## VI. The standard of due diligence

Having rejected strict verification (Part III) and mandatory disclosure (Part IV), there remains a fourth interpretation of Article 26(3): that platforms must implement a due diligence regime through which they obtain sufficient guarantees from upstream actors, conduct periodic verification, and maintain documentation – analogous in function, though not in legal roles, to the standard imposed on data controllers under GDPR Article 28(1) when engaging processors.

This interpretation is the only one that aligns the DSA's protective objective with proportionality and with the structural constraints of advertising technology systems.

The analogy proceeds on function. The platform is not the controller of the advertiser's profiling operation, nor is the advertiser the platform's processor under the GDPR. The DSA does not allocate controller–processor roles, and this article does not argue that GDPR role concepts should be transposed into the DSA.[^42] The relevant parallel, rather, is the compliance challenge that arises when one actor's legal obligation in regards of processing of personal data depends on the behaviour of other actors in a chain it does not fully control. In other words, it is the way in which the standard is interpreted which is a source of interpretative inspiration – not the question of whether it is applicable.

[^42]: cf EDPB, Draft Guidelines 3/2025 (n 12) paras 3–4 (DSA and GDPR are complementary but distinct regimes).

Drawing such parallels is natural.

In GDPR terms, a controller who outsources processing must ensure, through due diligence and contract, that the processor's conduct satisfies the Regulation; the controller is accountable for its selection and oversight but is not subject to strict liability for every downstream act.[^43] In DSA terms, a platform that presents advertisements must ensure it does not display advertisements based on prohibited profiling, but it cannot control or observe every upstream targeting decision. A due diligence standard requiring the platform to select and engage only advertising partners that can provide sufficient guarantees that they disallow special-category-based profiling for campaigns delivered to the platform, to monitor that assurance over time, and to react to indications of breach, is a proportionate way to give effect to Article 26(3) in a multi-actor ecosystem.

[^43]: European Data Protection Board, Guidelines on the Application of Article 24 and Article 28 GDPR (adopted 7 June 2024) paras 9–11, 17–21 (controller's duty to select processors providing sufficient guarantees and to verify those guarantees continuously, but not strict liability for all processor acts).

Three features of the Article 28 model are instructive for the DSA context.

First, the EDPB states that the obligation to use only processors "providing sufficient guarantees" is continuous and that controllers "should, at appropriate intervals, verify the processor's guarantees."[^44] The extent of verification varies with risk, and guarantees may be shown through documentation, codes of conduct, certification, or audit reports; controllers may use questionnaires, request policies, or carry out on-site audits as appropriate.[^45] Transposed by analogy, providers of online platforms would be expected to perform extensive verification for higher-risk advertising relationships – such as large-scale behavioural campaigns delivered via opaque server-side systems – and to rely on less intensive measures where risk is lower, such as direct-sold contextual campaigns trafficked by the platform itself.

[^44]: ibid para 11.

[^45]: ibid paras 10–11, 17; EDPB, Guidelines 07/2020 (n 38) paras 94–99 (on "sufficient guarantees" and continuous verification).

Second, the EDPB emphasizes that processors have a duty to assist controllers and to make available "all information necessary to demonstrate compliance" with Article 28, including information about systems functioning, measures, data location, and sub-processors, with such information flows specified in contract.[^46] Analogically, advertising partners should be contractually obliged to attest and document the design of their advertisement-buying systems in a way that demonstrates that special-category targeting is prevented for campaigns purchased against the platform's inventory, and to cascade that obligation to any sub-partners engaged in delivery to that inventory.

[^46]: EDPB, Guidelines on Article 24 and Article 28 (n 43) paras 20–22; GDPR (n 4) art 28(3)(h).

Third, the EDPB underscores that the controller remains responsible for the decision to authorise sub-processors and for verifying the sufficiency of guarantees across the chain; the processor remains liable to the controller for the sub-processor's performance.[^47] In the advertising context, the platform's contract with a demand partner should condition participation on the partner's duty to flow down the prohibition on special-category targeting to any further parties that determine targeting for the platform's audiences, coupled with rights for the platform to object to high-risk subcontracting and to terminate for breach.

[^47]: EDPB, Guidelines on Article 24 and Article 28 (n 43) paras 23–27; GDPR (n 4) art 28(4).

On this reading, a provider of an online platform would discharge Article 26(3) by structuring its advertising relationships and internal processes around four elements.

First, onboarding due diligence would assess whether the prospective advertising partner's systems and policies make it technically and organisationally impossible to target campaigns to the platform's inventory on the basis of special categories or profiling categories that function as proxies for them.[^48] The platform would require documentation of system design, configurations, and controls that preclude such targeting for the platform's supply, together with attestations by a responsible officer. Where available, the platform could rely on independent certifications or codes of conduct recognised under the GDPR – Articles 40 and 42 – as relevant evidence, not because the GDPR framework directly governs the DSA duty but because such instruments can show general adequacy of compliance culture and systems.[^49] The platform would document its assessment and decision, bearing in mind that special-category profiling presents higher risks to the rights and freedoms of individuals, warranting more intensive verification in accordance with the risk-based principle articulated by the EDPB in its guidance on Article 24 GDPR and echoed in the CJEU's accountability jurisprudence.[^50]

[^48]: The term "technically and organisationally impossible" reflects the high standard implicit in Article 26(3)'s absolute prohibition; the platform should seek partners whose systems preclude such targeting by design, not merely partners who promise to avoid it.

[^49]: EDPB, Guidelines 07/2020 (n 38) paras 94–97; GDPR (n 4) art 28(5), arts 40, 42.

[^50]: EDPB, Guidelines on Article 24 and Article 28 (n 43) paras 14–19; Case C-340/21 Natsionalna agentsia za prihodite EU:C:2023:986, para 36 (measures must be "appropriate to the level of risk").

Second, the platform's contracts would impose express obligations on partners not to present, or cause to be presented, any advertisement based on profiling using special categories within Article 9(1) GDPR, including by using profiling categories based on those special categories, when purchasing against the platform's inventory. The contracts would require the partner to flow these obligations down to any further parties involved in targeting for the platform's supply, and to make available information necessary for the platform to demonstrate compliance, including system descriptions, relevant policies, and changes thereto.[^51] The contract would set out audit and inspection rights limited to what is necessary to verify the guarantees, with appropriate confidentiality protections that are compatible with trade secrets law and data protection. Where the partner relies on general authorisation to engage sub-partners, the platform would specify criteria guiding such engagement – such as technical and organisational guarantees, expertise, reliability, and resources – and reserve the right to object to specific sub-partners that do not meet those criteria.[^52] This contractual architecture mirrors the processor–sub-processor structure under Article 28(2) and (4) GDPR, adapted to the DSA's presentation-layer focus.

[^51]: This mirrors the processor's obligation under Article 28(3)(h) GDPR to "make available to the controller all information necessary to demonstrate compliance with the obligations laid down in this Article."

[^52]: EDPB, Guidelines on Article 24 and Article 28 (n 43) paras 23–28; EDPB, Guidelines 07/2020 (n 38) paras 152–159.

Third, ongoing monitoring would occur at intervals that reflect the risk profile, size of spend, and technical architecture of the advertising relationship. The platform would establish reporting channels to detect complaints, regulator inquiries, or civil society findings suggesting that a partner enabled special-category targeting for the platform's inventory. Where the platform can instrument its advertisement servers to detect anomalies consistent with discriminatory delivery – while respecting data minimisation and avoiding processing special categories itself – it would do so at an aggregate level, not by ingesting per-impression targeting rationale.[^53] The platform would periodically review partner attestations and independent audit reports, check for changes in laws and technical standards, and adjust contract terms and controls as necessary. If information appears incomplete or inaccurate, the platform would request clarification and, where justified by risk, conduct targeted audits. All such measures would be documented in accordance with the accountability logic the EDPB describes for Articles 24 and 28 GDPR, which requires controllers to be able to demonstrate that processing is performed in accordance with the Regulation and that appropriate measures have been implemented.[^54]

[^53]: Aggregate monitoring might include, for example, detecting patterns in which advertisements for health products are systematically delivered to users who have not declared health interests, suggesting possible upstream profiling on health data. However, such monitoring must not entail processing individuals' special category data.

[^54]: EDPB, Guidelines on Article 24 and Article 28 (n 43) paras 19–22, 28; Case C-340/21 Natsionalna agentsia (n 50) para 52 (controller must be able to demonstrate appropriate measures).

Put differently, the platform's obligation is not to prevent every possible violation through technical means that do not exist; it is to implement and maintain a system of organisational safeguards designed to prevent violations, to detect signals of non-compliance, and to respond proportionately.

Fourth, when guarantees fail – when there is credible evidence that a partner served on the platform an advertisement based on prohibited profiling – the platform would apply a graduated response. Upon credible evidence of such a violation, the platform would promptly suspend the partner's ability to buy against the platform's inventory pending investigation. The platform would notify competent authorities as appropriate: Digital Services Coordinators for DSA matters, and, where there are indications of unlawful processing, data protection authorities.[^55] The platform would analyse the incident with the partner, require remediation steps such as system configuration changes or additional safeguards, and, where the breach reflects systemic deficiencies or bad faith, terminate the relationship. The platform would maintain evidence of its response for potential oversight and enforcement proceedings. Such a response framework is consistent with the EDPB's view that in high-risk processing scenarios controllers should increase their verification of guarantees and that processors must assist with documentation and information.[^56] It reflects the principle, recognised in the CJEU's case law on GDPR accountability, that the occurrence of a breach does not automatically establish that the controller's measures were inappropriate, but does trigger scrutiny of those measures and the controller's demonstration of appropriateness.[^57]

[^55]: On the interaction between DSCs and DPAs, see EDPB, Draft Guidelines 3/2025 (n 12) paras 3–4; G. Zanfir-Fortuna, O. Korovilas, Between the DSA and the GDPR: Ten Points of Interaction (Future of Privacy Forum, 2023) (mapping coordination needs between DSCs and DPAs).

[^56]: EDPB, Guidelines on Article 24 and Article 28 (n 43) paras 17–19, 29.

[^57]: Case C-340/21 Natsionalna agentsia (n 50) paras 30, 52 (occurrence of breach does not establish per se that measures were inappropriate; controller must demonstrate appropriateness).

The standard articulated here is not an argument that platforms may process special categories of personal data to police their partners, nor that platforms must obtain targeting parameters per impression. To that extent, it avoids the data minimisation collision identified in Part IV: it asks platforms to know their partners' systems, not their users' inferred traits. It centres organisational controls around partner guarantees, system design attestations, and independent evidence, rather than per-impression data ingestion. The CJEU has clarified, in the context of GDPR Article 24, that controllers bear the burden of demonstrating that they have implemented appropriate technical and organisational measures to ensure and to be able to show that processing is performed in accordance with the Regulation.[^58] In *Natsionalna agentsia za prihodite*, the Court held that the obligation to implement appropriate measures under Articles 24 and 32 must be assessed "in a concrete manner," with the controller bearing the burden of proving that measures ensured appropriate security, but without an irrebuttable presumption of inadequacy from the mere occurrence of a breach.[^59] In *BL v MediaMarktSaturn*, the Court reiterated that Article 24 lays down a general obligation to implement appropriate measures and to be able to demonstrate this, and that the burden of proof rests with the controller in compensation actions.[^60] While these rulings concern GDPR duties, they illustrate a general EU law approach to organisational duties: the obligation is to implement and evidence measures commensurate with risk, not to ensure an error-free outcome in complex systems.

[^58]: Case C-687/21 BL v MediaMarktSaturn Hagen-Iserlohn GmbH EU:C:2024:72, paras 36, 38, 42.

[^59]: Case C-340/21 Natsionalna agentsia (n 50) paras 25, 30, 36, 52.

[^60]: Case C-687/21 BL v MediaMarktSaturn (n 58) para 42.

Taking this a step further, the due diligence standard shifts the enforcement locus from unknowable targeting decisions – which occur upstream in proprietary systems using data to which the platform has no access – to verifiable organisational practices. A Digital Services Coordinator examining a platform's compliance with Article 26(3) can focus on whether the platform has instituted reasonable due diligence measures: partner selection criteria, contracts prohibiting special-category targeting for the platform's supply, monitoring procedures, documentation, and incident response. Where there is evidence that an advertiser or demand-side platform engaged in profiling using Article 9(1) data, the data protection authority can investigate and sanction the processing entity under the GDPR. This division of labour reduces incentives for platforms to over-collect targeting details to protect themselves from DSA liability, allows data protection authorities to deploy their expertise on processing, and aligns with the EDPB's view that the DSA's advertising provisions "complement" the GDPR and that enforcement will often engage both Digital Services Coordinators and data protection authorities.[^61] It also reduces the risk of *ne bis in idem*, as sanctions would target different legal interests: the platform's presentation duty under the DSA and the processor's data protection duties under the GDPR.

[^61]: EDPB, Draft Guidelines 3/2025 (n 12) paras 3–4; Zanfir-Fortuna, Korovilas (n 55).

## VII. An imperfect balance

Construing Article 26 in this manner is, as mentioned at the outset, not intuitive: legitimate concerns can (and must) be raised.

The first is that a due diligence standard provides insufficient protection because it tolerates some violations so long as the platform has exercised reasonable diligence – making it possible, in effect, to find them non-liable in cases as devastating as discussed in the Introduction. The second is that bad actors will exploit the standard by providing false assurances while conducting prohibited profiling – as one has no means to truly verify what happens behind the scenes. The third is that the due diligence regime imposes excessive burdens, particularly on small platforms that lack the resources to conduct extensive verification.

The sufficiency objection rests on an implicit comparison with a strict liability regime under which platforms would be liable for any occurrence of prohibited targeting, regardless of the platform's ability to detect or prevent it.

However, that comparison is not sound.

As demonstrated in Part III, strict liability is technically impossible in programmatic advertising environments where targeting decisions occur upstream in systems the platform cannot observe. The relevant comparison, therefore, is not between due diligence and strict liability, but between due diligence and the alternative outcomes that would follow from adopting an unworkable standard. If Article 26(3) were construed to impose strict liability, platforms would face a choice between exiting open programmatic advertising entirely – thereby concentrating advertising revenue in vertically integrated "walled gardens" that control both targeting and presentation – or implementing invasive disclosure mandates that would collide with data protection principles and expand joint controllership, as explained in Part IV.[^62] Neither outcome serves the DSA's protective objective. A due diligence standard, by contrast, preserves space for open advertising supply chains while creating enforceable expectations about partner selection, oversight, documentation, and responsiveness to breach. To that extent, the objection simply conflates the absence of absolute guarantee with the absence of effective protection.

[^62]: See Part IV above; cf Ad Targeting Transparency: An Operational Analysis of Publisher Observability, Control, and Evidence (technical white paper, 2025) 2–3 (adverse economics and consolidation pressures when liability is placed on publishers without observability).

Just as importantly, proportionality supports calibration rather than maximalism. The DSA is subject to the principle of proportionality, which requires that measures imposed by EU legislation be appropriate and necessary to achieve the legitimate objectives pursued, and that they do not go beyond what is necessary to attain those objectives.[^63] A platform that has taken reasonable, risk-commensurate steps to prevent the presentation of prohibited advertisements, documented its selection and monitoring of partners, and responded effectively to incidents has aligned its conduct with the DSA's protective objective within the limits that the technical architecture permits. The contrary approach would demand that platforms do what the ecosystem does not allow them to do without invasive changes that the DSA does not mandate.

[^63]: Case C-293/12 Digital Rights Ireland (n 26) paras 46–47; Case C-311/18 Schrems II (n 26) para 175.

The bad actor objection – that advertisers or demand-side platforms will provide false assurances – identifies a real risk but does not undermine the due diligence framework: that risk exists under any compliance regime short of an outright ban on third-party programmatic advertising. The appropriate response is to build into the due diligence framework both ex ante partner selection criteria that favour firms with credible compliance records, independent attestations, and recognised certifications, and *ex post* monitoring with real consequences for breach, including suspension, termination, and reporting to competent authorities.[^64] The EDPB's guidance on Article 28 GDPR contemplates reliance on approved codes of conduct or certifications as one means to demonstrate sufficient guarantees.[^65] In the DSA sphere, the development of advertising codes under Article 45 and of industry standards under Article 44 can help create verifiable compliance signals that platforms can reasonably trust absent contrary evidence.[^66] Where a platform is presented with credible indications of misrepresentation – through user complaints, regulator inquiries, investigative journalism, or civil society research – it must escalate its verification and, where the partner cannot provide satisfactory evidence that prohibited targeting has been prevented, suspend or terminate the relationship. Failure to respond to such signals would fall short of reasonable diligence and would constitute a violation of Article 26(3). However, in the absence of such signals, a platform that has conducted appropriate onboarding due diligence, obtained contractual guarantees with flow-down obligations, and implemented periodic monitoring has discharged its obligation.

[^64]: On incident response as an element of accountability, see EDPB, Guidelines on Article 24 and Article 28 (n 43) paras 28–29; Case C-340/21 Natsionalna agentsia (n 50) para 52.

[^65]: GDPR (n 4) art 28(5); EDPB, Guidelines 07/2020 (n 38) paras 94–97.

[^66]: DSA (n 1) arts 44–45; see also recital 68 ("might follow standards pursuant to Article 44").

The burden objection is legitimate as well, particularly with respect to small and micro platforms that display only a limited volume of third-party advertisements and lack the resources to conduct extensive verification. However, the answer lies in calibration. The EDPB's interpretation of Articles 24 and 28 GDPR reads risk into the determination of "appropriate measures," and makes the extent of verification vary with the risk presented by the processing operation.[^67]

[^67]: EDPB, Guidelines on Article 24 and Article 28 (n 43) paras 12–19, 29; Case C-340/21 Natsionalna agentsia (n 50) para 36 (measures must be "appropriate to the level of risk").

The same logic applies by analogy to Article 26(3). A small publisher that displays advertisements exclusively through a single well-documented advertising network, and that has adopted the network's attestations regarding the prohibition on special-category targeting, may satisfy Article 26(3) with proportionately modest onboarding checks and periodic review of the network's policies and any available audit reports. A very large online platform with complex integrations across dozens of demand-side platforms, by contrast, bears heavier obligations because of the scale and risk of potential harms, and because it has the resources to verify guarantees more extensively through detailed questionnaires, independent audits, and technical instrumentation.[^68] The DSA's framework for differentiated supervision of very large online platforms and search engines, which imposes heightened risk assessment and mitigation obligations on entities that reach at least 45 million average monthly active recipients in the Union, is consistent with this gradient.[^69] To that extent, the due diligence standard does not impose a one-size-fits-all burden; it articulates a principle – sufficient guarantees proportionate to risk – that scales with the nature, scope, and context of the platform's advertising operations.

[^68]: The differentiation reflects both the magnitude of potential harm (more users affected by violations) and the availability of resources to implement comprehensive due diligence.

[^69]: DSA (n 1) arts 33–44 (very large online platforms and search engines: risk assessments, mitigation obligations, independent audits); art 33(1) (threshold).

## VIII. Conclusion

Article 26(3) DSA prohibits providers of online platforms from presenting advertisements based on profiling using special categories of personal data. The provision operates at the presentation layer. However, as this Article has shown, the programmatic advertising ecosystem places targeting decisions with upstream actors whose logic platforms cannot observe. This structural asymmetry creates a compliance gap.

Three interpretations fail. Strict verification demands technical impossibility: platforms cannot observe upstream targeting decisions in real-time bidding and server-side architectures. Mandatory disclosure collides with data minimisation, risks transforming platforms into co-controllers of upstream profiling operations, and exceeds what Article 26(3) textually requires. Upstream regulation alone does not resolve the DSA's allocation of a presentation-layer duty to platforms.

By elimination, a due diligence standard emerges as the interpretation that aligns the DSA's protective objective with proportionality and feasibility. Drawing by analogy on GDPR Article 28(1)'s "sufficient guarantees" framework – without importing controller-processor roles into the DSA – platforms must select advertising partners that credibly preclude special-category targeting for the platform's inventory, impose contractual flow-down obligations, monitor guarantees proportionate to risk, document their measures, and respond decisively to indications of breach.

This standard does not eliminate all violations; it makes prevention and response auditable and enforceable in systems where absolute verification is neither technically possible nor compatible with data minimisation. The obligation is to implement and evidence measures commensurate with risk, not to guarantee an error-free outcome in multi-actor ecosystems the platform does not control.

The teenager, the person with diabetes, and the individual with gambling addiction will still encounter advertisements. Some of those advertisements may still be targeted in ways that feel intrusive or inappropriate – or that might be illegal. But a workable compliance standard – one that platforms can implement, regulators can enforce, and courts can apply with legal certainty – creates accountability where currently there is none. The obligation under Article 26(3) cannot be to prevent every possible violation through technical means that do not exist: it must be to implement and maintain organisational systems designed to prevent violations, to detect signals of non-compliance, and to respond proportionately.

Therefore, the duty not to present advertisements based on profiling of special categories must be interpreted as simply the one of showing due care. Such reading does not weaken the protection the Digital Services Act affords – instead, it makes that protection enforceable in the real world.

