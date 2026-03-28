⚖️  Domain Constraints
----------------------

.. warning::
   ⚠️  Any MIL run that produces evidence must comply with these constraints.
   Runs that violate them are **engineering exploration only** and must not appear
   in the certification evidence package.

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
| ⏱️  Timing fidelity       | Simulation timestep ≤ controller frame rate (typ. 20 ms)   |
+--------------------------+------------------------------------------------------------+
| 🔒 Configuration lock     | Tool versions, model hash, parameter file hash frozen      |
|                          | in CI before any evidence run                              |
+--------------------------+------------------------------------------------------------+

----

