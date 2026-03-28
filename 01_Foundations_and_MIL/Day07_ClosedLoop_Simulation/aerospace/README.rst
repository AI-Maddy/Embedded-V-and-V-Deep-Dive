✈️  Aerospace Focus — Day 07: Closed-Loop Simulation
=====================================================

.. image:: _images/badge_phase_mil.svg
   :alt: Phase: MIL

.. image:: _images/badge_standard_do178c.svg
   :alt: Standard: DO-178C / ARP4754A

.. image:: _images/badge_criticality_dal.svg
   :alt: Criticality: DAL-A/B

.. image:: _images/badge_focus_closedloop.svg
   :alt: Focus: Closed-Loop Simulation

.. note::
   🔄 **Closed-Loop Day** — Today we close the feedback loop: **controller ↔ plant
   ↔ sensors ↔ bus ↔ controller**.  Open-loop MIL (Day 06) verified individual
   command responses; closed-loop MIL verifies that the **entire flight-control
   system** behaves correctly when all elements interact simultaneously — including
   emergent dynamics that only appear when the loop is closed.

----

🎯 Objective
------------

Execute **full closed-loop aerospace MIL simulations** where the Flight Control
System (FCS) model commands actuators, the plant model responds aerodynamically,
sensors measure the result, data traverses the avionics bus, and the FCS reacts
again — verifying stability, tracking performance, fault tolerance, and mode
transitions under realistic feedback conditions.

----

🔭 Phase Context
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - 🏗️ **Phase**
     - MIL (Model-in-the-Loop) — closed-loop configuration
   * - 🎯 **Primary Focus**
     - System-level dynamic behaviour under continuous feedback
   * - 🔬 **Section Focus**
     - Aerospace closed-loop simulation and stability verification
   * - 📋 **Lifecycle Standard**
     - ARP4754A §5.4 (System Verification) + DO-178C Table A-7
   * - 💾 **Key Artifact**
     - Closed-loop time-history evidence with stability metrics

----

🔄  What Makes Closed-Loop Different from Open-Loop?
------------------------------------------------------

.. list-table::
   :widths: 5 45 50
   :header-rows: 1

   * - 
     - 🔓 Open-Loop (Day 06)
     - 🔒 Closed-Loop (Day 07)
   * - 🏗️
     - Controller receives **pre-recorded** stimuli
     - Controller receives **live plant feedback**
   * - 🔁
     - No feedback path; response is one-shot
     - Full feedback: command → actuator → plant → sensor → bus → command
   * - 🧪
     - Tests individual I/O mappings
     - Tests **emergent system behaviour** (stability, oscillation, coupling)
   * - ⚠️
     - Cannot detect PIO, limit-cycle, or feedback instability
     - **Can** detect PIO, limit-cycling, gain-margin violations
   * - 📊
     - Pass/fail: "does signal X match expected value?"
     - Pass/fail: "does the **system** remain stable, converge, and track?"

----

🏗️  Closed-Loop Architecture
------------------------------

