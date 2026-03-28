📋 Requirements Baseline
--------------------------

The mini-project uses 12 requirements derived from a simplified pitch-axis
autopilot specification.  Each requirement has a hazard linkage and DAL.

.. list-table::
   :widths: 15 45 20 10 10
   :header-rows: 1

   * - Req ID
     - Description
     - Hazard Linkage
     - DAL
     - Category
   * - **PA-REQ-001**
     - Pitch-axis controller shall track θ_cmd within ±0.5° RMS in steady
       flight (ATT mode).
     - H-001: loss of pitch control
     - A
     - Nominal
   * - **PA-REQ-002**
     - Settling time for a 5° step command shall be ≤ 3.0 s with ≤ 10 %
       overshoot.
     - H-001
     - A
     - Nominal
   * - **PA-REQ-003**
     - Mode transition ATT → VS shall complete within 200 ms with no
       transient > 2° deviation.
     - H-002: unstable mode change
     - A
     - Boundary
   * - **PA-REQ-004**
     - Mode transition VS → ALTS shall track altitude reference within
       ±50 ft within 15 s.
     - H-002
     - B
     - Boundary
   * - **PA-REQ-005**
     - Pitch-axis controller shall saturate elevator command at ±25° and
       produce a crew alert within 500 ms.
     - H-003: surface over-deflection
     - A
     - Boundary
   * - **PA-REQ-006**
     - Upon single IMU failure, the controller shall switch to backup IMU
       within 100 ms and maintain ≤ 1° transient.
     - H-004: sensor failure
     - A
     - Fault
   * - **PA-REQ-007**
     - Upon ADC loss, controller shall revert to ATT hold using last valid
       altitude; crew alert within 200 ms.
     - H-005: air-data failure
     - A
     - Fault
   * - **PA-REQ-008**
     - Elevator actuator jam at current position shall trigger OVRD mode
       within 300 ms.
     - H-006: actuator failure
     - A
     - Fault
   * - **PA-REQ-009**
     - ARINC 429 label stale-data (no update > 50 ms) shall trigger
       sensor-disagreement monitor.
     - H-007: bus data loss
     - A
     - Fault
   * - **PA-REQ-010**
     - In moderate turbulence (MIL-F-8785C Cat B), tracking error shall
       remain ≤ 1.5° RMS.
     - H-001
     - B
     - Boundary
   * - **PA-REQ-011**
     - Simultaneous IMU failure + turbulence shall not cause pitch
       divergence > 5° within 10 s.
     - H-004 + H-001
     - A
     - Multi-fault
   * - **PA-REQ-012**
     - All mode transitions shall be logged with timestamps and mode IDs
       on the bus (ARINC 429 label 320).
     - Audit requirement
     - C
     - Traceability

----

