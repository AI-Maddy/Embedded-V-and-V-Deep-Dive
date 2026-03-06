Theory — Day01 V-Model and Requirements
========================================

Learning Goal
-------------
Understand how requirement intent, verification strategy, and evidence evolve along the V-model.

Core Concepts
-------------
- Verification answers: “Did we build it right?”
- Validation answers: “Did we build the right thing?”
- Decomposition flows from system requirement to component-level checks.
- Integration evidence must roll back up to system intent.

Safety-Critical Framing
-----------------------
- A requirement is useful only if it is testable, bounded, and unambiguous.
- Hazard-linked requirements should have explicit rationale and acceptance thresholds.
- Traceability is the mechanism that protects confidence during change.

Practical Output for This Day
-----------------------------
- Requirement intent notes
- Verification method mapping (analysis/test/inspection)
- Initial trace links for planned scenarios

Knowledge Check
---------------
- Which requirement cannot currently be verified and why?
- Which assumption causes the largest risk if invalid?

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
