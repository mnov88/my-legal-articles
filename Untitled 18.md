
# **Algorithmic Gatekeeping in the Public Sphere: A Legal Analysis of AI-Assisted Filtering of Consultation Submissions under GDPR Article 22**

## **Executive Summary**

The digitization of public administration has precipitated a fundamental shift in the mechanics of participatory democracy. Facing an exponential increase in digital feedback, public authorities are increasingly turning to Artificial Intelligence (AI)—specifically Large Language Models (LLMs) and Natural Language Processing (NLP) tools—to aggregate, summarize, and filter public consultation submissions. This technological transition, while promising efficiency, introduces a layer of algorithmic gatekeeping that fundamentally alters the relationship between the citizen and the state. This report provides an exhaustive doctrinal analysis of whether such "upstream" AI filtering constitutes a violation of Article 22 of the General Data Protection Regulation (GDPR).  
Drawing heavily on the Court of Justice of the European Union’s (CJEU) landmark ruling in *SCHUFA* (C-634/21), the analysis demonstrates that the "determining role" doctrine has profoundly expanded the legal definition of an automated decision. The conventional administrative defense—that AI tools are merely preparatory aids for human decision-makers—is no longer legally robust. When AI systems filter, prioritize, or suppress submissions based on sentiment, stance, or quality metrics, they often function as the de facto decision-makers regarding the admissibility of citizen input.  
This report systematically addresses six critical unresolved legal questions: (1) the collapsing distinction between 'solely automated' processing and human review; (2) the classification of information gatekeeping as a justiciable 'decision'; (3) the attribution of liability for indirect effects on third-party administrative decisions; (4) the recognition of procedural determinations as producing 'legal' or 'similarly significant' effects; (5) the ontological boundary between content evaluation and prohibited profiling; and (6) the adequacy of Article 22(2)(b) safeguards in current administrative law frameworks. The findings suggest that without rigorous "human-in-the-loop" architectures and specific legislative authorization, the deployment of AI filtering in public consultations presents a high risk of infringing upon GDPR Article 22, Article 9 (special category data), and the fundamental right to good administration enshrined in the Charter of Fundamental Rights.  

---

## **I. Introduction: The Automation of Participatory Democracy**

The contemporary administrative state faces a dual crisis of capacity and legitimacy. On one hand, the ease of digital communication has enabled mass participation in public consultations, resulting in an influx of submissions that often exceeds the cognitive processing capacity of human civil servants.1 On the other hand, the imperative to maintain democratic responsiveness requires that these submissions be meaningfully considered. To bridge this gap, public authorities act as early adopters of AI technologies, deploying systems ranging from basic spam filters to advanced generative AI summarizers.2 These tools promise to synthesize millions of disparate citizen inputs into actionable policy insights, ostensibly enhancing the efficiency of the "notice and comment" rulemaking process.4  
However, the deployment of such technologies introduces a "black box" into the heart of democratic deliberation. When an algorithm determines which comments are "substantive" and which are "noise," it exercises a form of power that is distinct from traditional bureaucratic discretion. This power is exercised invisibly, upstream of the final policy decision, and often without the procedural safeguards that characterize administrative law.5  
The legal framework governing this technological shift is anchored in the General Data Protection Regulation (GDPR), specifically Article 22, which grants data subjects the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects or similarly significantly affects them.7 While Article 22 was drafted with private sector applications in mind—such as credit scoring and e-recruiting 9—its application to the public sector creates complex interpretive challenges. The core tension lies between the administrative necessity of automation and the prohibition of automated decisions that impact fundamental rights.  
Recent jurisprudence from the Court of Justice of the European Union (CJEU), particularly the *SCHUFA* judgment (Case C-634/21), has significantly altered the landscape of automated decision-making (ADM). By establishing that a preparatory automated score can constitute a "decision" if it plays a determining role in the final outcome, the Court has cast doubt on the legality of many "human-in-the-loop" systems used in public administration.7 If an AI filter suppresses a citizen's submission, and the human policymaker never sees it, the AI has effectively made the final decision regarding that citizen's participation.  
This report examines the legality of AI filtering through the lens of this evolving jurisprudence, integrating insights from administrative law, data protection regulations, and the emerging EU AI Act. It explores the friction between the "efficiency" of automated governance and the "fairness" mandated by the rule of law.  

---

## **II. The Technical and Legal Anatomy of AI Filtering**

To understand the legal implications, one must first dissect the technical mechanisms of AI filtering and how they map onto legal concepts. The use of AI in public consultations is not a monolithic practice but a spectrum of automated processing activities, each carrying distinct legal risks.

### **A. Taxonomy of AI Interventions in Consultation**

Public authorities utilize various AI techniques to manage the volume of submissions. These can be categorized by their function and their potential impact on the data subject (the submitter).  
**Table 1: Taxonomy of AI Processing in Public Consultations and GDPR Implications**

| AI Function | Technical Mechanism | Operational Consequence | Potential GDPR Classification |
| :---- | :---- | :---- | :---- |
| **Deduplication** | Similarity pipelines (e.g., scikit-learn, spaCy) identify identical text.2 | Groups mass campaigns/petitions into single entries. | Likely **not profiling** if limited to exact matches; low risk if human reviews the "master" copy. |
| **Spam/Toxicity Filtering** | Classifiers trained on datasets of spam or hate speech (e.g., OpenAI Content Filter).11 | **Blocks** or hides submissions deemed irrelevant, abusive, or dangerous. | **Automated Decision-Making (ADM)**. Rejection of input constitutes a decision on admissibility. |
| **Sentiment Analysis** | NLP models (BERT, RoBERTa) score text polarity (Positive/Negative).12 | Prioritizes or categorizes feedback based on emotional tone. | **Profiling** (Art. 4(4)). Evaluates "personal aspects" (attitude/opinion). Risk of Art. 9 violation (political opinion). |
| **Stance Detection** | Supervised learning models classify stance toward specific policy proposals (Support/Oppose).14 | Aggregates support levels; may filter "outliers" or minority views. | **Profiling** of political opinion. High risk if used to silence opposition. |
| **Summarization** | Generative LLMs (GPT-4, Claude) compress large text bodies into executive summaries.2 | **Omission** of nuances or minority viewpoints in the summary presented to humans. | **ADM with Indirect Effect**. The "decision" is the editorial choice of what to include/exclude. |

### **B. The "Upstream" Nature of Filtering**

In cybersecurity and network engineering, "upstream filtering" refers to the blocking of traffic at the ISP or network level before it reaches the end-user's device.5 In the context of public administration, AI acts as an "upstream filter" for the policymaker. The submissions are "traffic," and the civil servant is the "end-user."  
The legal criticality of upstream filtering lies in its invisibility. Unlike a rejected credit application where the applicant receives a notification, a filtered consultation submission simply disappears from the administrative record. The submitter receives no "bounce back" or rejection notice; the submission is technically "received" by the server but procedurally "dead" upon arrival.6 This creates a situation where the "decision" to exclude the citizen is made solely by the software, often without the knowledge of the human authority who is nominally responsible for the consultation. This structural opacity directly engages the "solely automated" prong of Article 22, as explored in the subsequent sections.  
---

