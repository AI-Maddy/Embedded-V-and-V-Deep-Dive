🏆 Aerospace Focus — Day 10: MIL Mini-Project Capstone
=======================================================

.. image:: _images/badge_phase_mil.svg
   :alt: Phase: MIL

.. image:: _images/badge_standard_do178c.svg
   :alt: Standard: DO-178C / DO-330

.. image:: _images/badge_criticality_dal.svg
   :alt: Criticality: DAL-A

.. image:: _images/badge_focus_capstone.svg
   :alt: Focus: MiniProject Capstone

.. note::
   🏁 **Capstone Day** — Everything from Days 01–09 converges here.  You will
   execute a **self-contained, DAL-A-grade MIL verification campaign** for an
   aerospace flight-control sub-function — from requirements through automated
   batch execution to a DER-ready evidence package — and defend the results in
   a simulated certification review.  This is the closest thing to a real
   DO-178C Table A-7 evidence submission you can do in a single day.

----

🎯 Objective
------------

Deliver a **complete, auditable MIL verification evidence package** for a
flight-control sub-function (longitudinal pitch-axis autopilot), covering:

1. Requirements with traceability IDs
2. Plant + controller model under configuration control
3. Scenario matrix (nominal + boundary + fault)
4. Automated batch execution with quantitative verdicts
5. Traceability report (requirement → scenario → verdict → artifact)
6. Residual-risk register with ownership
7. Simulated DER review defence

----

🔭 Phase Context
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - 🏗️ **Phase**
     - MIL (Model-in-the-Loop) — capstone integration
   * - 🎯 **Primary Focus**
     - End-to-end evidence package for a single sub-function
   * - 🔬 **Section Focus**
     - Aerospace MIL capstone — all techniques combined
   * - 📋 **Lifecycle Standard**
     - DO-178C §6.3 / Table A-7 + DO-330 + DO-331
   * - 💾 **Key Artifact**
     - ``MIL_Evidence_Package/`` — the final deliverable

----

🛩️  System Under Verification
-------------------------------

.. code-block:: text

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                 PITCH-AXIS AUTOPILOT (SUV)                            │
   │                                                                       │
   │  θ_cmd ──►┌─────────────┐  δe_cmd  ┌──────────┐  δe   ┌──────────┐  │
   │  (pitch   │  Pitch-Axis │ ───────► │ Actuator │ ────► │ Aircraft │  │
   │   ref)    │  Controller │          │  Model   │       │  Plant   │  │
   │           └──────┬──────┘          └──────────┘       └────┬─────┘  │
   │                  │                                         │        │
   │           ┌──────┴──────┐                           ┌──────┴─────┐  │
   │           │  Mode Logic │  ◄─── pilot discrete ──── │  Sensors   │  │
   │           │  (ALTS/VS/  │       mode switch         │ (IMU/ADC/  │  │
   │           │   ATT/OVRD) │                           │  AHRS)     │  │
   │           └─────────────┘                           └────────────┘  │
   │                                                                       │
   │  Modes:  ATT (attitude hold)  │  VS (vertical speed)  │             │
   │          ALTS (altitude select) │ OVRD (manual override)│            │
   └─────────────────────────────────────────────────────────────────────────┘

----

📋 Requirements Baseline
--------------------------

The mini-project uses 12 requirements derived from a simplified pitch-axis
autopilot specification.  Each requirement has a hazard linkage and DAL.

