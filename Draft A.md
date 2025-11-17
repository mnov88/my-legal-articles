## III. Copyright and software protection: instructions excluded as functional subject matter

Having established that prompts possess economic value but lack characteristics typical of high-value intellectual property, the analysis turns to whether EU legal frameworks accommodate prompt protection. This Part examines copyright protection under the InfoSoc Directive and software protection under Directive 2009/24/EC together, demonstrating that both fail for fundamentally similar reasons—prompts constitute functional instructions explicitly excluded from protection under the idea-expression dichotomy that structures EU intellectual property law. The analysis proceeds in four stages: first, establishing the harmonized originality standard applicable across all copyright subject matter; second, applying that standard to prompts and demonstrating that prompts constitute ideas rather than expression; third, showing that software protection fails because prompts are not programs but rather interfaces to programs; fourth, addressing database sui generis protection as a narrow exception applicable only to collections with substantial documented verification investment.

### The harmonized originality test: author's own intellectual creation

EU copyright law has converged on a unified originality standard applicable to all categories of works. Article 1(3) of Directive 2009/24/EC provides that "a computer program shall be protected if it is original in the sense that it is the author's own intellectual creation. No other criteria shall be applied to determine its eligibility for protection."[^23] The Court of Justice extended this standard beyond software to all copyrightable subject matter in *Infopaq International v Danske Dagblades Forening*, holding at paragraph 37 that "copyright within the meaning of Article 2(a) of Directive 2001/29 is liable to apply only in relation to a subject-matter which is original in the sense that it is its author's own intellectual creation."[^24] This is the harmonized test—no regional variations, no lower thresholds, no alternative standards.

[^23]: Directive 2009/24/EC of the European Parliament and of the Council of 23 April 2009 on the legal protection of computer programs [2009] OJ L111/16, art 1(3).

[^24]: Case C-5/08 Infopaq International v Danske Dagblades Forening EU:C:2009:465, para 37.

The Court has articulated this standard through several cumulative requirements. First, the work must reflect the author's personality—as stated in *Painer v Standard Verlags* at paragraph 88, "an intellectual creation is an author's own if it reflects the author's personality."[^25] Second, the author must have exercised free and creative choices; the *Painer* judgment continues at paragraph 89 that this occurs "if the author was able to express his creative abilities in the production of the work by making free and creative choices."[^26] Third, where technical considerations, rules, or constraints dictate expression, originality cannot be found—the Court held in *Brompton Bicycle v Chedech* at paragraph 24 that "where the realisation of a subject matter has been dictated by technical considerations, rules or other constraints which have left no room for creative freedom, that subject matter cannot be regarded as being original."[^27] Fourth, only expression receives protection, never ideas or principles—Article 1(2) of the Software Directive provides explicitly that "ideas and principles which underlie any element of a computer program, including those which underlie its interfaces, are not protected by copyright under this Directive."[^28] These requirements are cumulative; failure on any single element defeats protection.

[^25]: Case C-145/10 Painer v Standard Verlags EU:C:2011:798, para 88.

[^26]: ibid para 89.

[^27]: Case C-833/18 Brompton Bicycle v Chedech EU:C:2020:461, para 24.

[^28]: Software Directive (n 23) art 1(2).

The Court consolidated these principles in *Cofemel v G-Star Raw*, confirming at paragraph 29 that "a subject matter can be classified as a 'work' within the meaning of Directive 2001/29 only if it is an original subject matter in that it is the author's own intellectual creation."[^29] At paragraph 30, the Court clarified that "the assessment of the originality of a subject matter is therefore primarily based on whether that subject matter reflects the personality of its author, as an expression of his or her free and creative choices."[^30] This represents a harmonized standard displacing earlier national variations in originality thresholds.

[^29]: Case C-683/17 Cofemel v G-Star Raw EU:C:2019:721, para 29.

[^30]: ibid para 30.

### Application to prompts: instructions about ideas, not expression

With the legal test established, the critical question becomes whether AI prompts satisfy these cumulative requirements. The answer is no. The analysis reveals three insurmountable obstacles that apply regardless of prompt complexity.

