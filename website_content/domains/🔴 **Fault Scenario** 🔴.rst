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

