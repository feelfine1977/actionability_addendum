---
Title: "Why-Not Explainable Graph Recommender"
Authors: "Herve-Madelein Attolou, Katerina Tzompanaki, Kostas Stefanidis, Dimitris Kotzinos"
DOI: "10.1109/ICDE60146.2024.00178"
Year: "2024"
Publication Type: "Conference"
Discipline/Domain: "Computer Science / Artificial Intelligence"
Subdomain/Topic: "Explainable Recommender Systems, Counterfactual Explanations, Graph-based Recommendations"
Eligibility: "Eligible"
Overall Relevance Score: "90"
Operationalization Score: "95"
Contains Definition of Actionability: "Yes (implicit and explicit through actionable explanation design)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes"
Contains Interpretability: "Partial"
Contains Framework/Model: "Yes (EMiGRe)"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual + Experimental Evaluation"
Study Context: "Graph-based recommendation systems with user–item interaction data"
Geographic/Institutional Context: "CY Cergy Paris University, Tampere University"
Target Users/Stakeholders: "End-users of RS, system developers/debuggers"
Primary Contribution Type: "Algorithm/Framework Proposal with Evaluation"
Reason if Not Eligible: "N/A"
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
# Why-Not Explainable Graph Recommender (2024)
*Herve-Madelein Attolou, Katerina Tzompanaki, Kostas Stefanidis, Dimitris Kotzinos*
**DOI:** 10.1109/ICDE60146.2024.00178
**Domain:** [[Domain/Computer Science / Artificial Intelligence]]
**Subdomain/Topic:** Explainable Recommender Systems, Counterfactual Explanations, Graph-based Recommendations

## General Summary of the Paper
This paper introduces EMiGRe, a framework for generating Why-Not explanations in graph-based recommender systems, explaining why a desired item was not the top recommendation. Unlike existing explainable RS approaches (e.g., PRINCE), EMiGRe targets missing recommendations and outputs actionable insights in the form of counterfactual changes to the user’s interaction graph—either edges to remove (past actions) or edges to add (potential actions). The framework defines a formal problem setting, proposes search strategies (Add/Remove modes) with heuristics (Incremental, Powerset, Exhaustive Comparison), and evaluates performance on a processed Amazon reviews dataset. Results show feasibility, differences in runtime, success rates, and explanation size across methods. The authors highlight challenges such as popular items, cold-start users, and the need for meta-explanations.

## How Actionability is Understood
Actionability is framed as providing explanations that suggest concrete, feasible actions a user can take (or could have taken) to obtain the desired recommendation. This goes beyond interpretability by prescribing specific edge additions/removals in the user–item graph.  

  
“We opt for a form of Counterfactual Explanations… proposing a possible world that could have led to the desired outcome” (p. 1)  

  
“…provides… actionable insights on the source data and their interrelations” (p. 1)

## What Makes Something Actionable
Directly modifiable by the user (edges rooted at the user node)

Feasibility within privacy constraints (only user’s own actions)

Causally linked to producing the desired recommendation (must result in WNI being top-1)

Specificity (identifies exact edges to add or remove)

Adaptability to system constraints and user preferences

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): EMiGRe (Explainable Missing Graph Recommendation)

Methods/Levers: Counterfactual graph modifications via edge addition (Add Mode) or removal (Remove Mode)

Operational Steps / Workflow:

 1. Define Why-Not item (WNI)

 2. Identify candidate edges (user-rooted) influencing WNI ranking using Personalized PageRank contributions

 3. Search for minimal modification set (Incremental, Powerset, Exhaustive Comparison)

 4. Validate candidate explanations against top-1 constraint

Data &amp; Measures: Personalized PageRank scores, contribution metrics, runtime, success rate, explanation size

Implementation Context: Post-hoc explanation for graph-based RS, tested on Amazon product reviews

  
“…set of edges rooted at the user u node… to replace rec by WNI as the recommendation” (p. 5)  

  
“…propose… missing pertinent edges to be added… or existing edges to be removed” (p. 5)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — explicitly identifies specific, understandable actions (edges)  

CR (Contextual Relevance): Yes — actions are user-specific and relevant to target item  

FE (Feasibility): Yes — constrained to actions the user can perform  

TI (Timeliness): No — no explicit discussion of time sensitivity  

EX (Explainability): Yes — method provides causal reasoning via counterfactuals  

GA (Goal Alignment): Yes — directly tied to achieving WNI recommendation  

Other Dimensions Named by Authors: Privacy-preserving scope

## Theoretical or Conceptual Foundations
Counterfactual explanations (AI interpretability literature)

Graph-based recommendation and Personalized PageRank

Why-Not questions in databases and ranking functions

## Indicators or Metrics for Actionability
Success rate (ability to achieve WNI in top-1)

Size of explanation (fewer edges preferred)

Runtime efficiency (practicality of producing the explanation)

## Barriers and Enablers to Actionability
Barriers:

 - Cold start/low activity users (few modifiable edges)

 - Highly popular competing items (structurally difficult to displace)

 - Out-of-scope cases where only edge additions or removals are insufficient

Enablers:

 - Availability of rich user–item interaction data

 - Graph-based structure allowing edge-level manipulation

 - Efficient PPR computation methods

## Relation to Existing Literature
Extends explainable RS literature from Why to Why-Not scenarios, differing from PRINCE by:

Focusing on missing recommendations

Providing both past-action and future-action explanations

Builds on prior Why-Not work in databases and adapts it to graph RS with privacy-preserving constraints.

## Actionability-Focused Summary
The paper introduces EMiGRe, a novel framework for producing actionable Why-Not explanations in graph-based recommender systems. Actionability is defined through concrete, user-feasible modifications—adding or removing edges in the user–item graph—to achieve a specific desired recommendation. The framework operationalizes this via Personalized PageRank-based influence scoring and search strategies (Incremental, Powerset, Exhaustive Comparison), ensuring that the suggested actions directly cause the Why-Not item to become top-1. The approach is privacy-conscious, focusing only on the user’s own actions. Evaluation on Amazon review data shows varying trade-offs between runtime, explanation size, and success rates across methods. The work makes a strong conceptual and practical contribution to actionable explainability in RS, though timeliness is not addressed and popularity biases remain challenging.

## Supporting Quotes from the Paper
“We opt for a form of Counterfactual Explanations… proposing a possible world that could have led to the desired outcome” (p. 1)  

“…set of edges rooted at the user u node… to replace rec by WNI as the recommendation” (p. 5)  

“We provide more actionable explanations, by proposing not only existing actions… but also new actions” (p. 5)  

“This form of explanation provides user-comprehensible and actionable evidence of the trustworthiness of the system” (p. 4)

## Actionability References to Other Papers
Ghazimatin et al. (2020) — PRINCE: Provider-side Interpretability with Counterfactual Explanations in RS  

Miller (2017, 2021) — Contrastive explanation theory  

Database and IR Why-Not literature (e.g., Bidoit et al. 2014, Chapman &amp; Jagadish 2009)

---
