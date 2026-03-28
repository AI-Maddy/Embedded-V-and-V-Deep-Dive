Severity / Priority Colour Legend 🎨
-----------------------------------
- 🟢 : Low severity / low priority
- 🟡 : Medium severity / medium priority
- 🔴 : High severity / high priority

Checklist 📝
---------
☐ Scope and assumptions are explicit.
☐ Acceptance criteria are quantitative.
☐ Evidence set is complete and auditable.
☐ Follow-up actions are prioritized.

Additional Deep-Dive Notes 📊
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

.. list-table:: Standards References
   :widths: 20 80
   :stub-columns: 1

   * - Standard
     - Description
   * - IEC 62304
     - Medical device software — Software life cycle processes
   * - ISO 14971
     - Medical devices — Application of risk management to medical devices
   * - IEC 60601
     - Medical electrical equipment — General requirements for basic safety and essential performance

