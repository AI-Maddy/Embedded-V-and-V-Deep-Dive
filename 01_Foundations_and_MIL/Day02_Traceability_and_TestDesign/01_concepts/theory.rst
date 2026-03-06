Theory — Day02 Traceability and Test Design
===========================================

Learning Goal
-------------
Build test designs that are directly traceable to requirements and robust against change.

Traceability Principles
-----------------------
- Forward trace: requirement → test/design/artifact.
- Backward trace: artifact/verdict → originating requirement.
- Bidirectional trace reduces audit and regression risk.

Test Design Depth
-----------------
- Nominal tests prove intended behavior.
- Boundary tests expose sensitivity to limits.
- Negative/fault tests prove safe degradation and recovery.

Review Triggers
---------------
- Requirement changed without test update.
- Test exists without requirement linkage.
- Pass/fail criteria missing measurable thresholds.

Deliverable Expectations
------------------------
- Traceability matrix baseline
- Scenario set with coverage rationale
- Gap list for unverified requirements

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
