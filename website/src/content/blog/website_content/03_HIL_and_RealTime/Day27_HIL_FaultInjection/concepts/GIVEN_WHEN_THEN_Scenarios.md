---
title: "GIVEN WHEN THEN Scenarios"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---



# GIVEN / WHEN / THEN Scenarios 📜

-   **Nominal (🟢)**:
    -   **GIVEN** a properly configured HIL system,
    -   **WHEN** a fault is injected,
    -   **THEN** the system should respond according to the defined
        requirements.
-   **Boundary (🟡)**:
    -   **GIVEN** the system is operating at its maximum load,
    -   **WHEN** a fault is injected,
    -   **THEN** the system should maintain functionality without
        exceeding safety thresholds.
-   **Fault (🔴)**:
    -   **GIVEN** a critical component fails,
    -   **WHEN** the fault is injected,
    -   **THEN** the system should enter a safe state and log the
        failure.

::: note
::: title
Note
:::

These scenarios should be validated against the relevant standards to
ensure compliance and reliability.
:::

::: important
::: title
Important
:::

Regularly review and update the scenarios to reflect changes in system
design and operational requirements.
:::

::: note
::: title
Note
:::

This document should be used as a living document, continuously updated
to reflect the latest insights and methodologies in HIL fault injection,
ensuring alignment with industry standards such as IEC 62304 and ASPICE.
:::
