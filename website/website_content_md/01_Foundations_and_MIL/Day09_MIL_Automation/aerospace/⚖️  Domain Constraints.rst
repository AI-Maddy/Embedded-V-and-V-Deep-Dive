⚖️  Domain Constraints
----------------------

.. warning::
   ⚠️  Automation scripts that produce, transform, or verify certification evidence
   are **tools** under DO-330 and must be assessed for qualification.

+--------------------------+------------------------------------------------------------+
| Constraint               | Detail                                                     |
+==========================+============================================================+
| 📜 Compliance baseline   | DO-178C + DO-330 (tool qualification for automation)       |
+--------------------------+------------------------------------------------------------+
| 🔧 TQL for scripts       | Batch executor + verdict engine: **TQL-5** if output is    |
|                          | verified independently; **TQL-1** if output used directly  |
|                          | as coverage evidence without independent check.            |
+--------------------------+------------------------------------------------------------+
| 🔒 Determinism            | Every automated run must be bit-for-bit reproducible       |
|                          | given the same commit hash, environment, and seeds.        |
+--------------------------+------------------------------------------------------------+
| 📂 Configuration control | Scripts under the same Git repo + CI as the model;         |
|                          | script version locked in env_manifest.json.                |
+--------------------------+------------------------------------------------------------+
| 📋 Audit trail           | CI log must capture: who triggered, commit hash, start/end |
|                          | time, pass/fail, artifact locations.                       |
+--------------------------+------------------------------------------------------------+

----

