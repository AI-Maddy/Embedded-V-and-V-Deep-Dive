🧪 Domain-Specific Test Scenarios
----------------------------------

.. rubric:: 🟢 Nominal Scenario

Stable Normal Law flight-control mode tracking with realistic atmospheric disturbances
(Dryden turbulence, fixed seed).  All ARINC 429 labels in range; SSM = NO.  Expected:
attitude error < ±0.5°, no mode transition, no monitor flag asserted.

.. rubric:: 🟡 Boundary Scenario

High-workload pitch manoeuvre pushing AOA to ``α_warn − 1°``.  Gain scheduling
transitions through two adjacent table break-points.  Expected: soft-zone protection
entry cue asserted, no hard-protection activation, no PIO tendency.

.. rubric:: 🔴 Fault Scenario

Simultaneous ARINC 429 label stale (ADC-1 timeout) and SSM = NCD on the redundant
channel.  Expected: cross-channel monitor asserts ``DISAGREE`` within 100 ms;
reconfiguration manager switches to ``DEGRADED_MODE``; ECAM alert generated;
control law falls back to Direct Law with crew alert.

----

