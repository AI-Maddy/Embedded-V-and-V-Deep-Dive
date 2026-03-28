---
title: "Domain Constraints"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# ⚖️ Domain Constraints

::: warning
::: title
Warning
:::

⚠️ Automation scripts that produce, transform, or verify certification
evidence are **tools** under DO-330 and must be assessed for
qualification.
:::

+---------------------+------------------------------------------------+
| Constraint          | Detail                                         |
+=====================+================================================+
| 📜 Compliance       | DO-178C + DO-330 (tool qualification for       |
| baseline            | automation)                                    |
+---------------------+------------------------------------------------+
| 🔧 TQL for scripts  | Batch executor + verdict engine: **TQL-5** if  |
|                     | output is verified independently; **TQL-1** if |
|                     | output used directly as coverage evidence      |
|                     | without independent check.                     |
+---------------------+------------------------------------------------+
| 🔒 Determinis       |                                                |
| m \| Every automate |                                                |
| d run must be bit-f |                                                |
| or-bit reproducible |                                                |
|                     |                                                |
| :   | given the     |                                                |
|       same commit   |                                                |
|       hash,         |                                                |
|       environment,  |                                                |
|       and seeds.    |                                                |
+---------------------+------------------------------------------------+
| 📂 Configuration    | Scripts under the same Git repo + CI as the    |
| control             | model; script version locked in                |
|                     | env_manifest.json.                             |
+---------------------+------------------------------------------------+
| 📋 Audit trail      | CI log must capture: who triggered, commit     |
|                     | hash, start/end time, pass/fail, artifact      |
|                     | locations.                                     |
+---------------------+------------------------------------------------+

------------------------------------------------------------------------
