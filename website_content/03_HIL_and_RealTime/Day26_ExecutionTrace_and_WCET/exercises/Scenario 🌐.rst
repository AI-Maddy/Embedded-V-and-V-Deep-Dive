Scenario 🌐
-----------
- **Context**: Representative nominal operation for this day's topic, ensuring realistic conditions.
- **Variant A**: Boundary condition near timing/value/mode limits, testing the system's robustness.
- **Variant B**: Fault/negative stimulus with expected detection and recovery, validating fault tolerance.

.. important::
   This section is crucial for establishing the scenarios under which the system will be tested. Each scenario must be carefully crafted to reflect real-world conditions and edge cases.

Setup ⚙️
-------
- **Freeze configuration**: Ensure all parameters are locked to prevent unintended changes.
- **Assumptions**: Clearly document all assumptions made during the setup phase.
- **Acceptance thresholds**: Define clear criteria for success and failure.
- **Enable timestamped logging/tracing**: Activate detailed logging to capture all relevant data.
- **Artifact capture**: Ensure all outputs are stored for future analysis.
- **Confirm interface signal map**: Validate that all signals are correctly mapped.
- **Initial state baseline**: Establish a baseline for comparison during testing.

.. note::
   Proper setup is essential for the validity of the test results. Any oversight in this phase can lead to misleading conclusions.

Procedure 🛠️
-----------
1. **Run nominal scenario** 🟢: Execute the standard operation and record baseline outputs.
   - **GIVEN** the system is in a nominal state,  
   - **WHEN** the standard operation is executed,  
   - **THEN** the outputs should match the expected baseline.

2. **Run boundary variant** 🟡: Execute the boundary condition and capture divergences from the baseline.
   - **GIVEN** the system is at the boundary of operational limits,  
   - **WHEN** the boundary condition is executed,  
   - **THEN** any deviations from the baseline must be documented and analyzed.

3. **Run fault variant** 🔴: Introduce a fault condition and validate the system's safe handling and recovery.
   - **GIVEN** a fault is introduced into the system,  
   - **WHEN** the fault condition is executed,  
   - **THEN** the system should demonstrate safe recovery and log the incident.

4. **Repeat key run**: Confirm repeatability of results by rerunning critical tests.

.. warning::
   Ensure that each test run is conducted under controlled conditions to maintain the integrity of the results.