## **III. Question 1: 'Solely Automated' Processing vs. Meaningful Human Review**

The first critical legal question concerns the threshold at which a process is considered "solely automated" under Article 22(1). Administrative bodies routinely defend their use of AI by citing the "human-in-the-loop" defense: because a human official ultimately signs the policy document or reviews the *aggregated* report, they argue the process is not *solely* automated.17 However, a rigorous analysis of CJEU jurisprudence and EDPB guidelines suggests this defense is increasingly porous.

### **A. The "Rubber Stamping" Phenomenon and the Illusion of Oversight**

Article 22(1) applies only where there is *no* human involvement in the decision-making process. However, regulatory guidance has consistently held that this human involvement must be "meaningful" rather than a "token gesture".19 The concept of "meaningful human intervention" requires that the human actor has the *authority* and the *competence* to change the decision, and actually exercises this authority.17  
In the context of high-volume filtering, the "rubber stamping" phenomenon is acute. If an AI system flags 10,000 submissions as "spam" or "non-substantive," and a human officer simply approves this deletion in bulk without reviewing the individual contents, the human involvement is nominal.22 Research into automation bias confirms that humans are cognitively predisposed to trust automated outputs, especially when under time pressure or dealing with massive datasets.24  
Consequently, if the standard administrative procedure is to trust the AI filter's classification, the process is *de facto* solely automated. The EDPB has clarified that the controller cannot fabricate human involvement to avoid Article 22 provisions.19 If the human review is merely a procedural formality that validates the algorithm's output in "almost all cases," the decision remains solely automated in the eyes of the law.25

### **B. The *Schufa* Doctrine: The "Determining Role" Test**

The CJEU’s ruling in *SCHUFA* (C-634/21) provides the decisive analytical framework for this issue. The case concerned a credit scoring algorithm used by SCHUFA (a credit reference agency). The bank argued that SCHUFA did not make an automated decision because the bank's human employees made the final decision on the loan. The Court rejected this, holding that the automated score constituted a "decision" under Article 22 because it played a "determining role" in the bank's process.7  
**Table 2: The *Schufa* Analogy: From Credit Scoring to Public Consultation**

| Element | SCHUFA Case (Credit Scoring) | Public Consultation Case (AI Filtering) | Legal Consequence |
| :---- | :---- | :---- | :---- |
| **Automated Input** | Probability value (Score) generated by SCHUFA. | Relevance/Toxicity Score generated by AI Filter. | Both serve as the primary heuristic for the human decision-maker. |
| **Human Actor** | Bank employee granting the loan. | Civil servant drafting the policy summary. | The human actor relies on the automated input to manage complexity. |
| **Process Logic** | Low score $\\rightarrow$ Loan rejection in almost all cases. | "Toxic" tag $\\rightarrow$ Exclusion from analysis in almost all cases. | The automated classification predetermines the outcome. |
| **Information Gap** | Bank cannot explain the score; SCHUFA claims trade secrets. | Civil servant cannot explain the LLM's reasoning; vendor claims IP. | "Lacuna in legal protection" if Art. 22 doesn't apply to the algorithm. |

The Court's reasoning was purposive: interpreting Article 22 strictly to require the final formal act to be automated would allow controllers to circumvent the GDPR by inserting a human straw man.10 By analogy, in public consultations, if the AI filter's classification of a submission as "irrelevant" leads to its exclusion from the policy deliberation in essentially all cases, the AI has played a determining role. The filter *is* the decision-maker regarding the *admissibility* of that citizen's view.

### **C. The "Upstream" Trap: When Humans Never See the Data**

The *Schufa* doctrine is even more potent in the case of "upstream filtering" where the rejected content is never presented to the human. In *SCHUFA*, the bank employee at least saw the score and the application. In AI-moderated consultations, if the system is configured to auto-archive comments flagged as "abusive" or "spam" without a human queue, the "determining role" is absolute. The human policymaker is not even aware that a decision has been made to exclude specific feedback.27  
This scenario creates a paradox: the administration claims a human made the decision (the policy), but the dataset upon which that decision was based was curated solely by AI. The "decision" to exclude the specific citizen from the dataset was solely automated, and under *Schufa*, this upstream decision is justiciable under Article 22\.10  
---

## **IV. Question 2: Information Gatekeeping as a Justiciable 'Decision'**

The second unresolved question centers on the ontology of the "decision" itself. Public authorities typically argue that filtering is a preparatory administrative act—a mere processing step—rather than a "decision" with legal standing. This distinction, rooted in traditional administrative law, faces significant challenges under the GDPR's broader definitions.

### **A. The "Invisible Rejection" and Preparatory Acts**

In traditional administrative law, judicial review is often limited to final decisions that definitively determine the legal position of an individual.32 Intermediate measures, such as internal memos or preparatory reports, are generally not reviewable unless they produce independent legal effects.34 Public bodies argue that an AI summary or a filtered dataset is an "intermediate measure" preparing for the final regulation or policy.18  
However, the *Schufa* judgment explicitly dismantled this "preparatory act" defense in the context of automated processing. The Court held that classifying the automated score as merely preparatory would result in a "lacuna in legal protection".7 If the data subject cannot challenge the automated score (the preparatory act) because it is not "final," and cannot challenge the final decision on the grounds of the score (because the final decision-maker lacks the algorithm's logic), their rights under Article 22 and Article 15(1)(h) (right to explanation) are nullified.10  
Applying this to public consultations:

1. **The Act of Exclusion:** When an AI tool marks a submission as "Do Not Process," that is a final determination regarding that specific data packet. For the citizen, the process has ended; their input will not be heard.  
2. **Lack of Remedy:** If this exclusion is treated as merely preparatory, the citizen has no recourse. They cannot challenge the final policy on the grounds that "my specific comment was auto-deleted," because the policymaker is likely unaware of the deletion.  
3. **Conclusion:** Therefore, to ensure effective legal protection, the act of information gatekeeping—the filtering itself—must be qualified as a "decision" within the meaning of Article 22(1).28

### **B. The Power of Summarization as Decision-Making**

The issue extends beyond binary acceptance/rejection to the nuance of *summarization*. Generative AI models (LLMs) are increasingly used to synthesize thousands of comments into a "key themes" report.2 This process involves editorial decisions: selecting which points are "key" and which are "peripheral."  
If an LLM is tasked with summarizing 50,000 comments on a controversial zoning law, and it hallucinates or statistically marginalizes a valid minority objection (e.g., regarding a specific endangered species), that objection is effectively excised from the record.36 The "decision" here is the *determination of relevance*.  
Legal scholarship suggests that "summarization" by AI is not a neutral compression of data but a normative evaluation of content.38 When this evaluation determines whether a citizen's argument reaches the human decision-maker, it constitutes a "decision" that affects the citizen's participation rights. The "black box" nature of LLMs—where the logic of inclusion/exclusion is non-deterministic and opaque—exacerbates the legal risk, as it prevents the administration from verifying whether the summarization was fair or arbitrary.39  
---

## **V. Question 3: Indirect Effects and the Chain of Decision-Making**

The third question addresses the causal chain between the AI's output and the final administrative action. This involves the legal concept of "indirect effects" on third-party decisions (in this case, the human policymaker's decision).

