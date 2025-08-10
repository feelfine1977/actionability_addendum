---
Title: "Evidential Reasoning Approach for Predicting Popularity of Instagram Posts"
Authors: "L. Rivadeneira, I. Loor"
DOI: "10.1109/ACCESS.2024.3510637"
Year: "2024"
Publication Type: "Journal"
Discipline/Domain: "Computer Science / Social Media Analytics"
Subdomain/Topic: "Predictive modelling of social media engagement using evidential reasoning"
Eligibility: "Eligible"
Overall Relevance Score: "78"
Operationalization Score: "85"
Contains Definition of Actionability: "Yes (implicit)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes (MAKER)"
Operationalization Present: "Yes"
Primary Methodology: "Quantitative / Predictive Modelling (Machine Learning)"
Study Context: "Instagram post popularity prediction using visual and textual features"
Geographic/Institutional Context: "Harvard University (USA) &amp; University of Oxford (UK) Instagram accounts"
Target Users/Stakeholders: "Social media managers, marketing professionals, academic institutions, content strategists"
Primary Contribution Type: "Methodological framework and comparative evaluation"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Computer Science / Social Media Analytics]]"
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
# Evidential Reasoning Approach for Predicting Popularity of Instagram Posts (2024)
*L. Rivadeneira, I. Loor*
**DOI:** 10.1109/ACCESS.2024.3510637
**Domain:** [[Domain/Computer Science / Social Media Analytics]]
**Subdomain/Topic:** Predictive modelling of social media engagement using evidential reasoning

## General Summary of the Paper
The study applies the MAKER algorithm, grounded in evidential reasoning, to predict the popularity of Instagram posts (binary classification: high/low based on median likes). Using 2022 data from Harvard and Oxford, two models are built for each institution—one using textual features (emojis, sentiment, hashtags, mentions, season) and the other using visual features (image type, time of day, dominant colour). MAKER is compared against decision trees, SVM, and KNN, achieving higher precision and interpretability. The paper not only evaluates predictive performance but also extracts actionable patterns, such as Harvard’s popular posts tending toward vibrant, scenic images in certain seasons, and Oxford’s benefiting from emoji use and specific content structures.

## How Actionability is Understood
Implicitly defined as the capacity of model outputs to guide content strategy decisions through transparent, interpretable insights that reveal which post attributes are most likely to increase engagement.  

  
“MAKER’s interpretability means that it provides actionable insights… help users make informed decisions based on its insights and improve content strategies by revealing which features most influence engagement.” (p. 1)  

  
“While this study focuses on proposing a model for prediction purposes, it is essential to translate these findings into actionable strategies for decision-makers…” (p. 13)

## What Makes Something Actionable
Ability to identify specific post attributes correlated with higher popularity.

Transparency in reasoning (weights, reliabilities, evidence interdependencies).

Interpretability enabling justification of model outputs.

Context-specific feature patterns rather than one-size-fits-all rules.

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): MAKER (Maximum likelihood evidential reasoning).  

Methods/Levers: Integration of textual and visual post features into interpretable evidential reasoning models; optimisation of evidence weights and reliabilities.  

Operational Steps / Workflow: Data collection → Preprocessing → Feature extraction (textual/visual) → Model training/testing (5-fold split) → MAKER optimisation → Comparative performance evaluation → Pattern extraction for actionable strategies.  

Data &amp; Measures: Median likes threshold, emoji/hashtag/mention counts, sentiment, season, image type, dominant colour, time of day.  

Implementation Context: Official university Instagram accounts.  

  
“This transparency yields an interpretable model… examining the relationship between output and input variables, as well as the rationale behind the assignment of weights and reliabilities…” (p. 3)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — outputs are interpretable and grounded in transparent parameter assignment.  

CR (Contextual Relevance): Yes — feature influence patterns are institution-specific.  

FE (Feasibility): Partial — focuses on achievable content adjustments but omits resource constraints.  

TI (Timeliness): No explicit link.  

EX (Explainability): Yes — full traceability of decision process.  

GA (Goal Alignment): Partial — aligns model with engagement improvement goals but not broader organisational KPIs.  

Other Dimensions Named by Authors: Transparency, interpretability, data completeness handling.

## Theoretical or Conceptual Foundations
Evidential reasoning (ER) rule, based on Dempster-Shafer theory.

Transparency and interpretability in AI (Rudin, 2019).

Multimodal content engagement theory from prior social media analytics research.

## Indicators or Metrics for Actionability
Precision, recall, F1-score, AUC, RMSE (used to assess predictive reliability).

Likelihood scores for evidence patterns.

## Barriers and Enablers to Actionability
Barriers: API restrictions limiting automated data collection; exclusion of non-picture post formats; limited engagement metrics; manual feature categorisation.  

Enablers: MAKER’s robustness to incomplete data; integration of multimodal features; transparent modelling process.

## Relation to Existing Literature
Extends prior predictive models for Instagram by addressing interpretability and transparency gaps. Unlike black-box models (e.g., CNNs, fusion networks), MAKER enables actionable feature-level insights.

## Actionability-Focused Summary
The paper demonstrates how MAKER—a maximum likelihood evidential reasoning approach—can deliver not only accurate predictions of Instagram post popularity but also actionable, interpretable insights for content strategy. By modelling both textual and visual features, and optimising evidence weights/reliabilities, the approach surfaces institution-specific patterns (e.g., seasonal effects, colour palettes, emoji usage) linked to higher engagement. Actionability here is tied to the transparency and contextual relevance of outputs, empowering decision-makers to adjust strategies based on identified drivers of popularity. Compared to decision trees, SVM, and KNN, MAKER offers superior precision and interpretability, making it a valuable tool for data-informed social media management.

## Supporting Quotes from the Paper
“MAKER’s interpretability means that it provides actionable insights… help users make informed decisions based on its insights…” (p. 1)  

“Transparency yields an interpretable model… examining the relationship between output and input variables…” (p. 3)  

“It is essential to translate these findings into actionable strategies for decision-makers…” (p. 13)  

“Harvard’s popular posts typically show positive or neutral sentiment… Oxford’s popular posts… use more emojis, hashtags, and mentions.” (p. 11)

## Actionability References to Other Papers
Rudin, C. (2019) on interpretable models vs. black-box AI.  

Yang &amp; Xu (2017) on inferential modelling with data in evidential reasoning.  

Aramendia-Muneta et al. (2021) on key image attributes for engagement.

---
