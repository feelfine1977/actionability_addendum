---
Title: "Data-Driven Machine Learning-Informed Framework for Model Predictive Control in Vehicles"
Authors: "Edgar Amalyan, Shahram Latifi"
DOI: "https://doi.org/10.3390/info16060511"
Year: "2025"
Publication Type: "Journal"
Discipline/Domain: "Electrical and Computer Engineering / Automotive Control Systems"
Subdomain/Topic: "Hybrid Machine Learning–Model Predictive Control (ML–MPC) for vehicle subsystems"
Eligibility: "Eligible"
Overall Relevance Score: "90"
Operationalization Score: "88"
Contains Definition of Actionability: "Yes (explicitly in terms of “transforming ML outputs into actionable commands” for MPC)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes (MPC’s transparency offsets ML’s black-box nature)"
Contains Interpretability: "Yes (hybrid design enables interpreting ML outputs through MPC)"
Contains Framework/Model: "Yes (machine learning–informed MPC hybrid framework)"
Operationalization Present: "Yes (detailed multi-step workflow for training, inference, sliding-window smoothing, weighting, and integration with MPC)"
Primary Methodology: "Experimental + Conceptual Framework Development"
Study Context: "Performance vehicle suspension as primary subsystem case study; extensible to other systems like braking and traction"
Geographic/Institutional Context: "University of Nevada, Las Vegas, USA"
Target Users/Stakeholders: "Automotive engineers, control system designers, autonomous vehicle developers, performance vehicle tuners"
Primary Contribution Type: "Conceptual + Technical Framework with proof-of-concept implementation and evaluation"
Reason if Not Eligible: "n/a"
Domain Note: "[[Domain/Electrical and Computer Engineering / Automotive Control Systems]]"
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
# Data-Driven Machine Learning-Informed Framework for Model Predictive Control in Vehicles (2025)
*Edgar Amalyan, Shahram Latifi*
**DOI:** https://doi.org/10.3390/info16060511
**Domain:** [[Domain/Electrical and Computer Engineering / Automotive Control Systems]]
**Subdomain/Topic:** Hybrid Machine Learning–Model Predictive Control (ML–MPC) for vehicle subsystems

## General Summary of the Paper
The paper proposes and validates a machine learning–informed framework to enhance Model Predictive Control (MPC) in vehicles. Using a BMW M240i test platform, inertial data from accelerometers and gyroscopes were collected during controlled driving maneuvers. An XGBoost-based prototype classifier was trained on curated “seed” maneuver data, then used to pseudo-label a much larger “exemplar” dataset, enabling a robust inference model. The model classifies vehicle modes (e.g., braking, cornering) in real time with 97.6% accuracy. To ensure stability and responsiveness, predictions are processed using overlapping sliding windows and reverse exponential weighting. The paper details how such semantic mode predictions can feed into MPC systems for adaptive constraint tuning and control strategy updates. Applications span suspension adjustment, braking, traction, and energy management for conventional and autonomous vehicles.

## How Actionability is Understood
The authors explicitly define actionability as the transformation of ML outputs into real-world control actions via MPC, ensuring they are interpretable, safe, and optimally tuned for current vehicle conditions.  

  
“MPC in the hybrid approach translates ML outputs into actionable commands in the real world.” (p. 3)  

  
“By grading each subsystem’s real-world status and feeding those semantic modes into the optimizer, the approach generalizes effortlessly…” (p. 16)

## What Makes Something Actionable
Interpretability through MPC translating ML outputs into constraints and control commands  

Contextual relevance to current driving conditions  

Real-time responsiveness without destabilizing oscillations  

Feasibility for deployment on automotive ECUs  

Goal alignment with performance, safety, and comfort objectives

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): ML-informed MPC hybrid control framework  

Methods/Levers: Sensor fusion (accelerometer, gyroscope), XGBoost classification, pseudo-labeling, real-time inference pipeline  

