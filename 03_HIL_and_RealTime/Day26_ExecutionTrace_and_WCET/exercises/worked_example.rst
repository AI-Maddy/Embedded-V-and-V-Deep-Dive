Worked Example — Day26 ExecutionTrace and WCET 🚀
===================================================

Objective 🎯
-----------
Execute a practical **HIL** (Hardware-in-the-Loop) exercise for Day26 ExecutionTrace and WCET, producing audit-ready evidence that ensures compliance with industry standards such as DO-178C and ISO 26262. This exercise aims to validate the integration of hardware and software components under realistic operational conditions.

Mnemonic Acronym: **HIL-TRACE**  
**H**ardware integration  
**I**ntegration testing  
**L**ogging  
**T**iming analysis  
**R**ecovery validation  
**A**udit readiness  
**C**apture artifacts  
**E**vidence-based reporting  

Scenario 🌐
-----------
- **Context**: Representative nominal operation for this day's topic, ensuring realistic conditions.
- **Variant A**: Boundary condition near timing/value/mode limits, testing the system's robustness.
- **Variant B**: Fault/negative stimulus with expected detection and recovery, validating fault tolerance.

.. important::
   This section is crucial for establishing the scenarios under which the system will be tested. Each scenario must be carefully crafted to reflect real-world conditions and edge cases.

Setup ⚙️
-------
- **Freeze configuration**: Ensure all parameters are locked to prevent unintended changes.
- **Assumptions**: Clearly document all assumptions made during the setup phase.
- **Acceptance thresholds**: Define clear criteria for success and failure.
- **Enable timestamped logging/tracing**: Activate detailed logging to capture all relevant data.
- **Artifact capture**: Ensure all outputs are stored for future analysis.
- **Confirm interface signal map**: Validate that all signals are correctly mapped.
- **Initial state baseline**: Establish a baseline for comparison during testing.

.. note::
   Proper setup is essential for the validity of the test results. Any oversight in this phase can lead to misleading conclusions.

Procedure 🛠️
-----------
1. **Run nominal scenario** 🟢: Execute the standard operation and record baseline outputs.
   - **GIVEN** the system is in a nominal state,  
   - **WHEN** the standard operation is executed,  
   - **THEN** the outputs should match the expected baseline.

2. **Run boundary variant** 🟡: Execute the boundary condition and capture divergences from the baseline.
   - **GIVEN** the system is at the boundary of operational limits,  
   - **WHEN** the boundary condition is executed,  
   - **THEN** any deviations from the baseline must be documented and analyzed.

3. **Run fault variant** 🔴: Introduce a fault condition and validate the system's safe handling and recovery.
   - **GIVEN** a fault is introduced into the system,  
   - **WHEN** the fault condition is executed,  
   - **THEN** the system should demonstrate safe recovery and log the incident.

4. **Repeat key run**: Confirm repeatability of results by rerunning critical tests.

.. warning::
   Ensure that each test run is conducted under controlled conditions to maintain the integrity of the results.

🧭 Patterns 🔄
-------------
- Compare every stressed run against a baseline artifact to ensure consistency.
- Keep pass/fail logic requirement-driven, not tool-driven, to maintain focus on objectives.
- Separate observation from interpretation in reports to enhance clarity.

🚫 Anti-Patterns ❌
--------------------
- Tuning thresholds after seeing failing results can lead to biased outcomes.
- Mixing multiple uncontrolled changes in one run complicates analysis.
- Summarizing outcomes without raw evidence pointers undermines traceability.

⚠️ Pitfalls ⚠️
---------------
- Hidden dependencies in setup scripts can lead to unexpected behavior.
- Missing failure classification severity can obscure risk assessment.
- Incomplete handoff notes for unresolved issues can hinder future troubleshooting.

📚 Examples 📖
---------------
- **Example 1**: Nominal pass with a complete traceability chain, demonstrating compliance.
- **Example 2**: Boundary fail revealing timing jitter limit breach, necessitating further investigation.
- **Example 3**: Fault recovery success with documented residual risk, ensuring transparency.

✅ Best Practices 🏆
--------------------
- Keep rerun steps deterministic to ensure reliability.
- Store artifacts with version/time metadata for traceability.
- Review findings with the risk owner before closure to ensure alignment.

🧪 Heuristics 💡
-----------------
- If rerun differs unexpectedly, treat as an investigation trigger to uncover underlying issues.
- If a claim lacks artifact, downgrade confidence in the results.
- If risk is unresolved, status cannot be final pass, indicating further action is required.

🔎 Checklist ✔️
----------------
.. list-table:: Pre-Review Checklist
   :header-rows: 1

   * - Item
     - Status
   * - Functional evidence captured
     - ☐
   * - Timing evidence captured
     - ☐
   * - Robustness evidence captured
     - ☐
   * - Requirement-linked verdict table completed
     - ☐
   * - Residual risk and next actions documented
     - ☐

Phase Focus Note 📌
--------------------
This day emphasizes: **real-time integration behavior, interface timing, and hardware realism**, ensuring that all aspects of the system are thoroughly tested and validated against industry standards such as DO-178C, ISO 26262, and IEC 62304.
