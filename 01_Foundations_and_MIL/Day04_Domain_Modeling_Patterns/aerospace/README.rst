✈️  Aerospace Focus — Day 04: Domain Modeling Patterns
=======================================================

.. image:: _images/badge_phase_mil.svg
   :alt: Phase: MIL

.. image:: _images/badge_standard_do178c.svg
   :alt: Standard: DO-178C / DO-331

.. image:: _images/badge_criticality_dal.svg
   :alt: Criticality: DAL-A/B

.. image:: _images/badge_focus_modeling.svg
   :alt: Focus: Domain Modeling Patterns

.. note::
   🛡️ **DO-331 Important** — Model-Based Development and Verification (MBDV) is a
   first-class supplement to DO-178C.  Every modeling pattern you choose at MIL
   phase directly shapes coverage obligations, traceability structure, and the
   evidence baseline carried forward through SIL and HIL.

----

🎯 Objective
------------

Select, apply, and validate **aerospace-specific domain modeling patterns** that
correctly capture flight-control semantics, avionics interface contracts, and
safety-critical fault-containment behaviour — all traceable to ARP4754A / DO-178C
objectives before a single line of production code is generated.

----

🔭 Phase Context
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - 🏗️ **Phase**
     - MIL (Model-in-the-Loop)
   * - 🎯 **Primary Focus**
     - Model behaviour realism and requirement intent validation
   * - 🔬 **Section Focus**
     - Aerospace domain modeling patterns
   * - 📋 **Lifecycle Standard**
     - ARP4754A + DO-331 (MBDV supplement to DO-178C)
   * - 🗂️ **Key Artifact**
     - Verified model satisfying DO-330 TQL + model coverage report

----

🗺️  Aerospace Domain Modeling Pattern Catalogue
-------------------------------------------------

.. tip::
   💡 Each pattern below maps to one or more **ARP4754A development assurance
   requirements** and one or more **DO-178C / DO-331 verification objectives**.
   Use the Pattern ID as a tag on every model block, test case, and review record.

----

Pattern 1 — 🔄 Hierarchical Mode-Logic State Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

Flight-control law mode transitions: Normal Law → Alternate Law → Direct Law
(Airbus-style) or Normal / Secondary / Direct (Boeing-style).  Also applies to
autopilot engagement/disengagement logic, envelope-protection activation, and
TCAS/ACAS mode arbitration.

.. rubric:: Structure

.. code-block:: text

   ┌──────────────────────────────────────────────────────────┐
   │                   MODE SUPERVISOR (Stateflow)            │
   │                                                          │
   │  [NORMAL_LAW] ──fault──►  [ALTERNATE_LAW]               │
   │       ▲                        │  ──severe fault──►      │
   │       │ recovery (if safe)     ▼                         │
   │       └────────────── [DIRECT_LAW]                       │
   │                                                          │
   │  Entry actions  : latch gain set, arm monitors           │
   │  During actions : execute active law, update status bus  │
   │  Exit actions   : freeze integrators, log transition     │
   └──────────────────────────────────────────────────────────┘

.. rubric:: DO-178C / DO-331 Obligations

+-------------------------------------+----------------------------------------------+
| Obligation                          | Guidance                                     |
+=====================================+==============================================+
| 📊 Decision coverage (MC/DC)        | Every mode-transition condition must be       |
|                                     | independently exercised (DAL-A requirement).  |
+-------------------------------------+----------------------------------------------+
| 🔗 Requirement traceability         | Each transition guard maps to ≥1 system       |
|                                     | requirement ID (e.g. ``FCS-MODE-REQ-017``).   |
+-------------------------------------+----------------------------------------------+
| 🔒 Transition inhibit conditions    | Must be modelled explicitly — not implied     |
|                                     | by absence of a trigger.                      |
+-------------------------------------+----------------------------------------------+
| 🧪 Reachability proof               | Every state must be reachable by ≥1 test      |
|                                     | case; unreachable states are dead code.       |
+-------------------------------------+----------------------------------------------+

.. rubric:: ⚠️  Common Mistakes

- Implicit default transitions that bypass safety interlocks.
- Missing ``exit`` action to freeze integrators on unexpected mode exit.
- Writing guards as compound boolean expressions not decomposed for MC/DC.

----

Pattern 2 — 🧮 Gain-Scheduled Control Law Block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

Continuous variation of controller gains (pitch / roll / yaw channels) as a
function of flight envelope parameters: Mach number, dynamic pressure (Q),
altitude band, flap configuration, and CG range.

