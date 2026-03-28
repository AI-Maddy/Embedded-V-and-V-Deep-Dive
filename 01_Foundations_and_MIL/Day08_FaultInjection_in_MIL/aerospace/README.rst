💥 Aerospace Focus — Day 08: Fault Injection in MIL
=====================================================

.. image:: _images/badge_phase_mil.svg
   :alt: Phase: MIL

.. image:: _images/badge_standard_do178c.svg
   :alt: Standard: DO-178C / ARP4761

.. image:: _images/badge_criticality_dal.svg
   :alt: Criticality: DAL-A/B

.. image:: _images/badge_focus_fault.svg
   :alt: Focus: Fault Injection

.. note::
   🔥 **Fault Day** — Today we deliberately **break things**.  Fault injection at
   MIL phase is the cheapest place to verify that the Flight Control System
   detects, isolates, and recovers from every failure mode identified in the
   ARP4761 safety assessment — before any hardware is involved.  Every hazard in
   the FHA that is not injected at MIL is technical debt carried to SIL/HIL at
   10× cost.

----

🎯 Objective
------------

Systematically inject **aerospace-domain fault conditions** into closed-loop MIL
simulations, verify that monitors detect them within latency budgets, confirm that
reconfiguration logic activates correctly, and produce evidence that maps each
injected fault to its FHA/FMEA/FTA source — satisfying DO-178C verification
objectives and ARP4761 safety assessment obligations.

----

🔭 Phase Context
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - 🏗️ **Phase**
     - MIL (Model-in-the-Loop) — fault injection campaign
   * - 🎯 **Primary Focus**
     - Verify fault detection, isolation, and recovery (FDIR)
   * - 🔬 **Section Focus**
     - Aerospace fault injection methodology and evidence
   * - 📋 **Lifecycle Standard**
     - ARP4761 (safety assessment) + DO-178C Table A-7
   * - 💾 **Key Artifact**
     - Fault injection evidence package with FMEA/FTA traceability

----

🗺️  Aerospace Fault Taxonomy
------------------------------

.. tip::
   💡 Map every fault you inject to **at least one** of these categories.
   If a category has no linked injection test, the safety assessment has a gap.

.. list-table::
   :widths: 5 20 40 35
   :header-rows: 1

   * - #
     - 💥 Fault Category
     - Description
     - Example Injection
   * - 1
     - 📡 **Sensor Fault**
     - Sensor output deviates from truth: bias, drift, noise spike, stuck, NaN
     - IMU gyro stuck at last value; ADC α = NaN
   * - 2
     - 🔌 **Bus / Comms Fault**
     - ARINC 429 / AFDX data corruption, frame loss, stale label, SSM error
     - ARINC 429 label SSM forced to NCD; AFDX VL dropped
   * - 3
     - ⚙️ **Actuator Fault**
     - Actuator jam, runaway, rate-limit degradation, free-float
     - Elevator jammed at +3°; aileron runaway at max rate
   * - 4
     - 🧮 **Computation Fault**
     - Overflow, division-by-zero, mode-logic corruption, memory bit-flip
     - Gain table index out of range → clamped or wrapped?
   * - 5
     - ⚡ **Power / Discrete Fault**
     - Power bus dropout, discrete I/O stuck high/low, relay weld
     - Hydraulic system A → OFF at T = 30 s
   * - 6
     - 🌡️ **Environment Fault**
     - Icing, extreme temperature, windshear, volcanic ash
     - Sudden 30-kt windshear at 200 ft AGL during approach
   * - 7
     - 🔄 **Redundancy Fault**
     - Simultaneous or cascading faults across redundant channels
     - ADC-1 stale + ADC-2 NCD + ADC-3 bias drift (triple fail)

----

🔗  FMEA / FTA → Fault Injection Traceability
-----------------------------------------------

.. warning::
   ⚠️  DO-178C and ARP4761 require **explicit traceability** from every identified
   failure mode to at least one verification activity.  Fault injection at MIL is
   that activity for most FMEA items.

