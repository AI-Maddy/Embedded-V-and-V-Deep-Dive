---
title: "MIL Execution Architecture"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 🏗️ MIL Execution Architecture

**How a Single MIL Run Flows**

``` text
┌──────────────────────────────────────────────────────────────────────────┐
│                AEROSPACE MIL EXECUTION PIPELINE                         │
│                                                                          │
│  ① SCENARIO LOAD                                                        │
│     scenario.json → {req_ids, stimuli, thresholds, seeds}                │
│                          │                                               │
│  ② ENVIRONMENT VALIDATION                                               │
│     ├── model hash  == CI baseline?  ✅                                  │
│     ├── param hash  == CI baseline?  ✅                                  │
│     ├── tool version == locked?      ✅                                  │
│     └── seed value  == deterministic? ✅                                 │
│                          │                                               │
│  ③ SIMULATION EXECUTION                                                 │
│     Simulink / SCADE ──► Plant (JSBSim / Aero Blockset)                  │
│     FCS controller  ◄──► Bus I/O (ARINC 429 stimulus)                   │
│     Duration: T_sim (scenario-defined, typ. 30–300 s)                    │
│                          │                                               │
│  ④ SIGNAL LOGGING                                                       │
│     ├── .mat / HDF5 raw log (every logged signal, full rate)            │
│     ├── Bus traces (ARINC 429 labels: value + SSM + age)                │
│     └── Mode-transition event log (state, time, trigger)                │
│                          │                                               │
│  ⑤ VERDICT ENGINE                                                       │
│     ├── Assert: |pitch_error_rms| < 0.5° ?                              │
│     ├── Assert: mode_transition count == expected ?                      │
│     ├── Assert: monitor_flag latency ≤ 100 ms ?                         │
│     └── [PASS | FAIL | INCONCLUSIVE]                                    │
│                          │                                               │
│  ⑥ EVIDENCE PACKAGING                                                   │
│     evidence/2026-03-07_run-042/                                        │
│       ├── scenario.json      (frozen input)                              │
│       ├── raw_log.mat        (full signal dump)                         │
│       ├── bus_trace.csv      (ARINC 429 decode)                          │
│       ├── verdict.json       (pass/fail + rationale)                     │
│       ├── coverage.html      (Simulink Coverage snapshot)               │
│       ├── env_manifest.json  (hashes + versions)                         │
│       └── traceability.csv   (req → scenario → verdict)                  │
└──────────────────────────────────────────────────────────────────────────┘
```

