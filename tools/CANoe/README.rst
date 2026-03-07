.. _CANoe:

🧭 CANoe
========

🎯 **CANoe** - **C**apture, **A**nalyze, **N**etwork, **o**nline **E**valuation 🎯
--------------------------------------------------------

Use this tool for **network simulation, restbus and ECU interaction validation**.

⚙️ **SETUP** - **S**etup **E**nvironment, **T**ool, **U**nit, and **P**rofile 📈
-----------------
- Capture tool version, project/profile, and interface mapping.
- Define trigger points and logging granularity.
- Validate synchronization source before formal runs.

🟢 **Nominal Scenario**
------------------------

* GIVEN: Baseline configuration and test environment.
* WHEN: Run nominal test case.
* THEN: Verify expected results and store baseline artifacts.

🟡 **Boundary Scenario**
-------------------------

* GIVEN: Baseline configuration and test environment with boundary conditions.
* WHEN: Run boundary test case.
* THEN: Verify expected results and identify potential issues.

🔴 **Fault Scenario**
----------------------

* GIVEN: Baseline configuration and test environment with fault conditions.
* WHEN: Run fault test case.
* THEN: Verify expected results and identify potential failures.

📊 **Key Metrics**
------------------

| Metric | Description |
| --- | --- |
| DBC Coverage | Measures the percentage of DBC rules covered by the test cases. |
| Cycle-Time Conformance | Verifies that the system conforms to the specified cycle time. |
| Fault Frame Behavior | Analyzes the behavior of the system under fault conditions. |

✅ **Deliverables**
------------------

- Configuration snapshot
- Raw capture/trace/log files
- Analyst summary with verdict
- Follow-up action tracker

🔍 **Quality Controls**
-------------------

* Scenario-to-requirement traceability verified.
* Artifact naming/versioning consistency enforced.
* Review notes include residual risk and next experiment.

🔎 **Review Criteria**
------------------

- Is evidence reproducible across reruns?
- Are anomalies linked to objective requirements?
- Is residual risk clearly described?

.. note:: Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.

.. important:: Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.

**CANoe Verification & Validation (V&V) Mnemonic: C.A.N.O.E.**

C - Capture and analyze data
A - Analyze and verify results
N - Network and interface validation
O - Online evaluation and testing
E - Evidence-based decision-making

🔴🟡🟢 **Severity/Priority Legend**
-----------------------------------

🔴 **Critical**: High-risk, high-priority items
🟡 **Warning**: Medium-risk, medium-priority items
🟢 **Info**: Low-risk, low-priority items

**Pre-Review Checklist**
----------------------

☐ Review evidence for reproducibility across reruns.
☐ Verify anomalies are linked to objective requirements.
☐ Ensure residual risk is clearly described.
☐ Capture residual risk, ownership, and next action for each unresolved item.

**Additional Deep-Dive Notes**
---------------------------

* Domain Focus: General
* Phase Focus: Cross-Phase
* Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
* Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
* Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
* Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
* Example Expansion: include one nominal, one boundary, and one fault scenario per objective.

.. warning:: Hidden assumptions can lead to incorrect conclusions. Verify assumptions with evidence.

.. admonition:: Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.

**References**
--------------

* DO-178C: Software Considerations in Airborne Systems and Equipment Certification
* DO-254: Design Assurance Guidance for Airborne Electronic Hardware
* ISO 26262: Functional Safety for Road Vehicles
* IEC 62304: Medical Device Software - Software Life Cycle Processes
* ARP4754A/4761: Guidelines for Development of Civil Aircraft and Systems
* ASPICE: Automotive Spice

.. admonition:: Review this checklist before proceeding to the next phase.
