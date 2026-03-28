# 🏗️ Fault Injection Framework Architecture

``` text
┌──────────────────────────────────────────────────────────────────────────┐
│          AEROSPACE MIL FAULT INJECTION FRAMEWORK                        │
│                                                                          │
│  ┌──────────────────┐     ┌──────────────────────────────┐              │
│  │ Fault Scenario   │     │  FMEA / FTA                   │              │
│  │ Definition       │◄────│  Traceability Database        │              │
│  │ (JSON)           │     │  (H-xxx → FM-xxx → FI-xxx)    │              │
│  └────────┬─────────┘     └──────────────────────────────┘              │
│           │                                                              │
│           ▼                                                              │
│  ┌──────────────────────────────────────────────────┐                    │
│  │         FAULT INJECTION CONTROLLER               │                    │
│  │                                                  │                    │
│  │  for each fault in scenario:                     │                    │
│  │    if trigger_condition(t, state):                │                    │
│  │      activate_fault(target, type, params)        │                    │
│  │      log_injection_event(t, fault_id)            │                    │
│  └────────┬──────────────┬──────────────┬───────────┘                    │
│           │              │              │                                │
│           ▼              ▼              ▼                                │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐                         │
│  │ Sensor     │  │ Bus I/O    │  │ Actuator   │                         │
│  │ Models     │  │ Models     │  │ Models     │                         │
│  └──────┬─────┘  └──────┬─────┘  └──────┬─────┘                         │
│         └───────────────┼───────────────┘                                │
│                         ▼                                                │
│  ┌──────────────────────────────────────────────────┐                    │
│  │         FCS CONTROLLER (closed-loop)             │                    │
│  │           ↕ monitors + FDIR logic                │                    │
│  └────────┬─────────────────────────────────────────┘                    │
│           │                                                              │
│           ▼                                                              │
│  ┌──────────────────────────────────────────────────┐                    │
│  │         VERDICT ENGINE                           │                    │
│  │  • Detection latency vs. FHA budget              │                    │
│  │  • Correct mode transition?                      │                    │
│  │  • Safe state reached?                           │                    │
│  │  • Recovery within spec?                         │                    │
│  └────────┬─────────────────────────────────────────┘                    │
│           │                                                              │
│           ▼                                                              │
│  ┌──────────────────────────────────────────────────┐                    │
│  │         EVIDENCE PACKAGE                         │                    │
│  │  raw_log.mat · fault_event_log.csv ·             │                    │
│  │  verdict.json · traceability.csv                 │                    │
│  └──────────────────────────────────────────────────┘                    │
└──────────────────────────────────────────────────────────────────────────┘
```

------------------------------------------------------------------------
