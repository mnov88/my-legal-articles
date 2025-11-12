# Sample Prompts for Legal Research Multi-Agent Workflow

## Quick Start Prompts

### Initial Project Launch
```
Use the orchestrator agent to coordinate a comprehensive legal research project analyzing [YOUR TOPIC]. The final deliverable should be a [LENGTH] academic paper suitable for [AUDIENCE - law review, seminar paper, practice guide]. Key research questions include: [LIST 2-3 SPECIFIC QUESTIONS]. Timeline: [WEEKS/MONTHS].
```

### Research Planning Phase
```
Use the research-planner agent to create a detailed research strategy for [TOPIC]. Include: (1) comprehensive outline with 4-6 major sections, (2) source identification strategy, (3) methodology framework, and (4) argument development plan. Focus on [JURISDICTION] and consider [SPECIFIC LEGAL ISSUES].
```

### Source Discovery Phase
```
Have the source-discovery agent conduct systematic research on [TOPIC]. Priority areas: Supreme Court and Circuit Court cases from [YEARS], leading law review articles, relevant statutory materials, and empirical studies. Create annotated bibliography with relevance tiers. Target: 25-40 high-quality sources.
```

### Content Analysis Phase
```
Use the content-analyzer agent to systematically review the collected sources. For each source: extract key legal principles, identify relevant quotations for potential use, synthesize holdings and reasoning patterns, and assess relationship to research questions. Organize findings by research outline sections.
```

### Writing Development Phase
```
Have the writing-specialist agent draft [SECTION NAME] based on the research outline and analyzed sources. Target length: [WORDS]. Include: clear thesis statement, systematic argument development, integrated case law analysis, and policy considerations. Maintain scholarly tone appropriate for [AUDIENCE].
```

### Citation Integration Phase  
```
Use the citation-integrator agent to enhance the draft by strategically incorporating relevant quotations. Focus on: authority-building quotes from key cases, principle-articulation statements, and compelling policy language. Ensure smooth textual flow and consistent [CITATION STYLE] formatting.
```

### Quality Assurance Phase
```
Have the quality-assurance agent conduct comprehensive review of the complete draft. Assess: argument coherence and logical flow, citation accuracy and completeness, adherence to scholarly writing standards, and overall persuasiveness. Provide prioritized improvement recommendations.
```

## Specialized Workflow Prompts

### Constitutional Law Analysis
```
Orchestrator: Coordinate analysis of [CONSTITUTIONAL ISSUE] with focus on Supreme Court precedent evolution and circuit court applications. Research-planner should emphasize doctrinal development framework. Source-discovery should prioritize constitutional law databases and leading constitutional scholarship.
```

### Comparative Law Study
```
Use orchestrator to manage comparative analysis of [LEGAL ISSUE] across [JURISDICTIONS]. Research-planner should design systematic comparison framework. Source-discovery should conduct parallel research in each jurisdiction. Content-analyzer should identify patterns and distinguishing features across legal systems.
```

### Empirical Legal Research
```
Orchestrator: Coordinate interdisciplinary research combining legal analysis with empirical data on [TOPIC]. Source-discovery should locate both legal authorities and social science research. Content-analyzer should assess methodological quality of empirical studies. Writing-specialist should integrate statistical findings with legal reasoning.
```

### Legislative Analysis
```
Have orchestrator coordinate comprehensive legislative analysis of [STATUTE/BILL]. Research-planner should structure analysis around statutory interpretation methodology. Source-discovery should gather legislative history, regulatory materials, and judicial interpretations. Focus on practical implementation issues.
```

## Advanced Coordination Prompts

### Multi-Stage Project Management
```
Orchestrator: Implement three-phase approach: (1) Planning phase with research-planner and initial source-discovery, (2) Analysis phase with content-analyzer and preliminary writing-specialist work, (3) Integration phase with citation-integrator and quality-assurance. Schedule quality checkpoints between phases.
```

### Parallel Processing Workflow
```
Use orchestrator to coordinate parallel workflows: Team A (research-planner → source-discovery → content-analyzer) handling doctrinal analysis, Team B handling policy implications with different source focus. Synthesize results through writing-specialist after both teams complete analysis.
```

### Iterative Refinement Process
```
After initial draft completion, have orchestrator coordinate iterative improvement: quality-assurance identifies specific issues, writing-specialist addresses argument problems, citation-integrator handles attribution concerns, followed by second quality-assurance review. Continue until all critical issues resolved.
```

