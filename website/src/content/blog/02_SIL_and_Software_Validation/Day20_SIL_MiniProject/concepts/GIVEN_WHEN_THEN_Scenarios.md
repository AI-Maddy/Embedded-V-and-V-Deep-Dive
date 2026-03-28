---
title: "GIVEN WHEN THEN Scenarios"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---



# GIVEN / WHEN / THEN Scenarios 📖

-   **Nominal (🟢)**:
    -   **GIVEN** the software is operating within normal parameters,
    -   **WHEN** a valid input is received,
    -   **THEN** the expected output should be produced without errors.
-   **Boundary (🟡)**:
    -   **GIVEN** the software is operating at the edge of its defined
        limits,
    -   **WHEN** an input approaches the boundary condition,
    -   **THEN** the system should handle the input gracefully without
        failure.
-   **Fault (🔴)**:
    -   **GIVEN** a fault is injected into the system,
    -   **WHEN** the fault condition is triggered,
    -   **THEN** the system should detect the fault and initiate a
        predefined recovery procedure.

::: important
::: title
Important
:::

Adhere to the guidelines of ARP4754A and DO-254 when defining scenarios
to ensure comprehensive coverage of all potential operational states.
:::

::: warning
::: title
Warning
:::

Failure to adequately document assumptions and boundary conditions may
lead to significant project risks and undermine the validation efforts.
:::
