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
  .. note::
     ASIL A–D levels represent Automotive Safety Integrity Levels.
* ISO 21434 (cybersecurity) 🟡
  .. important::
     Cybersecurity is critical in the automotive domain.
* ASPICE process expectations 🔴
  .. warning::
     ASPICE compliance is essential for process maturity.

### Aerospace 🚀

* DO-178C (software) 🟢
  .. note::
     DO-178C is the standard for software development in the aerospace domain.
* DO-254 (hardware) 🟡
  .. important::
     DO-254 is the standard for hardware development in the aerospace domain.
* ARP4754A/ARP4761 safety lifecycle 🔴
  .. admonition::
     ARP4754A/ARP4761 is the standard for safety lifecycle management in the aerospace domain.

### Medical 💊

* IEC 62304 (software lifecycle) 🟢
  .. note::
     IEC 62304 is the standard for software lifecycle management in the medical domain.
* ISO 14971 (risk management) 🟡
  .. important::
     ISO 14971 is the standard for risk management in the medical domain.
* IEC 60601 safety context 🔴
  .. warning::
     IEC 60601 is the standard for safety context in the medical domain.

Evidence Expectations
---------------------

### Requirement Traceability

* Trace requirements from system intent to test verdict.
  .. note::
     Requirement traceability is essential for verification and validation.
* Verify requirement-to-test linkage.
  .. important::
     Requirement-to-test linkage ensures that tests are relevant and effective.

### Verification Artifacts

* Verification artifacts with timestamps, tool versions, and ownership.
  .. admonition::
     Verification artifacts should be well-documented and easily accessible.
* Include structural evidence (coverage/timing/object-code where applicable).
  .. note::
     Structural evidence provides insight into the system's internal behavior.

### Defect Triage History

* Track failed/blocked tests to corrective action.
  .. important::
     Defect triage history helps identify and address issues promptly.
* Document defect triage history and closure rationale.
  .. warning::
     Inadequate defect triage history can lead to missed opportunities for improvement.

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
  .. note::
     Requirements baseline provides a foundation for verification and validation.
* Verify test matrix, logs, traces, and signed summary report.
  .. important::
     Test matrix and logs ensure that tests are comprehensive and effective.

### Static-Analysis Outputs

* Include static-analysis outputs and deviation justifications.
  .. admonition::
     Static-analysis outputs provide insight into the system's internal behavior.
* Verify release decision note with risk disposition.
  .. warning::
     Inadequate release decision note can lead to missed opportunities for improvement.

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
  .. note::
     Embedded systems are critical in various domains, including automotive, aerospace, and medical.

### Phase Focus

* Cross-Phase verification and validation.
  .. important::
     Cross-Phase verification and validation ensure that the system meets requirements throughout its lifecycle.

### Evidence Priorities

* Functional correctness
  .. note::
     Functional correctness is essential for system reliability and safety.
* Timing behavior
  .. important::
     Timing behavior is critical in real-time systems.
* Robustness
  .. admonition::
     Robustness ensures that the system can withstand various environmental conditions.
* Traceability
  .. warning::
     Inadequate traceability can lead to missed opportunities for improvement.

### Patterns

* Baseline-first comparison
  .. note::
     Baseline-first comparison ensures that changes are properly assessed.
* Fixed acceptance thresholds
  .. important::
     Fixed acceptance thresholds provide a clear understanding of what is acceptable.
* Deterministic reruns
  .. admonition::
     Deterministic reruns ensure that tests are repeatable and reliable.

### Anti-Patterns

* Post-hoc threshold tuning
  .. warning::
     Post-hoc threshold tuning can lead to missed opportunities for improvement.
* Missing raw artifacts
  .. important::
     Missing raw artifacts can make it difficult to reproduce results.
* Incomplete negative-path checks
  .. admonition::
     Incomplete negative-path checks can lead to missed opportunities for improvement.

### Pitfalls

