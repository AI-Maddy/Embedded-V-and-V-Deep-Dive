🧪 Fault Injection Scenario Matrix
------------------------------------

.. rubric:: 🔴 FI-SEN-01: IMU Gyro Stuck-At

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-401, SSA-H-005                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Sensor — gyro p-axis stuck at last value          |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 25 s (during 10°/s roll manoeuvre)            |
+--------------------------+---------------------------------------------------+
| 🔗 FMEA link             | FM-005-01                                         |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Cross-channel monitor detects disagreement within |
|                          | 80 ms; median voter rejects stuck channel;        |
|                          | roll tracking RMS < 1° after recovery             |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-SEN-02: ADC Alpha Bias Ramp

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-402, SSA-H-003                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Sensor — α measurement drifts +0.5°/s             |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 30 s (cruise, straight and level)             |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Envelope-protection monitor detects before α      |
|                          | exceeds α_max; mode transitions to ALT_LAW;      |
|                          | crew alert within 2 s of protection activation    |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-BUS-01: ARINC 429 Label Stale (ADC-1)

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-310, SSA-H-003                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Bus — ADC-1 altitude label stops transmitting      |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 20 s                                          |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Frame-age counter exceeds MAX_AGE within 100 ms;  |
|                          | validity flag → STALE; FCS uses ADC-2 data;       |
|                          | no transient > 0.5° pitch error                   |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-BUS-02: AFDX Virtual Link Frame Loss Burst

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-312, SSA-H-007                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Bus — 500 ms burst of AFDX VL frame loss          |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 35 s                                          |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | FCS holds last-valid-value for ≤ T_HOLD (200 ms); |
|                          | after T_HOLD, switches to degraded source;        |
|                          | no uncommanded surface movement                   |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-ACT-01: Elevator Actuator Jam

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-450, SSA-H-003                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Actuator — elevator jammed at +2°                 |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 25 s (approach, 3000 ft, flaps 30)            |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | FCS detects jam (cmd ≠ position for > 200 ms);    |
|                          | standby actuator engaged within 500 ms;           |
|                          | pitch tracking restored < 1° error                |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-ACT-02: Aileron Runaway

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-452, SSA-H-004                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Actuator — left aileron drives to hard-stop at    |
|                          | maximum rate                                      |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 15 s (cruise, wings level)                    |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Rate monitor detects runaway within 50 ms;        |
|                          | hydraulic shutoff commanded; opposite aileron +   |
|                          | spoiler compensate; bank angle excursion < 10°    |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-ENV-01: Windshear During Approach

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-501, SSA-H-009                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Environment — 30-kt microburst windshear at       |
|                          | 200 ft AGL                                        |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | When alt_AGL crosses 200 ft during approach       |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Windshear warning generated within 3 s;           |
|                          | auto-throttle advances to TOGA; flight path       |
|                          | recovers to positive climb gradient within 8 s    |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-MULTI-01: FTA Cut Set — Dual ADC + Actuator Jam

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-310 + FCS-REQ-450, SSA-H-003 (cut set)   |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Combinatorial — ADC-1 stale (T=30s), ADC-2 NCD   |
|                          | (T=32s), elevator jam (T=40s)                     |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Each fault detected independently; final state:   |
|                          | DIRECT_LAW + standby actuator + crew alert;       |
|                          | positive control maintained throughout;           |
|                          | all transitions within FHA latency budgets        |
+--------------------------+---------------------------------------------------+

----

