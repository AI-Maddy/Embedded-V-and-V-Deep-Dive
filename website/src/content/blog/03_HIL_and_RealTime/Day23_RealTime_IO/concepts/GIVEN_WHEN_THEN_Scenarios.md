---
title: "GIVEN   WHEN   THEN Scenarios"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# GIVEN / WHEN / THEN Scenarios 📜

-   **Nominal 🟢**:
    -   **GIVEN** the system is operating under normal conditions,
    -   **WHEN** a valid input is received,
    -   **THEN** the expected output should be produced within the
        defined time frame.
-   **Boundary 🟡**:
    -   **GIVEN** the system is at the edge of its operational limits,
    -   **WHEN** an input is received that is at the threshold,
    -   **THEN** the system should handle the input gracefully without
        failure.
-   **Fault 🔴**:
    -   **GIVEN** a fault condition is introduced,
    -   **WHEN** the system detects the fault,
    -   **THEN** it should trigger the appropriate error handling
        mechanisms and log the fault for analysis.

::: important
::: title
Important
:::

Always refer to relevant standards such as IEC 62304 for software
lifecycle processes and DO-178C for software considerations in airborne
systems when developing concepts and verification strategies.
:::
