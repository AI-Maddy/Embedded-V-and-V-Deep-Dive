---
title: "Generated Code Structure"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 🗂️ Generated Code Structure

``` text
generated_code/
├── 📄 FCS_Pitch_Autopilot.c              ← main step function
├── 📄 FCS_Pitch_Autopilot.h              ← public interface
├── 📄 FCS_Pitch_Autopilot_private.h      ← internal types
├── 📄 FCS_Pitch_Autopilot_types.h        ← data type definitions
├── 📄 FCS_Pitch_Autopilot_data.c         ← calibration constants
├── 📄 rtwtypes.h                         ← Simulink base types
├── 📄 rt_nonfinite.c                     ← NaN/Inf guard (if any)
│
├── subsystems/
│   ├── 📄 PitchRateLimiter.c             ← rate-limiter subsystem
│   ├── 📄 ModeLogic.c                    ← mode state machine
│   ├── 📄 SensorVoting.c                 ← triplex sensor voter
│   ├── 📄 EnvelopeProtection.c           ← limit checking
│   └── 📄 ActuatorCommand.c              ← elevator servo output
│
├── integration/
│   ├── 📄 FCS_step.c                     ← 200 Hz cyclic entry point
│   ├── 📄 FCS_init.c                     ← power-on initialization
│   └── 📄 FCS_terminate.c                ← shutdown sequence
│
└── reports/
    ├── 📊 codegen_report.html            ← block ↔ code traceability
    ├── 📋 misra_report.html              ← MISRA C:2012 compliance
    └── 🔒 file_manifest.sha256           ← integrity hashes
```