.. list-table::
   :widths: 15 45 20 10 10
   :header-rows: 1

   * - Req ID
     - Description
     - Hazard Linkage
     - DAL
     - Category
   * - **PA-REQ-001**
     - Pitch-axis controller shall track θ_cmd within ±0.5° RMS in steady
       flight (ATT mode).
     - H-001: loss of pitch control
     - A
     - Nominal
   * - **PA-REQ-002**
     - Settling time for a 5° step command shall be ≤ 3.0 s with ≤ 10 %
       overshoot.
     - H-001
     - A
     - Nominal
   * - **PA-REQ-003**
     - Mode transition ATT → VS shall complete within 200 ms with no
       transient > 2° deviation.
     - H-002: unstable mode change
     - A
     - Boundary
   * - **PA-REQ-004**
     - Mode transition VS → ALTS shall track altitude reference within
       ±50 ft within 15 s.
     - H-002
     - B
     - Boundary
   * - **PA-REQ-005**
     - Pitch-axis controller shall saturate elevator command at ±25° and
       produce a crew alert within 500 ms.
     - H-003: surface over-deflection
     - A
     - Boundary
   * - **PA-REQ-006**
     - Upon single IMU failure, the controller shall switch to backup IMU
       within 100 ms and maintain ≤ 1° transient.
     - H-004: sensor failure
     - A
     - Fault
   * - **PA-REQ-007**
     - Upon ADC loss, controller shall revert to ATT hold using last valid
       altitude; crew alert within 200 ms.
     - H-005: air-data failure
     - A
     - Fault
   * - **PA-REQ-008**
     - Elevator actuator jam at current position shall trigger OVRD mode
       within 300 ms.
     - H-006: actuator failure
     - A
     - Fault
   * - **PA-REQ-009**
     - ARINC 429 label stale-data (no update > 50 ms) shall trigger
       sensor-disagreement monitor.
     - H-007: bus data loss
     - A
     - Fault
   * - **PA-REQ-010**
     - In moderate turbulence (MIL-F-8785C Cat B), tracking error shall
       remain ≤ 1.5° RMS.
     - H-001
     - B
     - Boundary
   * - **PA-REQ-011**
     - Simultaneous IMU failure + turbulence shall not cause pitch
       divergence > 5° within 10 s.
     - H-004 + H-001
     - A
     - Multi-fault
   * - **PA-REQ-012**
     - All mode transitions shall be logged with timestamps and mode IDs
       on the bus (ARINC 429 label 320).
     - Audit requirement
     - C
     - Traceability

----

🗺️  Scenario Matrix
---------------------

.. list-table::
   :widths: 12 12 38 18 20
   :header-rows: 1

   * - Scenario ID
     - Type
     - Description
     - Requirements
     - Key Metrics
   * - **SC-NOM-01**
     - 🟢 Nominal
     - 5° step command in ATT mode, calm air, 30 s sim
     - PA-REQ-001, 002
     - RMS error, settling time, overshoot
   * - **SC-NOM-02**
     - 🟢 Nominal
     - VS mode: 500 fpm climb command, cruise conditions
     - PA-REQ-001
     - VS tracking RMS, steady-state error
   * - **SC-BDY-01**
     - 🟡 Boundary
     - ATT → VS mode transition at Mach 0.78 / FL350
     - PA-REQ-003
     - Transition latency, max transient deviation
   * - **SC-BDY-02**
     - 🟡 Boundary
     - VS → ALTS capture at 35 000 ft target
     - PA-REQ-004
     - Altitude capture error, time to ±50 ft
   * - **SC-BDY-03**
     - 🟡 Boundary
     - Large step (20°) driving elevator to saturation limit
     - PA-REQ-005
     - Saturation detection, crew-alert latency
   * - **SC-BDY-04**
     - 🟡 Boundary
     - Moderate turbulence (MIL-F-8785C Cat B) in ATT mode
     - PA-REQ-010
     - RMS error under turbulence
   * - **SC-FLT-01**
     - 🔴 Fault
     - IMU #1 freeze at t = 10 s during ATT hold
     - PA-REQ-006
     - Switchover latency, transient deviation
   * - **SC-FLT-02**
     - 🔴 Fault
     - ADC total loss at t = 8 s during ALTS mode
     - PA-REQ-007
     - Reversion to ATT, crew alert latency
   * - **SC-FLT-03**
     - 🔴 Fault
     - Elevator actuator jam at δe = +12° at t = 12 s
     - PA-REQ-008
     - OVRD trigger latency, pitch divergence
   * - **SC-FLT-04**
     - 🔴 Fault
     - ARINC 429 stale data (no label update for 80 ms)
     - PA-REQ-009
     - Monitor trigger time, flag assertion
   * - **SC-MFT-01**
     - 🔴🔴 Multi
     - IMU failure + Cat B turbulence simultaneously
     - PA-REQ-011
     - Max pitch deviation in 10 s window
   * - **SC-TRC-01**
     - 📋 Trace
     - All mode transitions logged to ARINC 429 label 320
     - PA-REQ-012
     - Log completeness, timestamp accuracy

