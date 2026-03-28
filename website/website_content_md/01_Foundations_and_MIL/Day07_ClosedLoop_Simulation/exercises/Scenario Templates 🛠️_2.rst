Scenario Templates 🛠️
----------------------
🟢 **Nominal Scenario**  
**GIVEN**: A standard configuration and input set.  
**WHEN**: Simulation executes under normal conditions.  
**THEN**: Results match expected outputs with no anomalies.

🟡 **Boundary Scenario**  
**GIVEN**: Inputs near operational limits (e.g., timing thresholds).  
**WHEN**: Simulation executes with edge-case parameters.  
**THEN**: Outputs remain within acceptable tolerances, with no failures.

🔴 **Fault Scenario**  
**GIVEN**: Invalid or unexpected input sequences.  
**WHEN**: Simulation executes with fault-inducing conditions.  
**THEN**: System detects errors and recovers gracefully, meeting robustness criteria.

