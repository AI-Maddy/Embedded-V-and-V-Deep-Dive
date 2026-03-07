Medical Focus — Day30 Final Capstone 🟢
=====================================

Objective
---------
Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations. 💊

Phase Context
-------------
Phase: **HIL** 🤖
Primary focus: **hardware-integrated timing and interface confidence**.
Section focus: **results consolidation and release-readiness evidence**.

Domain Constraints
------------------
- Compliance baseline: **IEC 62304 + ISO 14971 + IEC 60601 context** 📚
  .. note::
    These standards provide a foundation for ensuring medical device safety and performance.

- Key hazard profile: incorrect dosage delivery, missed alarm, unsafe therapy continuation ⚠️
  .. important::
    These hazards must be mitigated through thorough testing and validation.

- Interface landscape: device buses, sensor links, alarm/event channels 📈
  .. warning::
    Inadequate interface management can lead to system failures and safety issues.

Domain-Specific Examples
------------------------
### Nominal Example 🟢
Therapy control with validated sensor feedback.

  .. code-block:: markdown

    * GIVEN: Sensor feedback is within valid range
    * WHEN: Therapy control algorithm is executed
    * THEN: Correct dosage is delivered and alarm is triggered

### Boundary Example 🟡
Near-threshold dosing and alarm escalation timing.

  .. code-block:: markdown

    * GIVEN: Sensor feedback is near threshold
    * WHEN: Therapy control algorithm is executed
    * THEN: Dosing is adjusted and alarm is escalated

### Fault Example 🔴
Sensor spike/dropout and actuator command rejection path.

  .. code-block:: markdown

    * GIVEN: Sensor feedback is faulty
    * WHEN: Therapy control algorithm is executed
    * THEN: Actuator command is rejected and system enters fault mode

Patterns
--------
### Derive Acceptance Thresholds 🟢
Derive acceptance thresholds from hazard-linked requirements.

  .. code-block:: markdown

    * Given: Hazard profile is defined
    * When: Acceptance thresholds are derived
    * Then: Thresholds are documented and reviewed

### Keep Interface Timing Contracts Explicit 🟡
Keep interface timing contracts explicit and reviewable.

  .. code-block:: markdown

    * Given: Interface timing contracts are defined
    * When: Contracts are reviewed and updated
    * Then: Timing contracts are up-to-date and accurate

### Compare Nominal and Stressed Traces 🔴
Compare nominal and stressed traces against the same baseline.

  .. code-block:: markdown

    * Given: Nominal and stressed traces are collected
    * When: Traces are compared
    * Then: Differences are documented and investigated

Anti-Patterns
-------------
### Generic Test Claims Without Domain Hazard Mapping 🔴
Generic test claims without domain hazard mapping.

  .. warning::
    This approach can lead to incomplete testing and safety issues.

### Pass/Fail Decisions Without Quantitative Thresholds 🔴
Pass/fail decisions without quantitative thresholds.

  .. important::
    Quantitative thresholds are essential for ensuring safety and performance.

### Evidence Summaries Without Raw Artifact References 🔴
Evidence summaries without raw artifact references.

  .. note::
    Raw artifact references are necessary for reproducing and verifying results.

Pitfalls
--------
### Hidden Assumptions in Environment or Calibration Setup 🔴
Hidden assumptions in environment or calibration setup.

  .. important::
    Assumptions must be documented and validated to ensure accuracy.

### Missing Negative-Path Scenarios for High-Criticality Behavior 🔴
Missing negative-path scenarios for high-criticality behavior.

  .. warning::
    Negative-path scenarios are essential for ensuring safety and performance.

### Incomplete Traceability from Requirement to Verdict 🔴
Incomplete traceability from requirement to verdict.

  .. note::
    Traceability is necessary for ensuring that requirements are met and verified.

Best Practices
--------------
### Tag Every Artifact with Domain Requirement IDs 🟢
Tag every artifact with domain requirement IDs.

  .. code-block:: markdown

    * Given: Artifacts are created
    * When: Requirement IDs are assigned
    * Then: Artifacts are tagged and reviewed

### Capture Timing + Functional Evidence in the Same Run Package 🟡
Capture timing + functional evidence in the same run package.

  .. important::
    This approach ensures that evidence is comprehensive and accurate.

### Record Residual Risk and Ownership Before Closure 🔴
Record residual risk and ownership before closure.

  .. note::
    Residual risk and ownership must be documented to ensure that issues are addressed.

Heuristics
----------
### If a Domain Hazard is Untested, Confidence is Provisional 🟢
If a domain hazard is untested, confidence is provisional.

  .. warning::
    Untested hazards can lead to safety issues and performance problems.

### If Rerun Differs Unexpectedly, Investigate Determinism First 🟡
If rerun differs unexpectedly, investigate determinism first.

  .. important::
    Determinism is essential for ensuring that results are reproducible and accurate.

### If Evidence is Indirect, Reduce Verdict Confidence Level 🔴
If evidence is indirect, reduce verdict confidence level.

  .. note::
    Indirect evidence can lead to incomplete testing and safety issues.

Checklist
---------
### Domain Hazard Coverage is Explicit ☐
Domain hazard coverage is explicit.

### Compliance References are Mapped to Evidence ☐
Compliance references are mapped to evidence.

### Nominal/Boundary/Fault Results are All Documented ☐
Nominal/boundary/fault results are all documented.

### Residual Risks and Next Actions are Assigned ☐
Residual risks and next actions are assigned.

### Evidence Summaries are Complete and Accurate ☐
Evidence summaries are complete and accurate.

### Raw Artifact References are Provided ☐
Raw artifact references are provided.

### Assumptions are Documented and Validated ☐
Assumptions are documented and validated.

### Negative-Path Scenarios are Included ☐
Negative-path scenarios are included.

### Traceability is Complete and Accurate ☐
Traceability is complete and accurate.

### Requirement IDs are Assigned ☐
Requirement IDs are assigned.

### Timing + Functional Evidence is Captured in the Same Run Package ☐
Timing + functional evidence is captured in the same run package.

### Residual Risk and Ownership are Documented ☐
Residual risk and ownership are documented.