### **A. The "Decisive Influence" Standard**

The *Schufa* court introduced the standard that an automated output constitutes a decision if it "draws strongly" on the automated value or if the value plays a "determining role".28 This creates a test of *factual influence* rather than formal authority.  
In the context of consultation filtering, the factual influence of the AI is often absolute regarding the *content* of the submissions.

* **Scenario:** An agency receives 100,000 comments. An AI tool filters out 20,000 as "spam/irrelevant." The human team only reviews the remaining 80,000.  
* **Analysis:** For the 20,000 excluded submitters, the AI played a "determining role." The human decision to proceed with the policy was based on a dataset defined by the AI. The AI's "decision" to exclude data point $X$ was the *proximate cause* of the human's failure to consider argument $X$.

This causal link is robust enough to trigger Article 22 liability. The CJEU emphasized that where a third party (the bank/agency) relies on the automated processing to establish a relationship or make a decision, the automated processing itself produces effects.7

### **B. Liability Chains and the "provider" vs. "Deployer"**

Under the AI Act and GDPR, confusion often arises regarding liability. Is it the software vendor (who trained the model) or the public authority (who deployed it) that makes the Article 22 decision?

* **Controller Responsibility:** The public authority is the Data Controller. They determine the "means and purposes" of the consultation. Even if they "outsource" the filtering to a vendor's cloud-based AI, the authority remains liable for the Article 22 breach.41  
* **The "Third Party" Dilemma:** In *Schufa*, the credit agency (provider) and the bank (user) were separate. The Court held the agency liable because otherwise, the bank could not provide the necessary explanations. Similarly, if a public authority uses a third-party AI platform (e.g., "ConsultationAI"), the authority cannot simply blame the vendor for "black box" errors. The authority must ensure the system complies with Article 22 *before* deployment, or else they are making unlawful automated decisions.35

---

## **VI. Question 4: Procedural Determinations as 'Decisions' with Significant Effects**

A pivotal defense for public authorities is that consultation responses are merely consultative. Unlike a credit denial or a firing, ignoring a comment does not arguably produce "legal effects" or "similarly significant effects" as required by Article 22\. However, a closer examination of administrative and constitutional law reveals this to be a misconception.

### **A. Legal Effects: The Aarhus Convention and Statutory Rights**

The "legal effect" threshold is met when a decision impacts a person's legal status or their rights under a contract or law.18 In the domain of environmental governance, the **Aarhus Convention** and its implementing EU Directive (2011/92/EU) grant the public explicit legal rights to participate in decision-making.45

* **The Statutory Right:** Article 6 of the Aarhus Convention requires that "due account" is taken of the outcome of public participation.47  
* **The Procedural Defect:** If an AI filter systematically excludes relevant submissions (e.g., flagging "climate change" as a political keyword in a apolitical planning consultation), the authority has failed to take "due account."  
* **The Legal Consequence:** In EU administrative law, a breach of essential procedural requirements—such as the failure to consider mandatory public input—can lead to the **annulment** of the final decision (e.g., development consent).49

Therefore, the automated filtering of a submission produces a "legal effect": it violates the citizen's statutory right to be heard and potentially renders the entire administrative proceeding unlawful.51 The "decision" to exclude the comment is a decision to deny the exercise of a statutory right.

### **B. Similarly Significant Effects: Democratic Exclusion**

Outside of strict statutory rights (like Aarhus), Article 22 also covers "similarly significant effects." The EDPB interprets this to include decisions that affect a person's behavior, choices, or access to services, or that lead to discrimination.18

* **Exclusion from the Polity:** The systemic exclusion of a citizen's voice from the democratic process is a significant effect. If an algorithm biases against non-standard dialects, minority languages, or specific socio-economic phrasing, it effectively disenfranchises those groups from the feedback loop.54  
* **Cumulative Impact:** While a single rejected comment might seem trivial, the *Schufa* court and data protection authorities look at the scale and nature of the processing. The automated mass-screening of public opinion shapes the "reality" perceived by the government. If that reality is distorted by algorithmic bias, the effect on the citizenry is significant—it erodes the democratic legitimacy of the state.56  
* **Chilling Effect:** Knowledge that submissions are filtered by AI may deter participation (a "chilling effect" on speech), which is a recognized harm in fundamental rights jurisprudence.58

---

## **VII. Question 5: Profiling vs. Content Evaluation: The Ontological Boundary**

A common technical defense is that NLP tools analyze *content* (text), not *people* (data subjects). Therefore, the processing is not "profiling" under Article 4(4) GDPR. This distinction is ontologically and legally precarious.

### **A. Inferring "Personal Aspects" from Text**

Article 4(4) defines profiling as automated processing to evaluate "personal aspects," including "personal preferences, interests, reliability, behaviour".59 Modern NLP techniques, specifically **Sentiment Analysis** and **Stance Detection**, are designed precisely to evaluate these aspects.

* **Sentiment as Preference:** When an AI tool analyzes a submission to determine if the author is "Angry," "Satisfied," or "Neutral," it is evaluating the data subject's personal preference and emotional state.14  
* **Stance as Interest:** Classifying a submission as "Pro-Policy" or "Anti-Policy" is an evaluation of the data subject's interests and reliability regarding the proposed measure.12  
* **Linkage to Identity:** Even if the text is anonymized, modern data practices often link submissions to IP addresses or user accounts to detect "bot" activity. Once this link exists, the text analysis becomes profiling of an identifiable natural person.62

### **B. Sentiment Analysis as Special Category Data Processing**

The legal stakes escalate dramatically when the "personal aspect" inferred is a **political opinion**. Under GDPR Article 9, data revealing political opinions is "special category data" (sensitive data), and its processing is generally prohibited.58

* **Inference of Politics:** In a public consultation regarding a controversial law (e.g., migration, tax reform), a submission expressing strong opposition inherently reveals a political opinion. If an NLP model categorizes this submission as "Opposed/Negative Sentiment," it is processing special category data.64  
* **Article 22(4) Prohibition:** Article 22(4) explicitly prohibits automated decisions based on special category data unless (a) the subject has given **explicit consent**, or (b) the processing is necessary for substantial public interest *and* suitable measures are in place.66  
* **The Violation:** Public authorities rarely obtain explicit consent to *profile* the political sentiment of a submitter for the purpose of filtering them out. The "substantial public interest" defense is weak for mere administrative efficiency. Thus, using sentiment analysis to deprioritize "negative" feedback is a *prima facie* violation of Article 22(4).68

---

## **VIII. Question 6: Article 22(2)(b) Safeguards in Administrative Contexts**

Article 22(2)(b) provides an exemption for automated decisions "authorised by Union or Member State law" to which the controller is subject, provided that law lays down "suitable measures to safeguard the data subject's rights." The final question is whether current national administrative laws meet this high bar.

### **A. The Adequacy of Statutory Authorization**