.. code-block:: text

   ┌────────────────────────────────────────────────────────────────────────────┐
   │            AEROSPACE CLOSED-LOOP MIL ARCHITECTURE                         │
   │                                                                            │
   │   ┌───────────────────┐     δ_cmd      ┌──────────────────┐               │
   │   │  FCS Controller   │──────────────►  │  Actuator Model  │               │
   │   │  (Simulink/SCADE) │                 │  (rate + pos     │               │
   │   │                   │  ◄──────────    │   limits + lag)  │               │
   │   │  • Normal Law     │  ARINC 429     └────────┬─────────┘               │
   │   │  • Alternate Law  │  sensor bus              │ δ_actual                │
   │   │  • Direct Law     │                          ▼                         │
   │   │  • Envelope Prot. │              ┌──────────────────────┐              │
   │   │  • Monitors       │              │   Plant / FDM Model  │              │
   │   └───────┬───────────┘              │   (JSBSim / Aero     │              │
   │           │                          │    Blockset 6-DOF)   │              │
   │           │ pilot_cmd                │                      │              │
   │           │                          │  • Aerodynamics      │              │
   │   ┌───────┴───────────┐              │  • Engine thrust     │              │
   │   │  Pilot / Autopilot│              │  • Atmosphere (ISA)  │              │
   │   │  Command Source   │              │  • Turbulence        │              │
   │   └──────────────────┘              │  • Gravity / inertia │              │
   │                                      └────────┬─────────────┘              │
   │                                               │ state vector              │
   │                                               │ (α, β, p, q, r,           │
   │                                               │  φ, θ, ψ, V, h)          │
   │                                               ▼                           │
   │                                    ┌──────────────────────┐               │
   │                                    │   Sensor Models      │               │
   │                                    │   • IMU (gyro + acc) │               │
   │                                    │   • ADC (α, Mach, Q) │               │
   │                                    │   • GPS              │               │
   │                                    │   • Noise + bias     │               │
   │                                    └────────┬─────────────┘               │
   │                                             │ measured states              │
   │                                             ▼                             │
   │                                  ┌────────────────────────┐               │
   │                                  │  ARINC 429 / AFDX Bus  │               │
   │                                  │  • BNR encoding        │               │
   │                                  │  • SSM status          │               │
   │                                  │  • Label scheduling    │               │
   │                                  │  • Frame age tracking  │               │
   │                                  └────────────┬───────────┘               │
   │                                               │                           │
   │                              feedback to FCS ─┘                           │
   └────────────────────────────────────────────────────────────────────────────┘

----

⚖️  Domain Constraints
----------------------

.. warning::
   ⚠️  Closed-loop MIL must satisfy all open-loop constraints (Day 06) **plus** the
   additional stability and coupling constraints below.

+--------------------------+------------------------------------------------------------+
| Constraint               | Detail                                                     |
+==========================+============================================================+
| 📜 Compliance baseline   | DO-178C / DO-254 + ARP4754A / ARP4761                      |
+--------------------------+------------------------------------------------------------+
| 🔁 Loop closure fidelity | Plant, sensor, actuator, and bus models must represent      |
|                          | the same frequency range as the controller bandwidth.      |
+--------------------------+------------------------------------------------------------+
| ⏱️  Timestep coherence    | All models in the loop must share the same fixed timestep  |
|                          | (typ. 5 ms / 200 Hz) or use co-simulation with explicit    |
|                          | rate-transition blocks.                                    |
+--------------------------+------------------------------------------------------------+
| 📐 Solver                | Fixed-step ``ode4`` only — variable-step introduces        |
|                          | non-deterministic phase lag that corrupts stability data.  |
+--------------------------+------------------------------------------------------------+
| 🌪️  Disturbance model     | Dryden turbulence per MIL-F-8785C with fixed seed;         |
|                          | severity levels: light / moderate / severe per scenario.   |
+--------------------------+------------------------------------------------------------+

----

📊  Closed-Loop Stability Metrics
-----------------------------------

.. tip::
   💡 These are the **key metrics** that distinguish closed-loop verification from
   open-loop.  Every closed-loop run must report these.

