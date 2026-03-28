🤖 Aerospace Focus — Day 09: MIL Automation
=============================================

.. image:: _images/badge_phase_mil.svg
   :alt: Phase: MIL

.. image:: _images/badge_standard_do178c.svg
   :alt: Standard: DO-178C / DO-330

.. image:: _images/badge_criticality_dal.svg
   :alt: Criticality: DAL-A/B

.. image:: _images/badge_focus_automation.svg
   :alt: Focus: MIL Automation

.. note::
   ⚙️ **Automation Day** — Manual MIL execution does not scale.  A DAL-A flight
   control program typically has 200–500 MIL scenarios across nominal, boundary,
   and fault categories.  Running them by hand introduces human error, breaks
   reproducibility, and blocks regression.  Today we build the **automation
   pipeline** that makes every MIL run scripted, repeatable, hash-verified, and
   evidence-packaged — ready for DER audit without a single manual click.

----

🎯 Objective
------------

Design and implement an **end-to-end MIL automation pipeline** for aerospace
verification: scenario loading → environment validation → batch execution →
verdict assignment → evidence packaging → traceability report generation — all
driven by scripts under configuration control, assessed against DO-330 tool
qualification requirements.

----

🔭 Phase Context
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - 🏗️ **Phase**
     - MIL (Model-in-the-Loop) — automation layer
   * - 🎯 **Primary Focus**
     - Scriptable, repeatable, evidence-grade batch execution
   * - 🔬 **Section Focus**
     - Aerospace MIL automation pipeline and CI integration
   * - 📋 **Lifecycle Standard**
     - DO-178C objectives + DO-330 (tool qualification for scripts)
   * - 💾 **Key Artifact**
     - Automation scripts + CI pipeline config + tool qualification record

----

🏗️  Automation Pipeline Architecture
--------------------------------------

.. code-block:: text

   ┌──────────────────────────────────────────────────────────────────────────┐
   │            AEROSPACE MIL AUTOMATION PIPELINE                             │
   │                                                                          │
   │  ┌─────────────────┐                                                     │
   │  │  Git Repository  │  ← model.slx + params.mat + scenarios/*.json       │
   │  │  (Version Ctrl)  │  ← scripts/ + ci_pipeline.yml + env_manifest.json  │
   │  └────────┬────────┘                                                     │
   │           │  push / merge-request                                        │
   │           ▼                                                              │
   │  ┌─────────────────────────────────────────────────┐                     │
   │  │  ① CI TRIGGER (Jenkins / GitLab CI / GitHub Actions)│                  │
   │  │     • checkout repo at locked commit hash        │                    │
   │  │     • verify env_manifest.json hashes            │                    │
   │  └────────┬────────────────────────────────────────┘                     │
   │           │                                                              │
   │           ▼                                                              │
   │  ┌─────────────────────────────────────────────────┐                     │
   │  │  ② ENVIRONMENT GATE                              │                    │
   │  │     • MATLAB version == locked?                  │                    │
   │  │     • model hash == baseline?                    │                    │
   │  │     • param hash == baseline?                    │                    │
   │  │     • toolbox licenses available?                │                    │
   │  │     ✅ PASS → proceed  │  ❌ FAIL → abort + notify│                    │
   │  └────────┬────────────────────────────────────────┘                     │
   │           │                                                              │
   │           ▼                                                              │
   │  ┌─────────────────────────────────────────────────┐                     │
   │  │  ③ BATCH EXECUTOR                                │                    │
   │  │     • Load scenario matrix (scenarios/*.json)    │                    │
   │  │     • for each scenario:                         │                    │
   │  │       └─ sim() → raw_log.mat                     │                    │
   │  │     • parsim() for N parallel workers            │                    │
   │  │     • Timeout watchdog per scenario              │                    │
   │  └────────┬────────────────────────────────────────┘                     │
   │           │                                                              │
   │           ▼                                                              │
   │  ┌─────────────────────────────────────────────────┐                     │
   │  │  ④ VERDICT ENGINE                                │                    │
   │  │     • Per-scenario quantitative pass/fail        │                    │
   │  │     • Detection latency, RMS error, overshoot    │                    │
   │  │     • verdict.json per run                       │                    │
   │  └────────┬────────────────────────────────────────┘                     │
   │           │                                                              │
   │           ▼                                                              │
   │  ┌─────────────────────────────────────────────────┐                     │
   │  │  ⑤ EVIDENCE PACKAGER                             │                    │
   │  │     • evidence/{date}_run-{id}/                  │                    │
   │  │     • raw_log + verdict + coverage + manifest    │                    │
   │  │     • chmod 444 (write-once)                     │                    │
   │  └────────┬────────────────────────────────────────┘                     │
   │           │                                                              │
   │           ▼                                                              │
   │  ┌─────────────────────────────────────────────────┐                     │
   │  │  ⑥ REPORT GENERATOR                              │                    │
   │  │     • Traceability matrix (req → scenario → verdict)│                 │
   │  │     • Coverage summary (Simulink Coverage)       │                    │
   │  │     • Detection latency histogram                │                    │
   │  │     • Fault coverage matrix                      │                    │
   │  │     • HTML + PDF output for DER review           │                    │
   │  └────────┬────────────────────────────────────────┘                     │
   │           │                                                              │
   │           ▼                                                              │
   │  ┌─────────────────────────────────────────────────┐                     │
   │  │  ⑦ NOTIFICATION + ARCHIVE                        │                    │
   │  │     • Email / Slack: campaign summary + link     │                    │
   │  │     • Artifact archive to network share / S3     │                    │
   │  │     • Git tag: mil_campaign_{date}_{hash}        │                    │
   │  └─────────────────────────────────────────────────┘                     │
   └──────────────────────────────────────────────────────────────────────────┘

----

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

🔄  CI Pipeline Configuration
-------------------------------

.. rubric:: GitLab CI Example (``gitlab-ci.yml``)

.. code-block:: yaml

   stages:
     - gate
     - execute
     - verdict
     - package
     - report

   variables:
     MATLAB_VER: "R2025a"
     CAMPAIGN_FILE: "campaign_manifest.json"

   env-gate:
     stage: gate
     script:
       - python3 scripts/env_gate.py
     artifacts:
       reports:
         junit: gate_report.xml

   mil-batch:
     stage: execute
     needs: [env-gate]
     script:
       - python3 scripts/run_batch.py
     timeout: 4h
     artifacts:
       paths:
         - evidence/
       expire_in: 90 days

   verdict:
     stage: verdict
     needs: [mil-batch]
     script:
       - python3 scripts/verdict_engine.py evidence/*/
     artifacts:
       paths:
         - evidence/*/verdict.json

   package:
     stage: package
     needs: [verdict]
     script:
       - bash scripts/evidence_packager.sh evidence/*_campaign
     artifacts:
       paths:
         - evidence/

   report:
     stage: report
     needs: [package]
     script:
       - python3 scripts/report_gen.py
     artifacts:
       paths:
         - evidence/**/MIL_Campaign_Report.html
         - evidence/**/traceability.csv

