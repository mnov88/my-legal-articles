
# Create a structured analysis framework for pricing models
import pandas as pd
import json

# Define the analytical framework dimensions
analytical_dimensions = {
    "Behavioral Economics": [
        "Anchoring effects",
        "Reference pricing",
        "Endowment effect",
        "Mental accounting",
        "Sunk cost fallacy",
        "Choice architecture",
        "Fairness perceptions",
        "Loss aversion"
    ],
    "Microeconomic Theory": [
        "Consumer surplus",
        "Price discrimination (1st, 2nd, 3rd degree)",
        "Demand elasticity",
        "Price-quantity relationships",
        "Utility maximization",
        "Marginal analysis",
        "Deadweight loss",
        "Market efficiency"
    ],
    "Competition Policy": [
        "Market power concentration",
        "Barriers to entry",
        "Vertical integration effects",
        "Price fixing risks",
        "Competitive dynamics",
        "Oligopoly behavior",
        "Regulatory compliance",
        "Anti-competitive effects"
    ],
    "Market Theory": [
        "Market structure impact",
        "Network effects",
        "Platform economics",
        "Two-sided markets",
        "Market segmentation",
        "Information asymmetry",
        "Price discovery mechanisms",
        "Market equilibrium"
    ],
    "Development Economics": [
        "Digital divide implications",
        "Access and affordability",
        "Equity considerations",
        "Economic inclusion",
        "Global vs local markets",
        "Infrastructure requirements",
        "Human capital development",
        "Technology adoption barriers"
    ],
    "Commons Management": [
        "Tragedy of the commons",
        "Free-rider problems",
        "Public goods provision",
        "Collective action",
        "Resource sustainability",
        "Trust commons",
        "Digital commons dynamics",
        "Overconsumption risks"
    ]
}

# Create pricing model comparison matrix
pricing_models = {
    "Tier-based Pricing": {
        "description": "Multiple subscription levels with proportional message/feature increases",
        "key_characteristics": [
            "Fixed tiers (e.g., Free, Pro, Max)",
            "Discrete jumps in capacity",
            "Predictable costs for users",
            "Selection effects across tiers"
        ],
        "examples": "ChatGPT Plus/Team/Enterprise, Claude Pro"
    },
    "Credit-based Pricing": {
        "description": "Pre-purchased credits consumed per use",
        "key_characteristics": [
            "Upfront payment for credit pool",
            "Flexible consumption",
            "Potential for credit expiration",
            "Risk transfer to consumer"
        ],
        "examples": "Midjourney credits, various AI platforms"
    },
    "Measured Pricing": {
        "description": "Token-based or exact usage measurement",
        "key_characteristics": [
            "Pay per token processed",
            "Granular cost tracking",
            "Variable monthly costs",
            "Direct cost-value alignment"
        ],
        "examples": "OpenAI API, Anthropic API, Google Vertex AI"
    },
    "Call-based Pricing": {
        "description": "Fixed cost per API call or message",
        "key_characteristics": [
            "Set number of calls per period",
            "Simple unit pricing",
            "Predictable per-call costs",
            "May ignore complexity differences"
        ],
        "examples": "Many SaaS APIs, unified API platforms"
    },
    "Flat-rate Pricing": {
        "description": "Unlimited usage for fixed fee",
        "key_characteristics": [
            "Predictable billing",
            "No usage anxiety",
            "Risk of over/under-utilization",
            "Simple value proposition"
        ],
        "examples": "Traditional software subscriptions, some streaming services"
    }
}

# Save structure for reference
print("Analytical Framework Dimensions:")
for dimension, factors in analytical_dimensions.items():
    print(f"\n{dimension}:")
    for factor in factors:
        print(f"  - {factor}")

print("\n\n" + "="*80)
print("Pricing Models Overview:")
print("="*80)
for model, details in pricing_models.items():
    print(f"\n{model}:")
    print(f"  Description: {details['description']}")
    print(f"  Examples: {details['examples']}")

# Create data structure for cross-cutting analysis
cross_cutting_themes = [
    "Micro vs Macro implications",
    "Short-term vs Long-term effects",
    "Consumer welfare impact",
    "Producer surplus distribution",
    "Market efficiency outcomes",
    "Innovation incentives",
    "Accessibility and equity",
    "Lock-in and switching costs",
    "Price transparency",
    "Behavioral biases exploitation"
]

print("\n\n" + "="*80)
print("Cross-Cutting Analytical Themes:")
print("="*80)
for theme in cross_cutting_themes:
    print(f"  - {theme}")

print("\n\nFramework successfully created for analysis.")
