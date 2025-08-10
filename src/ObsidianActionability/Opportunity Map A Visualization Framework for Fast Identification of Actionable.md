---
Title: "Opportunity Map: A Visualization Framework for Fast Identification of Actionable Knowledge"
Authors: "Kaidi Zhao, Bing Liu, Thomas M. Tirpak, Weimin Xiao"
DOI: "10.1145/1099554.1099684"
Year: "2005"
Publication Type: "Conference"
Discipline/Domain: "Computer Science / Information Systems"
Subdomain/Topic: "Data Mining, Visualization, Actionable Knowledge Discovery"
Eligibility: "Eligible"
Overall Relevance Score: "88"
Operationalization Score: "90"
Contains Definition of Actionability: "Yes (implicit and explicit elements)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Partial"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes (Opportunity Map)"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual with applied case study"
Study Context: "Post-mining analysis of large rule sets from data mining to identify actionable patterns"
Geographic/Institutional Context: "University of Illinois at Chicago; Motorola Labs (USA)"
Target Users/Stakeholders: "Data analysts, product designers, decision-makers in industrial contexts"
Primary Contribution Type: "Visualization framework and interactive analysis method"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Computer Science / Information Systems]]"
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
# Opportunity Map: A Visualization Framework for Fast Identification of Actionable Knowledge (2005)
*Kaidi Zhao, Bing Liu, Thomas M. Tirpak, Weimin Xiao*
**DOI:** 10.1145/1099554.1099684
**Domain:** [[Domain/Computer Science / Information Systems]]
**Subdomain/Topic:** Data Mining, Visualization, Actionable Knowledge Discovery

## General Summary of the Paper
The paper proposes the Opportunity Map, a visual data mining framework designed to quickly identify actionable knowledge from large sets of discovered rules. Drawing inspiration from the “House of Quality” in Quality Function Deployment, the framework organizes rules into a matrix of attributes (technical requirements) vs. classes (customer requirements), sorted by importance and actionability. Key sectors highlight priority opportunities, with drill-down and comparative study capabilities. The method emphasizes post-mining analysis, enabling users to isolate actionable rules by visually exploring their statistical strength (support/confidence) and domain relevance. A Motorola case study demonstrates the system’s ability to identify design-change opportunities that were missed by traditional mining thresholds.

## How Actionability is Understood
Actionability is framed as the ability of a rule or pattern to guide concrete interventions within the user’s domain to achieve desired effects. Attributes are deemed “actionable” if the user can influence them in practice. The focus is on practical utility, not just statistical significance.

  
“An attribute is actionable if the user is able to do something with that attribute to achieve some desired effects.” (p. 4)  

  
“Actionability is the key… It depends on the task that the user wants to perform.” (p. 1)

## What Makes Something Actionable
The attribute must be controllable within the user’s context.

The class or problem addressed must be important to the user’s goals.

The relationship between attribute and class should be clear, strong (support/confidence), and interpretable.

Patterns must be applicable to real-world decision-making, not just surprising.

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): Opportunity Map  

Methods/Levers: Visual prioritization matrix; user-driven sorting by importance and actionability; drill-down visualizations; comparative studies.  

Operational Steps / Workflow:  

 1. Mine rules (e.g., with class association rule miner CBA).  

 2. Visualize as attribute–class matrix.  

 3. Arrange classes (by importance) and attributes (by actionability).  

 4. Focus on top-left priority sector (important + actionable).  

 5. Drill down into attribute–class pairs to find finer-grained actionable rules.  

 6. Compare rule sets across subsets (e.g., product versions).  

Data &amp; Measures: Support and confidence of rules; number of rules per cell; coverage of data points.  

Implementation Context: Post-mining analysis in industrial product design/failure diagnosis.  

  
“This isolates a small area in the matrix… that may contain actionable rules.” (p. 2)  

  
“The insights from these rules are immediately actionable, as engineers can… identify/propose possible design changes.” (p. 8)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — visualization aids interpretation and explicit linking of attributes to classes.  

CR (Contextual Relevance): Yes — prioritization is based on user/application importance.  

FE (Feasibility): Yes — actionable attributes are defined as those under user control.  

TI (Timeliness): Partial — focuses on efficiency in identification, but not time-to-implementation.  

EX (Explainability): Partial — interpretability via visualization; not formal model explainability.  

GA (Goal Alignment): Yes — prioritization matrix directly aligns with application objectives.  

Other Dimensions Named by Authors: Unexpectedness (as contrast with actionability).

## Theoretical or Conceptual Foundations
Quality Function Deployment (House of Quality)  

Rule interestingness measures (objective vs. subjective) from data mining literature

## Indicators or Metrics for Actionability
Support and confidence of rules in priority sectors  

Number of rules covering key attribute–class intersections  

Coverage percentage of rules over relevant data points

## Barriers and Enablers to Actionability
Barriers: Imbalanced datasets, non-actionable attributes, overwhelming number of rules  

Enablers: Visualization of priorities, interactive drill-down, comparative analysis

## Relation to Existing Literature
The framework integrates subjective interestingness with visual analytics, diverging from existing visualization techniques that focus on support/confidence alone. Unlike prior methods, it explicitly incorporates actionability as a guiding principle for sorting and interpreting mined rules.

## Actionability-Focused Summary
The Opportunity Map framework offers a systematic and interactive way to identify actionable knowledge from large rule sets. By mapping attributes against classes and sorting them by user-defined importance and actionability, it isolates the most promising opportunities for intervention. It extends concepts from Quality Function Deployment to data mining, using cell-level visualization to show rule strength and coverage, and supports comparative analysis to uncover performance differences between products or scenarios. The Motorola case study illustrates how it can reveal design insights that traditional rule mining misses due to statistical thresholds. This makes it both a conceptual contribution to defining actionability and a practical tool for operationalizing it.

## Supporting Quotes from the Paper
“Actionability is the key… It depends on the task that the user wants to perform.” (p. 1)  

“An attribute is actionable if the user is able to do something with that attribute to achieve some desired effects.” (p. 4)  

“This isolates a small area in the matrix… that may contain actionable rules.” (p. 2)  

“The insights from these rules are immediately actionable…” (p. 8)

## Actionability References to Other Papers
[1] Adomavicius &amp; Tuzhilin (1997) — Action hierarchy approach.  

[17] Liu et al. (2001) — Identifying non-actionable association rules.  

[22] Piatesky-Shapiro &amp; Matheus (1994) — Interestingness of deviations.  

[26] Silberschatz &amp; Tuzhilin (1996) — Patterns interestingness framework.

---
