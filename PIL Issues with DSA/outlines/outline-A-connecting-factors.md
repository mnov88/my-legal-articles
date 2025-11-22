# Outline A: The connecting factors approach

Analytical flow: Which PIL standards apply → Why they apply (the deferral mechanism) → How CJEU interprets them → Why application to DSA is difficult → Do solutions from other regimes translate?

---

## 1. Introduction: the PIL deferral in DSA

The DSA creates Article 54 compensation rights but contains no autonomous PIL rules. Article 2(2)(h) and Recital 126 defer entirely to Brussels I bis and Rome II. This deferral raises a question: do general PIL connecting factors work for a digital services regulation designed around the country-of-origin principle?

---

## 2. Jurisdiction: the connecting factors under Brussels I bis

### 2.1 What are the applicable connecting factors?

Three jurisdictional bases available to DSA claimants under Brussels I bis.

First, defendant's domicile under Article 4. Second, "place where the harmful event occurred" under Article 7(2). Third, consumer's domicile under Articles 17-19 if conditions met.

DSA adds no special rule. Contrast with GDPR Article 79(2), which creates autonomous jurisdiction at data subject's habitual residence.

### 2.2 Why these connecting factors exist

Article 4 reflects actor sequitur forum rei — the defendant's expectation of being sued at home. Article 7(2) reflects proximity — courts nearest to the tort have evidentiary advantages. Articles 17-19 reflect protective policy — weaker party sues at home.

None of these rationales were designed for ubiquitous digital services operating from a single establishment across 27 markets.

### 2.3 CJEU interpretation of Article 7(2) for online torts

The "place where the harmful event occurred" has been interpreted in a line of cases.

Shevill (C-68/93): Bifurcation into Handlungsort (place of event) and Erfolgsort (place of damage). For cross-border defamation, claimant can sue at publisher's establishment for full damage or in each distribution state for local damage only — the "mosaic" approach.

eDate Advertising (C-509/09, C-161/10): For online personality rights of natural persons, additional ground created — "centre of interests" (usually habitual residence) with jurisdiction for full damage. Justified by the ubiquitous nature of internet publication.

Bolagsupplysningen (C-194/16): Centre of interests denied to legal persons. Companies must use mosaic approach or sue at defendant's domicile.

Gtflix TV (C-251/20): Reaffirmed mosaic for legal persons. Each Member State court has jurisdiction only for damage occurring in its territory.

### 2.4 Difficulty applying these connecting factors to DSA claims

The "Ireland problem." Major platforms — Meta, Google, TikTok, Apple — have EU headquarters in Ireland. Under Article 4, all claims against these platforms default to Irish courts unless special jurisdiction applies.

Article 7(2) Handlungsort provides no escape: the algorithmic decisions, content moderation policies, and system designs occur at the platform's establishment. The event giving rise to damage is in Ireland.

Article 7(2) Erfolgsort creates fragmentation. For a platform decision affecting users across all Member States — say, a change to recommendation algorithms — damage occurs everywhere simultaneously. The mosaic approach forces claimants to either sue in Ireland for full damage or fragment claims across 27 courts for local damage only.

Consumer jurisdiction (Articles 17-19) requires characterization of DSA claims as "matters relating to a contract." Platform-user relationships are contractual (Terms of Service), but Article 54 creates a statutory tort remedy for breach of regulatory obligations. Whether this qualifies as a "contract" under Article 17 is unsettled. The CJEU has not addressed whether statutory breach-of-duty claims arising from a contractual relationship fall within consumer jurisdiction.

The "prosumer" problem. Article 17 applies only to persons acting outside their trade or profession. Influencers, small traders, and gig workers using platforms occupy an ambiguous status. If classified as professionals, they lose consumer protective jurisdiction.

### 2.5 Do solutions from other regimes work?

GDPR Article 79(2) creates forum actoris: data subjects can sue at their habitual residence regardless of controller's establishment. This rule was specifically designed for cross-border data processing. DSA did not adopt this model despite identical cross-border dynamics.

Competition law private damages under Regulation 1/2003 and the Damages Directive use general Brussels I bis rules. CJEU in CDC Hydrogen Peroxide (C-352/13) located damage at the claimant's registered office where the affected market is. This "market effects" approach could inform DSA interpretation — the "damage" from a platform's DSA breach occurs where the claimant operates.

Copyright Directive Article 17 claims use Brussels I bis Article 7(2). CJEU in Pinckney (C-170/12) and Hejduk (C-441/13) allowed jurisdiction wherever infringing content is accessible. This accessibility test could extend to DSA — jurisdiction wherever the platform's service is accessible and damage occurs.

None of these solutions address the core problem: DSA claimants without GDPR overlap and without consumer status face the Ireland default.

