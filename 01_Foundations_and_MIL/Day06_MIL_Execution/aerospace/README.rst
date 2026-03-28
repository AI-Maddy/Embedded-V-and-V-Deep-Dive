✈️  Aerospace Focus — Day 06: MIL Execution
=============================================

.. image:: _images/badge_phase_mil.svg
   :alt: Phase: MIL

.. image:: _images/badge_standard_do178c.svg
   :alt: Standard: DO-178C / ARP4754A

.. image:: _images/badge_criticality_dal.svg
   :alt: Criticality: DAL-A/B

.. image:: _images/badge_focus_execution.svg
   :alt: Focus: MIL Execution

.. note::
   🏁 **Execution Day** — Today we move from setup to **running the models**.
   Every simulation run from this point generates artifacts that become certification
   evidence.  Configuration drift, non-determinism, or missing logs discovered later
   invalidate entire evidence packages — so get the run discipline right **now**.

----

🎯 Objective
------------

Execute **aerospace MIL simulations** against the verified toolchain (Day 05),
capture requirement-linked evidence, and determine pass/fail verdicts for flight
control system (FCS) scenarios — all in a reproducible, auditable pipeline that
satisfies DO-178C Table A-7 verification objectives.

----

🔭 Phase Context
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - 🏗️ **Phase**
     - MIL (Model-in-the-Loop)
   * - 🎯 **Primary Focus**
     - Execute models, capture evidence, assign verdicts
   * - 🔬 **Section Focus**
     - Aerospace MIL execution workflow
   * - 📋 **Lifecycle Standard**
     - ARP4754A + DO-178C Table A-7 (verification of outputs)
   * - 💾 **Key Artifact**
     - Run evidence package: logs + traces + verdicts + traceability matrix

----

⚖️  Domain Constraints
----------------------

.. warning::
   ⚠️  Any MIL run that produces evidence must comply with these constraints.
   Runs that violate them are **engineering exploration only** and must not appear
   in the certification evidence package.

+--------------------------+------------------------------------------------------------+
| Constraint               | Detail                                                     |
+==========================+============================================================+
| 📜 Compliance baseline   | DO-178C / DO-254 + ARP4754A / ARP4761                      |
+--------------------------+------------------------------------------------------------+
| ☠️  Key hazard profile    | Loss of control authority · Unstable mode transition ·     |
|                          | Stale avionics data · Latent sensor disagreement           |
+--------------------------+------------------------------------------------------------+
| 🔌 Interface landscape   | ARINC 429 · ARINC 664 (AFDX) · Discrete I/O               |
+--------------------------+------------------------------------------------------------+
| ⏱️  Timing fidelity       | Simulation timestep ≤ controller frame rate (typ. 20 ms)   |
+--------------------------+------------------------------------------------------------+
| 🔒 Configuration lock     | Tool versions, model hash, parameter file hash frozen      |
|                          | in CI before any evidence run                              |
+--------------------------+------------------------------------------------------------+

----

🏗️  MIL Execution Architecture
-------------------------------

.. rubric:: How a Single MIL Run Flows