.. list-table::
   :widths: 5 25 40 30
   :header-rows: 1

   * - #
     - Metric
     - What It Tells You
     - Pass Criteria (typical)
   * - 1
     - 📉 **Gain Margin (GM)**
     - How much gain increase the loop tolerates before instability
     - GM ≥ 6 dB (ARP4754A typical)
   * - 2
     - 📐 **Phase Margin (PM)**
     - How much phase lag the loop tolerates before instability
     - PM ≥ 45° (ARP4754A typical)
   * - 3
     - ⏱️  **Settling Time (T_s)**
     - Time to reach and stay within ±2 % of commanded value
     - T_s ≤ 2 s (pitch); ≤ 1.5 s (roll)
   * - 4
     - 📈 **Overshoot (%OS)**
     - Peak transient exceedance above commanded value
     - %OS ≤ 15 % (normal law)
   * - 5
     - 🔄 **Steady-State Error (e_ss)**
     - Residual error after transient decays
     - e_ss < 0.1° (attitude); < 0.5 kt (speed)
   * - 6
     - 🌀 **PIO Susceptibility Index**
     - Pilot-Induced Oscillation tendency (Neal-Smith, bandwidth)
     - Category I (no PIO tendency)
   * - 7
     - 🔒 **Limit-Cycle Amplitude**
     - Sustained oscillation amplitude (if any)
     - Zero (no limit cycle permitted)
   * - 8
     - 🛡️  **Monitor Detection Latency**
     - Time from injected fault to monitor flag assertion
     - ≤ 100 ms (per FHA latency budget)

----

🧪 Closed-Loop Test Scenario Matrix
-------------------------------------

.. rubric:: 🟢 CL-NOM-01: Pitch Doublet — Calm Air

.. code-block:: text

   Configuration:  NORMAL_LAW · Cruise (M 0.78, FL350)
   Command:        ±3° pitch doublet at T = 10 s, 25 s, 40 s
   Turbulence:     None
   Duration:       60 s
   ✅ Accept:       T_s < 2 s · %OS < 10 % · e_ss < 0.1° · no mode change

.. rubric:: 🟢 CL-NOM-02: Roll Step — Moderate Turbulence

.. code-block:: text

   Configuration:  NORMAL_LAW · Approach (M 0.22, 3 000 ft, flaps 30)
   Command:        25° bank-angle command at T = 15 s
   Turbulence:     Dryden moderate (σ_w = 3 m/s), seed #42
   Duration:       45 s
   ✅ Accept:       T_s < 1.5 s · %OS < 15 % · no PIO tendency · wings-level recovery < 3 s

.. rubric:: 🟡 CL-BDY-01: Envelope Excursion Near Stall

.. code-block:: text

   Configuration:  NORMAL_LAW → ENVELOPE_PROTECTION active
   Command:        Slow deceleration V → V_stall + 3 kt over 60 s
   Turbulence:     Dryden light, seed #42
   Duration:       120 s
   ✅ Accept:       Protection soft-cue activates at α_warn
                   Protection hard-override activates at α_max
                   No oscillation in protection engagement (hysteresis check)
                   Recovery after speed increase: protection deactivates within 3 s

.. rubric:: 🟡 CL-BDY-02: Gain-Schedule Cross-Over at High Q

.. code-block:: text

   Configuration:  NORMAL_LAW · Dive recovery (M 0.85 → M 0.6 at FL200)
   Command:        Pull-up command: 2.5 g load factor step
   Turbulence:     None
   Duration:       30 s
   ✅ Accept:       Gain table transitions smoothly (no > 2 % discontinuity)
                   Nz overshoot < 0.3 g · settling < 2 s · actuator stays within limits

.. rubric:: 🔴 CL-FLT-01: ADC Failure — Source Reconfiguration Under Load

.. code-block:: text

   Configuration:  NORMAL_LAW · Cruise (M 0.78, FL350) tracking heading 270°
   Fault:          T = 30 s: ADC-1 ARINC 429 SSM → NCD
                   T = 32 s: ADC-2 frame-age counter exceeds MAX_AGE
   Turbulence:     Dryden light, seed #42
   Duration:       90 s
   ✅ Accept:       Monitor DISAGREE flag within 100 ms of first fault
                   Reconfig to DEGRADED_MODE within 200 ms
                   ECAM CAS message generated
                   Transition to DIRECT_LAW — attitude maintained within ±5°
                   No transient > 1 g Nz during switchover

.. rubric:: 🔴 CL-FLT-02: Actuator Jam — Closed-Loop Recoverability

