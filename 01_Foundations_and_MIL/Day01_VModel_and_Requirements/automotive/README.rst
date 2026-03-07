Automotive Focus 🚗 — Day01 VModel and Requirements
===================================================

Objective 🎯
------------
Apply this day in **Automotive** context with explicit safety, compliance, and evidence expectations.

.. note::
   This document aligns with **ISO 26262**, **ISO 21434**, and **ASPICE** standards to ensure robust Model-in-the-Loop (MIL) verification processes.

Phase Context 🔍
----------------
Phase: **MIL**  
Primary focus: **Model behavior realism and requirement intent validation**  
Section focus: **Automotive verification workflow**  

🟢 **Nominal**: Validate model behavior under expected operating conditions.  
🟡 **Boundary**: Test edge cases and stress scenarios to ensure robustness.  
🔴 **Fault**: Simulate failure modes and assess system responses.

Domain Constraints 🚦
---------------------
- Compliance baseline: **ISO 26262 (ASIL) + ISO 21434**  
- Key hazard profile: unintended acceleration/deceleration, loss of stability, braking faults  
- Interface landscape: **CAN, LIN, FlexRay, Automotive Ethernet**  

.. important::
   Ensure all MIL tests are traceable to **ASIL** requirements and interface timing constraints.

Domain-Specific Examples 🛠️
----------------------------
**Scenario Templates**  

🟢 **Nominal**:  
GIVEN: Adaptive cruise control is active in normal traffic.  
WHEN: The vehicle maintains a steady speed and distance from the car ahead.  
THEN: The model must regulate speed and distance within specified thresholds.  

🟡 **Boundary**:  
GIVEN: Dense stop-and-go traffic with tight headway timing.  
WHEN: The vehicle accelerates and decelerates rapidly.  
THEN: The model must maintain stability and avoid collisions.  

🔴 **Fault**:  
GIVEN: Sensor dropout or invalid CAN frame injection.  
WHEN: The system detects erroneous data.  
THEN: The model must trigger fallback mechanisms and ensure safe operation.

Patterns 🧩
-----------
- Derive acceptance thresholds from hazard-linked requirements.  
- Keep interface timing contracts explicit and reviewable.  
- Compare nominal and stressed traces against the same baseline.  

.. admonition:: **Best Practice Reminder**  
   Always validate timing constraints against **ISO 26262** and **ASPICE** guidelines.

Anti-Patterns 🚫
----------------
- Generic test claims without domain hazard mapping.  
- Pass/fail decisions without quantitative thresholds.  
- Evidence summaries without raw artifact references.  

.. warning::
   Avoid vague test results that lack direct traceability to safety-critical requirements.

Pitfalls ⚠️
------------
- Hidden assumptions in environment or calibration setup.  
- Missing negative-path scenarios for high-criticality behavior.  
- Incomplete traceability from requirement to verdict.  

.. admonition:: **Critical Reminder**  
   Negative-path scenarios are mandatory for **ASIL D** compliance.

Best Practices 🌟
-----------------
- Tag every artifact with domain requirement IDs.  
- Capture timing + functional evidence in the same run package.  
- Record residual risk and ownership before closure.  

.. note::
   Use **ISO 26262** hazard analysis to prioritize testing scenarios and residual risk documentation.

Heuristics 🧠
-------------
- If a domain hazard is untested, confidence is provisional.  
- If rerun differs unexpectedly, investigate determinism first.  
- If evidence is indirect, reduce verdict confidence level.  

.. important::
   Always investigate unexpected test rerun results to ensure model determinism.

Checklist ✅
-----------
☐ Domain hazard coverage is explicit.  
☐ Compliance references are mapped to evidence.  
☐ Nominal/boundary/fault results are all documented.  
☐ Residual risks and next actions are assigned.  

.. admonition:: **Pre-Review Checklist**  
   Verify all artifacts are tagged with requirement IDs and mapped to compliance standards.

Domain Standards References 📚
------------------------------
- **ISO 26262**: Functional safety for automotive systems.  
- **ISO 21434**: Cybersecurity for automotive systems.  
- **ASPICE**: Automotive SPICE process assessment model.  

.. note::
   Refer to **ARP4754A** for system-level integration and verification workflows.  

Tabular Summary 📊
------------------
.. list-table:: Automotive MIL Verification Highlights  
   :header-rows: 1  

   * - **Aspect**  
     - **Nominal**  
     - **Boundary**  
     - **Fault**  
   * - **Scenario**  
     - Adaptive cruise control in normal traffic.  
     - Dense stop-and-go traffic with tight timing.  
     - Sensor dropout or invalid CAN frame injection.  
   * - **Focus**  
     - Speed and distance regulation.  
     - Stability and collision avoidance.  
     - Safe fallback mechanisms.  
   * - **Compliance**  
     - ISO 26262 ASIL B-D.  
     - ISO 26262 ASIL C-D.  
     - ISO 26262 ASIL D.  

.. admonition:: **Acronym Mnemonic: DRIVE**  
   - **D**: Determinism in model behavior.  
   - **R**: Residual risk documentation.  
   - **I**: Interface timing validation.  
   - **V**: Verification against hazards.  
   - **E**: Evidence traceability to requirements.
