Medical Infusion Pump Use Cases and Examples 🏥💊
==============================================

🟢 **Domain-Specific Mnemonic:** MIPUSE (Medical Infusion Pump Use
Scenarios and Evidence)

Purpose 🤔 \-\-\-\-\-\--🟢 **Nominal** (Expected Behavior) 🟡
**Boundary** (Edge Cases) 🔴 **Fault** (Error Conditions) Provide
domain-tailored use cases with evidence expectations aligned to **IEC
62304 + ISO 14971 + IEC 60601 context**.

Representative Use Cases 📝
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--### 1. Nominal
Mission/Profile Operation 🟢

-   GIVEN: Infusion pump is calibrated and configured correctly.

-   WHEN: User initiates therapy control with validated sensor feedback.

-   THEN: Pump delivers accurate and consistent medication dosages.

    ::: note
    ::: title
    Note
    :::

    This scenario is critical for ensuring the safety and efficacy of
    the infusion pump.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper calibration and configuration are essential for accurate
    dosing.
    :::

    ::: admonition
    This scenario demonstrates proper therapy control with validated
    sensor feedback.
    :::

\### 2. Boundary-Condition Operation near Limits 🟡

-   GIVEN: Infusion pump is operating near its capacity limits (e.g.,
    maximum flow rate).

-   WHEN: User attempts to initiate therapy control with near-threshold
    dosing.

-   THEN: Pump alerts user with timely and relevant alarm escalation.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly test boundary conditions may result in product
    failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper testing of boundary conditions is essential for ensuring
    infusion pump performance.
    :::

    ::: note
    ::: title
    Note
    :::

    This scenario demonstrates proper alarm escalation timing.
    :::

\### 3. Fault Detection, Containment, and Recovery 🔴

-   GIVEN: Infusion pump detects a sensor spike or dropout.

-   WHEN: Pump initiates actuator command rejection path.

-   THEN: Pump safely halts therapy and alerts user with error message.

    ::: important
    ::: title
    Important
    :::

    Proper fault detection and containment are essential for ensuring
    patient safety.
    :::

    ::: note
    ::: title
    Note
