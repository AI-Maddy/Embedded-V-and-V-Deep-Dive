**GIVEN / WHEN / THEN Templates** 🛠️
------------------------------------
- 🟢 **Nominal Scenario**:  
  GIVEN a valid input and standard configuration,  
  WHEN the model is executed under normal conditions,  
  THEN the output matches the expected requirement behavior.  

- 🟡 **Boundary Scenario**:  
  GIVEN an input near the operational limit,  
  WHEN the model is executed under stressed conditions,  
  THEN the output demonstrates compliance with defined thresholds.  

- 🔴 **Fault Scenario**:  
  GIVEN an invalid input or fault injection,  
  WHEN the model is executed,  
  THEN the system detects the fault and recovers per requirement specifications.  

.. warning::
   Ensure all fault scenarios comply with **ISO 26262 Part 4** and **DO-178C Section 6.4** for safety-critical systems.
