  
# **Private International Law and the Digital Services Act: A Framework for Private Compensation Claims**

## **Executive Summary**

The Regulation (EU) 2022/2065, known as the Digital Services Act (DSA), represents a watershed moment in the governance of the digital ecosystem. While much scholarly and professional attention has focused on its regulatory architecture—specifically the compliance obligations for Very Large Online Platforms (VLOPs) and the supervisory powers of the European Commission—a dormant giant lies within Article 54: the right to private compensation. This provision fundamentally alters the liability landscape for intermediaries, transforming regulatory non-compliance into a cause of action for civil damages.  
However, the DSA is not a self-contained civil code. It operates within the complex, pre-existing lattice of European private international law (PIL). The effectiveness of Article 54 is contingent upon the interaction between the DSA’s substantive rules and the procedural mechanisms of Regulation (EU) No 1215/2012 (Brussels I bis) and Regulation (EC) No 864/2007 (Rome II). This report provides an exhaustive, expert-level analysis of this interplay. It argues that while the DSA achieves regulatory harmonization, the private enforcement mechanism remains deeply fragmented. The "place of damage" rule in Rome II threatens to partition the Digital Single Market into twenty-seven distinct liability zones for compensation claims, creating a complex matrix of risks for providers and strategic hurdles for claimants.  
Furthermore, the report identifies a "collision course" between the DSA and parallel liability regimes—specifically the General Data Protection Regulation (GDPR), the revised Product Liability Directive (PLD), and the forthcoming AI Act. Navigating these overlapping jurisdictions requires a nuanced understanding of how statutory duties, strict liability, and fault-based torts interact in a cross-border context.  
---

## **1\. The Substantive Right to Compensation: Anatomy of Article 54 DSA**

### **1.1. Legal Characterization: A Hybrid Statutory Tort**

Article 54 of the DSA states: *"Recipients of the service shall have the right to seek, in accordance with Union and national law, compensation from providers of intermediary services, in respect of any damage or loss suffered due to an infringement by those providers of their obligations under this Regulation."*.1  
To understand the PIL implications, we must first characterize the legal nature of this right. It is not a "tort" in the traditional common law sense, nor a simple "delict" in the civil law tradition, but rather a *hybrid statutory remedy*. It is a right derived from EU regulation but implemented through national procedural law.  
The phrasing "in accordance with Union and national law" introduces a vertical choice-of-law complexity. The *existence* of the right is a matter of EU law (and thus autonomous interpretation by the CJEU), but the *modalities* of the remedy—quantification of damages, rules on joint and several liability, and limitation periods—are left to national law.2 This effectively bifurcates the cause of action:

1. **The Liability Trigger (EU Law):** The breach of the DSA obligation (e.g., failure to suspend a repeat infringer under Article 23\) is determined solely by the Regulation.  
2. **The Remedial Mechanism (National Law):** The calculation of the financial loss resulting from that failure is determined by the *lex causae* (the law applicable to the tort).

This structure mirrors the approach taken in data protection law under Article 82 GDPR, but with a critical difference: the DSA regulates conduct (due diligence) rather than a fundamental right (data protection) per se. Consequently, claimants must prove a specific breach of a *conduct obligation*, not just an adverse outcome. This suggests a fault-based regime where the "infringement" constitutes the fault (negligence or intent).

### **1.2. The Personal Scope: "Recipients" vs. Third Parties**

A rigorous textual analysis of Article 54 reveals a deliberate limitation of standing. Compensation is available to "recipients of the service." Defined in Article 3(b), a recipient is "any natural or legal person who uses an intermediary service, in particular for the purposes of seeking information or making it accessible." This creates a sharp dichotomy in the liability landscape:

* **The "Insider" Claimant (The Recipient):** Users, content creators, and business traders have standing under Article 54\. Their claims are "DSA claims" proper.  
* **The "Outsider" Claimant (The Third Party):** Individuals who are not users of the platform but are harmed by content on it (e.g., a non-user defamed by a tweet, or a copyright holder whose work is pirated on a platform they do not use) do *not* have standing under Article 54\.3

This distinction has profound PIL implications. An "insider" claimant can rely on the specific breach of DSA obligations (e.g., faulty notice-and-action mechanisms) as the basis for their claim. An "outsider" must rely on general national tort law (negligence, defamation), where the DSA obligations might only serve as a standard of care (*Reflexwirkung*). Thus, a single harmful event—e.g., the viral spread of a deepfake—could trigger two distinct PIL analyses: one for the user (contractual/statutory nexus) and one for the non-user (pure tort).

### **1.3. Typology of Compensable Harms**

The DSA does not explicitly define "damage or loss," but the context of EU consumer and digital law suggests a broad interpretation is mandated to ensure "effective" enforcement.

#### **1.3.1. Material and Non-Material Damage**

Drawing on the CJEU's jurisprudence in *UI v Österreichische Post AG* (C-300/21) regarding the GDPR, arguably no "threshold of seriousness" should apply to DSA claims.4

* **Material:** Direct financial loss. Example: A trader on an online marketplace loses revenue because the platform failed to verify the traceability of a competitor selling counterfeit goods (breach of Article 30).  
* **Non-Material:** Distress, reputational harm, or anxiety. Example: A user is harassed due to the platform's failure to enforce its terms and conditions regarding hate speech. The CJEU has confirmed that mere infringement is insufficient; actual harm must be proven, but "loss of control" or "anxiety" can constitute compensable harm.4

