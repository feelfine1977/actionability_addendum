---
Title: "CARE: Coherent Actionable Recourse based on Sound Counterfactual Explanations"
Authors: "Peyman Rasouli, Ingrid Chieh Yu"
DOI: "https://doi.org/10.1145/nnnnnnn.nnnnnnn"
Year: "2021"
Publication Type: "Conference"
Discipline/Domain: "Computer Science / Artificial Intelligence"
Subdomain/Topic: "Interpretable Machine Learning, Counterfactual Explanations, Actionable Recourse"
Eligibility: "Eligible"
Overall Relevance Score: "95"
Operationalization Score: "95"
Contains Definition of Actionability: "Yes"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual with empirical evaluation"
Study Context: "Model-agnostic counterfactual and recourse generation for classification and regression on tabular data"
Geographic/Institutional Context: "University of Oslo, Norway"
Target Users/Stakeholders: "End-users seeking actionable guidance from ML predictions; researchers in explainable AI"
Primary Contribution Type: "Modular explanation framework (CARE) integrating model-level and user-level constraints for actionable recourse"
Reason if Not Eligible: "n/a"
Domain Note: "[[Domain/Computer Science / Artificial Intelligence]]"
Feature Notes:
  - "[[Concept/CL - Clarity (Actionability)]]"
  - "[[Concept/CR - Contextual Relevance (Actionability)]]"
  - "[[Concept/FE - Feasibility (Actionability)]]"
  - "[[Concept/EX - Explainability (Actionability)]]"
  - "[[Concept/GA - Goal Alignment (Actionability)]]"
tags:
  - "feature/cl"
  - "feature/cr"
  - "feature/fe"
  - "feature/ex"
  - "feature/ga"
---
# CARE: Coherent Actionable Recourse based on Sound Counterfactual Explanations (2021)
*Peyman Rasouli, Ingrid Chieh Yu*
**DOI:** https://doi.org/10.1145/nnnnnnn.nnnnnnn
**Domain:** [[Domain/Computer Science / Artificial Intelligence]]
**Subdomain/Topic:** Interpretable Machine Learning, Counterfactual Explanations, Actionable Recourse

## General Summary of the Paper
The authors propose CARE, a modular, model-agnostic explanation framework for generating actionable recourse based on sound counterfactual explanations. CARE integrates four modules—Validity, Soundness, Coherency, and Actionability—organized hierarchically to address both model-level and user/domain-level requirements. Validity ensures minimal changes for achieving the desired outcome; Soundness enforces proximity and connectedness to real data; Coherency preserves correlations between features; and Actionability incorporates user-defined constraints with importance weights. Using a multi-objective optimization approach (NSGA-III), CARE generates multiple, diverse counterfactuals for classification and regression tasks with mixed data types. Experiments on standard datasets show CARE’s superior performance in realism, coherency, and user compliance compared to DiCE and CFPrototype.

## How Actionability is Understood
Actionability is defined as satisfying global and local user/domain-specific preferences through constraints on features (e.g., immutable/mutable status, value ranges), enabling recourse that is realistic, feasible, and aligned with the user’s circumstances.  

  
“A counterfactual should satisfy some global and local preferences that are domain-specific and defined by the end-user.” (p. 2)  

  
“An actionable explanation… takes into account the user’s preferences containing the name of mutable/immutable features, possible values, and their importance…” (p. 3)

## What Makes Something Actionable
Alignment with user-specified constraints (mutable/immutable features, allowed ranges/values)

Preservation of feature coherency under constraints

Feasibility in real-world terms (not recommending impossible changes)

Respecting constraint importance (prioritizing non-violable constraints)

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): CARE  

Methods/Levers: Modular hierarchy with four modules; multi-objective optimization using NSGA-III  

