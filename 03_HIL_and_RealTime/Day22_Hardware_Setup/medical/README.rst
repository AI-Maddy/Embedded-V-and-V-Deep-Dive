Medical Focus — Day22 Hardware Setup 🏥
========================================

Objective 🎯
---------
Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that all hardware interactions are thoroughly validated to maintain patient safety and device efficacy.

Phase Context 🔍
-------------
Phase: **HIL**  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **medical verification workflow**. This workflow is critical for ensuring that all components interact correctly under various scenarios, thereby safeguarding against potential failures.

Domain Constraints 🚧
------------------
- Compliance baseline: **IEC 62304 + ISO 14971 + IEC 60601 context**. These standards guide the safety and effectiveness of medical software and devices.
- Key hazard profile: 
  - Incorrect dosage delivery 🟡
  - Missed alarm 🔴
  - Unsafe therapy continuation 🔴
- Interface landscape: device buses, sensor links, alarm/event channels. Proper management of these interfaces is essential for reliable operation.

Domain-Specific Examples 📊
------------------------
- **Nominal**: therapy control with validated sensor feedback.  
  **GIVEN** a properly calibrated sensor, **WHEN** the therapy control system receives feedback, **THEN** it should deliver the correct dosage.
  
- **Boundary**: near-threshold dosing and alarm escalation timing.  
  **GIVEN** a dosing threshold, **WHEN** the dosage approaches the limit, **THEN** an alarm should trigger to alert the operator.
  
- **Fault**: sensor spike/dropout and actuator command rejection path.  
  **GIVEN** a sensor dropout, **WHEN** the actuator receives a command, **THEN** it should reject the command to prevent unsafe operation.

Patterns 🟢
--------
- Derive acceptance thresholds from hazard-linked requirements. This ensures that testing is relevant and focused on critical risks.
- Keep interface timing contracts explicit and reviewable. Clear documentation aids in traceability and accountability.
- Compare nominal and stressed traces against the same baseline to identify deviations and ensure robustness.

Anti-Patterns ⚠️
-------------
- Generic test claims without domain hazard mapping. This can lead to oversight of critical risks.
- Pass/fail decisions without quantitative thresholds. Such decisions lack rigor and can mislead stakeholders.
- Evidence summaries without raw artifact references. This undermines the validity of the claims made.

Pitfalls ⚠️
--------
- Hidden assumptions in environment or calibration setup can lead to unexpected failures during operation.
- Missing negative-path scenarios for high-criticality behavior can result in untested failure modes.
- Incomplete traceability from requirement to verdict can obscure accountability.

Best Practices 🌟
--------------
- Tag every artifact with domain requirement IDs to ensure traceability.
- Capture timing + functional evidence in the same run package for comprehensive validation.
- Record residual risk and ownership before closure to maintain accountability.

Heuristics 🔍
----------
- If a domain hazard is untested, confidence is provisional. Always ensure comprehensive testing.
- If rerun differs unexpectedly, investigate determinism first to understand variability.
- If evidence is indirect, reduce verdict confidence level to reflect uncertainty.

Pre-Review Checklist ✅
-----------------------
.. note:: Ensure all items are checked before proceeding to the review phase.
- [ ] Domain hazard coverage is explicit.
- [ ] Compliance references are mapped to evidence.
- [ ] Nominal/boundary/fault results are all documented.
- [ ] Residual risks and next actions are assigned.

.. important:: Following this checklist will help ensure that all critical aspects of the HIL setup are addressed, leading to a more robust verification process.

References 📚
-------------
- IEC 62304: Medical device software – Software life cycle processes
- ISO 14971: Medical devices – Application of risk management to medical devices
- IEC 60601: Medical electrical equipment – Part 1: General requirements for basic safety and essential performance

.. admonition:: Remember, the safety of medical devices is paramount. Always prioritize patient safety and regulatory compliance in every aspect of the verification process.