.. code-block:: text

   ┌──────────────────────────────────────────────────────────────────────────┐
   │                AEROSPACE MIL EXECUTION PIPELINE                         │
   │                                                                          │
   │  ① SCENARIO LOAD                                                        │
   │     scenario.json → {req_ids, stimuli, thresholds, seeds}                │
   │                          │                                               │
   │  ② ENVIRONMENT VALIDATION                                               │
   │     ├── model hash  == CI baseline?  ✅                                  │
   │     ├── param hash  == CI baseline?  ✅                                  │
   │     ├── tool version == locked?      ✅                                  │
   │     └── seed value  == deterministic? ✅                                 │
   │                          │                                               │
   │  ③ SIMULATION EXECUTION                                                 │
   │     Simulink / SCADE ──► Plant (JSBSim / Aero Blockset)                  │
   │     FCS controller  ◄──► Bus I/O (ARINC 429 stimulus)                   │
   │     Duration: T_sim (scenario-defined, typ. 30–300 s)                    │
   │                          │                                               │
   │  ④ SIGNAL LOGGING                                                       │
   │     ├── .mat / HDF5 raw log (every logged signal, full rate)            │
   │     ├── Bus traces (ARINC 429 labels: value + SSM + age)                │
   │     └── Mode-transition event log (state, time, trigger)                │
   │                          │                                               │
   │  ⑤ VERDICT ENGINE                                                       │
   │     ├── Assert: |pitch_error_rms| < 0.5° ?                              │
   │     ├── Assert: mode_transition count == expected ?                      │
   │     ├── Assert: monitor_flag latency ≤ 100 ms ?                         │
   │     └── [PASS | FAIL | INCONCLUSIVE]                                    │
   │                          │                                               │
   │  ⑥ EVIDENCE PACKAGING                                                   │
   │     evidence/2026-03-07_run-042/                                        │
   │       ├── scenario.json      (frozen input)                              │
   │       ├── raw_log.mat        (full signal dump)                         │
   │       ├── bus_trace.csv      (ARINC 429 decode)                          │
   │       ├── verdict.json       (pass/fail + rationale)                     │
   │       ├── coverage.html      (Simulink Coverage snapshot)               │
   │       ├── env_manifest.json  (hashes + versions)                         │
   │       └── traceability.csv   (req → scenario → verdict)                  │
   └──────────────────────────────────────────────────────────────────────────┘

----

🚀  Step-by-Step Execution Workflow
------------------------------------

.. rubric:: Step ① — 📋 Scenario Load

.. list-table::
   :widths: 5 30 65
   :header-rows: 1

   * - #
     - Action
     - Detail
   * - 1a
     - Select scenario from matrix
     - Each scenario maps to ≥1 requirement ID from the Verification Plan (VP).
   * - 1b
     - Load ``scenario.json``
     - Contains: stimuli profiles, acceptance thresholds, turbulence seed,
       duration, expected mode sequence, bus injection schedule.
   * - 1c
     - Validate schema
     - Run ``jsonschema`` check — reject malformed scenarios before execution.

.. rubric:: Step ② — 🔒 Environment Validation

.. code-block:: python

   # Pre-run environment gate (pseudo-code)
   import hashlib, json

   manifest = json.load(open("env_manifest.json"))
   assert hash_file("FCS_MIL.slx") == manifest["model_hash"], "MODEL DRIFT!"
   assert hash_file("params.mat")  == manifest["param_hash"], "PARAM DRIFT!"
   assert get_matlab_version()     == manifest["matlab_ver"],  "TOOL MISMATCH!"
   assert scenario["seed"]         == manifest["seed"],        "SEED CHANGED!"
   print("✅ Environment validated — safe to execute evidence run")

.. warning::
   🚨 If **any** hash check fails, the run must be classified as **exploration only**.
   Fix the drift, regenerate the manifest, and re-run.

.. rubric:: Step ③ — ▶️  Simulation Execution

+----------------------------+------------------------------------------------------------+
| Parameter                  | Typical Aerospace Value                                    |
+============================+============================================================+
| ⏱️  Timestep (``Ts``)       | 0.005 s (200 Hz) — matches FCS frame rate                  |
+----------------------------+------------------------------------------------------------+
| 🕐 Duration (``T_sim``)    | 30 s (short manoeuvre) to 300 s (full approach profile)    |
+----------------------------+------------------------------------------------------------+
| 🔢 Solver                  | Fixed-step ``ode4`` (Runge-Kutta) — DO-178C requires       |
|                            | deterministic solver; variable-step is not acceptable.     |
+----------------------------+------------------------------------------------------------+
| 🌪️  Turbulence model        | Dryden (``MIL-F-8785C``), deterministic seed               |
+----------------------------+------------------------------------------------------------+
| 🎛️  Controller mode         | Start in NORMAL_LAW; scenario prescribes transition        |
|                            | triggers if testing alternate / direct law.                |
+----------------------------+------------------------------------------------------------+
| 📡 Bus injection           | ARINC 429 labels injected at word rate (100 kbps);         |
|                            | fault injection starts at ``T_fault`` per scenario.        |
+----------------------------+------------------------------------------------------------+

