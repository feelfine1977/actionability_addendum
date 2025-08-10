---
Title: "Learning analytics dashboard: a tool for providing actionable insights to learners"
Authors: "Teo Susnjak, Gomathy Suganya Ramaswami, Anuradha Mathrani"
DOI: "https://doi.org/10.1186/s41239-021-00313-7"
Year: "2022"
Publication Type: "Journal"
Discipline/Domain: "Educational Technology / Learning Analytics"
Subdomain/Topic: "Learning Analytics Dashboards (LADs), Actionable Insights, Predictive and Prescriptive Analytics"
Eligibility: "Eligible"
Overall Relevance Score: "92"
Operationalization Score: "95"
Contains Definition of Actionability: "Yes (explicit and implicit)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes (proposed LAD integrating descriptive, predictive, prescriptive, interpretability, counterfactuals)"
Operationalization Present: "Yes"
Primary Methodology: "Mixed Methods (Systematic Literature Review + System Design)"
Study Context: "Higher Education, learner-facing dashboards"
Geographic/Institutional Context: "Massey University, New Zealand"
Target Users/Stakeholders: "Students (primary), instructors, higher education institutions"
Primary Contribution Type: "Conceptual framework + prototype implementation"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Educational Technology / Learning Analytics]]"
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
# Learning analytics dashboard: a tool for providing actionable insights to learners (2022)
*Teo Susnjak, Gomathy Suganya Ramaswami, Anuradha Mathrani*
**DOI:** https://doi.org/10.1186/s41239-021-00313-7
**Domain:** [[Domain/Educational Technology / Learning Analytics]]
**Subdomain/Topic:** Learning Analytics Dashboards (LADs), Actionable Insights, Predictive and Prescriptive Analytics

## General Summary of the Paper
The study systematically reviews 17 recently published LADs (2018–2021) to assess their capabilities, focusing on descriptive, predictive, and prescriptive analytics. Findings show most LADs rely on descriptive analytics; few integrate predictive analytics, and none deploy data-driven prescriptive analytics. The authors identify challenges in operationalizing LADs, such as representation &amp; actions, ethics, and agility. Based on identified gaps, they design a state-of-the-art LAD incorporating descriptive, predictive, and prescriptive components, with transparency through model interpretability, explainability, and counterfactuals. This prototype aims to provide learners with actionable insights to adjust learning behaviors. It is currently in pilot trials.

## How Actionability is Understood
Actionability is framed as the LAD’s ability to provide learners with insights that can trigger informed, specific behavioral changes to improve learning outcomes.  

  
“…understand why a model produced given predictions… what insights can be derived… in order to trigger actionable behavioral adjustments.” (p. 8)  

  
“Prescriptive outputs… tailored to each learner… issue advice on behavioral adjustments and learning strategies… to maximize learning outcomes…” (p. 4)

## What Makes Something Actionable
Interpretability and explainability of predictive models.

Presentation of counterfactuals showing how specific changes could improve outcomes.

Contextually relevant, personalized recommendations.

Evidence-based and data-driven suggestions.

Clarity and avoidance of cognitive overload.

Integration of predictive accuracy and confidence communication.

Goal alignment with learner objectives.

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): Proposed Multi-Panel LAD with descriptive, predictive, prescriptive, and interpretability layers.  

Methods/Levers: Machine learning models (CatBoost, scikit-learn), model interpretability tools (Anchors), counterfactual generation (Dice-ml).  

Operational Steps / Workflow: Data collection from LMS (Moodle) → preprocessing → predictive modeling → feature importance analysis → counterfactual generation → visualization in Power BI dashboard panels.  

Data &amp; Measures: Engagement metrics, assignment/test scores, demographic info, predictive risk scores, model accuracy, key predictive features, recommended behavioral changes.  

Implementation Context: Higher education institution pilot, 20 classes, ~4000 student dataset.  

  
“…counterfactuals indicate… minimal changes… would produce… more positive outcomes…” (p. 17)  

  
“…conversion of a black-box predictive model into a glass-box, human interpretable model…” (p. 16)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — Minimal use of colors, clear data-to-ink ratio (p. 17).  

CR (Contextual Relevance): Yes — Learner-specific metrics and comparisons (p. 16).  

FE (Feasibility): Yes — Recommendations based on minimal changes in controllable factors (p. 17).  

TI (Timeliness): Partial — Emphasis on early predictions for timely intervention, but no explicit real-time claim (p. 18).  

EX (Explainability): Yes — Feature importance, anchors, counterfactuals (p. 17–18).  

GA (Goal Alignment): Yes — Advice aimed at maximizing course completion and learning outcomes (p. 4, p. 17).  

Other Dimensions: Ethical transparency, cognitive load minimization.

## Theoretical or Conceptual Foundations
Explainable AI (XAI)

Counterfactual explanations (Wachter et al., 2017)

Learning analytics layers (descriptive, predictive, prescriptive)

Cognitive load theory in dashboard design (Tufte, 2001; Bera, 2016)

## Indicators or Metrics for Actionability
Predictive model accuracy (%)

Feature importance rankings

Risk classification (high/low)

Minimal change thresholds for outcome improvement

## Barriers and Enablers to Actionability
Barriers: Lack of interpretability in most LADs, technical complexity, concept drift, small datasets, ethical risks of misclassification.  

Enablers: Emerging XAI tools, counterfactual generation methods, integrated data sources, agile institutional processes.

## Relation to Existing Literature
Positions itself as first LAD to fully integrate descriptive, predictive, and data-driven prescriptive analytics with interpretability and counterfactuals. Critiques existing LADs for limited predictive capabilities and lack of actionable, personalized recommendations.

## Actionability-Focused Summary
This paper identifies significant gaps in the ability of existing LADs to deliver actionable insights, emphasizing that most are confined to descriptive analytics. It defines actionability as the provision of interpretable, explainable, personalized, and contextually relevant recommendations that learners can feasibly implement to improve outcomes. The proposed LAD operationalizes this by integrating descriptive, predictive, and prescriptive analytics, enhanced with model transparency and counterfactual-based recommendations. This combination is intended to bridge the gap between insight generation and behavior change, setting a benchmark for future LAD development in higher education.

## Supporting Quotes from the Paper
“Models need to possess explanatory characteristics… in order to trigger actionable behavioral adjustments.” (p. 8)  

“Prescriptive outputs… tailored to each learner… advice on behavioral adjustments…” (p. 4)  

“Counterfactuals indicate… minimal changes… would produce… more positive predictive outcomes.” (p. 17)  

“Conversion of a black-box predictive model into a glass-box… so that they can understand how their prediction is being derived.” (p. 16)

## Actionability References to Other Papers
Wachter et al. (2017) – Counterfactual explanations  

Ribeiro et al. (2018) – Anchors for interpretability  

Adadi &amp; Berrada (2018) – Explainable AI  

Baneres et al. (2019, 2021) – Early warning systems and predictive analytics in LA  

Rets et al. (2021), Valle et al. (2021) – Need for prescriptive recommendations in LADs

---
