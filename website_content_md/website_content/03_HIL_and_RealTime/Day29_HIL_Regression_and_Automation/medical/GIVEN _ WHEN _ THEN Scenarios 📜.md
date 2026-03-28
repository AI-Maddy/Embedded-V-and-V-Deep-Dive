# GIVEN / WHEN / THEN Scenarios 📜

-   **Nominal** 🟢:
    -   **GIVEN** a validated sensor feedback system,
    -   **WHEN** a therapy control command is issued,
    -   **THEN** the system should deliver the correct dosage without
        errors.
-   **Boundary** 🟡:
    -   **GIVEN** a near-threshold dosing scenario,
    -   **WHEN** the alarm escalation timing is triggered,
    -   **THEN** the system should activate alarms within the specified
        timing window.
-   **Fault** 🔴:
    -   **GIVEN** a sensor spike/dropout,
    -   **WHEN** an actuator command is issued,
    -   **THEN** the system should reject the command and log the fault
        appropriately.

::: important
::: title
Important
:::

Always refer to the relevant standards (IEC 62304, ISO 14971, IEC 60601)
when conducting HIL testing to ensure compliance and safety.
:::
