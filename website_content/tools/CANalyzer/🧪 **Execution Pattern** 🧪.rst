🧪 **Execution Pattern** 🧪
-------------------------

### 🟢 Nominal Scenario 🟢

.. note::
    Capture baseline artifacts under nominal conditions.

    GIVEN: System in nominal state 🟢.
    WHEN: Run tool with default settings.
    THEN: Store baseline artifacts.

### 🟡 Boundary Scenario 🟡

.. important::
    Inject edge conditions to test system limits.

    GIVEN: System in boundary state 🟡.
    WHEN: Run tool with modified settings.
    THEN: Verify system response.

### 🔴 Fault Scenario 🔴

.. warning::
    Introduce faults to test system robustness.

    GIVEN: System in fault state 🔴.
    WHEN: Run tool with fault injection.
    THEN: Verify system recovery.

