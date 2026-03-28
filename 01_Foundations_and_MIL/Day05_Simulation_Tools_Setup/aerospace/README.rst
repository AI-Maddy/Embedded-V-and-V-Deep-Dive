✈️  Aerospace Focus — Day 05: Simulation Tools Setup
=====================================================

.. image:: https://img.shields.io/badge/Phase-MIL-blue
   :alt: Phase: MIL

.. image:: https://img.shields.io/badge/Standard-DO--178C%20%2F%20ARP4754A-critical
   :alt: Standard: DO-178C / ARP4754A

.. image:: https://img.shields.io/badge/Criticality-DAL--A%2FB-red
   :alt: Criticality: DAL-A/B

.. note::
   🛡️ **Safety-Critical Context** — Every artifact produced in this section must be
   traceable to a hazard-linked requirement. Unsupported claims are not acceptable
   as evidence under DO-178C or ARP4754A reviews.

----

🎯 Objective
------------
Configure and validate **aerospace-grade simulation toolchains** for Model-in-the-Loop
(MIL) execution.  The goal is tool qualification evidence, repeatable execution
environments, and compliance-ready output artifacts.

Apply this day in **Aerospace** context with explicit safety, compliance, and
evidence expectations.

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
     - Aerospace verification workflow
   * - 📋 **Lifecycle Standard**
     - ARP4754A System Development Process
   * - 💾 **Software Standard**
     - DO-178C (DAL-A/B applicable)

----

🛠️  Aerospace Simulation Tools Landscape
-----------------------------------------

.. note::
   🔑 **DO-330 Reminder** — Every tool that produces, transforms, or verifies
   certification evidence must be assessed for Tool Qualification Level (TQL).
   The table below lists the typical TQL for each tool category.

The Day-05 setup task spans **five tool layers**.  All five must be configured,
version-locked, and cross-validated before a single MIL run is used as evidence.

.. rubric:: 🗂️  Tool Layer Overview

.. list-table::
   :widths: 5 25 30 20 20
   :header-rows: 1

   * - #
     - Layer
     - Purpose
     - Example Tools
     - DO-330 TQL
   * - 1
     - 🏗️ Modelling Environment
     - Block-diagram / dataflow modelling of controller + plant
     - MATLAB/Simulink, Ansys SCADE Suite
     - TQL-5 (model only); TQL-1 if generating qualified code
   * - 2
     - ✈️ Flight Dynamics / Plant
     - High-fidelity aerodynamic plant model for closed-loop MIL
     - JSBSim, FlightGear FDM, X-Plane SDK, OpenFlight
     - TQL-5 (stimulus source, not output generator)
   * - 3
     - 🔌 Avionics Bus Simulation
     - ARINC 429 / AFDX / MIL-STD-1553 stimulus and monitoring
     - Ballard ARINC, AIM GmbH AFDX Analyzer, DDC BU-65590
     - TQL-5; TQL-3 if bus replay drives coverage decisions
   * - 4
     - 🔬 Verification & Coverage
     - Structural coverage (MC/DC), static analysis, test execution
     - VectorCAST, LDRA Testbed, Polyspace, Cantata++, Reactis
     - TQL-1 (DAL-A/B coverage tools must be fully qualified)
   * - 5
     - 🤖 Test Automation & Reporting
     - Scripted MIL execution, regression, evidence packaging
     - RT-Tester, TPT (PikeTec), pytest + MATLAB Engine API
     - TQL-3 (automation drives output but not coverage data)

----

🏗️  Layer 1 — Modelling Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: MATLAB / Simulink (MathWorks)

The industry-standard block-diagram environment for flight-control MIL.

