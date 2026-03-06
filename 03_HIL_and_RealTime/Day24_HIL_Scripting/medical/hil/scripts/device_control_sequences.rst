Device Control Sequences — Medical
==================================

Purpose
-------
Document **Medical**-specific details for Day24 HIL Scripting with focus on automation and deterministic replay controls.

Domain Alignment
----------------
- Standard reference: **IEC 62304 + ISO 14971 + IEC 60601 context**
- Critical hazards: incorrect dosage delivery, missed alarm, unsafe therapy continuation
- Relevant interfaces: device buses, sensor links, alarm/event channels

Examples
--------
- Nominal path: therapy control with validated sensor feedback.
- Boundary path: near-threshold dosing and alarm escalation timing.
- Fault path: sensor spike/dropout and actuator command rejection path.

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
- Domain Focus: Medical
- Phase Focus: HIL
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.

Additional Deep-Dive Notes
--------------------------
- Domain Focus: Medical
- Phase Focus: HIL
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
