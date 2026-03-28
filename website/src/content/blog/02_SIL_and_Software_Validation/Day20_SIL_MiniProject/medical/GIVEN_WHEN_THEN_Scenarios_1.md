---
title: "GIVEN   WHEN   THEN Scenarios"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# GIVEN / WHEN / THEN Scenarios 📋

-   **Nominal** 🟢:
    -   **GIVEN** a validated sensor feedback system,
    -   **WHEN** therapy control is activated,
    -   **THEN** the system delivers the correct dosage as per the
        specifications.
-   **Boundary** 🟡:
    -   **GIVEN** a near-threshold dosing scenario,
    -   **WHEN** an alarm escalation is triggered,
    -   **THEN** the system responds within the defined timing
        constraints.
-   **Fault** 🔴:
    -   **GIVEN** a sensor spike/dropout,
    -   **WHEN** an actuator command is issued,
    -   **THEN** the system should reject the command and log the fault
        for analysis.

::: important
::: title
Important
:::

Always refer to the relevant domain standards such as IEC 62304, ISO
14971, and IEC 60601 for compliance and safety requirements during the
V&V process.
:::
