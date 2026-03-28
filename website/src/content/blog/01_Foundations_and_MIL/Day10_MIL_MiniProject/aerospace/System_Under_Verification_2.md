---
title: "System Under Verification 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🛩️ System Under Verification

``` text
┌─────────────────────────────────────────────────────────────────────────┐
│                 PITCH-AXIS AUTOPILOT (SUV)                            │
│                                                                       │
│  θ_cmd ──►┌─────────────┐  δe_cmd  ┌──────────┐  δe   ┌──────────┐  │
│  (pitch   │  Pitch-Axis │ ───────► │ Actuator │ ────► │ Aircraft │  │
│   ref)    │  Controller │          │  Model   │       │  Plant   │  │
│           └──────┬──────┘          └──────────┘       └────┬─────┘  │
│                  │                                         │        │
│           ┌──────┴──────┐                           ┌──────┴─────┐  │
│           │  Mode Logic │  ◄─── pilot discrete ──── │  Sensors   │  │
│           │  (ALTS/VS/  │       mode switch         │ (IMU/ADC/  │  │
│           │   ATT/OVRD) │                           │  AHRS)     │  │
│           └─────────────┘                           └────────────┘  │
│                                                                       │
│  Modes:  ATT (attitude hold)  │  VS (vertical speed)  │             │
│          ALTS (altitude select) │ OVRD (manual override)│            │
└─────────────────────────────────────────────────────────────────────────┘
```

------------------------------------------------------------------------
