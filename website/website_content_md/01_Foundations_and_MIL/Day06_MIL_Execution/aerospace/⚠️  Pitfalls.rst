⚠️  Pitfalls
------------

.. caution::

   Subtle execution-time issues that pass internal review but fail DER inspection:

   - 🕳️  **Solver order mismatch** — ``ode4`` (4th-order RK) at MIL but ``ode1``
     (Euler) at SIL code-gen; dynamics differ enough to invalidate back-to-back
     comparison.  Lock solver choice across phases.
   - 🕳️  **Floating-point host dependency** — x86 FMA instructions may produce
     different rounding than the target processor.  Use ``-ffp-contract=off`` or
     equivalent during code-gen to match MIL behaviour.
   - 🕳️  **Signal aliasing** — logging at 200 Hz while the plant model has dynamics
     at > 100 Hz violates Nyquist; important high-frequency oscillations disappear.
   - 🕳️  **Clock-wall-time correlation** — MIL runs faster than real-time; if any
     sub-model uses ``clock()`` or ``tic/toc`` it will produce wrong timing evidence.
   - 🕳️  **Turbulence seed collision** — two scenarios with the same Dryden seed
     produce identical disturbance; coverage appears broader than it actually is.

----

