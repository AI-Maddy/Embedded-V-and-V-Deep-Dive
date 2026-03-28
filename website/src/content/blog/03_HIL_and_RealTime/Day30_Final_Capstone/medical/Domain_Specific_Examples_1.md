---
title: "Domain Specific Examples"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---



# Domain-Specific Examples

\### Nominal Scenario 🟢 \* **GIVEN:** Therapy control system with
validated sensor feedback. \* **WHEN:** Normal operation with validated
sensor inputs. \* **THEN:** Therapy delivery is accurate and alarms are
triggered correctly.

\### Boundary Scenario 🟡 \* **GIVEN:** Therapy control system near
threshold dosing and alarm escalation timing. \* **WHEN:** Sensor inputs
are near threshold values. \* **THEN:** Alarms are triggered correctly
and therapy delivery is within acceptable limits.

\### Fault Scenario 🔴 \* **GIVEN:** Therapy control system with sensor
spike/dropout and actuator command rejection path. \* **WHEN:** Sensor
inputs are faulty or missing. \* **THEN:** Alarms are triggered
correctly and therapy delivery is rejected.
