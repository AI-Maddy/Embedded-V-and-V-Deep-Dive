# Additional Deep-Dive Notes 📘

-   **Domain Focus**: Automotive
-   **Phase Focus**: Model-in-the-Loop (MIL)
-   **Evidence Priorities**:
    -   Functional correctness
    -   Timing behavior
    -   Robustness under fault conditions
    -   Traceability to requirements
-   **Patterns**:
    -   Baseline-first comparison for all test cases
    -   Fixed acceptance thresholds for timing and functional
        performance
    -   Deterministic reruns to ensure reproducibility
-   **Anti-Patterns**:
    -   Post-hoc threshold tuning without justification
    -   Missing raw artifacts for traceability
    -   Incomplete negative-path checks
-   **Pitfalls**:
    -   Hidden assumptions in test setups
    -   Interface timing drift leading to non-deterministic behavior
    -   Weak requirement-to-test linkage
-   **Example Expansion**: Include one nominal 🟢, one boundary 🟡, and
    one fault 🔴 scenario per objective.
-   **Review Heuristic**: If a claim cannot be tied to an artifact, mark
    confidence as provisional and escalate for review.
-   **Checklist Extension**: Capture residual risk, ownership, and next
    action for each unresolved item.