First, prompts are instructions about what to create, not the expression itself. This implicates the core idea-expression dichotomy. Consider a prompt stating "create an impressionist-style painting of the Eiffel Tower at sunset, with warm orange and pink tones, soft brushstrokes suggesting movement, positioned at right third of composition following rule of thirds." This is elaborate—but it remains an instruction specifying the idea of what the AI should generate. The resulting AI-generated image would be the expression, if it qualifies as expression at all. Protecting the prompt would grant rights over the idea or concept described. The Court has been emphatic: ideas, including those underlying interfaces and interaction methods, receive no copyright protection.[^31]

[^31]: Case C-393/09 BSA v Ministerstvo kultury EU:C:2010:816, para 49.

The relevant parallel is to functional specifications in other domains. French courts have consistently held that cooking recipes constitute "succession of instructions, a method" belonging to the category of unprotectable know-how rather than intellectual works—copyright may protect creative literary description accompanying recipes, but not the functional list of ingredients or procedural steps.[^32] In *Levola Hengelo v Smilde Foods*, Advocate General Wathelet emphasized that "copyright does not protect the recipe as such (the idea)" because "copyright protection extends to original expressions and not to ideas, procedures, methods of operation."[^33] Similarly, abstract rules of a game constitute unprotectable methods and procedures, though the creative literary expression of those rules in a rulebook may be protected.[^34] Operating instructions present the same pattern—simple manuals constitute unprotectable procedures, with copyright attaching only to substantial creative expression in the arrangement or explanation of functional information.[^35] The pattern is consistent across functional domains.

[^32]: Cour de Cassation [1974] Bulletin civil IV n° 267.

[^33]: Case C-310/17 Levola Hengelo v Smilde Foods EU:C:2018:899 (Opinion of AG Wathelet) para 40.

[^34]: P.B. Hugenholtz and others, 'The Recasting of Copyright & Related Rights for the Knowledge Economy' (Institute for Information Law, 2006) 33–34.

[^35]: Bundesgerichtshof [1993] GRUR 34 (Bedienungsanleitung).

Prompts bear the same relationship to AI systems that recipes bear to cooking, game rules bear to gameplay, and operating instructions bear to equipment use. They describe what should be done, what functions should be performed, what constraints should be observed. The fact that prompts are written in natural language rather than formal notation does not alter their functional character—they remain instructions about methods and procedures of operation rather than literary expressions for their own sake. To that extent, prompts fall squarely within the category of functional instructions that copyright doctrine deliberately excludes.

Second, prompts are functionally dictated by their purpose: communicating instructions to AI systems. The *BSA* principle that "where the expression of those components is dictated by their technical function, the criterion of originality is not met" applies with particular force.[^36] A prompt's purpose is to effectively communicate with an AI model to achieve a desired output. This functional purpose constrains expression significantly. While some word choice flexibility exists, the prompt must use language the AI model will process effectively. It must specify parameters in ways the system recognizes. It must structure instructions for optimal results. These technical constraints reduce the space for free and creative choices.

[^36]: *BSA* (n 31) para 50.

Many prompt elements—parameter specifications, formatting conventions, strategic keyword placement—are dictated by AI model requirements rather than creative choice. The prompt engineer learns, through experimentation, which phrasings produce desired effects. That learning reflects skill and investment, but not necessarily the free creative choices reflecting personality that *Painer* and *Cofemel* require.[^37] The Court's *Football Dataco* precedent is dispositive: "the fact that the setting up of the database required...significant labour and skill of its author...cannot as such justify the protection of it by copyright" where "that labour and that skill do not express any originality in the selection or arrangement."[^38] Skill is not originality; investment is not creativity.

[^37]: *Painer* (n 25) para 89; *Cofemel* (n 29) para 30.

[^38]: Case C-604/10 Football Dataco v Yahoo! UK EU:C:2012:115, para 42.

Third, prompts raise merger concerns where limited ways exist to express particular instructions. When there are only a few ways to convey a specific instruction to an AI system, the expression merges with the idea, and copyright protection must be denied to prevent monopolization of the idea itself. Instructing an AI to "make the image brighter" or "write in a professional tone" or "use active voice" can be expressed in only limited ways that effectively communicate with AI systems. Protecting any of these formulations would effectively monopolize the underlying instruction itself. European copyright doctrine recognizes this principle through the *BSA* holding that where methods of implementing an idea are so limited that idea and expression become indissociable, no protection attaches.[^39] Even for more elaborate prompts, the specifications respond to functional requirements—specifying "formal tone" rather than "casual tone," requesting "Chicago citation style" rather than "MLA citation style," or setting "temperature at 0.3" rather than "temperature at 0.7" reflects optimization choices dictated by desired output characteristics, not creative expressions reflecting the author's personality. These are functional decisions, not creative choices.

