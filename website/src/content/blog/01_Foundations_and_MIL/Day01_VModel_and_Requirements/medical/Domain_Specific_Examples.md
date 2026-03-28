---
title: "Domain Specific Examples"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# Domain-Specific Examples 📊

**Nominal 🟢** GIVEN: A therapy control system with validated sensor
feedback WHEN: The system operates within expected ranges THEN: Therapy
is delivered as intended without deviation

**Boundary 🟡** GIVEN: Near-threshold dosing and alarm escalation timing
appropriately, and therapy remains safe

**Fault 🔴** GIVEN: Sensor spike/dropout and actuator command rejection
path WHEN: A fault occurs in the sensor or actuator THEN: The system
enters a safe state, halting therapy and issuing alerts
