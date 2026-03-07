Worked Example — Day28 Compliance Mapping 🌟
=========================================

Objective 🎯
---------
Execute a practical **HIL** (Hardware-in-the-Loop) exercise for Day28 Compliance Mapping and produce audit-ready evidence that demonstrates compliance with relevant standards such as DO-178C and DO-254. This exercise is vital for ensuring that the embedded system meets safety and performance requirements. By adhering to these standards, we ensure that our systems are not only functional but also safe for real-world applications. 

Scenario 📜
--------
- **Context**: representative nominal operation for this day topic, ensuring all systems are functioning as intended.
- **Variant A**: boundary condition near timing/value/mode limits, testing the robustness of the system.
- **Variant B**: fault/negative stimulus with expected detection and recovery, assessing the system's resilience.

Setup ⚙️
-----
- Freeze configuration, assumptions, and acceptance thresholds to establish a controlled environment.
- Enable timestamped logging/tracing and artifact capture for thorough documentation.
- Confirm interface signal map and initial state baseline to ensure clarity in testing parameters.

Procedure 📝
---------
1. Run nominal scenario and record baseline outputs to establish a reference point.
2. Run boundary variant and capture divergences to identify potential issues at the limits.
3. Run fault variant and validate safe handling/recovery to ensure system integrity under stress.
4. Repeat key run to confirm repeatability and reliability of results.

🧭 Patterns 🧭
-----------
- Compare every stressed run against a baseline artifact to maintain a clear understanding of system behavior.
- Keep pass/fail logic requirement-driven, not tool-driven, ensuring that the focus remains on meeting specifications.
- Separate observation from interpretation in reports to enhance clarity and objectivity.

🚫 Anti-Patterns 🚫
----------------
- Tuning thresholds after seeing failing results can lead to misleading conclusions.
- Mixing multiple uncontrolled changes in one run complicates analysis and can obscure root causes.
- Summarizing outcomes without raw evidence pointers undermines the credibility of findings.

⚠️ Pitfalls ⚠️
------------
- Hidden dependencies in setup scripts can lead to unexpected behaviors during testing.
- Missing failure classification severity can result in inadequate responses to issues.
- Incomplete handoff notes for unresolved issues may lead to miscommunication in future phases.

📚 Examples 📚
-----------
- **Example 1**: Nominal pass with complete traceability chain, demonstrating compliance with all requirements.
- **Example 2**: Boundary fail revealing timing jitter limit breach, highlighting the need for further investigation.
- **Example 3**: Fault recovery success with documented residual risk, showcasing the system's robustness.

✅ Best Practices ✅
----------------
- Keep rerun steps deterministic to ensure consistent results across multiple tests.
- Store artifacts with version/time metadata for traceability and accountability.
- Review findings with risk owner before closure to ensure all perspectives are considered.

🧪 Heuristics 🧪
-------------
- If rerun differs unexpectedly, treat as investigation trigger to explore underlying causes.
- If claim lacks artifact, downgrade confidence to reflect uncertainty in results.
- If risk is unresolved, status cannot be final pass, emphasizing the need for thorough risk management.

🔎 Checklist 📝
------------
- [ ] Functional, timing, robustness evidence captured.
- [ ] Requirement-linked verdict table completed.
- [ ] Residual risk and next actions documented.

Phase Focus Note 📌
----------------
This day emphasizes: **real-time integration behavior, interface timing, and hardware realism**. Understanding these aspects is crucial for successful HIL testing.

Severity Legend 🎨
-----------------
- 🟢 **Nominal**: All systems functioning as expected, indicating successful compliance.
- 🟡 **Boundary**: Systems operating at limits, requiring close monitoring to prevent failures.
- 🔴 **Fault**: Systems experiencing failures that require immediate attention and resolution.

Mnemonic Acronym: **HIL-PRIME** 🌈
-----------------------------------
- **P**rocedure
- **R**epeatability
- **I**ntegration
- **M**onitoring
- **E**vidence

GIVEN / WHEN / THEN Scenarios 🔍
--------------------------------
- **Nominal (🟢)**:
  - **GIVEN** a stable system configuration,
  - **WHEN** the nominal scenario is executed,
  - **THEN** all outputs should match the baseline.

- **Boundary (🟡)**:
  - **GIVEN** a system operating at its limits,
  - **WHEN** the boundary variant is executed,
  - **THEN** any divergences should be documented and analyzed.

- **Fault (🔴)**:
  - **GIVEN** a fault is introduced into the system,
  - **WHEN** the fault variant is executed,
  - **THEN** the system should demonstrate proper detection and recovery mechanisms.

.. important::
   Ensure that all findings are documented thoroughly to maintain compliance with standards such as ISO 26262 and IEC 62304. This documentation is crucial for audits and future reference.

.. warning::
   Be cautious of hidden dependencies that may affect the outcome of the tests. Always validate the setup before execution to mitigate risks.

.. note::
   This exercise is crucial for ensuring that the system meets the required safety and performance standards in embedded systems. Compliance with DO-178C and DO-254 is paramount for certification.

.. admonition::
   Regularly review and update your compliance mapping to reflect any changes in system design or requirements. This proactive approach will help maintain alignment with industry standards.

.. list-table:: Compliance Mapping References
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Description
   * - DO-178C
     - Software Considerations in Airborne Systems and Equipment Certification
   * - DO-254
     - Design Assurance Guidance for Airborne Electronic Hardware
   * - ISO 26262
     - Road Vehicles – Functional Safety
   * - IEC 62304
     - Medical Device Software – Software Life Cycle Processes
   * - ARP4754A
     - Guidelines for Development of Civil Aircraft and Systems
   * - ASPICE
     - Automotive SPICE Process Assessment Model

This comprehensive approach ensures that all aspects of the HIL exercise are covered, promoting a robust verification and validation process for embedded systems.