[^39]: *BSA* (n 31) para 50.

By elimination, prompts *qua* prompts—textual instructions provided to AI systems to generate desired outputs—do not meet the EU originality standard for copyright protection. The fundamental obstacles are insurmountable: prompts are instructions describing ideas about what to create rather than creative expression itself; they are functionally constrained by their communicative purpose; and protecting them would risk monopolizing ideas in violation of core copyright principles.

### Software protection: prompts as interfaces, not programs

Having established that prompts fail the originality standard as literary works under the InfoSoc Directive, a second pathway presents itself: protection as computer programs or preparatory design material under the Software Directive. This theory posits that prompts—particularly system prompts that configure AI behavior—function as specifications or instructions to computational systems and might therefore qualify under the Software Directive's framework. The answer is negative. The Court's restrictive interpretation of software protection scope renders this pathway equally unavailing; prompts are interfaces to programs, not programs themselves, and fall squarely within the express exclusion in Article 1(2).

The Software Directive provides in Article 1(1) that "Member States shall protect computer programs, by copyright, as literary works within the meaning of the Berne Convention. For the purposes of this Directive, the term 'computer programs' shall include their preparatory design material."[^40] Recital 7 elaborates that "the term 'computer program' shall include programs in any form, including those which are incorporated into hardware. This term also includes preparatory design work leading to the development of a computer program provided that the nature of the preparatory work is such that a computer program can result from it at a later stage."[^41]

[^40]: Software Directive (n 23) art 1(1).

[^41]: ibid recital 7.

The Court has interpreted this scope through three key decisions that prove dispositive. In *BSA v Ministerstvo kultury*, the Court held at paragraph 45 that graphical user interfaces "do not enable the reproduction of the computer program, but merely constitute one element of that program by way of which users make use of its features."[^42] Only the actual source code or object code constituting the program's expression receives protection; user-facing elements through which individuals interact with programs fall outside the Software Directive's scope. In *SAS Institute Inc v World Programming Ltd*, the Court held at paragraph 39 that "the functionality of a computer program, the programming language and the format of data files used in a computer program do not constitute a form of expression of that program and, as such, are not protected by copyright in computer programs."[^43] The Court emphasized at paragraph 40 that "to accept that the functionality of a computer program can be protected by copyright would amount to making it possible to monopolise ideas, to the detriment of technological progress and industrial development."[^44] Most recently, in *Sony Computer Entertainment Europe Ltd v Datel Design & Development Ltd*, the Court clarified that even the content of variables stored in RAM during program execution does not constitute an expression of the computer program subject to copyright protection.[^45]

[^42]: *BSA* (n 31) para 45.

[^43]: Case C-406/10 SAS Institute v World Programming EU:C:2012:259, para 39.

[^44]: ibid para 40.

[^45]: Case C-159/23 Sony Computer Entertainment Europe v Datel Design & Development EU:C:2024:649, paras 33–35.

Critically, Article 1(2) of the Software Directive establishes an express exclusion: "Ideas and principles which underlie any element of a computer program, including those which underlie its interfaces, are not protected by copyright under this Directive."[^46] Recital 11 reinforces this: "only the expression of a computer program is protected and...ideas and principles which underlie any element of a program, including those which underlie its interfaces, are not protected by copyright."[^47]

[^46]: Software Directive (n 23) art 1(2).

[^47]: ibid recital 11.

Applying this case law to prompts reveals that prompts do not qualify as "computer programs" under the Software Directive. Three barriers prove insurmountable. First, prompts are textual instructions provided as input to existing AI programs—they are not themselves source code or object code. They do not define the computational processes executed by the system. The AI model's trained weights, neural network architecture, and inference algorithms perform the actual computation. Prompts direct how those existing computational processes should be applied to particular tasks, but they do not constitute the code implementing those processes. Under the *BSA* principle that GUIs are not protected because they "merely constitute one element of that program by way of which users make use of its features," prompts likewise merely enable users to direct how existing AI programs should operate.[^48] Simply put: prompts are instructions *to* programs, not programs themselves.

