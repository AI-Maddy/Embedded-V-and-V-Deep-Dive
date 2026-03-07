Exercises — Day07 ClosedLoop Simulation 🚀
==========================================

🎯 Exercise Goal 🌟
-------------------
Practice **Day07 ClosedLoop Simulation** using reproducible tasks that demonstrate **MIL** evidence quality.

.. note::
   This exercise aligns with **DO-178C**, **ISO 26262**, and **ASPICE** standards for Model-in-the-Loop (MIL) verification.

🛠️ Practical Focus 🔧
----------------------
Primary focus: **model fidelity, requirement intent clarity, and simulation confidence**.

.. important::
   Use the **C.L.A.R.I.T.Y.** mnemonic to guide your MIL efforts:
   - **C**: Configuration snapshots
   - **L**: Link results to requirements
   - **A**: Artifact traceability
   - **R**: Repeatability of evidence
   - **I**: Identify residual risks
   - **T**: Thresholds defined upfront
   - **Y**: Yield actionable insights

🟢🟡🔴 Severity Legend
----------------------
- 🟢 Nominal: Expected behavior under standard conditions.
- 🟡 Boundary: Edge-case behavior near limits.
- 🔴 Fault: Error handling and recovery under abnormal conditions.

📋 Exercise Pack 📦
-------------------
1. 🟢 Nominal scenario with explicit pass/fail criteria.
2. 🟡 Boundary scenario near limits (timing, value, or mode transitions).
3. 🔴 Fault/negative scenario with expected detection and recovery behavior.
4. Rerun consistency check for repeatability.

.. admonition:: Example Reference
   :class: tip

   For **DO-178C**, ensure that simulation results are tied to requirement IDs and include evidence of deterministic behavior.

🧭 Patterns 🧩
--------------
- Define thresholds before execution.
- Capture one baseline and one stressed comparison artifact.
- Tie each exercise result to requirement IDs.

.. note::
   Thresholds should align with **ISO 26262** ASIL levels for safety-critical systems.

🚫 Anti-Patterns ❌
-------------------
- Running tests without fixed configuration snapshots.
- Declaring pass/fail without quantitative criteria.
- Logging summaries without raw evidence references.

⚠️ Pitfalls 🕵️‍♂️
------------------
- Timebase mismatch across tools/interfaces.
- Incomplete negative-path coverage.
- Non-deterministic reruns due to hidden setup changes.

.. warning::
   Hidden assumptions can invalidate your results. Always document your setup and dependencies.

📚 Examples 📖
--------------
- 🟡 Boundary timing overrun scenario with mitigation evidence.
- 🔴 Invalid input sequence demonstrating robust handling.
- 🟢 Regression rerun proving fix stability.

✅ Best Practices 🏆
--------------------
- Keep artifact names stable across reruns.
- Record environment/version metadata every run.
- Include residual risk with each unresolved finding.

.. important::
   Adhering to **ARP4754A/4761** ensures robust system-level validation and traceability.

🧪 Heuristics 🧠
---------------
- One failing test without root cause is incomplete work.
- Repeatability is required for confidence.
- If evidence is missing, result is provisional.

🔎 Checklist 📋
---------------
☐ Pass/fail thresholds are unambiguous.  
☐ Nominal + stress + fault evidence is present.  
☐ Traceability and residual risk are documented.  
☐ Configuration snapshots are captured for each run.  
☐ Environment/version metadata is logged.  
☐ Residual risks are assigned ownership and next actions.  

.. admonition:: Pre-Review Checklist
   :class: hint

   Before review, ensure:
   - All artifacts are traceable to requirements.
   - Evidence supports deterministic behavior.
   - Residual risks are clearly documented.

Scenario Templates 🛠️
----------------------
🟢 **Nominal Scenario**  
**GIVEN**: A standard configuration and input set.  
**WHEN**: Simulation executes under normal conditions.  
**THEN**: Results match expected outputs with no anomalies.

🟡 **Boundary Scenario**  
**GIVEN**: Inputs near operational limits (e.g., timing thresholds).  
**WHEN**: Simulation executes with edge-case parameters.  
**THEN**: Outputs remain within acceptable tolerances, with no failures.

🔴 **Fault Scenario**  
**GIVEN**: Invalid or unexpected input sequences.  
**WHEN**: Simulation executes with fault-inducing conditions.  
**THEN**: System detects errors and recovers gracefully, meeting robustness criteria.

List-Table: Evidence Priorities 📊
----------------------------------
.. list-table::
   :header-rows: 1

   * - Priority
     - Focus Area
     - Standard Reference
   * - 🟢 High
     - Functional correctness
     - **DO-178C**, **ISO 26262**
   * - 🟡 Medium
     - Timing behavior
     - **ASPICE**, **IEC 62304**
   * - 🔴 Critical
     - Robustness and fault recovery
     - **ARP4754A/4761**

Additional Deep-Dive Notes 📘
-----------------------------
- **Domain Focus**: General embedded systems.  
- **Phase Focus**: MIL.  
- **Evidence Priorities**: Functional correctness, timing behavior, robustness, and traceability.  
- **Patterns**: Baseline-first comparison, fixed acceptance thresholds, deterministic reruns.  
- **Anti-Patterns**: Post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.  
- **Pitfalls**: Hidden assumptions, interface timing drift, weak requirement-to-test linkage.  
- **Example Expansion**: Include one nominal, one boundary, and one fault scenario per objective.  
- **Review Heuristic**: If a claim cannot be tied to an artifact, mark confidence as provisional.  
- **Checklist Extension**: Capture residual risk, ownership, and next action for each unresolved item.
