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

Utilize the following scenarios to guide your testing and validation
efforts.
:::

-   **Nominal** 🟢: **GIVEN** the vehicle is in adaptive cruise mode,
    **WHEN** the traffic is flowing normally, **THEN** the speed
    regulation should maintain the set speed without deviation.
-   **Boundary** 🟡: **GIVEN** the vehicle is approaching a dense
    stop-and-go situation, **WHEN** the headway is tight and timing
    limits are reached, **THEN** the system should respond without
    unintended acceleration or braking.
-   **Fault** 🔴: **GIVEN** a sensor dropout occurs, **WHEN** an invalid
    CAN frame is injected, **THEN** the system should enter a safe state
    without compromising vehicle control.
