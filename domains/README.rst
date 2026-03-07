📚 Embedded Systems Verification and Validation (V&V) Domain 📚
===========================================================

🎯 **EMBEDD** Your Way to V&V Success 🎯
------------------------------------

.. important:: Capture focused artifacts for this scope with enough detail for independent technical review, adhering to industry standards such as DO-178C, DO-254, ISO 26262, IEC 62304, ARP4754A/4761, and ASPICE.

🧩 **EMBEDD** Mnemonic 🧩
-------------------

Use the **EMBEDD** mnemonic to remember the key elements:

    - **E**: Explicitly state the scope and assumptions 📝
    - **M**: Map scenario or procedure descriptions to objectives 🗺️
    - **B**: Bind raw evidence references to findings 🔗
    - **E**: Evaluate analysis summary and verdict 💡
    - **D**: Document open issues and follow-up actions 📝
    - **D**: Drive continuous improvement and iteration 🔁

    The expected content includes:

    - Scope and assumptions 📝
    - Scenario or procedure description 🗺️
    - Raw evidence references 🔗
    - Analysis summary and verdict 💡
    - Open issues and follow-up actions 📝
    - Continuous improvement and iteration plan 🔁

📋 Acceptance Criteria 📋
----------------------

.. admonition:: Objective and constraints are explicitly stated.

    .. list-table::
       :widths: 20 80
       :stub-columns: 1

       * - Criteria
         - Description
       * - Objective
         - Clearly stated objective and constraints 📝
       * - Evidence
         - Complete and accessible evidence set 🔗
       * - Findings
         - Mapped to scenario outcomes 🗺️
       * - Next Actions
         - Prioritized with ownership 📝
       * - Continuous Improvement
         - Iterative refinement and growth plan 🔁

🟢 **Nominal Scenario** 🟢
-------------------------

    GIVEN: [Normal operating conditions] 🟢
    WHEN: [Expected input or event] 🟢
    THEN: [Expected outcome or behavior] 🟢

    .. note:: Example: A nominal scenario for a temperature sensor might be:

        GIVEN: Temperature sensor is within normal operating range
        WHEN: User inputs a valid temperature reading
        THEN: Sensor outputs a correct temperature reading

🟡 **Boundary Scenario** 🟡
-------------------------

    GIVEN: [Boundary operating conditions] 🟡
    WHEN: [Input or event at boundary] 🟡
    THEN: [Expected outcome or behavior] 🟡

    .. note:: Example: A boundary scenario for a temperature sensor might be:

        GIVEN: Temperature sensor is at maximum operating temperature
        WHEN: User inputs a temperature reading at the maximum limit
        THEN: Sensor outputs a warning message indicating maximum temperature reached

🔴 **Fault Scenario** 🔴
-------------------------

    GIVEN: [Faulty operating conditions] 🔴
    WHEN: [Input or event triggering fault] 🔴
    THEN: [Expected outcome or behavior] 🔴

    .. note:: Example: A fault scenario for a temperature sensor might be:

        GIVEN: Temperature sensor is faulty and outputs incorrect readings
        WHEN: User inputs a temperature reading
        THEN: Sensor outputs an error message indicating faulty sensor

📏 Quality Bar 📏
--------------

.. warning:: Ensure the following quality attributes:

    .. list-table::
       :widths: 20 80
       :stub-columns: 1

       * - Attribute
         - Description
       * - Reproducible
         - Rerun steps produce consistent outcome 📝
       * - Traceable
         - Each finding links to objective/requirement IDs 🔗
       * - Auditable
         - Timestamps, versions, and ownership are present 📆
       * - Continuous Improvement
         - Iterative refinement and growth plan 🔁

⚠️ Typical Gaps ⚠️
--------------

.. warning:: Watch out for common gaps:

    - Missing setup assumptions causing non-repeatable runs 🚫
    - Incomplete raw evidence attached to final conclusions 🔗
    - No confidence statement for borderline or mixed outcomes 💡
    - Lack of continuous improvement and iteration plan 🔁

✅ Completion Checklist ✅
----------------------

.. note:: Use the following checklist:

    ☐ Context and constraints documented 📝
    ☐ Evidence attached and named consistently 🔗
    ☐ Findings summarized with confidence level 💡
    ☐ Next actions assigned with priority 📝
    ☐ Continuous improvement and iteration plan established 🔁

📝 Pre-Review Checklist 📝
------------------------

.. note:: Use the following checklist before reviewing:

    ☐ Are all objectives and constraints explicitly stated? 📝
    ☐ Is the evidence set complete and accessible? 🔗
    ☐ Are findings mapped to scenario outcomes? 🗺️
    ☐ Are next actions prioritized with ownership? 📝
    ☐ Are all quality attributes met? 📏
    ☐ Are all typical gaps addressed? ⚠️
    ☐ Is a continuous improvement and iteration plan in place? 🔁

📊 Additional Deep-Dive Notes 📊
---------------------------

.. note:: Consider the following:

    - Domain Focus: General 🌎
    - Phase Focus: Cross-Phase 🔄
    - Evidence Priorities: functional correctness, timing behavior, robustness, and traceability 🔍
    - Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns 📊
    - Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks 🚫
    - Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage 🤔
    - Example Expansion: include one nominal, one boundary, and one fault scenario per objective 📝
    - Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional 💡
    - Checklist Extension: capture residual risk, ownership, and next action for each unresolved item 📝

📚 Standards and References 📚
---------------------------

* DO-178C: Software Considerations in Airborne Systems and Equipment Certification 🚀
* DO-254: Design Assurance Guidance for Airborne Electronic Hardware 🛠️
* ISO 26262: Functional Safety for Road Vehicles 🚗
* IEC 62304: Medical Device Software - Software Life Cycle Processes 💊
* ARP4754A/4761: Guidelines and Requirements for the Development of Civil Aircraft and Systems ✈️
* ASPICE: Automotive Spice Process Improvement and Capability dEvelopment 🚗

📝 Review and Revision 📝
----------------------

.. note:: Review and revise this document regularly to ensure it remains accurate and up-to-date.

📊 Revision History 📊
-------------------

* [Insert revision history here]

📝 Acknowledgments 📝
------------------

* [Insert acknowledgments here]

📚 Copyright and License 📚
-------------------------

* [Insert copyright and license information here]
