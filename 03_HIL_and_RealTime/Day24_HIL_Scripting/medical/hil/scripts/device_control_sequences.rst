Device Control Sequences — Medical 🏥
=====================================

Purpose 📝
-------
Document **Medical**-specific details for Day24 HIL Scripting with focus on automation and deterministic replay controls.

Domain Alignment 🗂️
----------------
- Standard reference: **IEC 62304 + ISO 14971 + IEC 60601 context** [1]_
- Critical hazards: incorrect dosage delivery, missed alarm, unsafe therapy continuation
- Relevant interfaces: device buses, sensor links, alarm/event channels

.. important::
   Use the **MEDICS** mnemonic to ensure domain-specific considerations:

   - **M** : Mind the patient safety context
   - **E** : Evaluate critical hazards and risks
   - **D** : Determine relevant interfaces and constraints
   - **I** : Inspect requirements and test artifacts
   - **C** : Consider timing and functional outcomes
   - **S** : Set quantitative acceptance criteria

Examples 📚
--------
### Nominal Path 🟢
- **GIVEN** : Therapy control with validated sensor feedback
- **WHEN** : The system is in a steady state
- **THEN** : The therapy is delivered correctly and safely

### Boundary Path 🟡
- **GIVEN** : Near-threshold dosing and alarm escalation timing
- **WHEN** : The system is in a boundary condition
- **THEN** : The system responds correctly and safely

### Fault Path 🔴
- **GIVEN** : Sensor spike/dropout and actuator command rejection path
- **WHEN** : The system encounters a fault
- **THEN** : The system fails safely and reports the error

Patterns 🔍
--------
- Use requirement-linked checks for every scenario.
- Track timing and functional outcomes together.
- Keep setup reproducibility constraints explicit.

Anti-Patterns 🚫
-------------
- Domain-agnostic statements without measurable criteria.
- Ignoring interface constraints during analysis.
- Closing findings without residual risk statement.

Pitfalls 🚨
--------
- Missing sensor/actuator fault variants.
- Weak traceability from objective to artifact.
- Non-repeatable reruns from uncontrolled configuration drift.

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

References
----------
.. [1] IEC 62304 + ISO 14971 + IEC 60601 context

Pre-Review Checklist 📝
------------------------
☐ Verify that all examples are complete and accurate.
☐ Check that all patterns and anti-patterns are relevant and applicable.
☐ Review the checklist for completeness and accuracy.
☐ Ensure that all references are up-to-date and relevant.
