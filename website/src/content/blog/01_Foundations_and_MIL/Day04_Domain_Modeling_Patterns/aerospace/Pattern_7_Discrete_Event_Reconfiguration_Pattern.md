---
title: "Pattern 7   Discrete Event Reconfiguration Pattern"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# Pattern 7 --- 🔁 Discrete-Event Reconfiguration Pattern

**What It Models**

Automatic reconfiguration of sensor sources on fault detection --- for
example, switching from primary ADC to secondary ADC after a disagree
flag, or switching autopilot engagement from Lane 1 to Lane 2.

**Reconfiguration State Machine Skeleton**

``` text
┌──────────────────────────────────────────────────────────────┐
│            SOURCE SELECTION / RECONFIG MANAGER               │
│                                                              │
│  State: PRIMARY_ACTIVE                                       │
│    → Monitor: disagree_flag | data_stale | BIT_fail          │
│    → Transition: ──any flag──► SECONDARY_ACTIVE              │
│                                                              │
│  State: SECONDARY_ACTIVE                                     │
│    → Monitor: secondary_health                               │
│    → Transition: ──secondary_fail──► DEGRADED_MODE           │
│                                                              │
│  State: DEGRADED_MODE                                        │
│    → Alert crew (ECAM / CAS message)                         │
│    → Restrict flight envelope (speed / manoeuvre limits)     │
└──────────────────────────────────────────────────────────────┘
```

**⚠️ Critical Requirements**

-   Reconfiguration must be **monotonic** --- no spontaneous reversion
    to PRIMARY_ACTIVE without ground maintenance reset (prevents fault
    masking).
-   Latency from fault detection to source switch must satisfy FHA
    latency budget.
-   Reconfiguration event must be time-stamped and logged to the Flight
    Data Recorder bus (ARINC 717 or equivalent).

------------------------------------------------------------------------
