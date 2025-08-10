---
Title: "AI-Driven Whole-Exome Sequencing: Advancing Variant Interpretation and Precision Medicine"
Authors: "Faisal Aburub, Mayyas Al-Remawi, Rami A. Abdel-Rahem, Faisal Al-Akayleh, Ahmed S.A. Ali Agha"
DOI: "10.1109/ICCIAA65327.2025.11013653"
Year: "2025"
Publication Type: "Conference Proceeding"
Discipline/Domain: "Bioinformatics / Genomic Medicine"
Subdomain/Topic: "Whole-Exome Sequencing, AI for Variant Interpretation, Precision Medicine"
Eligibility: "Eligible"
Overall Relevance Score: "85"
Operationalization Score: "90"
Contains Definition of Actionability: "Yes (implicit, as clinically actionable insights in genomic medicine)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes (AI-driven WES pipeline with multi-omics integration and XAI)"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual / Review with applied case studies"
Study Context: "AI-enhanced WES in clinical genetic diagnostics"
Geographic/Institutional Context: "University of Petra, The University of Jordan (Jordan); applied references from Taiwan, South Korea, USA, etc."
Target Users/Stakeholders: "Clinicians, genomic researchers, bioinformaticians, healthcare policymakers"
Primary Contribution Type: "Conceptual framework with practical application examples for AI-driven WES"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Bioinformatics / Genomic Medicine]]"
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
# AI-Driven Whole-Exome Sequencing: Advancing Variant Interpretation and Precision Medicine (2025)
*Faisal Aburub, Mayyas Al-Remawi, Rami A. Abdel-Rahem, Faisal Al-Akayleh, Ahmed S.A. Ali Agha*
**DOI:** 10.1109/ICCIAA65327.2025.11013653
**Domain:** [[Domain/Bioinformatics / Genomic Medicine]]
**Subdomain/Topic:** Whole-Exome Sequencing, AI for Variant Interpretation, Precision Medicine

## General Summary of the Paper
This paper presents an AI-driven framework for whole-exome sequencing (WES) that aims to improve variant interpretation, pathogenicity prediction, and clinical decision-making in precision medicine. It reviews traditional and AI-based WES pipelines, compares WES and whole-genome sequencing, and outlines AI methods for variant calling, annotation, and prioritization. Key AI tools discussed include DeepVariant, DANN, ClinPred, and EVIDENCE. The framework integrates multi-omics data, phenotype-genotype correlations, and explainable AI (XAI) to enhance interpretability and trust. The authors also address ethical, legal, and implementation challenges such as privacy, bias, and regulatory compliance, recommending federated learning and fairness audits.

## How Actionability is Understood
The authors implicitly define actionability as the transformation of WES data into clinically relevant, timely, and trustworthy recommendations that can inform diagnosis, prognosis, and treatment in precision medicine.  

  
“AI… can pinpoint disease-associated variants, discover novel biomarkers, and guide personalized treatment strategies” (p. 1)  

  
“Integrating multi-omics data and correlating genotype with phenotype further enable personalized interventions, expediting the translation of WES findings into actionable treatments” (p. 4)

## What Makes Something Actionable
Accurate identification of pathogenic variants  

Contextual relevance through phenotype-genotype correlation  

Timely reporting and reduced turnaround times  

Interpretability and transparency in AI decision-making  

Integration of multi-omics data for holistic variant assessment  

Feasibility in clinical workflows (automation, reduced manual curation)

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): AI-driven WES pipeline with XAI  

Methods/Levers: ML/DL models (DeepVariant, DANN, AI Variant Prioritizer, EVIDENCE), phenotype extraction, multi-omics integration, federated learning  

Operational Steps / Workflow: Data preprocessing → AI variant calling → AI-based annotation → Phenotypic data integration → Prioritization → Explainable output for clinicians  

Data &amp; Measures: WES datasets, HPO terms, population frequency databases, functional impact scores, multi-omics profiles  

Implementation Context: Clinical genetic diagnostics and research workflows  

  
“An AI-powered WES pipeline… improved diagnostic yield to 41% for trio-WES cases and 28% for singletons, reducing reporting time to one week” (p. 2)  

  
“Federated learning enables secure genomic data sharing… maintaining privacy and compliance” (p. 2)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes – Output must be interpretable for clinicians via XAI.  

CR (Contextual Relevance): Yes – Integration of patient metadata and multi-omics.  

FE (Feasibility): Yes – Automation and reduced turnaround time.  

TI (Timeliness): Partial – Reporting time reduced to one week in tested pipelines.  

EX (Explainability): Yes – SHAP, LIME for AI transparency.  

GA (Goal Alignment): Yes – Prioritization aligned with clinical diagnostic objectives.  

Other Dimensions: Ethical compliance, fairness, reproducibility.

## Theoretical or Conceptual Foundations
AI interpretability frameworks (SHAP, LIME)  

Federated learning privacy models  

Prior variant prioritization frameworks (ClinPred, REVEL, CADD)

## Indicators or Metrics for Actionability
Diagnostic yield percentage  

Top-N ranking accuracy for causative variants  

Turnaround time (e.g., 1 week)  

Percentage increase in pathogenic/likely pathogenic classification after AI integration

## Barriers and Enablers to Actionability
Barriers: Data security, black-box AI, bias in training datasets, lack of regulatory clarity.  

Enablers: XAI frameworks, federated learning, inclusive datasets, standardization of AI pipelines.

## Relation to Existing Literature
Positions AI-driven WES as an evolution over traditional variant interpretation pipelines, improving diagnostic yield and speed while addressing trust and transparency concerns. Builds on prior variant prioritization and annotation tools, extending them with multi-omics integration and ethical safeguards.

## Actionability-Focused Summary
This paper conceptualizes actionability in WES as the delivery of accurate, relevant, interpretable, and timely genetic insights that directly inform patient care. By leveraging AI for variant calling, annotation, and prioritization—and integrating phenotype and multi-omics data—the framework operationalizes actionability through automation, accuracy gains, and interpretability tools like SHAP and LIME. The authors provide evidence of improved diagnostic yield and reduced turnaround time, while addressing ethical and implementation barriers such as bias, privacy, and transparency. Their proposed pipeline aligns closely with clinical goals, demonstrating how AI can bridge the gap between raw genomic data and actionable medical decisions.

## Supporting Quotes from the Paper
“AI… can pinpoint disease-associated variants, discover novel biomarkers, and guide personalized treatment strategies” (p. 1)  

“An AI-powered WES pipeline… improved diagnostic yield to 41% for trio-WES cases and 28% for singletons, reducing reporting time to one week” (p. 2)  

“Integrating multi-omics data and correlating genotype with phenotype further enable personalized interventions, expediting the translation of WES findings into actionable treatments” (p. 4)  

“Federated learning enables secure genomic data sharing… maintaining privacy and compliance” (p. 2)

## Actionability References to Other Papers
Huang et al. (2022) – AI Variant Prioritizer for integrating WES and phenotypic data  

Graham et al. (2018) – WES + metabolomics for variant prioritization  

Barcelona-Cabeza et al. (2021) – WES + RNA-Seq for improved variant detection  

Rusch et al. (2018) – Multi-omics integration in oncology  

Pinxten &amp; Howard (2014) – Ethical issues in genome sequencing

---
