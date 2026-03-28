# GIVEN / WHEN / THEN Scenarios 📜

-   **Nominal (🟢)**:
    -   **GIVEN** the hardware is powered on,
    -   **WHEN** the system receives a valid input signal,
    -   **THEN** the expected output should be generated within the
        defined response time.
-   **Boundary (🟡)**:
    -   **GIVEN** the hardware is operating at the upper limit of its
        specified temperature range,
    -   **WHEN** a signal is sent to the system,
    -   **THEN** the system should still respond correctly without
        failure.
-   **Fault (🔴)**:
    -   **GIVEN** a fault occurs in the communication interface,
    -   **WHEN** the system attempts to process the incoming data,
    -   **THEN** the system should enter a safe state and log the fault
        for analysis.

::: important
::: title
Important
:::

Always refer to the relevant domain standards (DO-178C, DO-254, ISO
26262) to ensure compliance and best practices in V&V activities.
:::
