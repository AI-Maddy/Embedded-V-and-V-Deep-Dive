Additional Deep-Dive Notes
--------------------------
- **Domain Focus**: General  
- **Phase Focus**: HIL  
- **Evidence Priorities**: Functional correctness, timing behavior, robustness, and traceability.  
- **Patterns**: Baseline-first comparison, fixed acceptance thresholds, deterministic reruns.  
- **Anti-Patterns**: Post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.  
- **Pitfalls**: Hidden assumptions, interface timing drift, weak requirement-to-test linkage.  
- **Example Expansion**: Include one nominal, one boundary, and one fault scenario per objective.  
- **Review Heuristic**: If a claim cannot be tied to an artifact, mark confidence as provisional.  
- **Checklist Extension**: Capture residual risk, ownership, and next action for each unresolved item.  

**Scenario Templates**  
- **Nominal 🟢**:  
  **GIVEN** a defined baseline scenario,  
  **WHEN** the system executes under normal conditions,  
  **THEN** the output should match the expected results.

- **Boundary 🟡**:  
  **GIVEN** a scenario at the edge of operational limits,  
  **WHEN** the system is subjected to boundary conditions,  
  **THEN** the system should maintain stability and provide valid outputs.

- **Fault 🔴**:  
  **GIVEN** a fault condition introduced in the system,  
  **WHEN** the system encounters this fault,  
  **THEN** it should trigger the appropriate error handling mechanisms and not propagate failure.  

.. list-table:: Severity/priority colour legend
   :widths: 10 10
   :header-rows: 1

   * - Severity Level
     - Description
   * - 🟢 Nominal
     - Normal operation, expected behavior.
   * - 🟡 Boundary
     - Edge cases, potential failure points.
   * - 🔴 Fault
     - Critical failures, system risks.