.. code-block:: text

   ┌──────────────────────────────────────────────────────────────────────────┐
   │         SAFETY ASSESSMENT  →  FAULT INJECTION  →  EVIDENCE             │
   │                                                                         │
   │  ARP4761 FHA                                                            │
   │    └── Hazard H-003: "Loss of pitch control authority"                  │
   │          Severity: CATASTROPHIC                                         │
   │                                                                         │
   │  ARP4761 FMEA                                                           │
   │    └── FM-003-01: "Elevator actuator jam"                               │
   │    └── FM-003-02: "Dual ADC failure (stale + NCD)"                      │
   │    └── FM-003-03: "IMU gyro runaway"                                    │
   │                                                                         │
   │  ARP4761 FTA                                                            │
   │    └── Cut set: FM-003-01 AND power-loss-to-standby-actuator            │
   │                                                                         │
   │  MIL Fault Injection                                                    │
   │    └── FI-003-01: inject elevator jam → verify standby switchover       │
   │    └── FI-003-02: inject dual ADC fail → verify DEGRADED_MODE entry     │
   │    └── FI-003-03: inject gyro runaway → verify median voter rejects     │
   │    └── FI-003-04: inject cut set → verify crew alert + safe state       │
   │                                                                         │
   │  Evidence Package                                                       │
   │    └── verdict.json: FI-003-01 → PASS (latency 87 ms < 100 ms budget)  │
   │    └── traceability.csv: H-003 → FM-003-01 → FI-003-01 → PASS          │
   └──────────────────────────────────────────────────────────────────────────┘

----

⚖️  Domain Constraints
----------------------

+--------------------------+------------------------------------------------------------+
| Constraint               | Detail                                                     |
+==========================+============================================================+
| 📜 Compliance baseline   | DO-178C / DO-254 + ARP4754A / ARP4761                      |
+--------------------------+------------------------------------------------------------+
| ☠️  Hazard severity        | Every CATASTROPHIC / HAZARDOUS FHA item must have ≥1       |
|                          | linked fault-injection scenario at MIL                     |
+--------------------------+------------------------------------------------------------+
| ⏱️  Latency budget         | Monitor detection latency from ARP4761 SSA — typically    |
|                          | 50–200 ms depending on hazard severity                     |
+--------------------------+------------------------------------------------------------+
| 🔌 Bus fidelity           | ARINC 429 SSM, frame age, and label scheduling must be    |
|                          | modelled; injecting a "generic error flag" is insufficient |
+--------------------------+------------------------------------------------------------+
| 🔒 Injection repeatability| Every injection uses a deterministic trigger (time or      |
|                          | state-based), not random — must be bit-for-bit repeatable  |
+--------------------------+------------------------------------------------------------+

----

🛠️  Fault Injection Techniques at MIL
---------------------------------------

.. rubric:: 1️⃣  Signal Override (Switch-Based)

The simplest technique: a Simulink switch block selects between the nominal signal
and the injected fault value based on a trigger.

.. code-block:: text

   nominal_signal ──┐
                    ├── [Switch] ──► downstream
   fault_value    ──┘
                    ▲
                    │  trigger: (sim_time >= T_fault)

**Pros:** Easy, deterministic, no model modification.
**Cons:** Can only inject at exposed signal points; cannot model internal corruption.

.. rubric:: 2️⃣  Parameter Perturbation

Modify a model parameter (gain, bias, limit) at runtime to simulate degradation.

.. code-block:: matlab

   % Inject 2°/s gyro bias ramp starting at T = 40 s
   if simTime >= 40
       gyro_bias = min(2.0, (simTime - 40) * 0.4);  % ramp 0.4 °/s²
       imu_output.p = imu_output.p + deg2rad(gyro_bias);
   end

**Use for:** Sensor drift, gain degradation, threshold corruption.

.. rubric:: 3️⃣  Bus-Level Injection

