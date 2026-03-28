# 🔍 Reviewer Checklist 🔍

☐ Are pass/fail rules explicit and reproducible? ☐ Is each key claim
backed by a concrete artifact? ☐ Are failures triaged with severity and
owner? ☐ Is handoff quality sufficient for the next phase? ☐ Are all
domain standards (DO-178C, DO-254, ISO 26262, IEC 62304, ARP4754A/4761,
ASPICE) properly considered? ☐ Are all required deliverables complete
and accurate?

Additional Deep-Dive Notes 📝
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   **Domain Focus**: General
-   **Phase Focus**: HIL
-   **Evidence Priorities**: Functional correctness, timing behavior,
    robustness, and traceability
-   **Patterns**: Baseline-first comparison, fixed acceptance
    thresholds, deterministic reruns
-   **Anti-Patterns**: Post-hoc threshold tuning, missing raw artifacts,
    incomplete negative-path checks
-   **Pitfalls**: Hidden assumptions, interface timing drift, weak
    requirement-to-test linkage
-   **Example Expansion**: Include one nominal, one boundary, and one
    fault scenario per objective
-   **Review Heuristic**: If a claim cannot be tied to an artifact, mark
    confidence as provisional
-   **Checklist Extension**: Capture residual risk, ownership, and next
    action for each unresolved item

::: warning
::: title
Warning
:::

Ensure all reviewer checklist items are completed before proceeding to
the next phase.
:::

::: important
::: title
Important
:::

Verify that all required deliverables are complete and accurate before
submitting for review.
:::

::: admonition
Reviewer feedback is essential for ensuring the quality and completeness
of the evidence.
:::
