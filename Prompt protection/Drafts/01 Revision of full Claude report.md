# Combined Copyright Chapter (Revised)

## Does EU law protect AI prompts as intellectual property?

Consider three prompts. First: "Summarize." Second: "Write a formal business letter declining a job offer, emphasizing gratitude for the opportunity while explaining the decision is based on accepting a position better aligned with long-term career goals in environmental policy." Third: a 400-word system prompt specifying tone, vocabulary constraints, citation formats, rhetorical strategies, prohibited topics, required factual accuracy standards, and iterative refinement protocols.

The question this Article asks is whether any of these—ranging from the trivial to the elaborate—can constitute works protected by copyright under European Union law.

The question matters because generative AI has created a novel category of potentially protectable subject matter. Commercial prompt marketplaces have proliferated—PromptBase reports over 370,000 users trading more than 220,000 prompts. Prompt engineering has emerged as a recognized skill commanding premium pricing. Yet the legal status remains uncertain.

This Article examines prompt protectability under four EU intellectual property frameworks: copyright law, software and database protection, patent law, and trade secrets.

The analysis proceeds by elimination. Part II establishes why prompts merit protection consideration—demonstrating investment, commercial value, creative labor, and appropriability concerns that justify legal analysis. Part III examines copyright protection, showing that prompts fail the harmonized originality standard because they constitute instructions about what to create rather than creative expression itself. Part IV addresses software and database protection. Part V considers patent protection. Part VI turns to trade secrets.

The conclusion is straightforward: while prompts theoretically could receive protection under trade secrets and, in exceptional cases, copyright, significant doctrinal obstacles exist under each regime. Most fundamentally, prompts constitute instructions describing ideas rather than expressing those ideas—placing them in tension with the foundational principle that intellectual property law does not protect abstract concepts.

## II. Why legal protection merits consideration

Before examining whether prompts receive protection, the threshold question is simpler: why would protection be justified?

Four rationales emerge.

### Investment and skill acquisition

Prompt engineering requires non-intuitive skill. Academic research by Oppenlaender and colleagues demonstrates empirically that while participants could evaluate prompt quality, they lacked the style-specific vocabulary and technical knowledge necessary for effective prompting.[^1] The study confirms that prompt engineering must be acquired through practice rather than being immediately accessible to any AI user.

The investment manifests in multiple forms. Time spent on iterative testing represents direct costs—sources document significant expenditure on trial-and-error experimentation with different formulations, parameter combinations, and phrasing strategies.[^2] Acquisition of technical knowledge about model architectures, attention mechanisms, and tokenization patterns requires study. Formal training through prompt engineering courses has become a commercial industry, with platforms charging €500–€2,000 for structured instruction.[^3]

This human capital investment creates economic value. Under traditional intellectual property theory, investment in skill development and knowledge creation justifies protection to incentivize continued innovation and prevent free-riding on others' expenditure.[^4]

[^1]: J. Oppenlaender, 'The Creativity of Text-to-Image Generation' (2022) Proceedings of the 25th International Academic Mindtrek Conference 192, 196–197 https://doi.org/10.1145/3569219.3569352.

[^2]: ibid 197 (documenting iterative refinement processes); see also M. Liu and others, 'Design Guidelines for Prompt Engineering Text-to-Image Generative Models' (2022) Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems 1, 8–9 https://doi.org/10.1145/3491102.3501825.

[^3]: See PromptHero, 'Prompt Engineering Courses' <https://prompthero.com/courses> accessed 15 October 2024 (listing courses at $199–$499).

[^4]: W.M. Landes and R.A. Posner, 'An Economic Analysis of Copyright Law' (1989) 18 Journal of Legal Studies 325, 326–328 (articulating incentive theory for IP protection).

### Commercial value and market evidence

The rapid emergence of commercial prompt marketplaces provides empirical evidence of economic value.

PromptBase, launched in June 2022 as the first major marketplace, reports over 370,000 users and more than 220,000 prompts available for purchase.[^5] Listed prices range from €1.99 to €4.99, with the platform retaining a 20% commission. Other marketplaces have followed: ChatX pays 39 CAD per accepted prompt submission; PromptHero offers millions of AI art images with visible prompts plus educational courses; PromptScoop features testimonials claiming €30,000 monthly earnings from prompt sales.[^6]

These platforms demonstrate a functioning market. Supply meets demand at non-trivial price points. Transaction volumes suggest genuine economic value rather than speculative trading.

Beyond direct sales, businesses derive competitive advantage from proprietary prompt libraries. Marketing agencies use optimized prompts to ensure consistent brand messaging across AI-generated content. Legal practices develop prompts that generate compliance-consistent document drafts. Software companies embed carefully calibrated prompts that define their AI assistants' behavior and personality. For enterprises using AI-powered services, optimized prompts represent cost savings through reduced token usage and improved first-attempt success rates—directly reducing API costs that scale with token consumption.[^7]

To that extent, prompts function as business assets with quantifiable value.

[^5]: PromptBase, 'About' <https://promptbase.com/about> accessed 15 October 2024.

[^6]: ChatX <https://chatx.ai>; PromptHero <https://prompthero.com>; PromptScoop <https://promptscoop.com> all accessed 15 October 2024.

[^7]: See OpenAI, 'Pricing' <https://openai.com/api/pricing> accessed 15 October 2024 (documenting token-based pricing where GPT-4 costs $0.03 per 1,000 prompt tokens).

### Creative and intellectual labor

The creative dimension of prompt engineering has been examined through computational creativity frameworks. Research by Bird evaluates prompts against established creativity theories, identifying novelty and value generation in sophisticated prompt construction.[^8]

Simple prompts offer limited creative choices. The instruction "create an image of a cat" involves minimal selection beyond the obvious words necessary to convey the concept.

Complex prompts differ. They involve selection of precise vocabulary that guides aesthetic outcomes; sequencing of instructions that determines how the model processes directives; strategic use of examples that anchor the model's interpretation; calibration of technical parameters (temperature, top-p sampling, frequency penalties) that shape output characteristics. These choices could reflect the personality and creative judgment of the prompt engineer—the same qualities that distinguish one technical writer's instruction manual from another's.[^9]

DLA Piper's legal analysis notes that sophisticated prompts "can be traced back to the creativity and personality of their author," drawing an analogy to technical writing that receives copyright protection despite its functional purpose.[^10] The intellectual labor extends beyond mere word choice to understanding AI model behaviors, anticipating failure modes, and crafting prompts that navigate the complex semantic space of large language models.

Put differently, prompt engineering resembles other forms of skilled communication—legal drafting, technical specification writing, search query formulation—where expertise produces value through precise use of language within constrained systems.

[^8]: S. Bird, 'Are Large Language Models Capable of Creative Cognition? An Analysis of Generative AI Using the Creative Cognition Approach' (2023) arXiv:2308.12626, 8–11.

[^9]: ibid 9–10 (discussing parameter selection as creative choice); see also Liu and others (n 2) 10–11 (documenting sophisticated prompt design patterns).

[^10]: DLA Piper, 'Copyright Protection for AI Prompts: The Next Frontier in Generative AI?' (2023) <https://www.dlapiper.com/insights/publications/2023/06/copyright-protection-for-ai-prompts> accessed 15 October 2024.

### Appropriability and free-riding

Without intellectual property protection, information asymmetry creates market dynamics that may discourage prompt development.

Once disclosed—whether through marketplace sales, through use in generating visible outputs, or through employee departure—a prompt becomes immediately copyable by competitors. Unlike physical goods or most digital products that require manufacturing capability or technical implementation, prompts are pure information. A string of text that can be copied instantly at zero marginal cost.

This creates severe appropriability problems. The developer invests time and resources upfront—weeks or months testing formulations, acquiring technical knowledge, refining outputs. But competitive advantage dissipates upon disclosure. Competitors can copy the prompt, make superficial modifications, and offer competing services without bearing development costs.

The temporal element matters. Investment occurs upfront. Returns depend on maintaining informational advantage. Disclosure destroys that advantage immediately and completely.

Trade secret protection partially addresses this through secrecy maintenance, but many commercial applications require prompt use in contexts where outputs are visible. Generated images may contain metadata revealing prompt structures. Generated text may exhibit patterns that enable reconstruction. Customer-facing AI services must disclose system behavior, potentially revealing underlying prompts. In these contexts, secrecy becomes difficult or impossible to maintain.[^11]

To that extent, standard appropriability theory suggests that some form of legal protection might be economically justified to prevent market failure.

[^11]: See Part VI below (analyzing secrecy challenges in commercial prompt use).

---

These four rationales establish the economic and policy case for considering legal protection.

The case is not absolute. Countervailing concerns exist: the risk of restricting access to AI technology through monopolization of basic communication methods; the danger of creating barriers to AI adoption by making users uncertain whether their prompts infringe others' rights; the fundamental question of whether prompts represent sufficiently original contributions to merit exclusive rights.

The strength of protection arguments varies dramatically with prompt complexity. Simple instructions like "Summarize" present minimal investment and negligible creativity. Sophisticated multi-paragraph prompts with specific technical parameters, carefully crafted examples, and strategic keyword sequencing might cross the threshold justifying protection.

With these economic foundations established, the analysis turns to examining whether—and how—existing EU legal frameworks accommodate prompt protection.

## III. Copyright protection: why prompts fail the originality standard

The question of whether prompts qualify for copyright protection under EU law requires analysis of the harmonized originality standard as interpreted by the Court of Justice of the European Union, application of the idea-expression dichotomy fundamental to copyright doctrine, and assessment of whether prompts constitute protectable expression or merely unprotectable instructions.

### The harmonized originality test and its requirements

EU copyright law has converged on a unified originality standard applicable to all categories of works.

The foundational provision appears in Article 1(3) of Directive 2009/24/EC (Software Directive), which provides that "a computer program shall be protected if it is original in the sense that it is the author's own intellectual creation. No other criteria shall be applied to determine its eligibility for protection."[^12]

The Court of Justice has extended this standard beyond software to all copyrightable subject matter. In *Infopaq International v Danske Dagblades Forening*, the Court held at paragraph 37 that "copyright within the meaning of Article 2(a) of Directive 2001/29 is liable to apply only in relation to a subject-matter which is original in the sense that it is its author's own intellectual creation."[^13] This represents a harmonized standard displacing earlier national variations in originality thresholds.

The Court has articulated this standard through several cumulative requirements that any work must satisfy.

[^12]: Directive 2009/24/EC of the European Parliament and of the Council of 23 April 2009 on the legal protection of computer programs [2009] OJ L111/16, art 1(3).

[^13]: Case C-5/08 Infopaq International v Danske Dagblades Forening EU:C:2009:465, para 37.

**First, the work must reflect the author's personality.** As the Court stated in *Painer v Standard Verlags* at paragraph 88, "an intellectual creation is an author's own if it reflects the author's personality."[^14] This personalizing requirement distinguishes copyright from patent or design protection focused on technical or aesthetic function.

**Second, the author must have exercised free and creative choices.** The *Painer* judgment continues at paragraph 89 that this occurs "if the author was able to express his creative abilities in the production of the work by making free and creative choices."[^15] The Court provided concrete examples in the photographic context: selection of background, pose of subject, lighting, angle, and subsequent processing decisions. Each choice permits the photographer to stamp the work with a "personal touch."[^16]

**Third, where technical considerations, rules, or constraints dictate expression, originality cannot be found.** The Court established this limitation in *BSA v Ministerstvo kultury* at paragraph 50: "where the expression of those components is dictated by their technical function, the criterion of originality is not met, since the different methods of implementing an idea are so limited that the idea and the expression become indissociable."[^17]

This principle was refined in *Brompton Bicycle v Chedech* at paragraph 24, where the Court held that "where the realisation of a subject matter has been dictated by technical considerations, rules or other constraints which have left no room for creative freedom, that subject matter cannot be regarded as being original."[^18] Even where a product's shape is partly necessary to obtain a technical result, copyright may apply if the shape nonetheless permits the author to express creative ability through free choices reflecting personality.

**Fourth, only expression receives protection, never ideas or principles.** Article 1(2) of the Software Directive provides explicitly that "ideas and principles which underlie any element of a computer program, including those which underlie its interfaces, are not protected by copyright under this Directive."[^19]

The Court emphasized this limitation in *BSA* at paragraph 49: "only the expression of a computer program is so protected, whereas ideas and principles which underlie any element of that program, including those which underlie its interfaces, are not."[^20] In *Infopaq* at paragraphs 45–46, the Court held that while "words, considered in isolation, are not as such an intellectual creation of the author who employs them," protection arises only through "the choice, sequence and combination of those words" that expresses creativity in an original manner.[^21] Critically, "words as such do not, therefore, constitute elements covered by the protection."

[^14]: Case C-145/10 Painer v Standard Verlags EU:C:2011:798, para 88.

[^15]: ibid para 89.

[^16]: ibid paras 90–91.

[^17]: Case C-393/09 BSA v Ministerstvo kultury EU:C:2010:816, para 50.

