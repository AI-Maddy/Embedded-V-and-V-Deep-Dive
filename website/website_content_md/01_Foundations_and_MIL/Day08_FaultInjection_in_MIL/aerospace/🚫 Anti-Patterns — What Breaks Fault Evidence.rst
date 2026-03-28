🚫 Anti-Patterns — What Breaks Fault Evidence
-----------------------------------------------

.. danger::
   ❌ These lead to DER rejection of the entire fault injection campaign:

- 🚩 Injecting faults as a **boolean error flag** instead of at the physical signal level —
  skips the realistic detection chain.
- 🚩 Testing only **single faults** when the FTA shows dual/triple cut sets as
  contributing to CATASTROPHIC hazards.
- 🚩 Fault injection scenarios that **cannot be re-run deterministically** — random
  injection timing without a fixed seed invalidates regression.
- 🚩 Pass/fail verdict based on "the system didn't crash" — must have **quantitative**
  detection latency + safe-state metrics.
- 🚩 No baseline (fault-free) comparison run — can't distinguish fault effects from
  nominal dynamics.
- 🚩 FMEA items not traced to injection scenarios — the safety argument has a gap.

----

