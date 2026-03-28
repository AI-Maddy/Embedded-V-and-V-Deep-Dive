📖 Scenario Templates 🧪
------------------------
**Nominal Scenario 🟢**  
GIVEN: A correctly configured model with valid inputs.  
WHEN: The model executes under nominal conditions.  
THEN: The system produces outputs that match the requirement intent.

**Boundary Scenario 🟡**  
GIVEN: A model with edge-case inputs (e.g., maximum allowable values).  
WHEN: The model executes under boundary conditions.  
THEN: The system maintains functional correctness but exhibits degraded performance within acceptable limits.

**Fault Scenario 🔴**  
GIVEN: A model with invalid or noisy inputs.  
WHEN: The model executes under fault conditions.  
THEN: The system detects the fault, triggers recovery mechanisms, and logs the event for analysis.