.. code-block:: matlab

   % === Headless MIL execution (MATLAB/Simulink) ===
   load('params.mat');                       % CI-locked parameters
   scenario = jsondecode(fileread('scenario.json'));
   set_param('FCS_MIL_Harness', 'StopTime', num2str(scenario.T_sim));
   set_param('FCS_MIL_Harness', 'FixedStep', '0.005');
   set_param('FCS_MIL_Harness', 'Solver', 'ode4');

   simOut = sim('FCS_MIL_Harness', 'ReturnWorkspaceOutputs', 'on');

   % Save raw log
   save(fullfile(scenario.evidence_dir, 'raw_log.mat'), 'simOut');
   fprintf('✅ Run complete: %s\n', scenario.id);

.. rubric:: Step ④ — 📊 Signal Logging Strategy

.. tip::
   💡 **Log everything at full rate** — storage is cheap; re-running a 5-minute sim
   because you forgot to log one signal is not.

+-------------------------------+------------------------------------------------+
| Signal Category               | What to Log                                    |
+===============================+================================================+
| 🎯 Primary outputs            | Pitch / Roll / Yaw commands; surface deflections|
+-------------------------------+------------------------------------------------+
| 📡 Bus I/O                    | ARINC 429 labels: raw word, decoded value,     |
|                               | SSM, age counter, validity flag                |
+-------------------------------+------------------------------------------------+
| 🔄 Mode state                 | Active law (NORMAL / ALT / DIRECT), transition |
|                               | trigger, timestamp                              |
+-------------------------------+------------------------------------------------+
| 🛡️  Monitor outputs            | Disagree flag, cross-channel delta, latency    |
|                               | from fault to flag assertion                   |
+-------------------------------+------------------------------------------------+
| 🌡️  Environment inputs         | Angle of attack, Mach, dynamic pressure Q,     |
|                               | turbulence components (u, v, w)                |
+-------------------------------+------------------------------------------------+
| 📐 Error signals              | Pitch error, roll error, heading error (RMS    |
|                               | computed post-run for verdict)                 |
+-------------------------------+------------------------------------------------+
| ⚙️  Actuator state             | Commanded vs. actual deflection; rate-limited  |
|                               | flag; saturation flag                          |
+-------------------------------+------------------------------------------------+

.. rubric:: Step ⑤ — ✅ Verdict Determination

.. code-block:: python

   # === Post-run verdict engine (Python) ===
   import numpy as np, json

   log = load_mat("evidence/2026-03-07_run-042/raw_log.mat")
   scenario = json.load(open("scenario.json"))

   verdicts = {}

   # --- Functional accuracy ---
   pitch_rms = np.sqrt(np.mean(log["pitch_error"] ** 2))
   verdicts["FCS-REQ-101"] = {
       "metric":    "pitch_error_rms",
       "value":     round(float(pitch_rms), 4),
       "threshold": 0.5,
       "unit":      "deg",
       "result":    "PASS" if pitch_rms < 0.5 else "FAIL",
   }

   # --- Monitor latency ---
   fault_time  = scenario["T_fault"]
   flag_time   = first_true_time(log["disagree_flag"])
   latency_ms  = (flag_time - fault_time) * 1000
   verdicts["FCS-REQ-204"] = {
       "metric":    "monitor_latency",
       "value":     round(float(latency_ms), 1),
       "threshold": 100.0,
       "unit":      "ms",
       "result":    "PASS" if latency_ms <= 100.0 else "FAIL",
   }

   # --- Mode transition count ---
   transitions = count_transitions(log["mode_state"])
   verdicts["FCS-REQ-310"] = {
       "metric":    "mode_transitions",
       "value":     transitions,
       "threshold": scenario["expected_transitions"],
       "unit":      "count",
       "result":    "PASS" if transitions == scenario["expected_transitions"] else "FAIL",
   }

   json.dump(verdicts, open("verdict.json", "w"), indent=2)
   overall = "PASS" if all(v["result"] == "PASS" for v in verdicts.values()) else "FAIL"
   print(f"{'✅' if overall == 'PASS' else '❌'} Overall verdict: {overall}")

