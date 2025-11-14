
This is a critical plan to update the current draft of Chapter III. For convinence of editing, the chapter is split into 3 files: [[draft-copyright-1]], [[draft-copyright-2]] and [[draft-copyright-3]] which can be edited directly. 
NOTE: It is crucial to carry out plan by phases and to fully adhere to [[Prompt protection/Style]] in any case. If this plan contains anything that conflicts with style instructions, they prevail.
# COMPREHENSIVE REVISION TO-DO PLAN: Chapter III

## Target: Reduce from ~11,000 words to ~7,000 words (36% reduction)

---

## PHASE 1: STRUCTURAL REORGANIZATION & MAJOR DOCTRINAL FIXES

### **Task 1.1: DELETE Part D (Identifiability) Entirely**

- **Action**: Remove entire section (currently ~800 words)
- **Rationale**: Fundamental misapplication of _Levola_. The case concerned whether taste itself (subjective, variable across perceivers, no objective notation) could be a "work." Prompts are text—perfectly identifiable as strings of characters. That outputs vary is irrelevant to identifiability of the prompt text itself.
- **Save**: Move the non-determinism point (1 paragraph, ~150 words) to Task 1.4 (preparatory material section)
- **Net reduction**: ~650 words
- **Doctrinal note**: If you want to salvage anything from _Levola_, reframe it narrowly: _Levola_ reinforces that copyright protects discrete expressive works, not open-ended system behavior. Use this to support _Sony Datel_ (variable outputs not protected), not to claim prompt text isn't identifiable.

---

### **Task 1.2: Merge Parts B & C into Single "Application to Prompts" Section**

- **Current**: Part B (~1,400 words) + Part C (~1,800 words) = 3,200 words
- **Target**: 1,800 words (44% reduction)

**New Structure:**

**B. Application of Originality Standard to Prompts** (1,800 words total)

1. **Introduction: The challenge for functional texts** (150 words)
    
    - State that prompts must be assessed under _Infopaq_/_Painer_/_Football Dataco_ framework
    - Note that functional texts consistently face higher originality thresholds
2. **Simple prompts** (400 words):
    
    - "Summarize" example (100 words) - single words excluded per _Infopaq_
    - Business letter example (250 words) - functional specifications dominate
    - National court practice (50 words) - German _Bedienungsanleitung_, French recipes, Dutch _Endstra_, Czech Municipal Court brief mention
3. **Complex prompts: The hard case** (1,250 words):
    
    - **Opening acknowledgment** (100 words): "The 400-word system prompt presents the strongest case for copyright protection. Academic analysis suggests longer texts provide more scope for creative choices. This deserves serious engagement."
        
    - **The functional constraint framework** (400 words):
        
        - _Football Dataco_/_Painer_: originality requires creative choices expressing personality
        - **Critical correction re: Brompton**: "Under _Football Dataco_, functional constraints narrow the space for creative choices. The CJEU in _Brompton Bicycle_ held that where technical considerations leave 'no room for creative freedom', originality fails. This is not a 'predominance' test—it requires examining whether meaningful creative latitude exists."
        - For prompts: choices respond to functional optimization requirements
        - Parameter specifications ("temperature=0.3"), formatting conventions, keyword placement—all dictated by what works with AI models
    - **Merger analysis** (350 words):
        
        - Many prompt elements have virtually no room for meaningful variation
        - "Use active voice" vs "employ active voice" vs "prefer active constructions"—trivial word substitution
        - "Formal tone" vs "professional tone" vs "business-appropriate style"—functionally equivalent
        - Where limited ways exist to express instructions, idea and expression merge
        - Reference _BSA_ para 50: protecting functionality would monopolize ideas
    - **Why accumulated complexity still fails** (400 words):
        
        - Length alone doesn't establish originality—_Football Dataco_ rejected sweat-of-brow
        - Operating manuals (German), recipes (French) remain unprotected despite length
        - System prompts aggregate functional specifications, each dictated by effectiveness
        - The whole reflects cumulative optimization decisions, not personality-expressing creativity
        - Even 400 words of specifications remain instructions about what to produce, not creative literary expression

**Eliminate**:

- Repetitive restatements of originality standard
- Multiple examples making identical points
- Excessive quotation of same CJEU paragraphs

---

### **Task 1.3: Consolidate Parts E & F into Single "Software Directive Exclusions" Section**

- **Current**: Part E (~3,200 words) + Part F (~900 words) = 4,100 words
- **Target**: 2,500 words (39% reduction)

**New Structure:**

**E. The Idea-Expression Dichotomy and Software Directive Exclusions** (2,500 words total)

1. **Framework: TRIPS 9(2) and Article 1(2)** (300 words)
    
    - TRIPS Art 9(2): expressions protected, not ideas/procedures/methods
    - Software Directive Art 1(2): expression protected, not ideas/principles underlying programs
    - Recital 11: interfaces explicitly excluded
    - This exclusion applies across all copyright directives
