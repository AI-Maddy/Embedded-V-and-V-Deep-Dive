powered on and configured, - **WHEN** a valid input signal is
received, - **THEN** the system should respond within the specified
timing profile.

-   

    **Boundary** 🟡:

    :   -   **GIVEN** the system is operating at the edge of its input
            range,
        -   **WHEN** a boundary condition is applied,
        -   **THEN** the system should maintain performance without
            failure.

-   

    **Fault** 🔴:

    :   -   **GIVEN** a simulated fault is injected into the system,
        -   **WHEN** the fault condition is triggered,
        -   **THEN** the system should enter a safe state or recover as
            defined by the requirements.

## Additional Deep-Dive Notes

-   **Domain Focus**: General
-   **Phase Focus**: HIL
-   **Evidence Priorities**: Functional correctness, timing behavior,
    robustness, and traceability.
-   **Patterns**: Baseline-first comparison, fixed acceptance
    thresholds, deterministic reruns.
-   **Anti-Patterns**: Post-hoc threshold tuning, missing raw artifacts,
    incomplete negative-path checks.
-   **Pitfalls**: Hidden assumptions, interface timing drift, weak
    requirement-to-test linkage.
-   **Example Expansion**: Include one nominal, one boundary, and one
    fault scenario per objective.
-   **Review Heuristic**: If a claim cannot be tied to an artifact, mark
    confidence as provisional.
-   **Checklist Extension**: Capture residual risk, ownership, and next
    action for each unresolved item.

::: warning
::: title
Warning
:::

Always ensure that your testing environment reflects real-world
conditions to avoid discrepancies in results.
:::
