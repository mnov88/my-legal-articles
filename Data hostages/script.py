
# Organize research findings into structured categories for each hypothesis

research_structure = {
    "H1_User_Fear_Content_Loss": {
        "behavioral_economics": [
            "Loss aversion: People value losses 2x more than equivalent gains (web:39, web:59, web:62)",
            "Endowment effect: Users overvalue content they 'own' (web:135, web:137, web:143)",
            "Sunk cost fallacy: Past investment drives continued platform use (web:39, web:40, web:50, web:51)",
            "Psychological ownership increases retention and loyalty (web:243, web:246, web:249)"
        ],
        "platform_lock_in": [
            "Switching costs create user lock-in effects (web:58, web:61, web:64, web:73)",
            "Network externalities amplify switching barriers (web:46, web:61)",
            "Data and content investment creates attachment (web:243, web:246, web:252)",
            "Free trials exploit endowment effect to increase retention (web:41, web:143)"
        ],
        "empirical_evidence": [
            "Users more likely to retain owned objects than acquire new ones (web:135)",
            "Psychological ownership increases satisfaction and contribution quality (web:243)",
            "Content creation increases sense of ownership and reduces switching (web:243)",
            "Platform loyalty correlates with data/content investment (web:46, web:53)"
        ],
        "user_retention_patterns": [
            "Habit formation and status quo bias drive continued use (web:39, web:40)",
            "Fear of missing out (FOMO) contributes to retention (web:39, web:44)",
            "Personalization creates switching barriers (web:207, web:212, web:217)",
            "Profile/content deletion perceived as significant loss (web:243)"
        ]
    },
    
    "H2_Companies_Exploit": {
        "dark_patterns_evidence": [
            "Dark patterns ubiquitous: 97% of popular EU sites use at least one (web:178)",
            "Cookie consent banners employ deceptive design (web:158, web:166, web:169)",
            "Difficult cancellation flows trap users (web:133, web:139, web:142)",
            "Hidden opt-outs and obfuscation common (web:24, web:27, web:133)"
        ],
        "data_deletion_threats": [
            "Roach Motel pattern: Easy to enter, hard to exit (web:138, web:142)",
            "Account deletion made deliberately complex (web:133, web:139)",
            "Data loss warnings used to discourage cancellation (web:133)",
            "Emotional manipulation in cancellation flows (web:24, web:133, web:169)"
        ],
        "business_practices": [
            "Short-term gains vs long-term trust erosion (web:133, web:153)",
            "Dark patterns used despite negative brand impact (web:133, web:153)",
            "Forced continuity subscriptions common (web:133, web:134)",
            "Services delete data to discourage switching (web:1, web:2, web:6)"
        ],
        "regulatory_findings": [
            "Belgian DPA found IAB system illegally uses dark patterns (web:173)",
            "Norwegian Consumer Council: 90% of sites use dark patterns (web:169)",
            "FTC enforcement against Amazon Prime dark patterns (web:139, web:142)",
            "First EU DPA explicit decision on dark patterns (web:172)"
        ]
    },
    
    "H3_GDPR_Legality": {
        "no_processing_obligation": [
            "GDPR requires legal basis but not obligation to process (web:95, web:96, web:98)",
            "Six legal bases, none mandates continuous processing (web:95, web:96, web:104)",
            "Controllers determine purposes and means (web:29, web:95)",
            "Service termination may end legal basis (web:102, web:215)"
        ],
        "data_retention_principles": [
            "Storage limitation principle: retain only as necessary (web:23, web:29, web:32)",
            "Purpose limitation: data kept only for specified purposes (web:32, web:35)",
            "No indefinite storage permitted (web:26, web:32)",
            "Retention must be justified and documented (web:29, web:32)"
        ],
        "right_to_erasure_limits": [
            "Article 17 has multiple exceptions (web:97, web:100, web:103)",
            "Legal obligations can justify retention (web:97, web:100, web:103)",
            "Defense of legal claims exception (web:97, web:100)",
            "Research purposes exception (web:106, web:112)"
        ],
        "data_portability_gaps": [
            "Article 20 limited to user-provided data (web:244, web:247, web:250)",
            "No interoperability requirement (web:242, web:244)",
            "Portability doesn't mandate compatibility (web:224, web:227, web:242)",
            "Implementation challenges significant (web:232, web:247)"
        ],
        "legal_basis_termination": [
            "Contract termination may end processing basis (web:102)",
            "Consent withdrawal requires cessation (web:96, web:109, web:114)",
            "No obligation to continue processing post-termination (web:102, web:215)",
            "Legitimate interest requires balancing test (web:95, web:96, web:105)"
        ],
        "compliance_findings": [
            "27% of services non-compliant with erasure (web:211)",
            "Deletion often incomplete or delayed (web:211, web:213)",
            "Over-retention violates data minimization (web:278)",
            "FTC enforcement against excessive retention (web:278)"
        ]
    }
}

# Key academic gaps and regulatory blind spots
regulatory_gaps = {
    "GDPR_limitations": [
        "No explicit prohibition of deletion-based retention strategies",
        "Dark patterns not directly addressed in GDPR text",
        "Fairness principle underspecified for interface design",
        "Consent manipulation through dark patterns insufficiently regulated",
        "Data portability too limited to enable true switching"
    ],
    "enforcement_challenges": [
        "First explicit dark patterns DPA decision only in 2023 (web:172)",
        "Limited case law on service termination data practices",
        "Difficulty proving unfair or deceptive intent",
        "Cross-border enforcement complexity",
        "Technical standards for portability lacking"
    ],
    "behavioral_exploitation_gaps": [
        "No regulation of psychological manipulation through data loss threats",
        "Sunk cost exploitation not addressed in law",
        "Endowment effect deliberately triggered by design",
        "Loss aversion weaponized in cancellation flows",
        "No requirement for neutral choice architecture"
    ],
    "research_needs": [
        "Empirical studies on user switching behavior with data loss",
        "Quantitative analysis of cancellation flow dark patterns",
        "Economic analysis of retention through content hostage-taking",
        "Legal analysis of fairness principle in data deletion context",
        "Comparative study of data portability effectiveness"
    ]
}

print("Research structure organized for 3 hypotheses")
print(f"H1 categories: {len(research_structure['H1_User_Fear_Content_Loss'])}")
print(f"H2 categories: {len(research_structure['H2_Companies_Exploit'])}")
print(f"H3 categories: {len(research_structure['H3_GDPR_Legality'])}")
print(f"Regulatory gaps identified: {len(regulatory_gaps['GDPR_limitations'])}")
