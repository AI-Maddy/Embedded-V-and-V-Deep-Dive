---
title: "Domain Specific Examples"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# Domain-Specific Examples 📋

-   **Nominal 🟢**: Therapy control with validated sensor feedback.
    **GIVEN**: A calibrated sensor and nominal therapy settings.
    **WHEN**: The therapy control loop is executed. **THEN**: Sensor
    feedback matches expected thresholds, and therapy is delivered
    correctly.
-   **Boundary 🟡**: Near-threshold dosing and alarm escalation timing.
    **GIVEN**: A therapy setting near the upper dosage limit. **WHEN**:
    The system detects a threshold breach. **THEN**: Alarm escalation
    occurs within the prescribed timing window.
-   **Fault 🔴**: Sensor spike/dropout and actuator command rejection
    path. **GIVEN**: A sensor experiences a transient spike/dropout.
    **WHEN**: The actuator receives an invalid command. **THEN**: The
    system rejects the command and triggers a fault response.
