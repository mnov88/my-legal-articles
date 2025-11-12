# Definitive Proof of AI Model Performance Degradation Over Time

Yes, there is definitive, quantifiable proof that AI generative and large language model outputs degrade over time, even from major providers. Multiple comprehensive studies have documented this phenomenon across different model types and provide specific metrics demonstrating performance decline.

## Documented Evidence from Stanford/Berkeley ChatGPT Study

The most significant evidence comes from a landmark study by researchers at Stanford University and UC Berkeley published in 2023. This research tracked the performance of GPT-4 and GPT-3.5 between March 2023 and June 2023, revealing dramatic degradation in just three months:[hdsr.mitpress.mit+1](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​

**GPT-4 Performance Drops:**

- **Prime number identification accuracy**: Plummeted from 97.6% in March 2023 to 2.4% in June 2023[tomshardware+2](https://www.tomshardware.com/news/chatgpt-response-quality-decline)​
    
- **Math problem solving**: Accuracy fell from 84.0% to 51.1% on prime vs. composite number tasks[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​
    
- **Happy number counting**: Performance dropped from 83.6% to 35.2%[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​
    
- **Code generation**: Directly executable code fell from over 52% to just 10%[reddit+1](https://www.reddit.com/r/ArtificialInteligence/comments/153iqbq/new_study_confirms_user_rumors_huge_drop_in/)​
    
- **Instruction following**: Answer extraction compliance dropped from 99.5% to 0.5%[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​
    

**Chain-of-thought prompting effectiveness**: The study found that GPT-4's ability to follow step-by-step reasoning instructions degraded significantly. In March, chain-of-thought prompting improved accuracy by 24.4%, but by June this improvement dropped to -0.1%.[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​

## Broader AI Model Degradation Statistics

Beyond the ChatGPT-specific findings, a comprehensive study published in Nature involving researchers from Harvard, MIT, and Cambridge provides broader evidence:[pmc.ncbi.nlm.nih+2](https://pmc.ncbi.nlm.nih.gov/articles/PMC9270447/)​

- **91% of machine learning models degrade over time** after deployment[fiddler+2](https://www.fiddler.ai/blog/91-percent-of-ml-models-degrade-over-time)​
    
- The study analyzed 32 datasets across four industries using four standard model types
    
- Degradation occurred even when underlying data showed minimal concept drift[nature](https://www.nature.com/articles/s41598-022-15245-z)​
    
- Models showed various degradation patterns including gradual decline, explosive failure, and increased error variability[nature](https://www.nature.com/articles/s41598-022-15245-z)​
    

## Model Collapse from Synthetic Data Training

Research published in Nature in 2024 demonstrates that training AI models on AI-generated data leads to "model collapse":[nature+2](https://www.nature.com/articles/s41586-024-07566-y)​

- Models trained recursively on synthetic data show progressive performance degradation[wikipedia+1](https://en.wikipedia.org/wiki/Model_collapse)​
    
- This creates a feedback loop where errors compound across generations[projectpro+1](https://www.projectpro.io/article/ai-model-collapse/1177)​
    
- The phenomenon affects both the quality and diversity of outputs[towardsdatascience+1](https://towardsdatascience.com/can-generative-ai-lead-to-ai-collapse-481966259d23/)​
    
- Even small amounts of synthetic data (as little as 1%) can trigger collapse[arxiv](http://arxiv.org/pdf/2410.04840.pdf)​
    

## Quantifiable Impacts and Measurements

The degradation is measurable across multiple dimensions:

**Response Quality Changes:**

- GPT-4 became significantly less verbose (response length dropped by over 90% in some tasks)[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​
    
- Models showed increased formatting errors and reduced adherence to instructions[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​
    
- Safety responses became more conservative but less explanatory[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​
    

**Task-Specific Performance:**

- Medical exam performance: GPT-4 accuracy dropped from 86.6% to 82.4% on USMLE tests[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​
    
- Opinion survey response rates: GPT-4 willingness to answer dropped from 97.6% to 22.1%[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​
    
- Code quality: While underlying code logic sometimes improved, formatting compliance deteriorated[hdsr.mitpress.mit](https://hdsr.mitpress.mit.edu/pub/y95zitmz)​
    

## Industry Recognition and Response

The degradation phenomenon has gained recognition across the AI industry:

- OpenAI has faced user complaints about declining ChatGPT quality[businessinsider+1](https://www.businessinsider.com/openai-gpt4-ai-model-got-lazier-dumber-chatgpt-2023-7)​
    
- Multiple AI companies report similar challenges with model drift[314e+1](https://www.314e.com/engineering-hub/why-is-my-ai-model-s-performance-degrading-how-to-solve-model-drift/)​
    
- Enterprise users increasingly implement monitoring systems to detect performance degradation[drpinnacle+1](https://www.drpinnacle.com/post/ai-model-degradation)​
    

## Temporal vs. Data-Driven Degradation

Importantly, research distinguishes between degradation caused by changing data (concept drift) and temporal degradation that occurs even with stable data:[aigl+1](https://www.aigl.blog/temporal-quality-degradation-in-ai-models/)​

- **AI aging**: Models degrade relative to their training time regardless of when training occurred[nature](https://www.nature.com/articles/s41598-022-15245-z)​
    
- **Temporal sensitivity**: Performance can decline even when data patterns remain consistent[nature](https://www.nature.com/articles/s41598-022-15245-z)​
    
- **Model-specific patterns**: Different algorithms show varying susceptibility to temporal degradation[nature](https://www.nature.com/articles/s41598-022-15245-z)​
    

The evidence conclusively demonstrates that AI model performance degradation over time is not just anecdotal but a measurable, quantifiable phenomenon affecting the majority of deployed models. This degradation occurs across different model types, providers, and applications, making continuous monitoring and periodic retraining essential for maintaining AI system reliability.

1. [https://hdsr.mitpress.mit.edu/pub/y95zitmz](https://hdsr.mitpress.mit.edu/pub/y95zitmz)
2. [https://arxiv.org/abs/2307.09009](https://arxiv.org/abs/2307.09009)
3. [https://www.tomshardware.com/news/chatgpt-response-quality-decline](https://www.tomshardware.com/news/chatgpt-response-quality-decline)
4. [https://promptengineering.org/the-gpt-4-controversy-a-deep-dive-into-model-performance-and-openais-policy/](https://promptengineering.org/the-gpt-4-controversy-a-deep-dive-into-model-performance-and-openais-policy/)
5. [https://www.reddit.com/r/ArtificialInteligence/comments/153iqbq/new_study_confirms_user_rumors_huge_drop_in/](https://www.reddit.com/r/ArtificialInteligence/comments/153iqbq/new_study_confirms_user_rumors_huge_drop_in/)
6. [https://pmc.ncbi.nlm.nih.gov/articles/PMC9270447/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9270447/)
7. [https://www.fiddler.ai/blog/91-percent-of-ml-models-degrade-over-time](https://www.fiddler.ai/blog/91-percent-of-ml-models-degrade-over-time)
8. [https://www.nature.com/articles/s41598-022-15245-z](https://www.nature.com/articles/s41598-022-15245-z)
9. [https://www.linkedin.com/posts/hakimelakhrass_91-of-ml-models-degrade-in-time-a-nature-activity-7298315717924290561-dSaZ](https://www.linkedin.com/posts/hakimelakhrass_91-of-ml-models-degrade-in-time-a-nature-activity-7298315717924290561-dSaZ)
10. [https://www.drpinnacle.com/post/ai-model-degradation](https://www.drpinnacle.com/post/ai-model-degradation)
11. [https://www.nature.com/articles/s41586-024-07566-y](https://www.nature.com/articles/s41586-024-07566-y)
12. [https://en.wikipedia.org/wiki/Model_collapse](https://en.wikipedia.org/wiki/Model_collapse)
13. [https://www.cs.ox.ac.uk/news/2356-full.html](https://www.cs.ox.ac.uk/news/2356-full.html)
14. [https://www.ibm.com/think/topics/model-collapse](https://www.ibm.com/think/topics/model-collapse)
15. [https://www.projectpro.io/article/ai-model-collapse/1177](https://www.projectpro.io/article/ai-model-collapse/1177)
16. [https://www.datacamp.com/blog/what-is-model-collapse](https://www.datacamp.com/blog/what-is-model-collapse)
17. [https://towardsdatascience.com/can-generative-ai-lead-to-ai-collapse-481966259d23/](https://towardsdatascience.com/can-generative-ai-lead-to-ai-collapse-481966259d23/)
18. [http://arxiv.org/pdf/2410.04840.pdf](http://arxiv.org/pdf/2410.04840.pdf)
19. [https://www.businessinsider.com/openai-gpt4-ai-model-got-lazier-dumber-chatgpt-2023-7](https://www.businessinsider.com/openai-gpt4-ai-model-got-lazier-dumber-chatgpt-2023-7)
20. [https://community.openai.com/t/declining-quality-of-openai-models-over-time-a-concerning-trend/847753](https://community.openai.com/t/declining-quality-of-openai-models-over-time-a-concerning-trend/847753)
21. [https://www.314e.com/engineering-hub/why-is-my-ai-model-s-performance-degrading-how-to-solve-model-drift/](https://www.314e.com/engineering-hub/why-is-my-ai-model-s-performance-degrading-how-to-solve-model-drift/)
22. [https://www.techbrew.com/stories/2025/02/06/why-ai-models-might-degrade-over-time](https://www.techbrew.com/stories/2025/02/06/why-ai-models-might-degrade-over-time)
23. [https://www.fiddler.ai/ml-model-monitoring-best-practices/how-do-i-monitor-model-degradation](https://www.fiddler.ai/ml-model-monitoring-best-practices/how-do-i-monitor-model-degradation)
24. [https://www.aigl.blog/temporal-quality-degradation-in-ai-models/](https://www.aigl.blog/temporal-quality-degradation-in-ai-models/)
25. [https://ieeexplore.ieee.org/document/10608150/](https://ieeexplore.ieee.org/document/10608150/)
26. [https://ieeexplore.ieee.org/document/10978540/](https://ieeexplore.ieee.org/document/10978540/)
27. [https://arxiv.org/abs/2506.17442](https://arxiv.org/abs/2506.17442)
28. [https://ieeexplore.ieee.org/document/11139657/](https://ieeexplore.ieee.org/document/11139657/)
29. [https://wseas.com/journals/isa/2025/a045109-001(2025).pdf](https://wseas.com/journals/isa/2025/a045109-001\(2025\).pdf)
30. [https://iopscience.iop.org/article/10.1088/2515-7655/add95e](https://iopscience.iop.org/article/10.1088/2515-7655/add95e)
31. [https://link.springer.com/10.1007/s10278-025-01493-8](https://link.springer.com/10.1007/s10278-025-01493-8)
32. [https://arxiv.org/abs/2403.02439](https://arxiv.org/abs/2403.02439)
33. [https://www.ijisrt.com/integrating-efficiency-sustainability-and-adaptability-in-ai-a-multidimensional-framework-for-cloudbased-business-intelligence](https://www.ijisrt.com/integrating-efficiency-sustainability-and-adaptability-in-ai-a-multidimensional-framework-for-cloudbased-business-intelligence)
34. [https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/slct.202501947](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/slct.202501947)
35. [https://arxiv.org/pdf/2401.14093.pdf](https://arxiv.org/pdf/2401.14093.pdf)
36. [http://arxiv.org/pdf/2404.05090.pdf](http://arxiv.org/pdf/2404.05090.pdf)
37. [http://arxiv.org/pdf/2404.01413.pdf](http://arxiv.org/pdf/2404.01413.pdf)
38. [http://arxiv.org/pdf/2503.23924v1.pdf](http://arxiv.org/pdf/2503.23924v1.pdf)
39. [https://arxiv.org/pdf/2309.15187.pdf](https://arxiv.org/pdf/2309.15187.pdf)
40. [http://arxiv.org/pdf/2405.03198.pdf](http://arxiv.org/pdf/2405.03198.pdf)
41. [https://www.reddit.com/r/singularity/comments/1eb7yru/evidence_that_training_models_on_aicreated_data/](https://www.reddit.com/r/singularity/comments/1eb7yru/evidence_that_training_models_on_aicreated_data/)
42. [https://www.sciencedirect.com/science/article/pii/S0378720625000060](https://www.sciencedirect.com/science/article/pii/S0378720625000060)
43. [https://arxiv.org/html/2501.04040v1](https://arxiv.org/html/2501.04040v1)
44. [https://www.rohan-paul.com/p/ml-interview-q-series-handling-llm](https://www.rohan-paul.com/p/ml-interview-q-series-handling-llm)
45. [https://www.byteplus.com/en/topic/549542](https://www.byteplus.com/en/topic/549542)
46. [https://research.aimultiple.com/model-drift/](https://research.aimultiple.com/model-drift/)
47. [https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf](https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf)
48. [https://www.sciencedirect.com/science/article/pii/S0950705125005490](https://www.sciencedirect.com/science/article/pii/S0950705125005490)
49. [https://www.ibm.com/think/topics/model-drift](https://www.ibm.com/think/topics/model-drift)
50. [https://arxiv.org/html/2409.07085v1](https://arxiv.org/html/2409.07085v1)
51. [https://isprs-archives.copernicus.org/articles/XLVIII-2-W8-2024/327/2024/](https://isprs-archives.copernicus.org/articles/XLVIII-2-W8-2024/327/2024/)
52. [https://dl.acm.org/doi/10.1145/3696410.3714632](https://dl.acm.org/doi/10.1145/3696410.3714632)
53. [https://mental.jmir.org/2024/1/e50150](https://mental.jmir.org/2024/1/e50150)
54. [https://www.semanticscholar.org/paper/e02a4282c10c8e7329d4513bd4635635b9d3a50a](https://www.semanticscholar.org/paper/e02a4282c10c8e7329d4513bd4635635b9d3a50a)
55. [https://ieeexplore.ieee.org/document/10629560/](https://ieeexplore.ieee.org/document/10629560/)
56. [https://ieeexplore.ieee.org/document/10907087/](https://ieeexplore.ieee.org/document/10907087/)
57. [https://www.ssrn.com/abstract=4390455](https://www.ssrn.com/abstract=4390455)
58. [https://ieeexplore.ieee.org/document/10159737/](https://ieeexplore.ieee.org/document/10159737/)
59. [https://arxiv.org/abs/2311.11695](https://arxiv.org/abs/2311.11695)
60. [https://www.mdpi.com/2504-4990/7/1/15](https://www.mdpi.com/2504-4990/7/1/15)
61. [https://arxiv.org/pdf/2304.08979.pdf](https://arxiv.org/pdf/2304.08979.pdf)
62. [https://aclanthology.org/2023.findings-acl.29.pdf](https://aclanthology.org/2023.findings-acl.29.pdf)
63. [https://www.tandfonline.com/doi/full/10.1080/2331186X.2023.2210461](https://www.tandfonline.com/doi/full/10.1080/2331186X.2023.2210461)
64. [https://hdsr.mitpress.mit.edu/pub/y95zitmz/download/pdf](https://hdsr.mitpress.mit.edu/pub/y95zitmz/download/pdf)
65. [https://www.tandfonline.com/doi/pdf/10.1080/23311916.2023.2222988?needAccess=true&role=button](https://www.tandfonline.com/doi/pdf/10.1080/23311916.2023.2222988?needAccess=true&role=button)
66. [https://arxiv.org/pdf/2302.04536.pdf](https://arxiv.org/pdf/2302.04536.pdf)
67. [http://arxiv.org/pdf/2303.12767.pdf](http://arxiv.org/pdf/2303.12767.pdf)
68. [https://arxiv.org/pdf/2302.10724.pdf](https://arxiv.org/pdf/2302.10724.pdf)
69. [https://nftnow.com/news/new-academic-study-calls-out-chatgpt-4-for-declining-performance/](https://nftnow.com/news/new-academic-study-calls-out-chatgpt-4-for-declining-performance/)
70. [https://www.youtube.com/watch?v=ej8TP7P7TiY](https://www.youtube.com/watch?v=ej8TP7P7TiY)
71. [https://asianews.network/us-study-shows-chatgpt-performance-declining-over-time/](https://asianews.network/us-study-shows-chatgpt-performance-declining-over-time/)
72. [https://www.innova.com.tr/en/blog/researchers-prove-chatgpts-behavior-is-changed-significantly](https://www.innova.com.tr/en/blog/researchers-prove-chatgpts-behavior-is-changed-significantly)
73. [https://huggingface.co/papers/2307.09009](https://huggingface.co/papers/2307.09009)
74. [https://bdtechtalks.com/2023/07/24/chatgpt-capabilities-degrading-study/](https://bdtechtalks.com/2023/07/24/chatgpt-capabilities-degrading-study/)
75. [https://arxiv.org/pdf/2307.09009.pdf](https://arxiv.org/pdf/2307.09009.pdf)
76. [https://arxiv.org/abs/2505.08803](https://arxiv.org/abs/2505.08803)
77. [https://arxiv.org/abs/2410.16713](https://arxiv.org/abs/2410.16713)
78. [https://dl.acm.org/doi/10.1145/3630106.3659029](https://dl.acm.org/doi/10.1145/3630106.3659029)
79. [https://arxiv.org/abs/2412.14689](https://arxiv.org/abs/2412.14689)
80. [https://arxiv.org/abs/2402.07043](https://arxiv.org/abs/2402.07043)
81. [https://www.semanticscholar.org/paper/6183173f384a1dc744752fbf0b09ee42d4f9a0be](https://www.semanticscholar.org/paper/6183173f384a1dc744752fbf0b09ee42d4f9a0be)
82. [https://arxiv.org/abs/2408.16333](https://arxiv.org/abs/2408.16333)
83. [https://arxiv.org/abs/2410.12954](https://arxiv.org/abs/2410.12954)
84. [https://arxiv.org/abs/2509.16499](https://arxiv.org/abs/2509.16499)
85. [https://arxiv.org/abs/2404.05868](https://arxiv.org/abs/2404.05868)
86. [https://arxiv.org/pdf/2410.16713.pdf](https://arxiv.org/pdf/2410.16713.pdf)
87. [http://arxiv.org/pdf/2410.12954.pdf](http://arxiv.org/pdf/2410.12954.pdf)
88. [http://arxiv.org/pdf/2406.07515.pdf](http://arxiv.org/pdf/2406.07515.pdf)
89. [https://arxiv.org/html/2403.07857v1](https://arxiv.org/html/2403.07857v1)
90. [http://arxiv.org/pdf/2402.07043.pdf](http://arxiv.org/pdf/2402.07043.pdf)
91. [https://sciencemediacentre.es/en/ai-models-trained-ai-generated-data-can-crash](https://sciencemediacentre.es/en/ai-models-trained-ai-generated-data-can-crash)
92. [https://arxiv.org/html/2410.12954v2](https://arxiv.org/html/2410.12954v2)
93. [https://mondo.com/insights/ai-model-collapse-what-it-is-why-it-matters-and-how-to-prevent-it/](https://mondo.com/insights/ai-model-collapse-what-it-is-why-it-matters-and-how-to-prevent-it/)
94. [https://www.nature.com/articles/s41586-025-08905-3](https://www.nature.com/articles/s41586-025-08905-3)
95. [https://www.davydovconsulting.com/post/newer-ai-models-are-trained-on-its-own-ai-data-deliver-lower-quality-result-than-older-ai-models-tra](https://www.davydovconsulting.com/post/newer-ai-models-are-trained-on-its-own-ai-data-deliver-lower-quality-result-than-older-ai-models-tra)
96. [https://www.nature.com/articles/d41586-024-02355-z](https://www.nature.com/articles/d41586-024-02355-z)
97. [https://arxiv.org/abs/2401.04212](https://arxiv.org/abs/2401.04212)
98. [http://www.ijirss.com/index.php/ijirss/article/view/8858](http://www.ijirss.com/index.php/ijirss/article/view/8858)
99. [https://pubs.acs.org/doi/10.1021/acs.analchem.4c04891](https://pubs.acs.org/doi/10.1021/acs.analchem.4c04891)
100. [https://www.mdpi.com/2227-7390/12/18/2954](https://www.mdpi.com/2227-7390/12/18/2954)
101. [https://onlinelibrary.wiley.com/doi/10.1155/adce/4278730](https://onlinelibrary.wiley.com/doi/10.1155/adce/4278730)
102. [https://ieeexplore.ieee.org/document/11080736/](https://ieeexplore.ieee.org/document/11080736/)
103. [https://www.semanticscholar.org/paper/d9cd5a1ba65a606e348850dd599eba07f101f9e0](https://www.semanticscholar.org/paper/d9cd5a1ba65a606e348850dd599eba07f101f9e0)
104. [https://academic.oup.com/book/8555/chapter/154434270](https://academic.oup.com/book/8555/chapter/154434270)
105. [https://www.semanticscholar.org/paper/660e03151743d91b09c4cde5594a86e708dcc299](https://www.semanticscholar.org/paper/660e03151743d91b09c4cde5594a86e708dcc299)
106. [http://www.liebertpub.com/doi/10.1089/adt.2015.29028.mfe](http://www.liebertpub.com/doi/10.1089/adt.2015.29028.mfe)
107. [https://arxiv.org/pdf/2412.17646.pdf](https://arxiv.org/pdf/2412.17646.pdf)
108. [http://arxiv.org/pdf/2402.14254.pdf](http://arxiv.org/pdf/2402.14254.pdf)
109. [https://arxiv.org/pdf/2002.05193.pdf](https://arxiv.org/pdf/2002.05193.pdf)
110. [https://arxiv.org/pdf/2411.00186.pdf](https://arxiv.org/pdf/2411.00186.pdf)
111. [http://arxiv.org/pdf/2011.02832.pdf](http://arxiv.org/pdf/2011.02832.pdf)
112. [https://pubmed.ncbi.nlm.nih.gov/35803963/](https://pubmed.ncbi.nlm.nih.gov/35803963/)
113. [https://www.youtube.com/watch?v=bZduK7n0tSo](https://www.youtube.com/watch?v=bZduK7n0tSo)
114. [https://nexla.com/ai-infrastructure/data-drift/](https://nexla.com/ai-infrastructure/data-drift/)
115. [https://arpa-h.gov/sites/default/files/2024-10/PRECISE-AI_ProposersDay.pdf](https://arpa-h.gov/sites/default/files/2024-10/PRECISE-AI_ProposersDay.pdf)
116. [https://arxiv.org/html/2506.17442v1](https://arxiv.org/html/2506.17442v1)
117. [https://www.tecton.ai/blog/good-models-go-bad/](https://www.tecton.ai/blog/good-models-go-bad/)