#### **1.3.2. The Problem of Pure Economic Loss**

The most commercially significant claims under the DSA will likely involve "pure economic loss"—financial harm unaccompanied by physical injury or property damage.

* **Scenario:** An algorithm update by a VLOP acts as a "shadowban," reducing an influencer's reach by 90%. The influencer suffers no property damage but massive income loss.  
* **Legal Friction:** National laws vary wildly on this. German law (§ 823 I BGB) is restrictive regarding pure economic loss in tort, often requiring a breach of a specific "protective law" (*Schutzgesetz*). Article 54 DSA aims to function as such a protective law. Conversely, French law (*dommage*) is more permissive.  
* **PIL Consequence:** Because Rome II (Article 15(c)) dictates that the applicable national law governs the "existence and nature" of damage, the recoverability of pure economic loss will depend entirely on the conflict of laws outcome. A claimant in Paris might recover, while a claimant in Berlin, on identical facts, might struggle unless the court accepts Article 54 DSA as a *Schutzgesetz*.6

### **1.4. Causality and Recital 122**

Recital 122 provides a critical interpretative guide: compensation should be for damage suffered "due to" an infringement. It clarifies that providers should be liable for damages "caused by" the infringement of their due diligence obligations.2  
This introduces a "but-for" causation requirement.

* *Example:* If a platform fails to provide a Statement of Reasons (Article 17\) for a content takedown, but the content was arguably illegal anyway, did the *failure to provide reasons* cause the damage? Or was the damage caused by the *takedown itself* (which might have been justified)?  
* Claimants will need to demonstrate that *compliance* with the DSA (e.g., a proper risk assessment) would have prevented the harm. This is a complex evidentiary hurdle, especially regarding systemic risks (Articles 34-35), where the causal link between a generic risk assessment failure and specific individual harm is tenuous.

---

## **2\. Judicial Competence: Navigating Brussels I bis in the Digital Age**

The DSA does not contain a *lex specialis* for jurisdiction. Therefore, Regulation (EU) No 1215/2012 (Brussels I bis) provides the exclusive framework for determining which Member State's courts are competent.8 The digital nature of the DSA creates specific friction points with the territorial logic of Brussels I bis.

### **2.1. General Jurisdiction: The "Ireland Problem" (Article 4\)**

The cornerstone of Brussels I bis is Article 4: defendants should be sued in the Member State of their domicile. For the digital ecosystem, this leads to a massive centralization of litigation.

* **The Reality:** Meta, Google, TikTok, Twitter (X), and Apple all have their European headquarters in Ireland (or Luxembourg for Amazon).  
* **The Consequence:** Without special jurisdiction grounds, the Irish courts would be the sole venue for private enforcement of the DSA against VLOPs. This creates a bottleneck and potentially prohibitive access-to-justice barriers for a claimant in Bulgaria or Portugal. While Article 4 provides a certain forum, it is rarely the strategic choice for claimants unless they are seeking to consolidate EU-wide claims in a single venue.10

### **2.2. Special Jurisdiction in Tort: The "Mosaic" of Article 7(2)**

Article 7(2) Brussels I bis allows a claimant to sue in "the courts for the place where the harmful event occurred." The CJEU's jurisprudence has bifurcated this into (a) the place of the causal event and (b) the place where the damage occurred.

#### **2.2.1. Locus Delicti Commissi (Place of the Event)**

For DSA claims, the "event giving rise to the damage" is the breach of the obligation.

* **Algorithmic Decisions:** If the breach is a failure in the design of a recommender system (Article 27), the event occurs where the engineering and policy decisions were made—typically the platform's HQ. This leads back to the defendant's domicile (Ireland), offering no new venue.  
* **Content Moderation:** If the breach is a failure to act on a notice (Article 16), the omission occurs where the team responsible for moderation sits. While this might be outsourced, legally, the decision is attributed to the controller's establishment.

#### **2.2.2. Locus Damni (Place of Damage) and the Mosaic Theory**

The "place of damage" is the claimant's primary gateway to local courts. However, the CJEU's "mosaic theory" (developed in *Shevill* C-68/93 and *eDate* C-509/09) creates a complex landscape for online harms.11

* **Personality Rights (Natural Persons):** If a user suffers reputational harm or privacy invasion (e.g., doxxing facilitated by a platform breach), they can sue in the courts of their "centre of main interests" (COMI)—usually their habitual residence—for the *entirety* of the damage worldwide.12 This is the "gold standard" for individual claimants under the DSA.  
* **Corporate Claimants:** In *Bolagsupplysningen* (C-194/16), the CJEU denied legal persons (corporations) the right to use the "centre of interests" ground for claiming full damages for personality rights infringements. A company suing for reputational harm can primarily sue at the place of the event (Ireland) or in each Member State where content was distributed (but only for damage in *that* state—the "mosaic").  
  * *Insight:* This severely disadvantages SMEs. An Italian SME harmed by a VLOP's systemic failure cannot easily sue for *full* EU-wide damages in Italy. They are forced to sue in Ireland or fragment their claim across 27 courts.

