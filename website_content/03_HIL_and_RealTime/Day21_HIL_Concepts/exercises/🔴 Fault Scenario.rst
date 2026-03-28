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