+----------------------------+-------------------------------------------------------------+
| Aspect                     | Detail                                                      |
+============================+=============================================================+
| 📦 Relevant toolboxes      | Simulink · Aerospace Blockset · Simulink Design Verifier ·  |
|                            | Simulink Requirements · Simulink Coverage · Embedded Coder  |
+----------------------------+-------------------------------------------------------------+
| 🔧 Setup steps             | 1. Install via MathWorks license server (version-locked).   |
|                            | 2. Enable ``slprj/`` build artefact capture in SLX project. |
|                            | 3. Configure ``sl_customization.m`` for company standards.  |
|                            | 4. Validate environment with ``sldemo_f14`` smoke test.     |
+----------------------------+-------------------------------------------------------------+
| ⚠️  DO-178C gotcha         | Simulink Design Verifier results are **not** a substitute   |
|                            | for structural coverage data from qualified execution.      |
+----------------------------+-------------------------------------------------------------+
| 📜 Qualification path      | DO-330 TQL-1 via MathWorks IEC Certification Kit + DO       |
|                            | Qualification Kit (requires separate purchase + SOI review).|
+----------------------------+-------------------------------------------------------------+
| 🔗 Version control         | Use ``.slx`` binary diff with ``matlab.unittest`` CI hooks. |
+----------------------------+-------------------------------------------------------------+

.. rubric:: Ansys SCADE Suite

Formally-proven synchronous dataflow environment targeting DAL-A avionics software.

+----------------------------+-------------------------------------------------------------+
| Aspect                     | Detail                                                      |
+============================+=============================================================+
| 📦 Modules                 | SCADE Suite · SCADE Display · SCADE Test · KCG code gen     |
+----------------------------+-------------------------------------------------------------+
| 🔧 Setup steps             | 1. Install with avionics profile; lock KCG version in CI.   |
|                            | 2. Configure qualification data package (QDP) path.         |
|                            | 3. Validate via official Ansys DO-178C QDP smoke test.      |
+----------------------------+-------------------------------------------------------------+
| ✅ Advantage               | KCG code generator ships with a pre-qualified DO-330 TQL-1  |
|                            | data package accepted by major certification authorities.   |
+----------------------------+-------------------------------------------------------------+
| ⚠️  Pitfall                | SCADE model tests do **not** automatically satisfy MC/DC    |
|                            | at source-code level — still need LDRA/VectorCAST on KCG    |
|                            | output if structural coverage is explicitly required.       |
+----------------------------+-------------------------------------------------------------+

----

✈️  Layer 2 — Flight Dynamics / Plant Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aerospace MIL requires a high-fidelity aerodynamic environment to close the loop
around the Flight Control System (FCS) model.

.. rubric:: JSBSim

Open-source, multi-platform flight dynamics model (FDM) used in UAV and GA aircraft
certification simulation environments.

- **Interface:** C++ API, Python bindings (``jsbsim`` PyPI package), Simulink S-Function wrapper.
- **Aircraft configs:** XML-based aerodynamic coefficient tables (CLα, CDβ, CMq …).
- **MIL integration:** wrap as a Simulink S-Function or call via co-simulation bus.
- **⚠️  TQL note:** JSBSim itself is TQL-5; validate accuracy against flight-test data
  before claiming it supports a qualification argument.

.. rubric:: FlightGear Flight Dynamics Model (FDM)

Open-source simulator with JSBSim or YASim FDMs.  Useful for pilot-in-the-loop (PIL)
closed-loop scenarios and visualisation during MIL runs.

- **Interface:** FlightGear Generic Protocol (UDP), FGNetFDM struct, or JSBSim direct.
- **MIL integration:** pipe FCS model outputs to FG over loopback UDP; log state vector.
- **⚠️  Gotcha:** FlightGear rendering adds non-deterministic latency — disable it
  (``--fdm=null --fog-fastest``) for headless regression runs.

.. rubric:: Simulink Aerospace Blockset

MathWorks-native 6-DOF equations of motion, atmosphere models (ISA, US76), and
actuator / sensor models tightly integrated in a Simulink diagram.

- **Key blocks:** ``6DOF (Euler Angles)`` · ``COESA Atmosphere Model`` ·
  ``Dryden Wind Turbulence`` · ``Discrete Wind Gust Model``
