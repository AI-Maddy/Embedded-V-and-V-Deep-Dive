Medical Focus — Day20 SIL MiniProject 🚑
=========================================

Objective 🎯
-----------
Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations. The primary goal is to ensure that software systems in medical devices are rigorously validated to meet safety and performance standards.

Phase Context 📅
----------------
Phase: **SIL (Software-in-the-Loop)**  
Primary focus: **software-level correctness, robustness, and structural evidence**.  
Section focus: **medical verification workflow** to ensure that all software components function correctly and safely in a simulated environment.

Domain Constraints 🛑
--------------------
- Compliance baseline: **IEC 62304 + ISO 14971 + IEC 60601 context**  
- Key hazard profile:  
  - Incorrect dosage delivery  
  - Missed alarm  
  - Unsafe therapy continuation  
- Interface landscape:  
  - Device buses  
  - Sensor links  
  - Alarm/event channels  

Domain-Specific Examples 📊
----------------------------
- **Nominal** 🟢: Therapy control with validated sensor feedback.  
- **Boundary** 🟡: Near-threshold dosing and alarm escalation timing.  
- **Fault** 🔴: Sensor spike/dropout and actuator command rejection path.  

Patterns 🟢
----------
- Derive acceptance thresholds from hazard-linked requirements.  
- Keep interface timing contracts explicit and reviewable.  
- Compare nominal and stressed traces against the same baseline for consistency.

Anti-Patterns 🔴
----------------
- Generic test claims without domain hazard mapping.  
- Pass/fail decisions without quantitative thresholds.  
- Evidence summaries without raw artifact references.  

Pitfalls ⚠️
-----------
- Hidden assumptions in environment or calibration setup.  
- Missing negative-path scenarios for high-criticality behavior.  
- Incomplete traceability from requirement to verdict.  

Best Practices 🌟
-----------------
- Tag every artifact with domain requirement IDs for traceability.  
- Capture timing + functional evidence in the same run package to ensure comprehensive validation.  
- Record residual risk and ownership before closure to maintain accountability.

Heuristics 🧠
-------------
- If a domain hazard is untested, confidence is provisional.  
- If rerun differs unexpectedly, investigate determinism first.  
- If evidence is indirect, reduce verdict confidence level accordingly.

Checklist ✅
-----------
.. note:: Ensure all items are checked before proceeding to the next phase.

- [ ] Domain hazard coverage is explicit.  
- [ ] Compliance references are mapped to evidence.  
- [ ] Nominal/boundary/fault results are all documented.  
- [ ] Residual risks and next actions are assigned.  

GIVEN / WHEN / THEN Scenarios 📋
-------------------------------
- **Nominal** 🟢:  
  - **GIVEN** a validated sensor feedback system,  
  - **WHEN** therapy control is activated,  
  - **THEN** the system delivers the correct dosage as per the specifications.

- **Boundary** 🟡:  
  - **GIVEN** a near-threshold dosing scenario,  
  - **WHEN** an alarm escalation is triggered,  
  - **THEN** the system responds within the defined timing constraints.

- **Fault** 🔴:  
  - **GIVEN** a sensor spike/dropout,  
  - **WHEN** an actuator command is issued,  
  - **THEN** the system should reject the command and log the fault for analysis.

.. important:: Always refer to the relevant domain standards such as IEC 62304, ISO 14971, and IEC 60601 for compliance and safety requirements during the V&V process.
