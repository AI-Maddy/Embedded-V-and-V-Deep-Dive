# GIVEN / WHEN / THEN Scenarios 🧪

-   **Nominal Scenario** 🟢 GIVEN a model configured with baseline
    assumptions, WHEN the nominal signal is applied, THEN the system
    meets requirement R1 with latency \< 10ms.
-   **Boundary Scenario** 🟡 GIVEN a model under high computational
    load, WHEN the signal approaches the jitter threshold, THEN the
    system meets requirement R2 with jitter \< 5ms.
-   **Fault Scenario** 🔴 GIVEN a model with invalid input, WHEN the
    signal exceeds the expected range, THEN the system violates
    requirement R3, and residual risk is logged.