- **⚠️  Pitfall:** Default Dryden turbulence uses a random seed — always fix the seed
  in the model workspace for deterministic regression.

----

🔌  Layer 3 — Avionics Bus Simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ARINC 429 / AFDX bus simulation is essential for aerospace MIL because the flight
computer communicates exclusively over certified data buses.

.. rubric:: Ballard Technology ARINC 429 / MIL-STD-1553

Hardware-in-the-loop and pure-software ARINC 429 simulation cards and APIs.

+------------------------+-------------------------------------------------------------------+
| Feature                | Detail                                                            |
+========================+===================================================================+
| Bus protocols          | ARINC 429 · MIL-STD-1553 B · ARINC 717                           |
+------------------------+-------------------------------------------------------------------+
| Software interface     | BTI DLL/API (Windows) · LabVIEW driver · MATLAB MEX wrapper       |
+------------------------+-------------------------------------------------------------------+
| MIL usage              | Inject ARINC 429 label sequences as plant outputs; monitor        |
|                        | FCS command bus labels for FCS output verification.               |
+------------------------+-------------------------------------------------------------------+
| ⚠️  Timing note        | ARINC 429 word rate is 12.5 kbps (low-speed) or 100 kbps;        |
|                        | verify simulation timestep is ≤ one word period.                  |
+------------------------+-------------------------------------------------------------------+

.. rubric:: AIM GmbH — AFDX / ARINC 664 Analyzer

Software-only AFDX network emulator widely used in commercial aircraft MIL/SIL.

- **Capabilities:** Virtual Link (VL) configuration, BAG enforcement, jitter injection,
  end-system frame capture.
- **Tools:** AIM AFDX Configurator + AFDX Analyzer (Wireshark plugin variant).
- **MIL integration:** Run AFDX emulator as a co-process; stimulate FCS model over
  loopback Ethernet with VL-constrained frames.
- **⚠️  Gotcha:** BAG timer resolution is 1 ms; ensure host OS timer resolution is
  set to ≤ 1 ms (``timeBeginPeriod(1)`` on Windows; ``PREEMPT_RT`` patch on Linux).

.. rubric:: DDC (Data Device Corporation) — BU-65590 / BU-67118

Industry-standard 1553 and ARINC 429 PMC/PCI cards with certified API.

- **Relevant for:** legacy military avionics (MIL-STD-1553B) simulation scenarios.
- **Python API:** ``bcTestNode`` example via NAIBRD SDK.

----

🔬  Layer 4 — Verification & Coverage Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: VectorCAST / C++ (Vector Informatik)

Automated unit and integration test framework with DO-178C MC/DC coverage reporting.

+----------------------------+-------------------------------------------------------------+
| Aspect                     | Detail                                                      |
+============================+=============================================================+
| 📋 Qualification            | Certified TQL-1 data package available for DO-178C DAL-A/B  |
+----------------------------+-------------------------------------------------------------+
| 📊 Coverage types           | Statement · Branch · MC/DC · Function call                  |
+----------------------------+-------------------------------------------------------------+
| 🔧 MIL link                 | Import Simulink code-gen output (``ert_main.c``) as a       |
|                            | VectorCAST component; map Simulink test cases to VC scripts.|
+----------------------------+-------------------------------------------------------------+
| ⚠️  Pitfall                 | Coverage holes in generated code are often in               |
|                            | ``rtwtypes.h`` cast macros — exclude with documented        |
|                            | deactivated code justification.                             |
+----------------------------+-------------------------------------------------------------+

.. rubric:: LDRA Testbed

Long-established static + dynamic analysis suite used by avionics OEMs for DO-178C
objective satisfaction (Objectives 4, 5, 6 coverage + data coupling).

- **Key features:** MISRA C:2012 checking · data/control coupling analysis · test
  case management · CI integration via Jenkins plugin.
- **TQL-1** qualification kit available for DAL-A programs.

.. rubric:: Polyspace Bug Finder / Code Prover (MathWorks)

