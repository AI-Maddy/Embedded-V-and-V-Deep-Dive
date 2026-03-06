📘 domains
=========

🎯 Purpose
----------
Capture focused artifacts for this scope with enough detail for independent technical review.

🧩 Expected Content
-------------------
- Scope and assumptions
- Scenario or procedure description
- Raw evidence references
- Analysis summary and verdict
- Open issues and follow-up actions

📋 Acceptance Criteria
----------------------
- Objective and constraints are explicitly stated.
- Evidence set is complete and accessible.
- Findings are mapped to scenario outcomes.
- Next actions are prioritized with ownership.

📏 Quality Bar
--------------
- Reproducible: rerun steps produce consistent outcome.
- Traceable: each finding links to objective/requirement IDs.
- Auditable: timestamps, versions, and ownership are present.

⚠️ Typical Gaps
---------------
- Missing setup assumptions causing non-repeatable runs.
- Incomplete raw evidence attached to final conclusions.
- No confidence statement for borderline or mixed outcomes.

✅ Completion Checklist
----------------------
- Context and constraints documented
- Evidence attached and named consistently
- Findings summarized with confidence level
- Next actions assigned with priority


Additional Deep-Dive Notes
--------------------------
- Domain Focus: General
- Phase Focus: Cross-Phase
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
- Phase Focus: Cross-Phase
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
