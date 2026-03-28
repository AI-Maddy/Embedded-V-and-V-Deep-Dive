# 🛰️ Day28 Compliance Mapping

## 🎯 Day Objective

Build practical confidence in this topic by producing requirement-linked
and review-ready evidence. **Mnemonic: C.A.R.E.** (Confidence,
Artifacts, Review, Evidence)

## 📌 Phase Context: HIL

This day emphasizes **real-time integration confidence on representative
hardware and buses**. The Hardware-in-the-Loop (HIL) testing phase is
crucial for validating embedded systems against their requirements in a
controlled environment. It ensures that the software and hardware
components interact correctly, providing a reliable platform for system
validation.

## 🧠 Concept Drilldown

-   **Primary Mechanism**: What signal, state, or computation governs
    expected behavior. This is the foundation of your testing strategy.
    Understanding the primary mechanism allows for targeted testing and
    effective troubleshooting.
-   **Boundary Conditions**: Where nominal assumptions start to break.
    Understanding these limits is key to ensuring system robustness.
    Testing at boundaries helps identify potential failure points before
    they occur in real-world scenarios.
-   **Safety Impact**: How failure propagates into system-level risk.
    Identifying potential failure modes helps in mitigating risks. A
    thorough analysis of safety impacts can lead to better design
    choices and enhanced system reliability.
-   **Verification Hook**: What observable artifact proves correctness.
    This artifact serves as the evidence of compliance with
    requirements. Artifacts such as logs, traces, and plots are
    essential for demonstrating that the system meets its
    specifications.

## 🛠️ Execution Workflow

1.  **Define Acceptance Criteria**: Establish clear and measurable
    pass/fail thresholds to guide testing. This clarity ensures that all
    stakeholders understand the success criteria.
2.  **Configure Baseline Scenario**: Set up a scenario with explicit
    assumptions to create a controlled environment. This baseline is
    critical for comparing results across different test runs.
3.  **Execute Nominal Run**: Capture primary artifacts during the
    nominal execution to establish a baseline for comparison. This run
    should reflect typical operational conditions.
4.  **Execute Stress/Fault Variants**: Record divergence behavior under
    stress or fault conditions to assess system resilience. This step is
    vital for understanding how the system behaves under less-than-ideal
    circumstances.
5.  **Consolidate Verdicts**: Use traceability links to connect results
    back to requirements and ensure comprehensive coverage. This step
    solidifies the relationship between testing outcomes and system
    requirements.

## 📊 Metrics and Evidence

-   **Functional Correctness**: Validate against requirement intent to
    ensure the system behaves as expected. This metric is fundamental
    for assessing system performance.
-   **Timing Profile**: Measure latency, jitter, and deadline adherence
    where applicable to assess performance. Timing metrics are critical
    in real-time systems where timing failures can lead to catastrophic
    results.
-   **Robustness**: Test under invalid, noisy, and edge inputs to
    evaluate system stability. Robustness testing ensures that the
    system can handle unexpected inputs gracefully.
-   **Evidence Completeness**: Compare against the planned scenario
    matrix to ensure all aspects are covered. A thorough review of
    evidence ensures that no critical areas are overlooked.

## ⚠️ Common Failure Modes

-   **Ambiguous Acceptance Criteria**: Lack of clarity can lead to
    inconsistent results before test execution. Clear criteria are
    essential for reliable testing outcomes.
-   **Hidden Model/Configuration Drift**: Variations between runs can
    obscure true system performance. Regular checks and balances are
    necessary to maintain consistency.
-   **Overlooking Degraded-Mode Checks**: Failing to test recovery paths
    can lead to unanticipated failures. Testing should include scenarios
    that simulate degraded performance.
-   **Incomplete Artifact Naming/Versioning**: Proper documentation is
    essential for traceability. Each artifact must be clearly named and
    versioned to avoid confusion.

## ✅ Required Deliverables

-   **Scenario Matrix**: Map objectives to scenarios clearly. This
    matrix should be comprehensive and easy to understand.
-   **Raw Logs/Traces/Plots**: Include timestamps for all artifacts
    collected. Accurate logging is crucial for post-test analysis.
-   **Requirement-Linked Verdict Summary**: Summarize findings with
    direct links to requirements. This summary provides a clear overview
    of compliance status.
-   **Residual-Risk and Next-Action List**: Identify unresolved issues
    and their ownership. This list is essential for ensuring that all
    risks are managed appropriately.

## 🔍 Reviewer Checklist

::: note
::: title
Note
:::

\- Are pass/fail rules explicit and reproducible? ☐ - Is each key claim
backed by a concrete artifact? ☐ - Are failures triaged with severity
and owner? ☐ - Is handoff quality sufficient for the next phase? ☐
:::

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

🔑 GIVEN / WHEN / THEN Scenarios
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- **Nominal
Scenario 🟢**: - **GIVEN** a configured system with valid inputs, -
**WHEN** the system executes the nominal run, - **THEN** the outputs
should match the expected results.

-   **Boundary Scenario 🟡**:
    -   **GIVEN** a system operating at the edge of its specifications,
    -   **WHEN** subjected to boundary conditions,
    -   **THEN** the system should maintain stability without failure.
-   **Fault Scenario 🔴**:
    -   **GIVEN** a system with a known fault injected,
    -   **WHEN** the system is executed,
    -   **THEN** it should trigger the appropriate error handling
        mechanisms.
-   **Checklist Extension**: Capture residual risk, ownership, and next
    action for each unresolved item.

::: important
::: title
Important
:::

\- Always ensure that your testing strategy aligns with relevant
standards such as DO-178C, DO-254, ISO 26262, IEC 62304, ARP4754A/4761,
and ASPICE to maintain compliance and quality assurance in embedded
systems development.
:::

::: warning
::: title
Warning
:::

\- Neglecting to follow the outlined processes can lead to significant
compliance and safety issues, potentially resulting in costly recalls or
system failures.
:::

::: admonition
\- Remember to document every step meticulously, as thorough
documentation is key to successful V&V in embedded systems.
:::

::: important
::: title
Important
:::

\- Engage with stakeholders regularly to ensure alignment on objectives
and expectations throughout the HIL testing phase.
:::
