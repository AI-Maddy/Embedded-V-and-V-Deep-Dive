-   🔴 Fault: Behavior under failure conditions.

## GIVEN / WHEN / THEN Scenarios

-   **Nominal Scenario**:
    -   **GIVEN** a configured HIL setup,
    -   **WHEN** executing a nominal test case,
    -   **THEN** the system should respond within the defined timing
        profile.
-   **Boundary Scenario**:
    -   **GIVEN** a near-threshold input signal,
    -   **WHEN** executing the boundary test case,
    -   **THEN** the system should maintain operational integrity
        without failure.
-   **Fault Scenario**:
    -   **GIVEN** a simulated fault in the system,
    -   **WHEN** executing the fault test case,
    -   **THEN** the system should enter a safe state or trigger
        recovery protocols.

::: note
::: title
Note
:::

Ensure to document all scenarios thoroughly for future reference and
traceability.
:::

::: important
::: title
Important
:::

Always validate that the acceptance criteria are aligned with the
requirements to avoid ambiguity.
:::

::: warning
::: title
Warning
:::

Be cautious of hidden assumptions that may lead to incorrect conclusions
during testing.
:::

## Additional Deep-Dive Notes

-   **Domain Focus**: General
-   **Phase Focus**: HIL
-   **Evidence Priorities**: functional correctness, timing behavior,
    robustness, and traceability.
-   **Patterns**: baseline-first comparison, fixed acceptance
    thresholds, deterministic reruns.
-   **Anti-Patterns**: post-hoc threshold tuning, missing raw artifacts,
    incomplete negative-path checks.
-   **Pitfalls**: hidden assumptions, interface timing drift, weak
    requirement-to-test linkage.
-   **Example Expansion**: include one nominal, one boundary, and one
    fault scenario per objective.
-   **Review Heuristic**: if a claim cannot be tied to an artifact, mark
    confidence as provisional.
-   **Checklist Extension**: capture residual risk, ownership, and next
    action for each unresolved item.

::: admonition
Remember that thorough documentation and clear communication are key to
successful HIL testing and validation.
:::

::: note
::: title
Note
:::

For further guidance, refer to the relevant standards: DO-178C, DO-254,
ISO 26262, IEC 62304, ARP4754A/4761, ASPICE.
:::
