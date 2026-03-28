Representative Use Cases
------------------------

### 🟢 Nominal Mission/Profile Operation 🟢

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - **Use Case**
        - **GIVEN**
        - **WHEN**
        - **THEN**
    *   - **Nominal Flight Control**
        - System is in nominal flight control mode
        - Expected disturbances are applied
        - System tracks the disturbances and maintains stability 🟢
    *   - **Boundary-Condition Operation**
        - System is in high-workload transition mode
        - Stability margins are approached
        - System behavior is evaluated for stability 🟡
    *   - **Fault Detection, Containment, and Recovery**
        - System is in fault detection mode
        - Bus label corruption and sensor disagreement occur
        - System detects and contains the fault, and recovers to a safe state 🔴

    .. note::
        These use cases are aligned to **DO-178C/DO-254**.

    .. important::
        These use cases are critical for ensuring the safety and reliability of the system.

### 🟡 Boundary-Condition Operation near Limits 🟡

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - **Use Case**
        - **GIVEN**
        - **WHEN**
        - **THEN**
    *   - **High-Workload Transition**
        - System is in high-workload transition mode
        - Workload is increased
        - System behavior is evaluated for stability and reliability 🟡
    *   - **Stability Margin Testing**
        - System is in stability margin testing mode
        - Stability margins are approached
        - System behavior is evaluated for stability and reliability 🟡
    *   - **Edge Cases**
        - System is in edge case testing mode
        - Extreme conditions are applied
        - System behavior is evaluated for stability and reliability 🔴

    .. warning::
        These use cases require careful consideration of the system's stability margins.

    .. admonition::
        Review these use cases carefully to ensure that the system's behavior is evaluated correctly.

### 🔴 Fault Detection, Containment, and Recovery 🔴

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - **Use Case**
        - **GIVEN**
        - **WHEN**
        - **THEN**
    *   - **Bus Label Corruption**
        - System is in fault detection mode
        - Bus label corruption occurs
        - System detects and contains the fault, and recovers to a safe state 🔴
    *   - **Sensor Disagreement**
        - System is in fault detection mode
        - Sensor disagreement occurs
        - System detects and contains the fault, and recovers to a safe state 🔴
    *   - **Fault Tolerance**
        - System is in fault tolerance testing mode
        - Faults are injected
        - System behavior is evaluated for fault tolerance and recovery mechanisms 🔴

    .. important::
        These use cases are critical for ensuring the system's fault tolerance and recovery mechanisms.

    .. admonition::
        Review these use cases carefully to ensure that the system's fault detection and recovery mechanisms are functioning correctly.