.. rubric:: Step ⑥ — 📦 Evidence Packaging

.. code-block:: text

   evidence/2026-03-07_run-042/
   ├── 📋 scenario.json           ← frozen scenario definition
   ├── 📊 raw_log.mat             ← full-rate signal dump
   ├── 📡 bus_trace.csv           ← ARINC 429 label decode log
   ├── 🔄 mode_transitions.csv    ← state, time, trigger
   ├── ✅ verdict.json             ← per-requirement pass/fail + values
   ├── 📈 coverage_report.html    ← Simulink Coverage snapshot
   ├── 🔒 env_manifest.json       ← tool + model + param hashes
   ├── 🗺️  traceability.csv        ← req_id → scenario_id → verdict
   └── 📝 run_notes.md            ← operator observations (if any)

----

🧪 Domain-Specific MIL Execution Scenarios
--------------------------------------------

.. rubric:: 🟢 NOM-01: Pitch Tracking in Calm Air

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement IDs       | FCS-REQ-101, FCS-REQ-102                          |
+--------------------------+---------------------------------------------------+
| 🌪️  Turbulence             | None (calm-air baseline)                          |
+--------------------------+---------------------------------------------------+
| 🎯 Command profile       | ±5° pitch doublet at 10 s, 20 s, 30 s              |
+--------------------------+---------------------------------------------------+
| ✅ Pass criteria          | Pitch RMS error < 0.5°; settling time < 2 s       |
+--------------------------+---------------------------------------------------+
| 🕐 Duration              | 60 s                                               |
+--------------------------+---------------------------------------------------+
| 🔢 Mode                  | NORMAL_LAW throughout                              |
+--------------------------+---------------------------------------------------+

.. rubric:: 🟡 BDY-01: Gain-Schedule Transition Near Stall Boundary

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement IDs       | FCS-REQ-205, FCS-REQ-206                          |
+--------------------------+---------------------------------------------------+
| 🌪️  Turbulence             | Dryden moderate (σ_w = 3 m/s), fixed seed #42     |
+--------------------------+---------------------------------------------------+
| 🎯 Command profile       | Slow deceleration from 250 kt to V_stall + 5 kt  |
+--------------------------+---------------------------------------------------+
| ✅ Pass criteria          | Protection enters soft zone; no hard override;    |
|                          | no gain-table discontinuity > 2 %                 |
+--------------------------+---------------------------------------------------+
| 🕐 Duration              | 120 s                                              |
+--------------------------+---------------------------------------------------+
| 🔢 Mode                  | NORMAL_LAW → verify no transition to ALT_LAW      |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FLT-01: Dual-ADC Stale Data with Sensor Disagreement

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement IDs       | FCS-REQ-310, FCS-REQ-311, FCS-REQ-401             |
+--------------------------+---------------------------------------------------+
| 🌪️  Turbulence             | Dryden light (σ_w = 1 m/s), fixed seed #42        |
+--------------------------+---------------------------------------------------+
| 💥 Fault injection       | T = 45 s: ADC-1 ARINC 429 label stale            |
|                          | T = 47 s: ADC-2 SSM → NCD (No Computed Data)      |
+--------------------------+---------------------------------------------------+
| ✅ Pass criteria          | Monitor asserts DISAGREE within 100 ms;           |
|                          | reconfig to DEGRADED_MODE within 200 ms;          |
|                          | no loss of positive control; ECAM alert generated |
+--------------------------+---------------------------------------------------+
| 🕐 Duration              | 90 s                                               |
+--------------------------+---------------------------------------------------+
| 🔢 Mode                  | NORMAL_LAW → DIRECT_LAW (automatic)               |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FLT-02: Actuator Saturation During Upset Recovery

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement IDs       | FCS-REQ-450, FCS-REQ-451                          |
+--------------------------+---------------------------------------------------+
| 💥 Fault injection       | T = 20 s: elevator actuator rate-limited to 50 %  |
+--------------------------+---------------------------------------------------+
| ✅ Pass criteria          | Anti-windup prevents integrator overshoot;         |
|                          | surface deflection stays within ± δ_max;           |
|                          | recovery within 10 s after fault cleared          |
+--------------------------+---------------------------------------------------+
| 🕐 Duration              | 60 s                                               |
+--------------------------+---------------------------------------------------+

