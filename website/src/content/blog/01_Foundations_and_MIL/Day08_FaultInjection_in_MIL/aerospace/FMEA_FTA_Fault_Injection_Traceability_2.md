---
title: "FMEA   FTA  Fault Injection Traceability 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🔗 FMEA / FTA → Fault Injection Traceability

::: warning
::: title
Warning
:::

⚠️ DO-178C and ARP4761 require **explicit traceability** from every
identified failure mode to at least one verification activity. Fault
injection at MIL is that activity for most FMEA items.
:::

``` text
┌──────────────────────────────────────────────────────────────────────────┐
│         SAFETY ASSESSMENT  →  FAULT INJECTION  →  EVIDENCE             │
│                                                                         │
│  ARP4761 FHA                                                            │
│    └── Hazard H-003: "Loss of pitch control authority"                  │
│          Severity: CATASTROPHIC                                         │
│                                                                         │
│  ARP4761 FMEA                                                           │
│    └── FM-003-01: "Elevator actuator jam"                               │
│    └── FM-003-02: "Dual ADC failure (stale + NCD)"                      │
│    └── FM-003-03: "IMU gyro runaway"                                    │
│                                                                         │
│  ARP4761 FTA                                                            │
│    └── Cut set: FM-003-01 AND power-loss-to-standby-actuator            │
│                                                                         │
│  MIL Fault Injection                                                    │
│    └── FI-003-01: inject elevator jam → verify standby switchover       │
│    └── FI-003-02: inject dual ADC fail → verify DEGRADED_MODE entry     │
│    └── FI-003-03: inject gyro runaway → verify median voter rejects     │
│    └── FI-003-04: inject cut set → verify crew alert + safe state       │
│                                                                         │
│  Evidence Package                                                       │
│    └── verdict.json: FI-003-01 → PASS (latency 87 ms < 100 ms budget)  │
│    └── traceability.csv: H-003 → FM-003-01 → FI-003-01 → PASS          │
└──────────────────────────────────────────────────────────────────────────┘
```

------------------------------------------------------------------------
