🏥 Medical Focus — Day30 Final Capstone 🏥
============================================

🟢 **Medical Mnemonic:** "M.A.D.E. S.A.F.E." - **M**edical **A**pplications **D**epend on **E**ffective **S**afety **A**ssurance, **F**ailure **E**valuation

Objective
---------
🟢 **Primary Goal:** Ensure **Medical** applications meet safety, compliance, and evidence expectations.

Phase Context
-------------
🟢 **Phase:** **HIL** (Hardware-in-the-Loop)
🟡 **Primary Focus:** **Hardware-Integrated Timing and Interface Confidence**
🔴 **Section Focus:** **Medical Verification Workflow**

Domain Constraints
------------------
🟢 **Compliance Baseline:** IEC 62304 + ISO 14971 + IEC 60601 context
🟡 **Key Hazard Profile:** Incorrect dosage delivery, missed alarm, unsafe therapy continuation
🔴 **Interface Landscape:** Device buses, sensor links, alarm/event channels

.. note::
   Compliance with IEC 62304, ISO 14971, and IEC 60601 standards is mandatory for medical device software.

Domain-Specific Examples
------------------------
### Nominal Scenario 🟢
* **GIVEN:** Therapy control system with validated sensor feedback.
* **WHEN:** Normal operation with validated sensor inputs.
* **THEN:** Therapy delivery is accurate and alarms are triggered correctly.

### Boundary Scenario 🟡
* **GIVEN:** Therapy control system near threshold dosing and alarm escalation timing.
* **WHEN:** Sensor inputs are near threshold values.
* **THEN:** Alarms are triggered correctly and therapy delivery is within acceptable limits.

### Fault Scenario 🔴
* **GIVEN:** Therapy control system with sensor spike/dropout and actuator command rejection path.
* **WHEN:** Sensor inputs are faulty or missing.
* **THEN:** Alarms are triggered correctly and therapy delivery is rejected.

Patterns
--------
### Pattern 1: Derive Acceptance Thresholds 🟢
* **Description:** Derive acceptance thresholds from hazard-linked requirements.
* **Benefits:** Ensures safety and compliance.
* **Standards References:** IEC 62304, ISO 14971

### Pattern 2: Keep Interface Timing Contracts Explicit 🟡
* **Description:** Keep interface timing contracts explicit and reviewable.
* **Benefits:** Ensures deterministic behavior.
* **Standards References:** IEC 60601

### Pattern 3: Compare Nominal and Stressed Traces 🟢
* **Description:** Compare nominal and stressed traces against the same baseline.
* **Benefits:** Ensures consistent behavior.
* **Standards References:** IEC 62304

Anti-Patterns
-------------
### Anti-Pattern 1: Generic Test Claims Without Domain Hazard Mapping 🔴
* **Description:** Generic test claims without domain hazard mapping.
* **Risks:** Incomplete or inaccurate testing.
* **Standards References:** ISO 14971

### Anti-Pattern 2: Pass/Fail Decisions Without Quantitative Thresholds 🔴
* **Description:** Pass/fail decisions without quantitative thresholds.
* **Risks:** Inconsistent or inaccurate testing.
* **Standards References:** IEC 62304

### Anti-Pattern 3: Evidence Summaries Without Raw Artifact References 🔴
* **Description:** Evidence summaries without raw artifact references.
* **Risks:** Incomplete or inaccurate documentation.
* **Standards References:** IEC 60601

Pitfalls
--------
### Pitfall 1: Hidden Assumptions in Environment or Calibration Setup 🔴
* **Description:** Hidden assumptions in environment or calibration setup.
* **Risks:** Incomplete or inaccurate testing.
* **Standards References:** ISO 14971

### Pitfall 2: Missing Negative-Path Scenarios for High-Criticality Behavior 🔴
* **Description:** Missing negative-path scenarios for high-criticality behavior.
* **Risks:** Incomplete or inaccurate testing.
* **Standards References:** IEC 62304

### Pitfall 3: Incomplete Traceability from Requirement to Verdict 🔴
* **Description:** Incomplete traceability from requirement to verdict.
* **Risks:** Incomplete or inaccurate documentation.
* **Standards References:** IEC 60601

Best Practices
--------------
### Best Practice 1: Tag Every Artifact with Domain Requirement IDs 🟢
* **Description:** Tag every artifact with domain requirement IDs.
* **Benefits:** Ensures traceability.
* **Standards References:** IEC 62304

### Best Practice 2: Capture Timing + Functional Evidence in the Same Run Package 🟢
* **Description:** Capture timing + functional evidence in the same run package.
* **Benefits:** Ensures consistency.
* **Standards References:** IEC 60601

### Best Practice 3: Record Residual Risk and Ownership Before Closure 🟢
* **Description:** Record residual risk and ownership before closure.
* **Benefits:** Ensures accountability.
* **Standards References:** ISO 14971

Heuristics
----------
### Heuristic 1: If a Domain Hazard is Untested, Confidence is Provisional 🟢
* **Description:** If a domain hazard is untested, confidence is provisional.
* **Benefits:** Ensures caution.
* **Standards References:** IEC 62304

### Heuristic 2: If Rerun Differs Unexpectedly, Investigate Determinism First 🟢
* **Description:** If rerun differs unexpectedly, investigate determinism first.
* **Benefits:** Ensures consistency.
* **Standards References:** IEC 60601

### Heuristic 3: If Evidence is Indirect, Reduce Verdict Confidence Level 🟢
* **Description:** If evidence is indirect, reduce verdict confidence level.
* **Benefits:** Ensures caution.
* **Standards References:** ISO 14971

Checklist
---------
☐ **Domain Hazard Coverage is Explicit**
☐ **Compliance References are Mapped to Evidence**
☐ **Nominal/Boundary/Fault Results are All Documented**
☐ **Residual Risks and Next Actions are Assigned**
☐ **All Artifacts are Tagged with Domain Requirement IDs**
☐ **Timing + Functional Evidence is Captured in the Same Run Package**

.. warning::
   Failure to follow these guidelines may result in incomplete or inaccurate verification.

.. important::
   These guidelines are based on IEC 62304, ISO 14971, and IEC 60601 standards.

.. admonition::
   These guidelines are subject to change and should be reviewed regularly.

Table of Domain Standards References
=====================================

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Standard
     - Description
     - Version
   * - IEC 62304
     - Medical Device Software
     - 3rd Edition
   * - ISO 14971
     - Medical Device Risk Management
     - 2nd Edition
   * - IEC 60601
     - Medical Electrical Equipment
     - 3rd Edition

Severity / Priority Colour Legend
---------------------------------

* 🟢: Low Severity / Low Priority
* 🟡: Medium Severity / Medium Priority
* 🔴: High Severity / High Priority
