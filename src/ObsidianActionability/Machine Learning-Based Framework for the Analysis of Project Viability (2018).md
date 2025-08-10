---
Title: "Machine Learning-Based Framework for the Analysis of Project Viability"
Authors: "Jean Marie Tshimula, Atsushi Togashi"
DOI: "10.1109/CCOMS.2018.8463273"
Year: "2018"
Publication Type: "Conference"
Discipline/Domain: "Data Science / Development Economics"
Subdomain/Topic: "Machine Learning for Investment Decision Support in African Development Projects"
Eligibility: "Eligible"
Overall Relevance Score: "82"
Operationalization Score: "90"
Contains Definition of Actionability: "Yes (implicit)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Partial"
Contains Interpretability: "No"
Contains Framework/Model: "Yes"
Operationalization Present: "Yes"
Primary Methodology: "Mixed Methods (Data Mining, Machine Learning, Topic Modeling)"
Study Context: "African Development Bank (AfDB) project portfolio analysis for investment guidance"
Geographic/Institutional Context: "Africa / AfDB (headquartered in Côte d’Ivoire)"
Target Users/Stakeholders: "Investors, policy makers, AfDB analysts"
Primary Contribution Type: "Machine Learning workflow for actionable investment guidance"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Data Science / Development Economics]]"
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
# Machine Learning-Based Framework for the Analysis of Project Viability (2018)
*Jean Marie Tshimula, Atsushi Togashi*
**DOI:** 10.1109/CCOMS.2018.8463273
**Domain:** [[Domain/Data Science / Development Economics]]
**Subdomain/Topic:** Machine Learning for Investment Decision Support in African Development Projects

## General Summary of the Paper
The paper presents a machine learning framework designed to process and analyze AfDB project data, converting it into actionable investment insights. The framework automates data collection via a custom R package, structures the data in MongoDB, and uses Random Forests to classify promising sectors and LDA to extract thematic investment opportunities from project descriptions. Results highlight seven key sectors aligned with AfDB’s “High Five” priorities, with agriculture emerging as the most promising. The system is intended to help investors identify viable projects and reduce decision-making risks.

## How Actionability is Understood
Actionability is implicitly understood as the ability of the analytical framework to transform raw project data into clear, sector-specific investment guidance that helps stakeholders make informed decisions about where to allocate resources.  

  
“…transforming the project data…into actionable insights and…giving investment directions to follow based on the promising sectors.” (p. 1)  

  
“…generate the knowledge required for orienting people…willing to know more details…with insightful guidance.” (p. 2)

## What Makes Something Actionable
Connection to AfDB’s strategic “High Five” priorities  

Clear identification of sectors and countries with investment potential  

Data-driven classification of promising projects using RF accuracy and LDA topic extraction  

Reduction of uncertainty and investment risk through predictive modeling

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): Machine Learning-Based Workflow (AfDB investment analysis)  

Methods/Levers: Web scraping (afdbr R package), MongoDB storage, Random Forests, LDA topic modeling  

Operational Steps / Workflow: Data extraction → Structured storage → Data cleaning &amp; translation → RF classification → LDA topic extraction → Sector prioritization  

Data &amp; Measures: Project descriptions, status, sector, elapsed time, reappraisal status  

Implementation Context: AfDB project portfolio  

  
“…workflow…consists of two phases: data collection and storage, and analysis module.” (p. 2)  

  
“…built a model with 100 trees…then built an LDA model to outline the data with 20 topics.” (p. 4)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — Clear sector classification and thematic topic identification aid understanding.  

CR (Contextual Relevance): Yes — Links directly to AfDB’s High Five priorities and African market trends.  

FE (Feasibility): Yes — Uses existing AfDB data and scalable ML methods.  

TI (Timeliness): No explicit reference.  

EX (Explainability): Partial — RF feature importance is used, but model interpretability is not deeply addressed.  

GA (Goal Alignment): Yes — Explicitly tied to AfDB’s strategic priorities.  

Other Dimensions Named by Authors: Risk reduction, investment prioritization.

## Theoretical or Conceptual Foundations
AfDB High Five priorities  

Random Forest classification theory (Breiman, 2001)  

LDA topic modeling (Blei et al., 2003)

## Indicators or Metrics for Actionability
RF classification accuracy (99.8%)  

Identification of top 7 sectors for investment  

Topic frequency and relevance to strategic priorities

## Barriers and Enablers to Actionability
Barriers: Missing project descriptions (7.1%), language inconsistencies requiring translation  

Enablers: Comprehensive AfDB dataset, automated continuous data scraping, alignment with strategic priorities

## Relation to Existing Literature
Positions itself as extending previous AfDB project evaluation models (e.g., Mubila et al. 2002) by focusing on ongoing and pipeline projects rather than completed ones, and by providing predictive and thematic insights rather than retrospective success factors.

## Actionability-Focused Summary
This paper develops and demonstrates a machine learning-based workflow to make AfDB project data actionable for investment decision-making. Actionability is conceptualized as the capacity to transform semi-structured development project data into clear, sector-specific, and risk-informed investment guidance. The approach operationalizes this via automated data extraction, structured storage, Random Forest classification of promising sectors, and LDA-based extraction of thematic opportunities, aligning outputs with AfDB’s High Five strategic priorities. The model achieves high classification accuracy and identifies agriculture as a flagship sector, alongside six other high-potential sectors. The framework serves as a replicable decision-support tool for investors and policy makers.

## Supporting Quotes from the Paper
“Transforming the project data…into actionable insights and…giving investment directions to follow based on the promising sectors.” (p. 1)  

“…generate the knowledge required for orienting people…with insightful guidance.” (p. 2)  

“…built a model with 100 trees…then built an LDA model to outline the data with 20 topics.” (p. 4)

## Actionability References to Other Papers
Mubila &amp; Lufumpa (2002) — Statistical model for project success factors  

Blei et al. (2003) — LDA model  

Breiman (2001) — Random Forests

---