2. **CRITICAL DOCTRINAL CLARIFICATION: The two-track structure** (250 words)
    
    - **NEW CONTENT**: "The Software Directive and InfoSoc Directive operate on separate tracks. Subject matter may be excluded as 'expression of a computer program' under Art 1(2) Software Directive yet still potentially protected as another work category under InfoSoc Directive."
    - Example: _BSA_ held GUIs are not protected _as computer programs_ but may be protected as graphic/artistic works if original
    - For prompts this means: even if excluded under Software Directive Art 1(2), must still examine whether they qualify as literary works under InfoSoc
    - Structure of remaining analysis: (a) prompts excluded under Software Directive, AND (b) they independently fail InfoSoc originality (already established in Part B)
3. **Interfaces excluded: BSA** (450 words)
    
    - **REVISED FORMULATION**: "In _BSA_, the CJEU held that graphical user interfaces do not constitute 'expression of a computer program' for purposes of Software Directive protection. GUIs are user-facing mechanisms for interacting with programs, not the program expression itself. Only source or object code constituting the program qualifies for Software Directive protection."
    - **Acknowledge**: "This does not mean GUIs can never be protected—they may qualify as artistic works under InfoSoc if original. But as program expression, they fall outside Art 1(2)."
    - Prompts as textual interfaces: just as GUIs provide visual interfaces, prompts provide natural language interfaces to AI systems
    - Neither constitutes the program itself—both are methods of communicating with existing computational systems
    - **For prompts specifically**: Unlike GUIs which may have autonomous visual/artistic content justifying InfoSoc protection, prompts typically consist of functional instructions lacking the creative expression necessary for literary work protection (see Part B)
    - Conclusion: Prompts excluded as program expression under Art 1(2), and separately fail originality for literary works
4. **Functionality excluded: SAS Institute** (500 words)
    
    - Court held functionality, programming language, data file formats not protected
    - Para 40: protecting functionality would monopolize ideas, harm technological progress
    - **REFINED BRIDGE TO PROMPTS**: "Prompts specify functionality—they describe what outputs AI should generate, not expressions of how the system generates them. They are methods for instructing computational systems."
    - **Critical addition re: natural language**: "The argument that natural language prompts function like programming languages requires careful formulation. SAS Institute concerned a formal programming language designed for computers. The stronger doctrinal foundation is Art 1(2)'s exclusion of 'ideas and principles underlying any element of a computer program, including those which underlie its interfaces.' Even if prompts are not themselves 'programming languages,' they constitute methods and principles for using AI interfaces—precisely what Art 1(2) excludes."
    - Python command `print("Hello")` and prompt "Write 'Hello'" both instruct computational systems
    - Natural language formulation doesn't transform instruction into protectable expression
    - Protecting prompts would enable monopolization of methods of operation—what _SAS Institute_ paras 39-40 forbid
5. **Data inputs excluded: Sony Datel** (450 words)
    
    - **PRECISE RATIO**: "The Court held that 'the content of the variables which are stored temporarily in a console's RAM memory during the playing of a video game does not itself constitute a form of expression of the computer program.' The Court's framework: protection covers textual forms (source/object code) that enable reproduction or subsequent creation of the program. Variable contents that do not allow reproduction fall outside Art 1."
    - **REFINED ANALOGY**: "Prompts function analogously to RAM variables—both are ephemeral, user-controlled data that modify how a pre-existing program behaves at runtime, without themselves enabling reproduction of the program itself."
    - RAM variables: data inputs to existing programs that control behavior
    - Prompts: textual inputs to existing AI programs that control operation
    - Both affect outputs generated; neither enables program reproduction
    - **Precision note**: "This does not mean all data inputs are necessarily unprotected—the holding is specifically that data inputs which do not constitute the textual form of the program expression and do not enable program reproduction fall outside Software Directive protection."
    - Prompts invoke existing computational processes; they don't constitute program expression
6. **Preparatory design material: Why prompts fail** (550 words)
    
    - Art 1(1): protection extends to preparatory design material
        
    - Recital 7: "provided that the nature of the preparatory work is such that a computer program can result from it at a later stage"
        
    - **Three obstacles**:
        
    - **First: No program results** (150 words)
        
        - Prompts lead to AI-generated outputs (text, images, analyses), not programs
        - AI model already exists as complete program
        - Prompt doesn't constitute design work for creating program—it's instructions for using existing program
    - **Second: Insufficient technical specificity** (200 words)
        
        - Preparatory material must possess technical specificity constraining implementation—"quasi-coding"
        - Flow charts, architecture documents qualify because they constrain programmer choices
        - Prompts are high-level natural language instructions leaving implementation entirely to AI
        - Don't specify neural network operations, mathematical processes—only desired output characteristics
    - **Third: Non-determinism** (200 words)
        
        - **Content moved from deleted Part D**: "Preparatory design material exhibits determinism—same specifications yield functionally equivalent implementations. Multiple programmers working from identical pseudocode produce equivalent programs."
        - "Prompts operate probabilistically. The same prompt submitted to the same AI model at different times generates varying outputs due to stochastic sampling, temperature parameters, random seeds, and non-deterministic inference processes."
        - "This non-determinism fundamentally distinguishes prompts from preparatory design materials, which must be sufficiently specified to enable consistent program implementation."
        - Academic support: Guadamuz, Sampaio on non-determinism problem