.. rubric:: Jenkins Declarative Pipeline (``Jenkinsfile``)

.. code-block:: groovy

   pipeline {
       agent { label 'matlab-r2025a' }
       options { timeout(time: 6, unit: 'HOURS') }

       stages {
           stage('Environment Gate') {
               steps { sh 'python3 scripts/env_gate.py' }
           }
           stage('Batch Execution') {
               steps { sh 'python3 scripts/run_batch.py' }
           }
           stage('Verdict') {
               steps { sh 'python3 scripts/verdict_engine.py evidence/*/' }
           }
           stage('Evidence Package') {
               steps { sh 'bash scripts/evidence_packager.sh evidence/*_campaign' }
           }
           stage('Report') {
               steps { sh 'python3 scripts/report_gen.py' }
           }
       }
       post {
           always {
               archiveArtifacts artifacts: 'evidence/**', fingerprint: true
               emailext subject: "MIL Campaign ${currentBuild.result}",
                        body: '${FILE, path="evidence/campaign_summary.json"}'
           }
       }
   }

----

📂  Evidence Folder Structure (Automated)
-------------------------------------------

.. code-block:: text

   evidence/2026-03-07_campaign/
   ├── 📋 campaign_manifest.json          ← frozen scenario matrix
   ├── 📊 campaign_summary.json           ← execution times + status
   ├── 🗺️  traceability.csv                ← req → scenario → verdict
   ├── 📄 MIL_Campaign_Report.html        ← DER-ready HTML report
   ├── 🔒 file_manifest.sha256            ← integrity hashes
   │
   ├── CL-NOM-01/
   │   ├── scenario.json
   │   ├── raw_log.mat
   │   ├── verdict.json
   │   ├── coverage.html
   │   └── env_manifest.json
   │
   ├── FI-ACT-01/
   │   ├── scenario.json
   │   ├── raw_log.mat
   │   ├── fault_event_log.csv
   │   ├── verdict.json
   │   └── env_manifest.json
   │
   └── ... (one folder per scenario)

----

🔧  DO-330 Tool Qualification for Automation Scripts
------------------------------------------------------

