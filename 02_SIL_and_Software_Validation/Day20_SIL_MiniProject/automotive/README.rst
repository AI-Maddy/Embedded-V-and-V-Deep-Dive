Automotive Focus — Day20 SIL MiniProject 🚗💡
==============================================

Objective 🎯
-----------
Apply this day in **Automotive** context with explicit safety, compliance, and evidence expectations. Our goal is to ensure that all software components meet the highest standards of safety and reliability, aligning with industry regulations and best practices.

Phase Context 🔍
----------------
Phase: **SIL (Software-in-the-Loop)**  
Primary focus: **software-level correctness, robustness, and structural evidence**.  
Section focus: **automotive verification workflow**.  

Domain Constraints ⚠️
----------------------
- Compliance baseline: **ISO 26262 (ASIL) + ISO 21434**  
- Key hazard profile: unintended acceleration/deceleration, loss of stability, braking faults  
- Interface landscape: CAN, LIN, FlexRay, Automotive Ethernet  

Domain-Specific Examples 📊
-----------------------------
- **Nominal (🟢)**: Adaptive cruise and speed regulation under normal traffic conditions.  
- **Boundary (🟡)**: Dense stop-and-go scenarios with tight headway and timing limits.  
- **Fault (🔴)**: Sensor dropout and invalid CAN frame injection.  

Patterns 🔄
---------
- Derive acceptance thresholds from hazard-linked requirements to ensure that safety-critical functions are validated against real-world scenarios.
- Keep interface timing contracts explicit and reviewable to maintain clarity and accountability in communication between components.
- Compare nominal and stressed traces against the same baseline to identify discrepancies and ensure robustness.

Anti-Patterns 🚫
----------------
- Generic test claims without domain hazard mapping lead to insufficient safety validation.
- Pass/fail decisions without quantitative thresholds can result in ambiguous outcomes.
- Evidence summaries without raw artifact references diminish the reliability of the validation process.

Pitfalls ⚠️
-----------
- Hidden assumptions in environment or calibration setup can lead to unexpected failures.
- Missing negative-path scenarios for high-criticality behavior can result in untested vulnerabilities.
- Incomplete traceability from requirement to verdict undermines the validation integrity.

Best Practices 🌟
-----------------
- Tag every artifact with domain requirement IDs to facilitate traceability and accountability.
- Capture timing + functional evidence in the same run package to streamline validation efforts.
- Record residual risk and ownership before closure to ensure that all risks are acknowledged and addressed.

Heuristics 💡
-------------
- If a domain hazard is untested, confidence is provisional; always seek to validate all potential risks.
- If rerun differs unexpectedly, investigate determinism first to ensure consistent results.
- If evidence is indirect, reduce verdict confidence level to reflect uncertainty.

Checklist ✅
-----------
.. list-table:: Pre-Review Checklist
   :widths: 20 80
   :header-rows: 1

   * - Item
     - Description
   * - Domain hazard coverage
     - Coverage is explicit and documented.
   * - Compliance references
     - References are mapped to evidence.
   * - Results documentation
     - Nominal/boundary/fault results are all documented.
   * - Residual risks
     - Residual risks and next actions are assigned.

GIVEN / WHEN / THEN Scenarios 📜
-------------------------------
.. note:: Use the following templates to define scenarios for testing.

- **Nominal (🟢)**:  
  **GIVEN** a vehicle in adaptive cruise mode,  
  **WHEN** the traffic is flowing normally,  
  **THEN** the vehicle maintains a safe distance and speed.

- **Boundary (🟡)**:  
  **GIVEN** a vehicle in stop-and-go traffic,  
  **WHEN** the lead vehicle suddenly brakes,  
  **THEN** the vehicle responds appropriately without collision.

- **Fault (🔴)**:  
  **GIVEN** a vehicle experiencing sensor dropout,  
  **WHEN** an invalid CAN frame is injected,  
  **THEN** the vehicle enters a safe state without unintended acceleration.

.. important:: Always ensure that all scenarios are tested thoroughly to maintain safety and compliance with relevant standards.

References 📚
------------
- ISO 26262: Road vehicles — Functional safety
- ISO 21434: Road vehicles — Cybersecurity engineering
- DO-178C: Software Considerations in Airborne Systems and Equipment Certification
- IEC 62304: Medical device software — Software life cycle processes
- ARP4754A: Guidelines for Development of Civil Aircraft and Systems
- ASPICE: Automotive SPICE Process Assessment Model

By adhering to these guidelines and best practices, we can ensure that our software-in-the-loop validation process is robust, compliant, and effective in mitigating risks associated with automotive systems.
