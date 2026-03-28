GIVEN / WHEN / THEN Scenarios
------------------------------
- **Nominal Scenario**: 
  - **GIVEN** a configured HIL setup,
  - **WHEN** executing a nominal test case,
  - **THEN** the system should respond within the defined timing profile.

- **Boundary Scenario**: 
  - **GIVEN** a near-threshold input signal,
  - **WHEN** executing the boundary test case,
  - **THEN** the system should maintain operational integrity without failure.

- **Fault Scenario**: 
  - **GIVEN** a simulated fault in the system,
  - **WHEN** executing the fault test case,
  - **THEN** the system should enter a safe state or trigger recovery protocols.

.. note::
   Ensure to document all scenarios thoroughly for future reference and traceability.

.. important::
   Always validate that the acceptance criteria are aligned with the requirements to avoid ambiguity.

.. warning::
   Be cautious of hidden assumptions that may lead to incorrect conclusions during testing.