.. tip::
   💡 Your automation scripts are **tools** under DO-330.  The table below shows
   the TQL assignment for each script component.

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Script Component
     - TQL
     - Rationale
   * - 🔒 ``env_gate.py``
     - TQL-5
     - Detects errors (hash mismatch) but does not produce evidence; output is
       advisory — a human reviews the gate result.
   * - 🤖 ``run_batch.py``
     - TQL-5
     - Executes Simulink ``sim()`` — the tool output (raw log) is independently
       verified by the verdict engine.
   * - ✅ ``verdict_engine.py``
     - TQL-3
     - Produces pass/fail verdicts that appear in evidence; output is reviewed but
       could introduce undetected errors (wrong threshold, wrong signal).
   * - 📦 ``evidence_packager.sh``
     - TQL-5
     - Performs file operations (copy, hash, chmod) — output integrity verified
       by SHA-256 manifest check.
   * - 📊 ``report_gen.py``
     - TQL-5
     - Renders data already verified by verdict engine; report is reviewed by DER.
   * - 📈 **Simulink Coverage tool**
     - TQL-1
     - Coverage measurement tool whose output is used directly as MC/DC evidence
       without independent re-verification (DAL-A requirement).

.. warning::
   ⚠️  If the ``verdict_engine.py`` output is used as **sole evidence** without
   independent review, it must be qualified as **TQL-1** — requiring full
   tool qualification data package per DO-330 §12.

----

⏱️  Parallel Execution Strategy
---------------------------------

.. code-block:: text

   ┌─────────────────────────────────────────────────────────────────┐
   │             parsim() PARALLEL EXECUTION LAYOUT                 │
   │                                                                 │
   │  Worker 1  ──► CL-NOM-01 ──► CL-NOM-02 ──► CL-BDY-01 ──►     │
   │  Worker 2  ──► CL-BDY-02 ──► FI-SEN-01 ──► FI-SEN-02 ──►     │
   │  Worker 3  ──► FI-BUS-01 ──► FI-BUS-02 ──► FI-ACT-01 ──►     │
   │  Worker 4  ──► FI-ACT-02 ──► FI-ENV-01 ──► FI-MULTI-01 ──►   │
   │                                                                 │
   │  Rules:                                                         │
   │  • Each worker: independent MATLAB process (no shared state)   │
   │  • Max workers: min(CPU cores, MATLAB licenses)                │
   │  • Timeout: 3× expected single-run duration per scenario       │
   │  • On failure: log error, continue remaining scenarios         │
   └─────────────────────────────────────────────────────────────────┘

.. code-block:: matlab

   % === parsim() batch execution ===
   scenarios = dir('scenarios/*.json');
   simIn = [];
   for i = 1:numel(scenarios)
       sc = jsondecode(fileread(fullfile('scenarios', scenarios(i).name)));
       simIn(i) = Simulink.SimulationInput('FCS_MIL_Harness');
       simIn(i) = simIn(i).setVariable('scenario', sc);
       simIn(i) = simIn(i).setModelParameter('StopTime', num2str(sc.T_sim));
       simIn(i) = simIn(i).setModelParameter('FixedStep', '0.005');
   end

   simOut = parsim(simIn, ...
       'ShowProgress', 'on', ...
       'UseFastRestart', 'on', ...
       'TransferBaseWorkspaceVariables', 'on', ...
       'ShowSimulationManager', 'off');

   fprintf('✅ %d/%d scenarios completed\n', ...
       sum(~arrayfun(@(s) isempty(s.ErrorMessage), simOut)), numel(simOut));

----

🧪 Automation Smoke-Test & Canary
------------------------------------

.. rubric:: 🐦 Canary Scenario

Before running the full campaign, execute a single known-good scenario as a sanity
gate:

.. code-block:: python

   def canary_check(eng, evidence_root):
       """Run minimal scenario to verify toolchain health."""
       print("🐦 Running canary check ...", flush=True)
       eng.eval("simOut = sim('FCS_MIL_Harness', 'StopTime', '5');", nargout=0)
       pitch_err = eng.workspace["pitch_error_rms"]
       assert pitch_err < 1.0, f"Canary FAILED: pitch_err={pitch_err}"
       print("✅ Canary passed — toolchain healthy")

.. rubric:: 🔁 Determinism Verification

After the campaign, re-run a random 10 % sample and compare logs bit-for-bit:

.. code-block:: python

   import random, filecmp

   def verify_determinism(evidence_root, sample_pct=0.1):
       scenarios = list(evidence_root.glob("*/raw_log.mat"))
       sample = random.sample(scenarios, max(1, int(len(scenarios) * sample_pct)))
       for orig_log in sample:
           # Re-run and save to temp
           rerun_log = rerun_scenario(orig_log.parent / "scenario.json")
           if not filecmp.cmp(str(orig_log), str(rerun_log), shallow=False):
               raise AssertionError(f"❌ Non-determinism detected: {orig_log.parent.name}")
           print(f"  ✅ {orig_log.parent.name} — bit-for-bit match")
       print(f"🧬 Determinism verified for {len(sample)} scenarios")

----

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

