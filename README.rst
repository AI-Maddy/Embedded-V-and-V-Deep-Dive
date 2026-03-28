Embedded V&V Deep Dive
======================

Repository Purpose
------------------

This repository provides a **deep, applied verification and validation curriculum** for
**MIL → SIL → HIL** across automotive, aerospace, and medical embedded systems.

Each of the 30 days produces **requirement-linked, review-ready evidence** following the
VERITAS framework: Verification, Evidence, Requirements, Intent, Traceability, Artifact, Standards.

Navigation Map
--------------

Foundations and MIL — Day01–Day10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Phase emphasis: model behavior realism, requirement intent, early defect discovery.*

- `01_Foundations_and_MIL/Day01_VModel_and_Requirements <01_Foundations_and_MIL/Day01_VModel_and_Requirements>`_ — V-model lifecycle, requirement decomposition
- `Day02 Traceability and Test Design <01_Foundations_and_MIL/Day02_Traceability_and_TestDesign>`_ — requirement-to-test traceability, test design patterns
- `Day03 Plant and Controller Modeling <01_Foundations_and_MIL/Day03_Plant_and_Controller_Modeling>`_ — physical plant models, PID/state-space controllers
- `Day04 Domain Modeling Patterns <01_Foundations_and_MIL/Day04_Domain_Modeling_Patterns>`_ — automotive, aerospace, and medical model idioms
- `Day05 Simulation Tools Setup <01_Foundations_and_MIL/Day05_Simulation_Tools_Setup>`_ — MATLAB/Simulink, OpenModelica, Python scripting
- `Day06 MIL Execution <01_Foundations_and_MIL/Day06_MIL_Execution>`_ — scenario execution, artifact capture, verdict recording
- `Day07 Closed-Loop Simulation <01_Foundations_and_MIL/Day07_ClosedLoop_Simulation>`_ — plant-in-the-loop, disturbance rejection
- `Day08 Fault Injection in MIL <01_Foundations_and_MIL/Day08_FaultInjection_in_MIL>`_ — sensor dropout, signal corruption, recovery paths
- `Day09 MIL Automation <01_Foundations_and_MIL/Day09_MIL_Automation>`_ — pytest-based batch execution, regression baselines
- `Day10 MIL Mini-Project <01_Foundations_and_MIL/Day10_MIL_MiniProject>`_ — integrated MIL evidence package per domain

SIL and Software Validation — Day11–Day20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Phase emphasis: software correctness, structural evidence, robustness under negative paths.*

- `Day11 Code Generation <02_SIL_and_Software_Validation/Day11_CodeGeneration>`_ — Embedded Coder/TargetLink output, MISRA C:2012 gate
- `Day12 SIL Setup <02_SIL_and_Software_Validation/Day12_SIL_Setup>`_ — host-based SIL harness, S-function wrapping
- `Day13 SIL Execution <02_SIL_and_Software_Validation/Day13_SIL_Execution>`_ — numerical equivalence vs model reference
- `Day14 Unit and Integration Testing <02_SIL_and_Software_Validation/Day14_Unit_and_Integration_Testing>`_ — VectorCAST/GoogleTest, interface contracts
- `Day15 Static Analysis <02_SIL_and_Software_Validation/Day15_StaticAnalysis>`_ — LDRA/Polyspace, MISRA/CERT-C rule sets
- `Day16 SIL Fault Injection <02_SIL_and_Software_Validation/Day16_SIL_FaultInjection>`_ — bit-flip, NULL pointer, stack overflow scenarios
- `Day17 Robustness and Negative Testing <02_SIL_and_Software_Validation/Day17_Robustness_and_NegativeTesting>`_ — out-of-range, wraparound, invalid-state inputs
- `Day18 Object-Code Verification DAL-A <02_SIL_and_Software_Validation/Day18_ObjectCode_Verification_DAL_A>`_ — TRACE32 PRACTICE scripts, DO-178C OC objectives
- `Day19 SIL Coverage MC/DC <02_SIL_and_Software_Validation/Day19_SIL_Coverage_MC_DC>`_ — 100% MC/DC on safety-critical functions, coverage gap triage
- `Day20 SIL Mini-Project <02_SIL_and_Software_Validation/Day20_SIL_MiniProject>`_ — integrated SIL evidence package per domain

HIL and Real-Time — Day21–Day30
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Phase emphasis: hardware realism, real-time determinism, bus/network integrity.*

