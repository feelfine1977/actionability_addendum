---
Title: "Individual and Group-level considerations of Actionable Recourse"
Authors: "Jayanth Yetukuri, Yang Liu"
DOI: "https://doi.org/10.1145/3600211.3604758"
Year: "2023"
Publication Type: "Conference"
Discipline/Domain: "Artificial Intelligence / Human-Centered Computing"
Subdomain/Topic: "Actionable Recourse, Fairness in Machine Learning, User Preferences, Plausibility"
Eligibility: "Eligible"
Overall Relevance Score: "85"
Operationalization Score: "78"
Contains Definition of Actionability: "Yes (explicitly in context of recourse viability)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Partial (linked to transparency and trust)"
Contains Interpretability: "Partial (discussed via counterfactual explanation methods)"
Contains Framework/Model: "Yes (proposed optimization approach incorporating preferences and plausibility)"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual + Quantitative Experiments"
Study Context: "Machine learning decision systems in lending, insurance, hiring"
Geographic/Institutional Context: "University of California, Santa Cruz; USA"
Target Users/Stakeholders: "Negatively impacted individuals seeking recourse; developers of ML decision systems"
Primary Contribution Type: "Conceptual framework + algorithmic method proposal with empirical demonstration"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Artificial Intelligence / Human-Centered Computing]]"
Feature Notes:
  - "[[Concept/CL - Clarity (Actionability)]]"
  - "[[Concept/CR - Contextual Relevance (Actionability)]]"
  - "[[Concept/FE - Feasibility (Actionability)]]"
  - "[[Concept/TI - Timeliness (Actionability)]]"
  - "[[Concept/EX - Explainability (Actionability)]]"
  - "[[Concept/GA - Goal Alignment (Actionability)]]"
tags:
  - "feature/cl"
  - "feature/cr"
  - "feature/fe"
  - "feature/ti"
  - "feature/ex"
  - "feature/ga"
---
# Individual and Group-level considerations of Actionable Recourse (2023)
*Jayanth Yetukuri, Yang Liu*
**DOI:** https://doi.org/10.1145/3600211.3604758
**Domain:** [[Domain/Artificial Intelligence / Human-Centered Computing]]
**Subdomain/Topic:** Actionable Recourse, Fairness in Machine Learning, User Preferences, Plausibility

## General Summary of the Paper
The paper explores how actionable recourse in ML decision systems can better account for individual user preferences and group-level plausibility to ensure fairness and feasibility. Current recourse methods optimize for factors like proximity, sparsity, and validity but often ignore personal constraints or socio-demographic context. The authors introduce three forms of user preference—scoring continuous features, ranking categorical features, and bounding feature values—and embed them in the optimization process for generating recourses. At the group level, they propose plausibility constraints based on the distribution of approved cases within the individual’s subgroup, aiming to avoid biased or impractical suggestions. Experimental results show that their method better adheres to individual preferences and mitigates plausibility bias across protected groups.

## How Actionability is Understood
Actionability is defined as the viability of taking a suggested action within the context of recourse for ML decisions. It encompasses both feasibility for the individual (personal constraints, preferences) and plausibility within the socio-demographic group context.  

  
“Ensure the actionability (the viability of taking a suggested action) of recourse.” (p. n/a)  

  
“Plausibility draws strong signals from group-level population information… to achieve low-cost recourses across protected groups.” (p. n/a)

## What Makes Something Actionable
Alignment with user preferences (continuous feature scores, categorical rankings, feature bounds)  

Feasibility given personal constraints  

Plausibility based on similarity to approved cases in the individual’s subgroup  

Transparency to build trust  

Fairness across groups with different distributional characteristics

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): Not formally named, but described as constrained optimization incorporating user preferences and group-level plausibility metrics.  

Methods/Levers: Optimization function embedding individual preferences; plausibility score constraint based on subgroup-approved distribution.  

Operational Steps / Workflow:  

 1. Collect individual user preferences (three types).  

 2. Integrate these as constraints in recourse optimization.  

 3. Calculate group-level plausibility score.  

 4. Generate recourse maximizing plausibility while respecting user constraints.  

Data &amp; Measures: Real-world datasets; plausibility score; recourse cost metrics.  

Implementation Context: Lending, insurance, hiring decisions.  

  
“We propose to capture… three types of user preferences… and embed them into an optimization function for guiding the recourse generation mechanism.” (p. n/a)  

  
“We quantify plausibility of recourse with respect to the approved sub-population of the individual’s group…” (p. n/a)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — linked to transparency and understandability in recourse generation.  

CR (Contextual Relevance): Yes — plausibility relies on subgroup context.  

FE (Feasibility): Yes — explicitly tied to personal constraints and preferences.  

TI (Timeliness): Partial — not directly addressed as a criterion.  

EX (Explainability): Partial — present via transparency but not deeply analyzed.  

GA (Goal Alignment): Yes — recourse must align with the individual’s goal of entering the approved subgroup.  

Other Dimensions Named by Authors: Plausibility; User Preference Diversity.

## Theoretical or Conceptual Foundations
Actionable Recourse in Linear Classification (Ustun et al., 2019)  

Counterfactual explanation generation methods (FACE, GS, CCHVAE)  

Local feasibility constraints (Mahajan et al., 2019)

## Indicators or Metrics for Actionability
Plausibility score based on proximity to approved subgroup manifold  

Recourse cost (individual and group-level)  

Adherence to stated user preferences

## Barriers and Enablers to Actionability
Barriers:  

 - Universal cost metrics ignoring personal constraints  

 - Distributional idiosyncrasies across groups  

 - Lack of integration of user preferences in current methods  

Enablers:  

 - Explicit collection of user preferences  

 - Group-level plausibility constraint  

 - Transparent recourse generation

## Relation to Existing Literature
The paper builds upon existing counterfactual explanation and actionable recourse literature but extends it by introducing a dual focus on individualized preference capture and group-level plausibility, which addresses fairness and feasibility more holistically than prior distance- or sparsity-based approaches.

## Actionability-Focused Summary
This paper advances the concept of actionable recourse by explicitly integrating individual-level preferences and group-level plausibility constraints into the generation process for counterfactual suggestions in ML decision systems. The authors propose an optimization-based framework that embeds user-defined continuous feature scores, categorical rankings, and bounds, while also evaluating the plausibility of recourse relative to the distribution of approved outcomes within the individual’s demographic group. By combining these perspectives, the method aims to enhance feasibility, fairness, and trustworthiness of recourse suggestions. Experimental results on real-world datasets demonstrate improved adherence to personal constraints and mitigation of plausibility bias across protected groups. The approach addresses gaps in current methods that focus mainly on universal cost functions and do not systematically incorporate socio-contextual constraints.

## Supporting Quotes from the Paper
“[Actionability is] the viability of taking a suggested action…” (p. n/a)  

“We propose to capture Alice’s three types of user preferences… and embed them into an optimization function…” (p. n/a)  

“We quantify plausibility of recourse with respect to the approved sub-population of the individual’s group…” (p. n/a)  

“Considering that she belongs to the sub-population of denied single parent, the recourse may not be actionable…” (p. n/a)

## Actionability References to Other Papers
Ustun et al. (2019) — Actionable Recourse in Linear Classification  

Mahajan et al. (2019) — Local feasibility in counterfactual explanations  

Mothilal et al. (2020) — Diverse counterfactual explanations  

Poyiadzi et al. (2020) — FACE method  

Laugel et al. (2017) — Inverse classification interpretability  

Pawelczyk et al. (2020) — CCHVAE counterfactual generation

---
