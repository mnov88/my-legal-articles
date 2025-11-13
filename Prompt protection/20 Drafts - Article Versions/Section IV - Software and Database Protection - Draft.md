# IV. Software and Database Protection

## A. The Software Directive 2009/24/EC

Beyond general copyright protection, the Software Directive establishes a specialized regime that might accommodate prompts where ordinary copyright fails. Article 1(1) provides that "Member States shall protect computer programs, by copyright, as literary works within the meaning of the Berne Convention" and that "the term 'computer programs' shall include their preparatory design material."[^68] Recital 7 elaborates that protection extends to "programs in any form, including those which are incorporated into hardware" and to "preparatory design work leading to the development of a computer program provided that the nature of the preparatory work is such that a computer program can result from it at a later stage."[^69]

[^68]: Software Directive (n 2) art 1(1).

[^69]: ibid recital 7.

Two potential theories present themselves. First, prompts might constitute "computer programs" within the meaning of the Directive – natural language instructions that direct computational processes and control AI system behavior. Second, prompts might qualify as "preparatory design material" from which AI outputs result at a later stage, analogous to specifications or pseudocode from which programmers implement software.

The CJEU's restrictive interpretation of the Software Directive's scope forecloses both theories.

In *Bezpečnostní softwarová asociace v Ministerstvo kultury* (BSA), the Court addressed whether graphical user interfaces qualify as protectable computer programs.[^70] The Court held that GUIs "do not enable the reproduction of the computer program, but merely constitute one element of that program by means of which users make use of the features of a computer program."[^71] Only the actual source code or object code constituting the program's expression receives protection under the Software Directive; user-facing elements through which individuals interact with software fall outside the Directive's scope.[^72]

[^70]: Case C-393/09 *Bezpečnostní softwarová asociace v Ministerstvo kultury* EU:C:2010:816.

[^71]: ibid para 42.

[^72]: ibid para 45.

This principle applies directly to prompts. Just as GUIs constitute user-facing elements enabling interaction with software rather than constituting the software itself, prompts constitute textual inputs enabling users to direct AI system behavior rather than constituting the AI programs themselves. Prompts do not "enable the reproduction of the computer program" – they do not contain or express the trained neural network weights, inference algorithms, or computational processes that constitute the AI system. They are inputs to programs, not programs.

The Court's decision in *SAS Institute Inc v World Programming Ltd* reinforces this conclusion through a different analytical path.[^73] SAS Institute concerned whether copyright protected the functionality, programming language, and data file formats of statistical analysis software. The Court held categorically that "neither the functionality of a computer program nor the programming language and the format of data files used in a computer program in order to exploit certain of its functions constitute a form of expression" protected under the Software Directive.[^74] The functionality of software – what it does, what operations it performs, what outputs it generates – remains unprotectable regardless of the skill and investment required to design it.[^75]

[^73]: Case C-406/10 *SAS Institute Inc v World Programming Ltd* EU:C:2012:259.

[^74]: ibid para 39.

[^75]: ibid para 45.

Prompts specify functionality – they describe what the AI should do, what outputs it should generate, what constraints it should observe, and what format results should take. This situates them squarely within the category of functional specifications that *SAS Institute* held unprotectable. The prompt "write a 500-word essay in academic style with Harvard citations addressing climate policy" specifies functionality as precisely as a software specification document that states "the program shall generate reports in PDF format containing statistical analyses with graphical visualizations." Both describe what outputs the system should produce; neither constitutes the expression of how the system produces those outputs.

The Court's reasoning in *SAS Institute* proves dispositive: "if it were accepted that the functionality of a computer program can be protected as such, that would amount to making it possible to monopolise ideas, to the detriment of technological progress and industrial development."[^76] Protecting prompts would monopolize methods of AI interaction – particular ways of instructing systems to perform functions – in violation of the principle that ideas, procedures, and methods must remain free for all to use and build upon.

[^76]: ibid para 40.

The CJEU's recent decision in *Sony Computer Entertainment Europe Ltd v Datel Design & Development Ltd* extends this restrictive approach to data inputs that control program behavior.[^77] The Court held that "the content of the variables which are stored temporarily in a console's RAM memory during the playing of a video game does not itself constitute a form of expression of the computer program which is protected by copyright."[^78] Variables stored in RAM – data values that directly affect how the program executes and what outputs it generates – are not protected as program expressions even when they control system operation.[^79]

