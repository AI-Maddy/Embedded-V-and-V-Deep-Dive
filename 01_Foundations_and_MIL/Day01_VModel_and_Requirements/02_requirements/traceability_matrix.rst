📈 Traceability Matrix — Day01 📊
=====================================

.. note:: This document provides guidelines for maintaining a bidirectional linkage between requirements, test scenarios, and evidence artifacts.

**Mnemonic Acronym:** TRACE

- T: Tie requirements to test scenarios
- R: Record evidence artifacts
- A: Audit links and verdicts
- C: Correct and complete requirements
- E: Ensure reproducibility

🔍 Purpose 🔎
-------------

Maintain bidirectional linkage between requirements, test scenarios, and evidence artifacts.

📝 Recommended Columns 📊
---------------------------

.. list-table:: Recommended Columns
   :widths: 20 20 20 20 20
   :stub-columns: 1

   * - Column Name
     - Description
     - Example
     - Standard Reference
     - Priority
   * - Requirement ID and criticality
     - Unique identifier for the requirement and its criticality level
     - REQ-001 (High)
     - DO-178C/DO-254
     - 🟢
   * - Verification method and scenario ID
     - Method used to verify the requirement and the corresponding test scenario ID
     - Testing (TS-001)
     - ISO 26262
     - 🟢
   * - Artifact location (log/plot/report)
     - Location of the evidence artifact
     - /logs/REQ-001.txt
     - IEC 62304
     - 🟢
   * - Verdict and issue linkage
     - Verdict of the test scenario and link to any issues
     - Pass (ISSUE-001)
     - ARP4754A/4761
     - 🟢
   * - Owner and last update timestamp
     - Owner of the requirement and the last update timestamp
     - John Doe (2022-01-01)
     - ASPICE
     - 🟡

📚 Usage Rules 📖
------------------

.. important:: No test scenario without requirement reference.

.. important:: No requirement marked complete without evidence artifact.

.. important:: Any requirement change triggers matrix review.

🔍 Quick Audit Checks 🔎
-------------------------

.. admonition:: Are failed tests linked to corrective actions?

.. admonition:: Are all critical requirements covered by at least one negative-path test?

.. admonition:: Are artifact links still valid and reproducible?

📝 GIVEN / WHEN / THEN Scenario Templates 📊
-------------------------------------------

### Nominal Scenario 🟢

* GIVEN: A requirement with a criticality level of High
* WHEN: The test scenario is executed with nominal inputs
* THEN: The test scenario passes, and the evidence artifact is generated

### Boundary Scenario 🟡

* GIVEN: A requirement with a criticality level of Medium
* WHEN: The test scenario is executed with boundary inputs
* THEN: The test scenario passes, and the evidence artifact is generated

### Fault Scenario 🔴

* GIVEN: A requirement with a criticality level of Low
* WHEN: The test scenario is executed with fault inputs
* THEN: The test scenario fails, and the issue is reported

📝 Pre-Review Checklist 📊
---------------------------

☐ Are all requirements tied to test scenarios?
☐ Are all test scenarios linked to evidence artifacts?
☐ Are all evidence artifacts reproducible?
☐ Are all critical requirements covered by at least one negative-path test?
☐ Are all failed tests linked to corrective actions?

📝 Additional Deep-Dive Notes 📊
---------------------------------

.. note:: Domain Focus: General

.. note:: Phase Focus: MIL

.. note:: Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.

.. note:: Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.

.. warning:: Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.

.. important:: Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.

.. admonition:: Example Expansion: include one nominal, one boundary, and one fault scenario per objective.

.. note:: Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.

.. note:: Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
