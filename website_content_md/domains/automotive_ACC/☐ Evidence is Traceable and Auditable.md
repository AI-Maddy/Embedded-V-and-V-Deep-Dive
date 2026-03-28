# ☐ Evidence is Traceable and Auditable

-   Ensure that evidence is traceable and auditable
-   Use a consistent naming convention for evidence types

☐ Compliance Mapping is Explicit =============================

-   Ensure that compliance mapping is explicit
-   Use a consistent naming convention for compliance references

☐ Open Issues include Priority and Owner
=====================================

-   Ensure that open issues include priority and owner
-   Use a consistent naming convention for open issues

☐ Review Heuristic is Applied ==========================

-   Apply the review heuristic to mark confidence as provisional if a
    claim cannot be tied to an artifact
-   Use a consistent naming convention for review heuristics

Additional Deep-Dive Notes 📝
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Domain Focus: Automotive

-   The domain focus is automotive
-   Use a consistent naming convention for domain-specific terms

\### Phase Focus: Cross-Phase

-   The phase focus is cross-phase
-   Use a consistent naming convention for phase-specific terms

\### Evidence Priorities: Functional Correctness, Timing Behavior,
Robustness, and Traceability

-   The evidence priorities are functional correctness, timing behavior,
    robustness, and traceability
-   Use a consistent naming convention for evidence priorities

\### Patterns: Baseline-First Comparison, Fixed Acceptance Thresholds,
Deterministic Reruns

-   The patterns are baseline-first comparison, fixed acceptance
    thresholds, and deterministic reruns
-   Use a consistent naming convention for patterns

\### Anti-Patterns: Post-Hoc Threshold Tuning, Missing Raw Artifacts,
Incomplete Negative-Path Checks

-   The anti-patterns are post-hoc threshold tuning, missing raw
    artifacts, and incomplete negative-path checks
-   Use a consistent naming convention for anti-patterns

\### Pitfalls: Hidden Assumptions, Interface Timing Drift, Weak
Requirement-to-Test Linkage

-   The pitfalls are hidden assumptions, interface timing drift, and
    weak requirement-to-test linkage
-   Use a consistent naming convention for pitfalls

\### Example Expansion: Include One Nominal, One Boundary, and One Fault
Scenario per Objective

-   Include one nominal, one boundary, and one fault scenario per
    objective
-   Use a consistent naming convention for scenario types

\### Review Heuristic: If a Claim Cannot be Tied to an Artifact, Mark
Confidence as Provisional

-   Use a review heuristic to mark confidence as provisional if a claim
    cannot be tied to an artifact
-   Use a consistent naming convention for review heuristics

\### Checklist Extension: Capture Residual Risk, Ownership, and Next
Action for Each Unresolved Item

-   Capture residual risk, ownership, and next action for each
    unresolved item
-   Use a consistent naming convention for checklist extensions

Standards References: ARP4754A/4761, ASPICE, DO-178C, DO-254, IEC 62304,
ISO 26262, ISO 21434

  -------------------- ----------------- ----------------- -----------------
  Scenario             Requirement       Hazard            Priority

  Nominal              Functional        Loss of Control   High
  Mission/Profile      Correctness                         
  Operation                                                

  Boundary-Condition   Timing Behavior   Collision         Medium
  Operation Near                                           
  Limits                                                   

  Fault Detection,     Robustness        System Failure    High
  Containment, and                                         
  Recovery                                                 

  Degraded-Mode        Functional        Loss of Control   Medium
  Continuation with    Correctness                         
  Safety Constraints                                       

  Regression Stability Timing Behavior   Collision         Low
  after Fixes                                              
  -------------------- ----------------- ----------------- -----------------

  : Mapping of Scenarios to Requirements and Hazards

Note: This is a sample mapping of scenarios to requirements and hazards.
The actual mapping will depend on the specific system and its
requirements.