- `Day21 HIL Concepts <03_HIL_and_RealTime/Day21_HIL_Concepts>`_ — HIL topology, signal conditioning, I/O mapping
- `Day22 Hardware Setup <03_HIL_and_RealTime/Day22_Hardware_Setup>`_ — dSPACE/National Instruments rig configuration
- `Day23 Real-Time I/O <03_HIL_and_RealTime/Day23_RealTime_IO>`_ — I/O latency, jitter characterization, deadline adherence
- `Day24 HIL Scripting <03_HIL_and_RealTime/Day24_HIL_Scripting>`_ — Python/ControlDesk automation, pass/fail verdict export
- `Day25 Bus and Network Analysis <03_HIL_and_RealTime/Day25_Bus_and_Network_Analysis>`_ — CAN/FlexRay/ARINC 429 message integrity
- `Day26 Execution Trace and WCET <03_HIL_and_RealTime/Day26_ExecutionTrace_and_WCET>`_ — Lauterbach TRACE32 WCET, CPU budget analysis
- `Day27 HIL Fault Injection <03_HIL_and_RealTime/Day27_HIL_FaultInjection>`_ — power-rail glitch, harness open-circuit, watchdog reset
- `Day28 Compliance Mapping <03_HIL_and_RealTime/Day28_Compliance_Mapping>`_ — DO-178C/DO-254/ISO 26262 objective-to-test traceability
- `Day29 HIL Regression and Automation <03_HIL_and_RealTime/Day29_HIL_Regression_and_Automation>`_ — nightly CI regression, trend dashboards
- `Day30 Final Capstone <03_HIL_and_RealTime/Day30_Final_Capstone>`_ — end-to-end MIL→SIL→HIL evidence package, compliance review

Learning Contract
-----------------

For every day and every domain:

1. **Explain** requirement intent and hazard context before touching tools.
2. **Execute** reproducible scenarios with explicit pass/fail thresholds.
3. **Evaluate** outcomes using objective metrics (numerical tolerance, coverage %, timing budget).
4. **Evidence** every claim with a timestamped, traceable artifact.

Standard Artifact Set
---------------------

Requirement-Linked Scenario Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 25 35 25

   * - Scenario ID
     - Type
     - Description
     - Evidence Artifact
   * - MIL-SCN-01
     - 🟢 Nominal
     - Closed-loop throttle demand 0–100 %; steady-state error < 2 % at nominal operating point
     - ``sim_log_day06_nom.csv``, response plot
   * - MIL-SCN-02
     - 🟡 Boundary
     - ADC input at ±32767 (full-scale); output clamped, no integer overflow, no saturation alarm missed
     - ``sim_log_day06_bnd.csv``, signal trace
   * - MIL-SCN-03
     - 🔴 Fault
     - Speed sensor dropout for 50 ms; limp-home mode activated within one control cycle
     - ``fault_trace_day08.csv``, verdict summary
   * - SIL-SCN-01
     - 🟢 Nominal
     - All 47 model output signals match generated C code to double-precision floating-point tolerance
     - ``sil_equiv_report_day13.html``
   * - SIL-SCN-02
     - 🟢 Nominal
     - 100 % MC/DC coverage achieved on braking-torque arbitration function (12 conditions)
     - ``coverage_report_day19.xml``
   * - SIL-SCN-03
     - 🔴 Fault
     - NULL-pointer and stack-overflow injected; safe-state reached in < 10 ms, no silent corruption
     - ``fault_log_day16.txt``, static analysis report
   * - HIL-SCN-01
     - 🟢 Nominal
     - 8 kHz control loop; interrupt latency ≤ 125 µs (80 % CPU budget), verified on target silicon
     - ``wcet_trace32_day26.pdf``
   * - HIL-SCN-02
     - 🔴 Fault
     - CAN bus error-frame injection; receiver recovers full communication within 3 message cycles
     - ``can_trace_day25.blf``, verdict table
   * - HIL-SCN-03
     - 🔴 Fault
     - 50 ms power-rail glitch; watchdog fires, ECU re-initialises cleanly in < 500 ms
     - ``hil_fault_day27.csv``, TRACE32 reset log

Timestamped Logs / Traces / Plots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All artifacts are named ``<type>_day<NN>_<domain>_<variant>.<ext>`` and stored alongside the
day folder that produced them. Every log includes: build hash, model/code version, timestamp
(ISO 8601), and the requirement IDs exercised.

Fault and Robustness Evidence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fault scenarios are documented with a four-field record:

- **Injected condition** — precise signal, duration, and magnitude
- **Expected system response** — requirement-specified safe state or recovery behaviour
- **Observed response** — timestamped measurement from log
- **Verdict** — PASS / FAIL / BLOCKED with triage note

