# GIVEN / WHEN / THEN Scenarios 📊

-   **Nominal (🟢)**:
    -   **GIVEN** the aircraft is in stable flight mode,
    -   **WHEN** a disturbance occurs,
    -   **THEN** the flight-control system maintains control within
        specified parameters, ensuring safe operation.
-   **Boundary (🟡)**:
    -   **GIVEN** the aircraft is near the stability margin,
    -   **WHEN** workload increases significantly,
    -   **THEN** the system should transition smoothly without loss of
        control, demonstrating robustness under stress.
-   **Fault (🔴)**:
    -   **GIVEN** a bus label corruption event occurs,
    -   **WHEN** the sensor data is inconsistent,
    -   **THEN** the system should trigger a fault response and revert
        to a safe state, ensuring safety is prioritized.

::: important
::: title
Important
:::

Remember to document all findings and ensure traceability to
requirements as per DO-178C and DO-254 standards.
:::

::: warning
::: title
Warning
:::

Failure to adhere to compliance standards may result in severe safety
implications, potentially endangering lives.
:::

::: admonition
Always review the interface landscape and ensure all components are
functioning as intended to maintain system integrity.
:::
