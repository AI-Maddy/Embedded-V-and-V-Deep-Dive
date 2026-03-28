    :::

    This scenario demonstrates proper fault detection and containment.
    :::

    ::: admonition
    This scenario is critical for ensuring infusion pump can handle
    faults.
    :::

\### 4. Degraded-Mode Continuation with Safety Constraints 🟢

-   GIVEN: Infusion pump experiences a partial failure (e.g., reduced
    flow rate).

-   WHEN: User continues therapy with safety constraints in place.

-   THEN: Pump maintains safe and consistent medication delivery.

    ::: note
    ::: title
    Note
    :::

    This scenario is critical for ensuring infusion pump can continue to
    operate safely in degraded modes.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper safety constraints are essential for ensuring patient safety.
    :::

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly implement safety constraints may result in
    product failures or safety issues.
    :::

\### 5. Regression Stability after Fixes 🟡

-   GIVEN: Infusion pump has undergone software updates or hardware
    modifications.

-   WHEN: User verifies therapy control with validated sensor feedback.

-   THEN: Pump demonstrates stable and accurate performance.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly test regression stability may result in product
    failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper testing of regression stability is essential for ensuring
    infusion pump performance.
    :::

    ::: note
    ::: title
    Note
    :::

    This scenario demonstrates proper regression stability.
    :::

Domain-Specific Examples 📚
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--### Example A (Nominal)
🟢

-   Therapy control with validated sensor feedback.

-   Evidence: Pump calibration and configuration records.

-   Compliance: IEC 60601-1:2012, Clause 8.2.1.

    ::: note
    ::: title
    Note
    :::

    This example demonstrates proper therapy control with validated
    sensor feedback.
    :::

    ::: important
