🔮 Heuristics
-------------

+---------------------------------------------+----------------------------------------------+
| Situation                                   | 💡 Action                                    |
+=============================================+==============================================+
| A domain hazard has no linked test case     | Confidence is **provisional** — block sign-off|
+---------------------------------------------+----------------------------------------------+
| Re-run produces unexpected difference       | Investigate **determinism** before re-testing |
+---------------------------------------------+----------------------------------------------+
| Evidence is indirect or inferred            | **Reduce** verdict confidence level; document |
+---------------------------------------------+----------------------------------------------+
| Coverage metric is near threshold           | Add targeted tests; do **not** widen threshold|
+---------------------------------------------+----------------------------------------------+
| Schedule pressure to skip fault scenarios   | Escalate — fault scenarios are **non-optional**|
+---------------------------------------------+----------------------------------------------+

----

