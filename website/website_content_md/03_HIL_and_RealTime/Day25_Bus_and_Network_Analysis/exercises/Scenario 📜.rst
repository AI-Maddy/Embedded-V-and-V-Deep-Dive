Scenario 📜
-----------
- **Context**: Representative nominal operation for this day's topic, ensuring that all components interact correctly under standard conditions.
- **Variant A**: Boundary condition near timing/value/mode limits, testing the system's response to extreme but valid inputs.
- **Variant B**: Fault/negative stimulus with expected detection and recovery, assessing the system's resilience and error-handling capabilities.

Setup ⚙️
-------
- Freeze configuration, assumptions, and acceptance thresholds to establish a stable testing environment.
- Enable timestamped logging/tracing and artifact capture for detailed post-exercise analysis.
- Confirm interface signal map and initial state baseline to ensure all components are correctly configured.

Procedure 🛠️
-----------
1. **Run Nominal Scenario**: Execute the nominal scenario and record baseline outputs for comparison.
2. **Run Boundary Variant**: Execute the boundary condition variant and capture any divergences from expected behavior.
3. **Run Fault Variant**: Execute the fault variant and validate the system's safe handling and recovery mechanisms.
4. **Repeat Key Run**: Conduct a key run to confirm repeatability of results, ensuring consistency across multiple executions.

🟢 Nominal Scenario:
   - **GIVEN** the system is in a nominal state,
   - **WHEN** the nominal scenario is executed,
   - **THEN** the outputs should match the established baseline.

🟡 Boundary Scenario:
   - **GIVEN** the system is near its operational limits,
   - **WHEN** the boundary variant is executed,
   - **THEN** the system should detect and report any deviations.

🔴 Fault Scenario:
   - **GIVEN** a fault is injected into the system,
   - **WHEN** the fault variant is executed,
   - **THEN** the system should recover safely and log the incident.

