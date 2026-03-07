🚗💻 Automotive Focus — Day30 Final Capstone 🚗💻
=====================================================

🔹 **Objective** 🔹
-------------------

🟢 **Verify Automotive Safety with Evidence** 📊
=====================================================

The primary objective of this capstone project is to verify automotive safety using evidence-based methods. This involves a thorough analysis of the automotive system's hardware and software components to ensure compliance with relevant safety standards.

🔹 **Phase Context** 🔹
----------------------

🟡 **HIL Phase** 🕒
-----------------

The Hardware-in-the-Loop (HIL) phase is a critical stage in the automotive verification and validation process. During this phase, the focus is on integrating hardware components with the system's software to ensure seamless interaction and compliance with safety standards.

🔹 **Domain Constraints** 🔹
-------------------------

🔴 **Compliance Baseline** 📝: **ISO 26262 (ASIL) + ISO 21434**
---------------------------------------------------------

The automotive domain is subject to strict safety standards, including ISO 26262 (ASIL) and ISO 21434. These standards provide guidelines for ensuring the functional safety and cybersecurity of automotive systems.

.. note::
    Compliance with these standards is mandatory to ensure the safety and reliability of automotive systems.

🔹 **Domain-Specific Mnemonic** 🔹
---------------------------------

**CARE** 🤝
------------

To ensure the safety and reliability of automotive systems, we use the **CARE** mnemonic:

- **C**: **Compliance** to standards (ISO 26262, ISO 21434)
- **A**: **Assurance** of safety through evidence
- **R**: **Risk** management and mitigation
- **E**: **Evidence**-driven decision-making

🔹 **Domain-Specific Examples** 🔹
---------------------------------

### 🟢 **Nominal Scenario** 🚗

GIVEN: A vehicle is operating under normal traffic conditions.
WHEN: The adaptive cruise control system is engaged.
THEN: The vehicle maintains a safe distance from the preceding vehicle.

### 🟡 **Boundary Scenario** 🚗

GIVEN: A vehicle is operating in dense stop-and-go traffic.
WHEN: The adaptive cruise control system is engaged.
THEN: The vehicle maintains a safe distance from the preceding vehicle and responds to sudden stops.

### 🔴 **Fault Scenario** 🚨

GIVEN: A vehicle's sensor system fails.
WHEN: The adaptive cruise control system is engaged.
THEN: The vehicle's emergency braking system is activated to prevent a collision.

🔹 **Patterns** 🔹
------------------

### 🟢 **Acceptance Thresholds** 📊

Derive acceptance thresholds from hazard-linked requirements to ensure that the system meets safety standards.

### 🟡 **Interface Timing Contracts** 🕒

Keep interface timing contracts explicit and reviewable to ensure seamless interaction between hardware and software components.

### 🟢 **Nominal and Stressed Traces** 📈

Compare nominal and stressed traces against the same baseline to identify potential safety issues.

🔹 **Anti-Patterns** 🔹
----------------------

### 🔴 **Generic Test Claims** 🚫

Avoid making generic test claims without domain hazard mapping, as this can lead to inadequate testing and potential safety issues.

### 🔴 **Pass/Fail Decisions** 🚫

Avoid making pass/fail decisions without quantitative thresholds, as this can lead to subjective and potentially incorrect conclusions.

### 🔴 **Evidence Summaries** 🚫

Avoid creating evidence summaries without raw artifact references, as this can lead to incomplete and inaccurate information.

🔹 **Pitfalls** 🔹
------------------

### 🔴 **Hidden Assumptions** 🤔

Be aware of hidden assumptions in environment or calibration setup, as these can lead to inaccurate test results and potential safety issues.

### 🔴 **Missing Negative-Path Scenarios** 🚨

Ensure that negative-path scenarios are included in testing to identify potential safety issues and mitigate risks.

### 🔴 **Incomplete Traceability** 📝

Ensure that there is complete traceability from requirement to verdict to maintain the integrity of the testing process.

🔹 **Best Practices** 🔹
-----------------------

### 🟢 **Artifact Tagging** 📝

Tag every artifact with domain requirement IDs to maintain traceability and ensure compliance with safety standards.

### 🟡 **Timing and Functional Evidence** 📊

Capture timing and functional evidence in the same run package to ensure comprehensive testing and analysis.

### 🟢 **Residual Risk and Ownership** 📝

Record residual risk and ownership before closure to ensure that potential safety issues are addressed and mitigated.

🔹 **Heuristics** 🔹
-------------------

### 🟢 **Provisional Confidence** 🤝

If a domain hazard is untested, confidence is provisional, and additional testing is required to ensure safety and reliability.

### 🟡 **Investigate Determinism** 🕒

If rerun differs unexpectedly, investigate determinism first to identify potential issues with the testing process.

### 🟢 **Reduced Verdict Confidence** 📊

If evidence is indirect, reduce verdict confidence level to ensure that conclusions are accurate and reliable.

🔹 **Checklist** 🔹
------------------

☐ **Domain Hazard Coverage** 📝
☐ **Compliance References** 📝
☐ **Nominal/Boundary/Fault Results** 📊
☐ **Residual Risks and Next Actions** 📝

.. warning::
    Failure to comply with ISO 26262 and ISO 21434 may result in safety-critical system failures.

.. important::
    Evidence-driven decision-making is critical in automotive safety verification and validation.

.. admonition::
    This document is not a substitute for professional expertise in automotive safety verification and validation.

🔹 **Compliance References** 🔹
------------------------------

.. list-table::
    :widths: 20 80
    :stub-columns: 1

    * - Standard
      - Description
    * - ISO 26262 (ASIL)
      - Functional safety standard for automotive systems
    * - ISO 21434
      - Cybersecurity standard for automotive systems

🔹 **Domain Hazard Coverage** 🔹
------------------------------

.. list-table::
    :widths: 20 40 20
    :stub-columns: 1

    * - Hazard ID
      - Description
      - Covered
    * - HAZ-001
      - Unintended acceleration
      - Yes
    * - HAZ-002
      - Loss of stability
      - Yes
    * - HAZ-003
      - Braking faults
      - Yes