Manipulate ARINC 429 / AFDX fields directly: SSM bits, BNR data field, label
number, or suppress the label entirely to simulate timeout.

.. code-block:: python

   # ARINC 429 label fault injection
   def inject_arinc_fault(label_stream, fault_type, t_inject):
       """Modify ARINC 429 label fields at injection time."""
       for word in label_stream:
           if word.time >= t_inject:
               if fault_type == "SSM_NCD":
                   word.ssm = 0b01          # No Computed Data
               elif fault_type == "SSM_FW":
                   word.ssm = 0b00          # Failure Warning
               elif fault_type == "STALE":
                   word.suppress = True     # stop label transmission
               elif fault_type == "CORRUPT_BNR":
                   word.data ^= 0x1FFFF     # flip all BNR bits
       return label_stream

**Use for:** Realistic avionics bus fault simulation (stale data, SSM errors, label corruption).

.. rubric:: 4️⃣  Actuator Fault Model

Replace the nominal actuator model with a fault-mode variant.

.. code-block:: text

   Fault Mode          │ Implementation
   ════════════════════╪════════════════════════════════════════════
   JAM                 │ Output frozen at position when fault fires
   RUNAWAY             │ Output ramps to hard-stop at max rate
   FREE-FLOAT          │ Output follows aerodynamic hinge moment
   RATE DEGRADATION    │ Max rate reduced to X % of nominal
   OSCILLATORY         │ Sinusoidal disturbance added to command

.. rubric:: 5️⃣  Environment Fault Injection

Inject windshear, icing, or extreme atmosphere deviations into the plant model.

.. code-block:: matlab

   % Inject 30-kt windshear during approach at 200 ft AGL
   if alt_agl <= 200 && alt_agl >= 50
       wind_shear_kts = 30 * (1 - (alt_agl - 50) / 150);  % ramp
       Vwind_x = wind_shear_kts * 0.5144;  % kt → m/s
   end

.. rubric:: 6️⃣  Combinatorial / Multi-Fault Injection

Inject two or more faults simultaneously or in sequence to test FTA cut sets.

.. code-block:: text

   ┌──────────────────────────────────────────────────────────────┐
   │            MULTI-FAULT INJECTION TIMELINE                   │
   │                                                              │
   │  T = 0 s     Normal operation (baseline)                    │
   │  T = 30 s    FAULT A: ADC-1 ARINC 429 label → STALE        │
   │  T = 32 s    FAULT B: ADC-2 SSM → NCD                       │
   │  T = 35 s    Expected: DISAGREE flag + DEGRADED_MODE entry  │
   │  T = 40 s    FAULT C: Elevator actuator jam                 │
   │  T = 42 s    Expected: Standby actuator active; crew alert  │
   │  T = 60 s    End of scenario                                │
   └──────────────────────────────────────────────────────────────┘

----

🧪 Fault Injection Scenario Matrix
------------------------------------

