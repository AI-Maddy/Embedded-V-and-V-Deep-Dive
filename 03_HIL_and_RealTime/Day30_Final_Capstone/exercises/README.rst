Exercises — Day30 Final Capstone 🎯
=====================================

**HIL** Evidence Quality Exercise Goal 🎯
----------------------------------------

Practice **HIL** evidence quality using reproducible tasks that demonstrate **HIL** evidence quality.

.. note:: The **HIL** Evidence Quality exercise is designed to practice the creation of high-quality evidence for HIL testing.

**HIL** Real-Time Integration Focus 🛠️
----------------------------------------

Primary focus: **real-time integration behavior, interface timing, and hardware realism**.

**HIL** Evidence Quality Mnemonic: **HILETS** - **H**ardware, **I**ntegration, **L**ogic, **E**xecution, **T**iming, **S**ynchronization

**HIL** Exercise Pack 📋
----------------------

### Nominal Scenario 🟢

GIVEN a well-defined set of requirements,
WHEN the system is executed with nominal inputs,
THEN the system shall produce the expected outputs and meet the requirement IDs.

1.  Define thresholds before execution.
2.  Capture one baseline artifact.
3.  Tie each exercise result to requirement IDs.

### Boundary Scenario 🟡

GIVEN a set of near-limit conditions (timing, value, or mode transitions),
WHEN the system is executed with boundary inputs,
THEN the system shall produce the expected outputs and meet the requirement IDs.

1.  Identify near-limit conditions (timing, value, or mode transitions).
2.  Capture one stressed comparison artifact.
3.  Verify that each exercise result meets the requirement IDs.

### Fault/Negative Scenario 🔴

GIVEN a fault or negative condition,
WHEN the system is executed with faulty inputs,
THEN the system shall detect and recover from the fault and meet the requirement IDs.

1.  Introduce a fault or negative condition.
2.  Capture expected detection and recovery behavior.
3.  Verify that each exercise result meets the requirement IDs.

### Rerun Consistency Check 🟢

GIVEN a consistent setup,
WHEN the exercise is rerun,
THEN the system shall produce the same outputs and meet the requirement IDs.

1.  Rerun the exercise with consistent setup.
2.  Verify that each exercise result meets the requirement IDs.

**HIL** Patterns 🧭
-------------------

*   Define thresholds before execution.
*   Capture one baseline and one stressed comparison artifact.
*   Tie each exercise result to requirement IDs.

**HIL** Anti-Patterns 🚫
----------------------

*   Running tests without fixed configuration snapshots.
*   Declaring pass/fail without quantitative criteria.
*   Logging summaries without raw evidence references.

.. warning:: Running tests without fixed configuration snapshots, declaring pass/fail without quantitative criteria, and logging summaries without raw evidence references are all anti-patterns that can lead to poor evidence quality.

**HIL** Pitfalls ⚠️
------------------

*   Timebase mismatch across tools/interfaces.
*   Incomplete negative-path coverage.
*   Non-deterministic reruns due to hidden setup changes.

**HIL** Examples 📚
-----------------

### Boundary Timing Overrun Scenario 🟡

GIVEN a set of near-limit timing conditions,
WHEN the system is executed with boundary inputs,
THEN the system shall produce the expected outputs and meet the requirement IDs.

*   Define near-limit timing conditions.
*   Capture stressed comparison artifact.
*   Verify that each exercise result meets the requirement IDs.

### Invalid Input Sequence 🔴

GIVEN an invalid input sequence,
WHEN the system is executed with faulty inputs,
THEN the system shall detect and recover from the fault and meet the requirement IDs.

*   Introduce invalid input sequence.
*   Capture expected detection and recovery behavior.
*   Verify that each exercise result meets the requirement IDs.

### Regression Rerun 🟢

GIVEN a consistent setup,
WHEN the exercise is rerun,
THEN the system shall produce the same outputs and meet the requirement IDs.

*   Rerun the exercise with consistent setup.
*   Verify that each exercise result meets the requirement IDs.

**HIL** Best Practices ✅
-------------------------

*   Keep artifact names stable across reruns.
*   Record environment/version metadata every run.
*   Include residual risk with each unresolved finding.

**HIL** Heuristics 🧪
-------------------

*   One failing test without root cause is incomplete work.
*   Repeatability is required for confidence.
*   If evidence is missing, result is provisional.

**HIL** Checklist 🔎
-------------------

### Pre-Review Checklist ☐

☐ Pass/fail thresholds are unambiguous.
☐ Nominal + stress + fault evidence is present.
☐ Traceability and residual risk are documented.
☐ All exercise results meet the requirement IDs.
☐ All exercise results have corresponding artifacts.
☐ All exercise results have residual risk documented.

### Review Checklist ☐

☐ All exercise results meet the requirement IDs.
☐ All exercise results have corresponding artifacts.
☐ All exercise results have residual risk documented.

Additional Deep-Dive Notes
--------------------------

### Domain Focus 📚

*   Domain: Embedded Systems
*   Phase Focus: HIL
*   Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
*   Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
*   Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
*   Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
*   Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
*   Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
*   Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.

Severity/Priority Legend
-------------------------

🟢 Nominal (Green)
🟡 Boundary (Yellow)
🔴 Fault (Red)

.. important:: The **HIL** Evidence Quality exercise is a critical component of the HIL testing process. It ensures that the evidence created is of high quality and meets the requirements of the project.

.. admonition:: The **HIL** Evidence Quality exercise is designed to be a challenging but rewarding experience. It requires careful planning, execution, and review to ensure that the evidence created meets the requirements of the project.

.. list-table:: HIL Exercise Pack

   * - Exercise Type
     - Description
   * - Nominal
     - Define thresholds before execution. Capture one baseline artifact. Tie each exercise result to requirement IDs.
   * - Boundary
     - Identify near-limit conditions (timing, value, or mode transitions). Capture one stressed comparison artifact. Verify that each exercise result meets the requirement IDs.
   * - Fault/Negative
     - Introduce a fault or negative condition. Capture expected detection and recovery behavior. Verify that each exercise result meets the requirement IDs.
   * - Rerun Consistency Check
     - Rerun the exercise with consistent setup. Verify that each exercise result meets the requirement IDs.

References
----------

*   DO-178C: Software Considerations in Airborne Systems and Equipment Certification
*   DO-254: Design Assurance Guidance for Airborne Electronic Hardware
*   ISO 26262: Functional Safety for Road Vehicles
*   IEC 62304: Medical Device Software - Software Life Cycle Processes
*   ARP4754A/4761: Guidelines and Requirements for the Development of Civil Aircraft and Systems
*   ASPICE: Automotive Software Process Improvement and Capability dEtermination
