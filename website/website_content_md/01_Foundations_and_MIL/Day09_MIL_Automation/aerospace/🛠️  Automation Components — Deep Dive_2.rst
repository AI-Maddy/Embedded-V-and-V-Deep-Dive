🛠️  Automation Components — Deep Dive
---------------------------------------

.. rubric:: ① 📋 Scenario Matrix Definition

Define the complete test matrix as a single JSON manifest linking requirements to
scenarios.

.. code-block:: json

   {
     "campaign": "MIL_FCS_v4.2",
     "date": "2026-03-07",
     "model": "FCS_MIL_Harness.slx",
     "scenarios": [
       {
         "id": "CL-NOM-01",
         "type": "nominal",
         "req_ids": ["FCS-REQ-101", "FCS-REQ-102"],
         "file": "scenarios/CL-NOM-01.json",
         "timeout_s": 120,
         "priority": 1
       },
       {
         "id": "FI-ACT-01",
         "type": "fault",
         "req_ids": ["FCS-REQ-450", "SSA-H-003"],
         "fmea_id": "FM-003-01",
         "file": "scenarios/FI-ACT-01.json",
         "timeout_s": 180,
         "priority": 1
       }
     ]
   }

.. rubric:: ② 🔒 Environment Gate Script

.. code-block:: python

   #!/usr/bin/env python3
   """env_gate.py — Pre-run environment validation (DO-330 TQL-5 tool)."""
   import hashlib, json, sys, subprocess

   def sha256(path):
       return hashlib.sha256(open(path, "rb").read()).hexdigest()

   manifest = json.load(open("env_manifest.json"))
   checks = {
       "model_hash":  sha256("FCS_MIL_Harness.slx") == manifest["model_hash"],
       "param_hash":  sha256("params.mat")           == manifest["param_hash"],
       "script_hash": sha256("scripts/run_batch.py") == manifest["script_hash"],
       "matlab_ver":  subprocess.check_output(
                          ["matlab", "-batch", "disp(version)"]
                      ).decode().strip() == manifest["matlab_ver"],
   }

   for name, ok in checks.items():
       status = "✅" if ok else "❌"
       print(f"  {status}  {name}")

   if not all(checks.values()):
       print("\n🚨 ENVIRONMENT GATE FAILED — aborting campaign")
       sys.exit(1)
   print("\n✅ Environment validated — safe to execute evidence campaign")

.. rubric:: ③ 🤖 Batch Executor (MATLAB + Python Orchestration)

.. code-block:: python

   #!/usr/bin/env python3
   """run_batch.py — Headless batch MIL execution with parsim support."""
   import matlab.engine, json, os, time, hashlib
   from pathlib import Path

   CAMPAIGN = json.load(open("campaign_manifest.json"))
   EVIDENCE_ROOT = Path("evidence") / f"{time.strftime('%Y-%m-%d')}_campaign"
   EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)

   # Start MATLAB engine
   eng = matlab.engine.start_matlab("-nodisplay -nosplash")
   eng.addpath("models", "scripts", nargout=0)
   eng.load("params.mat", nargout=0)

   results = []

   for sc in sorted(CAMPAIGN["scenarios"], key=lambda s: s["priority"]):
       sc_dir = EVIDENCE_ROOT / sc["id"]
       sc_dir.mkdir(exist_ok=True)

       print(f"\n▶️  Running {sc['id']} ...", flush=True)
       t0 = time.time()

       try:
           # Configure model from scenario
           scenario = json.load(open(sc["file"]))
           eng.workspace["scenario"] = scenario
           eng.eval(f"set_param('{CAMPAIGN['model'][:-4]}', "
                    f"'StopTime', '{scenario['T_sim']}')", nargout=0)

           # Execute
           eng.eval(f"simOut = sim('{CAMPAIGN['model'][:-4]}');", nargout=0)

           # Save raw log
           eng.eval(f"save('{sc_dir}/raw_log.mat', 'simOut');", nargout=0)

           elapsed = time.time() - t0
           results.append({"id": sc["id"], "status": "OK", "time_s": round(elapsed, 1)})
           print(f"  ✅ {sc['id']} completed in {elapsed:.1f} s")

       except Exception as e:
           results.append({"id": sc["id"], "status": "ERROR", "error": str(e)})
           print(f"  ❌ {sc['id']} FAILED: {e}")

   eng.quit()

   # Write campaign summary
   json.dump(results, open(EVIDENCE_ROOT / "campaign_summary.json", "w"), indent=2)
   passed = sum(1 for r in results if r["status"] == "OK")
   print(f"\n📊 Campaign complete: {passed}/{len(results)} scenarios executed successfully")

