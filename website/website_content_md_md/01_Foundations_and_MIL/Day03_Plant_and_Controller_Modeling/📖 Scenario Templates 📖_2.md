# 📖 Scenario Templates 📖

**GIVEN / WHEN / THEN Format**

🟢 **Nominal Scenario**: GIVEN the model is configured with baseline
parameters, WHEN the input signal is within expected range, THEN the
output matches the requirement intent without deviation.

🟡 **Boundary Scenario**: GIVEN the model is configured with edge-case
parameters, WHEN the input signal approaches the threshold, THEN the
output exhibits acceptable degradation within defined limits.

🔴 **Fault Scenario**: GIVEN the model is subjected to invalid input or
fault injection, WHEN the system enters degraded mode, THEN the output
demonstrates safe failure behavior as per requirements.