Operational Steps / Workflow:  

 1. VALIDITY: Enforce minimal, sparse changes to achieve the desired outcome.  

 2. SOUNDNESS: Ensure proximity and connectedness to real, same-class data points.  

 3. COHERENCY: Use correlation models to preserve feature relationships.  

 4. ACTIONABILITY: Apply user-defined constraints with importance weighting.  

Data &amp; Measures: Gower distance, Local Outlier Factor, HDBSCAN clustering, correlation measures (Pearson’s R, Cramer’s V), constraint satisfaction checks.  

Implementation Context: Model-agnostic; applicable to tabular classification/regression; handles mixed features.  

  
“We propose a constraint language… and the notion of constraint importance to weigh the constraints according to their importance for the user.” (p. 6)  

  
“CARE… generates actionable recourse by fulfilling the mentioned desiderata through objective functions organized in a modular hierarchy…” (p. 2)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — minimal, interpretable feature changes improve understandability (p. 3).  

CR (Contextual Relevance): Yes — proximity and connectedness ensure alignment with domain data (p. 2).  

FE (Feasibility): Yes — coherent changes preserve real-world plausibility (p. 2–3).  

TI (Timeliness): No — not explicitly addressed.  

EX (Explainability): Partial — explanations are inherent but focus is on actionable counterfactuals, not full causal interpretability.  

GA (Goal Alignment): Yes — constraints ensure user goals/preferences are respected (p. 6).  

Other Dimensions Named by Authors: Coherency, proximity, connectedness.

## Theoretical or Conceptual Foundations
Counterfactual explanations in XAI (Wachter et al., 2017)  

Proximity and connectedness metrics (Laugel et al., 2019)  

Actionable recourse frameworks (Ustun et al., 2019; Karimi et al., 2020)  

Multi-objective optimization (NSGA-III)

## Indicators or Metrics for Actionability
Actionability cost (sum of violated constraint importance values)

Proximity and connectedness scores to assess plausibility

Coherency rate (preservation of feature correlations)

## Barriers and Enablers to Actionability
Barriers: Conflicting constraints; lack of coherent feature changes; artifacts in model space (p. 2–3).  

Enablers: Modular structure allowing selective enforcement of properties; weighting of constraints by importance; correlation-based coherency preservation.

## Relation to Existing Literature
The paper extends prior counterfactual explanation methods by integrating seldom-addressed properties (connectedness, coherency) with actionability. Unlike works that equate proximity with connectedness, CARE treats them as complementary. It also operationalizes coherency, which previous methods neglected.

## Actionability-Focused Summary
CARE is a modular, model-agnostic framework for generating actionable recourse grounded in sound counterfactual explanations. It operationalizes four hierarchical properties—Validity, Soundness, Coherency, and Actionability—through specific objective functions optimized via NSGA-III. Validity ensures minimal, sparse changes; Soundness enforces proximity and connectedness to real, same-class data; Coherency preserves correlations between features; and Actionability integrates user-defined constraints with importance weighting. The approach applies to both classification and regression tasks with mixed-feature datasets. Empirical results show CARE outperforms DiCE and CFPrototype in producing coherent, realistic, and user-compliant recourse while maintaining diversity. The framework can serve as a benchmark for future actionable recourse research.

## Supporting Quotes from the Paper
“A counterfactual should satisfy some global and local preferences that are domain-specific and defined by the end-user.” (p. 2)  

“We introduce a novel notion of actionability that can cover various constraints and prioritize different preferences.” (p. 2)  

“Our proposed objective function… computes the actionability cost… according to the user’s preference.” (p. 6)  

“An actionable explanation… takes into account the user’s preferences containing the name of mutable/immutable features, possible values, and their importance…” (p. 3)

## Actionability References to Other Papers
Ustun, Spangher, Liu (2019) — Actionable recourse in linear classification  

Karimi et al. (2020) — Algorithmic recourse  

Wachter et al. (2017) — Counterfactual explanations  

Laugel et al. (2019) — Proximity and connectedness in counterfactuals  

Dandl et al. (2020) — Multi-objective counterfactual explanations

---
