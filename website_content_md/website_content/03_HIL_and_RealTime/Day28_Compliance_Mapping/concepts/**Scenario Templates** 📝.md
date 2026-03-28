# **Scenario Templates** 📝

-   **Nominal Scenario (🟢)**:
    -   **GIVEN** the system is operating under normal conditions,
    -   **WHEN** a valid input signal is received,
    -   **THEN** the system should respond within the specified time
        frame.
-   **Boundary Scenario (🟡)**:
    -   **GIVEN** the system is operating at the edge of its defined
        limits,
    -   **WHEN** an input signal approaches the maximum threshold,
    -   **THEN** the system should maintain stability without failure.
-   **Fault Scenario (🔴)**:
    -   **GIVEN** a sensor fails during operation,
    -   **WHEN** the system detects the fault,
    -   **THEN** it should trigger the predefined safe response
        mechanism.
