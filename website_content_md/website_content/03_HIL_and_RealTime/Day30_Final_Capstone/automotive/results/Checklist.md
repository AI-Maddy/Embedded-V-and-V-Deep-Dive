# Checklist

☐ Domain hazard coverage is explicit. ☐ Compliance references are mapped
to evidence. ☐ Nominal/boundary/fault results are all documented. ☐
Residual risks and next actions are assigned.

GIVEN / WHEN / THEN Scenario Templates
=====================================

\### Nominal 🟢 .. given:: Normal traffic conditions. .. when:: Adaptive
cruise and speed regulation are enabled. .. then:: The vehicle maintains
a safe distance and speed.

\### Boundary 🟡 .. given:: Dense stop-and-go traffic conditions. ..
when:: Tight headway and timing limits are applied. .. then:: The
vehicle maintains a safe distance and speed under stress.

\### Fault 🔴 .. given:: Sensor dropout and invalid CAN frame injection.
.. when:: The vehicle\'s adaptive cruise and speed regulation are
enabled. .. then:: The vehicle\'s safety features are triggered to
prevent accidents.