[^18]: Case C-833/18 Brompton Bicycle v Chedech EU:C:2020:461, para 24.

[^19]: Software Directive (n 12) art 1(2).

[^20]: *BSA* (n 17) para 49.

[^21]: *Infopaq* (n 13) paras 45–46.

The Court consolidated these principles in *Cofemel v G-Star Raw*, confirming at paragraph 29 that "a subject matter can be classified as a 'work' within the meaning of Directive 2001/29 only if it is an original subject matter in that it is the author's own intellectual creation."[^22] At paragraph 30, the Court clarified that "the assessment of the originality of a subject matter is therefore primarily based on whether that subject matter reflects the personality of its author, as an expression of his or her free and creative choices."[^23]

Crucially, the Court held in *Cofemel* that national legislation cannot confer copyright protection based on criteria other than originality—aesthetic effect or applied art status, for example—without violating the harmonized standard.[^24]

[^22]: Case C-683/17 Cofemel v G-Star Raw EU:C:2019:721, para 29.

[^23]: ibid para 30.

[^24]: ibid paras 31–32.

### Application to simple prompts

With the legal test established, the critical question becomes whether AI prompts satisfy these cumulative requirements.

For the one-word prompt "Summarize," the answer is straightforward and negative.

Single words are explicitly excluded from copyright protection. As the Court held in *Infopaq*, "words as such do not constitute elements covered by the protection" because "it is only through the choice, sequence and combination of those words that the author may express his creativity in an original manner."[^25] No creative choices are evident in selecting the single word "Summarize" to instruct an AI to perform summarization. The selection is dictated entirely by the functional goal of conveying a standard instruction.

Moreover, even if one imagined minimal creativity in word choice, the prompt would fail the requirement articulated in *Football Dataco v Yahoo! UK* that originality cannot arise from "significant labour and skill" alone but only from choices "through which its author expresses his creative ability in an original manner by making free and creative choices" reflecting personality.[^26]

To that extent, simple one-word or brief prompts fail decisively.

[^25]: *Infopaq* (n 13) paras 45–46.

[^26]: Case C-604/10 Football Dataco v Yahoo! UK EU:C:2012:115, para 38.

The intermediate prompt presents a more complex case but reaches the same conclusion.

Consider: "Write a formal business letter declining a job offer, emphasizing gratitude for the opportunity while explaining the decision is based on accepting a position better aligned with long-term career goals in environmental policy." This 33-word prompt involves choices in framing, sequencing, and specification—the author chose to request a "formal" letter, to emphasize "gratitude," to specify the explanation structure, and to particularize the career field as "environmental policy."

Do these choices suffice to meet the *Infopaq* standard?

The critical question is whether the choices reflect creative freedom or functional necessity. In the language of *Football Dataco*, whether "the setting up" of the prompt "is dictated by technical considerations, rules or constraints which leave no room for creative freedom."[^27]

Functional constraints dominate. The prompt's purpose is to convey instructions, and the specifications respond to practical requirements for generating useful output. The author's "creative choices" reduce to selecting among conventional descriptive terms for standard concepts. The instruction to write a "formal" rather than "casual" letter reflects the desired output characteristics rather than creative literary choice. The specification of "gratitude" and "career goals" describes the functional requirements of the communication rather than stamping the prompt with the author's personality.

Put differently, these are choices about what the AI should do—the idea or method of operation—not expressions of the author's creative vision through language selected for its aesthetic or literary qualities.

[^27]: *Football Dataco* (n 26) para 39.

### Application to complex prompts

The extensive system prompt—400 words specifying tone, vocabulary constraints, citation formats, rhetorical strategies, prohibited topics, accuracy standards, and refinement protocols—presents the strongest candidate for copyright protection based on length and apparent complexity.

Academic analysis of national court practice reveals that courts generally find longer texts more likely to exhibit originality because greater length provides more scope for individual creative choices. The German Bundesgerichtshof has held that even functional texts like operating instructions may be protected where they "deutlich überragen der Durchschnittsgestaltung"—distinctly exceed average design—through creative arrangement beyond routine formulation.[^28]

However, three fundamental obstacles remain.

[^28]: Bundesgerichtshof [1993] GRUR 34 (Bedienungsanleitung).

**First, prompts are instructions about what to create, not the expression itself.** This implicates the core idea-expression dichotomy.

A prompt stating "create an impressionist-style painting of the Eiffel Tower at sunset, with warm orange and pink tones, soft brushstrokes suggesting movement, positioned at right third of composition following rule of thirds, with foreground figures in shadow to create depth" is elaborate. But it remains an instruction specifying the idea of what the AI should generate. The resulting AI-generated image would be the expression—if it qualifies as expression at all.

Protecting the prompt would grant rights over the idea or concept described. The Court has been emphatic: ideas, including those underlying interfaces and interaction methods, receive no copyright protection.[^29]

The relevant parallel is to functional specifications and instructions in other domains. French courts have consistently held that cooking recipes constitute "succession of instructions, a method" belonging to the category of unprotectable know-how rather than intellectual works.[^30] Copyright may protect creative literary description accompanying recipes—vivid prose, personal anecdotes, evocative explanations—but not the functional list of ingredients or procedural steps, which remain free for all to use. In *Levola Hengelo v Smilde Foods*, Advocate General Wathelet emphasized in his opinion that "copyright does not protect the recipe as such (the idea)" because "copyright protection extends to original expressions and not to ideas, procedures, methods of operation."[^31]

Similarly, the abstract rules of a game constitute unprotectable methods and procedures, though the creative literary expression of those rules in a rulebook may be protected. Anyone can create a game with identical rules by expressing those rules differently.[^32]

Operating instructions present the same pattern. The German Bundesgerichtshof has consistently held that simple operating manuals—"Press button A, then B"—constitute unprotectable procedures, with copyright attaching only to substantial creative expression in the arrangement or explanation of functional information.[^33]

Prompts bear the same relationship to AI systems that recipes bear to cooking, game rules bear to gameplay, and operating instructions bear to equipment use. They describe what should be done, what functions should be performed, what constraints should be observed. The fact that prompts are written in natural language rather than formal notation does not alter their functional character—they remain instructions about methods and procedures of operation rather than literary expressions for their own sake.

[^29]: *BSA* (n 17) para 49.

[^30]: Cour de Cassation [1974] Bulletin civil IV n° 267 (holding recipes are "succession of instructions, a method").

[^31]: Case C-310/17 Levola Hengelo v Smilde Foods EU:C:2018:899 (Opinion of AG Wathelet) para 40.

[^32]: See generally P.B. Hugenholtz and others, 'The Recasting of Copyright & Related Rights for the Knowledge Economy' (Institute for Information Law, 2006) 33–34 (discussing game rules as unprotectable methods).

[^33]: Bundesgerichtshof (n 28).

**Second, prompts are functionally dictated by their purpose: communicating instructions to AI systems.**

The *BSA* principle that "where the expression of those components is dictated by their technical function, the criterion of originality is not met" applies with particular force.[^34] A prompt's purpose is to effectively communicate with an AI model to achieve a desired output. This functional purpose constrains expression significantly.

While some word choice flexibility exists, the prompt must use language the AI model will process effectively. It must specify parameters in ways the system recognizes. It must structure instructions for optimal results. These technical constraints reduce the space for free and creative choices.

Many prompt elements—parameter specifications, formatting conventions, strategic keyword placement—are dictated by AI model requirements rather than creative choice. The prompt engineer learns, through experimentation, which phrasings produce desired effects. That learning reflects skill and investment, but not necessarily the free creative choices reflecting personality that *Painer* and *Cofemel* require.[^35]

As the *Brompton Bicycle* decision clarified, even when some creative freedom remains, if "the realisation of a subject matter has been dictated by technical considerations, rules or other constraints which have left no room for creative freedom," originality fails.[^36]

This analysis proceeds on functional similarity. The constraint is not mechanical determination but functional optimization—the prompt's structure and content are shaped by what works to elicit desired AI behaviors rather than by expressive choices that stamp the author's personality on the work. The fact that effective prompt engineering requires skill, knowledge, and iterative refinement does not transform prompts into creative works. The Court's *Football Dataco* precedent is dispositive: "the fact that the setting up of the database required...significant labour and skill of its author...cannot as such justify the protection of it by copyright" where "that labour and that skill do not express any originality in the selection or arrangement."[^37]

[^34]: *BSA* (n 17) para 50.

[^35]: *Painer* (n 14) para 89; *Cofemel* (n 22) para 30.

[^36]: *Brompton Bicycle* (n 18) para 24.

[^37]: *Football Dataco* (n 26) para 42.

**Third, prompts raise merger concerns where limited ways exist to express particular instructions.**

When there are only a few ways to convey a specific instruction to an AI system, the expression merges with the idea, and copyright protection must be denied to prevent monopolization of the idea itself.

Instructing an AI to "make the image brighter" or "write in a professional tone" or "use active voice" can be expressed in only limited ways that effectively communicate with AI systems. "Make the image brighter" could be rephrased as "increase brightness" or "brighten the image," but these are functionally equivalent formulations differing only in trivial word choice. Protecting any of these formulations would effectively monopolize the underlying instruction itself.

European copyright doctrine, while not using the term "merger doctrine" explicitly, recognizes this principle through the *BSA* holding that where methods of implementing an idea are so limited that idea and expression become indissociable, no protection attaches.[^38] As the *BSA* decision emphasized, "to accept that the functionality of a computer program can be protected by copyright would amount to making it possible to monopolise ideas, to the detriment of technological progress and industrial development."[^39]

Even for more elaborate prompts, the specifications respond to functional requirements. Specifying "formal tone" rather than "casual tone," requesting "Chicago citation style" rather than "MLA citation style," or setting "temperature at 0.3" rather than "temperature at 0.7" reflects optimization choices dictated by desired output characteristics. These are functional parameters selected for their effects on AI behavior, not creative expressions reflecting the author's personality.

To that extent, the range of possible expressions narrows toward what is functionally necessary, and copyright protection becomes inappropriate because it would enable monopolization of the functional method itself.

[^38]: *BSA* (n 17) para 50.

[^39]: ibid para 48.

---

By elimination, complex prompts—like simple ones—fail the EU originality standard.

The fundamental obstacles are insurmountable: prompts are instructions describing ideas about what to create rather than creative expression itself; they are functionally constrained by their communicative purpose; and protecting them would risk monopolizing ideas in violation of core copyright principles.

### The idea-expression dichotomy as dispositive barrier

The principle that copyright protects expression but not underlying ideas, procedures, or methods of operation has constitutional status in EU copyright law.

Article 9(2) of the TRIPS Agreement—to which the EU is party through its WTO membership—states explicitly that "copyright protection shall extend to expressions and not to ideas, procedures, methods of operation or mathematical concepts as such."[^40] The WIPO Copyright Treaty, which the EU has implemented through the InfoSoc Directive, contains an identical provision in Article 2.[^41]

The Software Directive operationalizes this principle in Article 1(2), providing that "ideas and principles which underlie any element of a computer program, including those which underlie its interfaces, are not protected by copyright under this Directive."[^42] Recital 11 elaborates that "only the expression of a computer program is protected and that ideas and principles which underlie any element of a program, including those which underlie its interfaces, are not protected by copyright."[^43]

The Court has treated this as fundamental to copyright's proper scope across all work categories.

[^40]: Agreement on Trade-Related Aspects of Intellectual Property Rights [1994] art 9(2).

[^41]: WIPO Copyright Treaty (adopted 20 December 1996, entered into force 6 March 2002) art 2.

[^42]: Software Directive (n 12) art 1(2).

[^43]: ibid recital 11.

In *SAS Institute Inc v World Programming Ltd*, the Court confronted squarely the question of what distinguishes unprotectable ideas, procedures, and methods from protectable expression. The case concerned whether copyright protected the functionality of statistical analysis software.

The Court held categorically that "neither the functionality of a computer program nor the programming language and the format of data files used in a computer program in order to exploit certain of its functions constitute a form of expression" and thus cannot receive copyright protection.[^44] The reasoning is critical: "to accept that the functionality of a computer program can be protected by copyright would amount to making it possible to monopolise ideas, to the detriment of technological progress and industrial development."[^45]

Copyright's purpose is to protect creative expression while leaving ideas, concepts, and functional methods free for others to use and build upon. Protecting functionality would transform copyright into a patent-like monopoly without the stringent requirements of novelty, non-obviousness, and limited duration that justify patent protection.

The Court emphasized that copyright's comparative advantage is that "such protection covers only the individual expression of the work and thus leaves other authors the desired latitude to create similar or even identical programs provided that they refrain from copying."[^46]

[^44]: Case C-406/10 SAS Institute v World Programming EU:C:2012:259, para 39.

[^45]: ibid para 40.

[^46]: ibid para 45.

