🛠️  Step-by-Step Execution Guide
-----------------------------------

.. rubric:: Step ① — Project Setup (30 min)

.. code-block:: bash

   # Clone and set up project structure
   mkdir -p MIL_Capstone/{models,params,scenarios,scripts,evidence,templates}
   cd MIL_Capstone

   # Initialize version control
   git init
   git add -A
   git commit -m "Capstone: initial project scaffold"

   # Copy model and parameters
   cp ../FCS_Pitch_Autopilot.slx models/
   cp ../aero_params.mat params/
   cp ../scenario_templates/*.json scenarios/

.. rubric:: Step ② — Environment Gate (15 min)

.. code-block:: python

   #!/usr/bin/env python3
   """env_gate.py — Validate toolchain before capstone campaign."""
   import hashlib, json, sys

   manifest = json.load(open("env_manifest.json"))
   checks = {}

   for name, path in manifest["files"].items():
       expected = manifest["hashes"][name]
       actual = hashlib.sha256(open(path, "rb").read()).hexdigest()
       checks[name] = actual == expected
       icon = "✅" if checks[name] else "❌"
       print(f"  {icon} {name}: {'MATCH' if checks[name] else 'MISMATCH'}")

   if not all(checks.values()):
       print("\n🚨 Environment gate FAILED — fix before proceeding")
       sys.exit(1)
   print("\n✅ All hashes verified — capstone campaign cleared to start")

.. rubric:: Step ③ — Canary Check (10 min)

Run SC-NOM-01 (simplest nominal scenario) as a toolchain smoke test:

.. code-block:: python

   def canary(eng):
       """5° step in ATT mode — must settle < 3 s, RMS < 0.5°."""
       eng.eval("simOut = sim('FCS_Pitch_Autopilot', 'StopTime', '30');", nargout=0)
       rms = eng.eval("rms(simOut.pitch_error.Data)", nargout=1)
       ts  = eng.eval("stepinfo(simOut.pitch.Data, simOut.tout).SettlingTime", nargout=1)
       assert rms < 0.5, f"Canary FAIL: RMS={rms:.3f}"
       assert ts  < 3.0, f"Canary FAIL: Ts={ts:.2f}s"
       print(f"🐦 Canary PASS — RMS={rms:.3f}°, Ts={ts:.2f}s")

.. rubric:: Step ④ — Batch Execution (90 min)

Execute all 12 scenarios with automated verdicts:

.. code-block:: python

   #!/usr/bin/env python3
   """run_capstone.py — Full 12-scenario MIL capstone campaign."""
   import matlab.engine, json, time
   from pathlib import Path

   eng = matlab.engine.start_matlab("-nodisplay -nosplash")
   campaign = json.load(open("campaign_manifest.json"))
   evidence = Path("evidence") / f"capstone_{time.strftime('%Y%m%d_%H%M%S')}"
   evidence.mkdir(parents=True)

   results = []
   for sc in campaign["scenarios"]:
       sc_dir = evidence / sc["id"]
       sc_dir.mkdir()
       scenario = json.load(open(sc["file"]))

       print(f"\n▶️  [{sc['id']}] {sc['type'].upper()} — {scenario['description']}")
       t0 = time.time()

       # --- Configure ---
       eng.workspace["sc"] = scenario
       if "fault" in scenario:
           eng.eval(f"set_param('FCS_Pitch_Autopilot/{scenario['fault']['block']}', "
                    f"'Value', '{scenario['fault']['value']}')", nargout=0)

       eng.eval(f"set_param('FCS_Pitch_Autopilot', 'StopTime', "
                f"'{scenario['T_sim']}')", nargout=0)

       # --- Execute ---
       eng.eval("simOut = sim('FCS_Pitch_Autopilot');", nargout=0)
       eng.eval(f"save('{sc_dir}/raw_log.mat', 'simOut');", nargout=0)

       # --- Verdict ---
       verdict = evaluate_scenario(eng, sc_dir, scenario)
       elapsed = time.time() - t0

       icon = "✅" if verdict["overall"] == "PASS" else "❌"
       print(f"  {icon} {sc['id']}: {verdict['overall']} ({elapsed:.1f}s)")
       results.append({"id": sc["id"], **verdict, "time_s": round(elapsed, 1)})

   eng.quit()

   # Summary
   passed = sum(1 for r in results if r["overall"] == "PASS")
   print(f"\n{'='*60}")
   print(f"📊 CAPSTONE RESULT: {passed}/{len(results)} scenarios PASS")
   print(f"{'='*60}")
   json.dump(results, open(evidence / "campaign_results.json", "w"), indent=2)

.. rubric:: Step ⑤ — Evidence Packaging (15 min)

.. code-block:: bash

   #!/bin/bash
   # package_evidence.sh — Lock and manifest the evidence folder
   set -euo pipefail
   EVIDENCE="$1"

   # Generate SHA-256 manifest
   find "$EVIDENCE" -type f | sort | while read f; do
       sha256sum "$f"
   done > "$EVIDENCE/file_manifest.sha256"

   # Write README
   cat > "$EVIDENCE/README.md" << EOF
   # MIL Capstone Evidence Package
   - **Date**: $(date -u +%Y-%m-%dT%H:%M:%SZ)
   - **Commit**: $(git rev-parse HEAD)
   - **MATLAB**: R2025a
   - **Model**: FCS_Pitch_Autopilot.slx
   - **Scenarios**: $(ls -d "$EVIDENCE"/SC-* | wc -l)
   - **Result**: See campaign_results.json
   EOF

   # Lock (write-once)
   chmod -R a-w "$EVIDENCE"
   echo "🔒 Evidence locked: $EVIDENCE"

.. rubric:: Step ⑥ — Report Generation (20 min)

.. code-block:: python

   #!/usr/bin/env python3
   """generate_report.py — Traceability report + summary HTML."""
   import json, csv
   from pathlib import Path

   evidence = Path("evidence/capstone_latest")
   results = json.load(open(evidence / "campaign_results.json"))
   campaign = json.load(open("campaign_manifest.json"))

   # --- Traceability Matrix CSV ---
   with open(evidence / "traceability_matrix.csv", "w", newline="") as f:
       w = csv.writer(f)
       w.writerow(["Req_ID", "Scenario_ID", "Type", "Metric", "Value",
                    "Threshold", "Result", "Artifact_Path"])
       for sc in campaign["scenarios"]:
           r = next(x for x in results if x["id"] == sc["id"])
           for req_id in sc["req_ids"]:
               for chk_name, chk in r.get("checks", {}).items():
                   w.writerow([req_id, sc["id"], sc["type"], chk["metric"],
                               chk["value"], chk["threshold"], chk["result"],
                               f"{sc['id']}/raw_log.mat"])

   # --- Requirement Coverage Summary ---
   all_reqs = set()
   covered_reqs = set()
   for sc in campaign["scenarios"]:
       for req in sc["req_ids"]:
           all_reqs.add(req)
           r = next(x for x in results if x["id"] == sc["id"])
           if r["overall"] in ("PASS", "FAIL"):
               covered_reqs.add(req)

   coverage_pct = len(covered_reqs) / len(all_reqs) * 100
   print(f"📋 Requirement coverage: {len(covered_reqs)}/{len(all_reqs)} "
         f"({coverage_pct:.0f}%)")

   # --- Gap Analysis ---
   gaps = all_reqs - covered_reqs
   if gaps:
       print(f"⚠️  UNCOVERED requirements: {', '.join(sorted(gaps))}")
   else:
       print("✅ All requirements exercised by ≥ 1 scenario")

----

