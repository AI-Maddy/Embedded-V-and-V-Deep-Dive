Worked Example — Day21 HIL Concepts 🌟
===================================

Objective 🎯
---------
Execute a practical **HIL** (Hardware-in-the-Loop) exercise for Day21 HIL Concepts and produce audit-ready evidence that meets the highest standards of verification and validation.

Scenario 📜
--------
- **Context**: Representative nominal operation for this day topic.
- **Variant A**: Boundary condition near timing/value/mode limits.
- **Variant B**: Fault/negative stimulus with expected detection and recovery.

Setup ⚙️
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

Mnemonic Acronym: **HIL-PASS** (HIL Integration, Logging, Procedures, Artifacts, Scenarios, Success) 

🟢 Nominal Scenario
-------------------
**GIVEN** the system is configured with baseline parameters,  
**WHEN** the nominal scenario is executed,  
**THEN** the outputs should align with the expected baseline.

🟡 Boundary Scenario
-------------------
**GIVEN** the system is operating near its defined limits,  
**WHEN** the boundary variant is executed,  
**THEN** any divergences should be documented and analyzed.

🔴 Fault Scenario
-------------------
**GIVEN** a fault condition is introduced,  
**WHEN** the fault variant is executed,  
**THEN** the system should demonstrate safe handling and recovery procedures.

🧭 Patterns 🔍
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

🧪 Heuristics 💡
-------------
- If rerun differs unexpectedly, treat as investigation trigger.
- If claim lacks artifact, downgrade confidence.
- If risk is unresolved, status cannot be final pass.

🔎 Checklist ✅
------------
.. list-table:: Pre-Review Checklist
   :header-rows: 1

   * - Item
     - Status
   * - Functional, timing, robustness evidence captured.
     - ☐
   * - Requirement-linked verdict table completed.
     - ☐
   * - Residual risk and next actions documented.
     - ☐

Phase Focus Note 📝
----------------
This day emphasizes: **real-time integration behavior, interface timing, and hardware realism**. Adhere to standards such as DO-178C for software considerations, DO-254 for hardware aspects, and ISO 26262 for automotive safety to ensure compliance and thorough validation.