This principle extends beyond software to all categories of works. In *Levola Hengelo*, though concerning the copyrightability of taste, the Court articulated the broader framework: copyright requires not only originality but also that "only something which is the expression of the author's own intellectual creation may be classified as a 'work'" under the InfoSoc Directive.[^47] The Court noted that "in accordance with the Agreement on Trade-Related Aspects of Intellectual Property Rights...and with the WIPO Copyright Treaty...copyright protection may be granted to expressions, but not to ideas, procedures, methods of operation or mathematical concepts as such."[^48]

This is not merely a doctrinal technicality but reflects copyright's fundamental design. Ideas must remain "the common property of the whole world," while monopoly rights attach only to particular expressions of those ideas.[^49]

To that extent, determining whether prompts are protected requires asking whether they constitute expressions or instead embody ideas, procedures, or methods of operation that copyright law categorically excludes from protection.

[^47]: *Levola Hengelo* (n 31) para 36.

[^48]: ibid para 37.

[^49]: See generally P.B. Hugenholtz, 'Codifying the *Infopaq* Case Law - or Not?' in C. Angelopoulos (ed), *The Modernisation of European Copyright Law* (Kluwer 2017) 12–14 (discussing idea-expression dichotomy as fundamental copyright principle).

Prompts are most naturally characterized as instructions—they tell the AI system what to do, specifying procedures for generating output and methods of operation for responding to user queries. This characterization finds support in the analogies already examined: recipes as unprotectable succession of instructions, operating manuals as unprotectable procedures, game rules as unprotectable methods.

An additional parallel strengthens the case. If formal programming languages—Python syntax, Java conventions, SQL query structures—are unprotectable ideas and principles under the Software Directive, then natural language prompts that provide informal methods for instructing AI systems should be equally unprotectable for the same reasons.[^50] Both constitute methods of interaction with computational systems. Both specify functionality and desired operations. Both are means to an end rather than creative expressions in their own right.

The *SAS Institute* Court emphasized that programming languages constitute unprotectable ideas and principles underlying program interfaces.[^51] The same logic applies to natural language prompts. The prompt "summarize this text" is functionally equivalent to a programming language command `summarize(text)`—both are instructions specifying what computational operation should be performed. The natural language formulation does not transform the functional instruction into protectable expression any more than translating a Java command into English would make the command copyrightable.

[^50]: Software Directive (n 12) art 1(2); *BSA* (n 17) para 49 (holding that "ideas and principles which underlie any element of [a] program, including those which underlie its interfaces, are not protected").

[^51]: *SAS Institute* (n 44) para 46.

### Scholarly consensus

Academic commentary on prompt copyrightability has emerged rapidly with substantial consensus that prompts likely fail the originality threshold under EU law.

Professor He, writing in *GRUR International*, argues that "judicial recognition of text-to-image copyrightability at the current stage is dangerous" because "the practice is not in accordance with our traditional understanding of originality and the author-work relationship."[^52] He emphasizes that prompts constitute "merely unprotectable ideas" rather than expressions, noting that the U.S. Copyright Office has concluded that "prompts alone do not provide sufficient human control to make users of an AI system the authors of the output."[^53]

Professors Gervais and Hugenholtz address the question directly on the Kluwer Copyright Blog, identifying the critical problem: "The hard question is whether those creative choices—the originality, if any—of the prompt is 'transferable' into the product or output of the AI machine. This gets dangerously close to owning the underlying idea, and thus goes against a fundamental principle of international copyright law."[^54] They conclude that "if the originality of the instructions is not sufficiently reflected in the machine's product, there is no protected work in the output. That should be the default position."[^55]

Professor Quintais and Professor Hugenholtz, in their comprehensive analysis published in the *International Review of Intellectual Property and Competition Law*, argue that current EU copyright rules are "generally suitable and sufficiently flexible to deal with the challenges posed by AI-assisted output" when properly applied.[^56] They emphasize that where subject matter has been dictated by technical considerations leaving no room for creative freedom, originality cannot be found—a principle directly applicable to the functional nature of prompts.[^57]

To that extent, scholarly consensus aligns with doctrinal analysis: prompts fail the originality test.

[^52]: X. He, 'Human Authorship and AI-Generated Works: A Chinese Perspective' (2024) 55 IIC 321, 335.

[^53]: ibid 336 (citing U.S. Copyright Office, Copyright Registration Guidance: Works Containing Material Generated by Artificial Intelligence, 88 Fed Reg 16190 (16 March 2023)).

[^54]: D. Gervais and P.B. Hugenholtz, 'The AI-nundrum: Machines, Learning and Intellectual Property' (Kluwer Copyright Blog, 18 July 2023) <http://copyrightblog.kluweriplaw.com/2023/07/18/the-ai-nundrum-machines-learning-and-intellectual-property> accessed 15 October 2024.

[^55]: ibid.

[^56]: J.P. Quintais and P.B. Hugenholtz, 'The New Copyright Directive: A Complete (EU) Copyright Codification?' (2020) 51 IIC 28, 45.

[^57]: ibid 46–47.

### Exceptional cases

Two narrow exceptions merit consideration.

**First, exceptionally detailed and creative prompts that function as independent literary works might receive protection as such.** Consider a multi-thousand-word prompt that includes elaborate narrative descriptions, original metaphors, poetic language, and sophisticated rhetorical structures that go beyond mere instruction to constitute literary expression in their own right.

Such a prompt might be protectable as a literary work separate from any AI output it generates. However, this protection would extend only to the text of the prompt itself as a literary composition, not to any control over AI outputs generated from it or over similar functional prompts.

The distinction matters. Others could not copy the elaborate textual expression. But they could create functionally equivalent prompts that achieve similar AI outputs without infringing.

The strongest affirmative argument for prompt copyrightability relies on *Infopaq*'s holding that even 11-word excerpts "may be suitable for conveying to the reader the originality of a publication such as a newspaper article, by communicating to that reader an element which is, in itself, the expression of the intellectual creation of the author."[^58] If 11 words can be protected, surely 400 words of carefully crafted specifications can be.

However, this argument founders on a critical distinction. *Infopaq* concerned literary expression in newspaper articles where the journalist exercised creative freedom in word choice, phrasing, and presentation of ideas. The Court emphasized that "through the choice, sequence and combination of those words the author may express his creativity in an original manner and achieve a result which is an intellectual creation."[^59]

Prompts, by contrast, function as instructions rather than as literary communication. Their purpose is to specify procedures for the AI to execute, not to express the author's creative vision through language selected for its aesthetic or communicative qualities.

To that extent, prompts fall on the functional side of the line the Court has drawn between creative expression and utilitarian specification.

[^58]: *Infopaq* (n 13) para 47.

[^59]: ibid para 45.

**Second, prompts embedded in software as part of larger programs might receive protection as components of the software work.** Where a software application incorporates specific prompts as integral elements of its code—system prompts hardcoded into an AI application that define its behavior—those prompts might be protected as part of the overall software work under the Software Directive.[^60]

However, again, the protection attaches to the software work as a whole, not to the prompts as independent protectable subject matter.

[^60]: Software Directive (n 12) art 1(1).

These exceptions do not disturb the general conclusion.

Prompts *qua* prompts—textual instructions provided to AI systems to generate desired outputs—do not meet the EU originality standard for copyright protection.

# IV. Software protection: why prompts are neither programs nor preparatory design material

Having established that prompts fail the originality standard as literary works under the InfoSoc Directive, a second interpretive pathway presents itself: protection as computer programs or preparatory design material under the Software Directive.

This theory posits that prompts, particularly system prompts that configure AI behavior, function as specifications or instructions to computational systems and might therefore qualify under the Software Directive's framework. The argument proceeds on functional similarity: prompts directly influence AI computational processes, adjust probability distributions and attention mechanisms, and control program behavior—relationships that resemble the connection between preparatory design materials and final program code.

Two distinct claims require examination. First, whether prompts themselves constitute "computer programs" within the meaning of Article 1(1) of Directive 2009/24/EC. Second, whether prompts qualify as "preparatory design material" protected under the same provision.

Both claims fail.

## The Software Directive's scope and the CJEU's restrictive interpretation

The Software Directive provides comprehensive protection for computer programs. Article 1(1) states: "Member States shall protect computer programs, by copyright, as literary works within the meaning of the Berne Convention for the Protection of Literary and Artistic Works. For the purposes of this Directive, the term 'computer programs' shall include their preparatory design material."[^1]

Recital 7 elaborates the scope: "the term 'computer program' shall include programs in any form, including those which are incorporated into hardware. This term also includes preparatory design work leading to the development of a computer program provided that the nature of the preparatory work is such that a computer program can result from it at a later stage."[^2]

The Court of Justice has interpreted this scope through several key decisions that prove dispositive for prompt protection claims.

[^1]: Directive 2009/24/EC of the European Parliament and of the Council of 23 April 2009 on the legal protection of computer programs [2009] OJ L111/16, art 1(1).

[^2]: ibid recital 7.

In *Bezpečnostní softwarová asociace (BSA) v Ministerstvo kultury*, the Court addressed whether graphical user interfaces qualify as protectable computer programs. The Court held at paragraph 45 that GUIs "do not enable the reproduction of the computer program, but merely constitute one element of that program by way of which users make use of its features."[^3] Only the actual source code or object code constituting the program's expression receives protection. User-facing elements through which individuals interact with programs fall outside the Software Directive's scope.

The Court emphasized at paragraph 46 that protection extends solely to "the expression in any form of a computer program, which must be understood as referring to the expression, in any form, of the programmer's own intellectual creation."[^4] The GUI, while part of the user experience, does not constitute the program's expression—the code does.

[^3]: Case C-393/09 BSA v Ministerstvo kultury EU:C:2010:816, para 45.

[^4]: ibid para 46.

The Court further narrowed software protection scope in *SAS Institute Inc v World Programming Ltd*. At paragraph 39, the Court held that "the functionality of a computer program, the programming language and the format of data files used in a computer program do not constitute a form of expression of that program and, as such, are not protected by copyright in computer programs."[^5]

This holding is critical. Programming languages—the formal methods by which developers instruct computers—are explicitly excluded from protection as ideas and principles underlying programs rather than as expressions. The Court emphasized at paragraph 40 that "to the extent that logic, algorithms and programming languages comprise ideas and principles, those ideas and principles are not protected under this Directive."[^6]

The rationale, articulated at paragraph 40, mirrors the copyright chapter's analysis: "to accept that the functionality of a computer program can be protected by copyright would amount to making it possible to monopolise ideas, to the detriment of technological progress and industrial development."[^7]

[^5]: Case C-406/10 SAS Institute v World Programming EU:C:2012:259, para 39.

[^6]: ibid para 40.

[^7]: ibid.

More recently, in *Sony Computer Entertainment Europe Ltd v Datel Design & Development Ltd*, the Court clarified that even the content of variables stored in RAM during program execution does not constitute an expression of the computer program subject to copyright protection.[^8] Modification of data values during program execution does not amount to copyright infringement of the software code. The distinction between the program itself and the data it processes remains absolute.

[^8]: Case C-159/23 Sony Computer Entertainment Europe v Datel Design & Development EU:C:2024:649, paras 33–35.

Critically, Article 1(2) of the Software Directive establishes an express exclusion: "Ideas and principles which underlie any element of a computer program, including those which underlie its interfaces, are not protected by copyright under this Directive."[^9] Recital 11 reinforces this: "only the expression of a computer program is protected and...ideas and principles which underlie any element of a program, including those which underlie its interfaces, are not protected by copyright."[^10]

To that extent, the Court has constructed a narrow protective scope focused exclusively on program code—source or object code constituting the programmer's expression—while excluding functionality, interfaces, programming languages, and data from protection.

[^9]: Software Directive (n 1) art 1(2).

[^10]: ibid recital 11.

## Why prompts are not computer programs

Applying this case law to prompts reveals that prompts do not qualify as "computer programs" under the Software Directive.

Three barriers prove insurmountable.

**First, prompts are textual instructions provided as input to existing AI programs—they are not themselves source code or object code.** They do not define the computational processes executed by the system. The AI model's trained weights, neural network architecture, and inference algorithms perform the actual computation. Prompts direct how those existing computational processes should be applied to particular tasks, but they do not constitute the code implementing those processes.

Under the *BSA* principle that GUIs are not protected because they "merely constitute one element of that program by way of which users make use of its features," prompts likewise merely enable users to direct how existing AI programs should operate.[^11] Just as GUIs provide the mechanism for user interaction with software without constituting the software itself, prompts provide the mechanism for user interaction with AI systems without constituting the AI programs.

Put differently, prompts are instructions *to* programs, not programs themselves.

[^11]: *BSA* (n 3) para 45.

**Second, prompts function as interfaces—explicitly excluded from protection under Article 1(2).** An interface is the boundary across which users communicate with computational systems. Graphical user interfaces use visual elements; command-line interfaces use textual commands; application programming interfaces use function calls. Natural language prompts constitute yet another interface type—the mechanism by which users communicate instructions to AI systems in natural language rather than formal syntax.