----

🏗️  Capstone Execution Pipeline
----------------------------------

.. code-block:: text

   ┌───────────────────────────────────────────────────────────────────────┐
   │               DAY 10 — CAPSTONE PIPELINE                            │
   │                                                                     │
   │  ┌────────────────┐     ┌────────────────┐     ┌────────────────┐  │
   │  │  ① SETUP        │ ──► │  ② ENV GATE     │ ──► │  ③ CANARY      │  │
   │  │  • Clone repo   │     │  • Hash verify  │     │  • SC-NOM-01   │  │
   │  │  • Load params  │     │  • MATLAB ver   │     │  • Quick pass? │  │
   │  │  • Open model   │     │  • License chk  │     │  • Go / No-go  │  │
   │  └────────────────┘     └────────────────┘     └───────┬────────┘  │
   │                                                         │          │
   │                                                         ▼          │
   │  ┌────────────────┐     ┌────────────────┐     ┌────────────────┐  │
   │  │  ⑥ REPORT       │ ◄── │  ⑤ PACKAGE      │ ◄── │  ④ BATCH RUN   │  │
   │  │  • Traceability │     │  • SHA-256 hash │     │  • 12 scenarios│  │
   │  │  • Coverage map │     │  • Write-once   │     │  • Verdicts    │  │
   │  │  • HTML/PDF     │     │  • Manifest     │     │  • Coverage    │  │
   │  └───────┬────────┘     └────────────────┘     └────────────────┘  │
   │          │                                                         │
   │          ▼                                                         │
   │  ┌────────────────┐     ┌────────────────┐                        │
   │  │  ⑦ REVIEW       │ ──► │  ⑧ SIGN-OFF     │                        │
   │  │  • DER sim      │     │  • Risk register│                        │
   │  │  • Q&A defence  │     │  • Action items │                        │
   │  │  • Findings log │     │  • Gate decision│                        │
   │  └────────────────┘     └────────────────┘                        │
   └───────────────────────────────────────────────────────────────────────┘

----

⚖️  Domain Constraints — Capstone Scope
-----------------------------------------

.. warning::
   ⚠️  The mini-project evidence package must satisfy **DO-178C Table A-7** objectives
   for MIL-level verification.  Gaps found during the simulated DER review count as
   open findings that must be dispositioned before sign-off.

+--------------------------+------------------------------------------------------------+
| Constraint               | Detail                                                     |
+==========================+============================================================+
| 📜 Compliance baseline   | DO-178C + DO-331 (MBDV) + DO-330 (tool qualification)      |
+--------------------------+------------------------------------------------------------+
| 🏷️ Requirement coverage  | 12 / 12 requirements must be exercised by ≥ 1 scenario     |
+--------------------------+------------------------------------------------------------+
| 🔧 Verdict type          | Quantitative only — no "visual inspection" verdicts         |
+--------------------------+------------------------------------------------------------+
| 📂 Evidence form         | Structured folder (not a slide deck or Word doc)            |
+--------------------------+------------------------------------------------------------+
| 🔒 Reproducibility       | Determinism-verified by 10 % re-run sample                  |
+--------------------------+------------------------------------------------------------+
| 📋 TQL for scripts       | DO-330 TQL assessment for batch executor + verdict engine   |
+--------------------------+------------------------------------------------------------+

----

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

