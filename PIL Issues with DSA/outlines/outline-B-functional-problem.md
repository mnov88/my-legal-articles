# Outline B: The functional problem approach

Analytical flow: What does Article 54 require PIL to accomplish? → How does the current PIL framework perform each function? → Where does performance fail? → What explains the failure? → How have analogous regimes solved equivalent problems?

---

## 1. Introduction: what must PIL accomplish for DSA private enforcement?

Article 54 DSA creates a compensation right. For this right to be effective, PIL must accomplish four functions.

First, allocate judicial competence — determine which courts can hear DSA claims. Second, designate applicable law — determine which national tort law governs the compensation claim. Third, enable claim aggregation — allow related claims to be heard together efficiently. Fourth, facilitate recognition and enforcement — ensure judgments are effective cross-border.

This outline analyzes whether current PIL performs these functions for DSA private enforcement.

---

## 2. Allocating judicial competence

### 2.1 The function

Jurisdiction rules should balance three objectives. Claimant access — victims should be able to sue in a forum that is practically accessible. Defendant predictability — defendants should be able to anticipate where they may be sued. Adjudicative quality — courts with proximity to relevant facts should have priority.

For DSA claims by users against platforms, these objectives point in different directions. Claimant access suggests user's residence. Defendant predictability suggests platform's establishment. Adjudicative quality is unclear — digital evidence is location-agnostic.

### 2.2 Current PIL performance

Brussels I bis provides three bases for DSA claims.

Defendant's domicile (Article 4) satisfies defendant predictability but fails claimant access. Major platforms are established in Ireland. A Bulgarian user suing Meta must litigate in Dublin — expensive, unfamiliar, procedurally foreign.

Special tort jurisdiction (Article 7(2)) partially addresses claimant access. The "place where damage occurred" allows suit where the user suffered harm — usually their residence. But CJEU interpretation creates problems. Shevill's mosaic approach limits recovery to local damage unless suing at defendant's domicile. eDate's centre-of-interests exception applies only to natural persons' personality rights. Gtflix denied legal persons this benefit. Business users cannot sue at their centre of interests for full damage.

Consumer jurisdiction (Articles 17-19) provides claimant access for consumers. Article 18(1) allows consumers to sue "where the consumer is domiciled." But this requires characterizing DSA claims as "matters relating to a contract" — contested for statutory breach-of-duty claims. And it excludes business users entirely.

### 2.3 Where performance fails

Failure 1: Business user exclusion. The DSA protects all "recipients of the service" (Article 3(b)) — consumers and business users alike. Article 54 makes no distinction. But Brussels I bis consumer jurisdiction excludes business users. A small trader suspended from a marketplace cannot sue at home unless they establish Article 7(2) jurisdiction for full damage — which requires proving personality rights are at stake and they are a natural person.

Failure 2: Ireland concentration. For any claim that cannot invoke consumer jurisdiction or Article 7(2) full-damage jurisdiction, the defendant's domicile is the only option. This concentrates all non-consumer, non-personality-rights DSA litigation against VLOPs in Ireland. Irish courts become the de facto exclusive forum for DSA private enforcement.

Failure 3: Characterization uncertainty. Whether DSA claims qualify for consumer jurisdiction depends on characterization as "contractual." Platform-user relationships involve contracts (Terms of Service) but Article 54 creates a statutory right for breach of regulatory obligations. CJEU has not resolved whether statutory claims arising from contractual relationships fall within Articles 17-19. Claimants face threshold uncertainty before reaching the merits.

### 2.4 What explains the failure?

Brussels I bis was designed for traditional territorial disputes. Its connecting factors — domicile, place of harmful event, consumer contracts — presuppose geographically bounded conduct.

Digital services are not geographically bounded. A platform's decision — algorithm change, policy update, moderation action — occurs at its establishment but affects users across all markets simultaneously. The traditional connecting factors cannot capture this ubiquitous character.

The CJEU recognized this in eDate when creating the centre-of-interests ground for online personality rights. But that adaptation was narrow — natural persons, personality rights only. DSA claims by legal persons for non-personality harms remain governed by pre-internet connecting factors.

### 2.5 Analogous solutions

GDPR Article 79(2) directly addresses the problem. Data subjects can sue "before the courts of the Member State where the data subject has his or her habitual residence." This creates forum actoris — claimant's choice of home forum — without requiring characterization as contract or personality rights.

Recital 147 GDPR confirms that Article 79(2) "should be interpreted in accordance with the objectives of this Regulation" — i.e., effective protection.