The Software Directive's Article 1(2) excludes "ideas and principles which underlie any element of a computer program, including those which underlie its interfaces" from protection.[^12] If visual GUIs through which users interact with software are not protected as program expressions, textual prompts through which users interact with AI systems fall under the same exclusion. Both are methods of interaction rather than program code.

The *BSA* Court's reasoning applies directly: prompts "do not enable the reproduction of the computer program, but merely constitute one element...by way of which users make use of its features."[^13] Protecting prompts as computer programs would extend Software Directive protection beyond program expressions to user interaction methods—a result the Court has explicitly rejected.

[^12]: Software Directive (n 1) art 1(2).

[^13]: *BSA* (n 3) para 45.

**Third, under the *SAS Institute* precedent, prompts describe functionality rather than constituting program expression.** Prompts specify what outputs users want—"generate an image in impressionist style" or "write a formal business letter"—not how the AI system should implement those operations at the code level. They are analogous to specifying what function a program should perform, which the Court has held does not receive software protection.[^14]

The programming language analogy proves dispositive. If formal programming languages—Python syntax, SQL query structures, JavaScript conventions—are unprotectable ideas and principles under Article 1(2) and *SAS Institute*, then natural language prompts are equally unprotectable. Both are methods for instructing computational systems. Both specify desired operations. The Court held in *SAS* that programming languages constitute unprotectable ideas and principles underlying program interfaces.[^15]

A Python command `print("Hello, world")` and a prompt "Write 'Hello, world'" are functionally equivalent—both instruct a computational system to produce output. The natural language formulation does not transform the instruction into protectable program expression any more than translating a programming command into English would make the command copyrightable. If the formal instruction languages that developers use to write programs are unprotectable, the informal natural language instructions that users employ to direct pre-existing programs cannot receive greater protection.

To that extent, protecting prompts as computer programs would contradict the Court's holdings that programming languages—the actual methods by which programs are created—fall outside copyright protection as ideas and principles rather than expressions.

[^14]: *SAS Institute* (n 5) para 39.

[^15]: ibid para 40.

One might object that sophisticated prompts demonstrate technical expertise analogous to software specifications—prompt engineers learn optimal phrasing through experimentation, understanding of model architecture, and iterative refinement. However, this conflates functional skill with protectable expression. Software receives protection not because writing it requires expertise but because the code itself constitutes the programmer's expression of creative choices in implementing functionality. Prompts, even sophisticated ones, direct *use* of existing programs rather than constituting expressions that implement computational processes.

The skill in crafting effective prompts resembles skill in formulating database queries or writing effective search terms—valuable expertise that produces economic value, but not protectable expression under the Software Directive. The Court's *Football Dataco* principle, examined in the copyright chapter, applies equally here: "the fact that the setting up of the database required...significant labour and skill of its author...cannot as such justify the protection of it by copyright" where that labor does not express originality.[^16]

[^16]: Case C-604/10 Football Dataco v Yahoo! UK EU:C:2012:115, para 42.

## Why prompts are not preparatory design material

The preparatory design material category provides a potential alternative argument but ultimately fails for distinct reasons.

Recital 7 protects "preparatory design work leading to the development of a computer program provided that the nature of the preparatory work is such that a computer program can result from it at a later stage."[^17] Academic commentary interprets this as requiring preparatory work to be sufficiently detailed and technical that program implementation follows with minimal additional creative choices.[^18] Flow charts defining control structures, pseudocode specifying algorithms, and architecture documents constraining implementation choices may qualify because they function as blueprints from which programmers write source code implementing the design.

Prompts fail this standard because they do not lead to computer programs resulting from them.

[^17]: Software Directive (n 1) recital 7.

[^18]: See generally T. Dreier and P.B. Hugenholtz, *Concise European Copyright Law* (2nd edn, Kluwer 2016) 318–319 (discussing preparatory design material as requiring technical specificity approaching program implementation).

A prompt given to an AI system does not generate program code—it generates outputs like text or images. The AI model itself, which already exists as a complete program, processes the prompt. The prompt does not constitute design work for creating that program. Even if one argues that prompts could inform future AI model development, they lack the technical specificity and formality expected of preparatory design material.

Traditional preparatory design work—flow charts, technical specifications, architecture diagrams—defines how computational processes should be structured such that programmers can implement them deterministically. Two programmers working from the same detailed specification should produce functionally equivalent code. Prompts operate differently. The same prompt provided to the same AI model produces varying outputs across invocations. As Sampaio notes in his analysis on the Kluwer Copyright Blog, "the same prompt to the same model will not deliver the same results."[^19]

This lack of determinism fundamentally distinguishes prompts from preparatory design work. Specifications must be sufficiently precise to enable consistent program implementation. Prompts are high-level natural language instructions that guide probabilistic systems toward desired output characteristics without determining those outputs uniquely.

Moreover, preparatory design material receives protection because it represents the intellectual creation of the programmer in designing how the program will operate—the creative choices in structuring algorithms, organizing data, and architecting systems. These choices, when documented in specifications, constitute expressions of the designer's intellectual creation that lead directly to program implementation.

Prompts specify what users want AI systems to produce, not how those systems should be designed or implemented. They are consumer-facing instructions about desired outputs rather than developer-facing specifications about program structure. To that extent, prompts fall outside the category of preparatory design material even if they influence how AI systems are used.

[^19]: A. Sampaio, 'Are Prompts Copyrightable?' (Kluwer Copyright Blog, 14 June 2023) <http://copyrightblog.kluweriplaw.com/2023/06/14/are-prompts-copyrightable> accessed 15 October 2024.


By elimination, prompts do not qualify for protection as computer programs or preparatory design material under the Software Directive.

They are instructions *to* programs, not programs themselves. They function as interfaces explicitly excluded from protection under Article 1(2). They describe desired functionality rather than implementing it through code. They are analogous to programming languages—which the Court has held constitute unprotectable ideas and principles—except formulated in natural language rather than formal syntax. And they lack the technical specificity, deterministic relationship to program code, and design-focused function required for preparatory design material.

The Software Directive provides no basis for prompt protection.

# V. Patent protection: why prompts lack technical character

Having rejected copyright protection under the InfoSoc Directive and software protection under the Software Directive, a third interpretive pathway presents itself: patent protection under the European Patent Convention.

This theory posits that sophisticated prompts—particularly those optimizing AI system performance, reducing computational costs, or enabling novel applications—might constitute patentable inventions as computer-implemented methods or as components of technical systems. The argument proceeds on functional contribution: prompts that demonstrably improve processing efficiency, reduce token consumption, or enable technical applications might provide the "further technical effect" that European Patent Office jurisprudence requires for patenting computer-related inventions.

The analysis must focus on the European Patent Convention rather than EU directives, as patent law remains governed by the EPC—an international treaty to which all EU Member States are parties—rather than harmonized EU legislation. The question becomes whether prompts satisfy the technical character requirement articulated in EPO case law and the Guidelines for Examination.

The answer is negative. Prompts constitute excluded subject matter under Article 52(2) EPC, lack the technical character required for patentability, and fail the inventive step assessment under the COMVIK approach because their innovative features are linguistic and cognitive rather than technical.

## The EPC framework and exclusions from patentability

Article 52(1) EPC establishes the fundamental requirement: "European patents shall be granted for any inventions, in all fields of technology, provided that they are new, involve an inventive step and are susceptible of industrial application."[^1]

Article 52(2), however, excludes specific categories from patentability. It provides that "the following in particular shall not be regarded as inventions" and lists discoveries, scientific theories and mathematical methods; aesthetic creations; schemes, rules and methods for performing mental acts, playing games or doing business, and programs for computers; and presentations of information.[^2]

Critically, Article 52(3) adds: "Paragraph 2 shall exclude the patentability of the subject-matter or activities referred to therein only to the extent to which a European patent application or European patent relates to such subject-matter or activities as such."[^3] This "as such" qualification has driven EPO practice toward allowing patents for computer-implemented inventions that provide technical effects beyond the excluded subject matter itself.

Prompts face immediate obstacles under Article 52(2). They potentially fall within multiple exclusions simultaneously. They constitute methods for performing mental acts—linguistic formulation of instructions involves cognitive activity in structuring communication. They direct computer operations, implicating the exclusion for programs for computers. They structure how information is requested, falling within presentations of information. They arguably embody mathematical methods when they define algorithmic processes through natural language specifications.

To that extent, prompts must overcome a presumption of exclusion by demonstrating technical character that transcends their linguistic and cognitive nature.

[^1]: Convention on the Grant of European Patents (European Patent Convention) (adopted 5 October 1973, entered into force 7 October 1977, as revised 29 November 2000) art 52(1).

[^2]: ibid art 52(2).

[^3]: ibid art 52(3).

## EPO jurisprudence on technical character and further technical effect

The EPO has developed a two-stage framework for assessing computer-implemented inventions. At the first stage, inventions must have "technical character" to qualify as inventions under Article 52(1). At the second stage, they must provide inventive step based on technical contributions to the art under Article 56.

The landmark Board of Appeal decision *Computer Program Product/IBM* established the "further technical effect" test. The Board held that "a computer program product is not excluded from patentability under Article 52(2) and (3) EPC if, when it is run on a computer, it produces a further technical effect which goes beyond the 'normal' physical interactions between program (software) and computer (hardware)."[^4] Mere electrical currents and switching within computer hardware do not suffice. The further technical effect must reside in effects deriving from execution of the instructions—controlling an anti-lock braking system, managing processor load balancing, improving memory allocation, determining X-ray emission parameters, compressing video data, restoring digital images, or encrypting electronic communications.[^5]

The Enlarged Board of Appeal in *Programs for Computers* clarified that technical character requires providing "technical teaching"—instruction on how to solve a technical problem using technical means.[^6] The term "technical" remains deliberately undefined but is understood through case law application. Programming *per se* may involve technical considerations, but patentability requires "further technical considerations" beyond merely finding an algorithm to implement desired functionality.[^7]

[^4]: *Computer Program Product/IBM* T 1173/97 [2000] OJ EPO 609, Reasons 13.

[^5]: ibid.

[^6]: *Programs for Computers* G 3/08 [2011] OJ EPO 10, Reasons 10.13.

[^7]: ibid Reasons 10.13.1.

The *Two Identities/COMVIK* decision established the framework for assessing inventive step in mixed technical/non-technical inventions.[^8] Non-technical features making no contribution to technical character cannot support inventive step. These features are treated as "constraints" or "requirements" in formulating the objective technical problem. Even if non-technical features are novel and inventive in their own domain—a clever business method, for example—they contribute nothing to patent inventive step under Article 56 EPC.

Put differently, the inventive step assessment considers only technical contributions. Non-technical novelty, no matter how significant in its own field, is irrelevant to patentability.

The Enlarged Board confirmed in *Computer-Implemented Simulations* that the COMVIK approach applies to all computer-implemented inventions.[^9] Importantly, the Board held that "a computer-implemented simulation of a technical system or process that is claimed as such can, for the purpose of assessing inventive step, solve a technical problem by producing a technical effect going beyond the simulation's implementation on a computer."[^10] However, "it is not a sufficient condition that the simulation is based, in whole or in part, on technical principles underlying the simulated system or process."[^11]

[^8]: *Two Identities/COMVIK* T 641/00 [2003] OJ EPO 352.

[^9]: *Computer-Implemented Simulations* G 1/19 [2021] OJ EPO A77, Reasons 85.

[^10]: ibid Reasons 83.

[^11]: ibid Reasons 85.

The EPO updated its Guidelines for Examination in 2024 to address artificial intelligence specifically, treating AI and machine learning as forms of mathematical methods excluded under Article 52(2)(a).[^12] The Guidelines establish two categories where AI inventions may achieve patentability despite this exclusion.

First, AI may serve a specific technical purpose. Examples include processing audio, image, or video data for technical applications; speech recognition systems; and control systems in technical fields. A claimed example involves a neural network controlling fan blade flutter in gas turbine engines.[^13] The technical purpose grounds the invention in a technical field rather than abstract mathematics. The AI's function is technical—controlling physical phenomena—not merely cognitive or linguistic.

Second, AI may have a specific technical implementation affecting computing hardware or internal computer functioning. This includes new arrangements of computing hardware or effects on CPU-GPU interaction for machine learning with specific data structures.[^14] The implementation must go beyond generic computer use to affect the computing machinery itself in ways that solve technical problems related to the computer's operation.

The 2024 Guidelines also tightened sufficiency of disclosure requirements for AI inventions. Applications must disclose mathematical methods and characteristics of training data affecting technical effects in sufficient detail.[^15] Technical effects must be plausible across the entire claimed scope, demonstrated through explanations, mathematical proof, or experimental data. In *Blood Pressure Estimation*, the Board held that an application mentioning that training data must cover patients of different ages, sexes, and health conditions but providing no further details was insufficient—the skilled person could not train the network to achieve the claimed technical effect based on the disclosure.[^16]

To that extent, AI-related inventions face heightened scrutiny regarding both technical character and disclosure adequacy.

[^12]: European Patent Office, *Guidelines for Examination in the European Patent Office* (2024) G-II 3.3.1.