Formal static analysis tool; Code Prover can **prove absence** of certain run-time
errors (division-by-zero, overflow, NULL deref) — accepted as analysis evidence
under DO-178C Table A-7 objectives.

- **⚠️  Note:** Polyspace results supplement but do **not** replace structural coverage.
- **Integration:** Run as post-build step; pipe Orange/Red findings to JIRA for triage.

.. rubric:: Reactis (Reactive Systems)

Model-based test generation and coverage measurement directly on Simulink/Stateflow
models — generates test vectors that exercise condition/decision coverage at the
model level.

- **MIL role:** Generate model-level MC/DC test vectors automatically; replay on
  compiled code to confirm coverage transfers.
- **TQL:** TQL-1 qualification data package available.

----

🤖  Layer 5 — Test Automation & Reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: RT-Tester (Verified Systems International)

Platform-independent test automation tool designed specifically for DO-178C and
EN 50128 SIL-4; widely used in Airbus, Boeing, and Embraer programs.

- **Capabilities:** Time-triggered test scripts · TTCN-3 test suite import · hardware
  abstraction layer for HIL transition · automated verdict generation.
- **MIL integration:** Drive Simulink model via MATLAB Engine API; collect verdict
  and evidence in RT-Tester report format accepted by DERs.

.. rubric:: TPT — Time Partition Testing (PikeTec)

Graphical test modelling tool for embedded control software; especially strong for
time-series-based signal assertions.

+---------------------------+--------------------------------------------------------------+
| Feature                   | Detail                                                       |
+===========================+==============================================================+
| Test modelling            | State-machine-based test cases with signal stimuli + checks  |
+---------------------------+--------------------------------------------------------------+
| Simulink integration      | Direct SL block interface — no code generation required      |
+---------------------------+--------------------------------------------------------------+
| Reporting                 | HTML + PDF report with requirement traceability table        |
+---------------------------+--------------------------------------------------------------+
| DO-178C support           | Qualification kit targeting DAL-A; TQL-1 certificate        |
+---------------------------+--------------------------------------------------------------+

.. rubric:: pytest + MATLAB Engine API (Open-Source Stack)

Lightweight, CI-friendly alternative for teams that cannot afford commercial TQL-1
tools at the MIL phase (qualification is still required before SIL use as evidence).

.. code-block:: python

   # Example: headless Simulink MIL run from pytest
   import matlab.engine, pytest

   @pytest.fixture(scope="session")
   def eng():
       e = matlab.engine.start_matlab()
       e.addpath("models/FCS", nargout=0)
       yield e
       e.quit()

   def test_fcs_nominal_tracking(eng):
       eng.workspace["scenario"] = "NOM_01"
       eng.sim("FCS_MIL_Harness", nargout=0)
       pitch_err = eng.workspace["pitch_error_rms"]
       assert pitch_err < 0.5, f"Pitch RMS {pitch_err:.3f}° exceeds 0.5° threshold"

- **⚠️  TQL warning:** This stack is **not** qualified; all MIL results produced with
  it are engineering data only until the stack is assessed per DO-330.

----

🧲  Tool Integration Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following shows how the five layers connect for a typical aerospace MIL run:

.. code-block:: text

   ┌────────────────────────────────────────────────────────────────┐
   │               Aerospace MIL Toolchain — Data Flow              │
   ├──────────────────┬─────────────────────────────────────────────┤
   │  Requirements    │  DOORS NG / JAMA → Simulink Requirements     │
   │  (Layer 0)       │  (bidirectional traceability links)          │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  Plant FDM       │  JSBSim / Aerospace Blockset → Simulink      │
   │  (Layer 2)       │  S-Function (6-DOF state vector inputs)      │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  Bus Stimulus    │  Ballard/AIM → loopback → Simulink bus       │
   │  (Layer 3)       │  input blocks (ARINC 429 label stream)       │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  FCS Model       │  Simulink / SCADE controller block           │
   │  (Layer 1)       │  (DAL-A algorithm under test)                │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  Coverage Engine │  VectorCAST / LDRA / Reactis                 │
   │  (Layer 4)       │  (MC/DC data collected per run)              │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  Automation      │  RT-Tester / TPT / pytest orchestration      │
   │  (Layer 5)       │  → evidence package (logs + verdicts + VCRI) │
   └──────────────────┴─────────────────────────────────────────────┘