[^48]: *BSA* (n 31) para 45.

Second, prompts function as interfaces—explicitly excluded from protection under Article 1(2). An interface is the boundary across which users communicate with computational systems. Natural language prompts constitute an interface type—the mechanism by which users communicate instructions to AI systems in natural language rather than formal syntax. If visual GUIs through which users interact with software are not protected as program expressions, textual prompts through which users interact with AI systems fall under the same exclusion. The *BSA* Court's reasoning applies directly: prompts "do not enable the reproduction of the computer program, but merely constitute one element...by way of which users make use of its features."[^49]

[^49]: ibid para 45.

Third, under the *SAS Institute* precedent, prompts describe functionality rather than constituting program expression. If formal programming languages—Python syntax, SQL query structures, JavaScript conventions—are unprotectable ideas and principles under Article 1(2) and *SAS Institute*, then natural language prompts are equally unprotectable.[^50] Both are methods for instructing computational systems. Both specify desired operations. A Python command `print("Hello, world")` and a prompt "Write 'Hello, world'" are functionally equivalent—both instruct a computational system to produce output. The natural language formulation does not transform the instruction into protectable program expression any more than translating a programming command into English would make the command copyrightable.

[^50]: *SAS Institute* (n 43) paras 39–40.

Prompts also fail to qualify as preparatory design material. Recital 7 protects "preparatory design work leading to the development of a computer program provided that the nature of the preparatory work is such that a computer program can result from it at a later stage."[^51] Traditional preparatory design work—flow charts, technical specifications, architecture diagrams—defines how computational processes should be structured such that programmers can implement them deterministically. Prompts operate differently. A prompt given to an AI system does not generate program code—it generates outputs like text or images. The AI model itself already exists as a complete program. Moreover, the same prompt provided to the same AI model produces varying outputs across invocations due to probabilistic inference. As Sampaio notes, "the same prompt to the same model will not deliver the same results."[^52] This lack of determinism fundamentally distinguishes prompts from preparatory design work, which must be sufficiently precise to enable consistent program implementation.

[^51]: Software Directive (n 23) recital 7.

[^52]: A. Sampaio, 'Are Prompts Copyrightable?' (Kluwer Copyright Blog, 14 June 2023) <http://copyrightblog.kluweriplaw.com/2023/06/14/are-prompts-copyrightable> accessed 15 October 2024.

By elimination, prompts do not qualify for protection as computer programs or preparatory design material under the Software Directive. They are instructions *to* programs, not programs themselves. They function as interfaces explicitly excluded from protection under Article 1(2). They describe desired functionality rather than implementing it through code. To that extent, the Software Directive provides no basis for prompt protection—and this failure reinforces the copyright conclusion. Both frameworks exclude prompts for the same fundamental reason: prompts are functional instructions explicitly placed outside intellectual property protection under the idea-expression dichotomy. The pattern holds.

### Database sui generis protection: the verification investment exception

A narrow exception merits consideration. Directive 96/9/EC establishes sui generis protection for databases where the maker demonstrates "substantial investment in either the obtaining, verification or presentation of the contents."[^53] This protection operates independently of copyright, focusing on investment rather than originality. To that extent, it potentially accommodates prompt collections even where individual prompts lack originality.

[^53]: Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases [1996] OJ L77/20, art 7(1).

However, the Court's interpretation in *British Horseracing Board v William Hill* substantially narrows the scope. The Court held that investment in creating data does not qualify—only investment in obtaining existing data, verifying its accuracy or currency, or presenting it in a structured format receives protection.[^54] At paragraph 31, the Court stated that "the purpose of the protection...is to promote the establishment of storage and processing systems for existing information and not the creation of materials capable of being collected subsequently in a database."[^55] This distinction between creation and obtaining investment creates a perverse outcome: investment in engineering original prompts through testing and optimization receives no protection, while investment in verifying or presenting others' prompts might qualify.[^56] The creator goes unprotected; the compiler may be rewarded.

[^54]: Case C-203/02 British Horseracing Board v William Hill EU:C:2004:695, para 31.

[^55]: ibid.

