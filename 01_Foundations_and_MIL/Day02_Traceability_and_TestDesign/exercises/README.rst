Exercises — Day02 Traceability and TestDesign 🚀
===============================================

🌟 **TRACE** Mnemonic: Targeted Requirements, Artifacts, Coverage, Evidence 🌟
-------------------------------------------------------------------------------
The TRACE mnemonic ensures robust **Model-in-the-Loop (MIL)** validation:
- **T**: Targeted Requirements — Link every test to specific requirement IDs.
- **R**: Reliable Artifacts — Maintain reproducible evidence for every test.
- **A**: Adequate Coverage — Include nominal 🟢, boundary 🟡, and fault 🔴 scenarios.
- **C**: Clear Metrics — Define unambiguous thresholds for pass/fail criteria.
- **E**: Evidence Quality — Ensure raw artifacts, traceability, and residual risk are documented.

🎯 Exercise Goal 🎯
-------------------
Practice **Day02 Traceability and TestDesign** using reproducible tasks that demonstrate **MIL** evidence quality.

.. note::
   This exercise aligns with **DO-178C Section 6.3**, **ISO 26262 Part 6**, and **ASPICE SWE.4** requirements for traceability and test design.

🛠️ Practical Focus 🛠️
----------------------
Primary focus: **model fidelity, requirement intent clarity, and simulation confidence**.

.. important::
   Ensure all tests are deterministic and repeatable to comply with **DO-254 Appendix B** and **IEC 62304 Section 5.7**.

📋 Exercise Pack 📋
-------------------
1. 🟢 **Nominal Scenario**: Explicit pass/fail criteria tied to requirement IDs.
2. 🟡 **Boundary Scenario**: Near limits (timing, value, or mode transitions) with stressed comparison artifacts.
3. 🔴 **Fault/Negative Scenario**: Expected detection and recovery behavior with mitigation evidence.
4. 🟢 **Rerun Consistency Check**: Repeatability validation across multiple runs.

.. admonition:: Example Expansion
   Include one nominal, one boundary, and one fault scenario per objective to meet **ARP4754A Section 5.2** coverage expectations.

🧭 Patterns 🧭
--------------
- Define thresholds **before execution** to ensure objective criteria.
- Capture **baseline and stressed comparison artifacts** for traceability.
- Tie each exercise result to **requirement IDs** for audit readiness.

🚫 Anti-Patterns 🚫
-------------------
- Running tests without fixed **configuration snapshots**.
- Declaring pass/fail without **quantitative criteria**.
- Logging summaries without **raw evidence references**.

⚠️ Pitfalls ⚠️
---------------
- **Timebase mismatch** across tools/interfaces leading to invalid results.
- **Incomplete negative-path coverage** reducing robustness.
- **Non-deterministic reruns** due to hidden setup changes.

📚 Examples 📚
--------------
- 🟡 **Boundary Timing Overrun Scenario**: Demonstrate mitigation evidence for timing drift.
- 🔴 **Invalid Input Sequence**: Show robust handling of unexpected input.
- 🟢 **Regression Rerun**: Prove fix stability with consistent results.

✅ Best Practices ✅
-------------------
- Keep **artifact names stable** across reruns for traceability.
- Record **environment/version metadata** for every run.
- Include **residual risk** with each unresolved finding.

🧪 Heuristics 🧪
---------------
- 🔴 **One failing test** without root cause is incomplete work.
- 🟢 **Repeatability** is required for confidence in evidence.
- 🔴 **Missing evidence** renders the result provisional.

🔎 Pre-Review Checklist 🔎
--------------------------
☐ Pass/fail thresholds are **unambiguous**.  
☐ Nominal 🟢, stress 🟡, and fault 🔴 evidence is **present**.  
☐ **Traceability** to requirement IDs is documented.  
☐ **Residual risk** is captured for unresolved findings.  
☐ **Environment metadata** is recorded for reproducibility.  
☐ **Artifacts** are stable and named consistently across reruns.  

Additional Deep-Dive Notes 📖
-----------------------------
- **Domain Focus**: Embedded Systems  
- **Phase Focus**: MIL (Model-in-the-Loop)  
- **Evidence Priorities**: Functional correctness, timing behavior, robustness, and traceability.  
- **Patterns**: Baseline-first comparison, fixed acceptance thresholds, deterministic reruns.  
- **Anti-Patterns**: Post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.  
- **Pitfalls**: Hidden assumptions, interface timing drift, weak requirement-to-test linkage.  
- **Review Heuristic**: If a claim cannot be tied to an artifact, mark confidence as provisional.  
- **Checklist Extension**: Capture residual risk, ownership, and next action for each unresolved item.  

.. list-table:: Severity / Priority Colour Legend  
   :widths: 20 80  
   :header-rows: 1  

   * - Colour  
     - Meaning  
   * - 🟢  
     - Nominal scenario: Expected behavior under normal conditions.  
   * - 🟡  
     - Boundary scenario: Stress testing near operational limits.  
   * - 🔴  
     - Fault scenario: Negative-path testing with recovery validation.  

**GIVEN / WHEN / THEN Templates** 🛠️
------------------------------------
- 🟢 **Nominal Scenario**:  
  GIVEN a valid input and standard configuration,  
  WHEN the model is executed under normal conditions,  
  THEN the output matches the expected requirement behavior.  

- 🟡 **Boundary Scenario**:  
  GIVEN an input near the operational limit,  
  WHEN the model is executed under stressed conditions,  
  THEN the output demonstrates compliance with defined thresholds.  

- 🔴 **Fault Scenario**:  
  GIVEN an invalid input or fault injection,  
  WHEN the model is executed,  
  THEN the system detects the fault and recovers per requirement specifications.  

.. warning::
   Ensure all fault scenarios comply with **ISO 26262 Part 4** and **DO-178C Section 6.4** for safety-critical systems.
