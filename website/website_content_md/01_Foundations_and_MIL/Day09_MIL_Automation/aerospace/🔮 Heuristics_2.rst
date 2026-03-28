🔮 Heuristics
-------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| Campaign takes > 4 hours                      | Profile per-scenario time; move longest runs |
|                                               | to overnight nightly pipeline.               |
+-----------------------------------------------+----------------------------------------------+
| 3 % of scenarios flake on re-run              | Investigate non-determinism: seed, solver,   |
|                                               | Fast Restart cache, or host-specific float.  |
+-----------------------------------------------+----------------------------------------------+
| DER asks "how do I know the script ran        | Point to CI log, commit hash, env_manifest,  |
| correctly?"                                   | and DO-330 TQL assessment record.            |
+-----------------------------------------------+----------------------------------------------+
| New requirement added mid-campaign            | Add scenario to manifest, re-run only new    |
|                                               | scenario, regenerate traceability report.    |
+-----------------------------------------------+----------------------------------------------+
| Evidence folder is 50 GB                       | Archive raw logs to network store; keep      |
|                                               | verdict + traceability + manifest in Git.    |
+-----------------------------------------------+----------------------------------------------+

----

