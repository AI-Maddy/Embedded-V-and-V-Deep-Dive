Medical Focus — Day27 HIL FaultInjection 🌟
========================================

Objective 🎯
---------
Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that all hardware-in-the-loop (HIL) testing aligns with the highest standards of safety and efficacy, particularly in critical medical applications. This involves rigorous validation processes to confirm that the system operates correctly under all conditions, thereby safeguarding patient health and well-being. 

**Remember the mnemonic: HIL-MED** - **H**ardware, **I**ntegration, **L**ifecycle - **M**edical, **E**vidence, **D**ocumentation. This will help keep focus on the critical aspects of HIL testing in the medical field, ensuring that all team members are aligned with the objectives.

Phase Context 🔍
-------------
Phase: **HIL**  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **medical verification workflow**. This phase is crucial for validating that the hardware components interact seamlessly with the software, ensuring that the system behaves as intended under all conditions. HIL testing serves as a bridge between simulation and real-world application, allowing for a comprehensive assessment of system performance.

Domain Constraints 🚧
------------------
- Compliance baseline: **IEC 62304 + ISO 14971 + IEC 60601 context**. These standards provide the framework for software lifecycle processes, risk management, and medical electrical equipment safety, ensuring that all aspects of system design and testing adhere to best practices.
- Key hazard profile: 
  - **Incorrect dosage delivery** 🟡
  - **Missed alarm** 🔴
  - **Unsafe therapy continuation** 🔴
- Interface landscape: device buses, sensor links, alarm/event channels. Understanding these interfaces is vital for ensuring that the system responds correctly to various inputs and conditions, which is critical for patient safety.

Domain-Specific Examples 📊
------------------------
- **Nominal** 🟢: therapy control with validated sensor feedback. This represents the ideal operation of the system under normal conditions, ensuring that all components function as intended.
- **Boundary** 🟡: near-threshold dosing and alarm escalation timing. This tests the limits of system performance and ensures that it behaves correctly at critical thresholds, which is essential for maintaining safety margins.
- **Fault** 🔴: sensor spike/dropout and actuator command rejection path. This scenario tests the system's response to failures, ensuring that it can handle unexpected situations safely and effectively, thereby preventing potential harm to patients.

Patterns 🔄
--------
- Derive acceptance thresholds from hazard-linked requirements. This ensures that testing is aligned with the most critical safety concerns, allowing for effective risk management.
- Keep interface timing contracts explicit and reviewable. Clear contracts help in validating that all components meet their timing requirements, which is essential for reliable system performance.
- Compare nominal and stressed traces against the same baseline. This allows for a clear understanding of how the system performs under different conditions, facilitating better decision-making.

Anti-Patterns 🚫
-------------
- Generic test claims without domain hazard mapping. Always link tests to specific hazards to maintain relevance and safety, ensuring that all tests contribute to risk mitigation.
- Pass/fail decisions without quantitative thresholds. Establish clear metrics for success to avoid ambiguity and ensure that all stakeholders understand the criteria for acceptance.
- Evidence summaries without raw artifact references. Always provide traceability to support claims made in summaries, which is crucial for accountability and compliance.

Pitfalls ⚠️
--------
- Hidden assumptions in environment or calibration setup. Ensure that all assumptions are documented and validated to prevent unexpected failures during testing.
- Missing negative-path scenarios for high-criticality behavior. Testing should cover both positive and negative scenarios to ensure robustness and reliability in all situations.
- Incomplete traceability from requirement to verdict. Maintain a clear link between requirements and test outcomes to facilitate audits and reviews.

Best Practices 🌈
--------------
- Tag every artifact with domain requirement IDs. This enhances traceability and accountability, making it easier to track compliance with standards.
- Capture timing + functional evidence in the same run package. This provides a comprehensive view of system performance, allowing for better analysis and reporting.
- Record residual risk and ownership before closure. Understanding residual risks is essential for informed decision-making and ensuring that all potential issues are addressed.

Heuristics 🧠
----------
- If a domain hazard is untested, confidence is provisional. Always ensure comprehensive testing of all hazards to maintain high confidence in system safety.
- If rerun differs unexpectedly, investigate determinism first. Consistency is key in HIL testing, and any deviations should be thoroughly analyzed.
- If evidence is indirect, reduce verdict confidence level. Direct evidence is crucial for high-stakes medical applications, and reliance on indirect evidence should be minimized.

Checklist ✅
---------
.. list-table:: Pre-Review Checklist
   :widths: 20 80
   :header-rows: 1

   * - Item
     - Description
   * - Domain hazard coverage
     - Explicitly documented and mapped to testing scenarios.
   * - Compliance references
     - Mapped to evidence for clarity and accountability.
   * - Nominal/boundary/fault results
     - All results are documented and easily accessible.
   * - Residual risks
     - Clearly assigned with next actions outlined.

.. note:: 
   Ensure that all team members are familiar with the domain-specific standards and the importance of compliance in medical device testing. Continuous education and training are vital for maintaining high standards.

.. warning:: 
   Failing to address high-criticality faults can lead to severe consequences. Prioritize testing and validation of these scenarios to safeguard patient health and safety.

.. important:: 
   Always maintain a culture of safety and compliance within the team, as the implications of failure in the medical domain are significant. Encourage open communication about safety concerns.

.. admonition:: 
   Remember the mnemonic **HIL-MED**: **H**ardware, **I**ntegration, **L**ifecycle - **M**edical, **E**vidence, **D**ocumentation. This will help keep focus on the critical aspects of HIL testing in the medical field, ensuring that all team members are aligned with the objectives.

GIVEN / WHEN / THEN Scenarios 📋
------------------------------
- **Nominal 🟢**:
  - **GIVEN** the system is operating under normal conditions,
  - **WHEN** a validated sensor provides feedback,
  - **THEN** the therapy control should deliver the correct dosage as intended.

- **Boundary 🟡**:
  - **GIVEN** the system is near the threshold of dosing,
  - **WHEN** an alarm condition is triggered,
  - **THEN** the system should escalate the alarm appropriately without delay.

- **Fault 🔴**:
  - **GIVEN** a sensor experiences a spike or dropout,
  - **WHEN** the actuator receives a command,
  - **THEN** the system should reject the command and activate a safety protocol to prevent harm.
