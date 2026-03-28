🧪 Closed-Loop Test Scenario Matrix
-------------------------------------

.. rubric:: 🟢 CL-NOM-01: Pitch Doublet — Calm Air

.. code-block:: text

   Configuration:  NORMAL_LAW · Cruise (M 0.78, FL350)
   Command:        ±3° pitch doublet at T = 10 s, 25 s, 40 s
   Turbulence:     None
   Duration:       60 s
   ✅ Accept:       T_s < 2 s · %OS < 10 % · e_ss < 0.1° · no mode change

.. rubric:: 🟢 CL-NOM-02: Roll Step — Moderate Turbulence

.. code-block:: text

   Configuration:  NORMAL_LAW · Approach (M 0.22, 3 000 ft, flaps 30)
   Command:        25° bank-angle command at T = 15 s
   Turbulence:     Dryden moderate (σ_w = 3 m/s), seed #42
   Duration:       45 s
   ✅ Accept:       T_s < 1.5 s · %OS < 15 % · no PIO tendency · wings-level recovery < 3 s

.. rubric:: 🟡 CL-BDY-01: Envelope Excursion Near Stall

.. code-block:: text

   Configuration:  NORMAL_LAW → ENVELOPE_PROTECTION active
   Command:        Slow deceleration V → V_stall + 3 kt over 60 s
   Turbulence:     Dryden light, seed #42
   Duration:       120 s
   ✅ Accept:       Protection soft-cue activates at α_warn
                   Protection hard-override activates at α_max
                   No oscillation in protection engagement (hysteresis check)
                   Recovery after speed increase: protection deactivates within 3 s

.. rubric:: 🟡 CL-BDY-02: Gain-Schedule Cross-Over at High Q

.. code-block:: text

   Configuration:  NORMAL_LAW · Dive recovery (M 0.85 → M 0.6 at FL200)
   Command:        Pull-up command: 2.5 g load factor step
   Turbulence:     None
   Duration:       30 s
   ✅ Accept:       Gain table transitions smoothly (no > 2 % discontinuity)
                   Nz overshoot < 0.3 g · settling < 2 s · actuator stays within limits

.. rubric:: 🔴 CL-FLT-01: ADC Failure — Source Reconfiguration Under Load

.. code-block:: text

   Configuration:  NORMAL_LAW · Cruise (M 0.78, FL350) tracking heading 270°
   Fault:          T = 30 s: ADC-1 ARINC 429 SSM → NCD
                   T = 32 s: ADC-2 frame-age counter exceeds MAX_AGE
   Turbulence:     Dryden light, seed #42
   Duration:       90 s
   ✅ Accept:       Monitor DISAGREE flag within 100 ms of first fault
                   Reconfig to DEGRADED_MODE within 200 ms
                   ECAM CAS message generated
                   Transition to DIRECT_LAW — attitude maintained within ±5°
                   No transient > 1 g Nz during switchover

.. rubric:: 🔴 CL-FLT-02: Actuator Jam — Closed-Loop Recoverability

.. code-block:: text

   Configuration:  NORMAL_LAW · Approach (M 0.22, 3 000 ft)
   Fault:          T = 20 s: elevator actuator jammed at current position
   Turbulence:     Dryden moderate, seed #42
   Duration:       60 s
   ✅ Accept:       FCS detects jam (actuator position ≠ command for > 200 ms)
                   Switches to standby actuator within 500 ms
                   Pitch authority restored — tracking error < 1° after recovery
                   No divergent oscillation during switchover

.. rubric:: 🔴 CL-FLT-03: Double Sensor Disagree + Turbulence Gust

.. code-block:: text

   Configuration:  NORMAL_LAW · Cruise, heading hold
   Fault:          T = 40 s: IMU-1 gyro bias ramp (+2°/s over 5 s)
                   T = 42 s: ADC-1 α measurement frozen (stale)
   Turbulence:     Dryden severe (σ_w = 6 m/s), seed #99
   Duration:       120 s
   ✅ Accept:       Cross-channel monitor detects divergence within 150 ms
                   Median voter selects healthy channel
                   Attitude maintained within ±5° during transient
                   No unrecoverable divergence

----