General administrative laws that authorize "processing of data" or "digital government" are likely insufficient to authorize *solely automated filtering* under the strict requirements of the GDPR. Recital 71 mandates that the authorization must be specific.8  
**Comparative Analysis of National Frameworks:**

1. **Germany (VwVfG § 35a):**  
   * **The Rule:** Section 35a of the Administrative Procedure Act allows fully automated administrative acts (*Verwaltungsakt*) only where "permitted by a legal provision" and where there is "no discretion" or room for independent appreciation.71  
   * **Application:** Evaluating public comments is an inherently discretionary exercise (weighing arguments, assessing relevance). Therefore, fully automated filtering of consultation responses would likely fall *outside* the scope of § 35a, as it involves discretion. Without a specific legal basis, such automated filtering is unauthorized and thus illegal under Art 22(2)(b).73  
2. **France (CRPA Art. L311-3-1):**  
   * **The Rule:** The Code of Relations between the Public and the Administration allows individual decisions taken on the basis of algorithmic processing, provided the decision is explicitly mentioned and the rules defining the processing are communicated upon request.75  
   * **Application:** This framework is more permissive than the German one but imposes a strict **Transparency Condition**. If an authority uses a proprietary, "black box" LLM (like GPT-4) to filter comments and cannot explain the "rules defining the processing" (because the model is non-deterministic and opaque), it violates Article L311-3-1. The filtering becomes unlawful not because it is automated, but because it fails the explanation safeguard.30

### **B. The "Suitable Measures" Deficit**

Even if authorized by law, the controller must implement suitable measures, including the right to obtain human intervention, to express a point of view, and to contest the decision.66

* **The Notice Gap:** In AI filtering, the citizen is rarely notified that their submission was filtered out. Without notification ("You have been flagged as spam"), they cannot exercise their right to contest the decision or demand human intervention.51  
* **The "Black Box" Barrier:** Even if a citizen contests the filtering, the authority may be unable to provide a meaningful explanation of *why* the LLM rejected the comment, violating the right to good administration.79  
* **Conclusion:** Current administrative procedures for public consultations are architected for the era of paper mail; they lack the procedural "hooks" (notification, appeal mechanisms) necessary to make AI filtering compliant with Article 22 safeguards.10

---

## **IX. The Interplay with the AI Act and Future Regulation**

The regulatory landscape is tightening with the impending entry into force of the **EU AI Act**. This legislation explicitly codifies the risks identified in the GDPR analysis.

### **A. High-Risk Classification (Annex III)**

The AI Act classifies AI systems intended to be used for the "administration of justice and democratic processes" as **High-Risk** (Annex III, point 8).81 Specifically, systems used by public authorities to influence the outcome of elections or referenda, or to influence the democratic process, fall within this category.

* **Implication:** AI tools used to filter or summarize public consultation responses directly impact the democratic process. They are High-Risk AI systems.  
* **Obligations:** This classification triggers stringent obligations, including high-quality data governance (to prevent bias), record-keeping, transparency, and human oversight.83

### **B. Fundamental Rights Impact Assessment (FRIA)**

Article 27 of the AI Act requires deployers of high-risk AI systems (specifically public bodies) to conduct a **Fundamental Rights Impact Assessment (FRIA)** prior to deployment.84

* **The Assessment:** The authority must assess the specific risks of harm to the fundamental rights of the individuals affected (e.g., the right to freedom of expression, the right to good administration, non-discrimination).86  
* **The "Stop" Sign:** If an authority cannot guarantee that its AI filter will not disproportionately silence minority voices or misclassify valid dissent as "toxicity," the FRIA should theoretically prevent the deployment of the system.87 A negative FRIA would make the continued use of the system unlawful, reinforcing the Article 22 prohibition.

### **C. The European Ombudsman's Stance**

The European Ombudsman has already begun investigating the use of AI in public administration, emphasizing that efficiency cannot come at the cost of accountability.79 The Ombudsman recommends that public administrations must ensure AI systems are "tools to support decision-making" and not delegates of decision-making power. "Compliance checks" and "voluntary codes of conduct" are suggested to bridge the gap before the AI Act is fully operational.88 This soft law reinforces the hard law interpretation that "black box" filtering is maladministration.89  
---

## **X. Conclusion**

The inquiry into whether AI-assisted filtering of public consultation submissions violates GDPR Article 22 yields a nuanced but affirmatively critical conclusion. While public authorities often frame these tools as benign efficiency aids, the evolving jurisprudence of the CJEU, specifically the *Schufa* "determining role" doctrine, pierces this veil. When AI acts as a gatekeeper—filtering, suppressing, or prioritizing citizen input upstream of human review—it is making a "decision" with significant legal and democratic effects.  
**Summary of Legal Findings:**

1. **Solely Automated:** If the human reviewer does not audit the *excluded* submissions, the filtering process is solely automated. The "human-in-the-loop" is an illusion if they only see the "accepted" pile.  
2. **Decision Status:** Under *Schufa*, the upstream filtering constitutes a justiciable decision because it determines the admissibility of the citizen's input, predetermining the final outcome for that individual.  
3. **Effects:** Such decisions produce "legal effects" (violation of statutory participation rights like Aarhus) and "similarly significant effects" (exclusion from the democratic polity).  
4. **Profiling:** Use of Sentiment Analysis and Stance Detection constitutes profiling of "personal aspects" (political opinions), triggering the stricter prohibitions of Article 9 and Article 22(4).  
5. **Safeguards:** Existing national administrative laws (e.g., Germany, France) often lack the specific authorization and procedural safeguards (notification, contestability) required to legitimize *discretionary* automated filtering under Article 22(2)(b).

**Recommendations for Public Authorities:**  
To avoid unlawful automated decision-making, public authorities must restructure their AI deployment:

* **From Filtering to Tagging:** AI should never unilaterally *exclude* or *delete* submissions. It should function only to *tag* or *group* comments for human review (e.g., "Potential Spam" folder, not "Delete").  
* **Human Audit of the Negative:** Meaningful human intervention requires auditing the *rejected* pile, not just the accepted one.  
* **Transparency:** The use of AI in analyzing submissions must be publicly disclosed, including the logic of the filtering, to satisfy Article 13/14 GDPR and the principle of good administration.79  
* **Avoid Sentiment Scoring for Eligibility:** Using sentiment analysis to determine the *visibility* or *weight* of a submission carries unacceptable legal risk under Article 9 GDPR.

In the age of AI, the right to be heard must include the right not to be silenced by an algorithm. The current trajectory of "upstream filtering" risks creating a sanitized, automated democracy that hears only what the algorithm has been trained to select.  
---

*Note: Citations follow the format as provided in the research material.*

#### **Works cited**

