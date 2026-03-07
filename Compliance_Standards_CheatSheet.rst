Compliance Standards Cheat Sheet 📚
=====================================

Purpose 🎯
-----------

Quick-reference mapping between domain standards and expected verification evidence.

Domain Standards Mnemonic: **VAST** (Verification, Assurance, Standards, Traceability)

Severity/Priority Legend
-------------------------

| Color | Severity/Priority |
| --- | --- |
| 🟢 | Nominal (green) |
| 🟡 | Boundary (yellow) |
| 🔴 | Fault (red) |

Core Standards by Domain
------------------------

### Automotive 🚗

* ISO 26262 (ASIL A–D) 🟢
* ISO 21434 (cybersecurity) 🟡
* ASPICE process expectations 🔴

### Aerospace 🚀

* DO-178C (software) 🟢
* DO-254 (hardware) 🟡
* ARP4754A/ARP4761 safety lifecycle 🔴

### Medical 💊

* IEC 62304 (software lifecycle) 🟢
* ISO 14971 (risk management) 🟡
* IEC 60601 safety context 🔴

Evidence Expectations
---------------------

### Requirement Traceability

* Trace requirements from system intent to test verdict.
* Verify requirement-to-test linkage.

### Verification Artifacts

* Verification artifacts with timestamps, tool versions, and ownership.
* Include structural evidence (coverage/timing/object-code where applicable).

### Defect Triage History

* Track failed/blocked tests to corrective action.
* Document defect triage history and closure rationale.

Practical Review Checklist
--------------------------

☐ Is each requirement linked to at least one verification activity?
☐ Are failed/blocked tests tracked to corrective action?
☐ Are assumptions and environmental limits explicitly documented?
☐ Is residual risk accepted by the correct role/authority?

Audit-Ready Artifact Bundle
---------------------------

### Requirements Baseline

* Include requirements baseline and change history.
* Verify test matrix, logs, traces, and signed summary report.

### Static-Analysis Outputs

* Include static-analysis outputs and deviation justifications.
* Verify release decision note with risk disposition.

### Example Expansion

#### Nominal Scenario 🟢

* Given: System operates within specified requirements.
* When: Normal operating conditions are met.
* Then: System functions as expected.

#### Boundary Scenario 🟡

* Given: System operates at the edge of specified requirements.
* When: Boundary conditions are met.
* Then: System functions as expected with minor deviations.

#### Fault Scenario 🔴

* Given: System operates with a fault condition.
* When: Faulty behavior is detected.
* Then: System recovers or fails safely.

Additional Deep-Dive Notes
--------------------------

### Domain Focus

* General domain focus: embedded systems.

### Phase Focus

* Cross-Phase verification and validation.

### Evidence Priorities

* Functional correctness
* Timing behavior
* Robustness
* Traceability

### Patterns

* Baseline-first comparison
* Fixed acceptance thresholds
* Deterministic reruns

### Anti-Patterns

* Post-hoc threshold tuning
* Missing raw artifacts
* Incomplete negative-path checks

### Pitfalls

* Hidden assumptions
* Interface timing drift
* Weak requirement-to-test linkage

### Review Heuristic

* If a claim cannot be tied to an artifact, mark confidence as provisional.

### Checklist Extension

* Capture residual risk, ownership, and next action for each unresolved item.

.. note::
   This cheat sheet is intended to provide a quick reference for embedded systems verification and validation. It is not a comprehensive guide and should be used in conjunction with relevant domain standards and guidelines.

.. warning::
   Failure to follow domain standards and guidelines may result in non-compliance and potential safety risks.

.. important::
   This cheat sheet is subject to change and may not reflect the latest updates to domain standards and guidelines.

.. admonition::
   This cheat sheet is intended for informational purposes only and should not be used as a substitute for professional advice or guidance.
