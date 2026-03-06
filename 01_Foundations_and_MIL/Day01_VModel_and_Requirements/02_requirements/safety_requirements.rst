Safety Requirements — Day01
==========================

Goal
----
Translate hazards into enforceable, testable technical safety requirements.

Safety Requirement Structure
----------------------------
- Hazard reference and severity context.
- Safety mechanism and expected protective behavior.
- Fault detection timing and reaction constraints.
- Safe-state definition and recovery path.

Verification Focus
------------------
- Detection coverage under representative faults.
- False positive/negative behavior boundaries.
- Deterministic transition to safe state.

Review Questions
----------------
- Does each hazard have a linked safety requirement?
- Can the safety mechanism be bypassed unintentionally?
- Is residual risk disposition documented?

Additional Deep-Dive Notes
--------------------------
- Domain Focus: General
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
- Domain Focus: General
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
- Domain Focus: General
- Phase Focus: MIL
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