**Eliminate**:

- Old Part E.4 (recipes, game rules)—this repeats Part B material
- Redundant restatements of exclusion principles
- Multiple examples proving same point
- Repetitive transitional phrases

---

## PHASE 2: STREAMLINE & STRENGTHEN REMAINING SECTIONS

### **Task 2.1: Tighten Part A (Originality Standard)**

- **Current**: ~1,400 words
- **Target**: 1,000 words (29% reduction)

**Actions**:

1. State _Infopaq_ holding cleanly (100 words)
2. _Painer_/_Football Dataco_ elaboration (200 words)
3. _Cofemel_ harmonization and exclusivity of standard (200 words)
4. _Levola_ two-part requirement: originality + expression (150 words)
5. Remove extended Copyright Term Directive discussion—move one-paragraph version of term-mismatch to Part G
6. Tighten quotations—cite propositions, don't quote extensively
7. Remove repetitive explanations of same principle

**What to keep**:

- The core framework: author's own intellectual creation, free and creative choices, personal touch
- Rejection of sweat-of-brow
- _Cofemel_'s exclusivity—no alternative criteria permitted
- Two-part requirement from _Levola_

**What to cut**:

- Redundant quotations
- Over-explanation of settled principles
- Copyright Term Directive detail (keep policy point for Part G)

---

### **Task 2.2: Strengthen Part G (Policy Justifications)**

- **Current**: ~1,200 words
- **Target**: 1,100 words, but ADD new substantive content

**New Structure:**

1. **Interoperability requires interface freedom** (300 words)
    
    - Art 6 Software Directive: decompilation right for interoperability
    - Recital 10: connecting components of different manufacturers
    - Commission preparatory work: copyright's advantage is leaving latitude for independent development
    - Applied to prompts: users must be free to discover effective instructions
    - Protecting prompts would create barriers Art 6 seeks to prevent
2. **CRITICAL CITATION FIX: Reverse engineering and lawful acquirer rights** (250 words)
    
    - **DELETE reference to _UsedSoft_**
    - **REPLACE WITH**: "Art 5(3) and Art 6 Software Directive explicitly grant lawful acquirers rights to observe, study, and test programs to determine functionality. The CJEU has interpreted these provisions expansively in _SAS Institute_ and _Top System_ (C-13/20), confirming users' rights to understand program interfaces through lawful use and testing."
    - Apply to prompts: "When users experiment with AI systems to discover effective prompts, they engage in the same interface exploration that Arts 5(3) and 6 protect. Technical research demonstrates prompts are readily reverse-engineered from outputs through prompt extraction techniques—lawful reverse engineering under both Software Directive and Trade Secrets Directive (2016/943)."
    - Granting copyright would create legal barriers to reverse engineering EU policy deliberately avoids
3. **NEW SECTION: Access to justice and AI literacy concerns** (250 words)
    
    - **NEW CONTENT**: "Copyright protection for prompts would create severe access-to-justice problems. How would small businesses or individuals determine whether their prompting techniques infringe 70-year-old protected prompts? Unlike patents with searchable registries and clear claims, copyright arises automatically without notice or registration."
    - "Prompt libraries would become legal minefields. Every effective technique—requesting 'formal tone,' specifying 'step-by-step reasoning,' using 'chain-of-thought prompting'—could be someone's protected expression. Users would face unavoidable uncertainty about whether routine AI interaction infringes copyright."
    - "This would chill AI literacy development. Educators share prompting techniques; researchers publish effective strategies; communities collaboratively develop best practices. Copyright protection would restrict this cumulative learning essential to democratizing AI access."
    - "The policy mismatch is stark: copyright's 70-year monopoly applied to functional techniques whose value lies in widespread adoption and iterative improvement."
4. **Term mismatch** (250 words)
    
    - Copyright Term Directive: 70 years post mortem auctoris, justified for protecting cultural works across generations
    - Prompts optimized for GPT-4 may fail on GPT-5
    - Functional instructions with 6-month useful lives vs. multi-generational protection
    - Structural unsuitability of copyright's default term
    - Creates barriers to cumulative innovation, chills experimentation
    - **Moved from Part A**: "The Copyright Term Directive justifies its extraordinarily long term as necessary to 'protect works for two generations after the author's death' given increased human longevity. This rationale assumes cultural value persisting across generations—wholly inappropriate for functional instructions becoming technologically obsolete within months."

**Net change**: Remove ~100 words repetition, add ~250 words new access-to-justice content, fix UsedSoft citation error = +150 words, but within tolerance given importance

---

### **Task 2.3: Compress Part H (Scholarly Commentary)**

- **Current**: ~800 words
- **Target**: 450 words (44% reduction)

**Restructure**:

1. **Opening acknowledgment** (50 words): "Academic commentary on prompt copyrightability has converged substantially, though not unanimously, on skepticism toward protection under EU law."
    
