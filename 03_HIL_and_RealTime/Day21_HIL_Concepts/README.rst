🛰️ Day21 HIL Concepts
=====================

🎯 Day Objective
----------------
Build practical confidence in this topic by producing requirement-linked and review-ready evidence. 

.. important:: Remember, the goal is to ensure that all evidence is traceable to specific requirements, enhancing the reliability of our HIL processes.

📌 Phase Context: HIL
----------------------------------
This day emphasizes **real-time integration confidence on representative hardware and buses**. HIL testing is crucial for validating embedded systems, ensuring that software and hardware components interact as expected under various conditions.

🧠 Concept Drilldown
--------------------
- **Primary Mechanism**: What signal, state, or computation governs expected behavior.
- **Boundary Conditions**: Where nominal assumptions start to break, leading to potential failures.
- **Safety Impact**: How failure propagates into system-level risk, affecting overall safety.
- **Verification Hook**: What observable artifact proves correctness, ensuring that all tests are linked to requirements.

.. note:: Understanding these concepts is essential for effective HIL testing and for meeting standards such as DO-178C and ISO 26262.

🔑 Mnemonic Acronym: **HIL-SAFE**
- **H**ardware representation
- **I**ntegration confidence
- **L**inked requirements
- **S**afety impact assessment
- **A**cceptance criteria
- **F**ault tolerance
- **E**vidence completeness

🛠️ Execution Workflow
---------------------
1. Define acceptance criteria and measurable pass/fail thresholds.
2. Configure baseline scenario with explicit assumptions.
3. Execute nominal run and capture primary artifacts.
4. Execute stress/fault variants and record divergence behavior.
5. Consolidate verdicts with traceability links.

.. warning:: Ensure that each step is documented thoroughly to maintain compliance with relevant standards.

📊 Metrics and Evidence
-----------------------
- Functional correctness against requirement intent.
- Timing profile (latency, jitter, deadline adherence where applicable).
- Robustness under invalid/noisy/edge inputs.
- Evidence completeness vs planned scenario matrix.

.. important:: Metrics should be aligned with the requirements set forth in standards like IEC 62304 and ARP4754A.

⚠️ Common Failure Modes
-----------------------
- Ambiguous acceptance criteria before test execution.
- Hidden model/configuration drift between runs.
- Overlooking degraded-mode or recovery path checks.
- Incomplete artifact naming/versioning conventions.

.. admonition:: To mitigate these risks, establish clear documentation practices and regular reviews.

✅ Required Deliverables
------------------------
- Scenario matrix with objective mapping.
- Raw logs/traces/plots with timestamps.
- Requirement-linked verdict summary.
- Residual-risk and next-action list.

🔍 Reviewer Checklist
---------------------
- Are pass/fail rules explicit and reproducible? ☐
- Is each key claim backed by a concrete artifact? ☐
- Are failures triaged with severity and owner? ☐
- Is handoff quality sufficient for the next phase? ☐

.. note:: This checklist is essential for ensuring that all aspects of the HIL process are covered before moving to the next phase.

🔄 GIVEN / WHEN / THEN Scenarios
-------------------------------
- **Nominal Scenario 🟢**:
  - **GIVEN** a properly configured HIL setup,
  - **WHEN** a nominal input signal is applied,
  - **THEN** the system should respond within the defined timing thresholds.

- **Boundary Scenario 🟡**:
  - **GIVEN** an input signal at the edge of acceptable limits,
  - **WHEN** the system processes this signal,
  - **THEN** it should maintain stability without failure.

- **Fault Scenario 🔴**:
  - **GIVEN** a simulated fault condition in the hardware,
  - **WHEN** the system attempts to process the input,
  - **THEN** it should trigger the appropriate fault handling mechanisms.







Domain Breakdown
----------------

🚗 Automotive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Standards**: ISO 26262 (ASIL) + ISO 21434
- **Hazard profile**: unintended acceleration/deceleration, loss of stability, braking faults
- **Interfaces**: CAN, LIN, FlexRay, Automotive Ethernet
- **Representative fault**: Sensor dropout and invalid CAN frame injection, simulating real-world failures to assess system robustness.
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
- **Standards**: IEC 62304 (Software Life Cycle Processes) + ISO 14971 (Risk Management) + IEC 60601 (Medical Electrical Equipment).
- **Hazard profile**: incorrect dosage delivery, missed alarm, unsafe therapy continuation.
- **Interfaces**: device buses, sensor links, alarm/event channels.
- **Representative fault**: Sensor spike/dropout and actuator command rejection path.
- Full details: `medical/ <medical>`_
Additional Deep-Dive Notes
--------------------------
- Domain Focus: Automotive | Aerospace | Medical
- **Phase Focus**: HIL
- **Evidence Priorities**: functional correctness, timing behavior, robustness, and traceability.
- **Patterns**: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- **Anti-Patterns**: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- **Pitfalls**: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- **Example Expansion**: include one nominal, one boundary, and one fault scenario per objective.
- **Review Heuristic**: if a claim cannot be tied to an artifact, mark confidence as provisional.
- **Checklist Extension**: capture residual risk, ownership, and next action for each unresolved item.

.. important:: Always refer to the relevant standards (DO-178C, DO-254, ISO 26262, IEC 62304, ARP4754A/4761, ASPICE) when conducting HIL testing to ensure compliance and safety.
