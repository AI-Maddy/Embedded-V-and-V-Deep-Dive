🛰️ Day27 HIL FaultInjection
===========================

🎯 Day Objective
----------------
Build practical confidence in this topic by producing requirement-linked and review-ready evidence. This objective aligns with the mnemonic **C.R.E.A.T.E.**: **C**onfidence, **R**equirements, **E**vidence, **A**ssessments, **T**esting, **E**valuation. 

🌈 Remember: **C.R.E.A.T.E.** helps us focus on the essential elements of effective V&V in embedded systems!

📌 Phase Context: HIL
----------------------------------
This day emphasizes **real-time integration confidence on representative hardware and buses**, ensuring that our systems perform as expected under various conditions. HIL testing is crucial for validating embedded systems as it simulates real-world scenarios while allowing for controlled testing environments. 

.. note::
   HIL testing bridges the gap between simulation and real-world operation, providing invaluable insights into system behavior.

🧠 Concept Drilldown
--------------------
- **Primary Mechanism**: Identify what signal, state, or computation governs expected behavior. This is fundamental for establishing a baseline.
- **Boundary Conditions**: Understand where nominal assumptions start to break. This helps in identifying potential failure points.
- **Safety Impact**: Analyze how failure propagates into system-level risk, ensuring that safety-critical functions are not compromised.
- **Verification Hook**: Determine what observable artifact proves correctness, linking back to requirements for traceability.

.. important::
   Thoroughly understanding these concepts is vital for successful HIL testing and ensuring system reliability.

🛠️ Execution Workflow
---------------------
1. Define acceptance criteria and measurable pass/fail thresholds.
2. Configure baseline scenario with explicit assumptions.
3. Execute nominal run and capture primary artifacts.
4. Execute stress/fault variants and record divergence behavior.
5. Consolidate verdicts with traceability links.

📊 Metrics and Evidence
-----------------------
- Functional correctness against requirement intent.
- Timing profile (latency, jitter, deadline adherence where applicable).
- Robustness under invalid/noisy/edge inputs.
- Evidence completeness vs planned scenario matrix.

.. warning::
   Ensure that all metrics are clearly defined and documented to avoid misinterpretation during analysis.

⚠️ Common Failure Modes
-----------------------
- Ambiguous acceptance criteria before test execution.
- Hidden model/configuration drift between runs.
- Overlooking degraded-mode or recovery path checks.
- Incomplete artifact naming/versioning conventions.

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

🔴 Severity Legend
------------------
- 🟢 Nominal: Expected behavior under normal conditions.
- 🟡 Boundary: Behavior at the edge of operational limits.
- 🔴 Fault: Behavior under failure conditions.

GIVEN / WHEN / THEN Scenarios
------------------------------
- **Nominal Scenario**: 
  - **GIVEN** a configured HIL setup,
  - **WHEN** executing a nominal test case,
  - **THEN** the system should respond within the defined timing profile.

- **Boundary Scenario**: 
  - **GIVEN** a near-threshold input signal,
  - **WHEN** executing the boundary test case,
  - **THEN** the system should maintain operational integrity without failure.

- **Fault Scenario**: 
  - **GIVEN** a simulated fault in the system,
  - **WHEN** executing the fault test case,
  - **THEN** the system should enter a safe state or trigger recovery protocols.

.. note::
   Ensure to document all scenarios thoroughly for future reference and traceability.

.. important::
   Always validate that the acceptance criteria are aligned with the requirements to avoid ambiguity.

.. warning::
   Be cautious of hidden assumptions that may lead to incorrect conclusions during testing.







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
- **Standards**: IEC 62304 + ISO 14971 + IEC 60601 context. These standards provide the framework for software lifecycle processes, risk management, and medical electrical equipment safety, ensuring that all aspects of system design and testing adhere to best practices.
- **Hazard profile**: Incorrect dosage delivery, Missed alarm, Unsafe therapy continuation
- **Interfaces**: device buses, sensor links, alarm/event channels. Understanding these interfaces is vital for ensuring that the system responds correctly to various inputs and conditions, which is critical for patient safety.
- **Representative fault**: sensor spike/dropout and actuator command rejection path. This scenario tests the system's response to failures, ensuring that it can handle unexpected situations safely and effectively, thereby preventing potential harm to patients.
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

.. admonition::
   Remember that thorough documentation and clear communication are key to successful HIL testing and validation.

.. note::
   For further guidance, refer to the relevant standards: DO-178C, DO-254, ISO 26262, IEC 62304, ARP4754A/4761, ASPICE.