---

## 3. Applicable law: the connecting factors under Rome II

### 3.1 What are the applicable connecting factors?

Rome II Article 4(1) provides the general rule: lex loci damni — the law of the country where damage occurs, regardless of where the event giving rise to damage occurred.

Article 4(2) provides an exception for common habitual residence. Article 4(3) provides an escape clause for manifestly closer connection.

Special rules exist for product liability (Article 5), unfair competition (Article 6), and intellectual property (Article 8).

Article 1(2)(g) excludes "violations of privacy and rights relating to personality, including defamation."

### 3.2 Why these connecting factors exist

Lex loci damni under Article 4(1) represents a compromise between territorial sovereignty (each state governs harm within its borders) and victim protection (victim sues under familiar home law if that's where damage occurred).

The exclusion in Article 1(2)(g) exists because Member States could not agree on harmonization of personality rights — national laws diverge fundamentally on privacy, defamation, and reputation.

### 3.3 Interpretation in cross-border tort cases

The CJEU has interpreted "damage" narrowly under Rome II.

Lazar (C-350/14): Direct damage controls, not indirect financial consequences. For DSA, this means the immediate harm from the platform's breach (account suspension, content removal) determines applicable law, not downstream economic losses.

Florin Lazar further clarified that the "place of damage" is where the harmful effects of the wrongful act are felt, not where consequential financial loss materializes.

For ubiquitous online harms, Rome II provides less guidance than Brussels I bis. The CJEU has not addressed whether the eDate "centre of interests" approach applies to applicable law as well as jurisdiction.

### 3.4 Difficulty applying to DSA claims

The fragmentation paradox. DSA establishes country-of-origin supervision under Article 56(1) — the Digital Services Coordinator of the Member State of establishment has primary regulatory authority. Ireland supervises Meta; Luxembourg supervises Amazon.

Rome II creates country-of-destination liability. A platform's single policy decision — say, an advertising transparency failure under Article 26 — triggers 27 different applicable laws for compensation claims. A French user's claim is governed by French tort law; a Polish user's by Polish law.

This creates an inversion: regulatory compliance is assessed under one law (Ireland's DSA implementation), but civil liability for the same breach is assessed under 27 different national tort regimes.

The personality rights exclusion. Article 1(2)(g) excludes privacy and personality rights from Rome II's scope. Many DSA claims — wrongful content removal damaging reputation, discriminatory algorithmic treatment, doxxing through inadequate moderation — implicate personality rights. These claims fall outside harmonized PIL rules entirely, reverting to divergent national PIL regimes.

The Commission's January 2025 Report on Rome II (COM(2025) 20 final) identified "cases where damage occurs simultaneously in many jurisdictions" and "torts committed online" as requiring "further in-depth analysis."

Pure economic loss. DSA claims frequently involve pure economic loss — a trader's revenue decline from suspension, an influencer's earnings drop from shadowbanning. National tort laws diverge sharply on pure economic loss recovery. German law (§ 823(1) BGB) restricts recovery unless a specific "protective law" (Schutzgesetz) is breached. French law is more permissive. Under Rome II, whether Article 54 DSA qualifies as a Schutzgesetz depends on which national law applies — the classification is circular.

### 3.5 Do solutions from other regimes work?

GDPR does not create its own applicable law rule but the directly applicable nature of the Regulation means the substantive right is uniform; only remedial quantification differs.

Rome II Article 6(3) for competition law allows claimants suing at defendant's domicile to choose forum law if the market there is "directly and substantially affected." This claimant-friendly choice could be extended to DSA claims — allowing claimants in Ireland to apply Irish law even if damage occurred elsewhere.

Rome II Article 5 for product liability creates a cascade favoring consumer's habitual residence if the product was marketed there. A similar cascade for digital services — prioritizing user's habitual residence if service was directed there — would align PIL with DSA's market-access principle.

Rome II Article 8 for IP uses lex loci protectionis — the law of the country for which protection is claimed. This territorial approach is unsuitable for DSA because digital services are not territorially bounded like IP rights.

---

## 4. Joinder and multi-claim scenarios: when connecting factors collide

### 4.1 The problem of overlapping regimes

A single platform decision frequently breaches multiple instruments. Account suspension based on automated profiling may violate DSA Article 14 (content moderation), DSA Article 20 (statement of reasons), GDPR Article 22 (automated decision-making), and GDPR Article 82 (compensation). Content removal may breach DSA Article 16 and Copyright Directive Article 17(9).

Each claim has its own PIL framework. DSA uses general Brussels I bis and Rome II. GDPR has Article 79(2) special jurisdiction. Copyright uses Rome II Article 8 lex loci protectionis.

### 4.2 Brussels I bis Article 8(1) joinder

Article 8(1) permits suing multiple defendants at the domicile of any one if claims are "so closely connected that it is expedient to hear and determine them together to avoid the risk of irreconcilable judgments."

CJEU interpretation. CDC Hydrogen Peroxide (C-352/13) applied a liberal standard for competition damages: claims against multiple cartel members share the "same situation of fact and law" satisfying the connection requirement. Roche Nederland (C-539/03) applied a restrictive standard for IP: territorially distinct patent rights governed by different national laws are not sufficiently connected. Freeport (C-98/06) held that different legal bases — contract and tort — do not preclude joinder if factually connected.

Application to DSA. Claims against a platform and a content uploader for the same harmful content could potentially be joined under Article 8(1). The DSA claim against the platform (failure to remove) and the defamation claim against the uploader (publication) share the same factual situation. But they have different legal bases and may be governed by different applicable laws — the Roche concern. Whether this resembles CDC (same infringement, joint liability) or Roche (territorially distinct rights) is uncertain.

### 4.3 Can DSA and GDPR claims be heard together?

GDPR Article 79(2) creates special jurisdiction — data subjects can sue at their habitual residence. Brussels I bis has no equivalent for DSA claims.

If a French user sues a platform in France, they can rely on Article 79(2) for the GDPR claim but need Article 7(2) for the DSA claim. Do they need to establish separate jurisdictional bases or does Article 79(2) "pull in" the connected DSA claim?

CJEU has not addressed this. Arguments for consolidated jurisdiction: same factual matrix, efficiency, avoiding irreconcilable outcomes. Arguments against: Article 79(2) is lex specialis for data protection only, not a general jurisdictional attractor.

### 4.4 Do joinder solutions from other regimes work?

Competition law collective actions. The Damages Directive 2014/104 does not create special joinder rules; it relies on Brussels I bis. Collective actions for cartel damages have used CDC's liberal joinder approach.

Representative Actions Directive (EU) 2020/1828. RAD allows qualified entities to bring representative actions for violations of listed instruments — including DSA. But RAD contains no PIL rules. Qualified entities cannot rely on consumer jurisdiction (Article 17-19 Brussels I bis) because they are not consumers. They must sue at defendant's domicile or fragment under Article 7(2).

This creates a bottleneck: all EU-wide representative actions against VLOPs must be brought in Ireland or Luxembourg.

---

## 5. Synthesis: why general PIL connecting factors fail the DSA

### 5.1 The structural mismatch

General PIL connecting factors presuppose territorial disputes — a tort with identifiable location, parties in different places, courts with proximity advantages.

DSA regulates ubiquitous digital services operating from single establishments across all markets. The connecting factors do not fit.

Defendant's domicile (Article 4 Brussels I bis) creates monopolistic jurisdiction in Ireland. Place of damage (Article 7(2), Article 4(1) Rome II) creates fragmentation into 27 parallel regimes. Consumer jurisdiction (Articles 17-19) excludes business users and depends on contested characterization. Lex loci damni inverts the country-of-origin principle underlying DSA supervision.

### 5.2 The GDPR contrast

GDPR addressed this mismatch by creating Article 79(2) — an autonomous jurisdiction rule giving data subjects forum choice between controller's establishment and their own habitual residence.

DSA did not. The legislative history does not explain this omission. Possible explanations: (1) oversight — PIL implications not fully considered; (2) deliberate choice — preferring flexibility of general rules; (3) political constraints — Member States could not agree on special jurisdiction.

Whatever the reason, the result is incoherent: GDPR claims arising from the same platform conduct receive more favorable PIL treatment than DSA claims.

### 5.3 The reform question

Solutions from other regimes — competition law's market-effects approach, GDPR's forum actoris, product liability's consumer-residence cascade — could inform DSA-specific PIL rules.

An autonomous DSA jurisdiction provision modeled on Article 79(2) GDPR would allow recipients to sue at their habitual residence.

Rome II revision to include personality rights — signaled in the Commission's 2025 Report — would bring many DSA claims within harmonized applicable law rules.

Brussels I bis revision to address collective action jurisdiction would enable effective representative actions under DSA Article 86.

---

## 6. Conclusion

The DSA's deferral to general PIL connecting factors produces systematic incoherence. Jurisdiction concentrates in Ireland absent uncertain consumer characterization. Applicable law fragments into 27 regimes despite uniform substantive obligations. Multi-claim joinder is uncertain. Collective redress lacks jurisdictional infrastructure.

These are design failures, not interpretive difficulties. The connecting factors function as intended — they were simply not designed for regulation of cross-border digital services. Coherence requires either autonomous DSA PIL rules or revision of general PIL instruments to accommodate digital services.