1. Implementing Federal-Wide Comment Analysis Tool \- Project Open Data, accessed November 21, 2025, [https://resources.data.gov/assets/documents/CDOC\_Recommendations\_Report\_Comment\_Analysis\_FINAL.pdf](https://resources.data.gov/assets/documents/CDOC_Recommendations_Report_Comment_Analysis_FINAL.pdf)  
2. From Noise to Insight: Using AI to Rethink Public Comment Analysis | by Dr. Sandra Whitehead | Sep, 2025 | Medium, accessed November 21, 2025, [https://medium.com/@sandrawhitehead/from-noise-to-insight-using-ai-to-rethink-public-comment-analysis-58fa27c13900](https://medium.com/@sandrawhitehead/from-noise-to-insight-using-ai-to-rethink-public-comment-analysis-58fa27c13900)  
3. Summarizing Public Comments on Policy Proposals Using Large Language Models, accessed November 21, 2025, [https://www.ippapublicpolicy.org/file/paper/666960f7df1a8.pdf](https://www.ippapublicpolicy.org/file/paper/666960f7df1a8.pdf)  
4. Filtering Out the Noise: Does the APA Prevent Use of AI/ML tools in Agency Review of Public Comment? \- N.Y.U. Proceedings, accessed November 21, 2025, [https://proceedings.nyumootcourt.org/2024/09/filtering-out-the-noise-does-the-apa-prevent-use-of-ai-ml-tools-in-agency-review-of-public-comment/](https://proceedings.nyumootcourt.org/2024/09/filtering-out-the-noise-does-the-apa-prevent-use-of-ai-ml-tools-in-agency-review-of-public-comment/)  
5. Criminal Justice Information Services (CJIS) Security Policy \- FBI.gov, accessed November 21, 2025, [https://le.fbi.gov/file-repository/cjis\_security\_policy\_v5-9-3\_20230914-1.pdf](https://le.fbi.gov/file-repository/cjis_security_policy_v5-9-3_20230914-1.pdf)  
6. Listeners' Choices Online \- Southern California Law Review, accessed November 21, 2025, [https://southerncalifornialawreview.com/2025/09/25/listeners-choices-online/](https://southerncalifornialawreview.com/2025/09/25/listeners-choices-online/)  
7. SCHUFA Holding and Others (Scoring) \- EUR-Lex \- European Union, accessed November 21, 2025, [https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:62021CC0634](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:62021CC0634)  
8. Case C-634/21, OQ v. Land Hessen (C.J.E.U.) | International Legal Materials, accessed November 21, 2025, [https://www.cambridge.org/core/journals/international-legal-materials/article/case-c63421-oq-v-land-hessen-cjeu/C47E50588DBD88FD701E9756920CF81D](https://www.cambridge.org/core/journals/international-legal-materials/article/case-c63421-oq-v-land-hessen-cjeu/C47E50588DBD88FD701E9756920CF81D)  
9. Recital 71 \- Profiling \- General Data Protection Regulation (GDPR), accessed November 21, 2025, [https://gdpr-info.eu/recitals/no-71/](https://gdpr-info.eu/recitals/no-71/)  
10. “Major EU AI Banking Ruling Will Reverberate Across Sectors,” Law360, January 12, 2024., accessed November 21, 2025, [https://www.alston.com/en/insights/publications/2024/01/major-eu-ai-banking-ruling-will-reverberate](https://www.alston.com/en/insights/publications/2024/01/major-eu-ai-banking-ruling-will-reverberate)  
11. Azure OpenAI in Azure AI Foundry Models content filtering \- Microsoft Learn, accessed November 21, 2025, [https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter)  
12. How GDPR Affects AI-Powered Social Listening and Sentiment Analysis, accessed November 21, 2025, [https://www.gdpr-advisor.com/how-gdpr-affects-ai-powered-social-listening-and-sentiment-analysis/](https://www.gdpr-advisor.com/how-gdpr-affects-ai-powered-social-listening-and-sentiment-analysis/)  
13. AI Privacy Risks & Mitigations – Large Language Models (LLMs) \- European Data Protection Board, accessed November 21, 2025, [https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf](https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf)  
14. Artificial intelligence-enabled analysis of UK and US public attitudes on Facebook and Twitter towards COVID-19 vaccinations | medRxiv, accessed November 21, 2025, [https://www.medrxiv.org/content/10.1101/2020.12.08.20246231v1.full?6518=](https://www.medrxiv.org/content/10.1101/2020.12.08.20246231v1.full?6518)  
15. A deeper look into cybersecurity issues in the wake of Covid-19: A survey \- PubMed Central, accessed November 21, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9367180/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9367180/)  
16. SAC 056 SSAC Advisory on Impacts of Content Blocking via the Domain Name System \- icann, accessed November 21, 2025, [https://www.icann.org/en/groups/ssac/documents/sac-056-en.pdf](https://www.icann.org/en/groups/ssac/documents/sac-056-en.pdf)  
17. Automated Decisionmaking and Profiling (ADM) Requirements in U.S. State Privacy Laws, and Current State of Play in State AI Regulations \- Centre for Information Policy Leadership, accessed November 21, 2025, [https://www.informationpolicycentre.com/uploads/5/7/1/0/57104281/adm\_profiling\_requirements\_us\_privacy\_law\_cipl\_may24.pdf](https://www.informationpolicycentre.com/uploads/5/7/1/0/57104281/adm_profiling_requirements_us_privacy_law_cipl_may24.pdf)  
18. Automated Decision-Making Under the GDPR: \- The Future of Privacy Forum, accessed November 21, 2025, [https://fpf.org/wp-content/uploads/2022/05/FPF-ADM-Report-R2-singles.pdf](https://fpf.org/wp-content/uploads/2022/05/FPF-ADM-Report-R2-singles.pdf)  
19. Meaningful Human Intervention \- Autoriteit Persoonsgegevens, accessed November 21, 2025, [https://autoriteitpersoonsgegevens.nl/en/system/files?file=2025-03/Consultation%20Meaningful%20Human%20Intervention.pdf](https://autoriteitpersoonsgegevens.nl/en/system/files?file=2025-03/Consultation+Meaningful+Human+Intervention.pdf)  
20. Data (Use and Access) Bill: Automated decision-making in the spotlight \- Latham & Watkins LLP, accessed November 21, 2025, [https://www.lw.com/admin/upload/SiteAttachments/Data-Use-and-Access-Bill-Automated-decision-making-in-the-spotlight.pdf](https://www.lw.com/admin/upload/SiteAttachments/Data-Use-and-Access-Bill-Automated-decision-making-in-the-spotlight.pdf)  
21. Between Humans and Machines: Judicial Interpretation of the Automated Decision-Making Practices in the EU \- Oxford Academic, accessed November 21, 2025, [https://academic.oup.com/book/58128/chapter/479901013](https://academic.oup.com/book/58128/chapter/479901013)  
22. Strengthening legal protection against discrimination by algorithms and artificial intelligence, accessed November 21, 2025, [https://www.tandfonline.com/doi/full/10.1080/13642987.2020.1743976](https://www.tandfonline.com/doi/full/10.1080/13642987.2020.1743976)  
23. AI Regulation Through the Lens of Fundamental Rights: How Well Does the GDPR Address the Challenges Posed by AI? | European Papers, accessed November 21, 2025, [https://www.europeanpapers.eu/europeanforum/ai-regulation-through-the-lens-of-fundamental-rights](https://www.europeanpapers.eu/europeanforum/ai-regulation-through-the-lens-of-fundamental-rights)  
24. Handbook: AI and Public Administration: The (legal) limits of algorithmic governance.docx \- JuLIA Project, accessed November 21, 2025, [https://www.julia-project.eu/sites/default/files/2025-05/Final%20Handbook\_%20AI%20and%20Public%20Administration\_%20The%20%28legal%29%20limits%20of%20algorithmic%20governance.docx.pdf](https://www.julia-project.eu/sites/default/files/2025-05/Final%20Handbook_%20AI%20and%20Public%20Administration_%20The%20%28legal%29%20limits%20of%20algorithmic%20governance.docx.pdf)  
25. The Determining Role of the Schufa Score in Third-Party Decisions, accessed November 21, 2025, [https://paytechlaw.com/en/determining-role-of-schufa-score/](https://paytechlaw.com/en/determining-role-of-schufa-score/)  
26. EU – Cyber liability, automated decisions and other festive updates from the CJEU, accessed November 21, 2025, [https://www.linklaters.com/en-us/insights/blogs/digilinks/2023/december/eu---cyber-liability-automated-decisions-and-other-festive-updates-from-the-cjeu](https://www.linklaters.com/en-us/insights/blogs/digilinks/2023/december/eu---cyber-liability-automated-decisions-and-other-festive-updates-from-the-cjeu)  
27. When Is a Decision Automated? A Taxonomy for a Fundamental Rights Analysis | German Law Journal \- Cambridge University Press & Assessment, accessed November 21, 2025, [https://www.cambridge.org/core/journals/german-law-journal/article/when-is-a-decision-automated-a-taxonomy-for-a-fundamental-rights-analysis/362AF985585D28E5E762F4FEEF4719B7](https://www.cambridge.org/core/journals/german-law-journal/article/when-is-a-decision-automated-a-taxonomy-for-a-fundamental-rights-analysis/362AF985585D28E5E762F4FEEF4719B7)  
28. SCHUFA Holding \- CURIA \- Documents, accessed November 21, 2025, [https://curia.europa.eu/juris/document/document.jsf?docid=280426\&doclang=en](https://curia.europa.eu/juris/document/document.jsf?docid=280426&doclang=en)  
29. Algorithms, Credit Scoring and Data Protection: CJEU Case C-634/21 \- privacy law barrister, accessed November 21, 2025, [https://privacylawbarrister.com/2024/10/21/algorithms-credit-scoring-and-data-protection-cjeu-case-c-634-21/](https://privacylawbarrister.com/2024/10/21/algorithms-credit-scoring-and-data-protection-cjeu-case-c-634-21/)  
30. Algorithms, AI systems and public services: what rights do users have? \- Défenseur des Droits, accessed November 21, 2025, [https://www.defenseurdesdroits.fr/sites/default/files/2025-01/DDD\_rapport\_algorithmes-systemes-d-IA-et-services-publics\_EN\_2024\_20250109.pdf](https://www.defenseurdesdroits.fr/sites/default/files/2025-01/DDD_rapport_algorithmes-systemes-d-IA-et-services-publics_EN_2024_20250109.pdf)  
31. Key takeaways from the CJEU's recent automated decision-making rulings | IAPP, accessed November 21, 2025, [https://iapp.org/news/a/key-takeaways-from-the-cjeus-recent-automated-decision-making-rulings](https://iapp.org/news/a/key-takeaways-from-the-cjeus-recent-automated-decision-making-rulings)  
32. Judicial Review in an Integrated Administration: the Case of 'Composite Procedures', accessed November 21, 2025, [https://www.researchgate.net/publication/273333900\_Judicial\_Review\_in\_an\_Integrated\_Administration\_the\_Case\_of\_'Composite\_Procedures'](https://www.researchgate.net/publication/273333900_Judicial_Review_in_an_Integrated_Administration_the_Case_of_'Composite_Procedures')  
33. “The Judicial review of Regulatory Authorities” Paris, 6 December 2021 Answers to questionnaire: Lithuania \- ACA-Europe, accessed November 21, 2025, [https://www.aca-europe.eu/seminars/2021\_Paris/Lithuania.pdf](https://www.aca-europe.eu/seminars/2021_Paris/Lithuania.pdf)  
34. Reports of Cases \- EUR-Lex, accessed November 21, 2025, [https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:62011TJ0496](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:62011TJ0496)  
35. CJEU confirms preparatory acts can be automated individual decisions: the SCHUFA cases, accessed November 21, 2025, [https://www.twobirds.com/en/insights/2023/global/key-takeaways-from-the-schufa-case-of-the-cjeu](https://www.twobirds.com/en/insights/2023/global/key-takeaways-from-the-schufa-case-of-the-cjeu)  
36. GDPR and AI in 2026: Rules, Risks & Tools That Comply \- Sembly AI, accessed November 21, 2025, [https://www.sembly.ai/blog/gdpr-and-ai-rules-risks-tools-that-comply/](https://www.sembly.ai/blog/gdpr-and-ai-rules-risks-tools-that-comply/)  
37. Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models | Journal of Legal Analysis | Oxford Academic, accessed November 21, 2025, [https://academic.oup.com/jla/article/16/1/64/7699227](https://academic.oup.com/jla/article/16/1/64/7699227)  
38. Large Language Models in Legislative Content Analysis: A Dataset from the Polish Parliament \- arXiv, accessed November 21, 2025, [https://arxiv.org/html/2503.12100v1](https://arxiv.org/html/2503.12100v1)  
39. GDPR and Large Language Models: Technical and Legal Obstacles \- MDPI, accessed November 21, 2025, [https://www.mdpi.com/1999-5903/17/4/151](https://www.mdpi.com/1999-5903/17/4/151)  
40. Legal aspects of generative artificial intelligence and large language models in examinations and theses \- PMC \- NIH, accessed November 21, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11474642/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11474642/)  
41. Does Attorney-Client Privilege Survive When AI Listens? | Corporate Compliance Insights, accessed November 21, 2025, [https://www.corporatecomplianceinsights.com/does-attorney-client-privilege-survive-when-ai-listens/](https://www.corporatecomplianceinsights.com/does-attorney-client-privilege-survive-when-ai-listens/)  
42. AI and You: Confidentiality Risks of Using Transcription and Note-Taking Software During Meetings \- American Bar Association, accessed November 21, 2025, [https://www.americanbar.org/groups/gpsolo/resources/ereport/2025-september/ai-you-confidentiality-risks-meeting-transcription-note-taking-software/](https://www.americanbar.org/groups/gpsolo/resources/ereport/2025-september/ai-you-confidentiality-risks-meeting-transcription-note-taking-software/)  
43. EU's Highest Court Expands EU GDPR Restrictions on Automated Decision-Making, Profiling, and AI \- Morgan Lewis, accessed November 21, 2025, [https://www.morganlewis.com/pubs/2024/02/eus-highest-court-expands-eu-gdpr-restrictions-on-automated-decision-making-profiling-and-ai](https://www.morganlewis.com/pubs/2024/02/eus-highest-court-expands-eu-gdpr-restrictions-on-automated-decision-making-profiling-and-ai)  
44. THE EU INTERNAL MARKET IN THE NEXT DECADE – QUO VADIS? \- OAPEN Library, accessed November 21, 2025, [https://library.oapen.org/bitstream/handle/20.500.12657/98980/9789004712119\_webready\_content\_text.pdf?sequence=1](https://library.oapen.org/bitstream/handle/20.500.12657/98980/9789004712119_webready_content_text.pdf?sequence=1)  
45. Beyond the individual: governing AI's societal harm \- Internet Policy Review, accessed November 21, 2025, [https://policyreview.info/articles/analysis/beyond-individual-governing-ais-societal-harm](https://policyreview.info/articles/analysis/beyond-individual-governing-ais-societal-harm)  
46. IN THE EFTA COURT WRITTEN OBSERVATIONS THE EFTA SURVEILLANCE AUTHORITY IN CASE E-18/24, accessed November 21, 2025, [https://eftacourt.int/wp-content/uploads/2025/05/12\_ESA\_written-observations\_original-2.pdf?x50540](https://eftacourt.int/wp-content/uploads/2025/05/12_ESA_written-observations_original-2.pdf?x50540)  
47. Economic and Social Council Distr.: General \- Official Document System, accessed November 21, 2025, [https://documents.un.org/access.nsf/get?Open\&DS=ECE/MP.PP/2025/55\&Lang=E](https://documents.un.org/access.nsf/get?Open&DS=ECE/MP.PP/2025/55&Lang=E)  
48. Economic and Social Council \- UNECE, accessed November 21, 2025, [https://unece.org/sites/default/files/2025-11/ECE.MP\_.PP\_.2025.5.E.pdf](https://unece.org/sites/default/files/2025-11/ECE.MP_.PP_.2025.5.E.pdf)  
49. Case-law \- CURIA \- Documents \- European Union, accessed November 21, 2025, [https://curia.europa.eu/juris/document/document.jsf?text=\&doclang=EN\&docid=274102](https://curia.europa.eu/juris/document/document.jsf?text&doclang=EN&docid=274102)  
50. Action for annulment of an EU act \- European Parliament, accessed November 21, 2025, [https://www.europarl.europa.eu/RegData/etudes/BRIE/2019/642282/EPRS\_BRI(2019)642282\_EN.pdf](https://www.europarl.europa.eu/RegData/etudes/BRIE/2019/642282/EPRS_BRI\(2019\)642282_EN.pdf)  
51. Administrative law imlications of AI-driven public service delivery \- Law Gratis, accessed November 21, 2025, [https://www.lawgratis.com/blog-detail/administrative-law-imlications-of-ai-driven-public-service-delivery](https://www.lawgratis.com/blog-detail/administrative-law-imlications-of-ai-driven-public-service-delivery)  
52. EIA Directive Procedural Guarantees as Substantive Individual Rights in *IL v. Land Nordrhein-Westfalen*, accessed November 21, 2025, [https://repository.law.umich.edu/cgi/viewcontent.cgi?article=1123\&context=mjeal](https://repository.law.umich.edu/cgi/viewcontent.cgi?article=1123&context=mjeal)  
53. What does the UK GDPR say about automated decision-making and profiling? | ICO, accessed November 21, 2025, [https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/automated-decision-making-and-profiling/what-does-the-uk-gdpr-say-about-automated-decision-making-and-profiling/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/automated-decision-making-and-profiling/what-does-the-uk-gdpr-say-about-automated-decision-making-and-profiling/)  
54. Legal Pathways for Platform Accountability in Europe \- Digital Freedom Fund, accessed November 21, 2025, [https://digitalfreedomfund.org/support/resources-page/legal-pathways-for-platform-accountability-in-europe/](https://digitalfreedomfund.org/support/resources-page/legal-pathways-for-platform-accountability-in-europe/)  
55. Humans in automated decision-making under the GDPR and AI Act \- CIDOB, accessed November 21, 2025, [https://www.cidob.org/en/publications/humans-automated-decision-making-under-gdpr-and-ai-act](https://www.cidob.org/en/publications/humans-automated-decision-making-under-gdpr-and-ai-act)  
56. Co-Governance and the Future of AI Regulation \- Harvard Law Review, accessed November 21, 2025, [https://harvardlawreview.org/print/vol-138/co-governance-and-the-future-of-ai-regulation/](https://harvardlawreview.org/print/vol-138/co-governance-and-the-future-of-ai-regulation/)  
57. Reboot Democracy \- AI for Participatory Democracy, accessed November 21, 2025, [https://rebootdemocracy.ai/](https://rebootdemocracy.ai/)  
58. Data and Democracy in the Digital Age \- The Constitution Society, accessed November 21, 2025, [https://www.consoc.org.uk/wp-content/uploads/2018/07/Stephanie-Hankey-Julianne-Kerr-Morrison-Ravi-Naik-Data-and-Democracy-in-the-Digital-Age.pdf](https://www.consoc.org.uk/wp-content/uploads/2018/07/Stephanie-Hankey-Julianne-Kerr-Morrison-Ravi-Naik-Data-and-Democracy-in-the-Digital-Age.pdf)  
59. What is automated individual decision-making and profiling? | ICO, accessed November 21, 2025, [https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/automated-decision-making-and-profiling/what-is-automated-individual-decision-making-and-profiling/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/automated-decision-making-and-profiling/what-is-automated-individual-decision-making-and-profiling/)  
60. Art. 4 GDPR – Definitions \- General Data Protection Regulation (GDPR), accessed November 21, 2025, [https://gdpr-info.eu/art-4-gdpr/](https://gdpr-info.eu/art-4-gdpr/)  
61. Sentiment analysis in public health: a systematic review of the current state, challenges, and future directions \- Frontiers, accessed November 21, 2025, [https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1609749/full](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1609749/full)  
62. GDPR and unstructured data: is anonymization possible? \- Oxford Academic, accessed November 21, 2025, [https://academic.oup.com/idpl/article/12/3/184/6552802](https://academic.oup.com/idpl/article/12/3/184/6552802)  
63. Regulation of Social Media and Elections in Europe, accessed November 21, 2025, [https://journalismresearch.org/2024/12/regulation-of-social-media-and-elections-in-europe/](https://journalismresearch.org/2024/12/regulation-of-social-media-and-elections-in-europe/)  
64. Affective Computing and Emotional Data: Challenges and Implications in Privacy Regulations, The AI Act, and Ethics in Large Language Models \- arXiv, accessed November 21, 2025, [https://arxiv.org/html/2509.20153v2](https://arxiv.org/html/2509.20153v2)  
65. EDPS Opinion on online manipulation and personal data, accessed November 21, 2025, [https://www.edps.europa.eu/sites/default/files/publication/18-03-19\_online\_manipulation\_en.pdf](https://www.edps.europa.eu/sites/default/files/publication/18-03-19_online_manipulation_en.pdf)  
66. Art. 22 GDPR – Automated individual decision-making, including profiling \- General Data Protection Regulation (GDPR), accessed November 21, 2025, [https://gdpr-info.eu/art-22-gdpr/](https://gdpr-info.eu/art-22-gdpr/)  
67. Article No.22 \- UK GDPR \- Mishcon de Reya, accessed November 21, 2025, [https://www.mishcon.com/uk-gdpr/article-22](https://www.mishcon.com/uk-gdpr/article-22)  
68. Biometrics in the EU: Navigating the GDPR, AI Act \- IAPP, accessed November 21, 2025, [https://iapp.org/news/a/biometrics-in-the-eu-navigating-the-gdpr-ai-act](https://iapp.org/news/a/biometrics-in-the-eu-navigating-the-gdpr-ai-act)  
69. Political Parties and Data Profiling: Who Do They Think We Are? | Open Rights Group, accessed November 21, 2025, [https://www.openrightsgroup.org/publications/who-do-they-think-we-are-report/](https://www.openrightsgroup.org/publications/who-do-they-think-we-are-report/)  
70. Teachers in the loop? An analysis of automatic assessment systems under Article 22 GDPR | International Data Privacy Law | Oxford Academic, accessed November 21, 2025, [https://academic.oup.com/idpl/article/14/1/3/7451152](https://academic.oup.com/idpl/article/14/1/3/7451152)  
71. Automated Decision-Making Systems in German Administrative Law \- CERIDAP, accessed November 21, 2025, [https://ceridap.eu/automated-decision-making-systems-in-german-administrative-law/](https://ceridap.eu/automated-decision-making-systems-in-german-administrative-law/)  
72. Artificial Intelligence and Administrative Discretion: Exploring Adaptations and Boundaries, accessed November 21, 2025, [https://www.researchgate.net/publication/385191954\_Artificial\_Intelligence\_and\_Administrative\_Discretion\_Exploring\_Adaptations\_and\_Boundaries](https://www.researchgate.net/publication/385191954_Artificial_Intelligence_and_Administrative_Discretion_Exploring_Adaptations_and_Boundaries)  
73. A Kratt as an Administrative Body: Algorithmic Decisions and Principles of Administrative Law \- Juridica International, accessed November 21, 2025, [https://www.juridicainternational.eu/public/pdf/ji\_2020\_29\_47.pdf](https://www.juridicainternational.eu/public/pdf/ji_2020_29_47.pdf)  
74. Fully Automated Administrative Acts in the German Legal System\*, accessed November 21, 2025, [https://www.erdalreview.eu/free-download/978882553896011.pdf](https://www.erdalreview.eu/free-download/978882553896011.pdf)  
75. Legal Regulation of AI and Automated Decision-making in the Public Sector \- ANU Library, accessed November 21, 2025, [https://library-admin.anu.edu.au/intranet/publications-presentations/SIS-all-staff-meetings/files/2024-Symposium-Legal-Regulation-AI.pdf](https://library-admin.anu.edu.au/intranet/publications-presentations/SIS-all-staff-meetings/files/2024-Symposium-Legal-Regulation-AI.pdf)  
76. The Judicial Review of the Automated Administrative Act\*, accessed November 21, 2025, [https://www.erdalreview.eu/free-download/97888255389609.pdf](https://www.erdalreview.eu/free-download/97888255389609.pdf)  
77. Artificial Intelligence 2025 \- France | Global Practice Guides \- Chambers and Partners, accessed November 21, 2025, [https://practiceguides.chambers.com/practice-guides/artificial-intelligence-2025/france](https://practiceguides.chambers.com/practice-guides/artificial-intelligence-2025/france)  
78. Rethinking Administrative Law for Algorithmic Decision Making \- PMC \- NIH, accessed November 21, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9126137/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9126137/)  
79. Closing Note on the Strategic Initiative on how the European Commission decides on and uses artificial intelligence (SI/4/2024/MIK), accessed November 21, 2025, [https://www.ombudsman.europa.eu/de/doc/correspondence/en/196934](https://www.ombudsman.europa.eu/de/doc/correspondence/en/196934)  
80. Melanie Fink Presents on 'Good Administration in the Age of AI' at the European Ombudsman \- Universiteit Leiden, accessed November 21, 2025, [https://www.universiteitleiden.nl/en/news/2025/06/melanie-fink-presents-on-good-administration-in-the-age-of-ai-at-the-european-ombudsman](https://www.universiteitleiden.nl/en/news/2025/06/melanie-fink-presents-on-good-administration-in-the-age-of-ai-at-the-european-ombudsman)  
81. Annex III: High-Risk AI Systems Referred to in Article 6(2) | EU Artificial Intelligence Act, accessed November 21, 2025, [https://artificialintelligenceact.eu/annex/3/](https://artificialintelligenceact.eu/annex/3/)  
82. High-level summary of the AI Act | EU Artificial Intelligence Act, accessed November 21, 2025, [https://artificialintelligenceact.eu/high-level-summary/](https://artificialintelligenceact.eu/high-level-summary/)  
83. AI Act Service Desk \- Annex III \- European Union, accessed November 21, 2025, [https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3)  
84. AI Act Service Desk \- Article 27: Fundamental rights impact assessment for high-risk AI systems, accessed November 21, 2025, [https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27)  
85. Recital 96 \- Implementation of fundamental rights impact assessment and further follow-up measures \- AI Act, accessed November 21, 2025, [https://ai-act-law.eu/recital/96/](https://ai-act-law.eu/recital/96/)  
86. Public Authorities: What Role in the AI Act? \- Center for Democracy and Technology, accessed November 21, 2025, [https://cdt.org/insights/public-authorities-what-role-in-the-ai-act/](https://cdt.org/insights/public-authorities-what-role-in-the-ai-act/)  
87. Fundamental Rights Impact Assessments under the EU AI Act: Who, what and how? | Technology's Legal Edge, accessed November 21, 2025, [https://www.technologyslegaledge.com/2024/03/fundamental-rights-impact-assessments-under-the-eu-ai-act-who-what-and-how/](https://www.technologyslegaledge.com/2024/03/fundamental-rights-impact-assessments-under-the-eu-ai-act-who-what-and-how/)  
88. European Ombudsman makes suggestions to help ensure accountability in Commission's use of AI \- IOI News, accessed November 21, 2025, [https://www.theioi.org/ioi-news/current-news/european-ombudsman-makes-suggestions-to-help-ensure-accountability-in-commission-s-use-of-ai](https://www.theioi.org/ioi-news/current-news/european-ombudsman-makes-suggestions-to-help-ensure-accountability-in-commission-s-use-of-ai)  
89. European Commission breaches own AI guidelines by using ChatGPT in public documents, accessed November 21, 2025, [https://www.iccl.ie/news/european-commission-breaches-own-ai-guidelines-by-using-chatgpt-in-public-documents/](https://www.iccl.ie/news/european-commission-breaches-own-ai-guidelines-by-using-chatgpt-in-public-documents/)  
90. The Pan-European General Principles on Digitalisation of Public Administration, E-Government and (Semi-) Automated Administrative Decision-Making Processes \- ReNEUAL, accessed November 21, 2025, [http://www.reneual.eu/projects-and-publications/reneual-2-0?view=article\&id=31\&catid=2](http://www.reneual.eu/projects-and-publications/reneual-2-0?view=article&id=31&catid=2)