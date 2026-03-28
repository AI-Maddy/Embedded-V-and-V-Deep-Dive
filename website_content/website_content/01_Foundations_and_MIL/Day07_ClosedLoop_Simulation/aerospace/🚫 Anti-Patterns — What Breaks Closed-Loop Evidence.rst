🚫 Anti-Patterns — What Breaks Closed-Loop Evidence
-----------------------------------------------------

.. danger::
   ❌ Closed-loop adds new failure modes beyond open-loop anti-patterns:

- 🚩 Closing the loop around a **simplified plant** that omits actuator dynamics —
  stability margins will look better than reality; DER will reject.
- 🚩 Logging only the **command** and **response** without the intermediate feedback
  signals (sensor output, bus-decoded value, monitor states) — root-cause analysis
  becomes impossible when a failure occurs.
- 🚩 Using a **variable-step solver** for the plant while the controller runs fixed-step —
  introduces non-deterministic phase shift that corrupts margin measurements.
- 🚩 Testing only one axis at a time — cross-coupling bugs are invisible in
  single-axis closed-loop runs.
- 🚩 Skipping PIO assessment — "the pilot will adapt" is **not** an acceptable
  argument under MIL-STD-1797A / DO-178C.

----