.. rubric:: Key Implementation Rules

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 📐
     - Store gain tables as **parameter objects** (``Simulink.Parameter`` or SCADE
       ``const`` blocks) — never as magic numbers in subsystem masks.
   * - 🗃️
     - Version-control the gain dataset separately from the algorithm model;
       require a configuration item (CI) entry for every gain table change.
   * - 🌡️
     - Include an **atmosphere model** (COESA or ISA) to derive dynamic pressure
       from altitude + TAS inputs — do not use raw sensor values without validation.
   * - 🔒
     - Clamp all gain outputs to physical limits before they reach actuator commands;
       clamping logic must be separately verified, not absorbed into the gain table.
   * - 📏
     - Define gain scheduling break-points at flight-envelope boundary conditions
       to ensure test vectors hit every table segment.

.. rubric:: 🟡 Boundary Condition Pattern

.. code-block:: text

   Gain table break-points must be tested at:
     ├── Exactly at break-point value          (interpolation edge)
     ├── 1 LSB below break-point               (lower segment)
     ├── 1 LSB above break-point               (upper segment)
     └── Minimum and maximum table extent      (clamping)

----

Pattern 3 — 🔌 Avionics Bus Interface Model (ARINC 429 / AFDX)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

All sensor and cross-channel data arriving via ARINC 429 labels or AFDX Virtual
Links must be modelled with explicit **data validity**, **SSM (Sign/Status Matrix)**
decoding, **frame-age monitoring**, and **NCD (No Computed Data)** handling.

.. rubric:: ARINC 429 Label Validity State Machine

.. code-block:: text

   ┌────────────────────────────────────────────────────────────┐
   │             LABEL VALIDITY MONITOR (per label)             │
   │                                                            │
   │  INIT ──first valid word──► VALID                          │
   │          ◄──────────────────────  ◄── word within timeout  │
   │  VALID ──timeout exceeded──► STALE                         │
   │  VALID ──SSM = NCD/FW──────► INVALID                       │
   │  STALE ──valid word rcvd───► VALID  (if recovery enabled)  │
   │                                                            │
   │  Outputs: data_value · validity_flag · age_counter         │
   └────────────────────────────────────────────────────────────┘

.. rubric:: Modeling Rules

+----------------------------+------------------------------------------------------------+
| Rule                       | Detail                                                     |
+============================+============================================================+
| 🕐 Frame-age counter       | Increment every execution frame; reset on fresh label.     |
|                            | Declare stale when counter > ``MAX_AGE_FRAMES``.           |
+----------------------------+------------------------------------------------------------+
| 🚦 SSM decoding            | Decode SSM field explicitly: ``00`` = FW (failure warning),|
|                            | ``01`` = NCD, ``10`` = FT (functional test), ``11`` = NO   |
|                            | (normal operation).  Only ``NO`` may drive control law.    |
+----------------------------+------------------------------------------------------------+
| 🛡️ Downstream protection   | Gate every control-law input behind a validity check;      |
|                            | use last-valid-value (LVV) hold for ≤ ``T_HOLD`` duration. |
+----------------------------+------------------------------------------------------------+
| 🔢 Scaling / BNR encoding  | Apply ARINC 429 BNR resolution formula:                    |
|                            | ``value = raw_29bit × 2^(MSB_weight - 28)``               |
|                            | Verify against ICD before integration.                     |
+----------------------------+------------------------------------------------------------+
| 📋 ICD traceability        | Every decoded label must reference the ICD document,       |
|                            | revision, and label number in the block annotation.        |
+----------------------------+------------------------------------------------------------+

----

Pattern 4 — 🛡️ Safety Monitor / Cross-Channel Comparator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

Dual/triple redundant channel comparison logic that detects disagreement between
redundant sensors or computation lanes and triggers a fault flag within the latency
budget defined by the FHA.

.. rubric:: Pattern Variants

.. rubric:: 🔵 Dual-Channel Comparator (2oo2)

.. code-block:: text

   Channel_A ─┐
              ├──► |ΔA−B| > THRESHOLD? ──YES──► DISAGREE_FLAG
   Channel_B ─┘                          │
                                        NO
                                         └──► AGREE (use average or Channel_A)

.. rubric:: 🟣 Triple-Voting Median Select (2oo3)

.. code-block:: text

   Ch_A ─┐
   Ch_B ─┼──► Sort(A,B,C) → median value ──► Control Law Input
   Ch_C ─┘
          └──► |max−min| > THRESHOLD? ──YES──► MONITOR_FLAG + log outlier

.. rubric:: Critical Modeling Rules

- Monitor computation must be in a **separate subsystem** from the control law —
  never share state variables between the monitor and the monitored function.
