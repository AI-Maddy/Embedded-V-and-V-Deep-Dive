---
title: "GIVEN   WHEN   THEN Scenarios"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# GIVEN / WHEN / THEN Scenarios 📋

::: important
::: title
Important
:::

Use these scenarios to guide your testing strategy.
:::

-   **Nominal Scenario** 🟢:
    -   **GIVEN** a validated therapy control system,
    -   **WHEN** the sensor feedback is within expected ranges,
    -   **THEN** the system should deliver the correct dosage.
-   **Boundary Scenario** 🟡:
    -   **GIVEN** a dosing threshold near the upper limit,
    -   **WHEN** the alarm escalation timing is triggered,
    -   **THEN** the system should alert the operator without delay.
-   **Fault Scenario** 🔴:
    -   **GIVEN** a sensor dropout occurs,
    -   **WHEN** an actuator command is issued,
    -   **THEN** the system should safely reject the command and
        activate a fallback protocol.
