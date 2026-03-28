# GIVEN / WHEN / THEN Scenarios 📊

**Nominal Scenario 🟢** - **GIVEN** a properly configured HIL setup, -
**WHEN** the system is executed under normal conditions, - **THEN** it
should produce expected outputs without failures.

**Boundary Scenario 🟡** - **GIVEN** a HIL setup at the edge of
operational limits, - **WHEN** the system is executed, - **THEN** it
should handle boundary conditions gracefully without crashing.

**Fault Scenario 🔴** - **GIVEN** a HIL setup with a simulated fault, -
**WHEN** the system encounters the fault, - **THEN** it should detect
the fault and trigger the appropriate failure response. This structured
approach ensures that all potential scenarios are considered and
addressed.

::: important
::: title
Important
:::

Always refer to the relevant standards such as ISO 26262 for automotive
systems and IEC 62304 for software lifecycle processes to ensure
compliance and safety. Adhering to these standards is essential for
maintaining industry credibility and ensuring the safety of the systems
being developed.
:::

::: warning
::: title
Warning
:::

Failure to adhere to these guidelines may result in significant safety
risks and non-compliance with industry standards. It is imperative that
all team members are aware of these risks and take proactive measures to
mitigate them.
:::
