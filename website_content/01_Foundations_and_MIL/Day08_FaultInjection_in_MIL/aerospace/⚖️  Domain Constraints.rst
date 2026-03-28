⚖️  Domain Constraints
----------------------

+--------------------------+------------------------------------------------------------+
| Constraint               | Detail                                                     |
+==========================+============================================================+
| 📜 Compliance baseline   | DO-178C / DO-254 + ARP4754A / ARP4761                      |
+--------------------------+------------------------------------------------------------+
| ☠️  Hazard severity        | Every CATASTROPHIC / HAZARDOUS FHA item must have ≥1       |
|                          | linked fault-injection scenario at MIL                     |
+--------------------------+------------------------------------------------------------+
| ⏱️  Latency budget         | Monitor detection latency from ARP4761 SSA — typically    |
|                          | 50–200 ms depending on hazard severity                     |
+--------------------------+------------------------------------------------------------+
| 🔌 Bus fidelity           | ARINC 429 SSM, frame age, and label scheduling must be    |
|                          | modelled; injecting a "generic error flag" is insufficient |
+--------------------------+------------------------------------------------------------+
| 🔒 Injection repeatability| Every injection uses a deterministic trigger (time or      |
|                          | state-based), not random — must be bit-for-bit repeatable  |
+--------------------------+------------------------------------------------------------+

----

