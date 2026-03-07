Automotive Focus — Day30 Final Capstone 🚗💻
=============================================

Objective
---------
🟢 **Verify Automotive Safety with Evidence** 📊

Phase Context
-------------
🟡 **HIL Phase** 🕒
Primary focus: **hardware-integrated timing and interface confidence** 💻.
Section focus: **automotive verification workflow** 📈.

Domain Constraints
------------------
🔴 **Compliance Baseline** 📝: **ISO 26262 (ASIL) + ISO 21434**.
Key hazard profile: unintended acceleration/deceleration, loss of stability, braking faults 🚨.
Interface landscape: CAN, LIN, FlexRay, Automotive Ethernet 📈.

Domain-Specific Mnemonic
-------------------------
**CARE** 🤝
- **C**: **Compliance** to standards (ISO 26262, ISO 21434)
- **A**: **Assurance** of safety through evidence
- **R**: **Risk** management and mitigation
- **E**: **Evidence**-driven decision-making

Domain-Specific Examples
------------------------
🟢 **Nominal Scenario** 🚗
- Adaptive cruise and speed regulation under normal traffic.
🟡 **Boundary Scenario** 🚗
- Dense stop-and-go with tight headway and timing limits.
🔴 **Fault Scenario** 🚨
- Sensor dropout and invalid CAN frame injection.

Patterns
--------
🟢 **Acceptance Thresholds** 📊
- Derive acceptance thresholds from hazard-linked requirements.
🟡 **Interface Timing Contracts** 🕒
- Keep interface timing contracts explicit and reviewable.
🟢 **Nominal and Stressed Traces** 📈
- Compare nominal and stressed traces against the same baseline.

Anti-Patterns
-------------
🔴 **Generic Test Claims** 🚫
- Generic test claims without domain hazard mapping.
🔴 **Pass/Fail Decisions** 🚫
- Pass/fail decisions without quantitative thresholds.
🔴 **Evidence Summaries** 🚫
- Evidence summaries without raw artifact references.

Pitfalls
--------
🔴 **Hidden Assumptions** 🤔
- Hidden assumptions in environment or calibration setup.
🔴 **Missing Negative-Path Scenarios** 🚨
- Missing negative-path scenarios for high-criticality behavior.
🔴 **Incomplete Traceability** 📝
- Incomplete traceability from requirement to verdict.

Best Practices
--------------
🟢 **Artifact Tagging** 📝
- Tag every artifact with domain requirement IDs.
🟡 **Timing and Functional Evidence** 📊
- Capture timing + functional evidence in the same run package.
🟢 **Residual Risk and Ownership** 📝
- Record residual risk and ownership before closure.

Heuristics
----------
🟢 **Provisional Confidence** 🤝
- If a domain hazard is untested, confidence is provisional.
🟡 **Investigate Determinism** 🕒
- If rerun differs unexpectedly, investigate determinism first.
🟢 **Reduced Verdict Confidence** 📊
- If evidence is indirect, reduce verdict confidence level.

Checklist
---------
☐ **Domain Hazard Coverage** 📝
☐ **Compliance References** 📝
☐ **Nominal/Boundary/Fault Results** 📊
☐ **Residual Risks and Next Actions** 📝

Admonitions
------------

.. note::
    This document is intended to provide guidance on automotive safety verification and validation.

.. warning::
    Failure to comply with ISO 26262 and ISO 21434 may result in safety-critical system failures.

.. important::
    Evidence-driven decision-making is critical in automotive safety verification and validation.

.. admonition::
    This document is not a substitute for professional expertise in automotive safety verification and validation.

Table: Compliance References
=============================

+-----------------------+---------------------------------------+
| Standard             | Description                           |
+=======================+=======================================+
| ISO 26262 (ASIL)     | Functional safety standard for automotive |
|                       | systems                                |
+-----------------------+---------------------------------------+
| ISO 21434            | Cybersecurity standard for automotive  |
|                       | systems                                |
+-----------------------+---------------------------------------+

Table: Domain Hazard Coverage
=============================

| Hazard ID | Description | Covered |
|-----------+-------------+--------|
| HAZ-001   | Unintended  | Yes    |
|           | acceleration |        |
|-----------+-------------+--------|
| HAZ-002   | Loss of     | Yes    |
|           | stability    |        |
|-----------+-------------+--------|
| HAZ-003   | Braking     | Yes    |
|           | faults      |        |