----

🔧  Tool Setup Quick-Start Checklist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before executing the first MIL run, verify all of the following:

- ☐ **MATLAB/Simulink** version pinned in ``environment.lock`` (e.g. ``R2025a``).
- ☐ **Aerospace Blockset & Simulink Coverage** toolboxes installed and license-checked.
- ☐ **JSBSim** XML aircraft definition validated against published aerodynamic data.
- ☐ **ARINC 429 bus timing** confirmed: word rate, label set, and SSM encoding.
- ☐ **VectorCAST / LDRA** TQL data package version matches tool version in CI.
- ☐ **RT-Tester / TPT** script parameter file committed to version control.
- ☐ Tool configuration snapshot (hash) captured in the Configuration Index (CI).
- ☐ Smoke test ``sldemo_f14`` (or equivalent) passes with zero warnings on current host.
- ☐ All tool outputs directed to ``evidence/YYYY-MM-DD_run-NNN/`` folder structure.
- ☐ Independent reviewer has signed off on tool setup record before evidence runs begin.

----

⚖️  Domain Constraints
----------------------

.. warning::
   ⚠️  Violating any constraint below is a **DER finding** and will block SOI audits.

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
| 🕹️  Simulation scope      | Full-envelope plant model + avionics bus stimulus          |
+--------------------------+------------------------------------------------------------+
| 📂 Tool qualification    | TQL-5 minimum; TQL-1 for coverage measurement tools        |
+--------------------------+------------------------------------------------------------+

----

🧪 Domain-Specific Test Scenarios
----------------------------------

.. rubric:: 🟢 Nominal Scenario

Stable flight-control mode tracking with expected atmospheric disturbances.
Controller must maintain commanded attitude within ±0.5° over a full manoeuvre cycle.

.. rubric:: 🟡 Boundary Scenario

High-workload transition envelope near stability margins (e.g. approach to stall
boundary with envelope-protection logic active).  Acceptance: protection engages
before exceedance, no oscillatory divergence.

.. rubric:: 🔴 Fault Scenario

ARINC 429 bus label corruption combined with an independent sensor disagreement
event.  Expected: cross-channel monitor flags mismatch within 100 ms; control law
reverts to secondary mode without loss of positive control.

----

✅  Patterns — What Works
--------------------------

.. tip::
   💡 These patterns have been validated against DO-178C Stage-of-Involvement (SOI)
   checklists and ARP4754A development assurance reviews.

1. **🔗 Hazard-linked thresholds** — derive every acceptance threshold directly from
   the Functional Hazard Assessment (FHA); reference the FHA item ID in the test case.

2. **⏱️  Explicit timing contracts** — document bus timing (e.g. ARINC 429 word-rate
   100 words/s, latency ≤ 5 ms) as a first-class requirement, not as a footnote.

3. **📊 Baseline comparison** — compare nominal *and* stressed traces against the same
   golden baseline to surface regression across environmental changes.

4. **🗂️  Evidence packaging** — co-locate raw logs, analysis scripts, and verdict
   rationale in a single traceable artifact package.

5. **🤖 Automated regression** — script MIL execution so the full test suite can be
   re-run in under 10 minutes on any qualified workstation.

----

🚫 Anti-Patterns — What Breaks Audits
--------------------------------------

.. danger::
   ❌ The items below are the most common reasons aerospace DER reviews are **rejected**.

