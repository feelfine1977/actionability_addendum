# Synthesis + Clustering Prompt (Actionability Literature Review)
**Output format:** Produce a single, well-structured **Markdown (.md)** document as the final output.  
**Additionally create two CSV files** alongside the Markdown output:
1) `papers_features.csv` — one row per paper with key features (definition use, op. strategy, dimensions, representative quotes with page numbers).  
2) `domains_summary.csv` — one row per domain/cluster with key arguments, synthesis, and top quotes.

---

## Objective
Given the corpus of “actionability” papers (across multiple fields), **cluster** the literature by **domain** (e.g., healthcare, education, AI/ML, cybersecurity, urban sustainability, environmental/climate, policy, data mining/AKD, recommender systems, dashboards/viz, HUMINT/security studies, etc.). Within each domain, **synthesize** the **main argumentation patterns** about actionability: how it is *defined*, *made actionable* (operationalized), and which **dimensions** recur (Clarity—CL, Contextual Relevance—CR, Feasibility—FE, Timeliness—TI, Explainability—EX, Goal Alignment—GA). Briefly note **outliers** or alternative understandings.

## Scope & Exclusions
- The general visuals should **exclude process mining** papers.  
- Provide a **separate deeper analysis** (and visuals) **only for process mining** papers.

## Structure of the Markdown Output
1. **Executive Summary**  
   - 6–10 bullets capturing the cross-domain picture: most common definitions, operationalization patterns, which dimensions dominate, where disagreements occur, and which domains have the best evidence.
2. **Domain Clusters (Macro Synthesis)**  
   For each cluster (e.g., Healthcare, Education, AI/ML—Recourse & Explainability, Cybersecurity, Environmental/Climate, Urban Sustainability, Recommender Systems, Dashboards/Data Viz, HUMINT/Security Studies, Policy Agility, Web Usage Mining/AKD, IoT/Stream Reasoning, Scholarly Publishing, Situation Recognition, Oncology Precision Medicine):
   - **What “actionable” means here** (concise synthesis).
   - **How actionability is operationalized** (general strategy + noteworthy frameworks).
   - **Dominant dimensions** (CL/CR/FE/TI/EX/GA) and rationale.
   - **Most-cited operational levers** (methods, metrics, workflows).
   - **Most important quotes** (with **paper title** and **page number**) supporting the synthesis. Use brief block quotes.
   - **Notable disagreements or outliers** within the cluster.
3. **Cross-Cutting Dimensions (Meta-Synthesis)**  
   - For each dimension (CL, CR, FE, TI, EX, GA), summarize how it is understood and evidenced across domains.  
   - Include a short subsection: **“Authors who argue for actionability without defining it”** — report count and provide a brief synthesis of the main arguments they make (e.g., need for decision support, business relevance, translation to practice), and whether any papers diverge.
4. **Operationalization — Deep Dive**  
   - **General strategies** observed (e.g., two-way significance frameworks; decision rules; GLIA’s decidability/executability; counterfactuals/recourse; stream reasoning; DEA-DDF benchmarking; narrative/storytelling; stakeholder co-production; PDX functional validation; ctDNA longitudinal workflows; situation recognition with EventShop; Opportunity Map for post-mining actionability).  
   - **Representative frameworks** (2–5 per domain) with **short why-they-work** rationales and (if applicable) key equations or evaluation metrics.  
   - Provide **short, direct quotes** (with **title** + **page**) that anchor the definitions or “what makes it actionable.”
5. **Process Mining (Separate Section: Deep Analysis)**  
   - Summarize actionability in **process mining** papers **only** (or explain absence).  
   - Provide a structured mini-synthesis (definition presence, operationalization, gaps, and how PM work could become actionable).  
   - End with **recommendations** for making process mining insights actionable (e.g., mapping insights to decisions, units of change, constraints/costs, timeliness, explainability to non-experts).
6. **Appendix**  
   - **Data tables** with per-paper features (keep concise).  
   - Short **method note** on clustering and coding approach.

## Extraction & Evidence Requirements
- Use the **two CSVs** you produced in this run:
  - `papers_features.csv` for per-paper evidence.
  - `domains_summary.csv` for aggregated, domain-level synthesis.
- **Quote policy:** When including **direct quotes**, always add the **paper title** and **page number** in parentheses, e.g.,  
  > “…Actionable data…” — *User Perceptions of Actionability in Data Dashboards* (p. 257)
- **Evidence density:** Prefer 2–4 quotes per domain cluster; keep quotes short (≤25 words).  
- **Comparisons:** Note where **domains differ** (e.g., healthcare’s GLIA vs. AI’s counterfactual recourse; cyber’s policy agility vs. environmental science’s six-factor model).

## Deliverables
- **One Markdown file** (this synthesis)  
- **CSV 1**: `papers_features.csv` (one row per paper)  
- **CSV 2**: `domains_summary.csv` (one row per domain cluster)

## Grading Rubric (implicit)
- **Clarity**: Headings, bullets, and short paragraphs; no jargon without short definitions.  
- **Evidence**: Quotes with page numbers; explicit methods/metrics named.  
- **Synthesis**: Clear cross-domain threads and outliers, not a list.  
- **Operational Depth**: Concrete workflows and levers.  
- **Process Mining**: Treated separately with concrete recommendations.