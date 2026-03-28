🔄  What Makes Closed-Loop Different from Open-Loop?
------------------------------------------------------

.. list-table::
   :widths: 5 45 50
   :header-rows: 1

   * - 
     - 🔓 Open-Loop (Day 06)
     - 🔒 Closed-Loop (Day 07)
   * - 🏗️
     - Controller receives **pre-recorded** stimuli
     - Controller receives **live plant feedback**
   * - 🔁
     - No feedback path; response is one-shot
     - Full feedback: command → actuator → plant → sensor → bus → command
   * - 🧪
     - Tests individual I/O mappings
     - Tests **emergent system behaviour** (stability, oscillation, coupling)
   * - ⚠️
     - Cannot detect PIO, limit-cycle, or feedback instability
     - **Can** detect PIO, limit-cycling, gain-margin violations
   * - 📊
     - Pass/fail: "does signal X match expected value?"
     - Pass/fail: "does the **system** remain stable, converge, and track?"

----

