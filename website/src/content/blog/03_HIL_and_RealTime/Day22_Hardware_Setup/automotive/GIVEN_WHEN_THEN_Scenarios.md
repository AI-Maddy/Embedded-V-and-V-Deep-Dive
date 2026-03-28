---
title: "GIVEN   WHEN   THEN Scenarios"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# GIVEN / WHEN / THEN Scenarios 📜

-   **Nominal** 🟢:
    -   **GIVEN** the system is in normal traffic conditions,
    -   **WHEN** the adaptive cruise control is activated,
    -   **THEN** the vehicle maintains a safe distance and speed.
-   **Boundary** 🟡:
    -   **GIVEN** the system is in a dense stop-and-go traffic scenario,
    -   **WHEN** the vehicle approaches a stopping point,
    -   **THEN** the braking system engages effectively without
        exceeding timing limits.
-   **Fault** 🔴:
    -   **GIVEN** a sensor dropout occurs,
    -   **WHEN** an invalid CAN frame is injected,
    -   **THEN** the system should enter a safe state or provide a fault
        indication.

::: note
::: title
Note
:::

For further details on compliance and safety standards, refer to **ISO
26262** and **ISO 21434** documentation to ensure all requirements are
met.
:::

::: important
::: title
Important
:::

Always ensure that all test results are documented and reviewed to
maintain compliance and safety standards.
:::

::: warning
::: title
Warning
:::

Be vigilant for any hidden assumptions that may affect the validation
process, as they can lead to significant risks if left unaddressed.
:::
