# V. Patent Protection

## A. Patentability Requirements under the European Patent Convention

Patent protection for prompts requires analysis under the European Patent Convention rather than EU directives, as patent law remains governed by the EPC – an international treaty to which all EU Member States are parties – rather than harmonized EU legislation.[^96]

[^96]: Convention on the Grant of European Patents (adopted 5 October 1973, entered into force 7 October 1977, as amended) 1065 UNTS 199 ('EPC').

Article 52(1) EPC establishes the foundational requirement: "European patents shall be granted for any inventions, in all fields of technology, provided that they are new, involve an inventive step and are susceptible of industrial application."[^97] However, Article 52(2) excludes specific categories from patentability, stating that "the following in particular shall not be regarded as inventions": "(a) discoveries, scientific theories and mathematical methods; (b) aesthetic creations; (c) schemes, rules and methods for performing mental acts, playing games or doing business, and programs for computers; (d) presentations of information."[^98]

[^97]: ibid art 52(1).

[^98]: ibid art 52(2).

The qualification in Article 52(3) proves critical: "Paragraph 2 shall exclude the patentability of the subject-matter or activities referred to therein only to the extent to which a European patent application or European patent relates to such subject-matter or activities as such."[^99] This "as such" limitation has driven EPO practice toward allowing patents for computer-implemented inventions that provide technical effects beyond the excluded subject matter itself.

[^99]: ibid art 52(3).

EPO jurisprudence has developed the "technical character" requirement as the threshold for patent eligibility. The landmark Board of Appeal decision in *Computer Program Product/IBM* established that a computer program is not excluded from patentability if "when it is run on a computer, it produces a further technical effect which goes beyond the 'normal' physical interactions between program (software) and computer (hardware)."[^100] Examples of sufficient technical effects include controlling anti-lock braking systems, managing processor load balancing, optimizing memory allocation, and improving digital image processing.[^101]

[^100]: EPO Board of Appeal, T 1173/97 *Computer Program Product/IBM* [1999] OJ EPO 609, para 13.

[^101]: ibid.

The Enlarged Board of Appeal in *Programs for Computers* clarified that technical character requires providing "technical teaching" – instruction on how to solve a technical problem using technical means.[^102] The *Two Identities/COMVIK* decision established that non-technical features making no contribution to technical character cannot support inventive step; they are treated as constraints in formulating the objective technical problem.[^103]

[^102]: EPO Enlarged Board of Appeal, G 3/08 *Programs for Computers* [2011] OJ EPO 10, para 10.4.

[^103]: EPO Board of Appeal, T 641/00 *Two Identities/COMVIK* [2003] OJ EPO 352.

## B. Application to Prompts: Absence of Technical Character

Prompts fail patent protection for three fundamental reasons.

First, prompts constitute excluded subject matter under Article 52(2) EPC. They fall within multiple exclusions simultaneously: methods for performing mental acts (linguistic formulation is cognitive activity), presentations of information (prompts structure how information is requested), and programs for computers as such (prompts direct AI operation through textual instructions).[^104] The natural language formulation does not disguise their essentially excluded character – they remain linguistic constructs communicating intent rather than technical implementations.

[^104]: Martin J Adelman and others, *Cases and Materials on Patent Law* (5th edn, West Academic Publishing 2021) 127–132.

Second, prompts lack technical character within the meaning of EPO jurisprudence. The EPO requires "technical teaching" on how to solve a technical problem using technical means. Prompts do not provide such teaching – they specify what outputs are desired, not how to achieve them technically. The prompt does not control hardware, does not improve computer functioning, and does not process technical data in a technical manner. The AI model processes the prompt using its existing trained weights and algorithms, but the model is separate from the prompt. The prompt is input data, not a technical implementation.

The distinction proves dispositive. A technical problem must relate to a technical field and be solved by technical means producing technical effects. Prompt engineering addresses linguistic and cognitive problems: how to formulate instructions to improve AI output quality, relevance, format, or style. These are content quality issues, not technical problems in the EPO sense. As the Board of Appeal held in *Hitachi*, "an invention which would be obvious to a person skilled in the art using common general knowledge cannot be considered to involve an inventive step merely because a technical effect results when the invention is carried out in a computer."[^105]

[^105]: EPO Board of Appeal, T 0258/03 *Hitachi* [2004] OJ EPO 575, para 5.7.

Third, under the COMVIK approach, prompt innovations would be treated as non-technical constraints. Even if one claims "a computer-implemented method using prompts," the novelty and inventiveness resides in the prompt formulation – linguistic and cognitive choices – not in technical implementation. These non-technical features contribute nothing to inventive step. The technical problem reduces to "implement this linguistic requirement on a computer," which would be obvious to a competent computer scientist. The skilled person, defined as a computer scientist or AI engineer rather than a linguist, would find this obvious.

The parallel to business methods proves instructive. In *Pension Benefit Systems Partnership*, the Board of Appeal held that "features which do not contribute to the technical character of an invention cannot support the presence of an inventive step."[^106] Business method innovations, no matter how clever, cannot render obvious technical implementations non-obvious. Similarly, linguistic innovations in prompt formulation, no matter how sophisticated, cannot render obvious computer processing non-obvious.

[^106]: EPO Board of Appeal, T 0931/95 *Pension Benefit Systems Partnership* [2001] OJ EPO 441, para 6.

## C. Conclusion: Patents as an Unavailable Protection Mechanism

The conclusion is unequivocal: AI prompts cannot receive patent protection under current EPO practice. They constitute excluded subject matter as methods for performing mental acts, presentations of information, and computer programs as such. They lack technical character because they address linguistic and cognitive problems rather than technical problems. They fail to provide technical teaching on how to solve technical problems using technical means. Under the COMVIK approach, their innovative aspects are non-technical features that cannot support inventive step.

Academic commentary confirms this assessment. Professor Andres Guadamuz observes that prompts "are essentially instructions to the AI, much like a search query is an instruction to a search engine" and that "it would be difficult to argue that such instructions possess the technical character necessary for patent protection."[^107] Professor Daniel Gervais notes that "patent protection requires a technical contribution, which prompts – being linguistic formulations – do not provide."[^108]

[^107]: Andres Guadamuz, 'The Monkey Selfie: Copyright Lessons for Originality in Photographs and AI Works' (2018) 5 Internet Policy Review 1, 13.

[^108]: Daniel Gervais, 'Is Intellectual Property Law Ready for Artificial Intelligence?' (2020) 9 GRUR International 117, 123.

Patent law's technical character requirement, appropriate for its purpose of protecting technological innovation, means patents cannot accommodate linguistic or cognitive innovations like prompts regardless of their commercial value. The analysis must therefore turn to trade secrets as the potentially viable protection mechanism for commercially valuable prompts.
