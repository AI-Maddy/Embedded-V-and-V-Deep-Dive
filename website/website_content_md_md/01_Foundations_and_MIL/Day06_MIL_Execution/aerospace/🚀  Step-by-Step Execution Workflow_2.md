# 🚀 Step-by-Step Execution Workflow

**Step ① --- 📋 Scenario Load**

  -------------------------------------------------------------------------
  \#   Action                Detail
  ---- --------------------- ----------------------------------------------
  1a   Select scenario from  Each scenario maps to ≥1 requirement ID from
       matrix                the Verification Plan (VP).

  1b   Load `scenario.json`  Contains: stimuli profiles, acceptance
                             thresholds, turbulence seed, duration,
                             expected mode sequence, bus injection
                             schedule.

  1c   Validate schema       Run `jsonschema` check --- reject malformed
                             scenarios before execution.
  -------------------------------------------------------------------------

**Step ② --- 🔒 Environment Validation**

``` python
# Pre-run environment gate (pseudo-code)
import hashlib, json

manifest = json.load(open("env_manifest.json"))
assert hash_file("FCS_MIL.slx") == manifest["model_hash"], "MODEL DRIFT!"
assert hash_file("params.mat")  == manifest["param_hash"], "PARAM DRIFT!"
assert get_matlab_version()     == manifest["matlab_ver"],  "TOOL MISMATCH!"
assert scenario["seed"]         == manifest["seed"],        "SEED CHANGED!"
print("✅ Environment validated — safe to execute evidence run")
```

::: warning
::: title
Warning
:::

🚨 If **any** hash check fails, the run must be classified as
**exploration only**. Fix the drift, regenerate the manifest, and
re-run.
:::

**Step ③ --- ▶️ Simulation Execution**

  -----------------------------------------------------------------------
  Parameter              Typical Aerospace Value
  ---------------------- ------------------------------------------------
  ⏱️ Timestep (`Ts`)     0.005 s (200 Hz) --- matches FCS frame rate

  🕐 Duration (`T_sim`)  30 s (short manoeuvre) to 300 s (full approach
                         profile)

  🔢 Solver              Fixed-step `ode4` (Runge-Kutta) --- DO-178C
                         requires deterministic solver; variable-step is
                         not acceptable.

  🌪️ Turbulence model    Dryden (`MIL-F-8785C`), deterministic seed

  🎛️ Controller mode     Start in NORMAL_LAW; scenario prescribes
                         transition triggers if testing alternate /
                         direct law.

  📡 Bus injection       ARINC 429 labels injected at word rate (100
                         kbps); fault injection starts at `T_fault` per
                         scenario.
  -----------------------------------------------------------------------

``` matlab
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
```

**Step ④ --- 📊 Signal Logging Strategy**

::: tip
::: title
Tip
:::

💡 **Log everything at full rate** --- storage is cheap; re-running a
5-minute sim because you forgot to log one signal is not.
:::

  ------------------------------------------------------------------------
  Signal Category             What to Log                               
  --------------------------- ----------------------------------------- --
  🎯 Primary outputs          Pitch / Roll / Yaw commands; surface      
                              deflections                               

  📡 Bus I/O                  ARINC 429 labels: raw word, decoded       
                              value, SSM, age counter, validity flag    

  🔄 Mode state               Active law (NORMAL / ALT / DIRECT),       
                              transition \| trigger, timestamp          

  🛡️ Monitor outputs          Disagree flag, cross-channel delta,       
                              latency from fault to flag assertion      

  🌡️ Environment inputs       Angle of attack, Mach, dynamic pressure   
                              Q, turbulence components (u, v, w)        

  📐 Error signals            Pitch error, roll error, heading error    
                              (RMS computed post-run for verdict)       

  ⚙️ Actuator state           Commanded vs. actual deflection;          
                              rate-limited flag; saturation flag        
  ------------------------------------------------------------------------

**Step ⑤ --- ✅ Verdict Determination**

``` python
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
```

**Step ⑥ --- 📦 Evidence Packaging**

``` text
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
```

------------------------------------------------------------------------