----

✅  Patterns — What Works During MIL Execution
------------------------------------------------

.. tip::
   💡 These execution patterns are specifically about **running** the model, not
   designing it (Day 04) or setting up tools (Day 05).

1. **🔒 Pre-run gate** — Automate environment validation (hashes, versions, seeds)
   as a mandatory pre-condition; reject any run that fails the gate.

2. **📊 Log-everything-at-full-rate** — Storage is orders of magnitude cheaper than
   re-running a campaign.  Trim logs only in the analysis phase, never at capture.

3. **🤖 Headless batch execution** — Run the entire scenario matrix in a single
   scripted batch (``sim()`` loop or ``parsim()`` for parallel); never rely on
   manual point-and-click for evidence runs.

4. **📐 Quantitative verdicts** — Every pass/fail is a numeric comparison against a
   threshold defined in the scenario file; subjective "looks good" is never acceptable.

5. **📦 Atomic evidence folders** — One folder per run, with a unique monotonic ID.
   Folder is **write-once, read-many** — never modify after run completion.

6. **🔁 Deterministic re-run proof** — After every campaign, randomly re-run 10 % of
   scenarios and verify bit-for-bit identical logs.  Any diff triggers investigation.

----

🚫 Anti-Patterns — What Breaks MIL Evidence
---------------------------------------------

.. danger::
   ❌ These are the most common reasons MIL evidence packages are **rejected at SOI**.

- 🚩 Running simulations from the Simulink GUI instead of a script — no reproducibility.
- 🚩 Logging only "interesting" signals — post-hoc analysis discovers missing data.
- 🚩 Variable-step solver in evidence runs — output timing is non-deterministic.
- 🚩 Overwriting old run folders instead of creating new ones — evidence tampering risk.
- 🚩 Pass/fail assigned by visual inspection of a plot — not auditable.
- 🚩 Mixing exploration runs and evidence runs in the same folder tree.

----

⚠️  Pitfalls
------------

.. caution::

   Subtle execution-time issues that pass internal review but fail DER inspection:

   - 🕳️  **Solver order mismatch** — ``ode4`` (4th-order RK) at MIL but ``ode1``
     (Euler) at SIL code-gen; dynamics differ enough to invalidate back-to-back
     comparison.  Lock solver choice across phases.
   - 🕳️  **Floating-point host dependency** — x86 FMA instructions may produce
     different rounding than the target processor.  Use ``-ffp-contract=off`` or
     equivalent during code-gen to match MIL behaviour.
   - 🕳️  **Signal aliasing** — logging at 200 Hz while the plant model has dynamics
     at > 100 Hz violates Nyquist; important high-frequency oscillations disappear.
   - 🕳️  **Clock-wall-time correlation** — MIL runs faster than real-time; if any
     sub-model uses ``clock()`` or ``tic/toc`` it will produce wrong timing evidence.
   - 🕳️  **Turbulence seed collision** — two scenarios with the same Dryden seed
     produce identical disturbance; coverage appears broader than it actually is.

----

🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🏷️
     - Tag every run folder with ``{date}_{run-id}_{scenario-id}`` for instant lookup.
   * - ⏩
     - Use ``parsim()`` (MATLAB) or ``multiprocessing`` (Python) to run independent
       scenarios in parallel — but never share state between parallel workers.
   * - 📝
     - Write ``run_notes.md`` inside each evidence folder: machine ID, operator,
       any anomalies observed, reason for any manual intervention.
   * - 🔒
     - Set evidence folders to **read-only** (``chmod 444``) immediately after run
       completes; version-control only the manifest, not the raw logs.
   * - 🧬
     - Include a ``canary_check`` scenario — a known-good minimal run whose result
       is used as a sanity gate before processing the full campaign.
   * - 📈
     - Generate summary plots automatically as part of the verdict script, not manually;
       every plot must have title, axis labels, units, requirement ID, and verdict stamp.

----

🔮 Heuristics
-------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| Run completes but verdict is INCONCLUSIVE     | Check signal logging rate — aliasing may hide|
|                                               | the event.  Re-run at 2× sample rate.        |
+-----------------------------------------------+----------------------------------------------+
| Two identical scenarios yield different logs   | Verify seed, solver, and host.  Check for non|
|                                               | -deterministic block (e.g. ``clock()``)      |
+-----------------------------------------------+----------------------------------------------+
| Coverage gap in protection logic              | Add explicit scenario for hysteresis entry    |
|                                               | and exit; verify both independently.         |
+-----------------------------------------------+----------------------------------------------+
| Batch run takes > 4 hours                     | Profile per-scenario time; split long runs;  |
|                                               | use ``parsim()`` with 4–8 workers.           |
+-----------------------------------------------+----------------------------------------------+
| DER asks for raw log but file is 2 GB         | Provide HDF5 with signal index; include a    |
|                                               | viewer script that extracts requested signals.|
+-----------------------------------------------+----------------------------------------------+

----

📋 Pre-Closure Checklist
------------------------

.. rubric:: Gate: Must be 100 % complete before MIL execution evidence is submitted

- ☐ All scenarios in the Verification Plan matrix have been executed and have verdicts.
- ☐ 🟢 Nominal, 🟡 Boundary, and 🔴 Fault scenario categories each have ≥1 completed run.
- ☐ Environment manifest (``env_manifest.json``) hashes match CI baseline — no drift.
- ☐ Deterministic re-run (10 % sample) confirms bit-for-bit identical logs.
- ☐ Every verdict is **quantitative** — numeric value vs. threshold, not visual.
- ☐ Evidence folders are **read-only**; no post-run modifications.
- ☐ Traceability CSV maps every requirement ID → scenario ID → verdict → artifact path.
- ☐ Summary plots include title, axis labels, units, req ID, and verdict stamp.
- ☐ Canary check scenario passes — toolchain sanity confirmed.
- ☐ Coverage report (Simulink Coverage or equivalent) archived in evidence folder.
- ☐ Residual risks and next actions are assigned to named owners with due dates.

----

🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance to MIL Execution
   * - **DO-178C Table A-7**
     - Verification of Outputs — defines what evidence the MIL run must produce.
   * - **DO-331 §6.3**
     - Model simulation, model coverage analysis for MBDV-based verification.
   * - **ARP4754A §5.4**
     - Verification of Function Development — allocates verification activities to phases.
   * - **ARP4761**
     - FHA / FMEA — source of hazard-linked acceptance thresholds.
   * - **DO-330**
     - Tool qualification — applies to Simulink, coverage tools, and verdict scripts.
   * - **MIL-F-8785C**
     - Flying Qualities — defines Dryden turbulence models used as MIL stimuli.

----

.. admonition:: 🚀  Remember

   A MIL run is not a demo — it is a **certification evidence event**.  Every run
   must be scripted, deterministic, hash-verified, and verdict-stamped.  If you
   cannot reproduce a run bit-for-bit on a clean machine tomorrow, the evidence
   it produced is worthless.
