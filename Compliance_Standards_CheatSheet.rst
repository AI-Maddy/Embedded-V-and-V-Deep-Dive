Compliance Standards Cheat Sheet
===============================

Purpose
-------
Quick-reference mapping between domain standards and expected verification evidence.

Core Standards by Domain
------------------------
- Automotive: ISO 26262 (ASIL A–D), ISO 21434 (cybersecurity), ASPICE process expectations.
- Aerospace: DO-178C (software), DO-254 (hardware), ARP4754A/ARP4761 safety lifecycle.
- Medical: IEC 62304 (software lifecycle), ISO 14971 (risk management), IEC 60601 safety context.

Evidence Expectations
---------------------
- Requirement traceability from system intent to test verdict.
- Verification artifacts with timestamps, tool versions, and ownership.
- Structural evidence (coverage/timing/object-code where applicable).
- Defect triage history and closure rationale.

Practical Review Checklist
--------------------------
- Is each requirement linked to at least one verification activity?
- Are failed/blocked tests tracked to corrective action?
- Are assumptions and environmental limits explicitly documented?
- Is residual risk accepted by the correct role/authority?

Audit-Ready Artifact Bundle
---------------------------
- Requirements baseline and change history.
- Test matrix, logs, traces, and signed summary report.
- Static-analysis outputs and deviation justifications.
- Release decision note with risk disposition.

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
