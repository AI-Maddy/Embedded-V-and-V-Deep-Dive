⚖️  Domain Constraints
----------------------

.. warning::
   ⚠️  Every modeling pattern applied in this domain must satisfy the constraints
   below — they are **DER-observable** and form the basis of SOI-2 model review.

+--------------------------+------------------------------------------------------------+
| Constraint               | Detail                                                     |
+==========================+============================================================+
| 📜 Compliance baseline   | DO-178C / DO-254 + DO-331 + ARP4754A / ARP4761            |
+--------------------------+------------------------------------------------------------+
| ☠️  Key hazard profile    | Loss of control authority · Unstable mode transition ·     |
|                          | Stale avionics data · Latent sensor disagreement           |
+--------------------------+------------------------------------------------------------+
| 🔌 Interface landscape   | ARINC 429 · ARINC 664 (AFDX) · Discrete I/O               |
+--------------------------+------------------------------------------------------------+
| 🎛️  Model coverage        | DO-331 requires model-level MC/DC coverage evidence        |
|                          | in addition to (not instead of) source-code coverage.      |
+--------------------------+------------------------------------------------------------+
| 📐 Modelling standard    | All blocks must comply with MAAB (MathWorks Automotive     |
|                          | Advisory Board) or equivalent internal modelling guideline.|
+--------------------------+------------------------------------------------------------+

----

