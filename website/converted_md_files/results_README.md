Medical Focus --- Day30 Final Capstone 🏥
=====================================

**MEDICS** Mnemonic for HIL Phase 🤖
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   **M** - Mitigate hazards through thorough testing and validation
-   **E** - Ensure compliance with IEC 62304, ISO 14971, and IEC 60601
-   **D** - Document assumptions, raw artifact references, and residual
    risks
-   **I** - Interface management is critical for system safety and
    performance
-   **C** - Capture timing and functional evidence in the same run
    package
-   **S** - Safety and performance are top priorities in medical device
    development

Objective 🎯 \-\-\-\-\-\-\-\--Apply this day in **Medical** context with
explicit safety, compliance, and evidence expectations. 💊

Phase Context 🤖 \-\-\-\-\-\-\-\-\-\-\-\--Phase: **HIL**
(Hardware-in-the-Loop) Primary focus: **hardware-integrated timing and
interface confidence**. Section focus: **results consolidation and
release-readiness evidence**.

Domain Constraints 📚 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Compliance
baseline: **IEC 62304 + ISO 14971 + IEC 60601 context** .. note:: These
standards provide a foundation for ensuring medical device safety and
performance.

-   Key hazard profile: incorrect dosage delivery, missed alarm, unsafe
    therapy continuation ⚠️ .. important:: These hazards must be
    mitigated through thorough testing and validation.
-   Interface landscape: device buses, sensor links, alarm/event
    channels 📈 .. warning:: Inadequate interface management can lead to
    system failures and safety issues.

Domain-Specific Examples 📝
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--### Nominal Example 🟢
Therapy control with validated sensor feedback.

> ``` markdown
> * GIVEN: Sensor feedback is within valid range
> * WHEN: Therapy control algorithm is executed
> * THEN: Correct dosage is delivered and alarm is triggered
> ```

\### Boundary Example 🟡 Near-threshold dosing and alarm escalation
timing.

> ``` markdown
> * GIVEN: Sensor feedback is near threshold
> * WHEN: Therapy control algorithm is executed
> * THEN: Dosing is adjusted and alarm is escalated
> ```

\### Fault Example 🔴 Sensor spike/dropout and actuator command
rejection path.

> ``` markdown
> * GIVEN: Sensor feedback is faulty
> * WHEN: Therapy control algorithm is executed
> * THEN: Actuator command is rejected and system enters fault mode
> ```

Patterns 🔍 \-\-\-\-\-\-\--### Derive Acceptance Thresholds 🟢 Derive
acceptance thresholds from hazard-linked requirements.

> ``` markdown
> * Given: Hazard profile is defined
> * When: Acceptance thresholds are derived
> * Then: Thresholds are documented and reviewed
> ```

\### Keep Interface Timing Contracts Explicit 🟡 Keep interface timing
contracts explicit and reviewable.

> ``` markdown
> * Given: Interface timing contracts are defined
> * When: Contracts are reviewed and updated
> * Then: Timing contracts are up-to-date and accurate
> ```

\### Compare Nominal and Stressed Traces 🔴 Compare nominal and stressed
traces against the same baseline.

> ``` markdown
> * Given: Nominal and stressed traces are collected
> * When: Traces are compared
> * Then: Differences are documented and investigated
> ```

Anti-Patterns 🚫 \-\-\-\-\-\-\-\-\-\-\-\--### Generic Test Claims
Without Domain Hazard Mapping 🔴 Generic test claims without domain
hazard mapping.

> ::: warning
> ::: title
> Warning
> :::
>
> This approach can lead to incomplete testing and safety issues.
> :::

\### Pass/Fail Decisions Without Quantitative Thresholds 🔴 Pass/fail
decisions without quantitative thresholds.

> ::: important
> ::: title
> Important
> :::
>
> Quantitative thresholds are essential for ensuring safety and
> performance.
> :::

\### Evidence Summaries Without Raw Artifact References 🔴 Evidence
summaries without raw artifact references.

> ::: note
> ::: title
> Note
> :::
>
> Raw artifact references are necessary for reproducing and verifying
> results.
> :::

Pitfalls 🚨 \-\-\-\-\-\-\--### Hidden Assumptions in Environment or
Calibration Setup 🔴 Hidden assumptions in environment or calibration
setup.

> ::: important
> ::: title
> Important
> :::
>
> Assumptions must be documented and validated to ensure accuracy.
> :::

\### Missing Negative-Path Scenarios for High-Criticality Behavior 🔴
Missing negative-path scenarios for high-criticality behavior.

> ::: warning
> ::: title
> Warning
> :::
>
> Negative-path scenarios are essential for ensuring safety and
> performance.
> :::

\### Incomplete Traceability from Requirement to Verdict 🔴 Incomplete
traceability from requirement to verdict.

> ::: note
> ::: title
> Note
> :::
>
> Traceability is necessary for ensuring that requirements are met and
> verified.
> :::

Best Practices 🏆 \-\-\-\-\-\-\-\-\-\-\-\-\--### Tag Every Artifact with
Domain Requirement IDs 🟢 Tag every artifact with domain requirement
IDs.

> ``` markdown
> * Given: Artifacts are created
> * When: Requirement IDs are assigned
> * Then: Artifacts are tagged and reviewed
> ```

\### Capture Timing + Functional Evidence in the Same Run Package 🟡
Capture timing + functional evidence in the same run package.

> ::: important
> ::: title
> Important
> :::
>
> This approach ensures that evidence is comprehensive and accurate.
> :::

\### Record Residual Risk and Ownership Before Closure 🔴 Record
residual risk and ownership before closure.

> ::: note
> ::: title
> Note
> :::
>
> Residual risk and ownership must be documented to ensure that issues
> are addressed.
> :::

Heuristics 🔮 \-\-\-\-\-\-\-\-\--### If a Domain Hazard is Untested,
Confidence is Provisional 🟢 If a domain hazard is untested, confidence
is provisional.

> ::: warning
> ::: title
> Warning
> :::
>
> Untested hazards can lead to safety issues and performance problems.
> :::

\### If Rerun Differs Unexpectedly, Investigate Determinism First 🟡 If
rerun differs unexpectedly, investigate determinism first.

> ::: important
> ::: title
> Important
> :::
>
> Determinism is essential for ensuring that results are reproducible
> and accurate.
> :::

\### If Evidence is Indirect, Reduce Verdict Confidence Level 🔴 If
evidence is indirect, reduce verdict confidence level.

> ::: note
> ::: title
> Note
> :::
>
> Indirect evidence can lead to incomplete testing and safety issues.
> :::

Severity / Priority Colour Legend 🟢🟡🔴
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\* 🟢 -
Low severity / priority \* 🟡 - Medium severity / priority \* 🔴 - High
severity / priority

Pre-Review Checklist 📝 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--..
list-table:: :widths: 50 50 :stub-columns: 1

> -   -   [ ] Domain hazard coverage is explicit
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Compliance references are mapped to evidence
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Nominal/boundary/fault results are all documented
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Residual risks and next actions are assigned
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Evidence summaries are complete and accurate
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Raw artifact references are provided
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Assumptions are documented and validated
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Negative-path scenarios are included
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Traceability is complete and accurate
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Requirement IDs are assigned
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Timing + functional evidence is captured in the same run
>         package
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
>
> -   -   [ ] Residual risk and ownership are documented
>     -   Reference: IEC 62304, ISO 14971, IEC 60601