This model could be transposed to DSA. An "Article 54(2)" providing jurisdiction at recipient's habitual residence would accomplish the claimant-access function without current failures.

DMA lacks equivalent provision. Private enforcement of DMA obligations faces identical jurisdictional concentration.

---

## 3. Designating applicable law

### 3.1 The function

Choice of law rules should accomplish two objectives. Predictability — parties should be able to identify in advance which law governs their relationship. Alignment with regulatory purpose — applicable law should support the substantive goals of the regulation creating the right.

For DSA, the regulatory purpose is uniform platform obligations across the internal market. Private enforcement should reinforce this uniformity, not fragment it.

### 3.2 Current PIL performance

Rome II Article 4(1) designates lex loci damni — the law of the country where damage occurs. For DSA claims, this is typically the claimant's residence.

This initially appears claimant-friendly: users sue under their home tort law. But problems emerge with cross-border application.

A platform's single DSA breach — say, failure to provide statement of reasons under Article 20 — affects users across all Member States. Under Rome II, each user's claim is governed by their respective national law. Twenty-seven different tort regimes govern compensation for the identical regulatory breach.

### 3.3 Where performance fails

Failure 1: Fragmentation despite uniform obligation. The DSA creates uniform obligations — Article 14 applies identically to platforms regardless of where their users are located. But Rome II fragments liability: German tort law governs German users' claims, French tort law governs French users' claims. The platform faces 27 different standards for what compensation is owed for the same breach.

This inverts the country-of-origin principle. DSA supervision is centralized — Ireland's Digital Services Coordinator supervises Meta under Article 56(1). But liability is decentralized — each destination state's tort law governs compensation.

Failure 2: Personality rights exclusion. Rome II Article 1(2)(g) excludes "violations of privacy and rights relating to personality, including defamation." Many DSA claims implicate personality: wrongful content removal damaging reputation, discriminatory algorithmic treatment, publication of personal information through inadequate moderation.

These claims fall outside Rome II entirely. National PIL rules — divergent and unharmonized — determine applicable law. A French user's personality-rights claim may be governed by French PIL rules; a German user's by German PIL rules. The same platform breach triggers different applicable-law methodologies.

Failure 3: Pure economic loss divergence. DSA claims frequently involve pure economic loss — revenue decline from suspension, earnings drop from reduced visibility. National tort laws diverge fundamentally on pure economic loss recovery.

German law (§ 823(1) BGB) requires interference with an enumerated right or breach of a protective statute (Schutzgesetz). Whether DSA Article 54 qualifies as Schutzgesetz under German characterization is uncertain. French law (Article 1240 Code civil) has no such restriction. Under Rome II's lex loci damni, a German user may have no claim where a French user would recover.

### 3.4 What explains the failure?

Rome II was negotiated without digital services in mind. The lex loci damni rule reflects a territorial sovereignty compromise — each state governs harm within its borders. This works for geographically bounded torts: a car accident in Germany is governed by German law.

Digital services tort is not geographically bounded. A platform decision made in Ireland affects users in Germany, France, and Poland simultaneously. Lex loci damni does not select a single applicable law — it selects 27.

The Article 1(2)(g) exclusion reflects failed harmonization attempts. Member States could not agree on uniform personality rights rules in the early 2000s. The exclusion deferred the problem. Twenty years later, online personality harms are ubiquitous and the exclusion creates a gap at the centre of digital services liability.

### 3.5 Analogous solutions

GDPR does not solve applicable law — it creates uniform substantive rights directly applicable in all Member States. The "applicable law" question shifts from which tort law governs to which national implementation of GDPR applies. Since GDPR is maximally harmonized, divergence is minimal.

DSA takes the same approach for substantive obligations — directly applicable, uniform across Member States. But Article 54 defers to national law for the compensation remedy. National tort laws are not harmonized. The uniform-obligation / non-uniform-remedy structure creates the fragmentation.

Competition law private damages under the Damages Directive 2014/104 harmonize certain aspects — limitation periods, burden of proof, joint liability. This partial harmonization reduces divergence even where Rome II designates different national laws. A "DSA Damages Directive" could similarly harmonize remedial aspects.

Rome II Article 6(3)(b) allows claimants suing at defendant's domicile to choose forum law for competition claims if the market is directly and substantially affected there. A similar option for DSA — allowing claimants to choose law of platform's establishment — would reduce fragmentation by enabling single-law adjudication.

