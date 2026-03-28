---
title: "Domain Specific Examples"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# Domain-Specific Examples 📚

-   **Nominal 🟢**:
    -   Adaptive cruise and speed regulation under normal traffic.
    -   GIVEN: A calibrated model with nominal traffic inputs.
    -   WHEN: The model executes adaptive cruise control.
    -   THEN: Speed regulation remains within ±2% of target speed.
-   **Boundary 🟡**:
    -   Dense stop-and-go with tight headway and timing limits.
    -   GIVEN: Traffic density exceeds 80 vehicles/km.
    -   WHEN: Headway drops below 1.5 seconds.
    -   THEN: System maintains safe braking distance without
        oscillations.
-   **Fault 🔴**:
    -   Sensor dropout and invalid CAN frame injection.
    -   GIVEN: A simulated sensor dropout and corrupted CAN frames.
    -   WHEN: The model processes invalid data.
    -   THEN: The system triggers fallback safety mechanisms within
        100ms.
