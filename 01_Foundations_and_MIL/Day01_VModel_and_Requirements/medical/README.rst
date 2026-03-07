Medical Focus 🌡️ — Day01 VModel and Requirements
===============================================

Objective 🎯
------------
🌟 **Mission:** Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations.

🧠 **Mnemonic:** **SAFE-MED**  
**S**afety-focused  
**A**ccuracy in modeling  
**F**ault tolerance  
**E**vidence-based validation  
**M**easurement of risks  
**E**xecution traceability  
**D**omain compliance  

Phase Context 🔬
----------------
**Phase:** 🟢 **MIL** (Model-in-the-Loop)  
**Primary focus:** **Model behavior realism and requirement intent validation**  
**Section focus:** **Medical verification workflow**  

.. note::  
   MIL is a critical phase in embedded systems V&V, especially in the medical domain, where patient safety is paramount. Standards such as **IEC 62304**, **ISO 14971**, and **IEC 60601** provide essential guidance.

Domain Constraints 🩺
---------------------
- **Compliance baseline:**  
  - 🟢 **IEC 62304**: Software lifecycle processes  
  - 🟢 **ISO 14971**: Risk management for medical devices  
  - 🟢 **IEC 60601**: Electrical safety and essential performance  

- **Key hazard profile:**  
  - 🟡 Incorrect dosage delivery  
  - 🟡 Missed alarm  
  - 🔴 Unsafe therapy continuation  

- **Interface landscape:**  
  - 🟢 Device buses  
  - 🟢 Sensor links  
  - 🟡 Alarm/event channels  

Domain-Specific Examples 📊
---------------------------
**Nominal 🟢**  
GIVEN: A therapy control system with validated sensor feedback  
WHEN: The system operates within expected ranges  
THEN: Therapy is delivered as intended without deviation  

**Boundary 🟡**  
GIVEN: Near-threshold dosing and alarm escalation timing  
WHEN: The system approaches critical thresholds  
THEN: Alarms escalate appropriately, and therapy remains safe  

**Fault 🔴**  
GIVEN: Sensor spike/dropout and actuator command rejection path  
WHEN: A fault occurs in the sensor or actuator  
THEN: The system enters a safe state, halting therapy and issuing alerts  

Patterns 🧩
-----------
- Derive acceptance thresholds from hazard-linked requirements  
- Keep interface timing contracts explicit and reviewable  
- Compare nominal and stressed traces against the same baseline  

.. admonition:: **Important**  
   Patterns ensure consistency and traceability across the V&V lifecycle. They are essential for compliance with **IEC 62304** and **ISO 14971**.

Anti-Patterns 🚫
----------------
- Generic test claims without domain hazard mapping  
- Pass/fail decisions without quantitative thresholds  
- Evidence summaries without raw artifact references  

.. warning::  
   Avoid anti-patterns as they compromise compliance and patient safety. **ISO 14971** emphasizes the importance of hazard mapping and risk quantification.

Pitfalls ⚠️
------------
- Hidden assumptions in environment or calibration setup  
- Missing negative-path scenarios for high-criticality behavior  
- Incomplete traceability from requirement to verdict  

.. important::  
   Addressing pitfalls early prevents costly rework and ensures adherence to **IEC 62304** and **ISO 14971** standards.

Best Practices 🏆
-----------------
- Tag every artifact with domain requirement IDs  
- Capture timing + functional evidence in the same run package  
- Record residual risk and ownership before closure  

.. note::  
   Best practices align with **ASPICE** guidelines for traceability and evidence management.

Heuristics 🧠
-------------
- If a domain hazard is untested, confidence is provisional  
- If rerun differs unexpectedly, investigate determinism first  
- If evidence is indirect, reduce verdict confidence level  

Checklist ✅
-----------
☐ Domain hazard coverage is explicit  
☐ Compliance references are mapped to evidence  
☐ Nominal/boundary/fault results are all documented  
☐ Residual risks and next actions are assigned  

Severity Legend 🟢🟡🔴
---------------------
.. list-table:: **Severity Legend**  
   :header-rows: 1  

   * - **Severity**  
     - **Description**  
   * - 🟢 Nominal  
     - Expected system behavior under normal conditions  
   * - 🟡 Boundary  
     - Edge-case behavior near critical thresholds  
   * - 🔴 Fault  
     - System behavior under failure conditions  

References 📚
------------
- **IEC 62304**: Medical device software lifecycle processes  
- **ISO 14971**: Application of risk management to medical devices  
- **IEC 60601**: Medical electrical equipment safety and performance  
- **ASPICE**: Automotive SPICE process assessment model  

.. admonition:: **Remember SAFE-MED!**  
   Always prioritize **Safety**, **Accuracy**, **Fault tolerance**, **Evidence**, **Measurement**, **Execution traceability**, and **Domain compliance**.
