Worked Example — Day22 Hardware Setup 🚀
=========================================

Objective 🎯
---------
Execute a practical **HIL** (Hardware-in-the-Loop) exercise for Day22 Hardware Setup and produce audit-ready evidence. This exercise is crucial for ensuring that the embedded system meets its requirements and functions correctly in real-world scenarios.

Mnemonic Acronym: **HIL-SET** (Hardware Integration & Loop - Setup, Evidence, Testing)

Scenario 🔍
--------
- **Context**: representative nominal operation for this day's topic, ensuring that the system behaves as expected under normal conditions.
- **Variant A**: boundary condition near timing/value/mode limits, testing the system's robustness and performance under edge cases.
- **Variant B**: fault/negative stimulus with expected detection and recovery, validating the system's resilience and error-handling capabilities.

Setup ⚙️
-----
- Freeze configuration, assumptions, and acceptance thresholds to maintain consistency throughout the testing process.
- Enable timestamped logging/tracing and artifact capture to ensure all relevant data is collected for analysis.
- Confirm interface signal map and initial state baseline to establish a clear reference point for all subsequent tests.

Procedure 📝
---------
1. **Run Nominal Scenario**: Execute the nominal scenario and record baseline outputs. 
   - **GIVEN** the system is in a nominal state, 
   - **WHEN** the test is initiated, 
   - **THEN** the outputs should match the expected baseline.
   
2. **Run Boundary Variant**: Execute the boundary variant and capture divergences.
   - **GIVEN** the system is operating near its limits, 
   - **WHEN** the boundary test is conducted, 
   - **THEN** any deviations from expected behavior should be documented.

3. **Run Fault Variant**: Execute the fault variant and validate safe handling/recovery.
   - **GIVEN** a fault is injected into the system, 
   - **WHEN** the fault occurs, 
   - **THEN** the system should detect the fault and recover safely.

4. **Repeat Key Run**: Confirm repeatability by running key scenarios multiple times and comparing results.

🧭 Patterns 🌈
-----------
- Compare every stressed run against a baseline artifact to ensure consistency and reliability.
- Keep pass/fail logic requirement-driven, not tool-driven, to maintain focus on system requirements.
- Separate observation from interpretation in reports to enhance clarity and objectivity.

🚫 Anti-Patterns ⚠️
----------------
- Tuning thresholds after seeing failing results can lead to biased outcomes.
- Mixing multiple uncontrolled changes in one run complicates analysis and interpretation.
- Summarizing outcomes without raw evidence pointers undermines the validity of the findings.

⚠️ Pitfalls ⚠️
------------
- Hidden dependencies in setup scripts can lead to unexpected failures.
- Missing failure classification severity may result in inadequate risk assessment.
- Incomplete handoff notes for unresolved issues can hinder future troubleshooting efforts.

📚 Examples 📖
-----------
- **Example 1**: Nominal pass with complete traceability chain demonstrating compliance with requirements.
- **Example 2**: Boundary fail revealing timing jitter limit breach, necessitating further investigation.
- **Example 3**: Fault recovery success with documented residual risk, highlighting areas for improvement.

✅ Best Practices 🌟
----------------
- Keep rerun steps deterministic to ensure reproducibility of results.
- Store artifacts with version/time metadata for traceability and accountability.
- Review findings with risk owner before closure to ensure all concerns are addressed.

🧪 Heuristics 💡
-------------
- If rerun differs unexpectedly, treat as an investigation trigger to identify underlying issues.
- If claim lacks artifact, downgrade confidence in the result until sufficient evidence is provided.
- If risk is unresolved, status cannot be final pass, indicating the need for further action.

🔎 Checklist ✅
------------
- [ ] Functional, timing, robustness evidence captured.
- [ ] Requirement-linked verdict table completed.
- [ ] Residual risk and next actions documented.

Phase Focus Note 📌
----------------
This day emphasizes: **real-time integration behavior, interface timing, and hardware realism** to ensure that the embedded system operates effectively in its intended environment.

.. note::
   Refer to DO-178C for software considerations in airborne systems, and DO-254 for hardware aspects to ensure compliance with industry standards.

.. important::
   Ensure all team members are familiar with the HIL-SET mnemonic to promote a shared understanding of the objectives and processes involved in the exercise.
