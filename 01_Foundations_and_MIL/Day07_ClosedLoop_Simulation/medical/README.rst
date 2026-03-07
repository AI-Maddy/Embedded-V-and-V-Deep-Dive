Medical Focus — Day07 ClosedLoop Simulation 🚑
=============================================

Objective 🎯
------------
Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations.

.. note::
   This document aligns with **IEC 62304**, **ISO 14971**, and **IEC 60601** standards for medical device software lifecycle and risk management.

Phase Context 🌀
----------------
Phase: **MIL** (Model-in-the-Loop)  
Primary focus: **Model behavior realism and requirement intent validation**  
Section focus: **Medical verification workflow**  

.. admonition:: MIL Mnemonic: "SAFE"
   :class: tip

   - **S**: Simulate realistic medical scenarios  
   - **A**: Analyze boundary conditions  
   - **F**: Fault injection for robustness  
   - **E**: Evidence collection for compliance  

Domain Constraints ⚙️
---------------------
- **Compliance baseline**:  
  - IEC 62304: Software lifecycle processes  
  - ISO 14971: Risk management for medical devices  
  - IEC 60601: Electrical safety and performance  

- **Key hazard profile**:  
  - Incorrect dosage delivery 🟡  
  - Missed alarm 🟡  
  - Unsafe therapy continuation 🔴  

- **Interface landscape**:  
  - Device buses 🟢  
  - Sensor links 🟡  
  - Alarm/event channels 🔴  

Domain-Specific Examples 🩺
---------------------------
**Nominal Scenario 🟢**  
GIVEN: Therapy control system with validated sensor feedback  
WHEN: Sensor provides expected readings within calibrated range  
THEN: Therapy proceeds as intended, maintaining patient safety  

**Boundary Scenario 🟡**  
GIVEN: Near-threshold dosing and alarm escalation timing  
WHEN: Sensor readings approach critical thresholds  
THEN: Alarm escalates appropriately, ensuring timely intervention  

**Fault Scenario 🔴**  
GIVEN: Sensor spike/dropout or actuator command rejection  
WHEN: System encounters unexpected input or fails to execute commands  
THEN: Therapy halts safely, and error is logged for investigation  

Patterns 🧩
-----------
- Derive acceptance thresholds from hazard-linked requirements  
- Keep interface timing contracts explicit and reviewable  
- Compare nominal and stressed traces against the same baseline  

Anti-Patterns 🚫
----------------
- Generic test claims without domain hazard mapping  
- Pass/fail decisions without quantitative thresholds  
- Evidence summaries without raw artifact references  

Pitfalls ⚡
-----------
- Hidden assumptions in environment or calibration setup  
- Missing negative-path scenarios for high-criticality behavior  
- Incomplete traceability from requirement to verdict  

Best Practices 🌟
-----------------
- Tag every artifact with domain requirement IDs  
- Capture timing + functional evidence in the same run package  
- Record residual risk and ownership before closure  

Heuristics 🧠
-------------
- If a domain hazard is untested, confidence is provisional  
- If rerun differs unexpectedly, investigate determinism first  
- If evidence is indirect, reduce verdict confidence level  

Pre-Review Checklist ✅
-----------------------
☐ Domain hazard coverage is explicit  
☐ Compliance references are mapped to evidence  
☐ Nominal/boundary/fault results are all documented  
☐ Residual risks and next actions are assigned  

Severity / Priority Legend 🎨
-----------------------------
.. list-table::  
   :header-rows: 1  

   * - Severity Level  
     - Description  
   * - 🟢 Nominal  
     - Expected behavior under normal conditions  
   * - 🟡 Boundary  
     - Edge-case behavior near critical thresholds  
   * - 🔴 Fault  
     - Unexpected or unsafe behavior requiring mitigation  

References 📚
------------
- **IEC 62304**: Medical device software lifecycle processes  
- **ISO 14971**: Risk management for medical devices  
- **IEC 60601**: Electrical safety and performance standards  

.. important::
   Ensure all scenarios are mapped to compliance standards and domain-specific hazards.