2. **Core scholarly positions** (300 words):
    
    - **Xiyin He**: prompts as unprotectable ideas/methods
    - **Gervais & Hugenholtz**: transferability problem, danger of monopolizing ideas
    - **Quintais & Hugenholtz**: technical constraints leave no creative freedom
    - **Matulionyte & Ramalho**: protecting prompts would grant exclusive rights over methods
    - **Guadamuz & Sampaio**: non-determinism problem
3. **Acknowledgment of debate** (100 words):
    
    - **NEW**: "This scholarly consensus is not universal. Some commentators argue that complex system prompts exhibit genuine creativity warranting protection, and that denying protection eliminates incentives for prompt engineering investment. These arguments merit serious consideration and are addressed in Part K below."

**What to cut**:

- Extended quotations—cite for propositions only
- Repetitive explanations of points already made
- Over-reliance on blog sources—keep Kluwer blog citations but don't quote extensively

---

### **Task 2.4: Streamline Part J (Database Protection)**

- **Current**: ~1,600 words
- **Target**: 1,200 words (25% reduction)

**Actions**:

1. **Art 3 copyright for databases** (300 words):
    
    - Faster through definition, originality requirement
    - _Football Dataco_ framework
    - Applied to prompts: functional selection/arrangement vs. creative
    - Art 3(2): protection doesn't extend to contents
2. **Art 7 sui generis right** (900 words):
    
    - Keep _British Horseracing Board_ analysis—this is important and well-done
    - Creation vs. obtaining distinction
    - Verification and presentation pathways (narrow)
    - Practical conclusion

**What to cut**:

- Repetitive examples
- Over-explanation of settled database principles
- Some transitional phrases

**What to keep**:

- The creation/obtaining distinction—critical for prompts
- Verification/presentation narrow pathways
- Realistic assessment of what might qualify

---

### **Task 2.5: Improve Part K (Counterarguments) - Make More Charitable**

- **Current**: ~1,800 words
- **Target**: 1,600 words, but IMPROVE tone

**Restructure each counterargument**:

**Current pattern**:

> "**The argument:** [X] **The rebuttal:** This argument founders on..."

**NEW PATTERN**:

> "**The argument:** [X] **Strength of this argument:** [Acknowledge legitimate points] **Why it ultimately fails:**[Rebuttal]"

**Specific revisions**:

1. **Economic incentive argument** (500 words):
    
    - **Acknowledge**: "This argument has considerable force. Investment in prompt engineering is real and substantial. The concern about free-riding on optimization efforts is legitimate. Copyright's traditional purpose is to incentivize creation through temporary monopolies, and this logic has intuitive appeal for prompts."
    - **Then rebut**: Three reasons why copyright is nonetheless inappropriate tool
    - Maintain _Football Dataco_ sweat-of-brow rejection
    - Note alternative protections exist (trade secrets, contracts, technical measures)
    - Term mismatch creates perverse incentives
2. **Creative expression argument** (550 words):
    
    - **Acknowledge**: "Elaborate system prompts do involve linguistic choices. A 400-word prompt reflects decisions about phrasing, organization, and terminology. The author selects among alternatives. If an 11-word excerpt can be protected per _Infopaq_, the argument for 400-word prompts has surface plausibility."
    - **Then rebut**: Distinction between sophistication and creativity
    - Prompts are instructions about what to produce, not creative works
    - Recipe analogy: creative literary description (protected) vs. functional instructions (unprotected)
    - _Brompton_/_Football Dataco_ functional constraint framework
    - Merger where limited ways exist to express instructions
3. **Complexity threshold argument** (350 words):
    
    - **Acknowledge**: "_Cofemel_ established that 'no aesthetic or qualitative criteria should be applied.' The originality threshold is deliberately low. Multiple choices accumulate across a long prompt. This argument merits serious consideration."
    - **Then rebut**: Originality requires creative choices, not merely numerous choices
    - Functional specifications remain functional regardless of length
    - German/French case law on lengthy functional texts
    - Idea-expression merger where functional requirements dominate
4. **Technological neutrality argument** (200 words):
    
    - **Acknowledge**: "Copyright law should not arbitrarily discriminate based on technological context. This principle is sound and important."
    - **Then rebut**: The distinction is function, not technology
    - Recipes, instructions, specifications face same limitations in non-AI contexts
    - Purpose determines protection, not medium
    - Software Directive Art 1(2) exclusions apply regardless of interface type (visual, textual, natural language)

**Overall tone shift**:

- From: "This argument founders on..."
- To: "This argument has force because [X], but ultimately fails because [Y]."

**Net**: ~200 words cut from repetition, but stronger engagement with opposing views

---

### **Task 2.6: Radically Compress Part L (Synthesis)**

- **Current**: ~1,200 words
- **Target**: 400 words (67% reduction)

**New structure** (4 paragraphs):

**Paragraph 1** (100 words): "Three independent barriers defeat prompt copyrightability, each sufficient alone."

