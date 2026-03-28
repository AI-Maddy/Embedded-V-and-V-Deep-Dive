🗺️  Scenario Matrix
---------------------

.. list-table::
   :widths: 12 12 38 18 20
   :header-rows: 1

   * - Scenario ID
     - Type
     - Description
     - Requirements
     - Key Metrics
   * - **SC-NOM-01**
     - 🟢 Nominal
     - 5° step command in ATT mode, calm air, 30 s sim
     - PA-REQ-001, 002
     - RMS error, settling time, overshoot
   * - **SC-NOM-02**
     - 🟢 Nominal
     - VS mode: 500 fpm climb command, cruise conditions
     - PA-REQ-001
     - VS tracking RMS, steady-state error
   * - **SC-BDY-01**
     - 🟡 Boundary
     - ATT → VS mode transition at Mach 0.78 / FL350
     - PA-REQ-003
     - Transition latency, max transient deviation
   * - **SC-BDY-02**
     - 🟡 Boundary
     - VS → ALTS capture at 35 000 ft target
     - PA-REQ-004
     - Altitude capture error, time to ±50 ft
   * - **SC-BDY-03**
     - 🟡 Boundary
     - Large step (20°) driving elevator to saturation limit
     - PA-REQ-005
     - Saturation detection, crew-alert latency
   * - **SC-BDY-04**
     - 🟡 Boundary
     - Moderate turbulence (MIL-F-8785C Cat B) in ATT mode
     - PA-REQ-010
     - RMS error under turbulence
   * - **SC-FLT-01**
     - 🔴 Fault
     - IMU #1 freeze at t = 10 s during ATT hold
     - PA-REQ-006
     - Switchover latency, transient deviation
   * - **SC-FLT-02**
     - 🔴 Fault
     - ADC total loss at t = 8 s during ALTS mode
     - PA-REQ-007
     - Reversion to ATT, crew alert latency
   * - **SC-FLT-03**
     - 🔴 Fault
     - Elevator actuator jam at δe = +12° at t = 12 s
     - PA-REQ-008
     - OVRD trigger latency, pitch divergence
   * - **SC-FLT-04**
     - 🔴 Fault
     - ARINC 429 stale data (no label update for 80 ms)
     - PA-REQ-009
     - Monitor trigger time, flag assertion
   * - **SC-MFT-01**
     - 🔴🔴 Multi
     - IMU failure + Cat B turbulence simultaneously
     - PA-REQ-011
     - Max pitch deviation in 10 s window
   * - **SC-TRC-01**
     - 📋 Trace
     - All mode transitions logged to ARINC 429 label 320
     - PA-REQ-012
     - Log completeness, timestamp accuracy

----

