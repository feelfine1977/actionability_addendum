---
Title: "YarnSense: Automated Data Storytelling for Multimodal Learning Analytics"
Authors: "Gloria Milena Fernández-Nieto, Vanessa Echeverria, Roberto Martinez-Maldonado, Simon Buckingham Shum"
DOI: "N/A"
Year: "2024"
Publication Type: "Conference (Workshop Proceedings)"
Discipline/Domain: "Learning Analytics / Educational Technology"
Subdomain/Topic: "Automated Data Storytelling, Multimodal Learning Analytics, Nursing Simulation Training"
Eligibility: "Eligible"
Overall Relevance Score: "88"
Operationalization Score: "90"
Contains Definition of Actionability: "Yes (implicit)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual + Reference Implementation"
Study Context: "Clinical nursing simulation with 254 students, 6 teachers"
Geographic/Institutional Context: "Monash University (Australia), University of Technology Sydney, Escuela Superior Politecnica del Litoral (Ecuador)"
Target Users/Stakeholders: "Students, Teachers, Researchers in education/training"
Primary Contribution Type: "Architecture &amp; System Implementation"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Learning Analytics / Educational Technology]]"
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
# YarnSense: Automated Data Storytelling for Multimodal Learning Analytics (2024)
*Gloria Milena Fernández-Nieto, Vanessa Echeverria, Roberto Martinez-Maldonado, Simon Buckingham Shum*
**DOI:** N/A
**Domain:** [[Domain/Learning Analytics / Educational Technology]]
**Subdomain/Topic:** Automated Data Storytelling, Multimodal Learning Analytics, Nursing Simulation Training

## General Summary of the Paper
The authors present YarnSense, a multi-tier architecture for automatically generating educational data stories from multimodal behavioural data collected via wearable and environmental sensors, combined with teacher-defined pedagogical intentions. The aim is to transform raw sensor data into contextualised, interpretable, and pedagogically aligned narratives for student reflection. The architecture consists of: (1) a context modeller for teachers to define learning activities and assessment criteria; (2) a multimodal sensor data capture system; (3) multimodal modelling to generate learner models; and (4) a data storytelling generator combining visualisations and narratives. The system is demonstrated in large-scale nursing simulations with 254 students, producing automated feedback on errors and teamwork patterns. The paper discusses design considerations, alignment with learning theories, and potential future enhancements including LLM-based narrative generation.

## How Actionability is Understood
Actionability is framed implicitly as the ability of multimodal data outputs to support reflection, identify performance gaps, and align with pedagogical intentions so students can meaningfully improve.

  
“Based on the notion of data storytelling as a means of extracting actionable insights from data…” (Abstract)  

  
“…weaving complex data into coherent narratives that align with the teacher’s pedagogical intentions” (p. 9)

## What Makes Something Actionable
Alignment with teacher’s pedagogical intentions and learning design

Translation of raw sensor data into meaningful constructs

Integration of contextual knowledge (roles, resources, assessment criteria)

Clear visual and narrative presentation to non-experts

Timely delivery to support post-activity reflection

Inclusion of error detection and performance feedback linked to guidelines

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): YarnSense Architecture  

Methods/Levers: Pedagogical rule definition, sensor-based multimodal data capture, QE modelling, automated narrative &amp; visual generation  

Operational Steps / Workflow:  

 1. Teachers define learning context &amp; pedagogical intentions (Context Modeller)  

 2. Collect multimodal data from machine and human sensing  

 3. Transform into learner models via multimodal matrices and QE modelling  

 4. Generate DS outputs combining data, visuals, and teacher feedback  

Data &amp; Measures: Positioning data, physiological data, audio/video, logged actions  

Implementation Context: Nursing simulations with defined critical actions and teamwork assessment  

  
“Data from the Learner Model are visualised and combined with narratives to convey a story for an individual student or a team.” (p. 6)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — DS principles include removing unnecessary elements, highlighting important features  

CR (Contextual Relevance): Yes — tied to pedagogical intentions and activity specifics  

FE (Feasibility): Yes — aligned with realistic instructional and technological constraints  

TI (Timeliness): Yes — aimed at post-activity debriefs in near-real time  

EX (Explainability): Yes — multimodal constructs and DS enhance interpretability  

GA (Goal Alignment): Yes — narratives tied directly to teacher’s learning goals  

Other Dimensions Named by Authors: User agency in modifying rules; integration with teacher feedback loops

## Theoretical or Conceptual Foundations
Data Storytelling principles (purposeful communication, meaningful visuals, narrative structures)

Quantitative Ethnography (QE)  

Multimodal Matrix methodology  

Theory of Proxemics for spatial interaction analysis

## Indicators or Metrics for Actionability
Error detection types (Sequence, Timeliness, Frequency)

Time spent in proximity to patients or team members

Adherence to clinical guideline-timed actions

## Barriers and Enablers to Actionability
Barriers: Complexity of multimodal data; automation challenges for certain modalities; need for context-specific adaptation  

Enablers: Teacher-defined rules; automated DS generation; integration of multiple sensing modalities; near-real-time feedback

## Relation to Existing Literature
Builds on prior work in multimodal learning analytics and DS, extending from high-fidelity prototypes to fully automated, large-scale implementations. Addresses gaps in automation and pedagogical alignment.

## Actionability-Focused Summary
YarnSense operationalises actionability in educational analytics as the transformation of raw multimodal sensor data into timely, clear, pedagogically aligned data stories that facilitate reflection and performance improvement. By integrating teacher-defined assessment criteria with automated multimodal modelling and narrative visualisation, it ensures contextual relevance, clarity, and goal alignment. Its reference implementation in nursing simulations demonstrates scalability and adaptability, detecting clinically relevant errors and visualising teamwork dynamics in a form that is understandable to students and instructors. The architecture’s modular design supports user agency, explainability, and adaptability across contexts, positioning it as a robust model for automated, actionable learning analytics.

## Supporting Quotes from the Paper
“[...] based on the notion of data storytelling as a means of extracting actionable insights from data…” (Abstract)  

“... weaving complex data into coherent narratives that align with the teacher’s pedagogical intentions” (p. 9)  

“Data from the Learner Model are visualised and combined with narratives to convey a story for an individual student or a team.” (p. 6)

## Actionability References to Other Papers
Martinez-Maldonado et al. (2020) — Layered storytelling approach for multimodal learning analytics  

Echeverria et al. (2018) — Educational data storytelling for teacher attention  

Fernández-Nieto et al. (2022) — Combining visualisation, narrative, and storytelling for student data insights