## Troubleshooting Prompts

### Context Management
```
/clear
Use orchestrator to summarize project status and coordinate next phase. Current stage: [DESCRIPTION]. Completed deliverables: [LIST]. Next priorities: [TASKS]. Maintain focus on [CORE RESEARCH QUESTIONS].
```

### Quality Control Issues
```
Quality-assurance has identified these concerns: [LIST ISSUES]. Have orchestrator coordinate targeted fixes: writing-specialist should address [SPECIFIC ISSUES], citation-integrator should handle [ATTRIBUTION PROBLEMS]. Implement changes while preserving overall argument structure.
```

### Workflow Optimization
```
Orchestrator: Analyze workflow efficiency and adjust agent assignments. Current bottlenecks: [DESCRIBE]. Suggested improvements: [LIST]. Reallocate tasks to optimize for [TIMELINE/QUALITY] priorities. Maintain coordination standards.
```

## Prompt Engineering Tips for Agent Workflows

### Effective Delegation Language
```
✅ Good: "Use the research-planner agent to create a comprehensive outline focusing on constitutional interpretation methodology for AI regulation issues."

❌ Poor: "Plan research on AI law."
```

### Clear Success Criteria
```
✅ Good: "Source-discovery should find 15-20 primary authorities (cases, statutes) and 10-15 secondary sources (law reviews, treatises). Prioritize Supreme Court and [Circuit] decisions from 2015-2024."

❌ Poor: "Find some sources on this topic."
```

### Structured Handoffs
```
✅ Good: "After content-analyzer completes source review, have writing-specialist begin with Introduction section using the established outline structure. Target 800 words, include thesis statement and roadmap."

❌ Poor: "Now start writing."
```

### Quality-Focused Instructions
```
✅ Good: "Writing-specialist should maintain scholarly tone appropriate for law review submission. Include counterargument analysis, policy considerations, and clear reasoning chains. Use IRAC structure for case law analysis."

❌ Poor: "Make it sound academic."
```

## Integration with External Tools

### Database Search Coordination
```
Source-discovery: Conduct systematic searches in Westlaw, Lexis, and HeinOnline using these search strategies: [LIST KEYWORDS AND BOOLEAN COMBINATIONS]. Document search methodology and results. Verify currency of all primary authorities.
```

### Citation Management Integration
```
Citation-integrator: Apply Bluebook 21st edition standards consistently. For case citations include parallel citations where required by [JURISDICTION]. Maintain citation sentence formatting. Create bibliography in [FORMAT] for final deliverable.
```

### Document Management
```
Orchestrator: Maintain systematic file organization: research notes in /research/, draft sections in /drafts/, source materials in /sources/. Use consistent naming conventions: [SECTION]-v[NUMBER]-[DATE]. Track version control for all deliverables.
```

## Final Quality Control Prompts

### Comprehensive Review Request
```
Quality-assurance: Conduct final comprehensive review focusing on: (1) argument coherence and logical progression, (2) citation accuracy and completeness, (3) scholarly writing standards compliance, (4) counterargument treatment adequacy, (5) conclusion support by evidence. Provide specific improvement recommendations with priority rankings.
```

### Publication Preparation
```
Use orchestrator to coordinate publication preparation: quality-assurance final review, citation-integrator bibliography formatting, writing-specialist abstract/summary creation. Ensure compliance with [PUBLICATION/SUBMISSION] requirements. Final length verification and formatting check.
```

### Presentation Version Creation
```
After final paper completion, have writing-specialist create presentation version: extract key findings, create slide-appropriate summaries, identify crucial quotes and statistics. Target audience: [DESCRIPTION]. Length: [NUMBER] slides or [MINUTES] presentation time.
```

## Tips for Maximum Effectiveness

1. **Be Specific**: Always provide clear scope, timeline, and quality expectations
2. **Use Consistent Terminology**: Maintain the same legal concepts and terms throughout the workflow
3. **Stage Quality Checks**: Don't wait until the end - build in quality control at each major phase
4. **Coordinate Context**: Help agents understand how their work fits into the larger project
5. **Iterate Strategically**: Use feedback loops to improve quality, but don't over-revise
6. **Document Decisions**: Keep track of major analytical decisions and source choices
7. **Maintain Focus**: Keep the research questions clearly in view throughout the process

These prompts provide concrete starting points for each phase of legal research, but adapt them to your specific needs, timeline, and quality requirements.