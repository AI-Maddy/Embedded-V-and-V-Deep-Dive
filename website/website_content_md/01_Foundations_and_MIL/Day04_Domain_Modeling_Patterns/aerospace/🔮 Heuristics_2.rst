🔮 Heuristics
-------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| Mode transition fires unexpectedly            | Check guard condition for implicit priority  |
|                                               | or missing inhibit condition.                |
+-----------------------------------------------+----------------------------------------------+
| Gain table boundary test fails                | Verify break-point alignment and BNR         |
|                                               | quantisation; recheck ICD scaling formula.   |
+-----------------------------------------------+----------------------------------------------+
| Monitor asserts spuriously at startup         | Add ``INIT`` state to debounce first frame;  |
|                                               | document in Requirements.                    |
+-----------------------------------------------+----------------------------------------------+
| Coverage hole in protection logic             | Add explicit test for hysteresis band; check |
|                                               | both entry and exit conditions independently.|
+-----------------------------------------------+----------------------------------------------+
| Reconfiguration test flaky between runs       | Fix random seed; check for timing dependency |
|                                               | on host OS scheduler jitter.                 |
+-----------------------------------------------+----------------------------------------------+

----

