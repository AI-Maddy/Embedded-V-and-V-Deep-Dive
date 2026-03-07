Automotive Focus — Day30 Final Capstone 🚗💻
==============================================

Objective
---------
🟢 **Apply Automotive Safety & Compliance** with explicit safety, compliance, and evidence expectations.

Phase Context
-------------
🟡 **HIL (Hardware-in-the-Loop) Phase**:
Primary focus: **hardware-integrated timing and interface confidence**.
Section focus: **results consolidation and release-readiness evidence**.

Domain Constraints
------------------
☐ Compliance baseline: **ISO 26262 (ASIL) + ISO 21434** 📚
☐ Key hazard profile: unintended acceleration/deceleration, loss of stability, braking faults 🚨
☐ Interface landscape: CAN, LIN, FlexRay, Automotive Ethernet 📈

Domain-Specific Mnemonic: **C.A.R.E.** 🚗
- **C**: Compliance (ISO 26262, ISO 21434)
- **A**: Automotive (CAN, LIN, FlexRay, Automotive Ethernet)
- **R**: Requirements (hazard-linked, explicit, and reviewable)
- **E**: Evidence (nominal, boundary, fault, and residual risk)

Domain-Specific Examples
------------------------
### Nominal 🟢
Adaptive cruise and speed regulation under normal traffic.

### Boundary 🟡
Dense stop-and-go with tight headway and timing limits.

### Fault 🔴
Sensor dropout and invalid CAN frame injection.

Patterns
--------
### Derive Acceptance Thresholds 📈
Derive acceptance thresholds from hazard-linked requirements.

### Keep Interface Timing Contracts Explicit 📝
Keep interface timing contracts explicit and reviewable.

### Compare Nominal and Stressed Traces 📊
Compare nominal and stressed traces against the same baseline.

Anti-Patterns
-------------
### Generic Test Claims Without Domain Hazard Mapping 🚫
Generic test claims without domain hazard mapping.

### Pass/Fail Decisions Without Quantitative Thresholds 🤔
Pass/fail decisions without quantitative thresholds.

### Evidence Summaries Without Raw Artifact References 📝
Evidence summaries without raw artifact references.

Pitfalls
--------
### Hidden Assumptions in Environment or Calibration Setup 🤔
Hidden assumptions in environment or calibration setup.

### Missing Negative-Path Scenarios for High-Criticality Behavior 🚨
Missing negative-path scenarios for high-criticality behavior.

### Incomplete Traceability from Requirement to Verdict 📝
Incomplete traceability from requirement to verdict.

Best Practices
--------------
### Tag Every Artifact with Domain Requirement IDs 📝
Tag every artifact with domain requirement IDs.

### Capture Timing + Functional Evidence in the Same Run Package 📊
Capture timing + functional evidence in the same run package.

### Record Residual Risk and Ownership Before Closure 📝
Record residual risk and ownership before closure.

Heuristics
----------
### If a Domain Hazard is Untested, Confidence is Provisional 🤔
If a domain hazard is untested, confidence is provisional.

### If Rerun Differs Unexpectedly, Investigate Determinism First 🔍
If rerun differs unexpectedly, investigate determinism first.

### If Evidence is Indirect, Reduce Verdict Confidence Level 📊
If evidence is indirect, reduce verdict confidence level.

Checklist
---------
☐ Domain hazard coverage is explicit.
☐ Compliance references are mapped to evidence.
☐ Nominal/boundary/fault results are all documented.
☐ Residual risks and next actions are assigned.

GIVEN / WHEN / THEN Scenario Templates
=====================================

### Nominal 🟢
.. given:: Normal traffic conditions.
.. when:: Adaptive cruise and speed regulation are enabled.
.. then:: The vehicle maintains a safe distance and speed.

### Boundary 🟡
.. given:: Dense stop-and-go traffic conditions.
.. when:: Tight headway and timing limits are applied.
.. then:: The vehicle maintains a safe distance and speed under stress.

### Fault 🔴
.. given:: Sensor dropout and invalid CAN frame injection.
.. when:: The vehicle's adaptive cruise and speed regulation are enabled.
.. then:: The vehicle's safety features are triggered to prevent accidents.

Admonitions
------------

.. note:: Always follow the C.A.R.E. mnemonic to ensure compliance and safety.
.. warning:: Hidden assumptions in environment or calibration setup can lead to incorrect results.
.. important:: Evidence summaries without raw artifact references can lead to incomplete understanding.
.. admonition:: Always investigate determinism first if rerun differs unexpectedly.

Standards References
--------------------

- ISO 26262 (ASIL)
- ISO 21434
- ARP4754A/4761
- ASPICE
- IEC 62304

List Table
----------

+-----------------------+---------------+---------------+---------------+
| Domain Hazard        | Compliance    | Evidence      | Verdict        |
+=======================+===============+===============+===============+
| Unintended acceleration| ISO 26262    | Nominal,      | Safe distance  |
|                       |               | Boundary,     | and speed     |
|                       |               | Fault         | maintained     |
+-----------------------+---------------+---------------+---------------+
| Loss of stability     | ISO 21434    | Nominal,      | Vehicle        |
|                       |               | Boundary,     | stability      |
|                       |               | Fault         | maintained     |
+-----------------------+---------------+---------------+---------------+