Timing / Coverage Summaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Coverage reports exported from LDRA Testbed / VectorCAST in XML and HTML.
- WCET reports captured with Lauterbach TRACE32 PRACTICE scripts (see Day26 and Day18).
- MC/DC independence-pair tables linked to the DO-178C Table A-7 objectives (see Day19).

Compliance Mapping Notes
~~~~~~~~~~~~~~~~~~~~~~~~~

Traceability from test objective → test case → evidence artifact is maintained in the
scenario matrices inside each day folder. Day28 consolidates cross-phase coverage against
standard objectives.

Definition of Done (Per Day)
-----------------------------

☐ Scenario coverage executed as planned (all IDs in matrix have a result).

☐ Pass/fail rules applied consistently — thresholds set before execution, not after.

☐ Every finding traceable to a requirement or objective ID.

☐ Residual risks and next actions documented with owner and target date.

☐ Artifacts named, versioned, and committed alongside the day folder.

Severity / Priority Legend
---------------------------

- 🟢 **Nominal** — expected operating envelope, all safety margins satisfied
- 🟡 **Boundary** — at or near design limits; degraded-mode behaviour validated
- 🔴 **Fault** — error or failure condition; recovery path and safe-state verified

Pre-Review Checklist
--------------------

☐ All scenarios in the day's matrix have an explicit PASS, FAIL, or BLOCKED verdict.

☐ Each verdict is backed by a concrete, named artifact (log, report, plot).

☐ Failed or blocked items have a severity rating and an assigned owner.

☐ Timing and coverage claims are supported by tool-generated reports (not manual estimates).

☐ Residual risks are captured with mitigation rationale and next-action deadline.

☐ Artifact version (build hash / model tag) is recorded and traceable to the commit.

.. note::
   This repository is a living curriculum. Content is enriched incrementally; day folders
   are the authoritative source for domain-specific scenarios and evidence.

.. warning::
   All scenarios and scripts are for educational and authorized testing purposes only.

Table of Standards
==================

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Standard
     - Description and Relevance
   * - DO-178C
     - Software Considerations in Airborne Systems — primary reference for DAL-A/B software verification objectives (Sections 6.3, 6.4, Table A-7). Drives MC/DC coverage and object-code testing requirements.
   * - DO-254
     - Design Assurance Guidance for Airborne Electronic Hardware — complements DO-178C for FPGA/ASIC verification (Sections 5.3, 6.2).
   * - ISO 26262
     - Functional Safety for Road Vehicles — ASIL decomposition, software unit testing (Part 6), and hardware fault injection (Part 5). ASIL-D requires 100 % MC/DC.
   * - IEC 62304
     - Medical Device Software Life Cycle Processes — Class C software requires complete traceability and structural coverage (Section 5.7).
   * - ARP4754A / 4761
     - System and Software Interdependence / Safety Assessment — hazard analysis (FHA, FMEA, FTA) feeding safety requirements into the V-model.
   * - ASPICE SWE.4 / SWE.5
     - Automotive SPICE — software unit verification (SWE.4) and integration testing (SWE.5) process requirements.
   * - MISRA C:2012
     - Motor Industry Software Reliability Association C coding guidelines — mandatory and required rules enforced in static analysis gate (Day15).
   * - CERT-C
     - SEI CERT C Coding Standard — runtime-error and memory-safety rules applied alongside MISRA in safety-critical C code.

List of Tools
=============

