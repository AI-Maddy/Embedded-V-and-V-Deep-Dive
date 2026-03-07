🩺 Requirements — Medical 🩺
=============================

🎯 Purpose 🎯
-------------
Document **Medical**-specific details for Day02 Traceability and TestDesign with focus on use-case intent, assumptions, and acceptance criteria.

.. note::
   This document aligns with **Model-in-the-Loop (MIL)** phase objectives, ensuring traceability and robust test design for medical systems per IEC 62304 and ISO 14971 guidelines.

🌐 Domain Alignment 🌐
-----------------------

- **Standards Reference**:
  - IEC 62304: Software lifecycle processes
  - ISO 14971: Risk management for medical devices
  - IEC 60601: Safety and performance of medical electrical equipment
- **Critical Hazards**:
  - Incorrect dosage delivery 🔴
  - Missed alarm 🟡
  - Unsafe therapy continuation 🔴
- **Relevant Interfaces**:
  - Device buses 🟢
  - Sensor links 🟡
  - Alarm/event channels 🔴

.. important::
   Ensure all hazards are mitigated per IEC 62304 and ISO 14971 guidelines, with traceable links to requirements and test artifacts.

🧪 Examples 🧪
--------------

### 🟢 Nominal Scenario 🟢

GIVEN validated sensor feedback  
WHEN therapy control is initiated  
THEN the system delivers accurate therapy dosage within specified limits.

### 🟡 Boundary Scenario 🟡

GIVEN near-threshold dosing conditions  
WHEN alarm escalation timing is triggered  
THEN the system raises an alarm within the prescribed response time.

### 🔴 Fault Scenario 🔴

GIVEN a sensor spike/dropout  
WHEN an actuator command is issued  
THEN the system rejects unsafe commands and logs the fault for further analysis.

📐 Patterns 📐
-------------

- **Requirement-Linked Checks**:
  - Ensure every test scenario is tied to a specific requirement.
- **Timing and Functional Outcomes**:
  - Track both timing behavior and functional correctness in test results.
- **Setup Reproducibility**:
  - Maintain explicit constraints for reproducible test setups.

🚫 Anti-Patterns 🚫
-----------------

- Domain-agnostic statements without measurable criteria.
- Ignoring interface constraints during analysis.
- Closing findings without residual risk statement.

⚠️ Pitfalls ⚠️
-------------

- Missing sensor/actuator fault variants 🔴
- Weak traceability from objective to artifact 🟡
- Non-repeatable reruns from uncontrolled configuration drift 🔴

✅ Checklist ✅
-------------

☐ Scope and assumptions are explicit.  
☐ Acceptance criteria are quantitative.  
☐ Evidence set is complete and auditable.  
☐ Follow-up actions are prioritized.  
☐ Residual risks are documented.  
☐ Ownership and next actions are assigned for unresolved items.

📘 Additional Deep-Dive Notes 📘
---------------------------------

- **Domain Focus**: Medical 🩺  
- **Phase Focus**: MIL 🧩  
- **Evidence Priorities**:
  - Functional correctness 🟢  
  - Timing behavior 🟡  
  - Robustness 🔴  
  - Traceability 🟢  
- **Patterns**:
  - Baseline-first comparison 🟢  
  - Fixed acceptance thresholds 🟡  
  - Deterministic reruns 🟢  
- **Anti-Patterns**:
  - Post-hoc threshold tuning 🔴  
  - Missing raw artifacts 🟡  
  - Incomplete negative-path checks 🔴  
- **Pitfalls**:
  - Hidden assumptions 🟡  
  - Interface timing drift 🔴  
  - Weak requirement-to-test linkage 🟡  

🧪 Example Expansion 🧪
-----------------------

Include **one nominal**, **one boundary**, and **one fault scenario** per objective to ensure comprehensive coverage.

🔍 Review Heuristic 🔍
---------------------

If a claim cannot be tied to an artifact, mark confidence as **provisional** and escalate for further review.

🌟 Traceability Mnemonic: **MEDICS** 🌟
--------------------------------------

- **M**: Map requirements to tests explicitly.  
- **E**: Evaluate timing and functional outcomes.  
- **D**: Document evidence comprehensively.  
- **I**: Identify residual risks and ownership.  
- **C**: Confirm reproducibility of test setups.  
- **S**: Safeguard against domain-specific hazards.

📊 Tabular Summary 📊
---------------------

.. list-table:: Medical V&V Traceability Summary
   :header-rows: 1

   * - **Aspect**
     - **Severity**
     - **Standard Reference**
     - **Notes**
   * - Incorrect dosage delivery
     - 🔴 Critical
     - IEC 62304, ISO 14971
     - Requires robust validation and fault handling.
   * - Missed alarm
     - 🟡 Moderate
     - IEC 60601
     - Address timing constraints explicitly.
   * - Unsafe therapy continuation
     - 🔴 Critical
     - IEC 62304, ISO 14971
     - Ensure therapy termination mechanisms are fail-safe.
   * - Device buses
     - 🟢 Low
     - IEC 60601
     - Verify communication reliability.
   * - Sensor links
     - 🟡 Moderate
     - IEC 62304
     - Test for boundary conditions and fault scenarios.
   * - Alarm/event channels
     - 🔴 Critical
     - ISO 14971
     - Validate escalation and response timing.

.. admonition:: Final Note
   :class: tip

   Always align test design with domain-specific standards and ensure traceability from requirements to test artifacts for robust verification and validation.
