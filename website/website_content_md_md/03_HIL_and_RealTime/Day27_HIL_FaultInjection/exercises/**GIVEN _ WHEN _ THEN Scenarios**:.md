# **GIVEN / WHEN / THEN Scenarios**:

1.  **Nominal Scenario** 🟢:
    -   **GIVEN** the system is in a normal operational state,
    -   **WHEN** the standard test case is executed,
    -   **THEN** the results should meet the defined pass criteria.
2.  **Boundary Scenario** 🟡:
    -   **GIVEN** the system is operating at its limits,
    -   **WHEN** the boundary test case is executed,
    -   **THEN** the system should respond within acceptable thresholds.
3.  **Fault/Negative Scenario** 🔴:
    -   **GIVEN** a fault is injected into the system,
    -   **WHEN** the fault scenario is executed,
    -   **THEN** the system should detect the fault and recover
        appropriately.

::: important
::: title
Important
:::

Each scenario must be documented thoroughly to ensure traceability and
compliance with standards such as DO-178C and ISO 26262.
:::

**Additional Deep-Dive Notes**
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- **Domain Focus**:
General - **Phase Focus**: HIL - **Evidence Priorities**: functional
correctness, timing behavior, robustness, and traceability. -
**Patterns**: baseline-first comparison, fixed acceptance thresholds,
deterministic reruns. - **Anti-Patterns**: post-hoc threshold tuning,
missing raw artifacts, incomplete negative-path checks. - **Pitfalls**:
hidden assumptions, interface timing drift, weak requirement-to-test
linkage. - **Example Expansion**: include one nominal, one boundary, and
one fault scenario per objective. - **Review Heuristic**: if a claim
cannot be tied to an artifact, mark confidence as provisional. -
**Checklist Extension**: capture residual risk, ownership, and next
action for each unresolved item.

::: warning
::: title
Warning
:::

Always validate that your testing environment mirrors the production
environment to avoid discrepancies in results.
:::

  Scenario Type             Description                                                      Severity
  ------------------------- ---------------------------------------------------------------- ----------
  Nominal Scenario          Execute a standard test case with explicit pass/fail criteria.   🟢
  Boundary Scenario         Test near operational limits to assess system robustness.        🟡
  Fault/Negative Scenario   Simulate faults to evaluate detection and recovery behavior.     🔴
  Rerun Consistency Check   Verify repeatability of results under identical conditions.      🟢

  : Exercise Overview