**Paragraph 2** (100 words): "First, originality failure. Under _Football Dataco_/_Brompton Bicycle_, choices dictated by functional constraints don't reflect the 'personal touch' required. Prompt engineering choices respond to technical optimization—what works effectively with AI models—rather than artistic expression. National courts across Member States consistently exclude functional instructions absent substantial creative expression beyond functional necessity."

**Paragraph 3** (100 words): "Second, idea-expression exclusion. Prompts constitute instructions about what to create—specifications of ideas, methods, and procedures under TRIPS Art 9(2) and Software Directive Art 1(2). The CJEU's decisions in _BSA_, _SAS Institute_, and _Sony Datel_ establish that prompts are interfaces, functional specifications, and data inputs—all expressly excluded categories. Protecting prompts would monopolize methods of AI interaction, violating the fundamental principle that copyright extends to expression but not to underlying ideas, procedures, or methods."

**Paragraph 4** (100 words): "Third, database protection faces the _British Horseracing Board_ creation/obtaining distinction. Investment in creating prompts doesn't qualify; only narrow verification/presentation pathways remain. The convergence across copyright doctrines isn't coincidental—it reflects deliberate policy choices about preserving the public domain of methods, procedures, and building blocks necessary for innovation and competition. The Commission's Software Directive preparatory work emphasized leaving 'latitude to create similar or even identical programs' through independent development. Extending protection to prompts would eliminate that latitude."

**Eliminate**:

- All repetition of arguments already made
- Extended recapitulation of case law
- Detailed policy discussion (already in Part G)

---

### **Task 2.7: Keep Part M (Exceptional Cases) But Tighten**

- **Current**: ~600 words
- **Target**: 450 words (25% reduction)

**Actions**:

1. **Prompts embedded in literary works** (200 words):
    
    - French recipe analogy: creative narrative (protected) vs. functional instructions (unprotected)
    - A creative essay about prompting with literary commentary might be protected
    - But protection extends only to creative prose, not functional content
    - Competitors can extract and use functional specifications
2. **Prompts as source code modules** (200 words):
    
    - Where hard-coded into programs as string constants
    - Protected as part of program under Art 1(1)
    - But Art 1(2) still excludes ideas and principles
    - Extracting functional content and expressing differently doesn't infringe
    - Protection extends to specific textual expression in source, not functional method implemented
3. **Conclusion** (50 words):
    
    - Both exceptions confirm general rule
    - Copyright may protect creative embellishment or specific source code expression
    - Functional instructions themselves remain unprotected and free for use
    - Preserves copyright's fundamental balance

**What to cut**:

- Repetitive explanations
- Over-detailed elaboration of narrow scenarios
- Redundant restatement of principles

---

## PHASE 3: LINE-EDITING, DOCTRINAL PRECISION & POLISH

### **Task 3.1: Eliminate Repetitive Phrases Throughout**

**Search and reduce instances of:**

- "The CJEU held that..." (currently ~25 times → target ~12 times)
- "This principle applies to prompts..." (overused transition)
- "Copyright protection requires..." (repetitive)
- "The distinction is critical..." (overused emphasis)
- "As the Court held in..." (vary phrasing)

**Specific patterns to fix**:

- After first mention of case, use "the Court" not "the CJEU"
- Integrate holdings into flowing sentences, not always "The Court held that [quote]"
- Vary transition phrases
- Trust IIC readers to understand copyright basics—don't restate constantly

**Target reduction**: ~300 words of repetitive transitional phrases

---

### **Task 3.2: Fix All Citation Issues**

**Priority fixes**:

1. **Footnote 23-24** (Czech Municipal Court):
    
    - **Current**: Relies on Bird & Bird blog post for court decision
    - **Fix**: Either locate primary source/more authoritative report, OR
    - Revise to: "According to Bird & Bird's report of an unreported first-instance decision, the Czech Municipal Court in Prague held _obiter_ in April 2023 that..."
    - Add caveat: "While this is a first-instance decision without binding precedential value, it represents the first known judicial opinion directly addressing prompt copyrightability."
2. **Footnotes 77-79** (Kluwer Copyright Blog):
    
    - **Current**: Three consecutive Kluwer blog citations
    - **Fix**: Check whether any have been published in traditional academic outlets
    - If not, keep but acknowledge: "Academic commentary on this emerging issue has appeared primarily in blog format pending traditional publication..."
3. **Footnote 72** (_UsedSoft_):
    
    - **DELETE** from reverse engineering discussion
    - **REPLACE** with Art 5(3), Art 6 Software Directive directly, _SAS Institute_, _Top System_
4. **General citation check**:
    
    - Ensure all "accessed" dates consistent format
    - Parallel citations where appropriate
    - Verify all ECLI numbers correct
    - Check all paragraph references accurate

---

### **Task 3.3: CRITICAL DOCTRINAL PRECISION FIXES**

**These are the six issues identified in the critique—implement systematically:**

#### **Fix 3.3.1: Levola/Identifiability** (Already handled in Task 1.1)

- ✅ Deleted Part D entirely
- ✅ Non-determinism moved to preparatory material discussion

