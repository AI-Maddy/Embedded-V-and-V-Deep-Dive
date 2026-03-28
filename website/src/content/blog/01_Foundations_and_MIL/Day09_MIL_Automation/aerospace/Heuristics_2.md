---
title: "Heuristics 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🔮 Heuristics

+----------------------------------+---------------------------------+---+
| Situation                        | 💡 Action                       |   |
+==================================+=================================+===+
| Campaign takes \> 4 hours        | Profile per-scenario time; move |   |
|                                  | longest runs to overnight       |   |
|                                  | nightly pipeline.               |   |
+----------------------------------+---------------------------------+---+
| 3 % of scenarios flake on re-run | Investigate non-determinism:    |   |
|                                  | seed, solver, Fast Restart      |   |
|                                  | cache, or host-specific float.  |   |
+----------------------------------+---------------------------------+---+
| DER asks \"how do I know the     | Point to CI log, commit hash,   |   |
| script ran correctly?\"          | env_manifest, and DO-330 TQL    |   |
|                                  | assessment record.              |   |
+----------------------------------+---------------------------------+---+
| New requirement added            | Add scenario to manifest,       |   |
| mid-campaign                     | re-run only new scenario,       |   |
|                                  | regenerate traceability report. |   |
+----------------------------------+---------------------------------+---+
| Evi                              |                                 |   |
| dence folder is 50 GB \| Archive |                                 |   |
|  raw logs to network store; keep |                                 |   |
|                                  |                                 |   |
| :   | verdict + traceability +   |                                 |   |
|       manifest in Git. \|        |                                 |   |
+----------------------------------+---------------------------------+---+

------------------------------------------------------------------------
