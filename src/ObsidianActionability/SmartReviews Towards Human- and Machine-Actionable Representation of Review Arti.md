---
Title: "SmartReviews: Towards Human- and Machine-Actionable Representation of Review Articles"
Authors: "Allard Oelen, Markus Stocker, Sören Auer"
DOI: "https://doi.org/10.1007/978-3-030-91669-5_9"
Year: "2021"
Publication Type: "Conference"
Discipline/Domain: "Information Science / Digital Libraries"
Subdomain/Topic: "Semantic Publishing, Scholarly Knowledge Graphs, Review Article Authoring"
Eligibility: "Eligible"
Overall Relevance Score: "90"
Operationalization Score: "95"
Contains Definition of Actionability: "Yes (implicit via functional characteristics)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Partial"
Contains Interpretability: "Partial"
Contains Framework/Model: "Yes"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual with Implementation and Use Case Demonstration"
Study Context: "Scholarly review article authoring and publishing"
Geographic/Institutional Context: "L3S Research Center &amp; TIB Leibniz Information Centre, Germany"
Target Users/Stakeholders: "Academic authors, publishers, research communities, digital library developers"
Primary Contribution Type: "Conceptual framework and software tool implementation"
Reason if Not Eligible: "n/a"
Domain Note: "[[Domain/Information Science / Digital Libraries]]"
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
# SmartReviews: Towards Human- and Machine-Actionable Representation of Review Articles (2021)
*Allard Oelen, Markus Stocker, Sören Auer*
**DOI:** https://doi.org/10.1007/978-3-030-91669-5_9
**Domain:** [[Domain/Information Science / Digital Libraries]]
**Subdomain/Topic:** Semantic Publishing, Scholarly Knowledge Graphs, Review Article Authoring

## General Summary of the Paper
This paper presents SmartReviews, a new authoring and publishing framework for scholarly review articles that are both human- and machine-actionable. Built upon the Open Research Knowledge Graph (ORKG), SmartReviews address key weaknesses of current reviews: lack of updates, limited collaboration, restricted coverage, poor machine-actionability, accessibility issues, and weak systematic representation. The approach involves representing review content in a structured, semantic format, using comparison tables, ontologies, and linked data principles to enhance interoperability and FAIR compliance. A fully implemented tool, supporting community-based authoring and updating of living documents, is demonstrated through a use case on scholarly knowledge graphs. The evaluation shows that SmartReviews improve accessibility, interoperability, and reusability compared to traditional PDF-based reviews.

## How Actionability is Understood
Actionability here is framed in terms of both human and machine use: a review is actionable if it can be updated dynamically, collaboratively maintained, systematically represented, and queried or processed by machines via semantic web standards.  

  
“The key limitation is the inability of machines to access and process knowledge presented within review articles.” (p. 105)  

  
“The use of these technologies improves the machine-actionability of data and provides a means to make data FAIR.” (p. 107)

## What Makes Something Actionable
Updatable (living document concept with version control)

Collaboratively authored (community-based contributions with provenance tracking)

Structured &amp; semantic representation (linked data, ontologies, RDF)

Accessible (HTML format, WCAG compliance)

Interoperable (machine-readable formats, FAIR data principles)

Contextually linked (properties tied to ontologies to enhance interpretability)

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): SmartReviews within ORKG  

Methods/Levers: Use of RDF, ontologies (DOCO, Fabio, DEO), semantic comparison tables, living documents, collaborative editing model  

Operational Steps / Workflow:  

 1. Create sections (text, comparisons, visualizations, ontology tables, resource/property tables)  

 2. Populate with structured, linked data from ORKG  

 3. Maintain head version with version history for updates  

 4. Enable collaborative editing and attribution via acknowledgements  

Data &amp; Measures: RDF triples, SPARQL queries for retrieval, ontology-linked properties  

Implementation Context: Digital library / semantic publishing infrastructure  

  
“Comparison sections form the core of each review article.” (p. 108)  

  
“The data itself can be accessed via… SPARQL endpoint, RDF dump, and REST interface.” (p. 110)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes – clear structured representation via tables/visuals  

CR (Contextual Relevance): Yes – ontology linking ensures contextual meaning  

FE (Feasibility): Yes – enabled by ORKG platform and existing ontologies  

TI (Timeliness): Partial – supports updates but depends on community activity  

EX (Explainability): Partial – ontology tables explain properties but not all content  

GA (Goal Alignment): Yes – aligns with FAIR principles and open science goals  

Other Dimensions Named by Authors: Accessibility, Collaboration, Coverage

## Theoretical or Conceptual Foundations
Living documents concept (Shanahan 2015)  

Semantic Web and Linked Data principles (Berners-Lee et al., RDF, SPARQL)  

FAIR data principles (Wilkinson et al., 2016)

## Indicators or Metrics for Actionability
Ability to execute SPARQL queries over review content  

Presence of ontology-linked properties  

Version history and update frequency  

Accessibility compliance (HTML, WCAG)

## Barriers and Enablers to Actionability
Barriers: Researcher habits, resistance to change, lack of incentives for ongoing updates  

Enablers: Collaborative platform, attribution system, FAIR data standards, semantic web technologies

## Relation to Existing Literature
The authors situate their approach within semantic publishing research, citing prior calls for machine-readable scholarly content, living documents, and linked data approaches to overcome PDF limitations.

## Actionability-Focused Summary
The paper conceptualizes actionability in scholarly reviews as a combination of dynamic updatability, semantic structure, and both human- and machine-readability. SmartReviews operationalize this through a community-driven, living document model embedded in a knowledge graph, using linked data and ontologies to ensure interoperability and FAIR compliance. Actionability features include structured comparison tables, ontology-linked metadata, collaborative editing, and open accessibility. The implementation in ORKG demonstrates both feasibility and clear differentiation from static PDF reviews. While adoption challenges remain, the model offers a concrete, operational framework for transforming review articles into actionable scholarly resources.

## Supporting Quotes from the Paper
“The key limitation is the inability of machines to access and process knowledge presented within review articles.” (p. 105)  

“Comparison sections form the core of each review article.” (p. 108)  

“The data itself can be accessed via… SPARQL endpoint, RDF dump, and REST interface.” (p. 110)  

“The use of these technologies improves the machine-actionability of data and provides a means to make data FAIR.” (p. 107)

## Actionability References to Other Papers
Shanahan (2015) — Living documents concept  

Berners-Lee et al. (2001) — Semantic Web and Linked Data  

Wilkinson et al. (2016) — FAIR data principles  

Garcia-Castro et al. (2010) — Semantic living documents in life sciences

---