Operational Steps / Workflow:  

 1. Collect curated “seed” maneuver data  

 2. Train prototype classifier  

 3. Pseudo-label large exemplar dataset  

 4. Train inference model  

 5. Real-time operation using overlapping sliding window + reverse exponential weighting  

 6. Feed mode predictions to MPC for constraint/parameter updates  

Data &amp; Measures: Six inertial features (GForceX/Y/Z, GyroX/Y/Z) with defined sign conventions and physical meaning  

Implementation Context: Performance suspension tuning case study; extensible to brakes, traction, energy  

  
“An overlapping sliding-window grading approach with reverse exponential weighting smooths transient fluctuations while preserving responsiveness.” (p. 1)  

  
“The controller can adjust its own internal constraints…based on the inferred driving mode.” (p. 16)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — ML outputs interpreted via MPC into explicit commands (p. 3)  

CR (Contextual Relevance): Yes — Predictions reflect real-time driving modes for adaptive control (p. 16)  

FE (Feasibility): Yes — Tested with latency measurements; hardware considerations discussed (p. 13, p. 17)  

TI (Timeliness): Yes — Sliding window + weighting ensures rapid yet stable response (p. 12)  

EX (Explainability): Yes — MPC’s rule-based transparency provides explainability (p. 3)  

GA (Goal Alignment): Yes — Constraints tuned for performance, safety, comfort (p. 16)  

Other Dimensions Named by Authors: Stability through constraint management; robustness to sensor anomalies

## Theoretical or Conceptual Foundations
Model Predictive Control theory (receding horizon optimization, constraints)  

Semi-supervised ML (pseudo-labeling)  

Feature importance metrics from gradient-boosted decision trees

## Indicators or Metrics for Actionability
Real-time classification accuracy (97.6%)  

Latency (~119 µs inference + 32 µs aggregation)  

F1-scores per maneuver class  

Confusion matrix diagonality (low cross-mode error)

## Barriers and Enablers to Actionability
Barriers:  

 - Mislabeling under-represented scenarios  

 - Trade-off between window size and responsiveness  

 - Computational load on ECUs  

 - Limited coverage of rare driving conditions in datasets  

Enablers:  

 - MPC’s safeguard role against erroneous ML outputs  

 - Modular adaptability across vehicle subsystems  

 - High accuracy and generalization via pseudo-labeling

## Relation to Existing Literature
Positions itself as a practical, data-driven integration of ML and MPC, leveraging MPC’s transparency to offset ML’s opaqueness while using ML’s predictive adaptability to overcome MPC’s reliance on static models. Builds on prior work in ML for automotive perception and MPC for control, adding a structured hybridization pipeline.

## Actionability-Focused Summary
This paper offers a complete methodology for making ML outputs actionable in automotive control through MPC integration. Actionability is explicitly framed as the transformation of predictive insights into interpretable, constraint-adjusted commands. The proposed pipeline—seed data collection, prototype classification, pseudo-labeling, inference model training, sliding-window smoothing, and reverse exponential weighting—ensures timely, context-relevant, and safe control adjustments. The authors test the system on suspension control in a performance vehicle, achieving high accuracy and low latency, and argue that the approach generalizes to other vehicle subsystems. The framework’s strength lies in its balance between predictive adaptability and rule-based transparency, enabling both human interpretability and machine responsiveness.

## Supporting Quotes from the Paper
“MPC…translates ML outputs into actionable commands in the real world.” (p. 3)  

“By grading each subsystem’s real-world status and feeding those semantic modes into the optimizer, the approach generalizes effortlessly…” (p. 16)  

“An overlapping sliding-window grading approach with reverse exponential weighting smooths transient fluctuations while preserving responsiveness.” (p. 1)  

“The controller can adjust its own internal constraints…based on the inferred driving mode.” (p. 16)

## Actionability References to Other Papers
Norouzi et al. (2023) — ML–MPC integration review  

Maiworm et al. (2021) — Online learning-based MPC with stability guarantees  

Goel et al. (2023) — Semantically informed MPC for context-aware control  

Ribeiro et al. (2016) — Explaining predictions of classifiers

---
