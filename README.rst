🌟 Embedded V&V Deep Dive 🚀
=========================

🎯 Repository Purpose 📚
---------------------

This repository provides a **deep, applied verification and validation curriculum** for **MIL → SIL → HIL** across automotive, aerospace, and medical systems. 🚗🛫️💉

The **VERITAS** 🤖 mnemonic acronym is used throughout this repository to represent the key concepts of Verification, Evidence, Requirements, Intent, Traceability, Artifact, and Standards.

🧭 Navigation Map 🗺️
-----------------

### Foundations and MIL (Day01–Day10) 📚
🔹 **VERITAS** 🤖
-----------------

*   `Foundations and MIL <01_Foundations_and_MIL>`_
    *   Learn the fundamentals of embedded systems verification and validation.
    *   Understand the MIL (Model-in-the-Loop) phase.
    *   .. note:: Refer to DO-178C, DO-254, and ISO 26262 for industry standards and guidelines.

### SIL and Software Validation (Day11–Day20) 🤖
🔹 **VERITAS** 🤖
-----------------

*   `SIL and Software Validation <02_SIL_and_Software_Validation>`_
    *   Dive into the SIL (Software-in-the-Loop) phase.
    *   Learn how to validate software components.
    *   .. note:: Refer to IEC 62304 and ARP4754A/4761 for industry standards and guidelines.

### HIL and Real-Time (Day21–Day30) ⏰
🔹 **VERITAS** 🤖
-----------------

*   `HIL and Real-Time <03_HIL_and_RealTime>`_
    *   Explore the HIL (Hardware-in-the-Loop) phase.
    *   Understand real-time systems and their verification challenges.
    *   .. note:: Refer to ASPICE and ISO 26262 for industry standards and guidelines.

### Domain Scenario Bank 📚
🔹 **VERITAS** 🤖
-----------------

*   `Domain scenario bank <domains>`_
    *   Access a collection of domain-specific scenarios.
    *   Use them to practice your verification and validation skills.

### Tool Playbooks 🛠️
🔹 **VERITAS** 🤖
-----------------

*   `Tool playbooks <tools>`_
    *   Discover tool-specific playbooks.
    *   Learn how to use them effectively in your V&V workflow.

🧠 Learning Contract 📝
---------------------

### V&V Fundamentals
🔹 **VERITAS** 🤖
---------------

1.  Explain requirement intent and hazard context. 🤔
    *   **V** - Verification
    *   **E** - Evidence
    *   **R** - Requirements
    *   **I** - Intent
    *   **T** - Traceability
    *   **A** - Artifact
    *   **S** - Standards
2.  Execute reproducible verification scenarios. 💻
3.  Evaluate outcomes using objective metrics. 📊
4.  Evidence every claim with traceable artifacts. 📝

📦 Standard Artifact Set 📁
------------------------

### Requirement-Linked Scenario Matrix 📈
🔹 **VERITAS** 🤖
-----------------

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Scenario**
     - **Description**
   * - Scenario1
     - Scenario Description
   * - Scenario2
     - Scenario Description

### Timestamped Logs/Traces/Plots 📊
🔹 **VERITAS** 🤖
-----------------

*   A collection of logs, traces, and plots timestamped for reference.

### Fault and Robustness Evidence 🚨
🔹 **VERITAS** 🤖
-----------------

*   Evidence of faults and robustness testing.

### Timing/Coverage Summaries 🕒
🔹 **VERITAS** 🤖
-----------------

*   Summaries of timing and coverage metrics.

### Compliance Mapping Notes 📝
🔹 **VERITAS** 🤖
-----------------

*   Notes on compliance mapping.

✅ Definition of Done (Per Day) 📝
-------------------------------

### Scenario Coverage Executed as Planned 📈
🔹 **VERITAS** 🤖
-----------------

*   ☐ Scenario coverage executed as planned.

### Pass/Fail Rules Applied Consistently 📊
🔹 **VERITAS** 🤖
-----------------

*   ☐ Pass/fail rules applied consistently.

### Findings Traceable to Objective IDs 📝
🔹 **VERITAS** 🤖
-----------------

*   ☐ Findings traceable to objective IDs.

### Residual Risks and Next Actions Documented 📝
🔹 **VERITAS** 🤖
-----------------

*   ☐ Residual risks and next actions documented.

Severity/Priority Colour Legend 📊
---------------------------------

*   🟢 **Nominal** - Normal operation
*   🟡 **Boundary** - Edge cases
*   🔴 **Fault** - Error conditions

