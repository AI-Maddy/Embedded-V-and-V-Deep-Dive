---
title: "GIVEN   WHEN   THEN Scenarios"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# GIVEN / WHEN / THEN Scenarios 📋

-   **Nominal** 🟢:
    -   **GIVEN** a validated sensor feedback loop,
    -   **WHEN** the therapy control system is engaged,
    -   **THEN** the dosage delivered matches the prescribed amount.
-   **Boundary** 🟡:
    -   **GIVEN** a near-threshold dosing scenario,
    -   **WHEN** the alarm escalation timing is triggered,
    -   **THEN** the system should alert the operator within the
        specified time frame.
-   **Fault** 🔴:
    -   **GIVEN** a sensor spike/dropout event,
    -   **WHEN** the actuator command is issued,
    -   **THEN** the system must reject the command and log the fault.

::: note
::: title
Note
:::

Ensure all testing aligns with the relevant standards such as **IEC
62304** for software lifecycle processes and **ISO 14971** for risk
management in medical devices.
:::

::: important
::: title
Important
:::

Document all findings and evidence meticulously to support compliance
and safety claims.
:::

::: warning
::: title
Warning
:::

Failure to adhere to the outlined patterns and best practices may lead
to severe safety risks and regulatory non-compliance.
:::
