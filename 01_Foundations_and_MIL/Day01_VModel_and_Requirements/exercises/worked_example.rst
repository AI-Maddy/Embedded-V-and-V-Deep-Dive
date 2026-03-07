🌟 Worked Example — Day01 VModel and Requirements 🌟
===================================================

🔍 **Mnemonic Acronym: FOCUS** 🔍
---------------------------------
**F** - **Fidelity** of the model under test  
**O** - **Observability** of key signals and states  
**C** - **Confidence** in simulation outcomes  
**U** - **Understanding** of requirement intent  
**S** - **Severity** classification for anomalies  

🎯 Objective 🎯
--------------
Execute a practical **MIL** exercise for Day01 VModel and Requirements and produce audit-ready evidence for **DO-178C**, **ISO 26262**, and **ARP4754A** compliance.

.. important::
   The objective aligns with the **FOCUS** mnemonic to ensure model fidelity, simulation observability, and requirement clarity.

📖 Scenario 📖
--------------
🟢 **Nominal**: Representative operation for this day topic.  
🟡 **Boundary**: Stress conditions near timing/value/mode limits.  
🔴 **Fault**: Negative stimulus with expected detection and recovery.

.. note::
   Each scenario must be executed with timestamped logging and traceability to requirements.

**Scenario Templates**  
=======================
GIVEN: A pre-configured MIL environment with frozen assumptions.  
WHEN: A specific scenario (Nominal, Boundary, Fault) is executed.  
THEN: Outputs are captured, analyzed, and compared against requirements.

🛠️ Setup 🛠️
------------
- ☐ Freeze configuration, assumptions, and acceptance thresholds.  
- ☐ Enable timestamped logging/tracing and artifact capture.  
- ☐ Confirm interface signal map and initial state baseline.  

.. admonition:: Standards Reference
   :class: tip

   **DO-178C**: Configuration management and traceability  
   **ISO 26262**: Assumptions and acceptance thresholds  
   **IEC 62304**: Logging and artifact capture  

📋 Procedure 📋
---------------
1. 🟢 **Run Nominal Scenario**: Record baseline outputs and verify against requirements.  
2. 🟡 **Run Boundary Variant**: Capture divergences and analyze stress behavior.  
3. 🔴 **Run Fault Variant**: Validate safe handling and recovery mechanisms.  
4. **Repeat Key Runs**: Confirm repeatability and consistency.

.. warning::
   Ensure all runs are deterministic and reproducible. Non-deterministic behavior must trigger investigation.

🌈 Patterns 🌈
--------------
- Compare every stressed run against a baseline artifact.  
- Keep pass/fail logic **requirement-driven**, not tool-driven.  
- Separate observation from interpretation in reports.  

🚫 Anti-Patterns 🚫
------------------
- Tuning thresholds after seeing failing results.  
- Mixing multiple uncontrolled changes in one run.  
- Summarizing outcomes without raw evidence pointers.  

⚠️ Pitfalls ⚠️
---------------
- Hidden dependencies in setup scripts.  
- Missing failure classification severity.  
- Incomplete handoff notes for unresolved issues.  

📚 Examples 📚
--------------
- 🟢 **Example 1**: Nominal pass with complete traceability chain.  
- 🟡 **Example 2**: Boundary fail revealing timing jitter limit breach.  
- 🔴 **Example 3**: Fault recovery success with documented residual risk.  

✅ Best Practices ✅
-------------------
- Keep rerun steps deterministic.  
- Store artifacts with version/time metadata.  
- Review findings with risk owner before closure.  

🧪 Heuristics 🧪
----------------
- If rerun differs unexpectedly, treat as investigation trigger.  
- If claim lacks artifact, downgrade confidence.  
- If risk is unresolved, status cannot be final pass.  

🔎 Pre-Review Checklist 🔎
--------------------------
☐ Functional, timing, robustness evidence captured.  
☐ Requirement-linked verdict table completed.  
☐ Residual risk and next actions documented.  

.. admonition:: Standards Reference
   :class: tip

   **ARP4754A**: Functional evidence and requirement linkage  
   **DO-254**: Robustness validation  
   **ISO 26262**: Residual risk documentation  

📌 Phase Focus Note 📌
----------------------
This day emphasizes: **model fidelity, requirement intent clarity, and simulation confidence**.

.. note::
   The **FOCUS** mnemonic should guide all activities to ensure compliance with industry standards and best practices.

📊 Summary Table 📊
-------------------
.. list-table:: Execution Summary
   :header-rows: 1

   * - Scenario Type
     - Severity Level
     - Key Observations
     - Verdict
   * - Nominal
     - 🟢 Green
     - Baseline matched requirements
     - Pass
   * - Boundary
     - 🟡 Yellow
     - Timing jitter observed
     - Investigate
   * - Fault
     - 🔴 Red
     - Recovery successful, residual risk noted
     - Partial Pass
