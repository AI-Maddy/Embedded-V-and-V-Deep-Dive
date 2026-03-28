---
title: "Closed Loop Test Scenario Matrix"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 🧪 Closed-Loop Test Scenario Matrix

**🟢 CL-NOM-01: Pitch Doublet --- Calm Air**

``` text
✅ Accept:       T_s < 2 s · %OS < 10 % · e_ss < 0.1° · no mode change
```

**🟢 CL-NOM-02: Roll Step --- Moderate Turbulence**

``` text
✅ Accept:       T_s < 1.5 s · %OS < 15 % · no PIO tendency · wings-level recovery < 3 s
```

**🟡 CL-BDY-01: Envelope Excursion Near Stall**

``` text
✅ Accept:       Protection soft-cue activates at α_warn
                Protection hard-override activates at α_max
                No oscillation in protection engagement (hysteresis check)
                Recovery after speed increase: protection deactivates within 3 s
```

**🟡 CL-BDY-02: Gain-Schedule Cross-Over at High Q**

``` text
✅ Accept:       Gain table transitions smoothly (no > 2 % discontinuity)
                Nz overshoot < 0.3 g · settling < 2 s · actuator stays within limits
```

**🔴 CL-FLT-01: ADC Failure --- Source Reconfiguration Under Load**

``` text
                T = 32 s: ADC-2 frame-age counter exceeds MAX_AGE
✅ Accept:       Monitor DISAGREE flag within 100 ms of first fault
                Reconfig to DEGRADED_MODE within 200 ms
                ECAM CAS message generated
                Transition to DIRECT_LAW — attitude maintained within ±5°
                No transient > 1 g Nz during switchover
```

**🔴 CL-FLT-02: Actuator Jam --- Closed-Loop Recoverability**

``` text
✅ Accept:       FCS detects jam (actuator position ≠ command for > 200 ms)
                Switches to standby actuator within 500 ms
                Pitch authority restored — tracking error < 1° after recovery
                No divergent oscillation during switchover
```

**🔴 CL-FLT-03: Double Sensor Disagree + Turbulence Gust**

``` text
                T = 42 s: ADC-1 α measurement frozen (stale)
✅ Accept:       Cross-channel monitor detects divergence within 150 ms
                Median voter selects healthy channel
                Attitude maintained within ±5° during transient
                No unrecoverable divergence
```