#### **Fix 3.3.2: Brompton Bicycle**

**Location**: Part B (merged B+C), section on complex prompts

**Current problematic phrasing**:

> "Even where some flexibility exists in word choice, _Brompton Bicycle_ establishes that predominant functional constraint suffices to defeat originality."

**Corrected phrasing**:

> "Under _Football Dataco_, functional constraints narrow the space for creative choices—the more constraints dictate outcomes, the harder it is to demonstrate the 'personal touch' originality requires. The CJEU in _Brompton Bicycle_ held that where technical considerations leave 'no room for creative freedom,' originality fails. This is not a 'predominance' test but rather asks whether meaningful creative latitude exists despite functional requirements."

**Throughout Part B**:

- Don't claim _Brompton_ establishes "predominance" standard
- Anchor in _Football Dataco_: constraints narrow space
- Add merger: "For many prompt elements, constraints narrow space to the point of merger—virtually no room for meaningful choice remains"
- Use _Brompton_ more modestly: supports framework but doesn't establish new lower threshold

**Specific search-and-replace**:

- Find: "predominant functional constraint suffices"
- Replace: "where functional constraints leave virtually no room for creative freedom"

#### **Fix 3.3.3: BSA Two-Track Structure**

**Location**: Part E, section on interfaces

**Add new paragraph** (250 words) immediately after framework introduction:

> "A critical clarification: the Software Directive and InfoSoc Directive operate on separate tracks. Subject matter may be excluded as 'expression of a computer program' under Software Directive Art 1(2) yet still potentially qualify for protection as another work category under the InfoSoc Directive. In _BSA_, the CJEU held that GUIs do not constitute protected expression of computer programs, but acknowledged they may qualify as graphic or artistic works under InfoSoc if original. This two-track structure means that even if prompts are excluded under Software Directive Art 1(2), we must still examine whether they qualify as literary works under InfoSoc."

**Revise BSA discussion**:

- **Current**: "GUIs are not protected because they are user-facing interaction mechanisms"
- **Revised**: "GUIs are not protected _as computer programs_ because they are user-facing mechanisms for interaction, not program expression itself. However, they may be protected as artistic works if original."
- **Add for prompts**: "Unlike GUIs, which can have autonomous visual/artistic content, prompts typically consist of functional instructions lacking the creative literary expression necessary for InfoSoc literary work protection (as demonstrated in Part B)."

**Conclusion to BSA section**:

> "Prompts are excluded as program expression under Software Directive Art 1(2). They independently fail originality requirements for literary works under InfoSoc Directive (Part B). Both tracks converge on exclusion."

#### **Fix 3.3.4: SAS Institute Bridge**

**Location**: Part E, section on functionality

**Current problematic phrasing**:

> "If formal programming languages...are unprotectable ideas and principles...then natural language prompts are equally unprotectable."

**Add bridging paragraph** (150 words):

> "The argument that natural language prompts function like programming languages requires careful doctrinal foundation. _SAS Institute_ concerned a formal programming language designed specifically for instructing computers. One might object that prompts—natural language inputs to AI—differ categorically.
> 
> "However, the stronger doctrinal foundation doesn't depend on this metaphorical equivalence. Software Directive Art 1(2) excludes 'ideas and principles underlying any element of a computer program, including those which underlie its interfaces.' Even if prompts are not themselves 'programming languages' in the technical sense, they constitute methods and principles for using AI system interfaces—precisely what Art 1(2) excludes from protection. The _SAS Institute_ functionality reasoning applies: protecting the method of communicating with a system would monopolize ideas to the detriment of technological progress."

**Then continue** with current analysis about Python commands vs. prompts, but frame as additional support rather than primary argument.

#### **Fix 3.3.5: Sony Datel Precision**

**Location**: Part E, section on data inputs

**Add precision at opening** (100 words):

> "The Court's holding should be stated precisely: protection under the Software Directive covers textual forms (source code, object code) that enable reproduction or subsequent creation of the program. Variable contents stored in RAM during program execution, which do not enable program reproduction, fall outside Art 1 protection. This does not mean all data inputs are necessarily unprotected—the holding is specifically that data inputs which neither constitute the program's textual form nor enable its reproduction are excluded from Software Directive coverage."

**Strengthen analogy paragraph** (150 words):

> "Prompts function analogously to RAM variables in critical respects. Both are:
> 
> - Ephemeral: exist temporarily during system operation
> - User-controlled: determined by users, not inherent to program
> - Behavioral modifiers: affect how pre-existing program operates at runtime
> - Non-reproductive: do not enable reproduction of the program itself
> 
> "RAM variables control video game behavior by modifying computational state; prompts control AI behavior by specifying processing parameters. Neither constitutes the program expression—both are external inputs to existing systems. Just as RAM values invoke existing game code without reproducing it, prompts invoke existing AI model computations without reproducing the model."

#### **Fix 3.3.6: UsedSoft Citation Error**

**Location**: Part G, policy section

**DELETE** (currently in Task 2.2):

