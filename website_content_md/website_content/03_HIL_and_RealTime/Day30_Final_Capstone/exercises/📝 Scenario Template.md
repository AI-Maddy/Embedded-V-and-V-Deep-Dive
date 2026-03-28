# 📝 Scenario Template

\### Nominal Scenario 🟢

-   GIVEN: Representative nominal operation for this day topic.
-   WHEN: Run the nominal scenario.
-   THEN: Record baseline outputs.

\### Boundary Scenario 🟡

-   GIVEN: Boundary condition near timing/value/mode limits.
-   WHEN: Run the boundary variant.
-   THEN: Capture divergences.

\### Fault Scenario 🔴

-   GIVEN: Fault/negative stimulus with expected detection and recovery.
-   WHEN: Run the fault variant.
-   THEN: Validate safe handling/recovery.
