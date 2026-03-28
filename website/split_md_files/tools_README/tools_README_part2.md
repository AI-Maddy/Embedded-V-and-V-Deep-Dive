-   ISO 26262 (Functional Safety for Road Vehicles) 🟡
-   IEC 62304 (Medical Device Software - Software Life Cycle Processes)
    🟡
-   ARP4754A/4761 (System and Software Integrity Plans) 🔴
-   ASPICE (Automotive Safety Integrity Level Process for E/E Systems)
    🔴

\### Patterns and Anti-Patterns
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Patterns \-\-\-\-\-\-\-\-\-\--

-   Baseline-first comparison 🟢
-   Fixed acceptance thresholds 🟢
-   Deterministic reruns 🟢

\### Anti-Patterns \-\-\-\-\-\-\-\-\-\-\-\-\--

-   Post-hoc threshold tuning 🔴
-   Missing raw artifacts 🔴
-   Incomplete negative-path checks 🔴

\### Review Heuristic \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   If a claim cannot be tied to an artifact, mark confidence as
    provisional. 🟢

\### Checklist Extension \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   Capture residual risk
-   Ownership
-   Next action for each unresolved item

\### Example Expansion \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   Include one nominal, one boundary, and one fault scenario per
    objective. 🟢

\### Evidence Priorities \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   Functional correctness 🟢
-   Timing behavior 🟡
-   Robustness 🔴
-   Traceability 🔴

\### Pitfalls \-\-\-\-\-\-\-\--

-   Hidden assumptions 🔴
-   Interface timing drift 🔴
-   Weak requirement-to-test linkage 🔴

\### Example Use Cases \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Nominal Scenario \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   GIVEN: The system is in a normal operating state. 🟢
-   WHEN: The user inputs a valid command. 🟢
-   THEN: The system responds correctly. 🟢

\### Boundary Scenario \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   GIVEN: The system is in a normal operating state. 🟡
-   WHEN: The user inputs an invalid command. 🟡
-   THEN: The system responds with an error message. 🟡

\### Fault Scenario \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   GIVEN: The system is in a faulty state. 🔴
-   WHEN: The user inputs a valid command. 🔴
-   THEN: The system responds with an error message. 🔴

## \### Pre-Review Checklist

☐ Review all test objectives, assumptions, and acceptance criteria. ☐
Verify that all tool configurations and runtime options are
version-controlled. ☐ Execute nominal, boundary, and fault scenarios to
validate the system\'s behavior. ☐ Export raw outputs and derived
summaries to facilitate analysis and verification. ☐ Link findings to
requirement/objective references to ensure that the system meets the
specified requirements. ☐ Verify repeatability via rerun comparison. ☐
Check data integrity (timestamps and interfaces consistent). ☐ Map
findings to objective IDs and risk statements. ☐ Review all domain
standards and ensure compliance. ☐ Identify and address any cross-tool
pitfalls. ☐ Review all patterns and anti-patterns and ensure adherence.
☐ Review the review heuristic and ensure that confidence is marked as
provisional if a claim cannot be tied to an artifact. ☐ Review the
checklist extension and ensure that residual risk, ownership, and next
action for each unresolved item are captured. ☐ Review the example
expansion and ensure that one nominal, one boundary, and one fault
scenario per objective are included. ☐ Review the evidence priorities
and ensure that functional correctness, timing behavior, robustness, and
traceability are addressed. ☐ Review the pitfalls and ensure that hidden
assumptions, interface timing drift, and weak requirement-to-test
linkage are addressed. ☐ Review the example use cases and ensure that
nominal, boundary, and fault scenarios are included.

## \### Mnemonic Acronym: V&V-VIP

V&V-VIP stands for Verification and Validation Verification Insight
Process. It is a mnemonic acronym that helps remember the key steps in
