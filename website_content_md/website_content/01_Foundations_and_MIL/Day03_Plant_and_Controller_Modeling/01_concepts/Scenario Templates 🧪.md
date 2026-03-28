# Scenario Templates 🧪

**Nominal Scenario** 🟢 - **GIVEN**: A plant model with validated
parameters and a controller in nominal mode. - **WHEN**: The system
operates within expected ranges. - **THEN**: The output matches the
expected baseline with \<1% deviation.

**Boundary Scenario** 🟡 - **GIVEN**: A plant model with edge-case
parameters (e.g., maximum temperature). - **WHEN**: The controller
transitions between modes. - **THEN**: The system maintains stability
without exceeding safety thresholds.

**Fault Scenario** 🔴 - **GIVEN**: A plant model with injected
disturbances (e.g., sensor failure). - **WHEN**: The controller detects
the fault condition. - **THEN**: The system enters fallback mode and
logs the fault correctly.
