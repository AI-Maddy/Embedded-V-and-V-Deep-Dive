Aerospace — Aerospace
=====================

Purpose
-------
Document **Aerospace**-specific details for Day02 Traceability and TestDesign with focus on aerospace verification workflow.

Domain Alignment
----------------
- Standard reference: **DO-178C/DO-254 + ARP4754A/ARP4761**
- Critical hazards: loss of control authority, unstable mode transition, stale avionics data
- Relevant interfaces: ARINC 429/664, AFDX, discrete I/O

Examples
--------
- Nominal path: stable flight-control mode tracking with expected disturbances.
- Boundary path: high-workload transition envelope near stability margins.
- Fault path: bus label corruption and sensor disagreement event.

Patterns
--------
- Use requirement-linked checks for every scenario.
- Track timing and functional outcomes together.
- Keep setup reproducibility constraints explicit.

Anti-Patterns
-------------
- Domain-agnostic statements without measurable criteria.
- Ignoring interface constraints during analysis.
- Closing findings without residual risk statement.

Pitfalls
--------
- Missing sensor/actuator fault variants.
- Weak traceability from objective to artifact.
- Non-repeatable reruns from uncontrolled configuration drift.

Checklist
---------
- Scope and assumptions are explicit.
- Acceptance criteria are quantitative.
- Evidence set is complete and auditable.
- Follow-up actions are prioritized.

Additional Deep-Dive Notes
--------------------------
- Domain Focus: Aerospace
- Phase Focus: MIL
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.

Additional Deep-Dive Notes
--------------------------
- Domain Focus: Aerospace
- Phase Focus: MIL
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
