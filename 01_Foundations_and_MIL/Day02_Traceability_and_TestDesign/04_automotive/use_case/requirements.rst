Requirements — Automotive
=========================

Purpose
-------
Document **Automotive**-specific details for Day02 Traceability and TestDesign with focus on use-case intent, assumptions, and acceptance criteria.

Domain Alignment
----------------
- Standard reference: **ISO 26262 (ASIL) + ISO 21434**
- Critical hazards: unintended acceleration/deceleration, loss of stability, braking faults
- Relevant interfaces: CAN, LIN, FlexRay, Automotive Ethernet

Examples
--------
- Nominal path: adaptive cruise and speed regulation under normal traffic.
- Boundary path: dense stop-and-go with tight headway and timing limits.
- Fault path: sensor dropout and invalid CAN frame injection.

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
- Domain Focus: Automotive
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
- Domain Focus: Automotive
- Phase Focus: MIL
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
