---
title: "Heuristics 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🔮 Heuristics

+----------------------------------+---------------------------------+---+
| Situation                        | 💡 Action                       |   |
+==================================+=================================+===+
| Run completes but verdict is     | Check signal logging rate ---   |   |
| INCONCLUSIVE                     | aliasing may hide the event.    |   |
|                                  | Re-run at 2× sample rate.       |   |
+----------------------------------+---------------------------------+---+
| Two identical scenarios yiel     |                                 |   |
| d different logs \| Verify seed, |                                 |   |
|  solver, and host. Check for non |                                 |   |
|                                  |                                 |   |
| :   | -deterministic block (e.g. |                                 |   |
|       `clock()`) \|              |                                 |   |
+----------------------------------+---------------------------------+---+
| Coverage gap in protection logic | Add explicit scenario for       |   |
|                                  | hysteresis entry and exit;      |   |
|                                  | verify both independently. \|   |   |
+----------------------------------+---------------------------------+---+
| Batch run takes \> 4 hours       | Profile per-scenario time;      |   |
|                                  | split long runs; use `parsim()` |   |
|                                  | with 4--8 workers.              |   |
+----------------------------------+---------------------------------+---+
| DER asks for raw log but file is | Provide HDF5 with signal index; |   |
| 2 GB                             | include a \| viewer script that |   |
|                                  | extracts requested signals.     |   |
+----------------------------------+---------------------------------+---+

------------------------------------------------------------------------
