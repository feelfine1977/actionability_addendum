---
Title: "Development of Actionable Insights for Regulating Students’ Collaborative Writing of Scientific Texts"
Authors: "Christian Hoffmann, Nadine Mandran, Cédric d’Ham, Sébastien Rebaudo, Mohamed Anis Haddouche"
DOI: "https://doi.org/10.1007/978-3-031-16290-9_47"
Year: "2022"
Publication Type: "Conference Paper"
Discipline/Domain: "Learning Analytics / Educational Technology"
Subdomain/Topic: "Collaborative Writing, Teacher Dashboards, Educational Collaboration Analytics"
Eligibility: "Eligible"
Overall Relevance Score: "82"
Operationalization Score: "90"
Contains Definition of Actionability: "Yes (via Jørnø &amp; Gynther, 2018 and Martinez-Maldonado et al., 2021)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Partial"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes (Mapping “From Clicks to Constructs”)"
Operationalization Present: "Yes"
Primary Methodology: "Design-Based Research (Iterative User-Centered Design)"
Study Context: "Web-based science learning environment (LabNbook) for collaborative writing of scientific texts"
Geographic/Institutional Context: "Univ. Grenoble Alpes (France), IMT Atlantique (France)"
Target Users/Stakeholders: "Teachers in secondary and higher education"
Primary Contribution Type: "Indicators and visualizations for actionable insights in collaborative writing"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Learning Analytics / Educational Technology]]"
Feature Notes:
  - "[[Concept/CL - Clarity (Actionability)]]"
  - "[[Concept/CR - Contextual Relevance (Actionability)]]"
  - "[[Concept/EX - Explainability (Actionability)]]"
tags:
  - "feature/cl"
  - "feature/cr"
  - "feature/ex"
---
# Development of Actionable Insights for Regulating Students’ Collaborative Writing of Scientific Texts (2022)
*Christian Hoffmann, Nadine Mandran, Cédric d’Ham, Sébastien Rebaudo, Mohamed Anis Haddouche*
**DOI:** https://doi.org/10.1007/978-3-031-16290-9_47
**Domain:** [[Domain/Learning Analytics / Educational Technology]]
**Subdomain/Topic:** Collaborative Writing, Teacher Dashboards, Educational Collaboration Analytics

## General Summary of the Paper
The paper develops a set of computationally calculable indicators and visualizations to provide teachers with actionable insights for regulating students’ collaborative writing of scientific texts in the LabNbook online platform. Drawing from collaboration analytics theory and CSCW concepts, the authors define two key educational sub-constructs—symmetry in action and territorial functioning—and map them from raw data traces to teacher-facing dashboard elements. Using a design-based research approach, the team iterated through indicator and visualization design with teacher input. The resulting system allows teachers to distinguish between summative and integrative writing strategies and better assess collaboration dynamics. Lessons learned stress the importance of simplicity, iterative design, multiple complementary indicators, and ensuring teacher understanding.

## How Actionability is Understood
Actionable insights are defined (via Jørnø &amp; Gynther, 2018) as “data that allows a corrective procedure, or feedback loop, established for a set of actions.” Martinez-Maldonado et al. (2021) frame actionability as mapping low-level data to educationally meaningful higher-order constructs interpretable by educators.

  
“The challenge for designers of LADs is to provide teachers with actionable group insights defined… as ‘data that allows a corrective procedure, or feedback loop…’” (p. 535)  

  
“They emphasize the role of a clear ‘mapping from low-level data to higher-order constructs…’” (p. 535)

## What Makes Something Actionable
Clear mapping from trace data to meaningful educational constructs  

Relevance to teacher goals (e.g., assessing collaboration strategies)  

Understandable by the intended user (teacher)  

Presented in a way that supports immediate pedagogical decisions

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): Mapping “From Clicks to Constructs”  

Methods/Levers: Use of educational sub-constructs (symmetry in action, territorial functioning) derived from CSCW research  

Operational Steps / Workflow:  

 1. Collect authorship, timestamp, and version data  

 2. Calculate indicators (turn taking, writing time, contribution scores, cowriting score)  

 3. Visualize indicators in teacher-friendly timelines and panels  

 4. Teachers interpret in context to diagnose collaboration strategy  

Data &amp; Measures: Words added (difflib), editor changes, sentence-level overlap detection  

Implementation Context: LabNbook platform in science education  

  
“Our analytics are based on… symmetry in action and territorial functioning… translated… into computationally calculable indicators.” (p. 537)  

  
“Visualization… allows a teacher to get a wealth of information about how the report was co-constructed…” (p. 539)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — Simplicity and clear indicator definitions stressed (p. 540)  

CR (Contextual Relevance): Yes — Indicators tied directly to collaborative writing processes (p. 535)  

FE (Feasibility): No explicit link  

TI (Timeliness): No explicit link  

EX (Explainability): Partial — Mapping framework provides interpretability, but some computational steps abstracted from teachers (p. 537)  

GA (Goal Alignment): No explicit link  

Other Dimensions Named by Authors: Complementarity of indicators, avoidance of aggregation

## Theoretical or Conceptual Foundations
Jørnø &amp; Gynther’s definition of actionable insights  

Martinez-Maldonado et al.’s collaboration analytics model (five-step mapping)  

CSCW constructs: symmetry in action (Dillenbourg, 1999), territorial functioning (Larsen-Ledet &amp; Korsgaard, 2019)

## Indicators or Metrics for Actionability
Turn taking (number of editor changes)  

Writing time (active editing time in 30s windows)  

Contribution scores (words added)  

Cowriting score (percentage of sentences modified by multiple authors)

## Barriers and Enablers to Actionability
Barriers: Over-aggregation of indicators, complex visualizations reducing interpretability  

Enablers: Iterative teacher feedback, complementary indicators, simple visualizations, on-demand details

## Relation to Existing Literature
Builds on CSCW collaborative writing strategy distinctions (summative vs integrative), extends Martinez-Maldonado’s mapping model to sentence-level analytics, adapts actionability concepts to science education OLEs.

## Actionability-Focused Summary
The authors present a design-based research approach to developing actionable insights for regulating students’ collaborative writing of scientific texts. Using the LabNbook OLE, they operationalize CSCW concepts—symmetry in action and territorial functioning—into computational indicators such as turn taking, writing time, contribution scores, and cowriting percentage. These are visualized in a teacher dashboard, allowing quick assessment of collaboration strategies (summative vs integrative) and team dynamics. Actionability is understood as data enabling corrective pedagogical actions, achieved through clear mappings from trace data to educationally meaningful constructs. Iterative co-design with teachers informed indicator choice, visualization style, and usability considerations. The work contributes a replicable mapping framework and concrete, transferable dashboard elements.

## Supporting Quotes from the Paper
“[Actionable insights]… ‘data that allows a corrective procedure, or feedback loop…’” (p. 535)  

“They emphasize the role of a clear ‘mapping from low-level data to higher-order constructs…’” (p. 535)  

“Our analytics are based on… symmetry in action and territorial functioning…” (p. 537)  

“Visualization… allows a teacher to get a wealth of information about how the report was co-constructed…” (p. 539)

## Actionability References to Other Papers
Jørnø &amp; Gynther (2018) — Definition of actionable insights  

Martinez-Maldonado et al. (2021) — Collaboration analytics model  

Dillenbourg (1999) — Symmetry in action  

Larsen-Ledet &amp; Korsgaard (2019) — Territorial functioning in collaborative writing

---
