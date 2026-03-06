Worked Example — Day11 CodeGeneration
=====================================

Objective
---------
Execute a practical **SIL** exercise for Day11 CodeGeneration and produce audit-ready evidence.

Scenario
--------
- Context: representative nominal operation for this day topic.
- Variant A: boundary condition near timing/value/mode limits.
- Variant B: fault/negative stimulus with expected detection and recovery.

Setup
-----
- Freeze configuration, assumptions, and acceptance thresholds.
- Enable timestamped logging/tracing and artifact capture.
- Confirm interface signal map and initial state baseline.

Procedure
---------
1. Run nominal scenario and record baseline outputs.
2. Run boundary variant and capture divergences.
3. Run fault variant and validate safe handling/recovery.
4. Repeat key run to confirm repeatability.

🧭 Patterns
-----------
- Compare every stressed run against a baseline artifact.
- Keep pass/fail logic requirement-driven, not tool-driven.
- Separate observation from interpretation in reports.

🚫 Anti-Patterns
----------------
- Tuning thresholds after seeing failing results.
- Mixing multiple uncontrolled changes in one run.
- Summarizing outcomes without raw evidence pointers.

⚠️ Pitfalls
------------
- Hidden dependencies in setup scripts.
- Missing failure classification severity.
- Incomplete handoff notes for unresolved issues.

📚 Examples
-----------
- Example 1: Nominal pass with complete traceability chain.
- Example 2: Boundary fail revealing timing jitter limit breach.
- Example 3: Fault recovery success with documented residual risk.

✅ Best Practices
----------------
- Keep rerun steps deterministic.
- Store artifacts with version/time metadata.
- Review findings with risk owner before closure.

🧪 Heuristics
-------------
- If rerun differs unexpectedly, treat as investigation trigger.
- If claim lacks artifact, downgrade confidence.
- If risk is unresolved, status cannot be final pass.

🔎 Checklist
------------
- Functional, timing, robustness evidence captured.
- Requirement-linked verdict table completed.
- Residual risk and next actions documented.

Phase Focus Note
----------------
This day emphasizes: **software correctness, fault robustness, and structural evidence quality**.