---

## 4. Enabling claim aggregation

### 4.1 The function

Claim aggregation serves efficiency and coherence. Efficiency: related claims heard together avoid duplicative proceedings. Coherence: unified adjudication prevents contradictory outcomes on the same facts.

For DSA, aggregation matters in two contexts. Multi-party claims — many users affected by the same platform breach. Multi-basis claims — single user invoking DSA alongside GDPR, copyright, or other regimes.

### 4.2 Current PIL performance

Brussels I bis Article 8(1) permits joinder of claims against multiple defendants if "so closely connected that it is expedient to hear and determine them together to avoid the risk of irreconcilable judgments."

CJEU interpretation in CDC Hydrogen Peroxide (C-352/13) applied this liberally for competition damages — cartel members could be sued together. Roche Nederland (C-539/03) applied it restrictively for IP — different national patent rights were not sufficiently connected. Freeport (C-98/06) held that different legal bases (contract/tort) do not preclude joinder if facts are shared.

Brussels I bis Article 30 addresses related actions pending in different courts — allowing stay or decline of jurisdiction to avoid inconsistent outcomes.

Rome II Article 4(3) escape clause allows departure from lex loci damni where the tort is "manifestly more closely connected" with another country — potentially enabling single-law treatment for multi-state damage.

### 4.3 Where performance fails

Failure 1: Collective action jurisdiction gap. The Representative Actions Directive (EU) 2020/1828 enables qualified entities to bring collective actions for DSA violations (DSA Article 86). But Brussels I bis contains no collective action jurisdiction rule.

Qualified entities are not consumers — they cannot invoke Articles 17-19. They are not natural persons with personality rights — they cannot invoke eDate centre-of-interests. They must sue at defendant's domicile (Article 4) or fragment under Article 7(2) mosaic approach.

For EU-wide collective DSA claims against VLOPs, this means all roads lead to Ireland. Cross-border collective redress requires litigating in the defendant's home forum — undermining the access-to-justice rationale for collective mechanisms.

Failure 2: Multi-basis claim uncertainty. A user suing a platform for account suspension may have claims under DSA (inadequate reasons), GDPR (automated decision-making), and contract (Terms of Service breach). Each claim has its own PIL framework.

DSA claim: Brussels I bis general rules. GDPR claim: Article 79(2) special jurisdiction at habitual residence. Contract claim: Articles 17-19 if consumer, Article 7(1) if not.

Can these be heard together? Article 8(1) joinder requires "close connection." Whether claims with different legal bases against the same defendant for the same conduct satisfy this test is uncertain. Freeport suggests yes; Roche suggests limits where different laws apply.

If joinder fails, the user must bring separate proceedings — DSA claim in one forum, GDPR claim in another. This defeats aggregation efficiency and risks inconsistent outcomes.

Failure 3: Applicable law fragmentation for collective claims. Even if collective actions achieve jurisdictional aggregation (all claims in one court), Rome II fragments applicable law. A qualified entity representing users from 15 Member States must prove the DSA claim under 15 different national tort laws.

Practical adjudication becomes complex. The court must apply German law to German users, French law to French users, etc. — determining liability standards, damages calculation, and limitation periods separately for each national cohort.

### 4.4 What explains the failure?

Joinder rules presuppose discrete defendants and discrete claims. Article 8(1) addresses suing "a number of defendants" — multiple parties in the same proceeding. It does not address suing one defendant on behalf of many claimants.

Collective redress is structurally different: one action, many claimants, one defendant. Brussels I bis has no rule for this configuration.

The Representative Actions Directive did not fill this gap. RAD created substantive standing for qualified entities but did not create PIL rules. The Commission's proposal (COM(2018) 184) contained no jurisdiction article; the final Directive likewise omitted PIL.

This omission may reflect political constraints — Member States disagreed on collective action jurisdiction — or oversight — PIL implications were not fully analyzed. Either way, the result is a collective redress mechanism (RAD + DSA Article 86) without jurisdictional infrastructure.

### 4.5 Analogous solutions

U.S. federal class actions under FRCP 23 have nationwide jurisdiction once class certification is granted. The certifying court adjudicates all class members' claims under choice-of-law rules that may designate single or multiple state laws. This model is foreign to EU PIL but demonstrates that collective action and PIL can be structurally integrated.

Competition law collective actions have proceeded under CDC Hydrogen Peroxide's liberal joinder approach. Cartel damages claims by multiple purchasers against multiple cartelists have been aggregated in single proceedings. This suggests Article 8(1) can accommodate some multi-party configurations.