- Latency budget: monitor must assert flag within the time defined in the System
  Safety Assessment (SSA); model the worst-case execution path explicitly.
- All thresholds must be parametric (``Simulink.Parameter``); justify threshold
  values with reference to sensor accuracy budget from the SSA.

----

Pattern 5 — ✋ Envelope Protection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

Hard and soft envelope protection that prevents the aircraft from exceeding
structural, aerodynamic, or operating limits — e.g. AOA protection, load-factor
(Nz) protection, bank-angle protection, pitch-attitude protection.

.. rubric:: State Logic

.. code-block:: text

   ┌─────────────────────────────────────────────────────────┐
   │              ENVELOPE PROTECTION BLOCK                  │
   │                                                         │
   │  Measured_AOA ──► AOA_PROTECTION subsystem              │
   │                                                         │
   │  Soft Zone: α_warn ≤ α < α_max                          │
   │    → Stick force gradient increases (haptic cue)        │
   │    → Pitch-up authority reduced                         │
   │                                                         │
   │  Hard Zone: α ≥ α_max                                   │
   │    → Control law overrides pilot input                  │
   │    → Pitch-down command injected                        │
   │    → PROT_ACTIVE status broadcast on ARINC 429          │
   │                                                         │
   │  Recovery: α < α_warn − HYSTERESIS for T_RECOV          │
   │    → Protection deactivated; pilot authority restored   │
   └─────────────────────────────────────────────────────────┘

.. rubric:: ⚠️  Hazard-Linked Test Obligations

+-----------------------------------+------------------------------------------------+
| FHA Hazard                        | Required MIL Test Scenario                     |
+===================================+================================================+
| Unintended protection activation  | Nominal manoeuvre — assert protection = OFF    |
+-----------------------------------+------------------------------------------------+
| Failure to activate at limit      | Ramp α to α_max — assert protection activates  |
|                                   | before structural limit                         |
+-----------------------------------+------------------------------------------------+
| Oscillatory protection (hunting)  | Simulate α near threshold with noise — assert  |
|                                   | hysteresis prevents chattering                 |
+-----------------------------------+------------------------------------------------+
| Protection stuck active           | Recovery scenario — assert pilot authority     |
|                                   | restored within T_RECOV                        |
+-----------------------------------+------------------------------------------------+

----

Pattern 6 — ⏱️  Rate Limiter & Actuator Saturation Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

First-order actuator dynamics — position limit, rate limit, and back-EMF / hydraulic
pressure saturation — which are critical for stability analysis and PIO
(Pilot-Induced Oscillation) assessment.

.. rubric:: Model Structure

.. code-block:: text

   Commanded_δ ──► [Rate Limiter] ──► [Position Clamp] ──► [1st-order lag] ──► Actual_δ
                   max: +δ̇_max            ± δ_max          τ = 1/(2π·f_act)
                   min: −δ̇_max

.. rubric:: Key Modeling Rules

- Rate limit and position limit values must be requirement parameters, **not** hard-coded.
- Include a ``SATURATED`` status output; the control law must detect saturation and
  invoke anti-windup logic.
- Verify actuator model fidelity against hardware datasheet or test rig data before
  using in flight-envelope simulation.
- At MIL phase: test command profiles that deliberately drive saturation to confirm
  anti-windup prevents integrator wind-up and position overshoot.

----

Pattern 7 — 🔁 Discrete-Event Reconfiguration Pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

Automatic reconfiguration of sensor sources on fault detection — for example,
switching from primary ADC to secondary ADC after a disagree flag, or switching
autopilot engagement from Lane 1 to Lane 2.

.. rubric:: Reconfiguration State Machine Skeleton

.. code-block:: text

   ┌──────────────────────────────────────────────────────────────┐
   │            SOURCE SELECTION / RECONFIG MANAGER               │
   │                                                              │
   │  State: PRIMARY_ACTIVE                                       │
   │    → Monitor: disagree_flag | data_stale | BIT_fail          │
   │    → Transition: ──any flag──► SECONDARY_ACTIVE              │
   │                                                              │
   │  State: SECONDARY_ACTIVE                                     │
   │    → Monitor: secondary_health                               │
   │    → Transition: ──secondary_fail──► DEGRADED_MODE           │
   │                                                              │
   │  State: DEGRADED_MODE                                        │
   │    → Alert crew (ECAM / CAS message)                         │
   │    → Restrict flight envelope (speed / manoeuvre limits)     │
   └──────────────────────────────────────────────────────────────┘

.. rubric:: ⚠️  Critical Requirements

- Reconfiguration must be **monotonic** — no spontaneous reversion to PRIMARY_ACTIVE
  without ground maintenance reset (prevents fault masking).
