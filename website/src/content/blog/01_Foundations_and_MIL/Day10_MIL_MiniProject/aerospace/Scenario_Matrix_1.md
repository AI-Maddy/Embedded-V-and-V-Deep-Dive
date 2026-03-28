---
title: "Scenario Matrix"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  **SC-NOM-01**   🟢 Nominal 5° step command in ATT     PA-REQ-001,    RMS error,
                             mode, calm air, 30 s sim   002            settling time,
                                                                       overshoot

  **SC-NOM-02**   🟢 Nominal VS mode: 500 fpm climb     PA-REQ-001     VS tracking
                             command, cruise conditions                RMS,
                                                                       steady-state
                                                                       error

  **SC-BDY-01**   🟡         ATT → VS mode transition   PA-REQ-003     Transition
                  Boundary   at Mach 0.78 / FL350                      latency, max
                                                                       transient
                                                                       deviation

  **SC-BDY-02**   🟡         VS → ALTS capture at 35    PA-REQ-004     Altitude
                  Boundary   000 ft target                             capture error,
                                                                       time to ±50 ft

  **SC-BDY-03**   🟡         Large step (20°) driving   PA-REQ-005     Saturation
                  Boundary   elevator to saturation                    detection,
                             limit                                     crew-alert
                                                                       latency

  **SC-BDY-04**   🟡         Moderate turbulence        PA-REQ-010     RMS error under
                  Boundary   (MIL-F-8785C Cat B) in ATT                turbulence
                             mode                                      

  **SC-FLT-01**   🔴 Fault   IMU #1 freeze at t = 10 s  PA-REQ-006     Switchover
                             during ATT hold                           latency,
                                                                       transient
                                                                       deviation

  **SC-FLT-02**   🔴 Fault   ADC total loss at t = 8 s  PA-REQ-007     Reversion to
                             during ALTS mode                          ATT, crew alert
                                                                       latency

  **SC-FLT-03**   🔴 Fault   Elevator actuator jam at   PA-REQ-008     OVRD trigger
                             δe = +12° at t = 12 s                     latency, pitch
                                                                       divergence

  **SC-FLT-04**   🔴 Fault   ARINC 429 stale data (no   PA-REQ-009     Monitor trigger
                             label update for 80 ms)                   time, flag
                                                                       assertion

  **SC-MFT-01**   🔴🔴 Multi IMU failure + Cat B        PA-REQ-011     Max pitch
                             turbulence simultaneously                 deviation in 10
                                                                       s window

  **SC-TRC-01**   📋 Trace   All mode transitions       PA-REQ-012     Log
                             logged to ARINC 429 label                 completeness,
                             320                                       timestamp
                                                                       accuracy
