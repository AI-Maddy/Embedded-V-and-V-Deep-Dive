✅  Patterns — What Works for MIL Automation
----------------------------------------------

.. tip::
   💡 Automation patterns proven in DAL-A/B aerospace MIL campaigns.

1. **🔒 Hash-gated execution** — No run starts until ``env_gate.py`` confirms all
   hashes match.  This is your cheapest insurance against configuration drift.

2. **📋 Single-source-of-truth manifest** — One ``campaign_manifest.json`` defines
   every scenario; scripts read it, never hard-code scenario IDs.

3. **🤖 Idempotent scripts** — Re-running the same script on the same commit produces
   identical output.  No side effects, no global state, no ``tic/toc`` in logs.

4. **📦 Write-once evidence** — ``chmod 444`` immediately after run; never modify
   evidence after generation.  If a run must be repeated, create a new folder.

5. **📊 Automatic report generation** — Traceability CSV, HTML report, and latency
   histogram generated as the final pipeline stage — no manual post-processing.

6. **🐦 Canary-first execution** — Always run the canary before the full campaign;
   if the canary fails, the CI pipeline aborts before wasting compute hours.

----