[^56]: See *Fixtures Marketing Ltd v Oy Veikkaus Ab* (Case C-46/02) EU:C:2004:694, para 34 (applying same distinction).

Applied to prompts, database protection might apply to a curated collection if the collector demonstrates substantial documented investment in: systematic testing and verification of prompt effectiveness across multiple AI systems; quality assurance and reliability validation with documented metrics; and sophisticated presentation with search, categorization, and access systems. Protection would extend only to preventing extraction and reutilization of substantial portions of the collection, not to preventing independent creation or use of individual prompts. The term is fifteen years from completion.[^57] The scope is narrow.

[^57]: Database Directive (n 53) art 10(1).

This pathway remains narrow and creates perverse incentives—it rewards aggregation over innovation, protecting compilation investment while leaving creative development unprotected. Moreover, the substantial investment threshold requires documented proof. German courts applying corresponding national law have required claimants to quantify investment and demonstrate that extraction would unfairly benefit from that investment.[^58] Most businesses developing prompt libraries focus investment on prompt creation rather than verification of existing prompts, placing them outside the *BHB* framework. To that extent, database protection offers little practical value for prompt developers.

[^58]: See generally M. Leistner, 'The Protection of Databases' in A. Ohly (ed), *Common Principles of European Intellectual Property Law* (Mohr Siebeck 2012) 139–158.

### Scholarly consensus

Academic commentary on prompt copyrightability has converged on the conclusion that prompts likely fail the originality threshold under EU law. Professor He, writing in *GRUR International*, argues that "judicial recognition of text-to-image copyrightability at the current stage is dangerous" because "the practice is not in accordance with our traditional understanding of originality."[^59] He emphasizes that prompts constitute "merely unprotectable ideas" rather than expressions.[^60] Professors Gervais and Hugenholtz identify the critical problem: "The hard question is whether those creative choices—the originality, if any—of the prompt is 'transferable' into the product or output of the AI machine. This gets dangerously close to owning the underlying idea, and thus goes against a fundamental principle of international copyright law."[^61] They conclude that "if the originality of the instructions is not sufficiently reflected in the machine's product, there is no protected work in the output. That should be the default position."[^62] Professor Quintais and Professor Hugenholtz argue that current EU copyright rules are "generally suitable and sufficiently flexible to deal with the challenges posed by AI-assisted output" when properly applied, emphasizing that where subject matter has been dictated by technical considerations leaving no room for creative freedom, originality cannot be found.[^63]

[^59]: X. He, 'Human Authorship and AI-Generated Works: A Chinese Perspective' (2024) 55 IIC 321, 335.

[^60]: ibid 336.

[^61]: D. Gervais and P.B. Hugenholtz, 'The AI-nundrum: Machines, Learning and Intellectual Property' (Kluwer Copyright Blog, 18 July 2023) <http://copyrightblog.kluweriplaw.com/2023/07/18/the-ai-nundrum-machines-learning-and-intellectual-property> accessed 15 October 2024.

[^62]: ibid.

[^63]: J.P. Quintais and P.B. Hugenholtz, 'The New Copyright Directive: A Complete (EU) Copyright Codification?' (2020) 51 IIC 28, 45–47.

### The unified conclusion

The pattern is clear across copyright and software frameworks: EU law systematically excludes functional instructions from intellectual property protection. Prompts fail copyright because they constitute ideas about what to create rather than creative expression—they are instructions describing desired outputs, not literary works reflecting the author's personality through free and creative choices. Prompts fail software protection because they are interfaces through which users communicate with programs, not programs themselves—they are explicitly excluded under Article 1(2)'s provision that ideas and principles underlying interfaces receive no copyright protection. Database protection might apply to collections with documented verification investment, but this narrow exception rewards aggregation while leaving creative development unprotected. The exception does not change the rule.

To that extent, copyright and software protection fail for the same fundamental reason: prompts are quintessential examples of functional instructions that the idea-expression dichotomy deliberately places outside intellectual property protection. This is not an oversight or gap in the law—it reflects a deliberate policy choice to preserve the public domain of methods, procedures, and building blocks necessary for competition and cumulative innovation. The analysis now turns to patent protection, which similarly excludes prompts—though for distinct reasons grounded in the technical character requirement rather than the idea-expression dichotomy. Different framework, same result.