- Latency from fault detection to source switch must satisfy FHA latency budget.
- Reconfiguration event must be time-stamped and logged to the Flight Data Recorder
  bus (ARINC 717 or equivalent).

----

⚖️  Domain Constraints
----------------------

.. warning::
   ⚠️  Every modeling pattern applied in this domain must satisfy the constraints
   below — they are **DER-observable** and form the basis of SOI-2 model review.

+--------------------------+------------------------------------------------------------+
| Constraint               | Detail                                                     |
+==========================+============================================================+
| 📜 Compliance baseline   | DO-178C / DO-254 + DO-331 + ARP4754A / ARP4761            |
+--------------------------+------------------------------------------------------------+
| ☠️  Key hazard profile    | Loss of control authority · Unstable mode transition ·     |
|                          | Stale avionics data · Latent sensor disagreement           |
+--------------------------+------------------------------------------------------------+
| 🔌 Interface landscape   | ARINC 429 · ARINC 664 (AFDX) · Discrete I/O               |
+--------------------------+------------------------------------------------------------+
| 🎛️  Model coverage        | DO-331 requires model-level MC/DC coverage evidence        |
|                          | in addition to (not instead of) source-code coverage.      |
+--------------------------+------------------------------------------------------------+
| 📐 Modelling standard    | All blocks must comply with MAAB (MathWorks Automotive     |
|                          | Advisory Board) or equivalent internal modelling guideline.|
+--------------------------+------------------------------------------------------------+

----

🧪 Domain-Specific Test Scenarios
----------------------------------

.. rubric:: 🟢 Nominal Scenario

Stable Normal Law flight-control mode tracking with realistic atmospheric disturbances
(Dryden turbulence, fixed seed).  All ARINC 429 labels in range; SSM = NO.  Expected:
attitude error < ±0.5°, no mode transition, no monitor flag asserted.

.. rubric:: 🟡 Boundary Scenario

High-workload pitch manoeuvre pushing AOA to ``α_warn − 1°``.  Gain scheduling
transitions through two adjacent table break-points.  Expected: soft-zone protection
entry cue asserted, no hard-protection activation, no PIO tendency.

.. rubric:: 🔴 Fault Scenario

Simultaneous ARINC 429 label stale (ADC-1 timeout) and SSM = NCD on the redundant
channel.  Expected: cross-channel monitor asserts ``DISAGREE`` within 100 ms;
reconfiguration manager switches to ``DEGRADED_MODE``; ECAM alert generated;
control law falls back to Direct Law with crew alert.

----

✅  Patterns — What Works
--------------------------

.. tip::
   💡 Patterns validated against DER review records and ARP4754A compliance checklists.

1. **🔗 Requirement-first pattern selection** — choose a modeling pattern only after
   identifying which system requirement it satisfies; never add complexity for realism alone.

2. **🏷️  Parametric everything** — every threshold, limit, gain, and timeout as a
   ``Simulink.Parameter`` with a CI-controlled value file; hard-coded numbers are a
   compliance finding.

3. **🧩 Subsystem isolation** — every pattern lives in its own atomic subsystem with
   clearly defined inputs, outputs, and a bus object type; no cross-subsystem direct
   signal wiring.

4. **📘 Block annotation** — each non-trivial block carries an annotation linking it
   to its requirement ID, the pattern category, and the last review date.

5. **🔁 Deterministic execution** — all random inputs (turbulence, noise) use a fixed
   seed stored as a ``Simulink.Parameter``; re-run must be bit-for-bit identical.

----

🚫 Anti-Patterns — What Breaks Model Reviews
---------------------------------------------

.. danger::
   ❌ These are the most common model-review rejections in aerospace programs.

- 🚩 Implicit mode transitions with no guard condition documented.
- 🚩 Magic numbers in gain tables — DER will require justification for every value.
- 🚩 Safety monitors sharing state with the monitored function (defeats independence).
- 🚩 Parallel signal paths with inconsistent data types or sample rates.
- 🚩 Missing ``SATURATED`` / ``INVALID`` status outputs on bus interface blocks.
- 🚩 Model structural coverage untested — DO-331 requires model-level MC/DC evidence.
- 🚩 Reconfiguration logic that allows reversion without maintenance action.

----

⚠️  Pitfalls
------------

