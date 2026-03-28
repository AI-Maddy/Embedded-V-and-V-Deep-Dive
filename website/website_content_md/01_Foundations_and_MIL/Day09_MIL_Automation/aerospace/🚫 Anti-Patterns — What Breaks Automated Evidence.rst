🚫 Anti-Patterns — What Breaks Automated Evidence
----------------------------------------------------

.. danger::
   ❌ These automation mistakes have caused entire MIL campaigns to be rejected:

- 🚩 Automation scripts **not under version control** — DER cannot verify what ran.
- 🚩 Manual copy-paste of results into a report — breaks traceability chain.
- 🚩 ``parsim()`` workers sharing workspace variables — introduces race conditions.
- 🚩 Deleting or overwriting old evidence folders — evidence tampering risk.
- 🚩 CI pipeline with no timeout — a hung Simulink session blocks for hours with no alert.
- 🚩 Verdict engine reading the **wrong** raw log (path mismatch) — pass/fail is wrong.
- 🚩 Scripts using ``datetime.now()`` as a seed — non-deterministic injection timing.

----

