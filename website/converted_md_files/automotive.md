# Automotive 🚗 --- Enhanced Automotive Verification Workflow 🌟

## Purpose 🎯

Document **Automotive**-specific details for Day01 VModel and
Requirements with a focus on automotive Model-in-the-Loop (MIL)
verification workflow. This enhanced version incorporates domain
standards, mnemonic aids, and structured scenario templates to ensure
robust and traceable verification practices.

**Mnemonic Acronym: DRIVE** 🚦 - **D**: Define scope, assumptions, and
constraints with precision. - **R**: Review evidence for completeness,
traceability, and compliance. - **I**: Identify critical hazards,
interfaces, and failure modes. - **V**: Validate scenarios (Nominal 🟢,
Boundary 🟡, Fault 🔴) systematically. - **E**: Ensure reproducibility,
residual risk management, and ownership.

## Domain Alignment 🌍

-   **Standard References**:
    -   ISO 26262 (ASIL) --- Functional Safety
    -   ISO 21434 --- Cybersecurity Engineering
    -   ASPICE --- Automotive SPICE Process Assessment Model
    -   IEC 62304 --- Software Lifecycle Processes
-   **Critical Hazards**:
    -   🟡 Unintended acceleration/deceleration
    -   🔴 Loss of stability during cornering
    -   🔴 Braking system faults under emergency conditions
-   **Relevant Interfaces**:
    -   CAN (Controller Area Network)
    -   LIN (Local Interconnect Network)
    -   FlexRay
    -   Automotive Ethernet

::: note
::: title
Note
:::

Ensure hazard analyses align with ISO 26262 Part 3 and ISO 21434 risk
assessment methodologies.
:::

## Verification Scenarios 🧩

**Nominal Scenario** 🟢 - GIVEN: Adaptive cruise control is active under
normal traffic conditions. - WHEN: The vehicle encounters a lead car
traveling at a steady speed. - THEN: The system maintains a safe headway
distance and adjusts speed appropriately.

**Boundary Scenario** 🟡 - GIVEN: Dense stop-and-go traffic with tight
timing constraints. - WHEN: The vehicle approaches a lead car with rapid
deceleration. - THEN: The system maintains stability while adhering to
headway limits.

**Fault Scenario** 🔴 - GIVEN: A sensor dropout occurs during
operation. - WHEN: Invalid CAN frames are injected into the network. -
THEN: The system enters a safe state, alerts the driver, and logs the
fault.

::: important
::: title
Important
:::

Each scenario must include requirement-linked checks, timing analysis,
and functional outcome validation per ISO 26262 Part 6 and ASPICE SWE.4.
:::

## Patterns 🧩

-   **Requirement-linked checks**: Ensure every test case maps to
    specific requirements.
-   **Timing and functional outcomes**: Validate timing behavior and
    functional correctness simultaneously.
-   **Reproducibility constraints**: Ensure setups are deterministic and
    repeatable for MIL simulations.

## Anti-Patterns 🚫

-   **Domain-agnostic statements**: Avoid vague criteria without
    measurable outcomes.
-   **Ignoring interface constraints**: Always consider
    protocol-specific limitations (e.g., CAN frame timing).
-   **Closing findings prematurely**: Ensure residual risks are
    explicitly documented with ownership assigned.

## Pitfalls ⚠️

-   **Missing fault variants**: Include sensor and actuator fault
    scenarios for comprehensive coverage.
-   **Weak traceability**: Ensure every objective maps to an artifact
    and is auditable.
-   **Configuration drift**: Maintain controlled setups for repeatable
    results.

## Checklist ✅

☐ Scope and assumptions are explicitly defined. ☐ Acceptance criteria
are quantitative and measurable. ☐ Evidence set is complete, auditable,
and traceable. ☐ Follow-up actions are prioritized and documented. ☐
Residual risks are captured with ownership assigned.

::: admonition
Pre-Review Checklist Before proceeding, ensure: - All hazards are
identified and analyzed (ISO 26262 Part 3). - Cybersecurity risks are
assessed (ISO 21434). - Interfaces are validated for timing and protocol
compliance. - Evidence supports all claims with artifacts and
traceability.
:::

## Additional Deep-Dive Notes 📘

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

## Tabular Summary 📊

  ------------------------------------------------------------------------
  **Category**   **Examples**          **Standards       **Priority**
                                       Alignment**       
  -------------- --------------------- ----------------- -----------------
  Nominal        Adaptive cruise       ISO 26262 Part 6  🟢
  Scenario 🟢    control under normal                    
                 traffic conditions                      

  Boundary       Stop-and-go traffic   ISO 26262 Part 3  🟡
  Scenario 🟡    with tight headway                      
                 constraints                             

  Fault Scenario Sensor dropout and    ISO 26262 Part 5  🔴
  🔴             invalid CAN frame                       
                 injection                               
  ------------------------------------------------------------------------

  : Automotive MIL Verification Summary

::: warning
::: title
Warning
:::

Ensure all test results are reviewed for compliance with ISO 26262, ISO
21434, and ASPICE SWE.6.
:::