🎤  Simulated DER Review — Defence Questions
----------------------------------------------

.. tip::
   💡 Prepare to answer these questions during the simulated review.  Each
   question maps to a specific DO-178C concern.

.. list-table::
   :widths: 5 55 40
   :header-rows: 1

   * - #
     - DER Question
     - Expected Evidence
   * - 1
     - "Show me how PA-REQ-006 (IMU switchover) is verified."
     - SC-FLT-01 verdict.json + raw_log.mat plot showing switchover < 100 ms
   * - 2
     - "How do you know the verdict engine itself is correct?"
     - DO-330 TQL-3 assessment record + independent spot-check of 3 verdicts
   * - 3
     - "What happens if I re-run SC-BDY-01 — will I get the same result?"
     - Determinism verification log (10 % re-run bit-for-bit comparison)
   * - 4
     - "Your model has 4 modes — where is the transition coverage matrix?"
     - Mode-transition table: ATT↔VS, VS↔ALTS, any→OVRD (covered by SC-BDY-01..03, SC-FLT-03)
   * - 5
     - "PA-REQ-011 combines IMU failure and turbulence. Is this a worst-case?"
     - SC-MFT-01 uses Cat B turbulence (moderate); justify why Cat C (severe)
       is not required at MIL level (reserved for SIL/HIL)
   * - 6
     - "What residual risks remain after MIL?"
     - Residual-risk register with items, severity, and assigned owners
   * - 7
     - "Show your traceability from requirement to evidence artifact."
     - traceability_matrix.csv — every req → scenario → verdict → artifact path

----

📂  Deliverable Folder Structure
----------------------------------

.. code-block:: text

   MIL_Capstone/
   ├── 📋 campaign_manifest.json          ← frozen scenario matrix
   ├── 📋 env_manifest.json               ← hash-locked environment
   ├── 📋 DO330_TQL_Assessment.md         ← tool qualification record
   │
   ├── models/
   │   └── FCS_Pitch_Autopilot.slx        ← SUV model (locked hash)
   │
   ├── params/
   │   └── aero_params.mat                ← plant + controller gains
   │
   ├── scenarios/
   │   ├── SC-NOM-01.json → SC-NOM-02.json
   │   ├── SC-BDY-01.json → SC-BDY-04.json
   │   ├── SC-FLT-01.json → SC-FLT-04.json
   │   ├── SC-MFT-01.json
   │   └── SC-TRC-01.json
   │
   ├── scripts/
   │   ├── env_gate.py
   │   ├── run_capstone.py
   │   ├── verdict_engine.py
   │   ├── package_evidence.sh
   │   └── generate_report.py
   │
   ├── templates/
   │   └── capstone_report.html.j2
   │
   └── evidence/
       └── capstone_20260307_093000/
           ├── 📊 campaign_results.json
           ├── 🗺️  traceability_matrix.csv
           ├── 📄 MIL_Capstone_Report.html
           ├── 🔒 file_manifest.sha256
           ├── 📝 README.md
           │
           ├── SC-NOM-01/
           │   ├── scenario.json
           │   ├── raw_log.mat
           │   └── verdict.json
           │
           ├── SC-FLT-01/
           │   ├── scenario.json
           │   ├── raw_log.mat
           │   ├── fault_event_log.csv
           │   └── verdict.json
           │
           ├── SC-MFT-01/
           │   ├── scenario.json
           │   ├── raw_log.mat
           │   ├── fault_event_log.csv
           │   └── verdict.json
           │
           └── ... (12 scenario folders total)

----

📊  Scoring Rubric
--------------------

