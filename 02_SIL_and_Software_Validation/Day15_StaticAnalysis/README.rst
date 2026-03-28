⚙️ Day15 StaticAnalysis
=======================

🎯 Day Objective
----------------
Build practical confidence in this topic by producing requirement-linked and review-ready evidence.

📌 Phase Context: SIL
----------------------------------
This day emphasizes **software correctness, structural evidence, and robustness under negative paths**.

🧠 Concept Drilldown
--------------------
- Primary mechanism: what signal, state, or computation governs expected behavior.
- Boundary conditions: where nominal assumptions start to break.
- Safety impact: how failure propagates into system-level risk.
- Verification hook: what observable artifact proves correctness.

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
- Are pass/fail rules explicit and reproducible?
- Is each key claim backed by a concrete artifact?
- Are failures triaged with severity and owner?
- Is handoff quality sufficient for the next phase?








Domain Breakdown
----------------

🚗 Automotive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Standards**: ISO 26262 (ASIL) + ISO 21434
- **Hazard profile**: unintended acceleration/deceleration, loss of stability, braking faults
- **Interfaces**: CAN, LIN, FlexRay, Automotive Ethernet
- **Representative fault**: sensor dropout and invalid CAN frame injection.
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
- Domain Focus: Automotive | Aerospace | Medical
- Phase Focus: SIL
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
