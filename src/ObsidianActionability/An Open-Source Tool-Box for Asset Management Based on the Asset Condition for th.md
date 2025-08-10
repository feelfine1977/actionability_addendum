---
Title: "An Open-Source Tool-Box for Asset Management Based on the Asset Condition for the Power System"
Authors: "Gopal Lal Rajora, Miguel A. Sanz-Bobi, Carlos Mateo Domingo, Lina Bertling Tjernberg"
DOI: "10.1109/ACCESS.2025.3551663"
Year: "2025"
Publication Type: "Journal"
Discipline/Domain: "Electrical Engineering / Power Systems"
Subdomain/Topic: "Asset Management, Predictive Maintenance, Machine Learning for Power Grids"
Eligibility: "Eligible"
Overall Relevance Score: "90"
Operationalization Score: "95"
Contains Definition of Actionability: "Yes (implicit and explicit operational framing)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Partial"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual + Quantitative Case Study"
Study Context: "European ATTEST project; predictive maintenance for TSOs and DSOs"
Geographic/Institutional Context: "Spain (Universidad Pontificia Comillas), Sweden (KTH), European partners"
Target Users/Stakeholders: "Transmission System Operators (TSOs), Distribution System Operators (DSOs)"
Primary Contribution Type: "Framework + Open-source Tool"
Reason if Not Eligible: "n/a"
Domain Note: "[[Domain/Electrical Engineering / Power Systems]]"
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
# An Open-Source Tool-Box for Asset Management Based on the Asset Condition for the Power System (2025)
*Gopal Lal Rajora, Miguel A. Sanz-Bobi, Carlos Mateo Domingo, Lina Bertling Tjernberg*
**DOI:** 10.1109/ACCESS.2025.3551663
**Domain:** [[Domain/Electrical Engineering / Power Systems]]
**Subdomain/Topic:** Asset Management, Predictive Maintenance, Machine Learning for Power Grids

## General Summary of the Paper
The paper introduces an open-source asset management toolbox designed for TSOs and DSOs, integrating machine learning, clustering, and reinforcement learning to assess and optimize asset maintenance strategies. The method is structured into three modules: (1) characterization of asset health using multi-dimensional data (life assessment, health condition, maintenance, economic impact), (2) derivation of condition indicators from heterogeneous data, and (3) strategy recommendation via reinforcement learning (Q-learning). The toolbox enables proactive maintenance planning, resource optimization, and lifecycle extension. Case studies using 92 real-world transformers and synthetic datasets validate scalability and practical applicability. The system aligns with sustainable energy goals by improving grid reliability and operational efficiency.

## How Actionability is Understood
The paper explicitly links “actionable insights” to the ability to inform prioritized, effective maintenance strategies based on asset condition data. Actionability is defined through the generation of condition indicators and strategic recommendations that operators can directly implement.  

  
“The toolbox provides actionable insights for planning maintenance strategies and optimizing resource allocation.” (Abstract)  

  
“Each asset’s condition is evaluated… facilitating effective prioritization and decision-making for maintenance and management strategies.” (p. 6)

## What Makes Something Actionable
Measurable condition indicators across four dimensions: Life Assessment, Health Condition, Maintenance, Economic Impact.

Ability to compare across heterogeneous assets.

Prioritization thresholds for intervention.

Integration of predictive analytics (clustering + SOM) for early identification of risks.

Strategy recommendation system (Q-learning) that adapts to changes without manual rule rewriting.

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): ATTEST Asset Management Toolbox  

Methods/Levers: Data normalization, clustering (K-means, SOM), condition indicator computation, reinforcement learning for decision support.  

Operational Steps / Workflow:  

 1. Identify critical asset data.  

 2. Compute multi-dimensional condition indicators.  

 3. Cluster assets for pattern recognition.  

 4. Apply Q-learning to recommend optimal actions.  

 5. Simulate long-term strategies (Monte Carlo).  

Data &amp; Measures: Asset age, failure probability, internal temperature, dissolved gas analysis, MTTR, MTBF, maintenance costs, undelivered energy.  

Implementation Context: Tested on European TSO/DSO datasets; compatible with CIM, IEC 61850, MATPOWER formats.  

  
“This Module compares assets… recommending the most convenient actions… simulate and quantify the evolution… under different management strategies.” (p. 6–7)  

  
“The Q-learning algorithm… suggests actions with the highest potential reward.” (p. 8)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — Explicit, interpretable indicators for each dimension.  

 &gt; “Comparable condition indicators… allowing identification of assets requiring special attention.”  

CR (Contextual Relevance): Yes — Indicators adaptable to available data and operational context.  

FE (Feasibility): Yes — Prioritized strategies feasible given operational constraints.  

TI (Timeliness): Yes — Short-term and long-term analyses inform timely interventions.  

EX (Explainability): Partial — While results are interpretable, underlying ML models’ inner workings are not deeply unpacked.  

GA (Goal Alignment): Yes — Optimizes for reliability, cost-efficiency, and sustainability goals.  

Other Dimensions: Adaptability (tool modularity and format compatibility).

## Theoretical or Conceptual Foundations
Condition-based maintenance theory.

AI/ML for predictive asset management.

Reinforcement learning (Q-learning) for adaptive strategy optimization.

Multi-criteria decision analysis.

## Indicators or Metrics for Actionability
Multi-dimensional condition indicators (0–1 scale).

Total Indicator threshold (e.g., &gt;0.75 for critical attention).

Cluster patterns denoting asset health states.

## Barriers and Enablers to Actionability
Barriers: Data incompleteness, heterogeneity of formats, variability in monitoring availability.  

Enablers: Open-source modular design, integration with industry standards, compatibility with multiple data formats.

## Relation to Existing Literature
Positions itself as advancing AI-driven asset management from descriptive analytics to prescriptive decision-making, integrating clustering and RL for operational use.

## Actionability-Focused Summary
The paper offers a comprehensive, modular, open-source framework for transforming raw asset condition data into actionable maintenance and management strategies for power systems. Actionability here is operationalized as the process of quantifying multi-dimensional condition indicators, clustering similar assets for pattern recognition, and recommending specific interventions via reinforcement learning. The approach is designed to be adaptable to diverse data sources, scalable across network sizes, and integrable into existing operational platforms. This combination of predictive assessment and prescriptive recommendation directly supports timely, relevant, feasible, and goal-aligned decision-making for TSOs and DSOs, making the contribution both conceptually strong and practically implementable.

## Supporting Quotes from the Paper
“The toolbox provides actionable insights for planning maintenance strategies and optimizing resource allocation.” (Abstract)  

“Comparable condition indicators… allowing identification of assets requiring special attention.” (p. 6)  

“Optimal actions are determined using a Q-matrix… suggests actions with the highest potential reward.” (p. 7–8)  

“Assets are categorized as requiring priority attention and maintenance when the Total Indicator is nearly or exactly equal to one.” (p. 6)

## Actionability References to Other Papers
Rajora et al. (2024) — AI-based ML models for asset management.  

Žarković et al. (2021) — ML for transformer diagnostics.  

Li et al. (2023) — ML + blockchain in power management.  

Aminifar et al. (2022) — ML for asset management and protection.

---
