# Scenario Templates 📜

**Nominal Scenario 🟢** GIVEN: A model with verified inputs. WHEN:
Simulated under nominal conditions. THEN: The outputs match expected
behavior within tolerance.

**Boundary Scenario 🟡** GIVEN: A model with edge-case inputs. WHEN:
Simulated near operational limits. THEN: The outputs remain stable and
within safety thresholds.

**Fault Scenario 🔴** GIVEN: A model exposed to fault injection. WHEN:
Simulated under degraded conditions. THEN: The system detects and
mitigates the fault as per requirements.