.. rubric:: 🔴 FI-SEN-01: IMU Gyro Stuck-At

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-401, SSA-H-005                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Sensor — gyro p-axis stuck at last value          |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 25 s (during 10°/s roll manoeuvre)            |
+--------------------------+---------------------------------------------------+
| 🔗 FMEA link             | FM-005-01                                         |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Cross-channel monitor detects disagreement within |
|                          | 80 ms; median voter rejects stuck channel;        |
|                          | roll tracking RMS < 1° after recovery             |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-SEN-02: ADC Alpha Bias Ramp

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-402, SSA-H-003                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Sensor — α measurement drifts +0.5°/s             |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 30 s (cruise, straight and level)             |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Envelope-protection monitor detects before α      |
|                          | exceeds α_max; mode transitions to ALT_LAW;      |
|                          | crew alert within 2 s of protection activation    |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-BUS-01: ARINC 429 Label Stale (ADC-1)

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-310, SSA-H-003                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Bus — ADC-1 altitude label stops transmitting      |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 20 s                                          |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Frame-age counter exceeds MAX_AGE within 100 ms;  |
|                          | validity flag → STALE; FCS uses ADC-2 data;       |
|                          | no transient > 0.5° pitch error                   |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-BUS-02: AFDX Virtual Link Frame Loss Burst

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-312, SSA-H-007                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Bus — 500 ms burst of AFDX VL frame loss          |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 35 s                                          |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | FCS holds last-valid-value for ≤ T_HOLD (200 ms); |
|                          | after T_HOLD, switches to degraded source;        |
|                          | no uncommanded surface movement                   |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-ACT-01: Elevator Actuator Jam

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-450, SSA-H-003                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Actuator — elevator jammed at +2°                 |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 25 s (approach, 3000 ft, flaps 30)            |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | FCS detects jam (cmd ≠ position for > 200 ms);    |
|                          | standby actuator engaged within 500 ms;           |
|                          | pitch tracking restored < 1° error                |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-ACT-02: Aileron Runaway

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-452, SSA-H-004                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Actuator — left aileron drives to hard-stop at    |
|                          | maximum rate                                      |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | T = 15 s (cruise, wings level)                    |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Rate monitor detects runaway within 50 ms;        |
|                          | hydraulic shutoff commanded; opposite aileron +   |
|                          | spoiler compensate; bank angle excursion < 10°    |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-ENV-01: Windshear During Approach

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-501, SSA-H-009                            |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Environment — 30-kt microburst windshear at       |
|                          | 200 ft AGL                                        |
+--------------------------+---------------------------------------------------+
| ⏱️  Injection time        | When alt_AGL crosses 200 ft during approach       |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Windshear warning generated within 3 s;           |
|                          | auto-throttle advances to TOGA; flight path       |
|                          | recovers to positive climb gradient within 8 s    |
+--------------------------+---------------------------------------------------+

.. rubric:: 🔴 FI-MULTI-01: FTA Cut Set — Dual ADC + Actuator Jam

+--------------------------+---------------------------------------------------+
| Field                    | Value                                             |
+==========================+===================================================+
| 📋 Requirement ID        | FCS-REQ-310 + FCS-REQ-450, SSA-H-003 (cut set)   |
+--------------------------+---------------------------------------------------+
| 💥 Fault type            | Combinatorial — ADC-1 stale (T=30s), ADC-2 NCD   |
|                          | (T=32s), elevator jam (T=40s)                     |
+--------------------------+---------------------------------------------------+
| ✅ Accept                 | Each fault detected independently; final state:   |
|                          | DIRECT_LAW + standby actuator + crew alert;       |
|                          | positive control maintained throughout;           |
|                          | all transitions within FHA latency budgets        |
+--------------------------+---------------------------------------------------+

----

🏗️  Fault Injection Framework Architecture
--------------------------------------------

