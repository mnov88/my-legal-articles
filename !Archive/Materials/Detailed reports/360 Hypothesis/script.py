
# Let me create a summary analysis of the key findings from the research so far
# This will help structure the hypotheses testing

research_summary = {
    "H1_Technical_Constraints": {
        "Evidence_Supporting": [
            "LLM inference costs vary dramatically (200x-1000x reduction over 3 years) [web:27][web:30]",
            "GPU costs 15x higher than standard compute; unpredictable workloads [web:23]",
            "Computational costs depend on: model size, token count, reasoning depth [web:24][web:33][web:36]",
            "Infrastructure costs represent 24-34% of net margins [web:157]",
            "Real-time pricing requires complex tracking systems [web:95][web:98]",
            "Energy consumption varies based on usage patterns, location [web:82][web:94]",
            "Variable compute demands create forecasting challenges [web:20][web:26]"
        ],
        "Evidence_Against": [
            "Cloud providers successfully implement transparent per-token pricing [web:24][web:33]",
            "Metered billing works effectively in utilities, telecommunications [web:95][web:98][web:104]",
            "Dynamic pricing algorithms can calculate costs in real-time [web:31]",
            "AWS/Azure/GCP provide detailed cost breakdowns [web:25]"
        ]
    },
    "H2_Alternative_Models_Performance": {
        "Evidence_Supporting": [
            "Pure usage-based pricing increases customer churn due to unpredictability [web:57]",
            "Revenue recognition becomes difficult with variable costs [web:57]",
            "Commitment discounts don't work for unpredictable AI workloads [web:23]",
            "Pay-what-you-want reduces purchase rates, creates free-rider problems [web:108][web:112][web:122]",
            "High demand uncertainty makes pay-what-you-want suboptimal [web:125][web:126]"
        ],
        "Evidence_Against": [
            "Usage-based pricing aligns costs with value, improves fairness [web:60][web:98]",
            "Metered billing provides transparency and customer satisfaction [web:95][web:104]",
            "Hybrid models (usage + subscription) maximize consumer welfare [web:60][web:66]",
            "Pay-what-you-want can increase consumer welfare under uncertainty [web:125]"
        ]
    },
    "H3_Transferability_From_Similar_Industries": {
        "Evidence_Supporting": [
            "AI differs from utilities: unpredictable demand vs. stable consumption [web:57][web:23]",
            "Cloud electricity pricing faces similar challenges but different scale [web:82][web:94]",
            "Telecommunications pricing more stable than AI token consumption [web:95]",
            "Information asymmetry greater in AI than traditional services [web:79][web:96]"
        ],
        "Evidence_Against": [
            "Metered billing principles apply across industries [web:95][web:98][web:104]",
            "Cloud computing successfully adapted utility pricing model [web:76][web:89]",
            "Similar demand uncertainty issues resolved in other sectors [web:126][web:132]"
        ]
    },
    "H4_Transparency_Consumer_Outcomes": {
        "Evidence_Supporting": [
            "Price transparency can reduce consumer surplus [web:41]",
            "Information disclosure may worsen personalized pricing outcomes [web:75][web:163]",
            "Complexity creates decision fatigue, reduces satisfaction [web:62][web:127][web:133]",
            "Transparency requirements increase costs passed to consumers [web:63][web:71][web:74]",
            "Dynamic pricing transparency may enable collusion [web:40][web:163]",
            "Subscription inertia provides predictability consumers value [web:127][web:130][web:133]"
        ],
        "Evidence_Against": [
            "Price transparency improves competition and consumer welfare [web:41][web:61][web:74]",
            "Disclosure requirements protect against unfair practices [web:63][web:155][web:164]",
            "Transparency enables informed decision-making [web:37][web:51][web:69]",
            "Drip pricing bans increase total welfare [web:148][web:150][web:155]"
        ]
    }
}

# Count evidence for each hypothesis
for hypothesis, data in research_summary.items():
    supporting = len(data["Evidence_Supporting"])
    against = len(data["Evidence_Against"])
    print(f"{hypothesis}:")
    print(f"  Supporting evidence: {supporting} points")
    print(f"  Contradicting evidence: {against} points")
    print(f"  Ratio: {supporting/(supporting+against):.1%} supporting\n")
