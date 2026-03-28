🔮 Heuristics
-------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| Run completes but verdict is INCONCLUSIVE     | Check signal logging rate — aliasing may hide|
|                                               | the event.  Re-run at 2× sample rate.        |
+-----------------------------------------------+----------------------------------------------+
| Two identical scenarios yield different logs   | Verify seed, solver, and host.  Check for non|
|                                               | -deterministic block (e.g. ``clock()``)      |
+-----------------------------------------------+----------------------------------------------+
| Coverage gap in protection logic              | Add explicit scenario for hysteresis entry    |
|                                               | and exit; verify both independently.         |
+-----------------------------------------------+----------------------------------------------+
| Batch run takes > 4 hours                     | Profile per-scenario time; split long runs;  |
|                                               | use ``parsim()`` with 4–8 workers.           |
+-----------------------------------------------+----------------------------------------------+
| DER asks for raw log but file is 2 GB         | Provide HDF5 with signal index; include a    |
|                                               | viewer script that extracts requested signals.|
+-----------------------------------------------+----------------------------------------------+

----

