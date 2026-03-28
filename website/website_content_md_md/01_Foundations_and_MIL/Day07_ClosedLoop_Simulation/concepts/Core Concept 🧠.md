# Core Concept 🧠

-   **Define** the primary mechanism and expected behavior.
-   **Identify** assumptions and boundary conditions.
-   **State** what failure looks like and how it should be detected.

🟢 **Nominal Scenario**

:   **GIVEN** a model with validated inputs and expected outputs,
    **WHEN** the system operates under standard conditions, **THEN** the
    simulation should produce results that match the requirements
    traceability matrix.

🟡 **Boundary Scenario**

:   **GIVEN** a model with inputs at the edge of operational limits,
    **WHEN** the system is subjected to stress conditions, **THEN** the
    simulation should demonstrate graceful degradation or adherence to
    boundary thresholds.

🔴 **Fault Scenario**

:   **GIVEN** a model with an injected fault or invalid input, **WHEN**
    the system processes the fault condition, **THEN** the simulation
    should detect the fault and trigger the appropriate failure response
    mechanism.
