# Examples 🧪

-   **Nominal Scenario 🟢**:
    -   **GIVEN**: Stable flight-control mode tracking with expected
        disturbances.
    -   **WHEN**: The system receives nominal sensor inputs and executes
        control logic.
    -   **THEN**: The aircraft maintains stable flight within predefined
        thresholds.
-   **Boundary Scenario 🟡**:
    -   **GIVEN**: High-workload transition envelope near stability
        margins.
    -   **WHEN**: The system encounters rapid mode transitions with
        increased actuator demands.
    -   **THEN**: The system must recover stability without exceeding
        operational limits.
-   **Fault Scenario 🔴**:
    -   **GIVEN**: Bus label corruption and sensor disagreement event.
    -   **WHEN**: Fault injection simulates corrupted data on ARINC 429
        bus.
    -   **THEN**: The system detects the fault, isolates affected
        components, and transitions to a safe state.
