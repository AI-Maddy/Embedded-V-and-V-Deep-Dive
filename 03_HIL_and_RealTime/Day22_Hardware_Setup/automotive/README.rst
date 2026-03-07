Automotive Focus — Day22 Hardware Setup 🚗🔧
===========================================

Objective 🎯
-----------
Apply this day in **Automotive** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that all hardware components are thoroughly tested and validated to meet the highest safety standards, ensuring a reliable and safe driving experience.

Phase Context 🔍
----------------
Phase: **HIL**  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **automotive verification workflow**.  

Domain Constraints 🚧
---------------------
- Compliance baseline: **ISO 26262 (ASIL) + ISO 21434**  
- Key hazard profile: unintended acceleration/deceleration, loss of stability, braking faults  
- Interface landscape: CAN, LIN, FlexRay, Automotive Ethernet  

Domain-Specific Examples 🛠️
------------------------------
- **Nominal** 🟢: Adaptive cruise and speed regulation under normal traffic conditions.  
- **Boundary** 🟡: Dense stop-and-go scenarios with tight headway and timing limits.  
- **Fault** 🔴: Sensor dropout and invalid CAN frame injection leading to potential system failure.  

Patterns 🔄
----------
- Derive acceptance thresholds from hazard-linked requirements to ensure safety and reliability.
- Keep interface timing contracts explicit and reviewable to facilitate traceability and accountability.
- Compare nominal and stressed traces against the same baseline to identify discrepancies and ensure robustness.

Anti-Patterns ❌
----------------
- Generic test claims without domain hazard mapping, which can lead to unaddressed risks.
- Pass/fail decisions without quantitative thresholds, making it difficult to assess true performance.
- Evidence summaries without raw artifact references, leading to gaps in traceability and accountability.

Pitfalls ⚠️
-----------
- Hidden assumptions in environment or calibration setup can lead to unexpected results.
- Missing negative-path scenarios for high-criticality behavior can result in untested vulnerabilities.
- Incomplete traceability from requirement to verdict can undermine confidence in the validation process.

Best Practices 🌟
-----------------
- Tag every artifact with domain requirement IDs to ensure traceability and accountability.
- Capture timing + functional evidence in the same run package to streamline the validation process.
- Record residual risk and ownership before closure to ensure all potential issues are addressed.

Heuristics 🧠
-------------
- If a domain hazard is untested, confidence is provisional; further testing is required.
- If rerun differs unexpectedly, investigate determinism first to identify potential issues.
- If evidence is indirect, reduce verdict confidence level to reflect uncertainty.

Checklist ✅
-----------
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
--------------------------------
- **Nominal** 🟢: 
  - **GIVEN** the system is in normal traffic conditions, 
  - **WHEN** the adaptive cruise control is activated, 
  - **THEN** the vehicle maintains a safe distance and speed.

- **Boundary** 🟡: 
  - **GIVEN** the system is in a dense stop-and-go traffic scenario, 
  - **WHEN** the vehicle approaches a stopping point, 
  - **THEN** the braking system engages effectively without exceeding timing limits.

- **Fault** 🔴: 
  - **GIVEN** a sensor dropout occurs, 
  - **WHEN** an invalid CAN frame is injected, 
  - **THEN** the system should enter a safe state or provide a fault indication.

.. note:: For further details on compliance and safety standards, refer to **ISO 26262** and **ISO 21434** documentation to ensure all requirements are met.

.. important:: Always ensure that all test results are documented and reviewed to maintain compliance and safety standards.

.. warning:: Be vigilant for any hidden assumptions that may affect the validation process, as they can lead to significant risks if left unaddressed.
