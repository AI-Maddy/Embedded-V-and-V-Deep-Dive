---
title: "Domain Specific Examples"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# Domain-Specific Examples 📚

🟢 **Nominal Scenario**:

:   -   GIVEN adaptive cruise control is active.
    -   WHEN the vehicle follows normal traffic flow.
    -   THEN speed regulation should maintain headway within 2 meters.

🟡 **Boundary Scenario**:

:   -   GIVEN stop-and-go traffic with tight timing constraints.
    -   WHEN headway reduces to 1 meter.
    -   THEN system should avoid collisions while maintaining stability.

🔴 **Fault Scenario**:

:   -   GIVEN a sensor dropout occurs.
    -   WHEN invalid CAN frames are injected.
    -   THEN the system should enter a safe state and notify the driver.
