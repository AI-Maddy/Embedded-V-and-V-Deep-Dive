🟢🟡🔴 Scenario Templates 🧪
---------------------------
**Nominal Scenario 🟢**  
GIVEN: A model configured with baseline parameters.  
WHEN: The system executes under nominal conditions.  
THEN: The output matches expected behavior within defined thresholds.

**Boundary Scenario 🟡**  
GIVEN: A model configured with edge-case parameters.  
WHEN: The system operates near the limits of acceptable input.  
THEN: The system maintains functional correctness without exceeding timing constraints.

**Fault Scenario 🔴**  
GIVEN: A model subjected to invalid or noisy inputs.  
WHEN: The system encounters an unexpected failure condition.  
THEN: The system gracefully handles the fault and logs recovery actions.