.. list-table::
   :header-rows: 1
   :widths: 22 50 28

   * - Tool
     - Purpose
     - Phase / Domain
   * - MATLAB / Simulink
     - Model-based design, plant/controller modeling, automatic C code generation, SIL/PIL execution
     - MIL → SIL; all domains
   * - Stateflow
     - State-machine and flow-chart modeling for mode logic and fault management
     - MIL; automotive, aerospace
   * - OpenModelica / Scilab-Xcos
     - Open-source alternatives for plant modeling and closed-loop simulation
     - MIL; education and prototyping
   * - Python (pytest + pandas + matplotlib)
     - Test automation scripting, batch scenario execution, log parsing, regression dashboards
     - All phases; all domains
   * - VectorCAST / LDRA Testbed
     - Structural coverage measurement (MC/DC), unit and integration test harnesses
     - SIL; automotive, aerospace, medical
   * - Polyspace Code Prover / Bug Finder
     - Formal/abstract-interpretation static analysis — proves absence of runtime errors
     - SIL; safety-critical C/Ada
   * - Lauterbach TRACE32
     - On-target debugger, WCET measurement, RTOS-aware execution tracing, DO-178C object-code testing
     - HIL; aerospace DAL-A, automotive ASIL-D
   * - CANoe / CANalyzer
     - CAN/LIN/FlexRay/Ethernet bus simulation, CAPL scripting, error-frame injection, bus logging
     - HIL; automotive
   * - Astronics Ballard CoPilot
     - ARINC 429 / 717 bus simulation, monitoring, and scripting for avionics rigs
     - HIL; aerospace
   * - IPG CarMaker
     - Full-vehicle dynamics and ADAS closed-loop simulation with sensor-model integration
     - MIL / HIL; automotive ADAS
   * - dSPACE ControlDesk / SCALEXIO
     - Real-time HIL platform, I/O signal conditioning, automated test sequencing
     - HIL; automotive, aerospace
   * - GDB / Segger J-Link
     - Open-source on-target debugging (SWD/JTAG) for ARM/RISC-V MCUs
     - SIL / HIL; medical, automotive

List of Scenarios
=================

.. list-table::
   :header-rows: 1
   :widths: 18 15 67

   * - Scenario ID
     - Severity
     - Description
   * - MIL-NOM-01
     - 🟢
     - Throttle controller nominal step response: 0–80 % demand, rise time < 200 ms, steady-state error < 2 %
   * - MIL-BND-01
     - 🟡
     - Plant model at maximum rated RPM (6500); output clamped to torque limit, no overflow in fixed-point path
   * - MIL-FLT-01
     - 🔴
     - Speed sensor dropout 50 ms mid-manoeuvre; limp-home flag set within one sample, driver alert active
   * - MIL-FLT-02
     - 🔴
     - Simultaneous actuator saturation + noisy position feedback; model enters degraded mode without diverging
   * - SIL-NOM-01
     - 🟢
     - Generated C code produces numerically equivalent outputs to Simulink model on all 47 signal channels
   * - SIL-NOM-02
     - 🟢
     - Unit tests achieve 100 % MC/DC on torque arbitration function; all 12 independence pairs exercised
   * - SIL-BND-01
     - 🟡
     - INT16 accumulator at ±32767; saturation guard triggers, no undefined overflow behaviour in C
   * - SIL-FLT-01
     - 🔴
     - NULL-pointer injected at runtime; safe-state reached in < 10 ms, no silent data corruption observed
   * - SIL-FLT-02
     - 🔴
     - Stack-overflow induced by recursive call; watchdog pre-empts, reset counter incremented and logged
   * - HIL-NOM-01
     - 🟢
     - 8 kHz control loop on target ECU; interrupt latency ≤ 125 µs, CPU utilisation ≤ 80 % across 60 s run
   * - HIL-BND-01
     - 🟡
     - CAN bus at 95 % bus load; no message loss on safety-critical frames, latency within spec
   * - HIL-FLT-01
     - 🔴
     - CAN error-frame injection (bit-flip); receiver recovers full communication within 3 message cycles
   * - HIL-FLT-02
     - 🔴
     - 50 ms power-rail glitch on ECU supply; watchdog fires, re-initialisation completes in < 500 ms

Scenario Templates
==================

Nominal Scenario 🟢
--------------------

| **GIVEN**: A correctly configured system with valid inputs within the nominal operating envelope.
| **WHEN**: The system executes under those conditions for the defined test duration.
| **THEN**: All output signals remain within the requirement-specified tolerance bands, and all artifacts are captured without interruption.

Boundary Scenario 🟡
---------------------

| **GIVEN**: Inputs at or at the edge of the maximum allowable design range (e.g., full-scale ADC, rated RPM).
| **WHEN**: The system executes and encounters those boundary values.
| **THEN**: The system maintains functional correctness; any degraded-mode behaviour is within the acceptable limits stated in the requirement.

Fault Scenario 🔴
------------------

| **GIVEN**: An injected hardware or software fault (sensor dropout, corrupted signal, power glitch, invalid pointer).
| **WHEN**: The system operates with that fault present.
| **THEN**: The system detects the fault within the latency bound specified in the safety requirement, transitions to the defined safe state, and logs the event with a timestamp.