.. code-block:: text

   ┌──────────────────────────────────────────────────────────────────────────┐
   │          AEROSPACE MIL FAULT INJECTION FRAMEWORK                        │
   │                                                                          │
   │  ┌──────────────────┐     ┌──────────────────────────────┐              │
   │  │ Fault Scenario   │     │  FMEA / FTA                   │              │
   │  │ Definition       │◄────│  Traceability Database        │              │
   │  │ (JSON)           │     │  (H-xxx → FM-xxx → FI-xxx)    │              │
   │  └────────┬─────────┘     └──────────────────────────────┘              │
   │           │                                                              │
   │           ▼                                                              │
   │  ┌──────────────────────────────────────────────────┐                    │
   │  │         FAULT INJECTION CONTROLLER               │                    │
   │  │                                                  │                    │
   │  │  for each fault in scenario:                     │                    │
   │  │    if trigger_condition(t, state):                │                    │
   │  │      activate_fault(target, type, params)        │                    │
   │  │      log_injection_event(t, fault_id)            │                    │
   │  └────────┬──────────────┬──────────────┬───────────┘                    │
   │           │              │              │                                │
   │           ▼              ▼              ▼                                │
   │  ┌────────────┐  ┌────────────┐  ┌────────────┐                         │
   │  │ Sensor     │  │ Bus I/O    │  │ Actuator   │                         │
   │  │ Models     │  │ Models     │  │ Models     │                         │
   │  └──────┬─────┘  └──────┬─────┘  └──────┬─────┘                         │
   │         └───────────────┼───────────────┘                                │
   │                         ▼                                                │
   │  ┌──────────────────────────────────────────────────┐                    │
   │  │         FCS CONTROLLER (closed-loop)             │                    │
   │  │           ↕ monitors + FDIR logic                │                    │
   │  └────────┬─────────────────────────────────────────┘                    │
   │           │                                                              │
   │           ▼                                                              │
   │  ┌──────────────────────────────────────────────────┐                    │
   │  │         VERDICT ENGINE                           │                    │
   │  │  • Detection latency vs. FHA budget              │                    │
   │  │  • Correct mode transition?                      │                    │
   │  │  • Safe state reached?                           │                    │
   │  │  • Recovery within spec?                         │                    │
   │  └────────┬─────────────────────────────────────────┘                    │
   │           │                                                              │
   │           ▼                                                              │
   │  ┌──────────────────────────────────────────────────┐                    │
   │  │         EVIDENCE PACKAGE                         │                    │
   │  │  raw_log.mat · fault_event_log.csv ·             │                    │
   │  │  verdict.json · traceability.csv                 │                    │
   │  └──────────────────────────────────────────────────┘                    │
   └──────────────────────────────────────────────────────────────────────────┘

----

📊  Fault Injection Verdict Criteria
--------------------------------------

Every fault injection scenario must evaluate **all five** of these criteria:

.. list-table::
   :widths: 5 25 35 35
   :header-rows: 1

   * - #
     - Criterion
     - What Is Checked
     - Typical Threshold
   * - 1
     - 🔍 **Detection**
     - Did the monitor detect the fault?
     - Detection flag asserted = True
   * - 2
     - ⏱️  **Latency**
     - How fast was the fault detected?
     - T_detect − T_inject ≤ FHA budget (50–200 ms)
   * - 3
     - 🔄 **Isolation / Reconfig**
     - Did the system isolate the fault and reconfigure?
     - Correct mode-transition within reconfig budget
   * - 4
     - 🛡️  **Safe State**
     - Did the system reach a safe state?
     - No loss of positive control; transient within limits
   * - 5
     - 🔁 **Recovery**
     - Can the system recover after fault is cleared?
     - Tracking error returns to nominal within T_recovery

.. code-block:: python

   # === Fault injection verdict engine (Python) ===
   import numpy as np, json

   log = load_mat("evidence/FI-ACT-01/raw_log.mat")
   scenario = json.load(open("scenario.json"))

   T_inject = scenario["faults"][0]["t_inject"]
   T_detect = first_true_time(log["jam_detect_flag"])
   T_reconfig = first_true_time(log["standby_active_flag"])

   verdict = {}

   # 1. Detection
   verdict["detection"] = T_detect is not None
   # 2. Latency
   verdict["latency_ms"] = round((T_detect - T_inject) * 1000, 1) if T_detect else None
   verdict["latency_pass"] = verdict["latency_ms"] is not None and verdict["latency_ms"] <= 200
   # 3. Reconfig
   verdict["reconfig_ms"] = round((T_reconfig - T_inject) * 1000, 1) if T_reconfig else None
   verdict["reconfig_pass"] = verdict["reconfig_ms"] is not None and verdict["reconfig_ms"] <= 500
   # 4. Safe state
   max_pitch_err = np.max(np.abs(log["pitch_error"][log["time"] > T_inject]))
   verdict["safe_state"] = max_pitch_err < 5.0  # degrees
   # 5. Recovery
   recovery_window = log["pitch_error"][(log["time"] > T_reconfig + 2) & (log["time"] < T_reconfig + 10)]
   verdict["recovery_rms"] = round(float(np.sqrt(np.mean(recovery_window ** 2))), 3)
   verdict["recovery_pass"] = verdict["recovery_rms"] < 1.0

   overall = all([verdict["detection"], verdict["latency_pass"],
                   verdict["reconfig_pass"], verdict["safe_state"], verdict["recovery_pass"]])
   verdict["overall"] = "PASS" if overall else "FAIL"
   print(f"{'✅' if overall else '❌'} FI-ACT-01: {verdict['overall']}")
   json.dump(verdict, open("verdict.json", "w"), indent=2)

