🏥 Medical Focus — Day28 Compliance Mapping 🩺
=============================================

🎯 **Objective** 🎯
---------
Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that all hardware-in-the-loop (HIL) systems meet the stringent requirements of medical safety and efficacy. This is crucial for patient outcomes and regulatory adherence.

🔧 **Phase Context** 🔧
-------------
Phase: **HIL**  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **medical verification workflow**.  

📜 **Domain Constraints** 📜
------------------
- Compliance baseline: **IEC 62304 + ISO 14971 + IEC 60601 context**.
- Key hazard profile: 
  - Incorrect dosage delivery 🟡
  - Missed alarm 🔴
  - Unsafe therapy continuation 🔴
- Interface landscape: device buses, sensor links, alarm/event channels.

🧪 **Domain-Specific Examples** 🧪
------------------------
- **Nominal** 🟢: Therapy control with validated sensor feedback.
- **Boundary** 🟡: Near-threshold dosing and alarm escalation timing.
- **Fault** 🔴: Sensor spike/dropout and actuator command rejection path.

🔍 **Patterns** 🔍
--------
- Derive acceptance thresholds from hazard-linked requirements.
- Keep interface timing contracts explicit and reviewable.
- Compare nominal and stressed traces against the same baseline.

🚫 **Anti-Patterns** 🚫
-------------
- Generic test claims without domain hazard mapping.
- Pass/fail decisions without quantitative thresholds.
- Evidence summaries without raw artifact references.

⚠️ **Pitfalls** ⚠️
--------
- Hidden assumptions in environment or calibration setup.
- Missing negative-path scenarios for high-criticality behavior.
- Incomplete traceability from requirement to verdict.

🌟 **Best Practices** 🌟
--------------
- Tag every artifact with domain requirement IDs.
- Capture timing + functional evidence in the same run package.
- Record residual risk and ownership before closure.

🧠 **Heuristics** 🧠
----------
- If a domain hazard is untested, confidence is provisional.
- If rerun differs unexpectedly, investigate determinism first.
- If evidence is indirect, reduce verdict confidence level.

✅ **Checklist** ✅
---------
.. list-table:: Pre-Review Checklist
   :widths: 1 1
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

📊 **GIVEN / WHEN / THEN Scenarios** 📊
-------------------------------
**Nominal Scenario** 🟢  
GIVEN a validated sensor feedback system,  
WHEN therapy control is activated,  
THEN the system delivers the correct dosage without alarms.

**Boundary Scenario** 🟡  
GIVEN a near-threshold dosing condition,  
WHEN the alarm escalation timing is triggered,  
THEN the system must alert the operator within the defined time frame.

**Fault Scenario** 🔴  
GIVEN a sensor spike/dropout event,  
WHEN the actuator command is issued,  
THEN the system must reject the command and trigger a fault alarm.

.. note:: Ensure that all scenarios are tested and documented to maintain compliance with IEC 62304 and ISO 14971.

.. important:: Always prioritize safety-critical paths in testing to mitigate risks associated with high-hazard profiles.

.. warning:: Failure to adhere to these guidelines may result in non-compliance and jeopardize patient safety.

**HIL-MED** Mnemonic Acronym
----------------------------
H - Hazard Identification  
I - Interface Confidence  
L - Lifecycle Evidence  
M - Medical Context  
E - Explicit Requirements  
D - Documented Results

.. admonition:: Remember the HIL-MED approach for effective compliance mapping in medical systems!

🔴 **Severity / Priority Colour Legend** 🔴
-----------------------------------------
- 🟢: Nominal scenario (no fault or boundary conditions)
- 🟡: Boundary scenario (near-threshold conditions)
- 🔴: Fault scenario (error or failure conditions)

.. warning:: Use the colour legend to categorize and prioritize test scenarios based on their severity and potential impact on patient safety.

📚 **References** 📚
-------------------
- IEC 62304:2006 - Medical device software — Software life cycle processes
- ISO 14971:2019 - Medical devices — Application of risk management to medical devices
- IEC 60601:2005 - Medical electrical equipment — Part 1: General requirements for safety and essential performance
