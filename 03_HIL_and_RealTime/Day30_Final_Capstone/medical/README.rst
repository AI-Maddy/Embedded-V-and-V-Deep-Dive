Medical Focus — Day30 Final Capstone
====================================

🟢 **Medical Mnemonic:** "M.A.D.E." - **M**edical **A**pplications **D**epend on **E**ffective **V**erification

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

### Pattern 2: Keep Interface Timing Contracts Explicit 🟡
* **Description:** Keep interface timing contracts explicit and reviewable.
* **Benefits:** Ensures deterministic behavior.

### Pattern 3: Compare Nominal and Stressed Traces 🟢
* **Description:** Compare nominal and stressed traces against the same baseline.
* **Benefits:** Ensures consistent behavior.

Anti-Patterns
-------------
### Anti-Pattern 1: Generic Test Claims Without Domain Hazard Mapping 🔴
* **Description:** Generic test claims without domain hazard mapping.
* **Risks:** Incomplete or inaccurate testing.

### Anti-Pattern 2: Pass/Fail Decisions Without Quantitative Thresholds 🔴
* **Description:** Pass/fail decisions without quantitative thresholds.
* **Risks:** Inconsistent or inaccurate testing.

### Anti-Pattern 3: Evidence Summaries Without Raw Artifact References 🔴
* **Description:** Evidence summaries without raw artifact references.
* **Risks:** Incomplete or inaccurate documentation.

Pitfalls
--------
### Pitfall 1: Hidden Assumptions in Environment or Calibration Setup 🔴
* **Description:** Hidden assumptions in environment or calibration setup.
* **Risks:** Incomplete or inaccurate testing.

### Pitfall 2: Missing Negative-Path Scenarios for High-Criticality Behavior 🔴
* **Description:** Missing negative-path scenarios for high-criticality behavior.
* **Risks:** Incomplete or inaccurate testing.

### Pitfall 3: Incomplete Traceability from Requirement to Verdict 🔴
* **Description:** Incomplete traceability from requirement to verdict.
* **Risks:** Incomplete or inaccurate documentation.

Best Practices
--------------
### Best Practice 1: Tag Every Artifact with Domain Requirement IDs 🟢
* **Description:** Tag every artifact with domain requirement IDs.
* **Benefits:** Ensures traceability.

### Best Practice 2: Capture Timing + Functional Evidence in the Same Run Package 🟢
* **Description:** Capture timing + functional evidence in the same run package.
* **Benefits:** Ensures consistency.

### Best Practice 3: Record Residual Risk and Ownership Before Closure 🟢
* **Description:** Record residual risk and ownership before closure.
* **Benefits:** Ensures accountability.

Heuristics
----------
### Heuristic 1: If a Domain Hazard is Untested, Confidence is Provisional 🟢
* **Description:** If a domain hazard is untested, confidence is provisional.
* **Benefits:** Ensures caution.

### Heuristic 2: If Rerun Differs Unexpectedly, Investigate Determinism First 🟢
* **Description:** If rerun differs unexpectedly, investigate determinism first.
* **Benefits:** Ensures consistency.

### Heuristic 3: If Evidence is Indirect, Reduce Verdict Confidence Level 🟢
* **Description:** If evidence is indirect, reduce verdict confidence level.
* **Benefits:** Ensures caution.

Checklist
---------
☐ **Domain Hazard Coverage is Explicit**
☐ **Compliance References are Mapped to Evidence**
☐ **Nominal/Boundary/Fault Results are All Documented**
☐ **Residual Risks and Next Actions are Assigned**

.. note::
   This checklist is not exhaustive and should be adapted to the specific project needs.

.. warning::
   Failure to follow these guidelines may result in incomplete or inaccurate verification.

.. important::
   These guidelines are based on IEC 62304, ISO 14971, and IEC 60601 standards.

.. admonition::
   These guidelines are subject to change and should be reviewed regularly.

Table of Domain Standards References
=====================================

+-----------------------+---------------+---------------+
| Standard             | Description   | Version       |
+=======================+===============+===============+
| IEC 62304           | Medical Device| 3rd Edition   |
|                      | Software    |               |
+-----------------------+---------------+---------------+
| ISO 14971          | Medical Device| 2nd Edition   |
|                      | Risk Management|               |
+-----------------------+---------------+---------------+
| IEC 60601          | Medical Electrical| 3rd Edition  |
|                      | Equipment    |               |
+-----------------------+---------------+---------------+