.. list-table::
   :widths: 30 15 55
   :header-rows: 1

   * - Criterion
     - Weight
     - Scoring Guide
   * - 📋 **Requirement coverage**
     - 20 %
     - 12/12 = full marks; < 10 = partial; < 8 = fail
   * - 🧪 **Scenario diversity**
     - 15 %
     - Nominal + boundary + fault + multi-fault + trace = full
   * - ✅ **Verdict quality**
     - 20 %
     - All quantitative with thresholds from requirements; no "visual" verdicts
   * - 🗺️ **Traceability**
     - 15 %
     - Every requirement linked to ≥ 1 scenario → verdict → artifact path
   * - 📦 **Evidence package**
     - 10 %
     - Structured folder, SHA-256 manifest, write-once, README present
   * - 🤖 **Automation**
     - 10 %
     - Scripts run end-to-end without manual intervention
   * - 🎤 **DER review defence**
     - 10 %
     - 5/7 DER questions answered with evidence; residual-risk register complete

----

✅ Patterns — Capstone Best Practices
---------------------------------------

.. tip::
   💡 Patterns distilled from successful DAL-A MIL capstone submissions.

1. **🏁 Start with the traceability matrix, not the model** — If you know which
   requirements you must cover, the scenario matrix writes itself.  Starting with
   the model leads to "test what's easy, miss what's hard."

2. **🐦 Canary-first, always** — A 30-second canary that fails saves you from a
   90-minute wasted batch run.  Never skip the canary.

3. **🔢 Quantitative verdicts only** — "The pitch response looks OK" is not a
   verdict.  ``RMS_error = 0.31° < 0.50° → PASS`` is a verdict.

4. **📋 Evidence folder = single source of truth** — Everything the DER needs is
   inside ``evidence/``.  If an artifact is referenced but not in the folder, it
   doesn't exist.

5. **🔒 Hash everything** — Model, parameters, scripts, and evidence.  If a hash
   doesn't match between the manifest and the file, the whole campaign is suspect.

6. **📝 Write the residual-risk register before the review** — A DER who finds
   uncovered risks before you do will question your entire analysis.

----

🚫 Anti-Patterns
-----------------

.. danger::
   ❌ These mistakes will cause a capstone submission to be rejected:

- 🚩 **No scenario for a requirement** — "We plan to cover PA-REQ-011 in SIL" is
  not acceptable if the capstone scope says all 12 requirements.
- 🚩 **Manual verdict override** — Changing a FAIL to PASS in the JSON file without
  re-running is evidence tampering.
- 🚩 **Slide-deck evidence** — A PowerPoint with pasted screenshots is not an
  auditable evidence package.
- 🚩 **No fault scenarios** — A nominal-only campaign for a DAL-A system is
  grossly incomplete.
- 🚩 **Evidence folder not write-locked** — If files can be modified after the
  campaign, the DER will reject the package.
- 🚩 **Missing TQL assessment** — Scripts are tools; tools need DO-330 assessment.

----

⚠️  Pitfalls
------------

.. caution::

   Capstone-specific traps:

   - 🕳️ **Time management** — You have ~4 hours; if setup takes > 1 hour, you won't
     finish all 12 scenarios.  Use pre-built templates.
   - 🕳️ **Scope creep** — Resist adding a 13th scenario for "extra credit."  Cover
     the 12 requirements first; extras only if time permits.
   - 🕳️ **Fault injection breaks the model** — A poorly configured fault (e.g.,
     elevator jam at 90°) may crash Simulink.  Use guarded fault values.
   - 🕳️ **Report generation fails** — If ``generate_report.py`` crashes, you lose
     the traceability artifact.  Test the report script on canary output first.
   - 🕳️ **Git commit forgotten** — The evidence package references a commit hash;
     if you didn't commit before the run, the hash is wrong.

----

⚠️  Residual-Risk Register Template
--------------------------------------