[^13]: ibid.

[^14]: ibid.

[^15]: ibid F-III 3.4.

[^16]: *Blood Pressure Estimation* T 0161/18 (21 July 2020) Reasons 2.6.

## Application to prompts

Prompts fail the technical character requirement under current EPO practice for reasons that parallel, but are distinct from, the copyright and software protection failures examined in Parts III and IV.

The first obstacle is categorical. Prompts constitute excluded subject matter under multiple provisions of Article 52(2). They are linguistic constructs—text strings communicating intent rather than technical implementations. As methods for performing mental acts, they fall squarely within the exclusion: linguistic formulation is inherently cognitive activity involving choices about how to structure communication to achieve desired understanding. As presentations of information, they structure how information is requested from AI systems—the format, sequence, and framing of requests. As methods closely related to computer programs, they direct AI operation through natural language specifications rather than formal code.

The "as such" qualification in Article 52(3) does not rescue prompts because they remain purely linguistic and cognitive even when used with AI systems. Adding "implement on a computer" does not transform excluded subject matter into patentable inventions—this principle, established in EPO jurisprudence on business methods, applies equally to prompts.[^17]

[^17]: See *Pension Benefit Systems Partnership* T 931/95 [2001] OJ EPO 441 (holding that business methods remain unpatentable even when implemented on computers unless technical character derives from technical considerations beyond generic computer use).

The second obstacle is the absence of technical character. The EPO requires "technical teaching" on how to solve a technical problem using technical means.[^18] Prompts do not provide such teaching. They specify what outputs are desired—content characteristics, format preferences, stylistic constraints—not how to achieve them technically. The prompt does not control hardware, does not improve computer functioning beyond generic use, and does not process technical data in a technical manner yielding technical results.

The AI model processes the prompt using its existing trained weights and inference algorithms, but the model exists independently of any particular prompt. The prompt is input data directing how the model's capabilities should be applied, not a technical implementation defining those capabilities. This relationship resembles that between database queries and database systems—the query specifies what data should be retrieved, but provides no technical teaching about how the database operates.

The third obstacle concerns the nature of problems that prompts address. Typical prompt objectives include improving AI output quality, relevance, format, or stylistic appropriateness. These are content quality issues, not technical problems in the EPO sense. A technical problem must relate to a technical field and be solved by technical means producing technical effects.[^19] Prompt problems typically concern how to elicit better writing, structure information more effectively, reduce linguistic ambiguity, or improve comprehension—linguistic and cognitive problems, not technical problems amenable to technical solutions.

One might argue that prompts reducing token consumption or processing time solve technical problems—computational efficiency. However, such reductions typically result from linguistic optimization that makes instructions clearer or more concise, not from technical innovations in how AI systems process inputs. The efficiency gains derive from better communication, which remains a cognitive and linguistic contribution rather than a technical one. The EPO has consistently held that improvements resulting from non-technical innovations do not confer patentability even when those improvements have technical consequences.[^20]

[^18]: *Programs for Computers* (n 6) Reasons 10.13.

[^19]: *COMVIK* (n 8) Reasons 5–6.

[^20]: ibid Reasons 6 (non-technical features treated as given constraints in formulating objective technical problem).

The fourth obstacle emerges from the COMVIK approach to inventive step assessment. Even if one claims a "computer-implemented method using prompts," the novelty and inventiveness reside in the prompt formulation—linguistic and cognitive choices about how to structure instructions—not in technical implementation. Under COMVIK, these non-technical features contribute nothing to inventive step.[^21] They are treated as constraints or requirements given to the skilled person.

The technical problem then becomes "implement a system that processes this specified linguistic input on a computer," which would be obvious to a person skilled in the art. The skilled person, defined as a computer scientist or AI engineer rather than a linguist or communication specialist, would find the technical implementation straightforward. Any competent engineer could implement software that accepts and processes the specified prompt structure. The inventive contribution—the prompt formulation itself—is non-technical and therefore irrelevant to inventive step under Article 56 EPC.

Put differently, even if prompts cleared the technical character hurdle at the Article 52 stage, they would fail inventive step assessment because their innovative aspects lie outside the technical domain.

[^21]: ibid.

The fifth obstacle concerns determinism and reproducibility. The same prompt provided to the same AI model generates different outputs at different invocations due to the probabilistic nature of neural network inference and sampling procedures. This non-determinism contrasts sharply with patentable software inventions where specific code produces predictable technical effects under defined conditions. Patents typically claim predictable, reproducible technical results that can be verified and enforced. Prompts do not provide such determinism—they influence output probability distributions without determining outcomes uniquely.

This variability creates both practical and doctrinal problems. Practically, it becomes difficult to define the invention's scope with the precision patent law requires. Doctrinally, the lack of predictable technical results undermines the claim to providing technical teaching—if the same input produces varying outputs, the teaching does not reliably instruct how to solve the technical problem.

---

One might attempt several strategies to overcome these obstacles, but each fails upon analysis.

First, one might claim "a method of controlling a technical system using an AI system configured with prompt X." However, the prompt itself remains non-technical—merely adding technical context does not render the prompt patentable, just as the EPO has held that adding "use a computer" does not make business methods patentable.[^22] The technical system (gas turbine, medical device, industrial robot) may be technical, and the AI system processing sensor data may be technical, but if the novel contribution resides in the prompt's linguistic formulation, that contribution remains non-technical regardless of the technical context in which it is deployed.

Second, one might claim "a prompt structured to reduce processing tokens or memory consumption." However, this remains linguistic content optimization where computational reduction is incidental rather than the result of technical implementation innovation. The reduction occurs because clearer instructions require fewer tokens to convey equivalent information—a linguistic efficiency, not a technical innovation in how computers process information. The technical effect (reduced computation) derives from non-technical means (better communication), which the COMVIK approach excludes from inventive step consideration.

