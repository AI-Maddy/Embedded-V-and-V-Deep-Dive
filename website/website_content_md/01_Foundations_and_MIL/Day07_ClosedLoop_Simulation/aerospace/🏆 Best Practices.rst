🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🔗
     - Record **GM and PM** as first-class verdict fields alongside functional pass/fail.
   * - 🧮
     - Automate ``margin()`` extraction as a post-run step — never rely on manual Bode plot readings.
   * - 🌡️
     - Sweep environmental conditions (altitude, Mach, CG, weight) across the flight
       envelope; plot stability margins as a carpet plot for the full envelope.
   * - 📐
     - Validate plant model fidelity before closing the loop: compare open-loop plant
       response with known aerodynamic data (wind-tunnel or flight-test).
   * - 🔒
     - Include a **trim-state hash** in the environment manifest — if trim changes,
       all downstream closed-loop verdicts must be re-evaluated.
   * - 📦
     - Store linearised system objects (``ss``, ``tf``) in the evidence package alongside
       time-domain logs — reviewers need frequency-domain data for margin verification.

----