* Hidden assumptions
  .. note::
     Hidden assumptions can lead to incorrect conclusions.
* Interface timing drift
  .. important::
     Interface timing drift can lead to system failures.
* Weak requirement-to-test linkage
  .. warning::
     Weak requirement-to-test linkage can lead to missed opportunities for improvement.

### Review Heuristic

* If a claim cannot be tied to an artifact, mark confidence as provisional.
  .. note::
     Tying claims to artifacts ensures that evidence is reliable and trustworthy.

### Checklist Extension

* Capture residual risk, ownership, and next action for each unresolved item.
  .. important::
     Residual risk, ownership, and next action ensure that issues are properly addressed.

References
-----------

* ISO 26262:2018 - Road vehicles -- Functional safety
* ISO 21434:2020 - Road vehicles -- Cybersecurity engineering
* DO-178C:2012 - Software considerations in airborne systems and equipment certification
* DO-254:2010 - Design assurance guidance for airborne electronic hardware
* ARP4754A:2010 - Guidelines for development of civil aircraft and systems
* ARP4761:2010 - Guidelines and methods for conducting the failure modes, effects and criticality analysis (FMECA) of a system
* IEC 62304:2006 - Medical device software -- Software life cycle processes
* IEC 60601:2005 - Medical electrical equipment -- Part 1: General requirements for basic safety and essential performance
* ISO 14971:2019 - Medical devices -- Application of risk management to medical devices

.. note::
   This cheat sheet is intended to provide a quick reference for embedded systems verification and validation. It is not a comprehensive guide and should be used in conjunction with relevant domain standards and guidelines.

.. warning::
   Failure to follow domain standards and guidelines may result in non-compliance and potential safety risks.

.. important::
   This cheat sheet is subject to change and may not reflect the latest updates to domain standards and guidelines.

.. admonition::
   This cheat sheet is intended for informational purposes only and should not be used as a substitute for professional advice or guidance.

Table of Evidence Expectations
---------------------------

| Evidence Type | Description | Priority |
| --- | --- | --- |
| Requirement Traceability | Trace requirements from system intent to test verdict | 🟢 |
| Verification Artifacts | Verification artifacts with timestamps, tool versions, and ownership | 🟢 |
| Defect Triage History | Track failed/blocked tests to corrective action | 🟡 |
| Baseline-First Comparison | Compare changes against baseline | 🟡 |
| Fixed Acceptance Thresholds | Establish clear acceptance thresholds | 🟡 |
| Deterministic Reruns | Ensure repeatable and reliable tests | 🟢 |

Table of Patterns and Anti-Patterns
----------------------------------

| Pattern/Anti-Pattern | Description | Priority |
| --- | --- | --- |
| Baseline-First Comparison | Compare changes against baseline | 🟡 |
| Fixed Acceptance Thresholds | Establish clear acceptance thresholds | 🟡 |
| Deterministic Reruns | Ensure repeatable and reliable tests | 🟢 |
| Post-Hoc Threshold Tuning | Avoid adjusting thresholds after the fact | 🔴 |
| Missing Raw Artifacts | Ensure all raw artifacts are available | 🔴 |
| Incomplete Negative-Path Checks | Ensure all negative paths are tested | 🔴 |

Table of Pitfalls
-----------------

| Pitfall | Description | Priority |
| --- | --- | --- |
| Hidden Assumptions | Avoid making assumptions without evidence | 🔴 |
| Interface Timing Drift | Ensure interface timing is consistent | 🔴 |
| Weak Requirement-to-Test Linkage | Ensure strong linkage between requirements and tests | 🔴 |

Table of Review Heuristics
-------------------------

| Heuristic | Description | Priority |
| --- | --- | --- |
| Tying Claims to Artifacts | Ensure claims are tied to reliable evidence | 🟢 |
| Capturing Residual Risk | Ensure residual risk is properly addressed | 🟡 |
| Documenting Ownership and Next Action | Ensure ownership and next action are clear | 🟡 |
