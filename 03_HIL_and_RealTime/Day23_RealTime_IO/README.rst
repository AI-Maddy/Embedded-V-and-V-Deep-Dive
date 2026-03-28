🛰️ Day23 RealTime IO
====================

🎯 Day Objective
----------------
Build practical confidence in this topic by producing requirement-linked and review-ready evidence. **Remember: R.E.A.L.** - **R**equirements, **E**vidence, **A**cceptance, **L**inkage! 

📌 Phase Context: HIL
----------------------------------
This day emphasizes **real-time integration confidence on representative hardware and buses**. The Hardware-in-the-Loop (HIL) testing phase is crucial for ensuring that embedded systems behave as expected under real-world conditions.

🧠 Concept Drilldown
--------------------
- **Primary Mechanism**: What signal, state, or computation governs expected behavior.
- **Boundary Conditions**: Where nominal assumptions start to break.
- **Safety Impact**: How failure propagates into system-level risk.
- **Verification Hook**: What observable artifact proves correctness.

.. important::
   Understanding these concepts is essential for effective V&V in embedded systems, particularly under the guidelines of DO-178C and ISO 26262.

🛠️ Execution Workflow
---------------------
1. Define acceptance criteria and measurable pass/fail thresholds.
2. Configure baseline scenario with explicit assumptions.
3. Execute nominal run and capture primary artifacts.
4. Execute stress/fault variants and record divergence behavior.
5. Consolidate verdicts with traceability links.

.. note::
   Ensure that each step is documented thoroughly to maintain traceability and compliance with relevant standards.

📊 Metrics and Evidence
-----------------------
- Functional correctness against requirement intent.
- Timing profile (latency, jitter, deadline adherence where applicable).
- Robustness under invalid/noisy/edge inputs.
- Evidence completeness vs planned scenario matrix.

.. warning::
   Incomplete metrics can lead to misinterpretation of system performance and safety.

⚠️ Common Failure Modes
-----------------------
- Ambiguous acceptance criteria before test execution.
- Hidden model/configuration drift between runs.
- Overlooking degraded-mode or recovery path checks.
- Incomplete artifact naming/versioning conventions.

🔴 Severity Legend
-----------------
- 🟢 Nominal: Expected behavior under standard conditions.
- 🟡 Boundary: Behavior at the limits of expected conditions.
- 🔴 Fault: Behavior under failure conditions.

✅ Required Deliverables
------------------------
- Scenario matrix with objective mapping.
- Raw logs/traces/plots with timestamps.
- Requirement-linked verdict summary.
- Residual-risk and next-action list.

🔍 Reviewer Checklist
---------------------
- [ ] Are pass/fail rules explicit and reproducible?
- [ ] Is each key claim backed by a concrete artifact?
- [ ] Are failures triaged with severity and owner?
- [ ] Is handoff quality sufficient for the next phase?

.. important::
   This checklist is vital for ensuring that all aspects of V&V are covered before moving to the next phase.







Domain Breakdown
----------------

🚗 Automotive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Standards**: ISO 26262 (ASIL) + ISO 21434
- **Hazard profile**: unintended acceleration/deceleration, loss of stability, braking faults
- **Interfaces**: CAN, LIN, FlexRay, Automotive Ethernet
- **Representative fault**: Sensor dropout and invalid CAN frame injection leading to potential system failures.
- Full details: `automotive/ <automotive>`_

✈ Aerospace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Standards**: DO-178C/DO-254 + ARP4754A/ARP4761
- **Hazard profile**: loss of control authority, unstable mode transition, stale avionics data
- **Interfaces**: ARINC 429/664, AFDX, discrete I/O
- **Representative fault**: bus label corruption and sensor disagreement event.
- Full details: `aerospace/ <aerospace>`_

🩺 Medical
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Standards**: IEC 62304 (Software Life Cycle Processes), ISO 14971 (Risk Management), and IEC 60601 (Medical Electrical Equipment).
- **Hazard profile**: incorrect dosage delivery, missed alarm, unsafe therapy continuation.
- **Interfaces**: device buses, sensor links, alarm/event channels, which must be rigorously tested to ensure reliability and safety.
- **Representative fault**: sensor spike/dropout and actuator command rejection path, simulating failure modes to assess system robustness.
- Full details: `medical/ <medical>`_
Additional Deep-Dive Notes
--------------------------
- Domain Focus: Automotive | Aerospace | Medical
- **Phase Focus**: HIL
- **Evidence Priorities**: Functional correctness, timing behavior, robustness, and traceability.
- **Patterns**: Baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- **Anti-Patterns**: Post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- **Pitfalls**: Hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- **Example Expansion**: Include one nominal, one boundary, and one fault scenario per objective.

.. admonition::
   Use the following GIVEN / WHEN / THEN templates for scenario creation:
   - **Nominal (🟢)**: 
     - GIVEN the system is in a nominal state, 
     - WHEN the input signal is received, 
     - THEN the expected output should occur.
   - **Boundary (🟡)**: 
     - GIVEN the system is at the boundary of operational limits, 
     - WHEN the input signal is at the threshold, 
     - THEN the system should respond appropriately without failure.
   - **Fault (🔴)**: 
     - GIVEN a fault condition is simulated, 
     - WHEN the system encounters the fault, 
     - THEN it should enter a safe state or recover as designed.

.. note::
   Review heuristic: If a claim cannot be tied to an artifact, mark confidence as provisional.

.. important::
   Checklist extension: Capture residual risk, ownership, and next action for each unresolved item.