Pre-Review Checklist 📝
----------------------

### Review Checklist 📝
🔹 **VERITAS** 🤖
-----------------

*   ☐ Review all scenarios for completeness.
*   ☐ Verify that all requirements are met.
*   ☐ Ensure that all evidence is traceable.
*   ☐ Check for consistency in pass/fail rules.
*   ☐ Document residual risks and next actions.

.. note::
    This document is a work in progress and is subject to change.

.. warning::
    The information contained in this document is for educational purposes only.

.. important::
    The author is not responsible for any damages or losses resulting from the use of this document.

.. admonition::
    This document is intended for use by experienced professionals in the field of embedded systems verification and validation.

Table of Standards
=================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Standard**
     - **Description**
   * - DO-178C
     - Software Considerations in Airborne Systems
   * - DO-254
     - Design Assurance for Airborne Systems
   * - ISO 26262
     - Functional Safety for Road Vehicles
   * - IEC 62304
     - Medical Device Software Life Cycle Processes
   * - ARP4754A/4761
     - System and Software Interdependence
   * - ASPICE
     - Automotive Safety Process

List of Tools
=============

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Tool**
     - **Description**
   * - Tool1
     - Tool Description
   * - Tool2
     - Tool Description

List of Scenarios
================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Scenario**
     - **Description**
   * - Scenario1
     - Scenario Description
   * - Scenario2
     - Scenario Description

Scenario Templates
================

### Nominal Scenario 🟢
-----------------

*   GIVEN: Normal operating conditions
*   WHEN: The system is executed as designed
*   THEN: The system behaves as expected

### Boundary Scenario 🟡
-----------------

*   GIVEN: Edge case conditions
*   WHEN: The system is executed at the boundary of its operating range
*   THEN: The system behaves as expected

### Fault Scenario 🔴
-----------------

*   GIVEN: Error conditions
*   WHEN: The system is executed with a fault
*   THEN: The system behaves as expected

Example Scenario
==============

### Nominal Scenario 🟢
-----------------

*   GIVEN: The system is powered on and the user inputs a valid command
*   WHEN: The system executes the command as designed
*   THEN: The system displays the expected output

### Boundary Scenario 🟡
-----------------

*   GIVEN: The user inputs a command at the boundary of the system's operating range
*   WHEN: The system executes the command as designed
*   THEN: The system behaves as expected

### Fault Scenario 🔴
-----------------

*   GIVEN: The system is powered on and a fault is introduced
*   WHEN: The system executes as designed
*   THEN: The system behaves as expected

Table of Evidence
================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Evidence**
     - **Description**
   * - Evidence1
     - Evidence Description
   * - Evidence2
     - Evidence Description

Table of Compliance
================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Compliance**
     - **Description**
   * - Compliance1
     - Compliance Description
   * - Compliance2
     - Compliance Description

Table of Patterns
================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Pattern**
     - **Description**
   * - Pattern1
     - Pattern Description
   * - Pattern2
     - Pattern Description

Table of Anti-Patterns
=====================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Anti-Pattern**
     - **Description**
   * - Anti-Pattern1
     - Anti-Pattern Description
   * - Anti-Pattern2
     - Anti-Pattern Description

Table of Pitfalls
================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Pitfall**
     - **Description**
   * - Pitfall1
     - Pitfall Description
   * - Pitfall2
     - Pitfall Description

Table of Residual Risks
=====================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Residual Risk**
     - **Description**
   * - Residual Risk1
     - Residual Risk Description
   * - Residual Risk2
     - Residual Risk Description

Table of Next Actions
=====================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Next Action**
     - **Description**
   * - Next Action1
     - Next Action Description
   * - Next Action2
     - Next Action Description

Table of Ownership
================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Ownership**
     - **Description**
   * - Ownership1
     - Ownership Description
   * - Ownership2
     - Ownership Description

Table of Review Checklist
=========================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Review Checklist**
     - **Description**
   * - Review Checklist1
     - Review Checklist Description
   * - Review Checklist2
     - Review Checklist Description

Table of Review Status
=====================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Review Status**
     - **Description**
   * - Review Status1
     - Review Status Description
   * - Review Status2
     - Review Status Description

Table of Review Comments
=====================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Review Comment**
     - **Description**
   * - Review Comment1
     - Review Comment Description
   * - Review Comment2
     - Review Comment Description

Table of Review History
=====================

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - **Review History**
     - **Description**
   * - Review History1
     - Review History Description
   * - Review History2
     - Review History Description
