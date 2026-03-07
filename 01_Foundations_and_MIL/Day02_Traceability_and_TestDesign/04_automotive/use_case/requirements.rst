Requirements 🚗 — Automotive
============================

Purpose 🎯
---------
Document **Automotive**-specific details for Day02 Traceability and TestDesign with focus on use-case intent, assumptions, and acceptance criteria. This document aligns with **ISO 26262**, **ISO 21434**, and other relevant standards for Model-in-the-Loop (MIL) verification.

Domain Alignment 🌐
-------------------
- **Standards Referenced**:
  - ISO 26262: Functional safety for road vehicles (ASIL determination and safety goals).
  - ISO 21434: Cybersecurity engineering for automotive systems.
  - ASPICE: Process capability for automotive software development.
- **Critical Hazards**:
  - 🟢 Nominal: Adaptive cruise control maintaining safe distance.
  - 🟡 Boundary: Stop-and-go traffic with tight timing constraints.
  - 🔴 Fault: Sensor dropout leading to invalid CAN frame injection.
- **Relevant Interfaces**:
  - CAN (Controller Area Network)
  - LIN (Local Interconnect Network)
  - FlexRay
  - Automotive Ethernet

Mnemonic Acronym 🚦
-------------------
**TRACE**: Testable Requirements Aligned with Critical Evidence
- **T**: Traceability from requirement to test artifact.
- **R**: Robustness under nominal, boundary, and fault conditions.
- **A**: Alignment with domain-specific standards.
- **C**: Coverage of all critical hazards and interfaces.
- **E**: Evidence-based validation and verification.

Examples 📖
-----------
.. note::
   **Scenario Templates** for MIL Verification:

   **Nominal Scenario 🟢**:
   GIVEN: Adaptive cruise control is activated under normal traffic conditions.
   WHEN: The lead vehicle decelerates gradually.
   THEN: The system adjusts speed smoothly to maintain a safe distance.

   **Boundary Scenario 🟡**:
   GIVEN: Stop-and-go traffic with tight headway constraints.
   WHEN: The lead vehicle stops abruptly and resumes movement within 2 seconds.
   THEN: The system avoids collision and resumes speed regulation within 1 second.

   **Fault Scenario 🔴**:
   GIVEN: A sensor dropout occurs during operation.
   WHEN: An invalid CAN frame is injected into the network.
   THEN: The system enters a fail-safe mode and alerts the driver.

Patterns 🧩
-----------
- **Requirement-Linked Checks**:
  - Ensure every test case is traceable to a specific requirement.
  - Use tools like DOORS or Polarion for traceability management.
- **Timing and Functional Outcomes**:
  - Verify both timing constraints (e.g., response times) and functional correctness.
- **Setup Reproducibility**:
  - Define explicit constraints for test environment setup to ensure repeatability.

Anti-Patterns 🚫
----------------
.. warning::
   Avoid these practices to ensure robust MIL validation:

   - **Domain-Agnostic Statements**: Requirements lacking measurable criteria tied to automotive-specific hazards.
   - **Interface Blindness**: Ignoring constraints related to CAN, LIN, or FlexRay during analysis.
   - **Premature Closure**: Closing findings without documenting residual risks or follow-up actions.

Pitfalls ⚠️
------------
.. important::
   Common pitfalls to avoid:

   - **Sensor/Actuator Fault Variants**: Missing test cases for sensor failures or actuator malfunctions.
   - **Weak Traceability**: Failing to link objectives to artifacts (e.g., test cases, logs).
   - **Configuration Drift**: Non-repeatable test reruns due to uncontrolled environment changes.

Checklist ✅
------------
.. admonition:: Pre-Review Checklist
   :class: tip

   Before proceeding, ensure the following:

   - ☐ Scope and assumptions are explicit and documented.
   - ☐ Acceptance criteria are quantitative and measurable.
   - ☐ Evidence set is complete, auditable, and aligned with ISO 26262/21434.
   - ☐ Follow-up actions for unresolved items are prioritized and tracked.

Additional Deep-Dive Notes 📌
-----------------------------
- **Domain Focus**: Automotive MIL validation.
- **Phase Focus**: Model-in-the-Loop testing for functional correctness, timing behavior, and robustness.
- **Evidence Priorities**:
  - Functional correctness under nominal and fault conditions.
  - Timing behavior compliance with ISO 26262 timing requirements.
  - Robustness against cybersecurity threats (ISO 21434).
  - Traceability from requirement to test artifact.
- **Patterns**:
  - Baseline-first comparison for deterministic validation.
  - Fixed acceptance thresholds for measurable criteria.
  - Controlled environment for repeatable test runs.
- **Anti-Patterns**:
  - Post-hoc threshold tuning without justification.
  - Missing raw artifacts (e.g., logs, traces) for auditability.
  - Incomplete negative-path checks for fault scenarios.
- **Pitfalls**:
  - Hidden assumptions leading to invalid test results.
  - Interface timing drift causing unpredictable behavior.
  - Weak linkage between requirements and test cases.
- **Example Expansion**:
  - Include one nominal 🟢, one boundary 🟡, and one fault 🔴 scenario per objective.
- **Review Heuristic**:
  - If a claim cannot be tied to an artifact, mark confidence as provisional.
- **Checklist Extension**:
  - Capture residual risk, ownership, and next actions for unresolved items.

Tabular Summary 📊
------------------
.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - **Category**
     - **Description**
     - **Examples**
   * - Nominal 🟢
     - Normal operation under expected conditions.
     - Adaptive cruise control maintaining safe distance.
   * - Boundary 🟡
     - Edge cases with tight constraints or high variability.
     - Stop-and-go traffic with tight headway limits.
   * - Fault 🔴
     - Scenarios with injected errors or system failures.
     - Sensor dropout, invalid CAN frame injection.

.. note::
   For further guidance, refer to **ISO 26262**, **ISO 21434**, and **ASPICE** documentation.
