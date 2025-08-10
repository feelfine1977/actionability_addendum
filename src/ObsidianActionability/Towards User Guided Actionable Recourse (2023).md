---
Title: "Towards User Guided Actionable Recourse"
Authors: "Jayanth Yetukuri, Ian Hardy, Yang Liu"
DOI: "https://doi.org/10.1145/3600211.3604708"
Year: "2023"
Publication Type: "Conference"
Discipline/Domain: "Artificial Intelligence / Human-Centered Computing"
Subdomain/Topic: "Actionable Recourse, User Preferences in ML Explanations"
Eligibility: "Eligible"
Overall Relevance Score: "92"
Operationalization Score: "95"
Contains Definition of Actionability: "Yes (implicit, user-preference-centered)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes"
Contains Interpretability: "Partial"
Contains Framework/Model: "Yes (UP-AR optimization &amp; workflow)"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual with empirical evaluation"
Study Context: "Actionable recourse in ML decision-making across domains such as credit, hiring, insurance, and criminal justice"
Geographic/Institutional Context: "University of California, Santa Cruz; U.S."
Target Users/Stakeholders: "End-users affected by ML decisions (e.g., loan applicants), ML system designers"
Primary Contribution Type: "Method/Framework Proposal with Empirical Validation"
Reason if Not Eligible: "n/a"
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
# Towards User Guided Actionable Recourse (2023)
*Jayanth Yetukuri, Ian Hardy, Yang Liu*
**DOI:** https://doi.org/10.1145/3600211.3604708
**Domain:** [[Domain/Artificial Intelligence / Human-Centered Computing]]
**Subdomain/Topic:** Actionable Recourse, User Preferences in ML Explanations

## General Summary of the Paper
The authors introduce User Preferred Actionable Recourse (UP-AR), a novel method for generating actionable recourse that incorporates explicit user preferences into the optimization process. They argue that existing actionable recourse (AR) approaches prioritize technical efficiency (e.g., proximity, sparsity, cost) but often ignore individual feasibility rooted in user constraints and desires. UP-AR captures preferences in three forms — scoring continuous features, bounding feature values, and ranking categorical features — and embeds them as soft and hard constraints in a gradient-based optimization framework. The approach is validated empirically across credit, income, and criminal recidivism datasets, showing better adherence to user preferences (lower pRMSE) and competitive or superior performance on traditional AR metrics. The authors emphasize that tailoring recourse to user-specific feasibility increases trust, explainability, and adoption.

## How Actionability is Understood
Actionability is defined implicitly as the viability of taking a suggested action within the constraints and preferences of the individual. It is user-centered — what is actionable for one person may not be for another — and includes both universal feasibility constraints (e.g., immutable features) and local feasibility constraints (personal reluctances or capacities).  

  
“Actionability… is centered explicitly around individual preferences, and similar recourses… may not necessarily be equally actionable” (p.1)  

  
“AR aims to provide… a feasible action set which is both actionable by Alice and… as low-cost [as possible]” (p.1)

## What Makes Something Actionable
Alignment with individual user constraints and desires (hard and soft rules)

Ability to operationalize within user’s own cost and effort parameters

Feasibility in practice (e.g., avoiding impossible or undesirable feature changes)

Explainability of why the action is suggested and how it fits user preferences

Personalization beyond general feasibility rules

## How Actionability is Achieved / Operationalized
Framework/Approach Name: User Preferred Actionable Recourse (UP-AR)  

Methods/Levers: Gradient-based iterative optimization weighted by user preference scores; temperature scaling for categorical action frequency; cost correction to remove redundant steps.  

Operational Steps / Workflow:  

 1. Elicit three types of preferences (scoring, bounding, ranking) from the user.  

 2. Embed these as constraints in optimization.  

 3. Generate candidate recourse via stochastic gradient-based updates informed by user preference-weighted costs.  

 4. Apply redundancy and cost correction to finalize recourse.  

Data &amp; Measures: Percentile shift cost function; pRMSE to evaluate preference adherence; traditional AR metrics (success rate, redundancy, sparsity, proximity).  

Implementation Context: Credit lending, income prediction, recidivism risk prediction.  

  
“We start by enabling Alice to provide three types of user preferences… We embed them into an optimization function to guide the recourse generation mechanism” (p.2)  

  
“The proposed method minimizes the cost of a recourse weighted by Γᵢ for all actionable features” (p.3)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — user preference scores increase explainability (p.1)  

CR (Contextual Relevance): Yes — recourse tailored to individual user profile (p.1–2)  

FE (Feasibility): Yes — constraints ensure recommendations are viable for that user (p.1–3)  

TI (Timeliness): Partial — efficiency in generation is discussed, but timeliness as a decision-making window is not explicit  

EX (Explainability): Yes — preference-based reasoning improves explainability (p.1)  

GA (Goal Alignment): Yes — recourse aligned with user’s stated objectives (p.1–2)  

Other Dimensions: Diversity only as secondary contrast to preference tailoring

## Theoretical or Conceptual Foundations
Builds on Actionable Recourse (AR) as per Ustun et al. (2019)  

Local feasibility concept from Mahajan et al. (2019)  

Preference elicitation parallels human-in-the-loop approaches (De Toni et al., 2022)  

Optimization inspired by gradient-based adversarial example generation

## Indicators or Metrics for Actionability
pRMSE between desired and achieved feature cost proportions  

Constraint violations (lower is better)  

Redundancy (steps that don’t affect outcome)  

Sparsity (number of features changed)  

Proximity (l2 distance from original point)

## Barriers and Enablers to Actionability
Barriers: Ignoring user-specific constraints; reliance on universal cost functions; high redundancy; expensive categorical changes  

Enablers: Explicit preference capture; flexible optimization accommodating hard/soft constraints; cost correction

## Relation to Existing Literature
The authors note most AR literature focuses on universal feasibility and cost minimization, sometimes adding diversity to hedge against unknown preferences. UP-AR directly incorporates known preferences, going beyond diversity-based approaches by personalizing the optimization process.

## Actionability-Focused Summary
This paper reframes actionability in ML recourse as inherently user-specific and preference-driven, arguing that what is “doable” varies across individuals with identical profiles. The proposed UP-AR framework operationalizes this view by eliciting explicit user preferences in three structured forms and embedding them into a gradient-based recourse generation process. By weighting feature changes according to these preferences and applying redundancy/cost correction, UP-AR improves alignment between suggested actions and user feasibility, outperforming existing methods on preference adherence and maintaining strong results on traditional AR metrics. This personalized approach enhances trust and explainability, and positions actionability as a function of both model mechanics and user-centered feasibility constraints.

## Supporting Quotes from the Paper
“Actionability… is centered explicitly around individual preferences…” (p.1)  

“We start by enabling Alice to provide three types of user preferences… embed them into an optimization function…” (p.2)  

“Communicating in terms of preference scores… improves the explainability of a recourse generation mechanism” (p.1)  

“The proposed method minimizes the cost of a recourse weighted by Γᵢ for all actionable features” (p.3)

## Actionability References to Other Papers
Ustun et al. (2019) — Actionable Recourse in Linear Classification  

Mahajan et al. (2019) — Local Feasibility  

De Toni et al. (2022) — Human-in-the-loop preference elicitation  

Wachter et al. (2017) — Counterfactual Explanations  

Poyiadzi et al. (2020) — FACE method

---