🚫 Anti-Patterns — What Breaks Automated Evidence
----------------------------------------------------

.. danger::
   ❌ These automation mistakes have caused entire MIL campaigns to be rejected:

- 🚩 Automation scripts **not under version control** — DER cannot verify what ran.
- 🚩 Manual copy-paste of results into a report — breaks traceability chain.
- 🚩 ``parsim()`` workers sharing workspace variables — introduces race conditions.
- 🚩 Deleting or overwriting old evidence folders — evidence tampering risk.
- 🚩 CI pipeline with no timeout — a hung Simulink session blocks for hours with no alert.
- 🚩 Verdict engine reading the **wrong** raw log (path mismatch) — pass/fail is wrong.
- 🚩 Scripts using ``datetime.now()`` as a seed — non-deterministic injection timing.

----

⚠️  Pitfalls
------------

.. caution::

   Automation-specific traps in aerospace MIL:

   - 🕳️  **License contention** — ``parsim()`` with 8 workers needs 8 MATLAB licenses
     + 8 Simulink licenses + toolbox licenses.  If the license server is shared,
     workers queue and the campaign takes 4× longer.  Check ``license('inuse')``
     before setting worker count.
   - 🕳️  **Fast Restart cache corruption** — ``UseFastRestart`` caches compiled model
     state; if a scenario changes model parameters that require recompilation, the
     cache serves stale results.  Disable for fault-injection scenarios that modify
     model structure.
   - 🕳️  **CI artifact expiry** — GitLab CI defaults to 30-day artifact retention;
     certification evidence must be retained for product lifetime (20+ years).
     Archive to a separate long-term store.
   - 🕳️  **Path-length limits** — Windows CI runners hit 260-char path limits with
     deeply nested evidence folders.  Use short folder names or run on Linux.
   - 🕳️  **Timezone-dependent timestamps** — Use UTC everywhere in evidence folders and
     logs.  A DER comparing timestamps across time zones will find discrepancies.

----

🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🏷️
     - Version-tag every campaign: ``git tag mil_campaign_2026-03-07_abc1234``.
   * - ⏩
     - Profile per-scenario execution time; set timeout to 3× P95 to catch hangs without
       false alarms.
   * - 📝
     - Include a ``README.md`` inside every evidence folder: campaign ID, commit hash,
       operator, date, MATLAB version, total pass/fail count.
   * - 🔒
     - Store scripts SHA-256 in ``env_manifest.json`` alongside model and param hashes.
   * - 🧬
     - Run determinism verification as a CI stage (not optional — a failed check blocks
       the pipeline).
   * - 📊
     - Trend campaign pass-rate over time: a dropping pass-rate signals model regression.

----

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

📋 Pre-Closure Checklist
------------------------

.. rubric:: Gate: Must be 100 % complete before automated MIL evidence is submitted

- ☐ All automation scripts are under version control with locked hashes.
- ☐ ``env_gate.py`` passes on the CI runner — no environment drift.
- ☐ Campaign manifest lists every scenario; no ad-hoc additions outside the manifest.
- ☐ Canary scenario passes before full campaign execution.
- ☐ All scenarios executed with quantitative verdicts (no "visual inspection" verdicts).
- ☐ Determinism verification (10 % re-run) confirms bit-for-bit reproduction.
- ☐ Evidence folders are write-once (``chmod 444``), SHA-256 manifested.
- ☐ Traceability CSV links every requirement → scenario → verdict → artifact path.
- ☐ HTML report generated automatically — no manual edits.
- ☐ DO-330 TQL assessment record exists for each script component.
- ☐ CI pipeline config (``gitlab-ci.yml`` / ``Jenkinsfile``) committed and reviewed.
- ☐ Long-term evidence archive location confirmed (not relying on CI artifact retention).

----

🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance to MIL Automation
   * - **DO-330**
     - Software Tool Qualification — governs TQL assignment for automation scripts.
   * - **DO-178C §12**
     - Software verification process — requires documented, repeatable procedures.
   * - **DO-178C Table A-7**
     - Verification of outputs — automated verdicts satisfy these objectives.
   * - **ARP4754A §5.6**
     - Configuration management — applies to scripts, manifests, and evidence.
   * - **DO-331 §6.5**
     - MBDV tool qualification — extends DO-330 for model-based tools.
   * - **IEEE 828**
     - Configuration Management — general guidance for CI-controlled artifacts.

----

.. admonition:: 🚀  Remember

   Automation is not a convenience — it is a **compliance requirement** at scale.
   A manual MIL campaign with 400 scenarios is a human-error minefield: wrong
   parameter file, forgotten log, mismatched version, copy-paste verdict error.
   Automate the pipeline, lock the hashes, generate the reports, and let the DER
   audit the *process* instead of spot-checking the *artifacts*.