Table of Evidence
=================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Evidence Artifact
     - Description
   * - ``sim_log_<day>_<domain>_<variant>.csv``
     - Timestamped simulation log; all signal values at every sample step, including model version tag
   * - ``verdict_summary_<day>_<domain>.rst``
     - Pass/fail verdict table linked to requirement IDs, acceptance thresholds, and observed values
   * - ``coverage_report_<day>.xml / .html``
     - Structural coverage report (statement, branch, MC/DC) exported from VectorCAST or LDRA Testbed
   * - ``fault_trace_<day>_<scenario>.csv``
     - Fault injection trace: injected condition, timestamp of detection, recovery state, verdict
   * - ``wcet_trace32_<day>.pdf``
     - Worst-case execution time report from Lauterbach TRACE32 PRACTICE scripts on target silicon
   * - ``static_analysis_<day>.html``
     - MISRA C:2012 / CERT-C / Polyspace report; open findings triaged with severity and owner
   * - ``can_trace_<day>.blf``
     - CANoe/CANalyzer binary log of bus frames during fault-injection and recovery scenarios
   * - ``compliance_matrix_<day>.rst``
     - Requirement-to-test-to-evidence traceability matrix aligned to the applicable standard objectives

Table of Compliance
===================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Compliance Reference
     - How This Curriculum Addresses It
   * - DO-178C Table A-7 (MC/DC)
     - Day19 produces 100 % MC/DC reports for each safety-critical function; Day18 extends this to object-code level with TRACE32
   * - DO-178C Section 6.3 (Reviews)
     - Day01 reviewer checklist and verdict templates align to the formal review objectives
   * - ISO 26262-6 §8 (Unit Testing)
     - Day14 unit-test harnesses and Day19 MC/DC reports directly satisfy ASIL-D unit testing requirements
   * - ISO 26262-6 §9 (Integration Testing)
     - Day14 integration scenarios and Day25 bus-level tests cover software integration verification
   * - IEC 62304 §5.7 (Software Testing)
     - SIL days (11–20) produce the traceability and structural coverage required for Class C medical software
   * - ARP4761 (FHA / FMEA)
     - Day08 and Day16 fault-injection scenarios are derived from hazard analyses documented in the domain sub-folders
   * - ASPICE SWE.4
     - Day14 unit-test evidence and Day15 static analysis reports satisfy SWE.4 base practices
   * - MISRA C:2012
     - Day11 code-generation gate and Day15 static analysis enforce mandatory and required rule compliance

Table of Patterns
=================

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Pattern
     - Description
   * - Baseline-first comparison
     - Run and archive a clean nominal scenario before executing any stress or fault variant; all divergences are measured against that fixed baseline
   * - Fixed acceptance thresholds
     - Define numeric pass/fail bounds in the requirement before the test runs; never adjust thresholds post-execution to force a pass
   * - Deterministic rerun
     - Fix RNG seed, timestamp, and model configuration hash so that identical inputs always produce bit-identical outputs
   * - Traceability-by-construction
     - Tag every scenario, log file, and report to the requirement ID it verifies at the moment of creation, not as a post-processing step
   * - Phase-gate verdict
     - Issue an explicit PASS / FAIL / BLOCKED verdict before advancing to the next phase; no implicit carry-forward of unresolved findings

Table of Anti-Patterns
======================

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Anti-Pattern
     - Why It Is Harmful
   * - Post-hoc threshold tuning
     - Adjusting acceptance bounds after seeing results invalidates the independence of verification; constitutes a DO-178C / ISO 26262 finding
   * - Missing raw artifacts
     - Reporting only verdict summaries without underlying logs or traces makes independent audit and re-run impossible
   * - Untraceable scenarios
     - Test cases not linked to a requirement ID cannot contribute to coverage or compliance arguments
   * - Phantom coverage
     - Claiming structural coverage from host-PC runs of untranslated model code rather than the actual generated C on target
   * - Silent assumption creep
     - Undocumented changes to model version, compiler flags, or configuration between the baseline run and the regression run

Table of Pitfalls
=================

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Pitfall
     - Mitigation
   * - Interface timing drift
     - Model and code use different sample rates — always verify sample-rate consistency during code generation review (Day11)
   * - Hidden global state
     - Shared memory or static variables corrupt deterministic re-run; use memory-access analysis in static analysis gate (Day15)
   * - Overlooked degraded-mode paths
     - Nominal tests all pass but limp-home and recovery scenarios are absent; enforce fault-scenario quotas per day definition-of-done
   * - Weak negative-path coverage
     - Only happy-path scenarios executed; boundary and fault scenario IDs in the matrix are marked BLOCKED without investigation
   * - Incomplete artifact versioning
     - Log files lack build hash or model version tag, making exact re-run impossible; enforce naming convention at CI commit hook
