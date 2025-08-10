---
Title: "Prospective Longitudinal ctDNA Workflow Reveals Clinically Actionable Alterations in Ovarian Cancer"
Authors: "Jaana Oikkonen, Kaiyang Zhang, Liina Salminen, Ingrid Schulman, Kari Lavikka, Noora Andersson, Erika Ojanperä, Sakari Hietanen, Seija Grenman, Rainer Lehtonen, Kaisa Huhtinen, Olli Carpén, Johanna Hynninen, Anniina Färkkilä, Sampsa Hautaniemi"
DOI: "https://doi.org/10.1200/PO.18.00343"
Year: "2019"
Publication Type: "Journal"
Discipline/Domain: "Oncology / Precision Medicine"
Subdomain/Topic: "Circulating Tumor DNA (ctDNA) in High-Grade Serous Ovarian Cancer (HGSOC)"
Eligibility: "Eligible"
Overall Relevance Score: "90"
Operationalization Score: "95"
Contains Definition of Actionability: "Yes (implicit, clinically oriented)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes (workflow pipeline)"
Operationalization Present: "Yes"
Primary Methodology: "Mixed Methods (prospective clinical cohort, bioinformatics pipeline)"
Study Context: "Clinical workflow for longitudinal ctDNA analysis to guide treatment in HGSOC"
Geographic/Institutional Context: "Turku University Hospital &amp; University of Helsinki, Finland"
Target Users/Stakeholders: "Oncologists, molecular tumor boards, translational cancer researchers"
Primary Contribution Type: "Clinical proof-of-concept &amp; open-source workflow"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Oncology / Precision Medicine]]"
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
# Prospective Longitudinal ctDNA Workflow Reveals Clinically Actionable Alterations in Ovarian Cancer (2019)
*Jaana Oikkonen, Kaiyang Zhang, Liina Salminen, Ingrid Schulman, Kari Lavikka, Noora Andersson, Erika Ojanperä, Sakari Hietanen, Seija Grenman, Rainer Lehtonen, Kaisa Huhtinen, Olli Carpén, Johanna Hynninen, Anniina Färkkilä, Sampsa Hautaniemi*
**DOI:** https://doi.org/10.1200/PO.18.00343
**Domain:** [[Domain/Oncology / Precision Medicine]]
**Subdomain/Topic:** Circulating Tumor DNA (ctDNA) in High-Grade Serous Ovarian Cancer (HGSOC)

## General Summary of the Paper
This study presents a clinical and bioinformatics workflow for detecting clinically actionable alterations in HGSOC using longitudinal ctDNA sampling. The pipeline integrates &gt;500-gene targeted sequencing, a ctDNA-specific bioinformatics pipeline, and the Translational Oncology Knowledgebase to prioritize alterations based on ESCAT tiers. Across 12 patients, ctDNA mutations and CNAs showed high concordance with tumor tissue findings. Clinically actionable alterations were identified in 58% of patients, guiding therapy in one platinum-resistant case (ERBB2 amplification → trastuzumab + chemo) with significant tumor regression and CA-125 normalization. The workflow demonstrates early detection of poor responders and suggests potential for personalized treatment adaptation.

## How Actionability is Understood
Implicitly defined as the presence of genomic alterations in ctDNA that can be linked to existing therapies, ranked by clinical evidence (ESCAT tiers), and used to guide treatment decisions in real time. Actionability requires reliable detection, clinical relevance, and therapeutic linkage.

  
“Potentially clinically actionable alterations were validated… classified as most prominent (ESCAT… Scale for Clinical Actionability of Molecular Targets)” (p. 3)  

  
“The provided approach allows the selection of treatment options that target subclones that persist during therapy.” (p. 2)

## What Makes Something Actionable
Direct association with existing or investigational therapies  

Sufficient evidence of clinical relevance (ESCAT ranking)  

Persistence in tumor subclones during treatment  

Validation in tumor tissue (IHC/ISH)  

Concordance with patient’s mutational profile and disease context

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): Clinical ctDNA workflow integrating sequencing, bioinformatics pipeline, and Translational Oncology Knowledgebase  

Methods/Levers: &gt;500-gene targeted panel sequencing, variant/CNA calling, filtering, prioritization via knowledgebase, validation via IHC/ISH  

Operational Steps / Workflow: Longitudinal plasma sampling → sequencing → bioinformatics filtering → therapeutic matching (ESCAT) → validation → clinical decision  

Data &amp; Measures: VAF dynamics, mutation counts, CNA ratios, CA-125 levels  

Implementation Context: Prospective monitoring before, during, after chemotherapy in HGSOC  

  
“Longitudinal ctDNA sampling can be used to detect response… and identify clinically applicable mutations and copy number alterations.” (p. 2)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — clear link between detected alteration and therapeutic relevance (ESCAT criteria).  

CR (Contextual Relevance): Yes — therapy matching based on patient-specific ctDNA profile.  

FE (Feasibility): Yes — minimally invasive sampling, open-source tools.  

TI (Timeliness): Yes — early detection of poor responders after 1–2 chemo cycles.  

EX (Explainability): Yes — biological pathway context and evidence level for each alteration.  

GA (Goal Alignment): Yes — aligns with goal of improving survival in HGSOC by targeting resistant subclones.  

Other Dimensions Named by Authors: Concordance with tumor tissue; evidence-based prioritization (ESCAT).

## Theoretical or Conceptual Foundations
ESCAT (ESMO Scale for Clinical Actionability of Molecular Targets)  

Concepts from precision oncology: mTOR, HR deficiency, EGFR pathway targeting  

Longitudinal biomarker monitoring

## Indicators or Metrics for Actionability
Variant Allele Frequency (VAF) trends  

CNA ratios  

CA-125 tumor marker correlation  

ESCAT evidence tier assignment

## Barriers and Enablers to Actionability
Barriers: Low VAF subclonal mutations, ctDNA heterogeneity, validation requirements, therapy availability  

Enablers: Open-source pipeline, integration with knowledgebase, high plasma-tumor concordance, minimally invasive sampling

## Relation to Existing Literature
Builds on prior ctDNA monitoring studies (e.g., TP53 tracking in HGSOC) but extends to broad-panel actionable mutation detection and real-time therapeutic adaptation.

## Actionability-Focused Summary
This paper delivers a robust, clinically relevant framework for using longitudinal ctDNA profiling to guide therapy in HGSOC. Actionability is framed as the ability to detect and therapeutically match validated genomic alterations in a patient’s ctDNA profile, with emphasis on ESCAT evidence ranking and early detection of resistance. The study operationalizes this via a &gt;500-gene targeted sequencing panel, tailored bioinformatics pipeline, and knowledgebase integration, validated in a prospective cohort. The method not only identifies actionable alterations in over half of patients but also demonstrates a real-world therapy change with significant clinical benefit. The framework’s open-source nature enhances feasibility for clinical adoption.

## Supporting Quotes from the Paper
“We identified high-confidence, potentially clinically actionable mutations or CNAs in seven patients (58%).” (p. 6)  

“The provided approach allows the selection of treatment options that target subclones that persist during therapy.” (p. 2)  

“Treatment… was changed on the basis of detection of ERBB2 amplification… followed by significant tumor shrinkage.” (p. 1)  

“Longitudinal ctDNA sampling can be used… to identify poor-responding patients after first cycles of chemotherapy.” (p. 1)

## Actionability References to Other Papers
ESCAT framework: Mateo et al., 2018  

TP53 monitoring in HGSOC: Parkinson et al., 2016  

Pathway-specific targeting references for mTOR, HR deficiency, EGFR, CDK alterations

---