Third, and most promisingly, one might claim "an AI system with architecture co-designed to process prompts having structure X, wherein the architecture optimizes processing of said structure." This strategy shifts the invention from the prompt to the technical architecture. However, if the claim is drafted this way, the prompt is not the patentable subject matter—the system architecture is. The prompt becomes a feature of the claimed system rather than the invention itself. Moreover, such claims face scrutiny regarding whether the architectural choices are dictated by the prompt structure (in which case the prompt's non-technical character taints the architecture) or whether genuine technical innovation exists in the architecture independent of the prompt.

To that extent, no plausible claiming strategy renders prompts patentable under current EPO practice.

[^22]: *Pension Benefit Systems* (n 17) Reasons 5–6.

---

By elimination, AI prompts do not meet the requirements for patent protection under the European Patent Convention.

They constitute excluded subject matter under Article 52(2) as methods for performing mental acts, presentations of information, and subject matter closely related to computer programs as such. They lack technical character because they provide no technical teaching about solving technical problems using technical means—they specify desired outputs through linguistic formulation, not technical implementations. The problems they address are cognitive and communicative rather than technical. Under the COMVIK approach, their innovative features are non-technical and therefore contribute nothing to inventive step. And their non-deterministic nature undermines the predictability and reproducibility that patent protection presupposes.

Patent protection does not offer a viable path for protecting prompt innovations under current EPO jurisprudence.

# VI. Are AI prompts trade secrets under EU law?

This chapter establishes whether AI prompts – the instructions and queries users provide to large language models – qualify as trade secrets under Directive (EU) 2016/943 on the protection of undisclosed know-how and business information. The answer determines whether European businesses can legally prevent competitors from misappropriating valuable prompt engineering work, or whether the fundamental architecture of cloud-based AI services renders such protection untenable. The directive requires information to meet three cumulative elements: secrecy in the sense that it is not generally known or readily accessible; commercial value because it is secret; and reasonable steps under the circumstances to keep it secret. Applied to AI prompts, the first element confronts the problem that cloud-based AI architectures require transmitting prompts to third-party providers, potentially destroying secrecy through disclosure. The second element faces the challenge that prompts may derive value primarily from the underlying AI model rather than possessing independent commercial worth. The third element demands assessing what protective measures are feasible when prompts must be shared with commercial AI providers to function at all – a requirement that may be fundamentally incompatible with trade secret law's confidentiality expectations.

## The three-part test: secrecy, commercial value, and reasonable steps

Directive (EU) 2016/943, adopted on 8 June 2016 with a transposition deadline of 9 June 2018, harmonizes trade secrets protection across EU Member States by establishing minimum standards for civil remedies against unlawful acquisition, use, and disclosure. The directive's legal basis is Article 114 TFEU, which permits harmonization measures for the establishment and functioning of the internal market; this choice of legal basis – rather than Article 118 TFEU, which provides for creating unitary EU intellectual property rights – means the directive harmonizes divergent national laws rather than creating a supranational trade secret right. Article 17(2) of the Charter of Fundamental Rights of the European Union provides that "intellectual property shall be protected," establishing trade secrets protection as a fundamental right matter within the EU legal order. The directive implements the EU's obligations under Article 39 of the TRIPS Agreement, which requires WTO members to protect undisclosed information that is secret, has commercial value because it is secret, and has been subject to reasonable steps to keep it secret.

Article 2(1) of Directive 2016/943 defines "trade secret" as "information which meets all of the following requirements: (a) it is secret in the sense that it is not, as a body or in the precise configuration and assembly of its components, generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question; (b) it has commercial value because it is secret; (c) it has been subject to reasonable steps under the circumstances, by the person lawfully in control of the information, to keep it secret." This three-part definition remained essentially unchanged from the Commission's November 2013 proposal through final adoption in June 2016, demonstrating consensus that the TRIPS Article 39 formulation provides an appropriate international standard. The European Parliament attempted during the ordinary legislative procedure to add requirements that commercial value be "actual or potential significant" and that reasonable steps be "demonstrable" and "verifiable by the relevant competent judicial authorities," but the trilogue negotiations rejected these amendments, preserving the Commission's original formulation.

The directive's structure establishes that all three requirements are cumulative – failure to satisfy any single element defeats trade secret status entirely. Recital 14 explains that "it is important to establish a homogenous definition of a trade secret without restricting the subject matter to be protected" and that the definition "should cover know-how, business information and technological information where there is both a legitimate interest in keeping them confidential and a legitimate expectation that such confidentiality will be preserved." The directive explicitly excludes certain information from protection: Article 1(3) provides that "nothing in this Directive shall be understood to offer any ground for restricting the mobility of employees" and specifically excludes "employees' use of information that does not constitute a trade secret," "employees' use of experience and skills honestly acquired in the normal course of their employment," and additional contractual restrictions beyond those imposed in accordance with Union or national law. Article 3 further establishes that acquisition of a trade secret is lawful when obtained by independent discovery or creation, observation or study of publicly available products, reverse engineering through disassembly or testing of lawfully possessed products, or any other practice conforming to honest commercial practices. As we will see, these exclusions and lawful acquisition provisions become particularly significant for AI prompts, where reverse engineering from outputs and independent discovery through experimentation are both technically feasible and increasingly common.

## Secrecy defeated by disclosure to cloud AI providers

The first element – secrecy in the sense that information is "not, as a body or in the precise configuration and assembly of its components, generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question" – establishes an objective standard based on accessibility within relevant professional circles rather than requiring absolute secrecy. The Commission's Impact Assessment explained that this formulation allows situations where individual components may be publicly known but their specific combination or configuration remains secret; to that extent, a prompt constructed from publicly available techniques might still qualify if the precise assembly creates something not generally known. However, the secrecy requirement fundamentally requires that the information not be "readily accessible" to specialists in the field – and this is where AI prompts confront their most serious obstacle.

Cloud-based AI services – which represent the dominant deployment model for large language models as of October 2025 – require users to transmit prompts to third-party providers with each API call or chat interface interaction. OpenAI's GPT-4, Anthropic's Claude, Google's Gemini, and similar commercial offerings process prompts on the provider's infrastructure; the prompts necessarily travel across networks and reside, at least temporarily, on systems controlled by the AI provider rather than the user. Academic scholarship examining information flows in cloud computing contexts demonstrates that third-party disclosure potentially destroys trade secret status absent express or implied confidentiality agreements establishing duties not to use or disclose the information. Sharon K. Sandeen's analysis of cloud computing and trade secrets emphasizes that without contractual protections, information "known outside" the company by a service provider may lack the secrecy required for trade secret protection, and the information becomes "readily ascertainable" by the provider who possesses it.

The question thus becomes whether contractual confidentiality provisions in AI service agreements sufficiently preserve secrecy despite physical disclosure of prompts to the provider. Enterprise AI service agreements from major providers – such as Microsoft Azure OpenAI Service, Anthropic's enterprise plans, and Google Cloud's Vertex AI – typically include provisions stating that customer prompts and data will not be used to train models or disclosed to third parties. However, consumer-tier services – including the free ChatGPT interface and similar offerings – generally include terms of service permitting the provider to use inputs for model training and service improvement, representing a contractually authorized use that likely defeats trade secret status. German courts applying the Geschäftsgeheimnisgesetz (the German implementation of Directive 2016/943) have emphasized that disclosure to third parties without executed confidential disclosure agreements can result in loss of trade secret protection; the Higher Regional Court of Düsseldorf's 2021 decision established that vetting partners, ensuring minimum necessary disclosure, and maintaining executed NDAs constitute essential reasonable steps. Put differently, disclosure to a third party – even a service provider – without contractual confidentiality protections demonstrates that the information was not maintained as secret and fails both the secrecy element and the reasonable steps element.

National court decisions across Member States demonstrate strict application of the secrecy requirement in contexts involving third-party disclosure. The Dutch District Court Middle Netherlands in August 2018 held that technical drawings marked as confidential but shared with third parties without NDAs failed to qualify as trade secrets – the policy of maintaining secrecy existed, but the practice of unprotected disclosure defeated the claim. The Paris Court of Appeal in 2022 similarly held that sharing technical drawings with third parties without non-disclosure agreements failed the reasonable steps test, which necessarily implies that the information was not maintained as secret. To that extent, the judicial consensus across major tech hub jurisdictions – Germany, France, and the Netherlands – establishes that third-party disclosure without contractual protections defeats trade secret status regardless of other protective measures the holder may have implemented.

Applied to AI prompts, this doctrine creates a bright-line distinction: prompts submitted through enterprise AI services with contractual confidentiality protections potentially maintain secrecy (subject to the reasonable steps analysis discussed below), while prompts submitted through consumer-tier services without such protections fail the secrecy element and cannot qualify as trade secrets under EU law. This conclusion follows ineluctably from the principle that information disclosed to third parties without confidentiality agreements becomes "readily accessible" to those parties within the meaning of Article 2(1)(a), and specialists at AI providers – engineers, researchers, and data scientists who necessarily have at least potential access to user prompts – constitute "persons within the circles that normally deal with the kind of information in question." The secrecy element therefore establishes a threshold barrier: only prompts used exclusively through enterprise AI services with robust contractual confidentiality provisions can even potentially qualify as trade secrets.

## The puzzle of commercial value derived from proprietary models

The second element – that information "has commercial value because it is secret" – requires both that the information possess commercial value and that this value derive causally from the information's secrecy rather than from other characteristics. The Commission's Impact Assessment explained that information has commercial value "whether actual or potential" when "its unauthorized acquisition, use or disclosure is likely to harm the interests of the person lawfully controlling it, or where it undermines his or her scientific and technical potential, business or financial interests, strategic positions or ability to compete." Recital 14 of the directive emphasizes that the definition should cover information where there is "a legitimate interest in keeping them confidential and a legitimate expectation that such confidentiality will be preserved," and such information "should have a commercial value, whether actual or potential." The causal link – "because it is secret" – distinguishes trade secrets from other forms of valuable information; information that would retain its value even if publicly disclosed does not meet this requirement.

AI prompts present a distinctive challenge for the commercial value element because their utility depends fundamentally on the underlying large language model they instruct. A prompt engineered for ChatGPT produces value only when processed by OpenAI's GPT-4 or similar models; the same prompt applied to a different architecture may produce inferior results or fail entirely. This dependency raises the question whether prompts possess independent commercial value or merely derivative value that flows primarily from access to proprietary AI models. German courts have addressed this causal link question in other contexts – the Higher Regional Court of Düsseldorf held in 2021 that even if unauthorized use saves an infringer time or resources, if disclosure doesn't harm the holder's competitive position, the commercial value requirement may not be met. Applied to prompts, this suggests that if a prompt's value derives primarily from the underlying model rather than the prompt itself, and if disclosure of the prompt wouldn't harm the holder's competitive position because competitors lack access to the same model configuration, the commercial value element might fail.

However, three considerations support finding independent commercial value for sufficiently sophisticated prompts. First, the existence of commercial prompt marketplaces – PromptBase, FlowGPT, and similar platforms where users buy and sell prompts – demonstrates market recognition of prompts as valuable assets independent of any particular user's access to AI models. Prompts sold on these platforms derive value from their effectiveness across multiple users, each of whom has independent access to the underlying AI service; the prompt's value thus transcends any single user's model access. Second, specialized prompts that significantly improve output quality or efficiency provide measurable economic benefits – the pharmaceutical company vignette described prompts enabling 60% faster drug candidate identification, representing quantifiable time savings worth potentially millions of euros in accelerated research. Third, "system prompts" embedded in proprietary AI applications – instructions that customize how an AI model behaves within a specific application context – can represent substantial engineering investment and provide differentiation among competing products using the same underlying AI model.

The better view, therefore, distinguishes between simple prompts that any competent user could develop through brief experimentation – which lack the commercial value necessary for trade secret protection – and sophisticated prompts representing substantial investment in prompt engineering, testing, and refinement. The distinction parallels established trade secret doctrine protecting customer lists: publicly available contact information for individuals does not qualify as a trade secret, but a curated compilation of customers derived from substantial effort, investment, and analysis can qualify as a protectable compilation with commercial value deriving from the compilation itself rather than the individual data points. Similarly, individual prompting techniques may be publicly known, but a refined prompt representing months of optimization, A/B testing, and fine-tuning to achieve superior results constitutes a valuable compilation whose "precise configuration and assembly" – to use the language of Article 2(1)(a) – has commercial value because competitors lack this optimized formulation.

German courts applying the Geschäftsgeheimnisgesetz require objective proof that information has economic value, considering factors including value to the company, development costs, type of information, and importance to competitive position. The Higher Regional Court of Düsseldorf's nine-factor test for assessing trade secrets includes "value and development costs" and "importance to company" as distinct considerations, suggesting that even if information could theoretically be independently developed, the investment actually required to develop it contributes to its commercial value. Applied to AI prompts, this framework supports protecting prompts that represent substantial investment – documented development time, A/B testing costs, specialist salaries for prompt engineers – even if the prompts could theoretically be independently discovered, because the commercial value derives from avoiding the need to incur those development costs. To that extent, the commercial value element focuses not on whether information could be discovered independently in theory, but on whether the holder's actual investment in developing the information creates economic value that competitors could misappropriate by copying rather than independently investing.

The causal link – "because it is secret" – requires that disclosure would harm the holder's competitive advantage. For AI prompts, this test distinguishes between prompts whose disclosure would enable competitors to immediately replicate valuable outputs and prompts whose disclosure would provide minimal competitive benefit. Prompts that codify novel applications, combine techniques in non-obvious ways, or represent substantial optimization work satisfy this requirement because their disclosure allows competitors to appropriate the results of the holder's investment without incurring equivalent development costs. However, prompts that merely implement widely known techniques or achieve results that competitors have independently achieved fail this test – the value does not derive from secrecy because disclosure provides no competitive advantage. The commercial value element therefore operates as a filter, excluding trivial or widely known prompts while potentially protecting sophisticated prompts representing substantial investment and providing genuine competitive advantages to their holders.

## Reasonable steps in tension with cloud AI's distributed architecture  

The third element – that information "has been subject to reasonable steps under the circumstances, by the person lawfully in control of the information, to keep it secret" – requires trade secret holders to exercise what Recital 13 characterizes as a "duty of care as regards the preservation of the confidentiality of their valuable trade secrets." The "under the circumstances" qualifier establishes that the requirement is context-specific and proportionate, not absolute; the Commission's legislative history makes clear that measures need not be perfect or provide extreme security, and costs need not exceed the value of the secret. However, all Member State implementations and court decisions emphasize that holders must demonstrate actual protective measures, not merely stated policies – the Dutch court's pithy formulation that "policy without practice fails the reasonable steps test" captures the consensus approach across European jurisdictions.

German courts have developed the most detailed framework for assessing reasonable steps under the Geschäftsgeheimnisgesetz, establishing that protection requires measures at three levels: legal (non-disclosure agreements, employment contract provisions, contractual restrictions on partners), organizational (access restrictions, need-to-know policies, classification systems, employee training, exit procedures), and technical (passwords, encryption, access controls, authentication systems, monitoring). The Higher Regional Court of Düsseldorf's 2021 decision identified nine factors for proportionality assessment: type of trade secret, specific circumstances of use, value and development costs, nature of information, importance to company, size of company, usual confidentiality measures in the company, type of labeling or marking, and contractual provisions with employees and partners. French courts applying the Code de Commerce provisions implementing the directive emphasize that measures must be specific and targeted rather than blanket designations; generic "all information confidential" declarations in employment contracts are insufficient, and holders must specifically identify and mark confidential information, document protection measures taken, and implement both technical restrictions and contractual protections.

Applied to AI prompts, these requirements create significant challenges because the fundamental architecture of cloud AI services requires transmitting prompts across networks to third-party providers. The legal analytics firm in the opening vignette maintained NDAs, restricted internal access, and encrypted its prompt library – satisfying the legal and organizational prongs – but necessarily transmitted prompts to OpenAI's servers thousands of times daily through API calls. The pharmaceutical company's scientists used consumer ChatGPT accounts without confidentiality protections, clearly failing the reasonable steps test by disclosing prompts to a third party without contractual safeguards. The automotive manufacturer stored prompts in encrypted files accessible to only three senior engineers but still transmitted prompts to Anthropic's servers with each API call – potentially satisfying reasonable steps if, and only if, the manufacturer used Anthropic's enterprise service with contractual confidentiality protections.

The decisive question, then, is whether use of enterprise AI services with contractual confidentiality provisions, combined with internal controls on prompt access, constitutes "reasonable steps under the circumstances" or whether the necessity of transmitting prompts to third-party servers fundamentally defeats the secrecy requirement. National court guidance on third-party service providers suggests that contractual confidentiality provisions can suffice – the German courts' emphasis on "executed confidential disclosure agreements" implies that properly documented contractual protections with service providers satisfy reasonable steps even though the service provider necessarily accesses the information. The EUIPO's 2023 Trade Secrets Litigation Trends report notes that "reasonable steps" interpretation has shown significant development across Member States, with courts consistently requiring documented, implemented protection measures proportionate to the information's value.

However, the intersection of AI prompts with cloud computing reveals a structural tension: trade secret law developed in contexts where holders could maintain physical or at least exclusive digital control over secret information – customer lists in locked file cabinets, formulas in restricted laboratory notebooks, source code on access-controlled servers. Cloud AI services invert this model by requiring disclosure to third parties as a condition of using the information at all. The prompt cannot function without transmission to the AI provider's infrastructure; there is no equivalent to maintaining a chemical formula in a secured laboratory while using it in-house for manufacturing. To that extent, AI prompts represent a category of information where "reasonable steps" must necessarily include third-party disclosure, and the question becomes whether contractual protections can substitute for exclusive physical control.

The answer depends on the robustness of the contractual framework and its implementation. Enterprise AI agreements that contractually prohibit the provider from using prompts for any purpose other than processing the specific user's requests, that prohibit disclosure to other parties, that require deletion upon request, and that include audit rights allowing verification of compliance potentially satisfy the reasonable steps requirement – the holder has taken all measures feasible given the technical necessity of third-party processing. German courts' proportionality framework supports this conclusion: the nine-factor test includes "specific circumstances of use" as a factor, suggesting that if the information's use necessarily requires third-party involvement, reasonable steps must be assessed relative to that constraint rather than requiring impossible exclusive control. However, this conclusion requires documented evidence of the contractual protections, evidence that the enterprise service tier was selected rather than consumer services lacking such protections, internal controls limiting which employees can submit prompts and monitoring compliance, prompt sanitization procedures to remove unnecessary sensitive information before submission, and training ensuring employees understand the confidentiality framework.

Put differently, reasonable steps for AI prompts require a comprehensive protection program that acknowledges the necessity of third-party disclosure while minimizing associated risks: use exclusively of enterprise AI services with documented contractual confidentiality protections, internal access controls limiting who can create and submit prompts, technical measures including encryption in transit and at rest, classification systems identifying which prompts contain trade secret information, employee training on proper use of AI services, monitoring and audit procedures detecting unauthorized disclosure, and incident response plans addressing breaches. These measures parallel the protections German courts require for traditional trade secrets but adapted to accommodate the distributed architecture of cloud AI. This is straightforward as a doctrinal matter – reasonable steps must be "under the circumstances," and the circumstances of AI prompt use include technical necessity of third-party processing – but demanding as a practical matter, requiring substantial investment in legal, organizational, and technical infrastructure that many businesses have not yet implemented.

## Counterarguments: why prompts likely fail trade secret protection

Three principal arguments challenge whether AI prompts can or should qualify as trade secrets under Directive 2016/943, each rooted in fundamental characteristics of AI systems and trade secret doctrine. First, prompts may be insufficiently secret because they are too easily reverse-engineered from AI outputs, failing Article 2(1)(a)'s requirement that information be "not readily accessible." Second, prompts may lack the independent commercial value Article 2(1)(b) requires because their value derives primarily from underlying proprietary AI models rather than the prompts themselves. Third, reasonable steps may be structurally impossible for cloud-based AI prompts, defeating Article 2(1)(c), because the fundamental architecture requires disclosure to third parties in ways that existing trade secret doctrine has not accommodated.

The reverse engineering challenge rests on recent technical research demonstrating that effective prompts can be reconstructed from observing only a small number of AI outputs. Academic computer science research published in 2024 describes "reverse prompt engineering" techniques that reconstruct original prompts from as few as five text outputs using black-box, zero-shot methods that leverage the language model itself as an optimizer – the technique achieved prompts 5.8% closer in cosine similarity to originals than previous state-of-the-art methods. Earlier approaches including "logit2prompt" using next-token probability distributions and "output2prompt" requiring 64 outputs have established that prompt inference from outputs is not merely theoretical but practically achievable with commercially available tools. If prompts are reliably reconstructible from publicly available outputs through techniques that Article 3(1)(b) of the directive explicitly recognizes as lawful – "observation, study, disassembly or testing of a product or object that has been made available to the public or that is lawfully in the possession of the acquirer" – then prompts fail the secrecy requirement because they are "readily accessible" through proper means to any competitor willing to invest in reverse engineering.

This argument draws additional strength from Recital 16 of the directive, which provides that "in the interest of innovation and to foster competition, the provisions of this Directive should not create any exclusive right to know-how or information protected as trade secrets" and explicitly states that "reverse engineering of a lawfully acquired product should be considered as a lawful means of acquiring information, except when otherwise contractually agreed." The directive thus establishes a policy preference for permitting reverse engineering, and the ease with which prompts can be inferred from outputs suggests that the directive's drafters would not have intended to grant trade secret protection to information so readily reconstructible. Moreover, the widespread practice within the AI community of sharing and discussing effective prompts – exemplified by prompt marketplaces, online repositories, and technical forums where users freely exchange prompting techniques – demonstrates that prompts are not treated as confidential in industry practice, undermining claims that particular prompts meet the "not generally known among or readily accessible to persons within the circles that normally deal with the kind of information in question" standard.

The independent commercial value challenge contends that prompts function more like instructions for using a tool than like the tool itself, and that trade secret protection should not extend to mere usage instructions that derive their value entirely from proprietary tools owned by others. A prompt for ChatGPT is worthless without access to OpenAI's GPT-4 model; the pharmaceutical company's drug candidate identification prompts provide value only because Claude processes them, and Claude's capabilities derive from Anthropic's billions of dollars in model development investment rather than from the user's prompt engineering work. This dependency distinguishes prompts from paradigmatic trade secrets like chemical formulas or manufacturing processes, which have value independent of any third party's proprietary assets – a formula for a drug compound has value regardless of who manufactures it, and a manufacturing process has value to whoever controls the manufacturing facility. Prompts, by contrast, are entirely dependent on and subordinate to the underlying AI models, suggesting that any commercial value actually derives from model access rather than prompt design.

Furthermore, the high probability of independent discovery undermines commercial value claims for most prompts. Because prompt engineering is a relatively low-barrier skill – requiring no specialized equipment, no substantial capital investment, and no rare expertise – competitors can reasonably be expected to independently discover similar or functionally equivalent prompts through their own experimentation. The directive's Article 3(1)(a) explicitly recognizes "independent discovery or creation" as lawful, and if effective prompts for common tasks can be independently discovered by competent users within weeks or months of experimentation, the information lacks the durability and exclusivity characteristic of traditional trade secrets. Chemical formulas may remain secret for decades; manufacturing processes may resist independent discovery indefinitely; but AI prompts face the constant risk that competitors will independently converge on similar solutions through parallel experimentation, suggesting that the information's commercial value does not truly derive from its secrecy but rather from the prompter's access to the underlying model.

The structural impossibility argument contends that the "reasonable steps" requirement cannot be satisfied for information that must be disclosed to third-party cloud providers as a condition of use, and that extending trade secret protection to such information would distort the doctrine beyond its coherent boundaries. Trade secret law developed to protect information that holders could maintain under their exclusive physical or digital control – the formula kept in a vault, the customer list on a password-protected server, the manufacturing process known only to employees under strict NDAs. Cloud AI inverts this model by requiring disclosure as a precondition of use; the information must leave the holder's control and reside on third-party infrastructure to function at all. Even with contractual confidentiality provisions, the AI provider possesses the information, can technically access it, and represents a potential point of failure through security breaches, employee misconduct, or contractual breach.

This structural characteristic distinguishes AI prompts from other information processed by third-party service providers – payroll data sent to processing companies, tax information shared with accountants, or manufacturing specifications sent to contract manufacturers – because those third parties process the information but do not require the information to provide the service. A payroll processor could calculate employee payments with generic test data; an AI model cannot process a prompt without receiving the actual prompt. To that extent, the information disclosed to AI providers is not incidental to the service but constitutes the core input the service processes, creating a fundamental dependency incompatible with maintaining information as secret. Moreover, the potential for AI providers to inadvertently or deliberately use prompts for model training, to learn from aggregated prompt patterns across users, or to face legal obligations to disclose prompts to regulators or in litigation creates risks that no amount of contractual protection can fully eliminate – the information has entered a domain beyond the holder's exclusive control in ways that trade secret law has not traditionally accommodated.

These three challenges – insufficient secrecy due to reverse engineering, lack of independent commercial value, and structural impossibility of reasonable steps – collectively suggest that AI prompts represent a poor fit for trade secret protection under existing EU law. The directive's three-part test developed to protect information holders can maintain as genuinely confidential; prompts necessarily disclosed to cloud providers fall outside this paradigm. However, these arguments face responsive challenges that reveal the doctrinal question's complexity rather than definitively resolving it.

## Resolution: limited protection for sophisticated prompts under enterprise frameworks

The arguments against trade secret protection for AI prompts carry substantial force, but they prove too much – if accepted fully, they would also eliminate protection for other categories of information that Directive 2016/943 was clearly intended to protect. Software source code can be reverse-engineered from compiled binaries through decompilation and analysis, yet courts routinely recognize source code as protectable trade secrets; customer lists can be independently discovered through market research, yet compilations of customer information qualify as trade secrets when they represent substantial investment; business methods must be disclosed to employees and sometimes partners to be implemented, yet they remain protectable subject to reasonable confidentiality measures. The question is not whether AI prompts present distinctive challenges – they plainly do – but whether these challenges render protection impossible or merely demanding.

The Court of Justice of the European Union's decision in Case C-203/22, Dun \u0026 Bradstreet Austria, decided on 27 February 2025, provides crucial guidance on the intersection between algorithmic information and trade secret protection, though the case addressed GDPR transparency obligations rather than trade secret validity directly. The CJEU held that controllers using automated decision-making systems must provide "meaningful information about the logic involved" but need not disclose the algorithm itself; trade secret protection under Directive 2016/943 can justify withholding detailed algorithmic information from data subjects, though not from supervisory authorities or courts conducting proportionality assessments. The Court established that when a controller claims information contains trade secrets, the controller must provide allegedly protected information to the competent supervisory authority or court, which then balances competing rights and interests on a case-by-case basis – Austrian law creating a blanket exemption for trade secrets was impermissible. The decision thus acknowledges that algorithmic information including the logical instructions that control AI system behavior can qualify as trade secrets while emphasizing that protection is not absolute and must yield to competing fundamental rights and transparency obligations where proportionality requires.

Applied to AI prompts, the Dun \u0026 Bradstreet framework suggests that prompts can in principle qualify as trade secrets but face heightened scrutiny when their protection conflicts with transparency requirements under the GDPR, the AI Act, or other regulatory frameworks. The decision's emphasis on case-by-case balancing rather than categorical rules supports a nuanced approach that distinguishes between simple prompts offering minimal innovation and sophisticated prompts representing substantial investment and genuine competitive advantage. This parallels the Court's treatment of algorithms themselves – not categorically excluded from protection, but subject to disclosure requirements where fundamental rights or regulatory transparency obligations outweigh commercial confidentiality interests.

The resolution must therefore distinguish among prompt categories. First, simple prompts that any competent user could develop through minimal experimentation – basic formatting instructions, common prompting techniques, straightforward queries – do not qualify as trade secrets because they fail all three elements: they are "generally known" within professional circles using AI systems, lack commercial value because competitors can independently discover them trivially, and cannot justify substantial protective measures given their minimal value. These prompts resemble individual entries in a customer list – the format "Dear [Name]" or the technique of asking an AI to "explain in simple terms" is public knowledge, and compiling such techniques provides no more protection than collecting publicly available contact information.

Second, intermediate prompts representing modest optimization or specialization – domain-specific queries, tested formulations that improve reliability, or structured templates that standardize outputs – occupy ambiguous territory. These prompts might satisfy the commercial value element if they represent genuine efficiency improvements, and they might satisfy the secrecy element if not widely shared, but they face challenges under the reasonable steps requirement because the investment required to protect them (comprehensive legal, organizational, and technical measures) may exceed their value, failing proportionality. Moreover, the high probability of independent discovery for intermediate prompts – any competent practitioner working in the same domain will likely develop similar approaches – undermines claims that value derives from secrecy rather than from general domain expertise.

Third, sophisticated prompts representing substantial investment – months of prompt engineering work, extensive A/B testing, quantified performance improvements, integration into proprietary systems, or novel applications of AI capabilities – can potentially qualify as trade secrets if, and only if, used exclusively through enterprise AI services with robust contractual confidentiality provisions and subject to comprehensive internal protection measures. These prompts satisfy the secrecy element because, despite third-party disclosure to the AI provider, contractual prohibitions on use or disclosure render the information "not readily accessible" to competitors – the AI provider is contractually bound not to use prompts for training or disclose them to others, functionally limiting access as effectively as physical security measures. They satisfy the commercial value element because substantial investment in development creates value that competitors could misappropriate by copying rather than independently investing, and because documented performance improvements demonstrate economic worth. They satisfy the reasonable steps element through the comprehensive protection framework outlined above: enterprise service agreements, internal access controls, technical measures including encryption, classification systems, employee training, and monitoring.

This resolution draws support from German courts' proportionality framework under the Geschäftsgeheimnisgesetz, which requires balancing protection measures against information value and considering "specific circumstances of use." If prompts have substantial value (documented through development costs and performance improvements), and if their use necessarily requires third-party processing (inherent in cloud AI architecture), then reasonable steps must be assessed relative to these constraints – demanding exclusive physical control would be impossible, but requiring the maximum feasible protection given technical constraints is both possible and proportionate. The Dutch court's emphasis on actual practice over stated policy requires not merely adopting formal protection programs but implementing and enforcing them – employees who share prompts via consumer AI services in violation of company policy demonstrate that reasonable steps have not been taken in practice, regardless of written policies.

To that extent, the answer to whether AI prompts qualify as trade secrets under EU law depends critically on prompt sophistication and protection rigor: simple prompts categorically fail to qualify; sophisticated prompts representing substantial investment can qualify if subjected to comprehensive protection measures including exclusive use of enterprise AI services with contractual confidentiality provisions, internal access controls, technical protections, and documented enforcement; intermediate prompts face case-by-case assessment where proportionality and independent discovery probability will often defeat protection claims. This framework harmonizes with the directive's policy objectives – encouraging investment in valuable information while permitting reverse engineering, independent discovery, and employee mobility – by protecting genuine innovation while refusing protection to trivial or widely known techniques.

However, the framework faces two unresolved tensions that will require either CJEU clarification or legislative amendment to fully resolve. First, no CJEU decision has directly interpreted Directive 2016/943's three-part test – the directive entered into force in 2016 with a June 2018 transposition deadline, and as of October 2025, no preliminary ruling under Article 267 TFEU has addressed core definitional questions. National courts applying German, French, Dutch, and Irish implementing legislation have developed divergent approaches to "reasonable steps" in particular, with Germany's nine-factor proportionality test, the Netherlands' stringent practice-over-policy requirement, and France's procedural protections representing different doctrinal emphases. Until the CJEU addresses whether third-party disclosure with contractual protections can satisfy the secrecy and reasonable steps requirements, cross-border uncertainty will persist – prompts qualifying as trade secrets in Germany under proportionality analysis might fail in the Netherlands under the stringent practice-focused test.

Second, the intersection between trade secret protection and AI transparency requirements under the AI Act remains incompletely theorized. The AI Act imposes transparency obligations on high-risk AI systems including technical documentation, training data disclosure, and deployment logs – Recital provisions acknowledge that trade secret information "should be safeguarded" but provide no detailed operational guidance on balancing commercial confidentiality against regulatory transparency. Academic scholarship analyzing this tension argues that trade secrets and transparency mandates "directly stand at odds with critical constitutional concepts," and the EUIPO's 2023 Trade Secrets Litigation Trends report notes that developments are needed to clarify the potential role of trade secrets in the data economy. The Dun \u0026 Bradstreet decision provides a framework – case-by-case balancing by authorities or courts – but implementing this framework for AI Act compliance will require either Commission guidance or judicial decisions establishing when transparency obligations override trade secret protection.

Put differently, AI prompts can qualify as trade secrets under current EU law, but only sophisticated prompts subjected to rigorous protection measures, and even then subject to potential displacement by transparency requirements under the GDPR, AI Act, or other regulatory frameworks where fundamental rights or public interest considerations outweigh commercial confidentiality. The legal framework accommodates prompt protection within existing doctrine by treating third-party disclosure with contractual safeguards as consistent with secrecy and reasonable steps, but this accommodation is contestable and has not been tested through CJEU interpretation. Businesses seeking to protect valuable prompt engineering work must implement comprehensive protection programs exceeding the rigor typical for traditional trade secrets, and must prepare for the possibility that courts will require disclosure where transparency obligations so demand – trade secret protection for prompts exists under EU law, but it is conditional, demanding, and ultimately provisional pending authoritative judicial interpretation.


## Comparative framework analysis and the path forward

Having examined four potential IP frameworks - copyright, software/database protection, patents, and trade secrets - it is now possible to assess comparatively which approach offers the most appropriate protection for prompts, what tradeoffs each entails, and whether reform is needed.

### Comparative assessment of protection frameworks

**Copyright protection** offers strong rights (70 years post-author, exclusive reproduction and adaptation rights, cross-border harmonization) but imposes the fundamental requirement that works be "author's own intellectual creation" reflecting personality through free and creative choices. As demonstrated, prompts face insurmountable obstacles: they are instructions about what to create (ideas) rather than creative expression itself; they are functionally constrained by their communicative purpose; and protection would risk monopolizing ideas in violation of core principles. Copyright applies only in exceptional cases where prompts function as independent literary works, and even then, protection extends only to the textual expression, not to functional equivalents or AI outputs. The copyright framework's fixation on expression versus ideas makes it fundamentally unsuited to protecting instrumental instructions like prompts.

**Software protection** under the specialized regime similarly fails because prompts are not source code, object code, or preparatory design material from which programs result. The CJEU's narrow interpretation limiting protection to executable code expressions excludes user inputs and instructions. Database sui generis protection offers more promise for prompt collections but perversely protects investment in obtaining or verifying existing data while excluding investment in creating data - meaning the most valuable prompt collections developed through creative engineering receive no protection while compilations of others' prompts might. This creates misaligned incentives that fail to reward innovation.

**Patent protection** is categorically unavailable because prompts lack technical character, solve linguistic rather than technical problems, and constitute excluded subject matter (methods for performing mental acts, presentations of information). Under the COMVIK approach, prompt innovations are non-technical features contributing nothing to inventive step. The EPO's rigorous technical effect requirement, appropriate for its purposes, means patents cannot accommodate linguistic or cognitive innovations like prompts regardless of their commercial value.

**Trade secrets protection** is the only framework offering genuinely viable protection, but it is narrow, conditional, and fragile. Protection requires satisfaction of all three cumulative requirements (secrecy, value from secrecy, reasonable steps), each posing challenges. Secrecy must be maintained while using prompts commercially - feasible for internal use or B2B contexts with NDAs but difficult for consumer-facing services. The requirement that value derive from secrecy rather than from the AI model or general knowledge creates causation proof challenges. Reasonable steps requirements demand comprehensive security measures. Most critically, trade secret protection offers no rights against independent development or reverse engineering - competitors who reconstruct effective prompts through their own efforts or by analyzing outputs commit no violation. Protection lasts only while secrecy is maintained, and disclosure (intentional or inadvertent) destroys rights permanently with no residual protection.

### Tradeoffs and implications

Each framework embodies different policy balances between incentivizing creation and ensuring access. **Copyright's requirement of originality and creative expression** serves the policy goal of rewarding human creativity while preserving the public domain of ideas, facts, and functional information. Its inapplicability to prompts reflects that prompts are closer to functional instructions (like product specifications or search queries) than to creative works warranting exclusive rights. Extending copyright to prompts would expand IP protection beyond its traditional boundaries into the realm of utilitarian instruction-giving.

**Patent law's requirement of technical character** reflects the judgment that innovation in non-technical fields - business methods, mental processes, linguistic formulations - should remain freely available for competition. The EPO's insistence on "further technical effect" prevents monopolization of abstract ideas and methods regardless of their novelty or commercial value. This boundary excludes prompts not because they lack value but because patent law deliberately limits its scope to technical innovation. Extending patents to prompts would fundamentally alter the technical character requirement that has defined European patent law.

**Trade secret law's conditional protection** based on secrecy rather than disclosure reflects an opposite policy: information kept secret can be protected, but only as long as secrecy is maintained and only against wrongful acquisition. This allows protection for commercially valuable information (recipes, customer lists, technical know-how) while preserving rights to independent development and reverse engineering. For prompts, this framework is more naturally suited than copyright or patents because it protects valuable information without creating exclusive rights that block others from reaching the same information independently.

**Database sui generis protection** reflects a specific policy choice to protect investment in information aggregation separate from creativity. However, the CJEU's interpretation limiting protection to investment in obtaining (not creating) data creates the perverse outcome that creative prompt development is unprotected while mere aggregation is protected. This interpretive choice, arguably inconsistent with the Directive's recitals emphasizing protection of investment in "obtaining, verification or presentation," has been criticized by scholars but remains binding.

### The question of reform: is new legislation needed?

The analysis reveals a fundamental mismatch between existing IP categories and the characteristics of prompts. **Prompts occupy an uncomfortable middle ground**: more than mere ideas (requiring skill and investment), but less than creative expression (being functional instructions); commercially valuable (demonstrated by active marketplaces), but not traditionally protectable (falling outside existing categories); independently discoverable (multiple prompters can reach similar solutions), but requiring investment to develop (time, testing, expertise).

**Arguments supporting reform** and potential creation of sui generis protection include: (1) market failure - without protection, the appropriability problem discourages investment in prompt development once disclosure occurs; (2) innovation incentives - protecting prompts could encourage development of more sophisticated human-AI interaction methods; (3) international competitiveness - if other jurisdictions protect prompts more robustly, EU businesses may face disadvantages; (4) recognition of investment - prompt engineering requires genuine skill development and R&D deserving reward; (5) existing inadequacy - trade secrets offer only limited protection unsuited to many commercial models.

**Arguments against reform** and for maintaining current law include: (1) risk of monopolization - protecting prompts could restrict access to AI technology by monopolizing communication methods; (2) cumulative innovation - prompt engineering builds incrementally on others' work, and property rights could block this cumulative process; (3) trade secret sufficiency - businesses can protect genuinely valuable prompts through secrecy and contractual measures; (4) difficulty defining scope - where would protection begin and end given the spectrum from simple to complex prompts; (5) alternatives available - first-mover advantages, brand reputation, service quality, and contract law provide protection mechanisms; (6) idea-expression conflation - protecting prompts risks collapsing the idea-expression distinction central to IP law; (7) international fragmentation - EU-specific protection could create conflicts with trading partners.

The scholarly commentary generally counsels against hasty legislative intervention. Professors Quintais and Hugenholtz argue that existing EU copyright rules are "generally suitable and sufficiently flexible to deal with the challenges posed by AI-assisted output" when properly applied. The European Copyright Society has emphasized the need to "balance the interests of human authors and performers; the interests of users and of the wider public... [and] the enhancement of research and innovation." The European Parliament's 2020 Resolution emphasized providing "balanced and innovation-driven protection of intellectual property... to strengthen the international competitiveness of European companies, including against possible abusive litigation tactics."

**The AI Act's approach suggests regulatory restraint.** The Act addresses AI systems comprehensively but does not create new IP rights for prompts or AI outputs. Instead, Recital 106 requires that "providers of general purpose AI models should put in place a policy to comply with Union law on copyright and related rights, in particular to identify and comply with the reservation of rights expressed by rightsholders." This approach relies on existing copyright frameworks rather than inventing new categories. The emphasis on transparency (documenting training data, respecting opt-outs) addresses AI development broadly while leaving specific IP questions to existing frameworks and courts.

### Recommended approach

**In the near term, the appropriate approach is restraint pending judicial clarification and market evolution.** Several considerations support this recommendation:

**First, judicial interpretation of existing frameworks remains incomplete.** The CJEU has not yet addressed whether sophisticated prompts can satisfy the originality threshold, whether prompt collections qualify for database protection under verification investment, or how trade secret protection balances against AI Act transparency requirements. National courts are beginning to see cases involving prompt protection claims. Allowing case law to develop will clarify where existing doctrine settles before legislating.

**Second, the prompt engineering field is rapidly evolving.** Business models, technical practices, and economic dynamics are changing quickly. Legislative intervention now might entrench approaches that become obsolete or might fail to anticipate new developments. Regulatory humility counsels waiting until patterns stabilize.

**Third, alternative protection mechanisms exist.** Businesses can combine multiple strategies: (1) trade secrets for genuinely confidential prompts; (2) contracts imposing confidentiality and use restrictions; (3) technological protection measures restricting access; (4) first-mover advantages and brand reputation; (5) integration of prompts into larger protectable systems (software, databases). These combined approaches may provide adequate protection for most commercial models.

**Fourth, international coordination is essential.** IP protection is increasingly global. The U.S. Copyright Office has taken positions on AI-related issues. China's courts have issued decisions. WIPO has conducted extensive consultations. Unilateral EU action creating prompt-specific protection could create conflicts and fragmentation. Any reform should emerge from international dialogue.

**If reform ultimately proves necessary**, the most appropriate model would be a **limited sui generis right resembling database protection but focused on verification rather than creation**. Such a right might protect documented investment in: (1) systematic testing and verification of prompt effectiveness across multiple AI systems; (2) quality assurance and reliability validation; (3) performance metric documentation; (4) sophisticated presentation and access systems. Protection would extend only to preventing extraction and reutilization of substantial portions of prompt collections, not to preventing independent creation or use of individual prompts. The term should be short (perhaps 5-10 years rather than copyright's 70 years) to balance incentives against access. Most importantly, any protection must preserve rights to independent development, reverse engineering of publicly available outputs, and employee mobility with general skills.

## Conclusion

The question of whether EU law protects AI prompts reveals fundamental tensions between traditional intellectual property categories and novel forms of commercially valuable information emerging from human-AI interaction. The comprehensive legal analysis demonstrates that **prompts receive minimal protection under current EU law**. Copyright protection is unavailable because prompts constitute instructions about what to create (ideas) rather than creative expression, fail to reflect personality through free and creative choices in most cases, and are functionally constrained by their communicative purpose. Software protection fails because prompts are not source code, object code, or preparatory design material from which programs result. Database protection might apply to collections if substantial documented investment in verification or presentation (not creation) is proven, but the CJEU's narrow interpretation excludes most valuable prompt development investment. Patents are categorically unavailable because prompts lack technical character and constitute excluded subject matter.

**Trade secrets protection offers the only genuinely viable framework**, but protection is conditional and fragile. Sophisticated prompt systems maintained under rigorous secrecy with comprehensive protective measures might qualify, but simple prompts, prompts entered into public AI systems, and prompts readily reconstructible from outputs fail protection. The requirement that value derive from secrecy rather than from the underlying AI model creates proof challenges. Most critically, trade secret protection offers no rights against independent development or reverse engineering - competitors who reconstruct prompts through their own efforts commit no violation.

**Whether reform is needed remains uncertain and should await further developments.** The current legal regime reflects deliberate policy choices: copyright's fixation on creative expression versus functional instruction; patent law's limitation to technical innovation; trade secret law's conditioning protection on secrecy maintenance. These boundaries exclude prompts not because they lack value but because existing IP categories embody normative judgments about what types of information warrant exclusive rights.

The emergence of prompt engineering highlights a broader question: as AI systems become ubiquitous and human-AI interaction grows more sophisticated, do traditional IP categories adequately address new forms of valuable information? Prompts exemplify information that requires skill and investment to create, provides commercial advantage, but fits uncomfortably within existing frameworks. The challenge for EU IP law is balancing incentives for prompt development against the imperative to preserve access to AI technology, avoid monopolization of communication methods, and maintain the public domain of ideas and functional information.

For the present, businesses developing valuable prompts should rely on trade secret protection combined with contractual restrictions, using enterprise AI deployments with confidentiality protections rather than public AI services, implementing comprehensive security measures, and documenting investment in verification and testing. Courts should apply existing originality and technical character requirements rigorously rather than diluting standards to accommodate new subject matter. The European Commission should monitor developments but avoid hasty legislative intervention that might create unintended consequences or international conflicts. If reform ultimately proves necessary, it should take the form of a limited sui generis right focused on protecting documented verification investment rather than creative expression, with short protection terms and broad exceptions preserving independent development and employee mobility rights.

The fundamental lesson is that not all valuable information requires or should receive IP protection. Some information - including functional instructions, methods of communication, and practical know-how - may appropriately remain outside property rights regimes, accessible through learning, independent development, and market competition. Prompts may fall within this category. The current legal framework's restrictive approach to prompt protection reflects this judgment and should not be abandoned without compelling evidence that market failure requires intervention.