.. list-table::
   :widths: 10 35 12 15 28
   :header-rows: 1

   * - Risk ID
     - Description
     - Severity
     - Owner
     - Mitigation / Next Action
   * - RR-001
     - Multi-fault scenario (SC-MFT-01) used Cat B turbulence; Cat C
       (severe) not tested at MIL level.
     - Medium
     - V&V Lead
     - Plan Cat C scenario for SIL phase (Day 16).
   * - RR-002
     - Elevator actuator model uses first-order dynamics; real actuator
       has nonlinear backlash.
     - High
     - Plant Eng.
     - Replace with higher-fidelity actuator model before SIL.
   * - RR-003
     - ARINC 429 bus model uses ideal transport delay; no bit-error modeling.
     - Low
     - Avionics Eng.
     - Add bit-error injection at HIL phase (Day 25).
   * - RR-004
     - Coverage measurement relies on Simulink Coverage (TQL-1 tool);
       no independent re-measurement performed.
     - Medium
     - Tool Qual Lead
     - Complete DO-330 TQL-1 qualification data package by SIL entry.

----

🔮 Heuristics
--------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| 3 scenarios fail on first run                 | Don't panic — check canary first; if canary  |
|                                               | passes, investigate scenario config.         |
+-----------------------------------------------+----------------------------------------------+
| DER asks about a requirement you forgot       | Acknowledge the gap, add it to the residual- |
|                                               | risk register, assign an owner, and proceed. |
+-----------------------------------------------+----------------------------------------------+
| Evidence folder is 2 GB                       | Raw logs are large; that's expected.  Archive |
|                                               | to network store; keep verdict + trace in Git|
+-----------------------------------------------+----------------------------------------------+
| Report generation takes 10 min                | Profile: usually a slow ``read_mat()`` call. |
|                                               | Pre-extract verdict JSONs, skip raw re-parse.|
+-----------------------------------------------+----------------------------------------------+
| Determinism check fails for 1 scenario        | Investigate: solver tolerance, random seed,  |
|                                               | or Fast Restart cache.  Document finding.    |
+-----------------------------------------------+----------------------------------------------+

----

📋 Pre-Closure Checklist
--------------------------

.. rubric:: Gate: Must be 100 % complete before capstone sign-off

- ☐ All 12 requirements mapped to ≥ 1 scenario in campaign_manifest.json.
- ☐ All 12 scenarios executed with quantitative verdicts (no manual overrides).
- ☐ Canary scenario (SC-NOM-01) passed before full campaign.
- ☐ Determinism verification (10 % re-run) confirms reproducibility.
- ☐ Evidence folder write-locked (``chmod 444``), SHA-256 manifest generated.
- ☐ Traceability CSV links every Req → Scenario → Verdict → Artifact.
- ☐ HTML/PDF report generated automatically — no manual edits.
- ☐ DO-330 TQL assessment exists for batch executor + verdict engine.
- ☐ Residual-risk register populated with ≥ 3 identified items + owners.
- ☐ Git tag applied: ``mil_capstone_{date}_{hash}``.
- ☐ DER review defence prepared (answers for 7 standard questions).
- ☐ Handoff summary written: what MIL proved, what defers to SIL/HIL.

----

🔗 Standards Traceability
---------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Capstone Relevance
   * - **DO-178C Table A-7**
     - Verification of outputs — the primary compliance target for this capstone.
   * - **DO-178C §6.3**
     - Software verification process — the capstone implements this process.
   * - **DO-331 §6.5**
     - Model-based V&V — the model is the primary design representation.
   * - **DO-330 §12**
     - Tool qualification — scripts that produce evidence are tools.
   * - **ARP4754A §5.4**
     - Validation process — the capstone demonstrates process compliance.
   * - **ARP4761 §4**
     - Safety assessment — fault scenarios derive from FHA/FMEA.
   * - **MIL-F-8785C**
     - Flying qualities — turbulence categories for boundary scenarios.
   * - **IEEE 828**
     - Configuration management — Git-based CM for model + scripts + evidence.

----

.. admonition:: 🎓 Remember

   This capstone is not about writing perfect code.  It is about demonstrating
   that you can **plan, execute, and defend** a MIL verification campaign that a
   DER would accept.  The evidence package is your argument; the traceability
   matrix is your proof; the residual-risk register is your honesty.  Ship the
   package, defend the findings, own the gaps.
