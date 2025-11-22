# Joinder of Disputes and Applicable Law in Closely Connected Claims

## Document 4: Rules on Joinder and Determination of Applicable Law in Complex PIL Scenarios

This document analyzes the rules governing joinder of proceedings and determination of applicable law when DSA compensation claims are closely connected to claims under other EU instruments.

---

## Part I: Joinder of Related Actions under Brussels I bis

### Article 8(1) - Multiple Defendants and Joinder

**Provision:**
"A person domiciled in a Member State may also be sued:

(1) where he is one of a number of defendants, in the courts for the place where any one of them is domiciled, provided the claims are so closely connected that it is expedient to hear and determine them together to avoid the risk of irreconcilable judgments resulting from separate proceedings;"

### Requirements for Joinder

The CJEU has established a **two-part test** for Article 8(1):

#### 1. Claims Must Be "So Closely Connected"

**CJEU Interpretation (CDC v Akzo, C-352/13):**
- Claims share the **same situation of fact and law**
- Defendants addressed by single Commission cartel decision share same factual situation
- Different national tort laws do NOT prevent close connection
- Focus on whether **legal and factual questions** overlap substantially

**Application to DSA + Related Claims:**

**Example 1: DSA + GDPR (Automated Content Moderation)**
- **Factual unity**: Same platform decision (account suspension based on automated profiling)
- **Legal overlap**: Both involve automated decision-making, both protect against unlawful interference
- **Close connection**: YES - same factual event, overlapping legal issues
- **Conclusion**: Article 8(1) likely satisfied

**Example 2: DSA + Copyright Directive (Upload Filter)**
- **Factual unity**: Same removal decision by platform's automated filter
- **Legal overlap**: Content moderation (DSA) vs. copyright enforcement (Copyright Directive)
- **Close connection**: ARGUABLE - same act but different legal characterizations
- **Conclusion**: Borderline case; depends on judicial assessment

**Example 3: DSA + Product Liability (Defective Product on Marketplace)**
- **Factual unity**: Same transaction and same platform
- **Legal divergence**: Service liability (DSA) vs. product defect liability (PLD)
- **Close connection**: WEAK - different causes of action, different defendants (platform vs. manufacturer)
- **Conclusion**: Article 8(1) likely NOT satisfied unless platform liable under both regimes

#### 2. Risk of Irreconcilable Judgments

**CJEU Interpretation (CDC v Akzo, C-352/13):**
- "Irreconcilable" means **inconsistent application of same legal rule**
- Different outcomes based on different evidence = reconcilable
- Different outcomes based on contradictory legal reasoning = irreconcilable
- Risk must be **real**, not merely theoretical

**CJEU Interpretation (Roche Nederland, C-539/03):**
- Irreconcilable judgments exist when outcomes are "mutually exclusive"
- Example: One court finds patent valid, another finds it invalid
- Not sufficient that outcomes differ in amount of damages awarded

**Application to DSA Scenarios:**

**Scenario A: DSA Claim in France + GDPR Claim in Germany (Same Facts)**
- **Risk**: French court finds platform violated DSA Art. 14; German court finds GDPR compliant
- **Analysis**: If factual findings contradict (e.g., was decision automated?), judgments irreconcilable
- **Mitigation**: Article 30 (related actions) may allow stay or consolidation

**Scenario B: DSA Claim + Copyright Claim (Same Content Removal)**
- **Risk**: One court finds removal lawful under Copyright Directive; other finds unlawful under DSA
- **Analysis**: Not necessarily irreconcilable - different legal standards can coexist
- **Example**: Content removal can be copyright-compliant but DSA-violating if procedural safeguards ignored

---

### Strategic Use of Article 8(1) for Forum Selection

**Anchor Defendant Strategy:**
Claimant can choose forum by:
1. Selecting defendant domiciled in preferred Member State as "anchor defendant"
2. Joining other defendants under Article 8(1)
3. Obtaining jurisdiction over all defendants in preferred forum

