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