[^77]: Case C-159/23 *Sony Computer Entertainment Europe Ltd v Datel Design & Development Ltd* EU:C:2024:649.

[^78]: ibid para 33.

[^79]: ibid para 35.

The parallel to prompts is direct. Prompts function as inputs to AI systems that control how the system processes information and generates outputs, precisely analogous to RAM variables that control video game behavior. If data inputs that directly affect program operation are not protected as program expressions, then textual prompts that control AI operation should equally fall outside protection. Both are functional inputs to existing programs rather than expressions of the programs themselves.

The second theory – that prompts constitute preparatory design material – fails for three independent reasons.

First, Recital 7 requires that the preparatory work be "such that a computer program can result from it at a later stage."[^80] Prompts do not lead to computer programs; they lead to AI-generated outputs like text, images, or analyses. The AI model itself – which already exists as a complete program – processes the prompt, but the prompt does not constitute design work for creating that program. A prompt given to ChatGPT does not generate program code; it generates natural language responses by invoking existing computational processes.

[^80]: Software Directive (n 2) recital 7.

Second, preparatory design material protected under the Software Directive must possess sufficient technical specificity to constrain program implementation – what academic commentary describes as "quasi-coding" that approaches the precision of actual source code.[^81] Flow charts, detailed technical specifications, and architecture documents qualify because they provide sufficiently detailed instructions that programmers can implement them with minimal additional creative choices. Prompts lack this technical specificity; they are high-level natural language instructions that leave implementation entirely to the AI system's existing algorithms.

[^81]: Thomas Dreier and Gernot Schulze, *Urheberrechtsgesetz: UrhG Kommentar* (7th edn, C.H. Beck 2022) § 69a Rn. 23–27.

Third, preparatory design material exhibits determinism – the same specifications lead consistently to functionally equivalent implementations. As Ana Sampaio observes, "the same prompt to the same model will not deliver the same results."[^82] Prompts submitted to AI systems at different times generate varying outputs due to probabilistic sampling, temperature parameters, and stochastic inference processes. This non-determinism fundamentally distinguishes prompts from preparatory design materials, which must be sufficiently specified to enable consistent program implementation.

[^82]: Ana Sampaio, 'Are Prompts Copyrightable?' (Kluwer Copyright Blog, 14 June 2023) <http://copyrightblog.kluweriplaw.com/2023/06/14/are-prompts-copyrightable> accessed 10 November 2025.

The conclusion is unequivocal: prompts do not qualify for protection as computer programs or preparatory design material under the Software Directive. They are instructions to programs, not programs themselves; they specify desired functionality rather than implementing it; and they lack the technical specificity and determinism required for preparatory design work.

## B. The Database Directive 96/9/EC

While individual prompts fail both ordinary copyright and software protection, collections of prompts raise distinct questions under the Database Directive. The Directive establishes two forms of protection: copyright protection for original databases under Article 3, and a sui generis right protecting investment in databases under Article 7.[^83]

[^83]: Database Directive (n 2) arts 3, 7.

Article 1(2) defines "database" as "a collection of independent works, data or other materials arranged in a systematic or methodical way and individually accessible by electronic or other means."[^84] A collection of prompts clearly satisfies this definition – individual prompts constitute independent textual materials that can be arranged systematically by category, function, or effectiveness and accessed individually in digital repositories.

[^84]: ibid art 1(2).

Database copyright protection requires that "by reason of the selection or arrangement of their contents," databases "constitute the author's own intellectual creation."[^85] The CJEU held in *Football Dataco Ltd v Yahoo! UK* that originality demands "free and creative choices" in selection or arrangement that stamp the author's "personal touch" on the database.[^86] Where "the setting up of the database is dictated by technical considerations, rules or constraints which leave no room for creative freedom," the originality requirement fails.[^87]

[^85]: ibid art 3(1).

[^86]: *Football Dataco* (n 5) para 38.

[^87]: ibid para 39.