- 🚩 Generic test claims ("controller is stable") without explicit hazard mapping.
- 🚩 Pass/fail decisions without quantitative thresholds referenced to requirements.
- 🚩 Evidence summaries that omit raw artifact references (log files, MAT files, etc.).
- 🚩 Simulation environment differences between initial run and regression run.
- 🚩 Tool version mismatches not captured in the Configuration Index (CI).

----

⚠️  Pitfalls
------------

.. caution::

   Watch for these subtle failure modes that survive internal review but fail SOI:

   - 🕳️  **Hidden calibration assumptions** — environment constants hard-coded in the
     model instead of injected through a qualified parameter set.
   - 🕳️  **Missing negative-path coverage** — every HIGH/CATASTROPHIC hazard needs
     at least one explicitly failed-state scenario with measured recovery behaviour.
   - 🕳️  **Broken traceability chains** — a requirement that traces to a test but the
     test does not trace back to a verification result is a gap, even if the test passes.
   - 🕳️  **Float precision drift** — parameter rounding across tool boundaries can
     introduce sub-LSB errors that accumulate into mode-transition timing issues.

----

🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🏷️
     - Tag **every artifact** with domain requirement IDs (e.g. ``FCS-SYS-REQ-042``).
   * - ⏩
     - Capture timing **and** functional evidence in the same run package.
   * - 📝
     - Record residual risk and ownership **before** closure, not as a post-audit action.
   * - 🔒
     - Lock tool versions in a CI-controlled environment file; never allow ad-hoc upgrades
       mid-campaign.
   * - 🧬
     - Use deterministic simulation seeds so any run can be bit-for-bit reproduced.
   * - 🗺️
     - Maintain a living Verification Cross-Reference Index (VCRI) updated after every run.

----

🔮 Heuristics
-------------

+---------------------------------------------+----------------------------------------------+
| Situation                                   | 💡 Action                                    |
+=============================================+==============================================+
| A domain hazard has no linked test case     | Confidence is **provisional** — block sign-off|
+---------------------------------------------+----------------------------------------------+
| Re-run produces unexpected difference       | Investigate **determinism** before re-testing |
+---------------------------------------------+----------------------------------------------+
| Evidence is indirect or inferred            | **Reduce** verdict confidence level; document |
+---------------------------------------------+----------------------------------------------+
| Coverage metric is near threshold           | Add targeted tests; do **not** widen threshold|
+---------------------------------------------+----------------------------------------------+
| Schedule pressure to skip fault scenarios   | Escalate — fault scenarios are **non-optional**|
+---------------------------------------------+----------------------------------------------+

----

📋 Pre-Closure Checklist
------------------------

.. rubric:: Gate: Must be 100 % complete before evidence package is submitted

- ☐ Domain hazard coverage is **explicit** — every FHA item has ≥1 linked test case.
- ☐ Compliance references (DO-178C objectives, ARP4754A DAL) are mapped to evidence.
- ☐ Nominal / boundary / fault results are **all documented** with pass/fail verdict.
- ☐ Residual risks and next actions are **assigned** to named owners with due dates.
- ☐ Tool qualification records (TQL level + version) are included in evidence package.
- ☐ Simulation environment (OS, compiler, model version) is captured in the CI.
- ☐ VCRI is updated and reviewed by independent verification engineer.

----

🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance
   * - **DO-178C**
     - Software Considerations in Airborne Systems — primary software V&V standard.
   * - **DO-254**
     - Design Assurance Guidance for Airborne Electronic Hardware.
   * - **ARP4754A**
     - Guidelines for Development of Civil Aircraft and Systems.
   * - **ARP4761**
     - Guidelines and Methods for Safety Assessment Process.
   * - **DO-330**
     - Software Tool Qualification Considerations — governs MIL tool qualification.
   * - **DO-331**
     - Model-Based Development and Verification Supplement to DO-178C.

----

.. admonition:: 🚀  Remember

   In aerospace V&V, **the evidence IS the product**.  A perfect model with
   incomplete, untraceable, or non-reproducible evidence is worthless at
   certification.  Build the evidence pipeline before you build the test cases.
