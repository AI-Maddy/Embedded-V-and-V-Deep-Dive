⚖️  Domain Constraints
----------------------

.. warning::
   ⚠️  Violating any constraint below is a **DER finding** and will block SOI audits.

+--------------------------+------------------------------------------------------------+
| Constraint               | Detail                                                     |
+==========================+============================================================+
| 📜 Compliance baseline   | DO-178C / DO-254 + ARP4754A / ARP4761                      |
+--------------------------+------------------------------------------------------------+
| ☠️  Key hazard profile    | Loss of control authority · Unstable mode transition ·     |
|                          | Stale avionics data · Latent sensor disagreement           |
+--------------------------+------------------------------------------------------------+
| 🔌 Interface landscape   | ARINC 429 · ARINC 664 (AFDX) · Discrete I/O               |
+--------------------------+------------------------------------------------------------+
| 🕹️  Simulation scope      | Full-envelope plant model + avionics bus stimulus          |
+--------------------------+------------------------------------------------------------+
| 📂 Tool qualification    | TQL-5 minimum; TQL-1 for coverage measurement tools        |
+--------------------------+------------------------------------------------------------+

----

