🛰️ Day26 ExecutionTrace and WCET
================================

🎯 Day Objective
----------------
Build practical confidence in this topic by producing requirement-linked and review-ready evidence. 

**Mnemonic Acronym**: **EVIDENCE**  
- **E**xecution  
- **V**erification  
- **I**ntegration  
- **D**eliverables  
- **E**vidence  
- **N**ominal  
- **C**riteria  
- **E**valuation  

📌 Phase Context: HIL
----------------------------------
This day emphasizes **real-time integration confidence on representative hardware and buses**. The Hardware-in-the-Loop (HIL) approach allows for rigorous testing of embedded systems under realistic conditions, ensuring that both hardware and software components interact correctly.

🧠 Concept Drilldown
--------------------
- **Primary mechanism**: What signal, state, or computation governs expected behavior. This is the foundation of our verification efforts.
- **Boundary conditions**: Where nominal assumptions start to break. Understanding these limits is crucial for robust system design.
- **Safety impact**: How failure propagates into system-level risk. We must analyze potential failure modes to mitigate risks effectively.
- **Verification hook**: What observable artifact proves correctness. This could be logs, traces, or other evidence that supports our claims.

🛠️ Execution Workflow
---------------------
1. Define acceptance criteria and measurable pass/fail thresholds.  
2. Configure baseline scenario with explicit assumptions.  
3. Execute nominal run and capture primary artifacts.  
4. Execute stress/fault variants and record divergence behavior.  
5. Consolidate verdicts with traceability links.  

.. important::  
   Ensure that all acceptance criteria are aligned with the relevant standards such as DO-178C and ISO 26262 for safety-critical systems.

📊 Metrics and Evidence
-----------------------
- **Functional correctness** against requirement intent.  
- **Timing profile** (latency, jitter, deadline adherence where applicable).  
- **Robustness** under invalid/noisy/edge inputs.  
- **Evidence completeness** vs planned scenario matrix.  

.. note::  
   Metrics should be tracked in accordance with ARP4754A guidelines to ensure comprehensive coverage.

⚠️ Common Failure Modes
-----------------------
- Ambiguous acceptance criteria before test execution.  
- Hidden model/configuration drift between runs.  
- Overlooking degraded-mode or recovery path checks.  
- Incomplete artifact naming/versioning conventions.  

.. warning::  
   Failing to address these common pitfalls can lead to significant project delays and increased risk.

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

.. admonition::  
   Capture residual risk, ownership, and next action for each unresolved item to ensure accountability and clarity.







Domain Breakdown
----------------

🚗 Automotive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Standards**: ISO 26262 (ASIL) + ISO 21434
- **Hazard profile**: unintended acceleration/deceleration, loss of stability, braking faults
- **Interfaces**: CAN, LIN, FlexRay, Automotive Ethernet
- **Representative fault**: Sensor dropout and invalid CAN frame injection, simulating potential failures to assess system robustness.
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
- **Standards**: IEC 62304 + ISO 14971 + IEC 60601 context
- **Hazard profile**: incorrect dosage delivery, missed alarm, unsafe therapy continuation
- **Interfaces**: device buses, sensor links, alarm/event channels
- **Representative fault**: sensor spike/dropout and actuator command rejection path.
- Full details: `medical/ <medical>`_
Additional Deep-Dive Notes
--------------------------
- Domain Focus: Automotive | Aerospace | Medical- **Phase Focus**: HIL  
- **Evidence Priorities**: Functional correctness, timing behavior, robustness, and traceability.  
- **Patterns**: Baseline-first comparison, fixed acceptance thresholds, deterministic reruns.  
- **Anti-Patterns**: Post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.  
- **Pitfalls**: Hidden assumptions, interface timing drift, weak requirement-to-test linkage.  
- **Example Expansion**: Include one nominal, one boundary, and one fault scenario per objective.  
- **Review Heuristic**: If a claim cannot be tied to an artifact, mark confidence as provisional.  
- **Checklist Extension**: Capture residual risk, ownership, and next action for each unresolved item.  

**Scenario Templates**  
- **Nominal 🟢**:  
  **GIVEN** a defined baseline scenario,  
  **WHEN** the system executes under normal conditions,  
  **THEN** the output should match the expected results.

- **Boundary 🟡**:  
  **GIVEN** a scenario at the edge of operational limits,  
  **WHEN** the system is subjected to boundary conditions,  
  **THEN** the system should maintain stability and provide valid outputs.

- **Fault 🔴**:  
  **GIVEN** a fault condition introduced in the system,  
  **WHEN** the system encounters this fault,  
  **THEN** it should trigger the appropriate error handling mechanisms and not propagate failure.  

.. list-table:: Severity/priority colour legend
   :widths: 10 10
   :header-rows: 1

   * - Severity Level
     - Description
   * - 🟢 Nominal
     - Normal operation, expected behavior.
   * - 🟡 Boundary
     - Edge cases, potential failure points.
   * - 🔴 Fault
     - Critical failures, system risks.
