Medical Focus — Day21 HIL Concepts 🏥
=======================================

Objective 🎯
-----------
Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that our Hardware-in-the-Loop (HIL) testing meets the rigorous demands of the medical domain, safeguarding patient safety and enhancing device reliability.

Phase Context 🔍
----------------
Phase: **HIL**  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **medical verification workflow**.  

Domain Constraints 🚧
---------------------
- Compliance baseline: **IEC 62304** (Software Life Cycle Processes) + **ISO 14971** (Risk Management) + **IEC 60601** (Medical Electrical Equipment).
- Key hazard profile: incorrect dosage delivery, missed alarm, unsafe therapy continuation.
- Interface landscape: device buses, sensor links, alarm/event channels.

Domain-Specific Examples 📊
----------------------------
- **Nominal** 🟢: Therapy control with validated sensor feedback.
- **Boundary** 🟡: Near-threshold dosing and alarm escalation timing.
- **Fault** 🔴: Sensor spike/dropout and actuator command rejection path.

Patterns 🔄
-----------
- Derive acceptance thresholds from hazard-linked requirements.
- Keep interface timing contracts explicit and reviewable.
- Compare nominal and stressed traces against the same baseline.

Anti-Patterns 🚫
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
- Tag every artifact with domain requirement IDs.
- Capture timing + functional evidence in the same run package.
- Record residual risk and ownership before closure.

Heuristics 🧠
-------------
- If a domain hazard is untested, confidence is provisional.
- If rerun differs unexpectedly, investigate determinism first.
- If evidence is indirect, reduce verdict confidence level.

Checklist ✅
-----------
.. note:: Ensure that all items are checked before proceeding to the next phase.
- [ ] Domain hazard coverage is explicit.
- [ ] Compliance references are mapped to evidence.
- [ ] Nominal/boundary/fault results are all documented.
- [ ] Residual risks and next actions are assigned.

GIVEN / WHEN / THEN Scenarios 📋
-------------------------------
.. important:: Use these scenarios to guide your testing strategy.

- **Nominal Scenario** 🟢:
  - **GIVEN** a validated therapy control system,
  - **WHEN** the sensor feedback is within expected ranges,
  - **THEN** the system should deliver the correct dosage.

- **Boundary Scenario** 🟡:
  - **GIVEN** a dosing threshold near the upper limit,
  - **WHEN** the alarm escalation timing is triggered,
  - **THEN** the system should alert the operator without delay.

- **Fault Scenario** 🔴:
  - **GIVEN** a sensor dropout occurs,
  - **WHEN** an actuator command is issued,
  - **THEN** the system should safely reject the command and activate a fallback protocol.

Domain-Specific Mnemonic Acronym 🧩
------------------------------------
**HIL-MED**: **H**ardware **I**ntegration for **L**ifecycles in **M**edical **E**vidence **D**elivery. This acronym serves as a reminder of the critical components in HIL testing within the medical domain.

.. warning:: Always ensure that your testing aligns with the latest standards and best practices to maintain compliance and safety in medical applications.
