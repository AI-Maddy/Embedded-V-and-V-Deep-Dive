# 🔮 Heuristics

+---------------------------------+------------------------------------+
| > Situation                     | > 💡 Action \|                     |
|                                 |                                    |
| ==============                  | =============                      |
| =============================== | =================================+ |
|                                 |                                    |
| :   A domain hazard has no      | :   Confidence is **provisional**  |
|     linked test case            |     --- block sign-off\|           |
+---------------------------------+------------------------------------+
|                                 |                                    |
+---------------------------------+------------------------------------+
| Re-run produces unexpected      | Investigate **determinism** before |
| difference                      | re-testing \|                      |
+---------------------------------+------------------------------------+
| Evidence is indirect or         | **Reduce** verdict confidence      |
| inferred                        | level; document \|                 |
+---------------------------------+------------------------------------+
| Coverage metric is near         | Add targeted tests; do **not**     |
| threshold                       | widen threshold\|                  |
+---------------------------------+------------------------------------+
| Schedule pressure to skip fault | Escalate --- fault scenarios are   |
| scenarios                       | **non-optional**                   |
+---------------------------------+------------------------------------+

------------------------------------------------------------------------
