---
Title: "Explaining Aggregate Behaviour in Cognitive Agent Simulations Using Explanation"
Authors: "Tobias Ahlbrecht, Michael Winikoff"
DOI: "https://doi.org/10.1007/978-3-030-30391-4_8"
Year: "2019"
Publication Type: "Conference"
Discipline/Domain: "Artificial Intelligence, Multi-Agent Systems"
Subdomain/Topic: "Cognitive agents, Explainable AI, Agent-based simulation"
Eligibility: "Eligible"
Overall Relevance Score: "87"
Operationalization Score: "85"
Contains Definition of Actionability: "Yes (implicit, tied to usefulness of explanations for simulation refinement and decision-making)"
Contains Systematic Features/Dimensions: "Yes (implicit through explanation properties such as specificity, contextual relevance, and testability)"
Contains Explainability: "Yes"
Contains Interpretability: "Partial"
Contains Framework/Model: "Yes (aggregation mechanism for explanations)"
Operationalization Present: "Yes"
Primary Methodology: "Conceptual + Simulation-based demonstration"
Study Context: "Traffic simulation with cognitive BDI agents"
Geographic/Institutional Context: "TU Clausthal, Germany; Victoria University of Wellington, New Zealand"
Target Users/Stakeholders: "Simulation developers, researchers, possibly decision-makers using simulation results"
Primary Contribution Type: "Methodological framework and proof-of-concept"
Reason if Not Eligible: "n/a"
Domain Note: "[[Domain/Artificial Intelligence, Multi-Agent Systems]]"
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
# Explaining Aggregate Behaviour in Cognitive Agent Simulations Using Explanation (2019)
*Tobias Ahlbrecht, Michael Winikoff*
**DOI:** https://doi.org/10.1007/978-3-030-30391-4_8
**Domain:** [[Domain/Artificial Intelligence, Multi-Agent Systems]]
**Subdomain/Topic:** Cognitive agents, Explainable AI, Agent-based simulation

## General Summary of the Paper
This paper presents a method for obtaining actionable understanding of aggregate behaviour in cognitive agent-based simulations by aggregating individual agent explanations. Built on the BDI (Belief-Desire-Intention) agent model and an explanation mechanism for single-agent behaviour, the approach combines explanations from multiple agents to answer queries about collective actions or emergent phenomena. A traffic simulation case study demonstrates the method: explanations for why agents choose specific routes are aggregated to reveal behavioural patterns, test hypotheses (e.g., effect of bridge closures), and detect unrealistic decision-making logic. The authors also outline a process where human analysts use aggregated explanations iteratively to refine questions, run counterfactual tests, and improve simulations.

## How Actionability is Understood
The paper implicitly defines actionability as the capacity of aggregated explanations to support simulation developers in understanding, validating, and improving simulations—particularly by enabling specific, testable insights about group behaviour. Actionability arises when explanations help identify causes, guide counterfactual experimentation, and inform targeted changes.  

  
“...obtain useful (and actionable) insight into the behaviour of agent-based simulation...” (p. 129)  

  
“...this link would become less used. This hypothesis was therefore tested by re-running the simulation...” (p. 140)

## What Makes Something Actionable
Specific to the scenario and time frame (not just generic dynamics)  

Links aggregate behaviour to identifiable causal factors  

Supports hypothesis testing via simulation modification  

Enables detection of unintended or unrealistic behaviours  

Relates factors directly to agent decision logic and environment conditions

## How Actionability is Achieved / Operationalized
Framework/Approach Name(s): Aggregated Explanation Mechanism  

Methods/Levers: Logging explanatory factors in agent code; aggregating factors across relevant agents; frequency analysis to identify key drivers  

Operational Steps / Workflow:  

 1. Pose a query about aggregate behaviour  

 2. Identify relevant agents  

 3. Generate individual explanations using BDI-based mechanism  

 4. Aggregate factors and count frequencies  

 5. Filter and interpret most common factors  

 6. Optionally run counterfactual simulations to test hypotheses  

Data &amp; Measures: Counts of explanatory factor occurrences per agent for a given query  

Implementation Context: Applied to a simplified traffic simulation with road network, bridges, and route-choice agents  

  
“A straightforward way to aggregate explanations is to count the occurrences of all explanatory factors that are related to a query, and list the most common ones.” (p. 138)  

  
“...we might modify c (or the parameters) and re-run the simulation to check...” (p. 138)

## Dimensions and Attributes of Actionability (Authors’ Perspective)
CL (Clarity): Yes — Explanations are explicitly linked to decision logic, making cause understandable.  

 &gt; “...preferred the road from 1 to 2 over the road from 1 to 3 because there was traffic...” (p. 137)  

CR (Contextual Relevance): Yes — Explanations are scenario- and query-specific.  

FE (Feasibility): Partial — Hypotheses can be tested via simulation reruns.  

TI (Timeliness): Partial — Insights are generated in sync with simulation analysis.  

EX (Explainability): Yes — Mechanism based on BDI folk psychology concepts.  

GA (Goal Alignment): Partial — Explanations align with agents’ stated goals (e.g., reach destination).  

Other Dimensions Named by Authors: Testability, specificity, frequency-based relevance.

## Theoretical or Conceptual Foundations
BDI model of cognitive agents  

Folk psychology explanation concepts (Malle, 2004)  

Explanation frameworks in AI (Winikoff et al., 2018)

## Indicators or Metrics for Actionability
Frequency of explanatory factors across relevant agents  

Presence of causal, scenario-specific factors in top-ranked list  

Change in observed behaviour after modifying implicated conditions

## Barriers and Enablers to Actionability
Barriers: Noise from less relevant factors; difficulty in filtering relevant factors; unrealistic agent logic producing misleading explanations.  

Enablers: Structured logging of decision rationale; aggregation process; human-in-the-loop query refinement and counterfactual testing.

## Relation to Existing Literature
Builds on work explaining single-agent behaviour (e.g., Winikoff et al., 2018) and extends to independent multi-agent aggregates—addressing a gap where prior work lacked mechanisms for aggregating explanations.

## Actionability-Focused Summary
The authors propose a method to explain aggregate behaviour in cognitive agent-based simulations by aggregating individual agent explanations derived from BDI-based decision models. Actionability here means the ability to produce scenario-specific, testable insights into collective behaviour that aid simulation refinement and debugging. The method operationalizes actionability through a structured process: pose a query, collect and aggregate explanations, identify common causal factors, and, if needed, test them via simulation modifications. The traffic simulation case study illustrates how this approach can reveal whether route choices result from congestion, infrastructure status, or flawed logic, leading to targeted fixes. Key actionable features include clarity, contextual relevance, testability, and goal alignment. The framework provides both a conceptual contribution and a practical demonstration, scoring high in relevance and operationalization due to its explicit link between explanation mechanisms and actionable insight generation.

## Supporting Quotes from the Paper
“...obtain useful (and actionable) insight into the behaviour of agent-based simulation...” (p. 129)  

“A straightforward way to aggregate explanations is to count the occurrences of all explanatory factors...” (p. 138)  

“...preferred the road from 1 to 2 over the road from 1 to 3 because there was traffic...” (p. 137)  

“This hypothesis was therefore tested by re-running the simulation...” (p. 140)

## Actionability References to Other Papers
Malle, B.F. (2004) — Folk psychology framework for explanation  

Winikoff et al. (2018) — Single-agent explanation mechanism  

Harbers et al. (2010) — Early proposal for explaining collective behaviour

---
