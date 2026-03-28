Domain-Specific Examples
------------------------

### 🟢 Nominal Example 🟢

*   **Example A**: stable flight-control mode tracking with expected disturbances.
    GIVEN: System is in nominal flight control mode
    WHEN: Expected disturbances are applied
    THEN: System tracks the disturbances and maintains stability 🟢

    .. note::
        This example is aligned to **DO-178C/DO-254**.

    .. important::
        This example is critical for ensuring the safety and reliability of the system.

### 🟡 Boundary Example 🟡

*   **Example B**: high-workload transition envelope near stability margins.
    GIVEN: System is in high-workload transition mode
    WHEN: Stability margins are approached
    THEN: System behavior is evaluated for stability 🟡

    .. warning::
        This example requires careful consideration of the system's stability margins.

    .. admonition::
        Review this example carefully to ensure that the system's behavior is evaluated correctly.

### 🔴 Fault Example 🔴

*   **Example C**: bus label corruption and sensor disagreement event.
    GIVEN: System is in fault detection mode
    WHEN: Bus label corruption and sensor disagreement occur
    THEN: System detects and contains the fault, and recovers to a safe state 🔴

    .. important::
        This example is critical for ensuring the system's fault tolerance and recovery mechanisms.

    .. admonition::
        Review this example carefully to ensure that the system's fault detection and recovery mechanisms are functioning correctly.

