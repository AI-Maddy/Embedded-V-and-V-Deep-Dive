🌟 Worked Example — Day06 MIL Execution 🌟
=========================================

Objective 🎯
------------
Execute a practical **MIL** exercise for Day06 MIL Execution and produce audit-ready evidence, ensuring compliance with standards like **DO-178C**, **ISO 26262**, and **ASPICE**.

🛠️ **Mnemonic Acronym: MIL STAR**
---------------------------------
**M**odel fidelity  
**I**nterface validation  
**L**ogging and tracing  
**S**imulation confidence  
**T**iming analysis  
**A**udit-ready evidence  
**R**epeatability  

Scenario 🖼️
------------
GIVEN a representative MIL setup:
- 🟢 Nominal: Regular operation under expected conditions.  
- 🟡 Boundary: Stress test near timing/value/mode limits.  
- 🔴 Fault: Negative stimulus with expected detection and recovery.  

WHEN the scenarios are executed:
- 🟢 Nominal: Baseline outputs are recorded.  
- 🟡 Boundary: Divergences are captured for analysis.  
- 🔴 Fault: Safe handling and recovery mechanisms are validated.  

THEN the results must:
- 🟢 Confirm compliance with requirements.  
- 🟡 Highlight boundary condition behaviors.  
- 🔴 Document fault recovery and residual risks.  

Setup 🛠️
---------
- Freeze configuration, assumptions, and acceptance thresholds.  
- Enable timestamped logging/tracing and artifact capture.  
- Confirm interface signal map and initial state baseline.  

.. note::
   Ensure all configuration files are version-controlled and traceable to the requirement baseline (DO-178C, ISO 26262).

Procedure 📋
------------
1. 🟢 Run nominal scenario and record baseline outputs.  
2. 🟡 Run boundary variant and capture divergences.  
3. 🔴 Run fault variant and validate safe handling/recovery.  
4. Repeat key runs to confirm repeatability.  

.. important::
   Always validate against requirement-driven pass/fail criteria, not tool-driven metrics.

🧭 Patterns for Success
-----------------------
- Compare every stressed run against a baseline artifact.  
- Keep pass/fail logic requirement-driven, not tool-driven.  
- Separate observation from interpretation in reports.  

🚫 Anti-Patterns to Avoid
-------------------------
- Tuning thresholds after seeing failing results.  
- Mixing multiple uncontrolled changes in one run.  
- Summarizing outcomes without raw evidence pointers.  

⚠️ Pitfalls to Watch
---------------------
- Hidden dependencies in setup scripts.  
- Missing failure classification severity.  
- Incomplete handoff notes for unresolved issues.  

📚 Examples for Clarity
-----------------------
.. list-table::
   :header-rows: 1

   * - Example
     - Description
     - Outcome
   * - Example 1 🟢
     - Nominal pass with complete traceability chain.
     - Fully compliant and audit-ready.
   * - Example 2 🟡
     - Boundary fail revealing timing jitter limit breach.
     - Requires further investigation and mitigation.
   * - Example 3 🔴
     - Fault recovery success with documented residual risk.
     - Residual risks logged for risk owner review.

✅ Best Practices Checklist
---------------------------
- Keep rerun steps deterministic.  
- Store artifacts with version/time metadata.  
- Review findings with risk owner before closure.  

🧪 Heuristics for MIL Execution
-------------------------------
- If rerun differs unexpectedly, treat as investigation trigger.  
- If claim lacks artifact, downgrade confidence.  
- If risk is unresolved, status cannot be final pass.  

🔎 Pre-Review Checklist
-----------------------
☐ Functional, timing, robustness evidence captured.  
☐ Requirement-linked verdict table completed.  
☐ Residual risk and next actions documented.  
☐ Configuration freeze confirmed (DO-178C Section 6.3).  
☐ Timestamped logs verified for completeness.  

Phase Focus Note 📝
-------------------
This day emphasizes: **model fidelity, requirement intent clarity, and simulation confidence**.  

.. admonition:: Standards Alignment
   :class: important

   Ensure compliance with **DO-178C**, **ISO 26262**, **IEC 62304**, and **ASPICE** throughout the MIL execution process.
