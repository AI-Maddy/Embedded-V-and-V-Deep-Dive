Automotive Focus — Day27 HIL FaultInjection 🚗💨
=================================================

Objective 🎯
-----------
Apply this day in **Automotive** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that all components of the system are rigorously tested to meet safety standards and operational reliability. This is crucial for maintaining trust in automotive systems, where safety is paramount.

Phase Context 🔍
----------------
Phase: **HIL**  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **automotive verification workflow**. This phase is critical as it bridges the gap between software and hardware, ensuring that both work seamlessly together in real-time scenarios. The integration of hardware-in-the-loop (HIL) testing allows for a comprehensive assessment of system behavior under various conditions.

Domain Constraints 🚧
---------------------
- Compliance baseline: **ISO 26262 (ASIL) + ISO 21434**  
- Key hazard profile: unintended acceleration/deceleration, loss of stability, braking faults  
- Interface landscape: CAN, LIN, FlexRay, Automotive Ethernet  

Domain-Specific Examples 📊
-----------------------------
- **Nominal** 🟢: Adaptive cruise and speed regulation under normal traffic conditions.  
- **Boundary** 🟡: Dense stop-and-go with tight headway and timing limits, testing the system's response under stress.  
- **Fault** 🔴: Sensor dropout and invalid CAN frame injection, simulating real-world failures to assess system robustness.

Patterns 🔄
-----------
- Derive acceptance thresholds from hazard-linked requirements to ensure all tests align with safety objectives.  
- Keep interface timing contracts explicit and reviewable for traceability and accountability.  
- Compare nominal and stressed traces against the same baseline to identify discrepancies and validate performance.

Anti-Patterns ❌
----------------
- Generic test claims without domain hazard mapping, leading to potential oversight of critical issues.  
- Pass/fail decisions without quantitative thresholds, which can obscure the true performance of the system.  
- Evidence summaries without raw artifact references, making it difficult to verify claims.

Pitfalls ⚠️
-----------
- Hidden assumptions in environment or calibration setup can lead to unexpected results.  
- Missing negative-path scenarios for high-criticality behavior can result in untested vulnerabilities.  
- Incomplete traceability from requirement to verdict undermines the integrity of the V&V process.

Best Practices 🌟
-----------------
- Tag every artifact with domain requirement IDs to enhance traceability and accountability.  
- Capture timing + functional evidence in the same run package to streamline verification efforts.  
- Record residual risk and ownership before closure to ensure all stakeholders are aware of potential issues.

Heuristics 💡
-------------
- If a domain hazard is untested, confidence is provisional; always validate against known risks.  
- If rerun differs unexpectedly, investigate determinism first to ensure consistent results.  
- If evidence is indirect, reduce verdict confidence level to reflect uncertainty.

Checklist ✅
-----------
.. note:: Use the checklist to ensure all aspects of the V&V process are covered.

- [ ] Domain hazard coverage is explicit.  
- [ ] Compliance references are mapped to evidence.  
- [ ] Nominal/boundary/fault results are all documented.  
- [ ] Residual risks and next actions are assigned.  

GIVEN / WHEN / THEN Scenarios 📜
---------------------------------
- **Nominal** 🟢:  
  - **GIVEN** the vehicle is in adaptive cruise mode,  
  - **WHEN** the traffic is flowing normally,  
  - **THEN** the vehicle maintains a safe distance and speed.

- **Boundary** 🟡:  
  - **GIVEN** the vehicle is in stop-and-go traffic,  
  - **WHEN** the headway is less than 1 meter,  
  - **THEN** the vehicle responds without unintended acceleration.

- **Fault** 🔴:  
  - **GIVEN** a sensor dropout occurs,  
  - **WHEN** an invalid CAN frame is injected,  
  - **THEN** the system enters a safe state without loss of control.

References 📚
-------------
- ISO 26262: Road vehicles – Functional safety  
- ISO 21434: Road vehicles – Cybersecurity engineering  
- ARP4754A: Guidelines for Development of Civil Aircraft and Systems  
- DO-178C: Software Considerations in Airborne Systems and Equipment Certification  

.. important:: Always ensure that the latest versions of standards are referenced and adhered to during the V&V process.

.. note:: Remember the mnemonic **CARS** (Compliance, Acceptance, Reliability, Safety) to keep the focus on essential aspects of automotive V&V.

.. warning:: Failing to adhere to these guidelines may result in critical safety oversights, leading to potential hazards in real-world applications.
