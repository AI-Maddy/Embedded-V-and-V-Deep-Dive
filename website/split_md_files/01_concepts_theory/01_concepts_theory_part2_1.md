    artifacts, incomplete negative-path checks.
-   **Pitfalls** ⚠️: Hidden assumptions, interface timing drift, weak
    requirement-to-test linkage.
-   **Example Expansion** 🔬: Include one nominal, one boundary, and one
    fault scenario per objective.
-   **Review Heuristic** 🧠: If a claim cannot be tied to an artifact,
    mark confidence as provisional.
-   **Checklist Extension** 📋: Capture residual risk, ownership, and
    next action for each unresolved item.

## Tabular Summary 📊

  Priority                    Focus Area                   Standards Reference
  --------------------------- ---------------------------- ---------------------
  🟢 Functional Correctness   Plant and Controller Logic   DO-178C, ISO 26262
  🟡 Timing Behavior          Interface Contracts          ARP4754A
  🔴 Robustness               Fault Scenarios              DO-254, IEC 62304
  🟢 Traceability             Requirements and Artifacts   ISO 26262

  : Evidence Priorities and Focus Areas

::: admonition
Final Note Ensure all captured evidence is actionable, traceable, and
review-ready for downstream phases.
:::