> "UsedSoft confirmed that interface information necessary for interoperability must remain accessible even when obtained through reverse engineering."

**REPLACE WITH** (250 words):

> "Software Directive Arts 5(3) and 6 explicitly grant lawful acquirers rights to observe, study, and test programs to determine functionality. Art 5(3) permits observation, study, or testing of a program 'in order to determine the ideas and principles which underlie any element of the program' when done 'while performing any of the acts of loading, displaying, running, transmitting or storing the program which he is entitled to do.' Art 6 permits decompilation when necessary to achieve interoperability with independently created programs.
> 
> "The CJEU has interpreted these provisions expansively. In _SAS Institute_, the Court confirmed that studying program functionality to understand interfaces is permitted. In _Top System_ (C-13/20), the Court held that error correction under Art 5(1) extends broadly to lawful acquirers. These decisions reflect a policy choice: users must be free to understand and work with interfaces of programs they lawfully access.
> 
> "Applied to prompts: when users experiment with AI systems to discover which instructions produce desired outputs, they engage in precisely the interface exploration that Arts 5(3) and 6 protect. Technical research on prompt extraction demonstrates that prompts can be reverse-engineered from outputs by analyzing response patterns—this constitutes lawful reverse engineering under both the Software Directive and Directive 2016/943 on trade secrets (which permits reverse engineering of lawfully acquired products). Granting copyright protection to prompts would create legal barriers to this interface learning that EU policy deliberately protects."

---

### **Task 3.4: Strengthen Weak Passages & Improve Flow**

**Priority areas beyond those already addressed**:

1. **Introduction to Part B** (merged simple/complex prompts):
    
    - Add signposting: "We examine simple prompts first, then engage seriously with the hardest case—complex system prompts—to demonstrate why even substantial length and apparent sophistication fail the originality threshold."
2. **Transition from Part B to Part E**:
    
    - Current section break may feel abrupt
    - Add bridge: "Even if prompts could satisfy originality requirements (which Part B demonstrates they cannot), they face independent exclusion under the idea-expression dichotomy as operationalized through the Software Directive."
3. **Part E subsection transitions**:
    
    - Each CJEU case needs brief transition showing how it builds on previous
    - After _BSA_: "The exclusion of interfaces complements a broader exclusion of functionality itself, addressed in _SAS Institute_."
    - After _SAS Institute_: "Beyond interfaces and functionality, the Court has excluded variable data inputs from program expression, as _Sony Datel_ confirms."
4. **Part K opening**:
    
    - Current: "The analysis has established multiple grounds..."
    - Better: "The foregoing analysis demonstrates multiple converging grounds for exclusion. We now examine the strongest affirmative arguments—not to dismiss them, but to show why they fail to overcome these structural barriers."
5. **Connection from counterarguments to database protection**:
    
    - Add explicit transition: "Having addressed arguments for individual prompt protection, we turn to whether collections of prompts might receive database protection—a distinct form of protection with its own requirements."

---

### **Task 3.5: Final Consistency Check**

**Actions**:

1. **Terminology consistency**:
    
    - "Prompt" vs "AI prompt" vs "textual prompt"—choose one
    - "System prompt" vs "elaborate prompt" vs "complex prompt"—be consistent
    - "AI system" vs "AI model" vs "large language model"—choose appropriate level of generality
2. **Case citation consistency**:
    
    - First mention: full case name with case number
    - Subsequent: short form ("the Court held," "_SAS Institute_ established")
    - Ensure consistent
3. **Cross-reference check**:
    
    - "As established in Part B" / "examined below in Part G"
    - After reorganization, ensure all cross-references accurate
4. **Footnote formatting**:
    
    - Check OSCOLA compliance throughout
    - Ibid usage correct
    - Parallel citations where needed
5. **Signal words**:
    
    - "First," "Second," "Third"—ensure sequences complete
    - "Moreover," "Furthermore," "Additionally"—don't overuse
    - "However," "Nevertheless," "Nonetheless"—vary

---

## WORD COUNT SUMMARY (UPDATED)

|Section|Current|Target|Change|Notes|
|---|---|---|---|---|
|**A. Originality Standard**|1,400|1,000|-400|Streamline, move term discussion|
|**B. Application to Prompts** (merged B+C)|3,200|1,800|-1,400|Acknowledge hard case, add Brompton fix|
|**D. Identifiability**|800|DELETE|-800|Fundamental misapplication of _Levola_|
|**E. Software Directive** (merged E+F)|4,100|2,500|-1,600|Add two-track clarification, fix all 6 doctrinal issues|
|**G. Policy**|1,200|1,100|-100|Add access-to-justice, fix UsedSoft, net +150 acceptable|
|**H. Scholarly Commentary**|800|450|-350|Add acknowledgment of debate|
|**J. Database Protection**|1,600|1,200|-400|Keep _BHB_ analysis strong|
|**K. Counterarguments**|1,800|1,600|-200|Make more charitable|
|**L. Synthesis**|1,200|400|-800|Radical compression|
|**M. Exceptional Cases**|600|450|-150|Tighten but keep structure|
|**Line-editing reductions**|—|—|-300|Repetitive phrases|
|**TOTAL**|~11,000|~7,100|**-3,900**|Slightly over target but necessary for doctrinal fixes|

