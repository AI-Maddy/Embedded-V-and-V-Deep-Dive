---
title: "Domain Specific Examples  2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# Domain-Specific Examples 🩺

**Nominal Scenario 🟢** GIVEN: Therapy control system with validated
sensor feedback WHEN: Sensor provides expected readings within
calibrated range THEN: Therapy proceeds as intended, maintaining patient
safety

**Boundary Scenario 🟡** GIVEN: Near-threshold dosing and alarm
escalation timing WHEN: Sensor readings approach critical thresholds
THEN: Alarm escalates appropriately, ensuring timely intervention

**Fault Scenario 🔴** GIVEN: Sensor spike/dropout or actuator command
rejection WHEN: System encounters unexpected input or fails to execute
commands THEN: Therapy halts safely, and error is logged for
investigation
