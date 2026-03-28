🛩️  System Under Verification
-------------------------------

.. code-block:: text

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                 PITCH-AXIS AUTOPILOT (SUV)                            │
   │                                                                       │
   │  θ_cmd ──►┌─────────────┐  δe_cmd  ┌──────────┐  δe   ┌──────────┐  │
   │  (pitch   │  Pitch-Axis │ ───────► │ Actuator │ ────► │ Aircraft │  │
   │   ref)    │  Controller │          │  Model   │       │  Plant   │  │
   │           └──────┬──────┘          └──────────┘       └────┬─────┘  │
   │                  │                                         │        │
   │           ┌──────┴──────┐                           ┌──────┴─────┐  │
   │           │  Mode Logic │  ◄─── pilot discrete ──── │  Sensors   │  │
   │           │  (ALTS/VS/  │       mode switch         │ (IMU/ADC/  │  │
   │           │   ATT/OVRD) │                           │  AHRS)     │  │
   │           └─────────────┘                           └────────────┘  │
   │                                                                       │
   │  Modes:  ATT (attitude hold)  │  VS (vertical speed)  │             │
   │          ALTS (altitude select) │ OVRD (manual override)│            │
   └─────────────────────────────────────────────────────────────────────────┘

----

