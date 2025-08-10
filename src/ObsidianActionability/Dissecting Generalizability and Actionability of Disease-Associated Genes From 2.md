---
Title: "Dissecting Generalizability and Actionability of Disease-Associated Genes From 20 Worldwide Ethnolinguistic Cultural Groups"
Authors: "Emile R. Chimusa, Shatha Alosaimi, Christian D. Bope"
DOI: "10.3389/fgene.2022.835713"
Year: "2022"
Publication Type: "Journal Article"
Discipline/Domain: "Genetics / Genomic Medicine"
Subdomain/Topic: "Clinical actionability of disease-associated genes, population genomics, genetic diversity"
Eligibility: "Eligible"
Overall Relevance Score: "90"
Operationalization Score: "85"
Contains Definition of Actionability: "Yes (explicit and comparative definitions)"
Contains Systematic Features/Dimensions: "Yes"
Contains Explainability: "Yes"
Contains Interpretability: "Yes"
Contains Framework/Model: "Yes (comparative genomic analysis framework)"
Operationalization Present: "Yes"
Primary Methodology: "Quantitative (Population genetics analysis using WGS/WES data)"
Study Context: "Genetic diversity and actionability of disease-associated genes across 20 ethnolinguistic cultural groups worldwide"
Geographic/Institutional Context: "Global, with emphasis on African populations (Bantu, Khoesan) and comparative groups from other continents"
Target Users/Stakeholders: "Genomic researchers, clinical geneticists, public health practitioners, policy makers in precision medicine"
Primary Contribution Type: "Empirical study with conceptual framing"
Reason if Not Eligible: "N/A"
Domain Note: "[[Domain/Genetics / Genomic Medicine]]"
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
# Dissecting Generalizability and Actionability of Disease-Associated Genes From 20 Worldwide Ethnolinguistic Cultural Groups (2022)
*Emile R. Chimusa, Shatha Alosaimi, Christian D. Bope*
**DOI:** 10.3389/fgene.2022.835713
**Domain:** [[Domain/Genetics / Genomic Medicine]]
**Subdomain/Topic:** Clinical actionability of disease-associated genes, population genomics, genetic diversity

## General Summary of the Paper
The paper investigates the distribution and clinical actionability of disease-associated genetic variants across 20 worldwide ethnolinguistic cultural groups, emphasizing African populations. Using WGS/WES data from the African Genome Variation Project and 1000 Genomes Project, the authors analyze SNP frequencies, proportions of pathogenic variants, derived allele distributions, and heterozygosity in genes linked to HIV/AIDS, TB, malaria, sickle cell disease, and ACMG-designated actionable genes. They find that African groups—particularly Bantu and Khoesan—display the highest genetic diversity but that many ACMG actionable genes have low derived allele proportions in African populations, raising concerns about the transferability of current actionable gene lists. The study advocates for population-specific actionable gene lists to improve equity in genomic medicine.

## How Actionability is Understood
Actionability is framed through multiple authoritative definitions:  

ClinGen: clinically prescribed interventions effective for prevention, reduced clinical burden, delayed onset, or improved outcomes in undiagnosed adults.  

100,000 Genomes Project: variants that, if identified pre-symptomatically, can significantly prevent or mitigate severe, life-threatening, and clinically significant diseases.  

Also operationally tied to classification processes involving ethical approval, annotation databases, pathogenicity scoring, and allele frequency considerations.  

  
“Actionability as clinically prescribed interventions to a genetic disorder that is effective for prevention, lowered clinical burden or delay for a clinical disease, or improved clinical treatments and outcomes…” (p. 2)  

  
“…variants that can significantly prevent (or result in illness…if identified before symptoms become apparent.” (p. 2)

## What Makes Something Actionable
Clinically preventable or mitigable before symptom onset  

Severity and clinical significance of condition  

Established interventions exist with proven benefit  

Variant classification supported by evidence and ethical review  

Population-specific allele frequency and pathogenicity evidence  

Functional impact predictions from multiple annotation tools

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): Comparative population genomics actionability assessment  

Methods/Levers: Joint variant calling across global ethnolinguistic groups; functional annotation via ANNOVAR; filtering by deleteriousness consensus (≥17/21 prediction tools)  

