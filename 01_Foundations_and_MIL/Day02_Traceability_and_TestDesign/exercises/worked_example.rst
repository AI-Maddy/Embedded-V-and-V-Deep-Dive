🎯 Worked Example — Day02 Traceability and TestDesign
=====================================================

Objective 🌟
------------
Execute a practical **MIL** exercise for Day02 Traceability and TestDesign and produce audit-ready evidence.

.. note::
   This exercise aligns with **DO-178C** objectives for software verification, **DO-254** for hardware traceability, and **ISO 26262** for functional safety. Ensure compliance with these standards throughout the activity.

🌈 TRACE Mnemonic 🌈
-------------------
To ensure comprehensive traceability in MIL testing, remember **TRACE**:
- **T**: Timestamped logging for evidence
- **R**: Requirement-driven pass/fail criteria
- **A**: Artifact capture for audit trails
- **C**: Clear classification of results (Nominal 🟢, Boundary 🟡, Fault 🔴)
- **E**: Evidence-based reporting and risk documentation

Scenario 🧩
-----------
GIVEN a representative **MIL** model setup:
- 🟢 Nominal: Standard operation within expected parameters.
- 🟡 Boundary: Near-limit conditions for timing, value, or mode.
- 🔴 Fault: Negative stimulus with expected detection and recovery.

WHEN executing the test cases:
- 🟢 Nominal: The model operates as intended without deviations.
- 🟡 Boundary: The model approaches its operational limits.
- 🔴 Fault: The model encounters an error condition.

THEN validate the following:
- 🟢 Nominal: Outputs match baseline expectations.
- 🟡 Boundary: Divergences are captured and analyzed.
- 🔴 Fault: Safe handling and recovery are confirmed.

Setup ⚙️
---------
- ☐ Freeze configuration, assumptions, and acceptance thresholds.
- ☐ Enable timestamped logging/tracing and artifact capture.
- ☐ Confirm interface signal map and initial state baseline.
- ☐ Verify compliance with **ARP4754A** system development processes.

Procedure 🛠️
-------------
1. 🟢 Run nominal scenario and record baseline outputs.
2. 🟡 Run boundary variant and capture divergences.
3. 🔴 Run fault variant and validate safe handling/recovery.
4. 🟢 Repeat key run to confirm repeatability.

.. important::
   Ensure all test runs are conducted under identical conditions to maintain determinism. This is critical for **DO-178C** and **ISO 26262** compliance.

📊 Results Analysis
-------------------
.. list-table::
   :header-rows: 1

   * - Scenario
     - Expected Outcome
     - Observed Outcome
     - Verdict
   * - 🟢 Nominal
     - Outputs match baseline
     - Outputs match baseline
     - PASS
   * - 🟡 Boundary
     - Divergences within acceptable limits
     - Timing jitter exceeds threshold
     - FAIL
   * - 🔴 Fault
     - Recovery mechanism activates
     - Recovery mechanism activates
     - PASS

🧭 Patterns for Success
------------------------
- Compare every stressed run against a baseline artifact.
- Keep pass/fail logic requirement-driven, not tool-driven.
- Separate observation from interpretation in reports.

🚫 Anti-Patterns to Avoid
-------------------------
- Tuning thresholds after seeing failing results.
- Mixing multiple uncontrolled changes in one run.
- Summarizing outcomes without raw evidence pointers.

⚠️ Common Pitfalls
-------------------
- Hidden dependencies in setup scripts.
- Missing failure classification severity.
- Incomplete handoff notes for unresolved issues.

📚 Worked Examples
------------------
- **Example 1**: 🟢 Nominal pass with complete traceability chain.
- **Example 2**: 🟡 Boundary fail revealing timing jitter limit breach.
- **Example 3**: 🔴 Fault recovery success with documented residual risk.

✅ Best Practices
-----------------
- ☐ Keep rerun steps deterministic.
- ☐ Store artifacts with version/time metadata.
- ☐ Review findings with risk owner before closure.

🧪 Heuristics for Investigation
-------------------------------
- If rerun differs unexpectedly, treat as investigation trigger.
- If claim lacks artifact, downgrade confidence.
- If risk is unresolved, status cannot be final pass.

🔎 Pre-Review Checklist
-----------------------
- ☐ Functional, timing, robustness evidence captured.
- ☐ Requirement-linked verdict table completed.
- ☐ Residual risk and next actions documented.
- ☐ Compliance with **DO-178C**, **DO-254**, and **ISO 26262** verified.

Phase Focus Note 🛡️
--------------------
This day emphasizes: **model fidelity, requirement intent clarity, and simulation confidence**.

.. admonition:: Standards Reminder
   :class: important

   Ensure all traceability artifacts meet the audit requirements of **DO-178C**, **DO-254**, and **ISO 26262**. This includes timestamped logs, requirement-linked results, and residual risk documentation.
