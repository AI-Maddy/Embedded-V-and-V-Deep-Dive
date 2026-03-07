Medical Focus 🌡️ — Day02 Traceability and TestDesign
====================================================

Objective 🎯
------------
🌟 **M.E.D.I.C.A.L.** Mnemonic 🌟  
Mastering Embedded Design Integrity for Compliance and Assurance in Lifecycle  

- **M**: Model behavior realism  
- **E**: Evidence-based validation  
- **D**: Domain-specific hazard mapping  
- **I**: Interface timing contracts  
- **C**: Compliance to IEC 62304, ISO 14971, IEC 60601  
- **A**: Artifact traceability  
- **L**: Lifecycle risk management  

The goal of this session is to apply **Medical** context principles with explicit focus on safety, compliance, and evidence expectations.

Phase Context 🧩
----------------
Phase: **MIL** (Model-in-the-Loop)  
Primary focus: **model behavior realism and requirement intent validation**  
Section focus: **medical verification workflow**  

.. note::  
   MIL is a critical phase in medical device development where model fidelity and requirement traceability are validated. This ensures early detection of design flaws and compliance gaps.

Domain Constraints ⚙️
---------------------
- **Compliance baseline**:  
  - IEC 62304: Software lifecycle processes  
  - ISO 14971: Risk management for medical devices  
  - IEC 60601: Electrical safety and essential performance  

- **Key hazard profile**:  
  - Incorrect dosage delivery 🟡  
  - Missed alarm 🔴  
  - Unsafe therapy continuation 🟢  

- **Interface landscape**:  
  - Device buses  
  - Sensor links  
  - Alarm/event channels  

.. important::  
   Hazards must be mapped explicitly to requirements and test cases to ensure traceability and risk mitigation.

Domain-Specific Examples 📋
---------------------------
- **Nominal 🟢**: Therapy control with validated sensor feedback.  
  **GIVEN**: A calibrated sensor and nominal therapy settings.  
  **WHEN**: The therapy control loop is executed.  
  **THEN**: Sensor feedback matches expected thresholds, and therapy is delivered correctly.  

- **Boundary 🟡**: Near-threshold dosing and alarm escalation timing.  
  **GIVEN**: A therapy setting near the upper dosage limit.  
  **WHEN**: The system detects a threshold breach.  
  **THEN**: Alarm escalation occurs within the prescribed timing window.  

- **Fault 🔴**: Sensor spike/dropout and actuator command rejection path.  
  **GIVEN**: A sensor experiences a transient spike/dropout.  
  **WHEN**: The actuator receives an invalid command.  
  **THEN**: The system rejects the command and triggers a fault response.

Patterns 🧵
-----------
- Derive acceptance thresholds from hazard-linked requirements.  
- Keep interface timing contracts explicit and reviewable.  
- Compare nominal and stressed traces against the same baseline.  

.. admonition:: Standards Reference  
   IEC 62304 requires that software safety classifications are tied to risk levels, ensuring that acceptance thresholds align with hazard severity.

Anti-Patterns 🚫
----------------
- Generic test claims without domain hazard mapping.  
- Pass/fail decisions without quantitative thresholds.  
- Evidence summaries without raw artifact references.  

.. warning::  
   Avoid using generic claims or vague thresholds, as they undermine compliance and safety assurance.

Pitfalls ⚠️
-----------
- Hidden assumptions in environment or calibration setup.  
- Missing negative-path scenarios for high-criticality behavior.  
- Incomplete traceability from requirement to verdict.  

.. important::  
   Ensure that every assumption is documented and validated to avoid hidden risks during certification audits.

Best Practices 🌟
-----------------
- Tag every artifact with domain requirement IDs.  
- Capture timing + functional evidence in the same run package.  
- Record residual risk and ownership before closure.  

.. note::  
   Residual risks must be explicitly documented and assigned to owners for follow-up actions.

Heuristics 🧠
------------
- If a domain hazard is untested, confidence is provisional.  
- If rerun differs unexpectedly, investigate determinism first.  
- If evidence is indirect, reduce verdict confidence level.  

Checklist ✅
-----------
☐ Domain hazard coverage is explicit.  
☐ Compliance references are mapped to evidence.  
☐ Nominal/boundary/fault results are all documented.  
☐ Residual risks and next actions are assigned.  
☐ Interface timing contracts are validated.  
☐ Acceptance thresholds are derived from requirements.  
☐ Evidence includes raw artifacts and summaries.  

.. admonition:: Pre-Review Reminder  
   Before proceeding, ensure all checklist items are addressed and traceability is complete.

List of Severity Levels 🟢🟡🔴
============================
.. list-table:: Severity Levels and Descriptions  
   :widths: 20 80  
   :header-rows: 1  

   * - **Severity Level**  
     - **Description**  
   * - 🟢 Nominal  
     - Expected behavior under normal operating conditions.  
   * - 🟡 Boundary  
     - Behavior near thresholds or limits, requiring close monitoring.  
   * - 🔴 Fault  
     - Erroneous or unsafe behavior requiring immediate intervention.  

.. admonition:: Compliance Note  
   Ensure that severity levels align with ISO 14971 risk management classifications for medical devices.