Operational Steps / Workflow:  

 1. Identify disease-associated and ACMG actionable genes from curated databases (GWAS Catalog, DisGeNET, ACMG list)  

 2. Extract relevant SNPs from WGS/WES datasets  

 3. Perform quality control, phasing, and haplotype inference  

 4. Analyze genetic structure (PCA), pathogenicity proportions, derived allele frequencies, MAF distributions  

 5. Compare patterns across 20 ethnolinguistic groups  

Data &amp; Measures: SNP counts, proportion pathogenic, derived allele proportion, heterozygosity metrics  

Implementation Context: Global, cross-population genomic comparatives  

  
“…combine many annotation pipelines during filtering and prioritization of mutations…” (p. 2)  

  
“…proportion of pathogenic variants within ACG-specific genes from ethnolinguistic cultural groups…” (p. 4)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — clear variant classification processes are necessary (p. 2)  

CR (Contextual Relevance): Yes — population-specific allele frequency and disease relevance critical (p. 6–8)  

FE (Feasibility): Yes — intervention must be possible and effective (p. 2)  

TI (Timeliness): Partial — early/pre-symptomatic detection mentioned but not deeply operationalized  

EX (Explainability): Yes — reliance on multiple annotation tools and known pathogenicity databases (p. 2, 9)  

GA (Goal Alignment): Yes — alignment with improved global healthcare equity and personalized medicine (p. 1, 8)  

Other Dimensions Named by Authors: Transferability/generalizability, genetic diversity, pathogenicity burden

## Theoretical or Conceptual Foundations
ClinGen actionability framework  

100,000 Genomes Project protocol  

ACMG actionable gene list standards  

Population genomics concepts of genetic diversity, derived allele frequencies, linkage disequilibrium

## Indicators or Metrics for Actionability
Proportion of pathogenic variants per gene in a population  

Minor allele frequency (MAF) distributions  

Proportion of derived alleles  

Gene-specificity of SNP frequency  

Observed vs. expected heterozygosity

## Barriers and Enablers to Actionability
Barriers:  

 - Limited transferability of ACMG actionable gene lists to African populations  

 - Knowledge bias in existing variant databases toward non-African populations  

 - Variation in derived allele distributions affecting predictive validity  

Enablers:  

 - High-quality population-specific genomic data  

 - Multi-tool annotation consensus  

 - Cross-population comparative frameworks

## Relation to Existing Literature
Builds on prior work highlighting disparities in actionable variant frequencies between European and African populations (e.g., Dorschner et al. 2016; Amendola et al. 2015). Expands by integrating multi-continental ethnolinguistic perspectives and four African high-burden diseases.

## Actionability-Focused Summary
The study critically assesses the global generalizability of ACMG’s actionable gene list and known disease-associated genes for HIV/AIDS, TB, malaria, and sickle cell disease. It reveals that African populations, particularly Bantu and Khoesan, have the highest genetic diversity but often lower derived allele proportions in ACMG actionable genes, challenging the transferability of current lists. Actionability is framed as dependent on clinical preventability, disease severity, intervention feasibility, population relevance, and robust pathogenicity evidence. Operationalization involves large-scale genomic data integration, multi-tool variant annotation, and cross-population analysis of pathogenic burden, allele frequencies, and genetic diversity. The findings argue for population-specific actionable gene lists to improve equity in precision medicine.

## Supporting Quotes from the Paper
“Actionability as clinically prescribed interventions… effective for prevention, lowered clinical burden…” (p. 2)  

“…classification of variants to be clinically actionable… can only emerge during the process of seeking ethical approval…” (p. 2)  

“…high genetic diversity in the present actionable and known disease-associated genes… suggesting the limitation of transferability…” (p. 1)  

“…combine many annotation pipelines during filtering and prioritization…” (p. 2)  

“…proportion of pathogenic variants within ACG-specific genes…” (p. 4)

## Actionability References to Other Papers
Hunter et al., 2016 — ClinGen actionability assessment protocol  

Bope et al., 2019 — in silico mutation prediction challenges in African genomes  

Dorschner et al., 2016; Amendola et al., 2015 — disparities in actionable variants between populations  

ACMG-73 actionable genes list

---
