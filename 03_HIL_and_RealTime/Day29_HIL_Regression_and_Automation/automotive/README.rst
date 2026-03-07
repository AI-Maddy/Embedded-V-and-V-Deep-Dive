Automotive Focus — Day29 HIL Regression and Automation 🚗💨
==========================================================

Objective 🎯
---------
Apply this day in **Automotive** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that all hardware-in-the-loop (HIL) tests are conducted with a focus on safety-critical systems, adhering to the highest standards of verification and validation. This aligns with our mnemonic acronym **HIL-SAFE** (HIL Integration for Safety Assurance and Functional Evaluation).

Phase Context 🔍
-------------
Phase: **HIL**  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **automotive verification workflow**.  

Domain Constraints 🚧
------------------
- Compliance baseline: **ISO 26262 (ASIL) + ISO 21434**
- Key hazard profile: unintended acceleration/deceleration, loss of stability, braking faults
- Interface landscape: CAN, LIN, FlexRay, Automotive Ethernet

Domain-Specific Examples 📝
------------------------
- **Nominal** 🟢: Adaptive cruise and speed regulation under normal traffic conditions.
- **Boundary** 🟡: Dense stop-and-go scenarios with tight headway and timing limits.
- **Fault** 🔴: Sensor dropout and invalid CAN frame injection.

Patterns 🔄
--------
- Derive acceptance thresholds from hazard-linked requirements.
- Keep interface timing contracts explicit and reviewable.
- Compare nominal and stressed traces against the same baseline.

Anti-Patterns 🚫
-------------
- Generic test claims without domain hazard mapping.
- Pass/fail decisions without quantitative thresholds.
- Evidence summaries without raw artifact references.

Pitfalls ⚠️
--------
- Hidden assumptions in environment or calibration setup.
- Missing negative-path scenarios for high-criticality behavior.
- Incomplete traceability from requirement to verdict.

Best Practices 🌟
--------------
- Tag every artifact with domain requirement IDs.
- Capture timing + functional evidence in the same run package.
- Record residual risk and ownership before closure.

Heuristics 🧠
----------
- If a domain hazard is untested, confidence is provisional.
- If rerun differs unexpectedly, investigate determinism first.
- If evidence is indirect, reduce verdict confidence level.

Checklist ✅
---------
.. list-table:: Pre-Review Checklist
   :header-rows: 1

   * - Item
     - Status
   * - Domain hazard coverage is explicit.
     - ☐
   * - Compliance references are mapped to evidence.
     - ☐
   * - Nominal/boundary/fault results are all documented.
     - ☐
   * - Residual risks and next actions are assigned.
     - ☐

GIVEN / WHEN / THEN Scenarios 📜
-------------------------------
- **Nominal Scenario** 🟢:
  - **GIVEN** the vehicle is in adaptive cruise mode,
  - **WHEN** the traffic conditions are normal,
  - **THEN** the vehicle maintains a safe distance and speed.

- **Boundary Scenario** 🟡:
  - **GIVEN** the vehicle is in stop-and-go traffic,
  - **WHEN** the headway is minimal,
  - **THEN** the system must respond without unintended acceleration.

- **Fault Scenario** 🔴:
  - **GIVEN** a sensor dropout occurs,
  - **WHEN** an invalid CAN frame is injected,
  - **THEN** the system should enter a safe state without loss of control.

.. note::
   This document aligns with the following standards: ISO 26262, ISO 21434, and other relevant automotive safety standards. Always ensure compliance with these guidelines during the HIL testing phase.

.. important::
   Remember that thorough documentation and traceability are essential for compliance and safety in automotive systems. Each test must be backed by clear evidence and linked to specific requirements.

.. warning::
   Failing to address high-criticality scenarios can lead to severe safety risks. Always prioritize testing for unintended behaviors and ensure that all potential hazards are accounted for in your verification strategy.