----

✅  Patterns — What Works for Fault Injection
-----------------------------------------------

.. tip::
   💡 Fault injection patterns that have survived DER review in DAL-A programs.

1. **🗂️  FMEA-first injection planning** — Start from the ARP4761 FMEA work product;
   create one injection scenario per failure mode; tag each with the FMEA item ID.

2. **⏱️  Time-triggered + state-triggered injection** — Use time-triggered injection
   for repeatable regression; add state-triggered variants (e.g. "inject when α > 12°")
   for corner-case coverage.

3. **📊 Baseline-then-fault comparison** — Always run the identical scenario without
   fault injection first; diff the two logs to isolate fault effects from nominal dynamics.

4. **🔄 Incremental severity escalation** — For each fault type, start with the mildest
   variant (small bias), then escalate to worst-case (stuck, runaway); plot detection
   latency vs. severity to find the detection threshold.

5. **🧩 Combinatorial coverage from FTA cut sets** — Use the Fault Tree minimal cut sets
   to define multi-fault injection scenarios; verify that the system reaches a safe state
   even when the full cut set fires.

6. **📦 Injection event log** — Log the exact injection time, target signal, fault type,
   and parameter values in a machine-readable ``fault_event_log.csv``; this is the DER's
   primary evidence that the injection was correct.

----

🚫 Anti-Patterns — What Breaks Fault Evidence
-----------------------------------------------

.. danger::
   ❌ These lead to DER rejection of the entire fault injection campaign:

- 🚩 Injecting faults as a **boolean error flag** instead of at the physical signal level —
  skips the realistic detection chain.
- 🚩 Testing only **single faults** when the FTA shows dual/triple cut sets as
  contributing to CATASTROPHIC hazards.
- 🚩 Fault injection scenarios that **cannot be re-run deterministically** — random
  injection timing without a fixed seed invalidates regression.
- 🚩 Pass/fail verdict based on "the system didn't crash" — must have **quantitative**
  detection latency + safe-state metrics.
- 🚩 No baseline (fault-free) comparison run — can't distinguish fault effects from
  nominal dynamics.
- 🚩 FMEA items not traced to injection scenarios — the safety argument has a gap.

----

⚠️  Pitfalls
------------

.. caution::

   Subtle fault-injection pitfalls specific to aerospace MIL:

   - 🕳️  **Injection point too late in the chain** — injecting at the bus-decoded
     output skips the SSM/BNR decoding path; inject at the raw bus interface to test
     the full detection chain.
   - 🕳️  **Fault clears itself** — if the injection uses ``sim_time`` but the model
     resets time on reconfig, the fault disappears; use a persistent fault flag.
   - 🕳️  **Monitor tested with the fault it was designed for** — the monitor passes,
     but a slightly different fault (same sensor, different failure mode) escapes;
     test every FMEA variant, not just the design-case fault.
   - 🕳️  **Actuator fault model ignores aerodynamic load** — a jammed actuator in
     reality sees aerodynamic hinge moment; if your model holds position with zero
     force, the plant response is unrealistically benign.
   - 🕳️  **Windshear injection without pilot model** — windshear recovery requires
     TOGA thrust; if the pilot/autoland model doesn't respond, the scenario is invalid.
   - 🕳️  **Transient masking** — a fault injected during a manoeuvre transient may be
     masked by the normal dynamics; inject at both steady-state and transient
     operating points.

----

🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🏷️
     - Tag every injection scenario with ``FI-{category}-{number}`` (e.g. ``FI-SEN-01``).
   * - 📐
     - Define injection parameters in ``scenario.json``, never as hard-coded model changes.
   * - 🔒
     - Use a **fault injection controller** subsystem — a single block that reads the
       scenario file and applies all faults; never scatter injection logic across the model.
   * - 📊
     - Plot **detection latency histogram** across all scenarios — identify outliers.
   * - 🧬
     - Re-run 20 % of fault scenarios bit-for-bit to confirm deterministic injection.
   * - 🗺️
     - Maintain a **fault coverage matrix**: rows = FMEA items, columns = FI scenarios;
       every cell must be linked or justifiably excluded.

----

🔮 Heuristics
-------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| Monitor fails to detect injected fault        | Check injection point — is it upstream of the|
|                                               | monitor's observation point?                 |
+-----------------------------------------------+----------------------------------------------+
| Detection latency exceeds FHA budget by 10 ms | Verify bus timing + frame-age counter        |
|                                               | resolution; 1-frame jitter may explain.      |
+-----------------------------------------------+----------------------------------------------+
| Multi-fault scenario causes model divergence  | Add saturation / integrator reset on mode    |
|                                               | transition; verify anti-windup fires.        |
+-----------------------------------------------+----------------------------------------------+
| Same fault, different severity → wildly       | Investigate non-linear monitor threshold;    |
| different latency                             | small faults may straddle detection boundary.|
+-----------------------------------------------+----------------------------------------------+
| Regression run detects fault 5 ms faster      | Check if trim state or turbulence seed       |
|                                               | changed — both shift the detection baseline. |
+-----------------------------------------------+----------------------------------------------+
| DER asks "why no combined sensor + actuator   | Point to FTA cut set analysis; if no such    |
| fault?"                                       | cut set exists, justify; if it does, add it. |
+-----------------------------------------------+----------------------------------------------+

----

📋 Pre-Closure Checklist
------------------------

.. rubric:: Gate: Must be 100 % complete before fault injection evidence is submitted

- ☐ Every CATASTROPHIC and HAZARDOUS FHA item has ≥1 linked fault injection scenario.
- ☐ FMEA → FI traceability matrix is complete — no unlinked failure modes.
- ☐ FTA minimal cut sets have combinatorial injection scenarios.
- ☐ All 5 verdict criteria (detection, latency, reconfig, safe state, recovery) evaluated.
- ☐ Baseline (fault-free) comparison run exists for every fault scenario.
- ☐ Injection event log (``fault_event_log.csv``) recorded for every run.
- ☐ Detection latency histogram generated — no outliers exceed FHA budget.
- ☐ 20 % re-run confirms bit-for-bit deterministic injection.
- ☐ Fault coverage matrix reviewed by independent safety engineer.
- ☐ Residual risks (uninjected FMEA items) justified and assigned to SIL/HIL.

----

🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance to Fault Injection
   * - **ARP4761**
     - Safety assessment methods: FHA, FMEA, FTA — source of fault scenarios.
   * - **ARP4754A §5.5**
     - Safety assessment and system verification — requires fault analysis evidence.
   * - **DO-178C Table A-7**
     - Verification of outputs — fault injection is part of robustness verification.
   * - **DO-331 §6.4**
     - Model robustness testing — MBDV supplement for fault scenarios at model level.
   * - **DO-254 §6.3**
     - Hardware fault analysis — for combined SW/HW fault modes.
   * - **SAE ARP5107**
     - Common Mode Failure analysis guidelines — drives multi-fault scenarios.

----

.. admonition:: 🚀  Remember

   Fault injection is not about proving the system **works** — nominal tests do that.
   Fault injection is about proving the system **fails safely**.  Every hazard in the
   FHA is a question: "What happens when this goes wrong?"  Your fault injection
   campaign is the answer — and the answer must be documented, quantified, and
   traceable all the way back to the safety assessment.
