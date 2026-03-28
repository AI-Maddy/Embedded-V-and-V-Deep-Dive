---
title: "Closed Loop Architecture"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🏗️ Closed-Loop Architecture

``` text
┌────────────────────────────────────────────────────────────────────────────┐
│            AEROSPACE CLOSED-LOOP MIL ARCHITECTURE                         │
│                                                                            │
│   ┌───────────────────┐     δ_cmd      ┌──────────────────┐               │
│   │  FCS Controller   │──────────────►  │  Actuator Model  │               │
│   │  (Simulink/SCADE) │                 │  (rate + pos     │               │
│   │                   │  ◄──────────    │   limits + lag)  │               │
│   │  • Normal Law     │  ARINC 429     └────────┬─────────┘               │
│   │  • Alternate Law  │  sensor bus              │ δ_actual                │
│   │  • Direct Law     │                          ▼                         │
│   │  • Envelope Prot. │              ┌──────────────────────┐              │
│   │  • Monitors       │              │   Plant / FDM Model  │              │
│   └───────┬───────────┘              │   (JSBSim / Aero     │              │
│           │                          │    Blockset 6-DOF)   │              │
│           │ pilot_cmd                │                      │              │
│           │                          │  • Aerodynamics      │              │
│   ┌───────┴───────────┐              │  • Engine thrust     │              │
│   │  Pilot / Autopilot│              │  • Atmosphere (ISA)  │              │
│   │  Command Source   │              │  • Turbulence        │              │
│   └──────────────────┘              │  • Gravity / inertia │              │
│                                      └────────┬─────────────┘              │
│                                               │ state vector              │
│                                               │ (α, β, p, q, r,           │
│                                               │  φ, θ, ψ, V, h)          │
│                                               ▼                           │
│                                    ┌──────────────────────┐               │
│                                    │   Sensor Models      │               │
│                                    │   • IMU (gyro + acc) │               │
│                                    │   • ADC (α, Mach, Q) │               │
│                                    │   • GPS              │               │
│                                    │   • Noise + bias     │               │
│                                    └────────┬─────────────┘               │
│                                             │ measured states              │
│                                             ▼                             │
│                                  ┌────────────────────────┐               │
│                                  │  ARINC 429 / AFDX Bus  │               │
│                                  │  • BNR encoding        │               │
│                                  │  • SSM status          │               │
│                                  │  • Label scheduling    │               │
│                                  │  • Frame age tracking  │               │
│                                  └────────────┬───────────┘               │
│                                               │                           │
│                              feedback to FCS ─┘                           │
└────────────────────────────────────────────────────────────────────────────┘
```

------------------------------------------------------------------------
