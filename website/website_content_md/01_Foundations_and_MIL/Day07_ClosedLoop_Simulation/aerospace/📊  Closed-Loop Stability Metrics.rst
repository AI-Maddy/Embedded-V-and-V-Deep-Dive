📊  Closed-Loop Stability Metrics
-----------------------------------

.. tip::
   💡 These are the **key metrics** that distinguish closed-loop verification from
   open-loop.  Every closed-loop run must report these.

.. list-table::
   :widths: 5 25 40 30
   :header-rows: 1

   * - #
     - Metric
     - What It Tells You
     - Pass Criteria (typical)
   * - 1
     - 📉 **Gain Margin (GM)**
     - How much gain increase the loop tolerates before instability
     - GM ≥ 6 dB (ARP4754A typical)
   * - 2
     - 📐 **Phase Margin (PM)**
     - How much phase lag the loop tolerates before instability
     - PM ≥ 45° (ARP4754A typical)
   * - 3
     - ⏱️  **Settling Time (T_s)**
     - Time to reach and stay within ±2 % of commanded value
     - T_s ≤ 2 s (pitch); ≤ 1.5 s (roll)
   * - 4
     - 📈 **Overshoot (%OS)**
     - Peak transient exceedance above commanded value
     - %OS ≤ 15 % (normal law)
   * - 5
     - 🔄 **Steady-State Error (e_ss)**
     - Residual error after transient decays
     - e_ss < 0.1° (attitude); < 0.5 kt (speed)
   * - 6
     - 🌀 **PIO Susceptibility Index**
     - Pilot-Induced Oscillation tendency (Neal-Smith, bandwidth)
     - Category I (no PIO tendency)
   * - 7
     - 🔒 **Limit-Cycle Amplitude**
     - Sustained oscillation amplitude (if any)
     - Zero (no limit cycle permitted)
   * - 8
     - 🛡️  **Monitor Detection Latency**
     - Time from injected fault to monitor flag assertion
     - ≤ 100 ms (per FHA latency budget)

----

