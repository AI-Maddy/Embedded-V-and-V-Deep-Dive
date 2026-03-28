---
title: "Domain Constraints 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# ⚖️ Domain Constraints

::: warning
::: title
Warning
:::

⚠️ Any MIL run that produces evidence must comply with these
constraints. Runs that violate them are **engineering exploration only**
and must not appear in the certification evidence package.
:::

+--------------------+-----------------------------------------------+---+
| Constraint         | Detail                                        |   |
+====================+===============================================+===+
| 📜 Compliance      | DO-178C / DO-254 + ARP4754A / ARP4761         |   |
| baseline           |                                               |   |
+--------------------+-----------------------------------------------+---+
| ☠️ Key hazard      | Loss of control authority · Unstable mode     |   |
| profile            | transition · Stale avionics data · Latent     |   |
|                    | sensor disagreement                           |   |
+--------------------+-----------------------------------------------+---+
| 🔌 Interface       | ARINC 429 · ARINC 664 (AFDX) · Discrete I/O   |   |
| landscape          | \|                                            |   |
+--------------------+-----------------------------------------------+---+
| ⏱️ Timing fidelity | Simulation timestep ≤ controller frame rate   |   |
|                    | (typ. 20 ms)                                  |   |
+--------------------+-----------------------------------------------+---+
| 🔒 Con             |                                               |   |
| figuration lock \| |                                               |   |
|  Tool versions, mo |                                               |   |
| del hash, paramete |                                               |   |
| r file hash frozen |                                               |   |
|                    |                                               |   |
| :   | in CI before |                                               |   |
|       any evidence |                                               |   |
|       run \|       |                                               |   |
+--------------------+-----------------------------------------------+---+

------------------------------------------------------------------------
