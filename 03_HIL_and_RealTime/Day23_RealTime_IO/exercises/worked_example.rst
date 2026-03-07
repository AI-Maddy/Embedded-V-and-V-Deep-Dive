Worked Example — Day23 RealTime IO 🌟
========================================

Objective 🎯
---------
Execute a practical **HIL** (Hardware-in-the-Loop) exercise for Day23 RealTime IO and produce audit-ready evidence that meets the standards of DO-178C and ISO 26262.

Scenario 📜
--------
- **Context**: representative nominal operation for this day topic.
- **Variant A**: boundary condition near timing/value/mode limits.
- **Variant B**: fault/negative stimulus with expected detection and recovery.

Setup 🛠️
-----
- Freeze configuration, assumptions, and acceptance thresholds.
- Enable timestamped logging/tracing and artifact capture.
- Confirm interface signal map and initial state baseline.

Procedure 📝
---------
1. Run nominal scenario and record baseline outputs.
2. Run boundary variant and capture divergences.
3. Run fault variant and validate safe handling/recovery.
4. Repeat key run to confirm repeatability.

🟢 Nominal Scenario
-------------------
**GIVEN** the system is configured correctly,  
**WHEN** the nominal scenario is executed,  
**THEN** baseline outputs should match expected results.

🟡 Boundary Scenario
-------------------
**GIVEN** the system is operating near timing/value/mode limits,  
**WHEN** the boundary variant is executed,  
**THEN** divergences from the baseline should be documented and analyzed.

🔴 Fault Scenario
-------------------
**GIVEN** a fault/negative stimulus is introduced,  
**WHEN** the fault variant is executed,  
**THEN** the system should detect the fault and demonstrate safe handling/recovery.

🧭 Patterns 🧩
-----------
- Compare every stressed run against a baseline artifact.
- Keep pass/fail logic requirement-driven, not tool-driven.
- Separate observation from interpretation in reports.

🚫 Anti-Patterns ⚠️
----------------
- Tuning thresholds after seeing failing results.
- Mixing multiple uncontrolled changes in one run.
- Summarizing outcomes without raw evidence pointers.

⚠️ Pitfalls 🚧
------------
- Hidden dependencies in setup scripts.
- Missing failure classification severity.
- Incomplete handoff notes for unresolved issues.

📚 Examples 📖
-----------
- **Example 1**: Nominal pass with complete traceability chain.
- **Example 2**: Boundary fail revealing timing jitter limit breach.
- **Example 3**: Fault recovery success with documented residual risk.

✅ Best Practices 🌈
----------------
- Keep rerun steps deterministic.
- Store artifacts with version/time metadata.
- Review findings with risk owner before closure.

🧪 Heuristics 🧠
-------------
- If rerun differs unexpectedly, treat as investigation trigger.
- If claim lacks artifact, downgrade confidence.
- If risk is unresolved, status cannot be final pass.

🔎 Checklist ✅
------------
.. list-table:: Pre-Review Checklist
   :widths: 20 80
   :header-rows: 1

   * - Item
     - Description
   * - Functional Evidence
     - Functional, timing, robustness evidence captured.
   * - Verdict Table
     - Requirement-linked verdict table completed.
   * - Residual Risk
     - Residual risk and next actions documented.

Phase Focus Note 📌
----------------
This day emphasizes: **real-time integration behavior, interface timing, and hardware realism** in accordance with ARP4754A and DO-254 standards.

.. note::
   Ensure all documentation is aligned with the relevant V&V standards to maintain compliance and traceability.

.. important::
   Regularly review and update the checklist to reflect any changes in project scope or requirements.