Applied to prompt collections, this standard proves difficult to satisfy. If prompts are selected based on effectiveness for different tasks – customer service versus creative writing versus technical documentation – the selection principle reflects functional optimization rather than creative choices expressing personality. If prompts are arranged alphabetically, by task type, or by effectiveness metrics, the arrangement follows conventional organizational schemes rather than reflecting creative ability. The rejection of "sweat of the brow" protection in *Football Dataco* proves dispositive: "the fact that the setting up of the database required...significant labour and skill of its author...cannot as such justify the protection of it by copyright...if that labour and that skill do not express any originality in the selection or arrangement of that data."[^88]

[^88]: ibid para 42.

Even where database copyright might apply to a prompt collection exhibiting genuinely creative selection or arrangement, Article 3(2) expressly provides that "the copyright protection of databases...shall not extend to their contents and shall be without prejudice to any rights subsisting in those contents themselves."[^89] Database copyright protects the structure – creative selection and arrangement – but not the data elements within the collection. Users could extract and reuse individual prompts without infringing database copyright, which protects only against extraction or reuse of substantial portions reflecting the protected selection or arrangement.

[^89]: Database Directive (n 2) art 3(2).

The sui generis right established in Article 7 provides an alternative protection mechanism independent of originality requirements. Article 7(1) grants database makers who demonstrate "qualitatively and/or quantitatively a substantial investment in either the obtaining, verification or presentation of the contents" the right "to prevent extraction and/or re-utilization of the whole or of a substantial part...of the contents of that database."[^90] This protection regime – created precisely because the CJEU's restrictive originality standard left commercially valuable databases unprotected by copyright – might apply to prompt collections involving substantial investment.

[^90]: ibid art 7(1).

However, the CJEU's interpretation in *British Horseracing Board Ltd v William Hill Organization Ltd* dramatically narrowed sui generis protection through a critical distinction between investment in creating data versus investment in obtaining existing data.[^91] The Court held that "the resources used to seek out existing independent materials and collect them in the database" qualifies as protected investment, but "not the resources used for the creation of materials which make up the contents of a database."[^92] British Horseracing Board invested £4 million annually in creating horse racing data – determining race dates, creating lists of runners and riders – but the Court ruled this was investment in creating data, not obtaining data, and therefore did not qualify for sui generis protection.[^93]

[^91]: Case C-203/02 *British Horseracing Board Ltd v William Hill Organization Ltd* EU:C:2004:695.

[^92]: ibid para 31.

[^93]: ibid paras 33–34.

This distinction creates a fundamental obstacle for prompt collections. Most prompt engineering involves creating new prompts through iterative testing, trial-and-error refinement, and development of effective formulations. This is investment in creation, not obtaining. Under *British Horseracing Board*, such creative investment does not qualify for sui generis protection. The labour of developing effective prompts, testing variations, and optimizing formulations – the primary source of value in prompt libraries – constitutes creation of data rather than obtaining existing data.

Two narrow exceptions might provide sui generis protection. First, investment in "verification" or "presentation" of contents qualifies even where obtaining investment is absent.[^94] If a prompt library maker invests substantially in systematically testing prompts across multiple AI systems, quality control verification, effectiveness validation, and reliability assurance, this verification activity could constitute protected investment. Second, investment in sophisticated presentation systems – advanced search and categorization frameworks, metadata systems, recommendation algorithms, or technical interfaces requiring substantial resources – might qualify as presentation investment.[^95]

[^94]: Database Directive (n 2) art 7(1).

[^95]: Thomas Aplin and Jennifer Davis, *Intellectual Property Law: Text, Cases, and Materials* (4th edn, Oxford University Press 2020) 374–377.

The practical conclusion for prompt collections is nuanced. Collections where investment primarily focuses on creating original prompts receive no sui generis protection under current CJEU interpretation. However, collections where substantial documented investment has been made in systematically collecting prompts created by third parties, in rigorous verification and testing protocols, or in sophisticated presentation systems might qualify. The burden rests on the database maker to prove substantial investment in obtaining, verification, or presentation specifically – not merely in creation.

This creates an asymmetry: the most valuable prompt collections, developed through intensive creative engineering and testing to discover effective formulations, receive no sui generis protection because that investment constitutes creation. Less creative collections that aggregate existing prompts from external sources might receive protection. This outcome highlights tensions in the Database Directive's implementation that seem poorly suited to knowledge-intensive industries where creation and curation merge.