.. rubric:: ④ ✅ Verdict Engine

.. code-block:: python

   #!/usr/bin/env python3
   """verdict_engine.py — Quantitative pass/fail for each scenario."""
   import numpy as np, json
   from pathlib import Path

   def evaluate_scenario(sc_dir: Path, scenario: dict) -> dict:
       log = load_mat(sc_dir / "raw_log.mat")
       verdict = {"scenario_id": scenario["id"], "checks": {}}

       for check in scenario["acceptance_criteria"]:
           signal = log[check["signal"]]
           if check["metric"] == "rms":
               value = float(np.sqrt(np.mean(signal ** 2)))
           elif check["metric"] == "max_abs":
               value = float(np.max(np.abs(signal)))
           elif check["metric"] == "latency_ms":
               t_event = first_true_time(log[check["flag_signal"]])
               value = (t_event - check["t_reference"]) * 1000 if t_event else None

           passed = value is not None and eval(f"{value} {check['op']} {check['threshold']}")
           verdict["checks"][check["req_id"]] = {
               "metric": check["metric"],
               "value": round(value, 4) if value else None,
               "threshold": check["threshold"],
               "op": check["op"],
               "result": "PASS" if passed else "FAIL",
           }

       verdict["overall"] = ("PASS" if all(
           c["result"] == "PASS" for c in verdict["checks"].values()
       ) else "FAIL")

       json.dump(verdict, open(sc_dir / "verdict.json", "w"), indent=2)
       return verdict

.. rubric:: ⑤ 📦 Evidence Packager

.. code-block:: bash

   #!/bin/bash
   # evidence_packager.sh — Lock evidence folder and generate manifest
   set -euo pipefail

   EVIDENCE_DIR="$1"

   # Generate SHA-256 manifest for every file in the evidence folder
   find "$EVIDENCE_DIR" -type f | sort | while read -r f; do
       sha256sum "$f"
   done > "$EVIDENCE_DIR/file_manifest.sha256"

   # Set read-only (write-once, read-many)
   chmod -R a-w "$EVIDENCE_DIR"

   echo "🔒 Evidence folder locked: $EVIDENCE_DIR"
   echo "📋 File count: $(wc -l < "$EVIDENCE_DIR/file_manifest.sha256")"

.. rubric:: ⑥ 📊 Report Generator

.. code-block:: python

   #!/usr/bin/env python3
   """report_gen.py — Generate traceability + summary reports."""
   import json, csv
   from pathlib import Path
   from jinja2 import Template

   EVIDENCE_ROOT = Path("evidence/2026-03-07_campaign")

   # Collect all verdicts
   verdicts = []
   for vf in sorted(EVIDENCE_ROOT.glob("*/verdict.json")):
       verdicts.append(json.load(open(vf)))

   # --- Traceability CSV ---
   with open(EVIDENCE_ROOT / "traceability.csv", "w", newline="") as f:
       w = csv.writer(f)
       w.writerow(["req_id", "scenario_id", "metric", "value", "threshold", "result"])
       for v in verdicts:
           for req_id, chk in v["checks"].items():
               w.writerow([req_id, v["scenario_id"], chk["metric"],
                           chk["value"], chk["threshold"], chk["result"]])

   # --- Summary statistics ---
   total    = len(verdicts)
   passed   = sum(1 for v in verdicts if v["overall"] == "PASS")
   failed   = total - passed
   print(f"📊 Campaign Summary: {passed}/{total} PASS, {failed} FAIL")

   # --- HTML report (Jinja2 template) ---
   tmpl = Template(open("templates/mil_report.html.j2").read())
   html = tmpl.render(verdicts=verdicts, total=total, passed=passed, failed=failed)
   (EVIDENCE_ROOT / "MIL_Campaign_Report.html").write_text(html)
   print("📄 HTML report generated")

----