A Brussels I bis revision creating collective action jurisdiction — allocating competence to courts of the defendant's domicile or principal place of affected activity — would address the gap. The Commission's 2025 Brussels I bis Report (mandated by Article 79) may recommend such revision.

---

## 5. Recognition and enforcement

### 5.1 The function

Judgments must be enforceable where defendants have assets. For platforms established in one Member State (Ireland) with assets in others (bank accounts, data centres, subsidiaries), recognition and enforcement rules determine practical effectiveness.

### 5.2 Current PIL performance

Brussels I bis Chapter III provides for automatic recognition (Article 36) and streamlined enforcement (Articles 39-44). Judgments from one Member State are enforceable in others without exequatur.

This functions well for DSA. An Irish judgment against Meta is enforceable across the EU. A French judgment against a French subsidiary is likewise enforceable.

### 5.3 Where performance fails

Limited failures in this area. Brussels I bis recognition/enforcement rules work as designed.

One edge issue: judgments based on exorbitant national jurisdiction (where Brussels I bis does not apply) may face recognition challenges. For DSA claims against non-EU platforms (e.g., X/Twitter's uncertain establishment status), national exorbitant rules may apply. Resulting judgments may face Article 45 refusal grounds in other Member States.

### 5.4 What explains the performance?

Recognition and enforcement were the first PIL domain harmonized in the EU (1968 Brussels Convention). Decades of refinement produced robust rules. Unlike jurisdiction and applicable law — where digital services create novel problems — recognition and enforcement rules are technology-neutral.

---

## 6. Synthesis: functional deficits and reform options

### 6.1 Summary of performance

Allocating judicial competence: Partial failure. Consumer jurisdiction works for consumer claimants who can characterize claims as contractual. Article 7(2) works for natural persons with personality rights claims. Business users and legal persons face Ireland concentration.

Designating applicable law: Systematic failure. Rome II fragments liability into 27 regimes. Personality rights exclusion creates gaps. Pure economic loss divergence produces outcome divergence for identical breaches.

Enabling claim aggregation: Structural failure. No collective action jurisdiction. Multi-basis claim joinder uncertain. Applicable law fragmentation defeats collective efficiency.

Recognition and enforcement: Functional success. Brussels I bis Chapter III works as designed.

### 6.2 Reform options by function

For judicial competence: Autonomous DSA jurisdiction rule modeled on GDPR Article 79(2). Recipients can sue at their habitual residence or at platform's establishment.

For applicable law: Two approaches. First, Rome II revision to (a) include personality rights within scope, (b) create special rule for digital services (e.g., law of recipient's habitual residence or platform's establishment at claimant's option). Second, partial harmonization directive for DSA damages — limitation periods, burden of proof, damages floor — reducing divergence even if Rome II designates different national laws.

For claim aggregation: Brussels I bis revision creating collective action jurisdiction. Qualified entities can sue at defendant's domicile or principal place of affected activity. Rome II revision allowing single applicable law for collective claims — either law of forum or law of defendant's habitual residence.

### 6.3 Likelihood of reform

Rome II revision: The Commission's January 2025 Report identified online torts and multi-jurisdictional damage as problems requiring "further in-depth analysis." This signals possible legislative proposal, though timelines are uncertain.

Brussels I bis revision: Article 79 mandates Commission report on application. The 2025 report may recommend collective action jurisdiction provisions.

DSA-specific rules: Amendment to DSA adding Article 54(2) jurisdiction provision would be fastest path. Does not require reopening Rome II or Brussels I bis. Political appetite uncertain — DSA recently adopted, Member States may resist early amendment.

---

## 7. Conclusion

The DSA's PIL framework fails two of three core functions. Judicial competence allocation excludes business users and concentrates non-consumer litigation in Ireland. Applicable law designation fragments liability despite uniform obligations. Claim aggregation lacks jurisdictional infrastructure and faces applicable law fragmentation.

These failures are not incidental. They reflect structural mismatch between general PIL rules — designed for territorial disputes — and digital services regulation — governing ubiquitous cross-border conduct.

Reform requires either autonomous DSA PIL rules (following GDPR's Article 79(2) model) or revision of general PIL instruments to accommodate digital services. The former is faster; the latter is more comprehensive. Either path requires recognizing that Article 54's compensation right is incomplete without PIL infrastructure adequate to its purpose.