**Limitations:**
- **Abuse of process**: Joining defendant "solely with the object of removing [other defendant] from the jurisdiction" (Art. 8(2))
- **Close connection must be genuine**
- Courts may scrutinize whether anchor defendant is genuine party to dispute

**Example: Platform + Content Uploader:**
- User sues platform (Ireland) + original uploader (France) for defamatory content
- Brings action in France (uploader's domicile)
- Seeks to join Irish platform under Article 8(1)
- **Question**: Are claims sufficiently connected?
  - Platform liability: DSA Art. 14 (notice-and-action)
  - Uploader liability: Defamation tort
  - **Different legal bases, but same factual event**
  - Courts may find sufficient connection

---

### Article 30 - Related Actions (Lis Pendens)

**Provision:**
"(1) Where related actions are pending in the courts of different Member States, any court other than the court first seised may stay its proceedings.

(2) Where the action in the court first seised is pending at first instance, any other court may also, on the application of one of the parties, decline jurisdiction if the court first seised has jurisdiction over the actions in question and its law permits the consolidation thereof.

(3) For the purposes of this Article, actions are deemed to be related where they are so closely connected that it is expedient to hear and determine them together to avoid the risk of irreconcilable judgments resulting from separate proceedings."

### Difference Between Article 8(1) and Article 30(3)

| **Aspect** | **Article 8(1)** | **Article 30(3)** |
|-----------|----------------|-----------------|
| **Stage** | Initial jurisdiction determination | After proceedings commenced in multiple forums |
| **Purpose** | Consolidate claims at outset | Prevent parallel proceedings |
| **Test** | Same ("closely connected") | Same definition |
| **Outcome** | Single court has jurisdiction | Court may stay or decline jurisdiction |
| **Discretion** | Claimant's initial choice | Court's discretion to stay/decline |

### Application to DSA + Related Claims

**Scenario: Parallel Proceedings**

**Facts:**
- User brings DSA claim against platform in France (Art. 7(2) - place of damage)
- Same user brings GDPR claim against same platform in Ireland (Art. 79(2) GDPR - establishment)
- Both claims arise from same content moderation decision

**Options:**

**Option 1: Stay French Proceedings (Art. 30(1))**
- French court may stay pending Irish proceedings
- Discretionary power
- Factors: Which court first seised? Judicial economy? 

**Option 2: French Court Declines Jurisdiction (Art. 30(2))**
- Requires: Irish court has jurisdiction over both actions
- Requires: Irish law permits consolidation
- **Problem**: Does Irish court have jurisdiction over DSA claim?
  - Not under GDPR Art. 79(2) (that's only for GDPR claims)
  - Would need Brussels I bis basis (Art. 4 or Art. 7(2))

**Option 3: Irish Court Consolidates**
- If both claims properly before Irish court
- Irish procedural law must permit joinder
- **Efficient**: Single proceeding for all claims

---

## Part II: Determining Applicable Law in Complex Scenarios

### General Principle: Separate Characterization

**Fundamental Rule:**
Each legal claim is **independently characterized** and subject to its own conflict-of-laws analysis.

**Implication for DSA Claims:**
- **DSA claim**: Subject to Rome II (generally Art. 4 - lex loci damni)
- **GDPR claim**: Subject to Rome II + GDPR specifics
- **Copyright claim**: Subject to Rome II Art. 8 (lex loci protectionis)
- **Contract claim**: Subject to Rome I

**Result:** Potential for **dépeçage** (split applicable law)

---

### Scenario Analysis: Applicable Law in Overlapping Claims

#### Scenario 1: DSA + GDPR (Overlapping Facts)

**Facts:**
- French user's account suspended by platform established in Ireland
- Suspension based on automated processing of personal data
- User claims: (1) DSA Art. 14 violation, (2) GDPR Art. 22 violation

**Step 1: Characterization**

**DSA Claim:**
- **Nature**: Non-contractual obligation arising from unlawful service restriction
- **Regulation**: Rome II
- **Provision**: Article 4(1) - general rule

**GDPR Claim:**
- **Nature**: Non-contractual obligation arising from unlawful data processing
- **Regulation**: Rome II (applicable to torts)
- **Provision**: Article 4(1) - but modified by GDPR's substantive rules

**Step 2: Connecting Factors**

**DSA Claim (Rome II Art. 4(1)):**
- **Lex loci damni**: France (where user suffered damage from account suspension)
- **French law** applies to DSA claim

**GDPR Claim:**
- **Rome II Art. 4(1)**: France (where user suffered damage)
- **BUT**: GDPR has territorial scope (Art. 3) and substantive provisions that may override
- **Analysis**: GDPR applies as EU Regulation; French implementation of GDPR + GDPR itself

**Step 3: Potential for Escape Clause (Rome II Art. 4(3))**

- **Question**: Is tort manifestly more closely connected to Ireland (platform establishment)?
- **Factors**:
  - Platform's terms of service (possibly Irish law)
  - Location of automated decision-making system (Ireland)
  - **BUT**: User's habitual residence and place of damage in France
- **Conclusion**: Unlikely to displace lex loci damni; **French law applies**

**Step 4: Overriding Mandatory Provisions (Rome II Art. 16)**

- **Question**: Are DSA/GDPR rules "overriding mandatory provisions"?
- **GDPR**: Arguably yes - fundamental rights protection, public interest
- **DSA**: Arguably yes - platform regulation in public interest
- **Effect**: Even if foreign law applies, forum's DSA/GDPR implementation cannot be excluded

**Result:**
- **Both claims governed primarily by French law** (implementation of GDPR and DSA)
- **EU Regulations (GDPR, DSA) directly applicable** regardless of connecting factor
- **No conflict** in this scenario

---

#### Scenario 2: DSA + Copyright Directive (Content Removal)

**Facts:**
- Spanish user uploads video to platform established in Netherlands
- Platform removes video based on copyright claim by German rightholder
- User claims: (1) DSA Art. 14 violation (improper removal), (2) Copyright Directive Art. 17 violation (safeguards not applied)

**Step 1: Characterization**

**DSA Claim:**
- **Nature**: Service provider's unlawful content moderation
- **Rome II Art. 4(1)** - lex loci damni

**Copyright Claim:**
- **Nature**: Infringement of intellectual property right (or defense against infringement allegation)
- **Rome II Art. 8** - lex loci protectionis

**Step 2: Applicable Law Analysis**

**DSA Claim:**
- **Place of damage**: Spain (user's location, reputational/economic harm)
- **Applicable law**: **Spanish law**

**Copyright Claim:**
- **Which country's protection claimed?**
  - User uploads video accessible EU-wide
  - Rightholder can claim protection in **any Member State** where copyright exists
  - **Typically**: Country where work exploited or distributed
- **Lex loci protectionis**: Potentially **multiple laws** (each MS where accessible)
- **Practical approach**: Law of country where main exploitation (may be multiple)

**Problem: Divergent Applicable Laws**

- **DSA aspects**: Spanish law
- **Copyright aspects**: German law (if that's where protection claimed) OR Dutch law OR multiple laws

**Solution 1: Court applies both laws (dépeçage)**
- DSA-specific issues (procedural safeguards, statement of reasons): Spanish DSA implementation
- Copyright-specific issues (is work protected, does exception apply): German copyright law

**Solution 2: Escape Clause (Rome II Art. 4(3))**
- **Argument**: Copyright and DSA claims manifestly more closely connected to one law
- **Counter-argument**: Copyright is territorial by nature; cannot apply single law
- **Likely outcome**: Dépeçage unavoidable

**Step 3: Role of EU Harmonization**

- **DSA**: Directly applicable Regulation - same across EU
- **Copyright Directive**: Harmonized but requires national implementation
- **Effect**: Less divergence than might appear, but **national procedural differences remain**

**Result:**
- **DSA claim**: Spanish law
- **Copyright claim**: Multiple laws (territorial approach)
- **Complexity**: Court must apply multiple laws to single factual scenario

---

#### Scenario 3: DSA + P2B + Contract (Business User Suspension)

**Facts:**
- Italian business sells products on marketplace platform established in Luxembourg
- Platform suspends business account for alleged ToS violations
- Business claims: (1) DSA Art. 20 violation (inadequate reasons), (2) P2B Regulation violation (unfair suspension), (3) Breach of contract

**Step 1: Characterization**

**DSA Claim:**
- **Nature**: Non-contractual obligation (tort)
- **Rome II Art. 4**

**P2B Claim:**
- **Nature**: Mixed - could be contractual OR tort
- **If contractual**: Rome I
- **If tort**: Rome II

**Contract Claim:**
- **Nature**: Contractual
- **Rome I Art. 4** (contracts for provision of services)

**Step 2: Applicable Law**

**Contract Claim (Rome I):**
- **Article 4(1)(b)**: Law of service provider's habitual residence = **Luxembourg**
- **Unless**: Parties chose different law (Art. 3) OR manifestly more closely connected (Art. 4(3))

**DSA Claim (Rome II):**
- **Lex loci damni**: Italy (where business suffered damage)
- **Italian law** applies to DSA claim

**P2B Claim:**
- **If characterized as contract**: Luxembourg law (follows contract)
- **If characterized as tort**: Italian law (lex loci damni)
- **Analytical challenge**: P2B regulates **contractual relationship** but creates **mandatory obligations**

**Step 3: Interaction of Applicable Laws**

**Scenario A: Luxembourg law applies to contract**
- Contract interpreted under Luxembourg law
- **BUT**: DSA and P2B are **directly applicable EU Regulations**
- **Effect**: Luxembourg law must incorporate DSA/P2B mandatory requirements
- **Result**: Luxembourg contractual law + DSA/P2B mandatory provisions

**Scenario B: Italian law applies to tort claims**
- DSA/P2B violations characterized as torts
- Italian law determines damages, remedies, procedure
- **Result**: Italian tort law + DSA/P2B mandatory provisions

**Step 4: Overriding Mandatory Provisions**

- **DSA Art. 14, 20**: Arguably overriding mandatory (public interest in platform fairness)
- **P2B Regulation**: Arguably overriding mandatory (protect business users)
- **Rome I Art. 9**: Forum's overriding mandatory provisions apply
- **Rome II Art. 16**: Forum's overriding mandatory provisions apply

**Result:**
- **Contract governed by**: Luxembourg law (lex causae) + Italian overriding mandatory provisions (if Italian court)
- **Tort governed by**: Italian law
- **DSA/P2B**: Apply as directly applicable EU law + national implementation
- **Practical effect**: All claims resolved with reference to Italian implementation of DSA/P2B + Luxembourg contract law principles

---

#### Scenario 4: DSA + Product Liability + Consumer Rights (Marketplace)

**Facts:**
- Austrian consumer purchases defective product via online marketplace (established in Ireland)
- Product causes personal injury and property damage
- Consumer claims: (1) Product liability against manufacturer and platform, (2) DSA Art. 6(5) platform liability, (3) Consumer rights violations

**Step 1: Characterization**

**Product Liability:**
- **Rome II Art. 5** - special rules for product liability

**DSA Claim:**
- **Rome II Art. 4** - general tort rule

**Consumer Rights:**
- **Rome I Art. 6** - consumer contracts (if contractual aspects)

**Step 2: Applicable Law - Product Liability (Rome II Art. 5)**

Rome II Art. 5 creates a **cascade of connecting factors**:

**(a) Law of consumer's habitual residence** (Austria) - **IF product marketed there**: YES
- **Austrian law applies** to product liability claim

**Step 3: Applicable Law - DSA Claim (Rome II Art. 4)**

- **Lex loci damni**: Austria (where consumer suffered injury)
- **Austrian law applies** to DSA Art. 6(5) claim

**Step 4: Applicable Law - Consumer Contract (Rome I Art. 6)**

**Article 6(1):**
- Contract governed by law of consumer's habitual residence = **Austria**
- **Mandatory provisions** of Austrian consumer law cannot be derogated by choice of law

**Result: Convergence**
- **All claims point to Austrian law**
- **Reason**: Consumer protection and product liability rules favor consumer's residence
- **Practical advantage**: Single law applies to entire dispute

**Step 5: Role of Escape Clauses**

**Rome II Art. 4(3):** Manifestly closer connection?
- **Unlikely**: Consumer protection policies favor consumer's residence
- **No reason to depart** from Austrian law

**Rome II Art. 5 (product liability):** Defendant could not reasonably foresee marketing?
- **Unlikely**: Major online marketplace markets EU-wide
- **Platform cannot invoke** this defense

---

### Special Case: Ubiquitous Online Harms

#### Problem of Multi-State Damage

**Scenario:**
- False information posted about business on social media platform
- Information accessible in all EU Member States
- Business suffers reputational harm in multiple countries

**Legal Question:** Which law applies?

**Option 1: Mosaic Approach (Multiple Laws)**
- Following CJEU case law (Shevill, Gtflix TV)
- **Each Member State's law** applies to damage in that territory
- **Result**: Potentially 27 different applicable laws

**Option 2: Single Applicable Law**
- Lex loci damni = place of **principal damage** (center of interests)
- Following eDate/Martinez for personality rights
- **Result**: Law of one Member State applies to all damage

**Option 3: Escape Clause (Rome II Art. 4(3))**
- Manifestly more closely connected to single law
- **Argument**: Ubiquitous harm requires single law for practicality
- **Counter-argument**: Would undermine territorial approach

**Current State of Law:**
- **Jurisdiction**: CJEU allows both mosaic (local damage) and full jurisdiction (center of interests for personality rights)
- **Applicable law**: Rome II less clear; Art. 4(1) points to lex loci damni
- **Scholarly debate**: Should Rome II adopt eDate approach for applicable law?

**Practical Impact on DSA Claims:**
- **If mosaic approach**: Complex multi-law analysis
- **If single law approach**: More practical but less protective of territorial sovereignty
- **Current practice**: Courts likely apply lex loci damni, but may use Art. 4(3) escape clause for ubiquitous harms

---

## Part III: Special PIL Rules and Their Interaction

### Rule 1: Rome I Art. 6 (Consumer Contracts)

**When Applicable:**
- Consumer contract for services (e.g., social media premium subscription)
- Professional directs activities to consumer's Member State

**Effect:**
- **Mandatory provisions** of consumer's law apply
- Cannot be derogated by choice of law

**Interaction with DSA:**
- If DSA claim characterized as **contractual**: Rome I Art. 6 applies
- If DSA claim characterized as **tort**: Rome II Art. 4 applies
- **Hybrid situation**: Some aspects contractual (ToS), some tort (unlawful content moderation)

**Solution:**
Courts must characterize claim carefully:
- **Primary obligation breached**: Contract (service provision) or tort (unlawful interference)?
- **Nature of damage**: Breach of contract or independent tortious harm?

---

### Rule 2: Rome II Art. 6 (Unfair Competition)

**When Applicable:**
- Unfair commercial practices (e.g., dark patterns, misleading advertising)

**Connecting Factor:**
- **Law of country where competitive relations or collective consumer interests affected**

**Interaction with DSA:**
- DSA Art. 25 prohibits dark patterns
- If characterized as **unfair competition**: Rome II Art. 6 applies
- If characterized as **service tort**: Rome II Art. 4 applies

**Difference:**
- **Art. 6**: Focuses on market affected (may be multiple)
- **Art. 4**: Focuses on where individual damage occurred

**Example:**
- Platform uses dark patterns targeting French users
- **Rome II Art. 6**: French law (market affected)
- **Rome II Art. 4**: Also French law (user's damage)
- **Result**: Convergence in this case

---

### Rule 3: Rome II Art. 8 (Intellectual Property)

**When Applicable:**
- Copyright, trademark, patent infringement claims

**Connecting Factor:**
- **Lex loci protectionis** - law of country for which protection claimed

**Interaction with DSA:**
- Content moderation often involves copyright claims (Art. 17 Copyright Directive)
- **IP aspects**: Rome II Art. 8
- **Service aspects**: Rome II Art. 4
- **Result**: Dépeçage (split applicable law)

**Complexity:**
Court must apply:
- **Lex loci protectionis** for copyright validity, infringement, exceptions
- **Lex loci damni** for DSA procedural requirements, damages calculation

---

### Rule 4: Overriding Mandatory Provisions (Rome I Art. 9, Rome II Art. 16)

**Definition:**
Provisions whose respect is **crucial for safeguarding public interests** (political, social, economic organization)

**Examples:**
- Labor law protections
- Consumer protection laws
- Competition law
- **Arguably**: GDPR, DSA, P2B (platform regulation in public interest)

**Effect:**
**Forum's overriding mandatory provisions apply** regardless of applicable law

**Application to DSA:**

**Arguments FOR DSA as Overriding Mandatory:**
1. Public interest in platform regulation
2. Fundamental rights protection (freedom of expression, privacy)
3. Market fairness and consumer protection
4. DSA explicitly states obligations apply regardless of establishment

**Arguments AGAINST:**
1. DSA Art. 2(2)(h) defers to PIL rules
2. DSA Art. 54 references "Union and national law" (doesn't claim overriding status)
3. CJEU restrictive interpretation of overriding mandatory provisions (Nikiforidis)

**Likely Outcome:**
- **Core substantive obligations** (e.g., Art. 14 content moderation): Overriding mandatory
- **Procedural requirements** (e.g., Art. 20 statement of reasons): Overriding mandatory
- **Compensation details** (quantum, limitation periods): Subject to applicable law (lex causae)

---

## Part IV: Collective Redress and Representative Actions

### Representative Actions Directive (EU) 2020/1828

**Relevance to DSA:**
DSA Art. 86 explicitly references representative actions for collective interests

**PIL Implications:**

#### Jurisdiction (Brussels I bis)

**Article 4:** Defendant's domicile - **general rule**

**Article 7(2):** Place where harmful event occurred - **alternative forum**
- **Collective actions**: Multiple victims in multiple Member States
- **Question**: Can representative entity choose any forum where damage occurred?
- **Recent scholarship**: Argues for **consolidated jurisdiction** at one forum for EU-wide claims

**Article 8(1):** Multiple defendants
- **If multiple platforms sued**: Can join at domicile of any one defendant

#### Applicable Law

**Question:** In representative action covering victims from multiple Member States, which law applies?

**Option 1: Single Applicable Law**
- **Advantage**: Efficiency, uniformity
- **Problem**: Which law? Forum law? Defendant's law?
- **Rome II does not provide for this**

**Option 2: Multiple Applicable Laws**
- Apply law of each victim's country
- **Advantage**: Respects lex loci damni principle
- **Problem**: Extremely complex, may make collective redress impractical

**Option 3: Forum Law as Procedural**
- **Forum determines**:
  - Procedural rules for collective actions
  - Standing of representative entity
  - Opt-in vs. opt-out
- **Applicable law determines**:
  - Substantive liability
  - Damages calculation

**Current Approach:**
- **No harmonized solution**
- **Member States differ** in treatment of collective actions' PIL
- **DSA provides no specific guidance**

---

## Part V: Synthesis and Practical Framework

### Decision Tree for Determining Applicable Law in DSA + Related Claims

**Step 1: Identify all potential legal bases**
- DSA violation?
- GDPR violation?
- Copyright infringement?
- Contract breach?
- Consumer rights violation?
- Other?

**Step 2: Characterize each claim**
- **Contractual** → Rome I
- **Non-contractual (tort)** → Rome II
- **IP infringement** → Rome II Art. 8
- **Product liability** → Rome II Art. 5
- **Consumer contract** → Rome I Art. 6

**Step 3: Apply connecting factors**
- **Rome I Art. 4**: Service provider's residence (default)
- **Rome I Art. 6**: Consumer's residence (mandatory rules)
- **Rome II Art. 4**: Place of damage (lex loci damni)
- **Rome II Art. 5**: Consumer's residence (if product marketed there)
- **Rome II Art. 8**: Country for which protection claimed (lex loci protectionis)

**Step 4: Consider escape clauses**
- **Rome I Art. 4(3)**: Manifestly more closely connected?
- **Rome II Art. 4(3)**: Manifestly more closely connected?

**Step 5: Apply overriding mandatory provisions**
- **Forum's mandatory rules** (Rome I Art. 9, Rome II Art. 16)
- **EU Regulations directly applicable** (DSA, GDPR, P2B)

**Step 6: Resolve conflicts/overlaps**
- **If same law applies**: No conflict
- **If different laws**: Dépeçage (apply each to respective issue)
- **If irreconcilable**: Court must choose primary characterization

---

### Summary Table: Joinder and Applicable Law

| **Scenario** | **Joinder (Art. 8(1))** | **Primary Applicable Law** | **Secondary Considerations** |
|-------------|------------------------|--------------------------|----------------------------|
| **DSA + GDPR (same facts)** | Likely YES (closely connected) | Lex loci damni (user's location) | Both are EU Regulations; convergence likely |
| **DSA + Copyright** | Arguable (same event, different legal bases) | DSA: lex loci damni; Copyright: lex loci protectionis | Dépeçage required |
| **DSA + P2B (business user)** | Likely YES | Contract: service provider's law; Tort: lex loci damni | Overriding mandatory provisions apply |
| **DSA + Product Liability** | Depends (if platform liable under both) | Rome II Art. 5 cascade (consumer's residence if marketed) | Convergence likely in consumer cases |
| **DSA + Consumer contract** | Depends on characterization | If contract: Rome I Art. 6; If tort: Rome II Art. 4 | Consumer protection rules favor consumer's law |

---

## Part VI: Open Questions and Academic Debate

### Question 1: Should DSA Have Its Own PIL Regime?

**Arguments FOR:**
- **Uniformity**: Avoid fragmentation across Member States
- **Predictability**: Clear rules for platforms and users
- **GDPR precedent**: Art. 79(2) creates special jurisdiction rule

**Arguments AGAINST:**
- **Flexibility**: General PIL rules allow case-by-case justice
- **Harmonization exists**: DSA is directly applicable Regulation
- **Complexity**: Adding more special rules increases overall complexity

**Current Status:** DSA defers to general PIL (Art. 2(2)(h))

---

### Question 2: How to Handle Ubiquitous Online Harm?

**Problem:** Single online publication causes damage in all 27 Member States

**Option A: Mosaic Approach**
- Maintain territoriality principle
- Each Member State's law applies to local damage
- **Critique**: Impractical, fragments liability

**Option B: Center of Interests**
- Apply law of victim's center of interests (habitual residence)
- **Critique**: Works for individuals, but corporations?

**Option C: Marketplace Approach**
- Apply law where platform primarily operates
- **Critique**: Favors platforms, undermines protection

**Current Status:** Ongoing academic debate; no CJEU guidance on applicable law (only jurisdiction)

---

### Question 3: Interaction of Multiple Protective Regimes

**Problem:** Consumer is also data subject and internet user

**Overlapping Protections:**
- Consumer law (Rome I Art. 6)
- Data protection (GDPR Art. 79(2))
- DSA user protections (Art. 54)

**Question:** Can claimant invoke **most favorable** PIL rule from each regime?

**Answer:** Likely NO - characterization determines which regime applies

**But:** Overriding mandatory provisions allow **cumulation** of protections

---

## Conclusion

The PIL framework for DSA compensation claims is **complex and multi-layered**:

1. **No autonomous DSA PIL regime** - defers to Brussels I bis and Rome II

2. **Joinder possible** under Brussels I bis Art. 8(1) for closely connected claims

3. **Applicable law determined separately** for each characterization:
   - Torts: Rome II Art. 4 (lex loci damni)
   - IP: Rome II Art. 8 (lex loci protectionis)  
   - Contracts: Rome I (various rules)

4. **Overriding mandatory provisions** ensure minimum standards apply

5. **Practical challenges**: Dépeçage, multiple proceedings, forum shopping

6. **Academic consensus**: Current framework workable but suboptimal; future reform may be needed

---

*Document prepared for academic research purposes.*