.. code-block:: text

   Configuration:  NORMAL_LAW · Approach (M 0.22, 3 000 ft)
   Fault:          T = 20 s: elevator actuator jammed at current position
   Turbulence:     Dryden moderate, seed #42
   Duration:       60 s
   ✅ Accept:       FCS detects jam (actuator position ≠ command for > 200 ms)
                   Switches to standby actuator within 500 ms
                   Pitch authority restored — tracking error < 1° after recovery
                   No divergent oscillation during switchover

.. rubric:: 🔴 CL-FLT-03: Double Sensor Disagree + Turbulence Gust

.. code-block:: text

   Configuration:  NORMAL_LAW · Cruise, heading hold
   Fault:          T = 40 s: IMU-1 gyro bias ramp (+2°/s over 5 s)
                   T = 42 s: ADC-1 α measurement frozen (stale)
   Turbulence:     Dryden severe (σ_w = 6 m/s), seed #99
   Duration:       120 s
   ✅ Accept:       Cross-channel monitor detects divergence within 150 ms
                   Median voter selects healthy channel
                   Attitude maintained within ±5° during transient
                   No unrecoverable divergence

----

🔬  Closed-Loop Analysis Techniques
-------------------------------------

.. rubric:: 1️⃣  Time-Domain Step Response Analysis

Extract settling time, overshoot, and steady-state error from the closed-loop
time history.

.. code-block:: python

   import numpy as np

   def step_response_metrics(time, response, command, tolerance=0.02):
       """Compute T_s, %OS, e_ss from closed-loop step response."""
       final_val  = command
       error      = response - final_val
       e_ss       = abs(error[-1])
       peak       = np.max(response)
       overshoot  = max(0, (peak - final_val) / abs(final_val)) * 100  # %

       # Settling: last time |error| > tolerance * |final_val|
       band       = tolerance * abs(final_val)
       outside    = np.where(np.abs(error) > band)[0]
       t_settle   = time[outside[-1]] - time[0] if len(outside) > 0 else 0.0

       return {"T_s": t_settle, "OS_pct": overshoot, "e_ss": e_ss}

.. rubric:: 2️⃣  Frequency-Domain Margin Estimation

Linearise the closed-loop model at the operating point and extract gain/phase margin.

.. code-block:: matlab

   % === Linearise FCS + plant at cruise trim ===
   io = getlinio('FCS_CL_Harness');           % mark loop-break points
   linsys = linearize('FCS_CL_Harness', io);
   [GM, PM, Wcg, Wcp] = margin(linsys);
   fprintf('Gain Margin: %.1f dB @ %.1f rad/s\n', 20*log10(GM), Wcg);
   fprintf('Phase Margin: %.1f deg @ %.1f rad/s\n', PM, Wcp);
   assert(20*log10(GM) >= 6, 'Gain margin below 6 dB!');
   assert(PM >= 45,          'Phase margin below 45 deg!');

.. rubric:: 3️⃣  PIO Susceptibility Assessment

Use bandwidth / phase-delay criteria (MIL-STD-1797A) or Neal-Smith analysis.

.. code-block:: text

   Category I  (no PIO tendency):  ω_BW > 2 rad/s AND τ_p < 0.12 s
   Category II (mild tendency):    ω_BW > 1 rad/s AND τ_p < 0.20 s
   Category III (PIO prone):       anything worse → FAIL

.. rubric:: 4️⃣  Limit-Cycle Detection

Check for sustained oscillations in the residual after the command transient decays.

.. code-block:: python

   def detect_limit_cycle(signal, time, window_start, fft_threshold=0.01):
       """Return True if a limit cycle is detected in the tail of the signal."""
       idx = time >= window_start
       tail = signal[idx] - np.mean(signal[idx])
       spectrum = np.abs(np.fft.rfft(tail))
       spectrum /= len(tail)
       dominant = np.max(spectrum[1:])  # exclude DC
       return dominant > fft_threshold, dominant

