🔀  Model → Code Traceability
-------------------------------

.. code-block:: text

   ┌──────────────────────────────────────────────────────────────────────────┐
   │                    TRACEABILITY CHAIN                                    │
   │                                                                          │
   │  Requirement        Simulink Block          Generated C Code              │
   │  ─────────────      ──────────────          ────────────────              │
   │                                                                          │
   │  PA-REQ-001   ──►   PID_Pitch/Sum1    ──►   FCS_Pitch_Autopilot.c:142   │
   │  (pitch track)      PID_Pitch/Gain1          rtb_Sum1 = ...              │
   │                                                                          │
   │  PA-REQ-003   ──►   ModeLogic/         ──►   ModeLogic.c:87             │
   │  (mode trans)       Stateflow Chart          switch(mode_state) { ...    │
   │                                                                          │
   │  PA-REQ-005   ──►   EnvProtect/        ──►   EnvelopeProtection.c:54    │
   │  (saturation)       Saturation Block         if (cmd > 25.0f) cmd=25.0f; │
   │                                                                          │
   │  PA-REQ-006   ──►   SensorVoting/      ──►   SensorVoting.c:31          │
   │  (IMU switch)       Voter Logic              median_select(imu, 3);      │
   │                                                                          │
   └──────────────────────────────────────────────────────────────────────────┘

   Evidence artifact:  codegen_report.html  →  every block ↔ line mapping
   Anchored to:        Git commit hash + model SHA-256

----