#### **2.2.3. Pure Economic Loss and the "Holterman" Effect**

For claims involving purely financial loss (e.g., an app developer delisted from an app store), the location of damage is contested.

* **The Tibor Trans / Volkswagen Jurisprudence:** In *Volkswagen* (C-343/19), the CJEU located the damage for purchasers of defective cars where the car was purchased.  
* **Application to DSA:** For digital services, this suggests the damage occurs where the service is *supplied* or *accessed*. If a French trader uses a marketplace to sell to Germans, and the account is suspended, is the damage in France (trader's bank account/operations) or Germany (lost sales)?  
* The CJEU in *Marinari* (C-364/93) ruled that the place where assets are held is not sufficient if the initial damage occurred elsewhere. However, for digital services, the "initial damage" (loss of digital visibility) arguably occurs on the user's screen/interface in their home state.14

### **2.3. The Consumer Protective Regime (Articles 17-19)**

The most potent tool for individual DSA claimants is the consumer jurisdiction rules.

* **Mechanism:** A consumer can sue the "other party to a contract" in the courts of the consumer's domicile (Article 18(1)).  
* **Condition:** The professional must "direct" activities to that Member State (Article 17(1)(c)). VLOPs, by definition, direct activities to all EU states.  
* **Scope:** This applies to "matters relating to a contract." While Article 54 DSA is a statutory claim, the relationship between a user and a platform is fundamentally contractual (Terms of Service).  
* **Strategic Advantage:** A user suing under Art. 54 can likely frame the breach of the DSA as a breach of the implied contractual term to provide a lawful service. This creates a "parasitic" tort jurisdiction attached to the consumer contract jurisdiction, allowing the user to sue at home for *all* claims.16  
* **Limit:** This only applies to B2C. "Prosumers" (influencers, Uber drivers) often fail the "consumer" test if the use is predominantly professional, pushing them back into the unfriendly Article 7(2) regime.

### **2.4. Joinder and the "Anchor Defendant" (Article 8(1))**

Article 8(1) Brussels I bis permits suing multiple defendants in the domicile of one of them (the anchor), provided claims are "closely connected."

* **DSA Application:** A user might wish to sue:  
  1. **Defendant A:** The Content Creator (domiciled in Germany) for defamation.  
  2. **Defendant B:** The Platform (domiciled in Ireland) for failure to remove the defamation (DSA breach).  
* **The Strategy:** The user could sue both in Ireland (Platform's domicile) or Germany (Creator's domicile).  
* **The Obstacle:** The CJEU in *Reisch Montage* (C-103/05) requires a risk of irreconcilable judgments. Since the liability of the creator (primary tortfeasor) and the platform (negligence in intermediation) rest on different legal bases, courts might find the connection insufficient for joinder in the *claimant's* home court under Art 8(1), though suing both in the *anchor's* domicile is generally easier.17

---

## **3\. Applicable Law: The Rome II Maze**

Establishing jurisdiction is only the first step. The court must then determine the applicable substantive law. The DSA creates a harmonized *duty*, but it relies on national law for the *remedy*. Regulation (EC) No 864/2007 (Rome II) is the compass for this determination.19

### **3.1. The General Rule: Lex Loci Damni (Article 4(1))**

Article 4(1) Rome II dictates: *"The law applicable to a non-contractual obligation... shall be the law of the country in which the damage occurs irrespective of the country in which the event giving rise to the damage occurred."*.21

#### **3.1.1. The Fragmentation of Liability**

This rule is the single biggest source of fragmentation for DSA liability.

* **The Scenario:** A platform established in Ireland makes a single policy decision (e.g., regarding ad transparency) that violates the DSA. This single decision affects 27 million users across all Member States.  
* **The Result:**  
  * For a user in France, French tort law applies to the damages.  
  * For a user in Poland, Polish tort law applies.  
* **The "Country of Origin" Paradox:** The DSA proudly champions the Country of Origin (COO) principle for *regulatory supervision* (Article 2(3) DSA)—meaning only Ireland regulates the platform's compliance. However, for *private liability*, Rome II dictates the *Country of Destination*. The platform must comply with Irish administrative rules but is liable under 27 different civil codes for the damages caused by non-compliance.8

### **3.2. Specific Torts: Exceptions to the General Rule**

Rome II contains specific rules that may override Article 4(1) for certain types of DSA breaches.

#### **3.2.1. Unfair Competition (Article 6\)**

If the DSA breach constitutes an act of unfair competition (e.g., a marketplace manipulating rankings to favor its own products—a breach of Article 6(d) DMA or general fairness principles in DSA), Article 6(1) Rome II applies.

* **The Rule:** The law of the country where "competitive relations or the collective interests of consumers are, or are likely to be, affected."  
* **Relevance:** This is vital for "Dark Patterns" (Article 25 DSA). A dark pattern affects the collective interests of consumers in a specific market. Thus, if a platform deploys a dark pattern in Italy, Italian law applies to the damages claim, regardless of where the platform is headquartered. This aligns the applicable law with the market affected, preventing platforms from hiding behind the law of their domicile.24

#### **3.2.2. Environmental Damage (Article 7\)**

"Systemic Risks" under the DSA (Article 34\) include actual or foreseeable negative effects on "public health."

* **The Rule:** Article 7 Rome II allows the claimant to choose between the law of the damage (lex loci damni) or the law of the event (lex loci delicti).  
* **Scenario:** A viral "choking challenge" spreads on a platform due to algorithm negligence, causing injury to a child in Spain. The platform is in Ireland.  
* **Application:** The claimant can choose Spanish law (likely higher consumer protection) or Irish law. This gives a strategic advantage to victims of physical/health-related systemic harms.25

### **3.3. The Role of Terms of Service and Party Autonomy (Article 14\)**

Article 14 Rome II allows parties to choose the applicable law for their non-contractual obligations.

* **Timing:** For B2C (business-to-consumer), such a choice must be made *after* the dispute has arisen. A pre-dispute choice of law clause in the Terms of Service covering tort claims is **void** against a consumer (Article 14(1)(b)).  
* **Commercial Users:** For B2B relationships (e.g., platform vs. merchant), a pre-dispute choice of law is valid if "freely negotiated." However, standard ToS are rarely "freely negotiated." Courts may strike down these clauses if they deprive the weaker party of protection, pushing the determination back to Article 4(1).26

---

## **4\. Complex Interplay and Hybrid Claims**

DSA compensation claims will rarely exist in isolation. They will often be pleaded alongside violations of other digital regulations, creating "hybrid" disputes with conflicting jurisdictional and applicable law rules.

### **4.1. The DSA-GDPR Collision**

The overlap between the DSA and GDPR is substantial, particularly regarding advertising (Article 26 DSA) and data-driven dark patterns.27

* **Jurisdictional Conflict:**  
  * **DSA:** Relies on Brussels I bis (General rules).  
  * **GDPR:** Contains a specific jurisdiction rule in Article 79(2) GDPR, allowing claimants to sue where the controller has an establishment OR where the data subject resides.  
* **The "Exclusive Jurisdiction" Debate:** Is Article 79 GDPR exhaustive? In the *TikTok* case (Dutch courts), the court accepted jurisdiction for a combined claim involving GDPR and general tort (potentially DSA-like duties) violations. The court found that Article 79 GDPR provided a basis for the data protection aspects, while Brussels I bis covered the rest.  
* **Practical Implication:** A claimant might find it easier to establish jurisdiction for the GDPR part of a claim (due to the specific pro-claimant rule in Art 79\) than for the DSA part (which might require proving "consumer" status under Art 17 Brussels I bis to get the same home-court advantage). This could lead to the "slicing" of claims.29

### **4.2. The Product Liability Directive (PLD) and Software**

The new Product Liability Directive (PLD) explicitly covers software and AI systems as "products."

* **The Scenario:** A recommender system (software) is "defective" and radicalizes a user, causing psychological harm.  
  * **Claim 1 (DSA):** Breach of Article 34 (Systemic Risk assessment). Fault-based.  
  * **Claim 2 (PLD):** Defective product. Strict liability.  
* **PIL Nuance:** Article 5 of Rome II has a specific rule for product liability: it points to the law of the habitual residence of the person sustaining damage, *if the product was marketed there*.  
* **Convergence:** Fortunately, Rome II Art 5 and Art 4(1) (General Tort) usually lead to the same result (the victim's home law) in these cases. However, the *burden of proof* differs radically. The DSA claim requires proving negligence; the PLD claim requires proving a defect. Claimants will plead both to maximize chances of success.31

### **4.3. The AI Act and Presumptions of Fault**

The forthcoming AI Liability Directive (AILD) proposes a "presumption of causality" for non-compliance with the AI Act.

* **Synergy:** If a VLOP fails to comply with the AI Act regarding its algorithms (e.g., lack of human oversight), this regulatory finding can be transported into a DSA compensation claim to satisfy the "infringement" and "causality" requirements of Article 54 DSA.  
* **PIL Angle:** The applicable law for the "presumption" itself would likely be determined by Rome II (law of the tort). If the applicable national law (e.g., German law) has stricter evidence rules, the EU-level presumption in the AILD acts as a harmonizing procedural overlay, overriding conflicting national procedural rules.34

---

## **5\. Collective Redress and the Representative Actions Directive (RAD)**

Given the "diffuse" nature of digital harm—where millions suffer small individual losses—collective redress is the engine of DSA enforcement.

### **5.1. The RAD Mechanism**

Directive (EU) 2020/1828 (RAD) allows "Qualified Entities" (QEs) to bring representative actions for infringements of EU law, including the DSA (which is annexed to the RAD).

* **Standing:** QEs have standing to seek both injunctive measures (stopping the breach) and redress measures (compensation).  
* **Cross-Border Actions:** A QE from one Member State can sue in another.

### **5.2. The Jurisdictional Gap**

A critical flaw exists in the interplay between RAD and Brussels I bis.

* **No "Class" Jurisdiction:** Brussels I bis does not have a specific rule for collective actions.  
* **Consumer Rule Inapplicable:** The privileged "consumer jurisdiction" (Article 18\) applies only to a "consumer." The CJEU in *Schrems* (C-498/16) held that a claimant suing on assigned claims loses their consumer status. Similarly, a QE is not a "consumer."  
* **Consequence:** A QE representing 10,000 French consumers cannot rely on Article 18 to sue a US platform in French courts. They must rely on:  
  1. **Article 4:** Sue in the defendant's domicile (Ireland/Luxembourg). This forces all EU collective actions into one or two jurisdictions.  
  2. **Article 7(2):** Sue in France based on the "place of damage."  
* **The Fragmentation Risk:** If a QE represents consumers from France, Germany, and Italy, suing in France under Article 7(2) allows the court to hear *only* the claims regarding damage in France (Mosaic Theory). The court creates a jurisdictional wall against the German and Italian claims. To get a pan-European judgment, the QE *must* go to the defendant's domicile (Ireland). This creates a massive logistical bottleneck and disincentivizes cross-border collective redress.36

---

## **6\. Systemic Risk and the Challenge of "Pure Economic Loss"**

The DSA's concept of "Systemic Risk" (Articles 34-35) covers harms to civic discourse, electoral processes, and public security. Translating these societal harms into private compensation claims presents the ultimate PIL challenge.

### **6.1. Individualizing Systemic Harm**

How does an individual prove they were damaged by a "risk to civic discourse"?

* **Example:** A platform allows a bot network to inflate ad prices. The harm is purely financial (advertisers pay more).  
* **PIL Divergence:**  
  * **France:** Broad recovery under Art 1240 Civil Code.  
  * **Germany:** § 823(1) BGB excludes pure economic loss. The claimant must rely on § 823(2) (breach of a protective statute). The German courts must decide if Art 34 DSA is a *Schutzgesetz* intended to protect individual assets, or just the public interest.  
  * **England (Non-EU, but influential):** Tort of "breach of statutory duty" is strictly limited.

### **6.2. The Applicable Law Lottery**

Because Rome II Art 4(1) points to the law of the market/user, a platform's liability for a systemic failure will vary based on the user's location.

* **Scenario:** A data leak exposes users to phishing.  
* **Outcome:** Users in GDPR-friendly jurisdictions with generous non-material damage awards (e.g., Austria, post-*Post* case) will recover. Users in jurisdictions requiring "serious harm" thresholds might not.  
* **Conclusion:** The "Systemic Risk" obligations of the DSA are uniform, but the *financial consequences* of breaching them are geographically contingent. This undermines the predictability the DSA sought to create.7

---

## **7\. Conclusion: A Mosaic of Justice**

The private international law framework for DSA compensation claims is characterized by a tension between the Regulation's harmonizing objective and the fragmented reality of EU procedural law.  
Article 54 DSA creates a uniform *right*, but **Brussels I bis** and **Rome II** ensure that its enforcement remains local and diverse. The "place of damage" rule (Article 4(1) Rome II) effectively partitions the Digital Single Market into 27 liability zones. While this favors victims by applying their local laws, it creates legal uncertainty for providers regarding their exposure to "pure economic loss" and "non-material damage" claims.  
The interaction with the GDPR and the new AI Act adds further layers of complexity. The potential for parallel proceedings—where a single algorithmic failure triggers DSA, GDPR, PLD, and AI Act claims—requires sophisticated legal navigation. The **Representative Actions Directive**, while promising, is hamstrung by the lack of a dedicated jurisdictional rule in Brussels I bis, often forcing European consumers to litigate in Ireland or Luxembourg to achieve true cross-border redress.

### **7.1. Synthesis of Key Findings**

| Feature | Legal Source | Impact on DSA Compensation Claims |
| :---- | :---- | :---- |
| **Jurisdiction (General)** | Brussels I bis Art 4 | Concentrates litigation in Ireland/Luxembourg (Def. Domicile). |
| **Jurisdiction (Tort)** | Brussels I bis Art 7(2) | "Mosaic Theory" forces fragmentation of cross-border claims unless suing at source. |
| **Jurisdiction (Consumer)** | Brussels I bis Art 18 | Potent for individuals; inaccessible for SMEs and Collective Actions (QEs). |
| **Applicable Law** | Rome II Art 4(1) | *Lex Loci Damni* applies 27 different tort laws to a single platform policy. |
| **Unfair Competition** | Rome II Art 6 | Law of the affected market applies; key for "Dark Pattern" claims. |
| **Systemic Risk** | DSA Art 34 \+ National Tort Law | Recoverability of "pure economic loss" depends entirely on the random luck of the user's domicile law. |

### **7.2. Future Outlook**

The "Report on the application of the Brussels I Regulation" (mandated by Article 79 of that Regulation) provides a future legislative window to address these gaps. Specifically, creating a specialized jurisdiction for **Representative Actions**—allowing a QE to sue in the place where the *majority* of consumers are affected—would significantly enhance the efficacy of Article 54 DSA.40 Until then, private enforcement of the DSA will remain a complex, multi-jurisdictional chessboard.  
---

### **Table 3: Comparative Analysis of Overlapping Liability Regimes**

| Instrument | Trigger for Liability | Nature of Liability | Jurisdiction Rule | Applicable Law Rule |
| :---- | :---- | :---- | :---- | :---- |
| **DSA (Art 54\)** | Infringement of Due Diligence | Fault-based (Negligence/Breach of Duty) | Brussels I bis (General) | Rome II Art 4(1) (Place of Damage) |
| **GDPR (Art 82\)** | Unlawful Processing | Strict(er) Liability / Presumed Fault | Art 79 GDPR (*Lex Specialis* \- Home Court) | Rome II Art 4(1) |
| **Product Liability (PLD)** | Defect in Product (Software) | Strict Liability | Brussels I bis | Rome II Art 5 (Habitual Residence) |
| **AI Act** | Non-compliance (High Risk) | Fault-based (with AILD presumptions) | Brussels I bis | Rome II Art 4(1) |
| **UCPD (via National Law)** | Unfair Commercial Practice | Fault/Strict (varies by MS) | Brussels I bis | Rome II Art 6 (Market Effect) |

*End of Report*

#### **Works cited**

1. Article 54, the Digital Services Act (DSA), accessed November 22, 2025, [https://www.eu-digital-services-act.com/Digital\_Services\_Act\_Article\_54.html](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_54.html)  
2. RISING ABOVE LIABILITY: THE DIGITAL SERVICES ACT AS A BLUEPRINT FOR THE SECOND GENERATION OF GLOBAL INTERNET RULES \- Berkeley Technology Law Journal, accessed November 22, 2025, [https://btlj.org/wp-content/uploads/2024/01/0002\_38-3\_Husovec.pdf](https://btlj.org/wp-content/uploads/2024/01/0002_38-3_Husovec.pdf)  
3. Compensation Claims under the Digital Services Act \- Reed Smith LLP, accessed November 22, 2025, [https://viewpoints.reedsmith.com/post/102jglg/compensation-claims-under-the-digital-services-act](https://viewpoints.reedsmith.com/post/102jglg/compensation-claims-under-the-digital-services-act)  
4. Compensation under Art. 82 GDPR: A mere violation is not enough | Insights \- Mayer Brown, accessed November 22, 2025, [https://www.mayerbrown.com/en/insights/publications/2023/05/compensation-under-art-82-gdpr-a-mere-violation-is-not-enough](https://www.mayerbrown.com/en/insights/publications/2023/05/compensation-under-art-82-gdpr-a-mere-violation-is-not-enough)  
5. CJEU Rejects Minimum Threshold for GDPR Claims, accessed November 22, 2025, [https://www.globalprivacyblog.com/2023/05/cjeu-rejects-minimum-threshold-for-gdpr-claims/](https://www.globalprivacyblog.com/2023/05/cjeu-rejects-minimum-threshold-for-gdpr-claims/)  
6. WHERE DOES ECONOMIC LOSS OCCUR? MATTHIAS LEHMANN\* 1\. The Role of the Place of Damage in Private International Law The financial, accessed November 22, 2025, [https://deicl.univie.ac.at/fileadmin/user\_upload/i\_deicl/Lehmann/Publikationen/Lehmann\_2011\_Economic\_loss\_occur.pdf](https://deicl.univie.ac.at/fileadmin/user_upload/i_deicl/Lehmann/Publikationen/Lehmann_2011_Economic_loss_occur.pdf)  
7. Full article: Toxic recommender algorithms: immunities, liabilities and the regulated self-regulation of the Digital Services Act and the Online Safety Act, accessed November 22, 2025, [https://www.tandfonline.com/doi/full/10.1080/17577632.2024.2408912](https://www.tandfonline.com/doi/full/10.1080/17577632.2024.2408912)  
8. European Union Law Working Papers, accessed November 22, 2025, [https://law.stanford.edu/wp-content/uploads/2024/02/EU-Law-WP-85-Stikovic.pdf](https://law.stanford.edu/wp-content/uploads/2024/02/EU-Law-WP-85-Stikovic.pdf)  
9. Regulation \- 1215/2012 \- EN \- Brussels I bis \- EUR-Lex \- European Union, accessed November 22, 2025, [https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32012R1215](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex:32012R1215)  
10. international law association lisbon conference (2022) protection of privacy in private international and procedural law, accessed November 22, 2025, [https://www.ila-hq.org/en/documents/protec-1](https://www.ila-hq.org/en/documents/protec-1)  
11. Jurisdiction Concerning Actions by a Legal Person for Disparaging Statements on the Internet: The Persistence of the Mosaic Approach | European Papers, accessed November 22, 2025, [https://www.europeanpapers.eu/europeanforum/jurisdiction-concerning-actions-by-legal-person-for-disparaging-statements-on-internet-mosaic-approach](https://www.europeanpapers.eu/europeanforum/jurisdiction-concerning-actions-by-legal-person-for-disparaging-statements-on-internet-mosaic-approach)  
12. CJEU on the place of the damage under Article 7(2) of Brussels Ia as regards violation of personality rights of a legal person \- Conflict of Laws .net, accessed November 22, 2025, [https://conflictoflaws.net/2017/cjeu-on-the-place-of-the-damage-under-article-72-of-brussels-ia-as-regards-violation-of-personality-rights-of-a-legal-person/](https://conflictoflaws.net/2017/cjeu-on-the-place-of-the-damage-under-article-72-of-brussels-ia-as-regards-violation-of-personality-rights-of-a-legal-person/)  
13. Giustizia consensuale \- Radboud Repository, accessed November 22, 2025, [https://repository.ubn.ru.nl/bitstream/handle/2066/289314/289314.pdf?sequence=1\&isAllowed=y](https://repository.ubn.ru.nl/bitstream/handle/2066/289314/289314.pdf?sequence=1&isAllowed=y)  
14. CJEU clarifies jurisdiction for follow-on damage claims \- Stibbe, accessed November 22, 2025, [https://www.stibbe.com/publications-and-insights/cjeu-clarifies-jurisdiction-for-follow-on-damage-claims](https://www.stibbe.com/publications-and-insights/cjeu-clarifies-jurisdiction-for-follow-on-damage-claims)  
15. Landmark judgment by the EU Court of Justice on the interpretation of the place of harmful event under Regulation Brussels I bis for the determination of alternative grounds of jurisdiction in pan-European cartel damages cases \- CDC, accessed November 22, 2025, [https://carteldamageclaims.com/2019/08/05/landmark-judgment-by-the-eu-court-of-justice-on-the-interpretation-of-the-place-of-harmful-event-under-regulation-brussels-i-bis-for-the-determination-of-alternative-grounds-of-jurisdiction-in-pan-eur/](https://carteldamageclaims.com/2019/08/05/landmark-judgment-by-the-eu-court-of-justice-on-the-interpretation-of-the-place-of-harmful-event-under-regulation-brussels-i-bis-for-the-determination-of-alternative-grounds-of-jurisdiction-in-pan-eur/)  
16. International private law aspects and dispute settlement related to transnational company agreements \- European Commission, accessed November 22, 2025, [https://ec.europa.eu/social/BlobServlet?docId=4815\&langId=en](https://ec.europa.eu/social/BlobServlet?docId=4815&langId=en)  
17. Strict Interpretation of Article 8(1) Brussels I (recast): Limits on Non-Anchor Defendants' Jurisdiction: High Court of Ireland | CaseMine, accessed November 22, 2025, [https://www.casemine.com/commentary/uk/strict-interpretation-of-article-8(1)-brussels-i-(recast):-limits-on-non-anchor-defendants%E2%80%99-jurisdiction/view](https://www.casemine.com/commentary/uk/strict-interpretation-of-article-8\(1\)-brussels-i-\(recast\):-limits-on-non-anchor-defendants%E2%80%99-jurisdiction/view)  
18. In order to establish jurisdiction under Article 8(1) of the Recast Brussels Regulation, does the anchor defendant need to be domiciled in England? | Practical Law, accessed November 22, 2025, [https://uk.practicallaw.thomsonreuters.com/a-017-2480?transitionType=Default\&contextData=(sc.Default)](https://uk.practicallaw.thomsonreuters.com/a-017-2480?transitionType=Default&contextData=\(sc.Default\))  
19. Regulation (EC) No 864/2007 of the European Parliament and of the Council of 11 July 2007 on the law applicable to non-contractual obligations (Rome II) \- EUR-Lex, accessed November 22, 2025, [https://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2007:199:0040:0049:EN:PDF](https://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2007:199:0040:0049:EN:PDF)  
20. Governing law and jurisdiction: Rome II \- Pinsent Masons, accessed November 22, 2025, [https://www.pinsentmasons.com/out-law/guides/governing-law-and-jurisdiction-rome-ii](https://www.pinsentmasons.com/out-law/guides/governing-law-and-jurisdiction-rome-ii)  
21. Applicable law: the step-by-step approach necessary under article 4 of the Rome II Regulation \- Clyde & Co, accessed November 22, 2025, [https://connectedworld.clydeco.com/post/102jan1/applicable-law-the-step-by-step-approach-necessary-under-article-4-of-the-rome-i](https://connectedworld.clydeco.com/post/102jan1/applicable-law-the-step-by-step-approach-necessary-under-article-4-of-the-rome-i)  
22. Personal Injury and Article 4(3) of Rome II Regulation \- Conflict of Laws .net, accessed November 22, 2025, [https://conflictoflaws.net/2021/personal-injury-and-article-43-of-rome-ii-regulation/](https://conflictoflaws.net/2021/personal-injury-and-article-43-of-rome-ii-regulation/)  
23. CJEU confirms the limitations of MS' powers to regulate online services providers based in other MS \- Hogan Lovells, accessed November 22, 2025, [https://www.hoganlovells.com/en/publications/cjeu-confirms-the-limitations-of-ms-powers-to-regulate-online-services-providers-based-in-other-ms](https://www.hoganlovells.com/en/publications/cjeu-confirms-the-limitations-of-ms-powers-to-regulate-online-services-providers-based-in-other-ms)  
24. Study on EU instruments, accessed November 22, 2025, [https://www.parlament.gv.at/dokument/XXVIII/EU/45074/imfname\_11541968.pdf](https://www.parlament.gv.at/dokument/XXVIII/EU/45074/imfname_11541968.pdf)  
25. List of publications from the EP Think Tank \- European Union, accessed November 22, 2025, [https://www.europarl.europa.eu/thinktank/en/research/advanced-search/pdf?keywords=1211](https://www.europarl.europa.eu/thinktank/en/research/advanced-search/pdf?keywords=1211)  
26. Jurisdiction and governing law – Rome II \- Kennedys Law, accessed November 22, 2025, [https://www.kennedyslaw.com/en/thought-leadership/article/jurisdiction-and-governing-law-rome-ii/](https://www.kennedyslaw.com/en/thought-leadership/article/jurisdiction-and-governing-law-rome-ii/)  
27. Art. 82 GDPR – Right to compensation and liability \- General Data Protection Regulation (GDPR), accessed November 22, 2025, [https://gdpr-info.eu/art-82-gdpr/](https://gdpr-info.eu/art-82-gdpr/)  
28. EU's Digital Services Act Just Became Applicable: Outlining Ten Key Areas of Interplay with the GDPR \- The Future of Privacy Forum, accessed November 22, 2025, [https://fpf.org/blog/eus-digital-services-act-just-became-applicable-outlining-ten-key-areas-of-interplay-with-the-gdpr/](https://fpf.org/blog/eus-digital-services-act-just-became-applicable-outlining-ten-key-areas-of-interplay-with-the-gdpr/)  
29. News Archieven \- Bureau Brandeis, accessed November 22, 2025, [https://bureaubrandeis.com/category/news/?lang=en](https://bureaubrandeis.com/category/news/?lang=en)  
30. Financing Collective Actions in the Netherlands \- PURE.EUR.NL., accessed November 22, 2025, [https://pure.eur.nl/ws/portalfiles/portal/155567615/Financing\_Collective\_Actions\_in\_the\_Netherlands.pdf](https://pure.eur.nl/ws/portalfiles/portal/155567615/Financing_Collective_Actions_in_the_Netherlands.pdf)  
31. The new EU Product Liability Directive: key implications for automotive and autonomous vehicle companies | Perspectives | Reed Smith LLP, accessed November 22, 2025, [https://www.reedsmith.com/en/perspectives/2025/10/the-new-eu-product-liability-key-implications-autonomous-vehicle](https://www.reedsmith.com/en/perspectives/2025/10/the-new-eu-product-liability-key-implications-autonomous-vehicle)  
32. Revised Product Liability Directive | European Parliament, accessed November 22, 2025, [https://www.europarl.europa.eu/RegData/etudes/BRIE/2023/739341/EPRS\_BRI(2023)739341\_EN.pdf](https://www.europarl.europa.eu/RegData/etudes/BRIE/2023/739341/EPRS_BRI\(2023\)739341_EN.pdf)  
33. EU Product Liability and AI: Key Reforms Explained \- Mason Hayes Curran, accessed November 22, 2025, [https://www.mhc.ie/latest/insights/revised-product-liability-directive-and-the-proposed-artificial-intelligence-liability-directive](https://www.mhc.ie/latest/insights/revised-product-liability-directive-and-the-proposed-artificial-intelligence-liability-directive)  
34. EU AI Act unpacked \#13: Unlocking synergies: Navigating the AI Act and the Digital Services Act \- Freshfields Technology Quotient, accessed November 22, 2025, [https://technologyquotient.freshfields.com/post/102jhbz/eu-ai-act-unpacked-13-unlocking-synergies-navigating-the-ai-act-and-the-digita](https://technologyquotient.freshfields.com/post/102jhbz/eu-ai-act-unpacked-13-unlocking-synergies-navigating-the-ai-act-and-the-digita)  
35. Modified Liability for AI: EU Review of AI Liability Rules \- Orrick, accessed November 22, 2025, [https://www.orrick.com/en/Insights/2023/05/Modified-Liability-for-AI-EU-Review-of-AI-Liability-Rules](https://www.orrick.com/en/Insights/2023/05/Modified-Liability-for-AI-EU-Review-of-AI-Liability-Rules)  
36. Private International Law and Cross-Border Collective Redress \- BEUC, accessed November 22, 2025, [https://www.beuc.eu/sites/default/files/publications/BEUC-X-2022-085\_Private\_International\_Law\_and\_Cross-Border\_Collective\_Redress.pdf](https://www.beuc.eu/sites/default/files/publications/BEUC-X-2022-085_Private_International_Law_and_Cross-Border_Collective_Redress.pdf)  
37. Comparative Legal Study on Procedural Rules and their Impact on Collective Redress Actions in Europe \- BEUC, accessed November 22, 2025, [https://www.beuc.eu/sites/default/files/publications/BEUC-X-2025-026\_Study\_Procedural\_Rules\_Impact\_on\_Collective\_Redress\_in\_EU.pdf](https://www.beuc.eu/sites/default/files/publications/BEUC-X-2025-026_Study_Procedural_Rules_Impact_on_Collective_Redress_in_EU.pdf)  
38. The Impact of Increased Mass Litigation in Europe \- European Centre for International Political Economy, accessed November 22, 2025, [https://ecipe.org/wp-content/uploads/2025/02/ECI\_OccasionalPaper\_03-2025\_LY07.pdf](https://ecipe.org/wp-content/uploads/2025/02/ECI_OccasionalPaper_03-2025_LY07.pdf)  
39. APPLYING THE ECONOMIC LOSS RULE IN TEXAS \- Baylor University, accessed November 22, 2025, [https://www.baylor.edu/content/services/document.php/176869.pdf](https://www.baylor.edu/content/services/document.php/176869.pdf)  
40. The Brussels Ibis reform, third state defendants and the Dutch experience \- NIPR Online, accessed November 22, 2025, [https://www.nipr-online.eu/pdf/NIPR\_01\_2025\_Henckel\_2.pdf](https://www.nipr-online.eu/pdf/NIPR_01_2025_Henckel_2.pdf)