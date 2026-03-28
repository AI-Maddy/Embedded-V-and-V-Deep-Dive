# GIVEN / WHEN / THEN Scenarios 📋

**Nominal** 🟢: - **GIVEN** a validated therapy control system, -
**WHEN** the sensor feedback is within expected ranges, - **THEN** the
system delivers the correct dosage without errors.

**Boundary** 🟡: - **GIVEN** a dosing threshold close to the maximum
limit, - **WHEN** the alarm escalation timing is triggered, - **THEN**
the system must respond within the defined timing constraints.

**Fault** 🔴: - **GIVEN** a sensor dropout occurs, - **WHEN** an
actuator command is issued, - **THEN** the system must reject the
command and log the fault for analysis.
