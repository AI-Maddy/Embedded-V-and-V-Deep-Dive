Pattern 6 — ⏱️  Rate Limiter & Actuator Saturation Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

First-order actuator dynamics — position limit, rate limit, and back-EMF / hydraulic
pressure saturation — which are critical for stability analysis and PIO
(Pilot-Induced Oscillation) assessment.

.. rubric:: Model Structure

.. code-block:: text

   Commanded_δ ──► [Rate Limiter] ──► [Position Clamp] ──► [1st-order lag] ──► Actual_δ
                   max: +δ̇_max            ± δ_max          τ = 1/(2π·f_act)
                   min: −δ̇_max

.. rubric:: Key Modeling Rules

- Rate limit and position limit values must be requirement parameters, **not** hard-coded.
- Include a ``SATURATED`` status output; the control law must detect saturation and
  invoke anti-windup logic.
- Verify actuator model fidelity against hardware datasheet or test rig data before
  using in flight-envelope simulation.
- At MIL phase: test command profiles that deliberately drive saturation to confirm
  anti-windup prevents integrator wind-up and position overshoot.

----

