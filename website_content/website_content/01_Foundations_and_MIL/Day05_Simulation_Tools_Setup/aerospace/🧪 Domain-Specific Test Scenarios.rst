🧪 Domain-Specific Test Scenarios
----------------------------------

.. rubric:: 🟢 Nominal Scenario

Stable flight-control mode tracking with expected atmospheric disturbances.
Controller must maintain commanded attitude within ±0.5° over a full manoeuvre cycle.

.. rubric:: 🟡 Boundary Scenario

High-workload transition envelope near stability margins (e.g. approach to stall
boundary with envelope-protection logic active).  Acceptance: protection engages
before exceedance, no oscillatory divergence.

.. rubric:: 🔴 Fault Scenario

ARINC 429 bus label corruption combined with an independent sensor disagreement
event.  Expected: cross-channel monitor flags mismatch within 100 ms; control law
reverts to secondary mode without loss of positive control.

----