---

## EXECUTION ORDER (REVISED)

### **Week 1: Major Surgery + Critical Doctrinal Fixes**

**Days 1-2**:

1. Delete Part D entirely (Task 1.1)
2. Implement all six doctrinal fixes systematically (Task 3.3):
    - ✅ Levola (already handled by deletion)
    - Add two-track structure paragraph to Part E
    - Fix all Brompton "predominance" language in Part B
    - Add SAS Institute bridge paragraph
    - Add Sony Datel precision paragraphs
    - Replace UsedSoft with correct citations

**Days 3-4**: 3. Merge B+C into unified Part B (Task 1.2) 4. Merge E+F into unified Part E (Task 1.3)

**Days 5-7**: 5. Compress Part L to 400 words (Task 2.6) 6. First pass line-editing for repetitive phrases (Task 3.1)

**Result**: ~2,900 words removed + all critical doctrinal fixes implemented

---

### **Week 2: Refinement & Strengthening**

**Days 8-10**: 7. Tighten Parts A, H, J, M per targets (Tasks 2.1, 2.3, 2.4, 2.7) 8. Strengthen Part G with access-to-justice content (Task 2.2) 9. Make Part K more charitable (Task 2.5)

**Days 11-14**: 10. Fix all citation issues systematically (Task 3.2) 11. Improve weak passages and transitions (Task 3.4)

**Result**: ~800 more words removed, new substantive content added, citations corrected

---

### **Week 3: Polish & Final Review**

**Days 15-17**: 12. Final line-edit for repetitive phrases (Task 3.1 completion) 13. Consistency check (Task 3.5): - Terminology - Case citations - Cross-references - Footnote formatting - Signal words

**Days 18-21**: 14. Read entire chapter aloud for flow 15. Check every doctrinal claim against case law 16. Verify all six doctrinal fixes implemented correctly 17. Final word count check 18. Prepare for submission

**Result**: Final ~300 words removed, overall quality dramatically improved, all doctrinal issues addressed

---

## PRIORITY RANKING (UPDATED)

### **CRITICAL (Do First—Week 1)**

- Task 1.1: Delete Part D (Levola misapplication)
- Task 3.3: Implement all six doctrinal fixes systematically
    - **Most critical**: Two-track structure, Brompton softening, UsedSoft removal
- Task 1.2: Merge B+C
- Task 1.3: Merge E+F

### **HIGH PRIORITY (Week 2)**

- Task 2.2: Strengthen policy with access-to-justice + fix UsedSoft
- Task 2.5: Make counterarguments charitable
- Task 3.2: Fix all citation issues
- Task 2.6: Compress synthesis

### **MEDIUM PRIORITY (Week 2-3)**

- Tasks 2.1, 2.3, 2.4, 2.7: Standard tightening
- Task 3.4: Strengthen weak passages
- Task 3.1: Repetitive phrase elimination

### **POLISH (Week 3)**

- Task 3.5: Final consistency check

---

## QUALITY CONTROL CHECKLIST

Before considering revision complete, verify:

**Doctrinal Issues (All Six Fixed)**:

- [ ] _Levola_ identifiability section deleted
- [ ] Two-track structure (Software Directive vs. InfoSoc) explicitly explained in Part E
- [ ] _Brompton_ no longer claims "predominance" test—softened to _Football Dataco_ framework
- [ ] _SAS Institute_ bridge improved—not solely relying on "prompts = programming languages"
- [ ] _Sony Datel_ ratio stated precisely, analogy explicit
- [ ] _UsedSoft_ removed from reverse engineering discussion, replaced with Art 5(3), Art 6, _SAS Institute_, _Top System_

**Structural**:

- [ ] Parts B+C successfully merged into coherent unit
- [ ] Parts E+F successfully merged into coherent unit
- [ ] Part L compressed to ~400 words without losing core message
- [ ] All cross-references updated after reorganization

**Tone & Engagement**:

- [ ] Part K counterarguments acknowledge strengths before rebutting
- [ ] Complex prompts (Part B) treated as "hard case" deserving serious engagement
- [ ] Acknowledges scholarly debate isn't unanimous (Part H)

**Citations**:

- [ ] Czech Municipal Court source improved or caveated
- [ ] Kluwer blog reliance acknowledged or improved
- [ ] _UsedSoft_ citation error corrected
- [ ] All "accessed" dates consistent
- [ ] All ECLI numbers verified

**Length**:

- [ ] Target ~7,000-7,100 words achieved
- [ ] ~36% reduction from original
- [ ] No critical analysis lost

**Polish**:

- [ ] Terminology consistent throughout
- [ ] Repetitive phrases eliminated
- [ ] Transitions smooth
- [ ] Readable aloud without awkwardness

---

Does this comprehensive plan capture everything? Any sections you want to adjust or clarify?