----

✅  Patterns — What Works for Closed-Loop
-------------------------------------------

.. tip::
   💡 These patterns are specific to **closed-loop** simulation — they build on
   open-loop patterns from Day 06.

1. **🔄 Loop-break linearisation** — Insert ``getlinio()`` break points at the
   actuator output *before* the first evidence run; extract GM/PM automatically
   after every closed-loop scenario.  Store margins in ``verdict.json``.

2. **📉 Multi-axis coupling check** — Run simultaneous pitch + roll commands to
   verify that cross-coupling stays below the spec limit.  Many bugs only appear
   when two axes are active.

3. **🌪️  Progressive turbulence escalation** — Run the same scenario at light,
   moderate, and severe turbulence; plot RMS tracking error vs. turbulence intensity
   to identify the stability cliff.

4. **⏱️  Transport-delay sweep** — Add artificial bus delay (0, 5, 10, 15 ms) to
   the ARINC 429 feedback path and measure how gain/phase margin degrades; find
   the maximum tolerable delay.

5. **🔒 Freeze-frame assertion** — At the instant of fault injection, log the
   complete state vector; use it as the initial condition for a targeted re-run
   that tests recovery from that exact configuration.

6. **📊 Spectral noise floor check** — After a nominal run, FFT the tracking error
   tail; any peak > noise floor indicates an undamped mode or limit cycle.

----

🚫 Anti-Patterns — What Breaks Closed-Loop Evidence
-----------------------------------------------------

.. danger::
   ❌ Closed-loop adds new failure modes beyond open-loop anti-patterns:

- 🚩 Closing the loop around a **simplified plant** that omits actuator dynamics —
  stability margins will look better than reality; DER will reject.
- 🚩 Logging only the **command** and **response** without the intermediate feedback
  signals (sensor output, bus-decoded value, monitor states) — root-cause analysis
  becomes impossible when a failure occurs.
- 🚩 Using a **variable-step solver** for the plant while the controller runs fixed-step —
  introduces non-deterministic phase shift that corrupts margin measurements.
- 🚩 Testing only one axis at a time — cross-coupling bugs are invisible in
  single-axis closed-loop runs.
- 🚩 Skipping PIO assessment — "the pilot will adapt" is **not** an acceptable
  argument under MIL-STD-1797A / DO-178C.

----

⚠️  Pitfalls
------------

.. caution::

   Closed-loop-specific traps:

   - 🕳️  **Algebraic loop** — Simulink may insert a unit-delay to break an algebraic
     loop; this adds 1× Ts of phase lag that shifts the real phase margin by several
     degrees — check the model diagnostics for implicit delays.
   - 🕳️  **Sensor-model fidelity mismatch** — an ideal sensor (zero noise, zero bias)
     makes the closed loop look better than the real system; always include at least
     the noise and bias from the sensor datasheet.
   - 🕳️  **Trim-state dependency** — a closed-loop run must start from a trimmed
     equilibrium.  If the model is not trimmed, the first few seconds are a transient
     artefact, not a design response.  Use ``operspec()`` + ``findop()`` to compute trim.
   - 🕳️  **Turbulence correlation** — if pitch and roll turbulence channels use the
     same seed, cross-coupling appears artificially low.  Use independent seeds per axis.
   - 🕳️  **Co-simulation rate mismatch** — plant at 100 Hz, controller at 200 Hz
     without a proper rate-transition block causes sample-and-hold glitches that
     masquerade as instability.

----

🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🔗
     - Record **GM and PM** as first-class verdict fields alongside functional pass/fail.
   * - 🧮
     - Automate ``margin()`` extraction as a post-run step — never rely on manual Bode plot readings.
   * - 🌡️
     - Sweep environmental conditions (altitude, Mach, CG, weight) across the flight
       envelope; plot stability margins as a carpet plot for the full envelope.
   * - 📐
     - Validate plant model fidelity before closing the loop: compare open-loop plant
       response with known aerodynamic data (wind-tunnel or flight-test).
   * - 🔒
     - Include a **trim-state hash** in the environment manifest — if trim changes,
       all downstream closed-loop verdicts must be re-evaluated.
   * - 📦
     - Store linearised system objects (``ss``, ``tf``) in the evidence package alongside
       time-domain logs — reviewers need frequency-domain data for margin verification.

----

🔮 Heuristics
-------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| Settling time increases across runs           | Check if trim state drifted; re-trim and     |
|                                               | recompute.                                   |
+-----------------------------------------------+----------------------------------------------+
| Gain margin < 6 dB at one flight point        | **Do not** tune gain — investigate whether   |
|                                               | the plant model is missing an aero mode.     |
+-----------------------------------------------+----------------------------------------------+
| PIO index shifts from Cat I to Cat II         | Add transport-delay sweep; identify the delay|
|                                               | contribution that pushes category.           |
+-----------------------------------------------+----------------------------------------------+
| Cross-coupling exceeds spec on combined       | Check gain-scheduling alignment between axes;|
| pitch + roll manoeuvre                        | verify decoupling compensator coefficients.  |
+-----------------------------------------------+----------------------------------------------+
| Limit cycle detected in FFT at 8 Hz           | Suspect actuator rate-limiter interaction;   |
|                                               | increase rate limit or add notch filter.     |
+-----------------------------------------------+----------------------------------------------+
| Closed-loop run diverges after 60 s           | Likely integrator wind-up; verify anti-windup|
|                                               | logic fires when actuator saturates.         |
+-----------------------------------------------+----------------------------------------------+

----

📋 Pre-Closure Checklist
------------------------

.. rubric:: Gate: Must be 100 % complete before closed-loop MIL evidence is submitted

- ☐ All scenarios in the closed-loop matrix (NOM / BDY / FLT) have verdicts.
- ☐ **Gain margin ≥ 6 dB** and **phase margin ≥ 45°** verified at all linearisation points.
- ☐ PIO susceptibility assessed — Category I confirmed (or justified deviation).
- ☐ Limit-cycle check (FFT tail analysis) — zero sustained oscillation.
- ☐ Multi-axis coupling test (pitch + roll combined) executed and within spec.
- ☐ Turbulence escalation (light / moderate / severe) shows graceful degradation, no cliff.
- ☐ Sensor noise and bias included in all evidence runs (no ideal sensors).
- ☐ Trim state documented and hash-locked in environment manifest.
- ☐ Linearised system objects (``ss``/``tf``) archived in evidence folder.
- ☐ Transport-delay sensitivity logged — maximum tolerable delay documented.
- ☐ All open-loop checklist items (Day 06) also satisfied.
- ☐ Residual risks assigned to named owners with due dates.

----

🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance to Closed-Loop Simulation
   * - **DO-178C Table A-7**
     - Verification of outputs of integration process — closed-loop is integration-level.
   * - **DO-331 §6.3**
     - Model simulation coverage — closed-loop scenarios contribute to model MC/DC.
   * - **ARP4754A §5.4**
     - System verification — closed-loop captures system-level interaction evidence.
   * - **MIL-STD-1797A**
     - Flying Qualities — defines bandwidth, phase-delay, PIO criteria.
   * - **MIL-F-8785C**
     - Flying Qualities — Dryden turbulence model definition.
   * - **ARP4761**
     - Safety assessment — FHA provides latency budgets used in fault scenarios.

----

.. admonition:: 🚀  Remember

   An open-loop test proves the controller **computes** correctly.
   A closed-loop test proves the system **flies** correctly.
   Stability margins, PIO freedom, cross-coupling limits, and fault recoverability
   are properties that **only exist when the loop is closed** — they are the reason
   this day exists.
