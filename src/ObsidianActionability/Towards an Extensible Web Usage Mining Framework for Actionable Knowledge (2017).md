---
Title: "Towards an Extensible Web Usage Mining Framework for Actionable Knowledge"
Authors: "N. Pushpalatha, S. Sai Satyanarayana Reddy"
DOI: "n/a"
Year: "2017"
Publication Type: "Conference Paper"
Discipline/Domain: "Computer Science / Data Mining"
Subdomain/Topic: "Web Usage Mining, Actionable Knowledge, Fuzzy Clustering"
Eligibility: "Eligible"
Overall Relevance Score: "78"
Operationalization Score: "82"
Contains Definition of Actionability: "Implicit"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Partial"
Contains Interpretability: "Partial"
Contains Framework/Model: "Yes (XWUMF)"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual + Experimental (Prototype implementation)"
Study Context: "Web log analysis for user behaviour and business intelligence"
Geographic/Institutional Context: "India (JNTU Hyderabad, Vardhaman College of Engineering)"
Target Users/Stakeholders: "Businesses, Web Analysts, Decision-Makers"
Primary Contribution Type: "Framework and Algorithm Proposal (XWUMF, SWUM)"
Reason if Not Eligible: "n/a"
Domain Note: "[[Domain/Computer Science / Data Mining]]"
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
# Towards an Extensible Web Usage Mining Framework for Actionable Knowledge (2017)
*N. Pushpalatha, S. Sai Satyanarayana Reddy*
**DOI:** n/a
**Domain:** [[Domain/Computer Science / Data Mining]]
**Subdomain/Topic:** Web Usage Mining, Actionable Knowledge, Fuzzy Clustering

## General Summary of the Paper
The paper introduces the eXtensible Web Usage Mining Framework (XWUMF) designed to process web log data using a hybrid approach of fuzzy clustering and user behaviour analysis. This extensible architecture accommodates new algorithms and supports personalized analysis settings. A core contribution is the Sequential Web Usage Miner (SWUM) algorithm, which identifies user patterns from sequential web logs using minimum time and minimum confidence thresholds. The prototype implementation demonstrated the ability to extract patterns that, when interpreted by domain experts, yield actionable knowledge for businesses. Empirical results from four datasets (one real, three synthetic) highlight the framework’s efficiency in execution time and memory usage.

## How Actionability is Understood
The authors implicitly define actionability as the transformation of web usage patterns into “business intelligence” that supports expert decision-making and improves customer-centric strategies.

  
“The patterns when interpreted by domain experts can result in business intelligence.” (p. 1)  

  
“Our empirical results revealed that the framework helps in discovering actionable knowledge.” (p. 1)

## What Makes Something Actionable
Derives from meaningful usage patterns that reflect actual user behaviour.  

Must be interpretable by domain experts to support decision-making.  

Should enable customer-centric strategies in competitive environments.  

Requires quality thresholds (MinTime, MinConfidence) to ensure reliability of patterns.

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): XWUMF (eXtensible Web Usage Mining Framework)  

Methods/Levers: Hybrid fuzzy clustering + user behaviour analysis; sequential mining with quality thresholds.  

Operational Steps / Workflow: Pre-processing → Fuzzy clustering → Usage mining → Pattern discovery → Pattern analysis → Business intelligence.  

Data &amp; Measures: Execution time, memory usage; MinTime and MinConfidence thresholds.  

Implementation Context: Tested on WDC dataset + 3 synthetic datasets.  

  
“The framework supports a hybrid approach which can have fuzzy clustering techniques and web mining techniques working together…” (p. 2)  

  
“Sequential Web Usage Miner… generates patterns that reflect user behaviour.” (p. 3)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes – Patterns must be interpretable by domain experts.  

CR (Contextual Relevance): Yes – Patterns tied to customer behaviour for strategic business use.  

FE (Feasibility): Yes – Extensible design allows integration of algorithms suitable for different domains.  

TI (Timeliness): Partial – Execution time evaluated, but real-time capability not central.  

EX (Explainability): Partial – Domain expert interpretation required; not fully automated explainability.  

GA (Goal Alignment): Yes – Focused on customer-centric business intelligence.  

Other Dimensions Named by Authors: Extensibility, personalization, performance efficiency.

## Theoretical or Conceptual Foundations
Business intelligence theory (data-to-decision processes)  

Web usage mining and fuzzy logic principles

## Indicators or Metrics for Actionability
Execution time  

Memory usage  

Minimum time threshold (MinTime)  

Minimum confidence threshold (MinConfidence)

## Barriers and Enablers to Actionability
Barriers: Domain dependence for interpretation; quality of raw web logs; computational constraints.  

Enablers: Extensible framework; hybrid methodology; performance tuning via parameters.

## Relation to Existing Literature
The authors situate their work in the context of prior research in fuzzy logic, neural networks, case-based reasoning, and semantic web mining, noting that most approaches are domain-specific and lack extensibility for future technologies.

## Actionability-Focused Summary
Pushpalatha and Reddy (2017) propose XWUMF, an extensible, hybrid framework for mining actionable knowledge from web usage logs. Actionability is understood as the extraction of patterns that can be interpreted by domain experts to produce customer-centric business intelligence. The Sequential Web Usage Miner algorithm operationalizes actionability by filtering and validating patterns based on statistical thresholds. Evaluated through execution time and memory usage on multiple datasets, the framework is positioned as adaptable, scalable, and domain-agnostic, with the potential to support strategic decision-making across sectors.

## Supporting Quotes from the Paper
“The patterns when interpreted by domain experts can result in business intelligence.” (p. 1)  

“The framework supports a hybrid approach which can have fuzzy clustering techniques and web mining techniques working together…” (p. 2)  

“Sequential Web Usage Miner… generates patterns that reflect user behaviour.” (p. 3)  

“Our empirical results revealed that the framework helps in discovering actionable knowledge.” (p. 1)

## Actionability References to Other Papers
Lin &amp; Hong (2013) – Fuzzy web mining survey  

He (2013) – Case-based reasoning + text mining for UX improvement  

Abello et al. (2015) – Semantic web for OLAP exploration

---
