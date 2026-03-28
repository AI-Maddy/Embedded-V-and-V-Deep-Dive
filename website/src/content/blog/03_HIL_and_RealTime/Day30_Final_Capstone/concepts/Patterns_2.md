---
title: "Patterns"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🧭 **Patterns**

\### Define Invariants First, Then Derive Measurable Checks

-   Invariants are the properties that remain unchanged throughout the
    system\'s operation.
-   Measurable checks are the tests that can be used to verify these
    invariants.

\### Keep Interface Contracts Explicit (Units, Ranges, Rates)

-   Interface contracts are the agreements between components regarding
    the exchange of data.
-   These contracts should be explicit and well-defined.

\### Map Each Concept to at Least One Evidence Artifact

-   Evidence artifacts are the tangible results of the verification
    process.
-   Each concept should be mapped to at least one evidence artifact.

🚫 **Anti-Patterns** \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Explaining Theory Without Measurable Acceptance Criteria

-   Theory without measurable acceptance criteria is not sufficient for
    verification.
-   Acceptance criteria should be well-defined and measurable.

\### Treating Boundary Behavior as Optional

-   Boundary behavior is not optional; it is critical for ensuring the
    correct operation of the system.
-   Boundary behavior should be properly addressed.

\### Using Undocumented Assumptions During Analysis

-   Undocumented assumptions can lead to incorrect conclusions.
-   Assumptions should be well-documented and properly addressed.

⚠️ **Pitfalls** \-\-\-\-\-\-\-\-\-\-\-\-\--

\### Hidden Model/Configuration Drift Across Runs

-   Model/configuration drift can lead to incorrect conclusions.
-   The model/configuration should be properly validated and verified.

\### Mixing Requirement Intent with Implementation Details

-   Mixing requirement intent with implementation details can lead to
    confusion.
-   Requirements and implementation details should be properly
    separated.

\### Missing Traceability Links in Review Notes

-   Missing traceability links can make it difficult to understand the
    verification process.
-   Traceability links should be properly maintained.