.. caution::

   Subtle issues that pass informal review but fail formal SOI-2 model inspection:

   - 🕳️  **Undocumented implicit ordering** — Simulink evaluates subsystems in
     topological order; if execution order is not explicit, timing anomalies appear
     only in code generation, not at model level.
   - 🕳️  **Fixed-point overflow in gain scheduling** — BNR scaling applied before
     fixed-point quantisation can cause silent saturation at extreme envelope corners.
   - 🕳️  **SSM decoded as boolean** — collapsing ``NCD``, ``FW``, ``FT`` into a
     single ``invalid`` boolean loses information needed by the monitor logic.
   - 🕳️  **Hysteresis parameter not requirement-linked** — protection hysteresis values
     require a safety justification traced to the SSA; "chosen by test" is not acceptable.
   - 🕳️  **Reconfiguration latency untested** — the model may switch correctly in
     steady state but exceed the FHA latency budget under high computational load.

----

🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🏷️
     - Tag every subsystem with the Pattern ID (e.g. ``PAT-04-MODE``, ``PAT-04-MONITOR``).
   * - 📐
     - Enforce MAAB / DO-331 modelling guidelines via ``modeladvisor`` check on every commit.
   * - 🔒
     - Protect all parameter files with CI hash; reject runs with hash mismatch.
   * - 🗂️
     - Maintain a **Model Architecture Document (MAD)** that maps each subsystem to its
       ARP4754A allocation and DO-178C software component.
   * - 🧬
     - Run Simulink Design Verifier (SDV) for reachability and dead-logic checks as a
       supplement to manual review — flag all unreachable states for justification.
   * - 📊
     - Capture model-level coverage (Simulink Coverage) alongside source-code coverage;
       gaps at model level predict gaps at code level.

----

🔮 Heuristics
-------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| Mode transition fires unexpectedly            | Check guard condition for implicit priority  |
|                                               | or missing inhibit condition.                |
+-----------------------------------------------+----------------------------------------------+
| Gain table boundary test fails                | Verify break-point alignment and BNR         |
|                                               | quantisation; recheck ICD scaling formula.   |
+-----------------------------------------------+----------------------------------------------+
| Monitor asserts spuriously at startup         | Add ``INIT`` state to debounce first frame;  |
|                                               | document in Requirements.                    |
+-----------------------------------------------+----------------------------------------------+
| Coverage hole in protection logic             | Add explicit test for hysteresis band; check |
|                                               | both entry and exit conditions independently.|
+-----------------------------------------------+----------------------------------------------+
| Reconfiguration test flaky between runs       | Fix random seed; check for timing dependency |
|                                               | on host OS scheduler jitter.                 |
+-----------------------------------------------+----------------------------------------------+

----

📋 Pre-Closure Checklist
------------------------

.. rubric:: Gate: Must be 100 % complete before model baseline is submitted for SOI-2

- ☐ All seven domain modeling patterns applied where required are tagged in the model.
- ☐ Every pattern has ≥1 nominal, ≥1 boundary, and ≥1 fault-scenario test case.
- ☐ All model parameters are ``Simulink.Parameter`` objects with CI-controlled values.
- ☐ ``modeladvisor`` check passes with zero errors against MAAB / DO-331 profile.
- ☐ Simulink Coverage report shows ≥ 100 % decision coverage at model level.
- ☐ Safety monitors are in independent subsystems; independence justified in MAD.
- ☐ All ARINC 429 / AFDX label SSM fields decoded explicitly (no boolean collapse).
- ☐ Reconfiguration latency verified against FHA latency budget in test log.
- ☐ Model Architecture Document (MAD) updated and peer-reviewed.
- ☐ Residual risks identified, assigned, and tracked to closure.

----

🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard / Reference
     - Relevance to Domain Modeling Patterns
   * - **DO-178C**
     - Software V&V objectives; MC/DC coverage at source-code level.
   * - **DO-331**
     - MBDV supplement — model coverage, model traceability, and model-based test requirements.
   * - **ARP4754A**
     - System development process; allocates functions to items; defines DAL.
   * - **ARP4761**
     - FHA / FMEA / FTA methods; source of hazard thresholds and latency budgets.
   * - **ARINC 429**
     - Digital information transfer; BNR encoding; SSM definitions; label allocation.
   * - **ARINC 664 Pt. 7**
     - AFDX Virtual Link configuration; BAG / SKEWmax timing parameters.
   * - **MAAB Control Algorithm Modeling Guidelines**
     - Simulink / Stateflow modeling conventions for safety-critical software.

----

.. admonition:: 🚀  Remember

   In aerospace domain modeling, **the pattern IS the argument**.  Choosing the right
   pattern — hierarchical state machine for mode logic, explicit SSM decoding for bus
   interfaces, independent monitors for cross-channel comparison — tells the DER
   exactly how your design handles failures before they reach the hardware.
   Document your pattern choices; they are certification evidence.
