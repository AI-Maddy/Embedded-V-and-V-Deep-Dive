Medical Infusion Pump Use Cases and Examples 🏥💊
==============================================

🟢 **Domain-Specific Mnemonic:** MIPUSE (Medical Infusion Pump Use
Scenarios and Evidence)

Purpose 🤔 \-\-\-\-\-\--🟢 **Nominal** (Expected Behavior) 🟡
**Boundary** (Edge Cases) 🔴 **Fault** (Error Conditions) Provide
domain-tailored use cases with evidence expectations aligned to **IEC
62304 + ISO 14971 + IEC 60601 context**.

Representative Use Cases 📝
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--### 1. Nominal
Mission/Profile Operation 🟢

-   GIVEN: Infusion pump is calibrated and configured correctly.

-   WHEN: User initiates therapy control with validated sensor feedback.

-   THEN: Pump delivers accurate and consistent medication dosages.

    ::: note
    ::: title
    Note
    :::

    This scenario is critical for ensuring the safety and efficacy of
    the infusion pump.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper calibration and configuration are essential for accurate
    dosing.
    :::

    ::: admonition
    This scenario demonstrates proper therapy control with validated
    sensor feedback.
    :::

\### 2. Boundary-Condition Operation near Limits 🟡

-   GIVEN: Infusion pump is operating near its capacity limits (e.g.,
    maximum flow rate).

-   WHEN: User attempts to initiate therapy control with near-threshold
    dosing.

-   THEN: Pump alerts user with timely and relevant alarm escalation.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly test boundary conditions may result in product
    failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper testing of boundary conditions is essential for ensuring
    infusion pump performance.
    :::

    ::: note
    ::: title
    Note
    :::

    This scenario demonstrates proper alarm escalation timing.
    :::

\### 3. Fault Detection, Containment, and Recovery 🔴

-   GIVEN: Infusion pump detects a sensor spike or dropout.

-   WHEN: Pump initiates actuator command rejection path.

-   THEN: Pump safely halts therapy and alerts user with error message.

    ::: important
    ::: title
    Important
    :::

    Proper fault detection and containment are essential for ensuring
    patient safety.
    :::

    ::: note
    ::: title
    Note
    :::

    This scenario demonstrates proper fault detection and containment.
    :::

    ::: admonition
    This scenario is critical for ensuring infusion pump can handle
    faults.
    :::

\### 4. Degraded-Mode Continuation with Safety Constraints 🟢

-   GIVEN: Infusion pump experiences a partial failure (e.g., reduced
    flow rate).

-   WHEN: User continues therapy with safety constraints in place.

-   THEN: Pump maintains safe and consistent medication delivery.

    ::: note
    ::: title
    Note
    :::

    This scenario is critical for ensuring infusion pump can continue to
    operate safely in degraded modes.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper safety constraints are essential for ensuring patient safety.
    :::

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly implement safety constraints may result in
    product failures or safety issues.
    :::

\### 5. Regression Stability after Fixes 🟡

-   GIVEN: Infusion pump has undergone software updates or hardware
    modifications.

-   WHEN: User verifies therapy control with validated sensor feedback.

-   THEN: Pump demonstrates stable and accurate performance.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly test regression stability may result in product
    failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper testing of regression stability is essential for ensuring
    infusion pump performance.
    :::

    ::: note
    ::: title
    Note
    :::

    This scenario demonstrates proper regression stability.
    :::

Domain-Specific Examples 📚
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--### Example A (Nominal)
🟢

-   Therapy control with validated sensor feedback.

-   Evidence: Pump calibration and configuration records.

-   Compliance: IEC 60601-1:2012, Clause 8.2.1.

    ::: note
    ::: title
    Note
    :::

    This example demonstrates proper therapy control with validated
    sensor feedback.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper calibration and configuration are essential for accurate
    dosing.
    :::

    ::: admonition
    This example demonstrates proper therapy control.
    :::

\### Example B (Boundary) 🟡

-   Near-threshold dosing and alarm escalation timing.

-   Evidence: Pump performance data and user feedback.

-   Compliance: IEC 60601-1:2012, Clause 8.2.2.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly test boundary conditions may result in product
    failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper testing of boundary conditions is essential for ensuring
    infusion pump performance.
    :::

    ::: note
    ::: title
    Note
    :::

    This example demonstrates proper alarm escalation timing.
    :::

\### Example C (Fault) 🔴

-   Sensor spike/dropout and actuator command rejection path.

-   Evidence: Pump error logs and user feedback.

-   Compliance: IEC 60601-1:2012, Clause 8.2.3.

    ::: important
    ::: title
    Important
    :::

    Proper fault detection and containment are essential for ensuring
    patient safety.
    :::

    ::: note
    ::: title
    Note
    :::

    This example demonstrates proper fault detection and containment.
    :::

    ::: admonition
    This example demonstrates proper fault detection and containment.
    :::

Patterns 📈 \-\-\-\-\-\-\--### 1. Map each scenario to requirement and
hazard identifiers 🟢

-   Use a single, standardized notation for requirement and hazard IDs.

-   Ensure clear and concise descriptions for each ID.

    ::: note
    ::: title
    Note
    :::

    This pattern ensures clear and concise descriptions for each ID.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper mapping is essential for ensuring requirements are properly
    linked to test cases.
    :::

    ::: admonition
    This pattern ensures that requirements are properly linked to test
    cases.
    :::

\### 2. Use one baseline artifact set for comparison across variants 🟡

-   Establish a common reference point for artifact comparison.

-   Ensure artifacts are properly version-controlled and tracked.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly use a baseline artifact set may result in
    product failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper use of a baseline artifact set is essential for ensuring
    consistency and reproducibility.
    :::

    ::: note
    ::: title
    Note
    :::

    This pattern ensures consistency and reproducibility across
    variants.
    :::

\### 3. Preserve raw captures alongside interpreted findings 🔴

-   Store raw data and logs alongside interpreted results.

-   Ensure data integrity and availability for future reference.

    ::: important
    ::: title
    Important
    :::

    Proper preservation of raw captures is essential for ensuring data
    integrity and availability.
    :::

    ::: note
    ::: title
    Note
    :::

    This pattern ensures that raw data and logs are properly captured
    and stored.
    :::

Anti-Patterns 🚫 \-\-\-\-\-\-\-\-\-\-\-\--### 1. Broad "pass" claims
without scenario-level evidence 🔴

-   Avoid making general claims without specific evidence.

-   Provide detailed scenario-level evidence to support claims.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly provide scenario-level evidence may result in
    product failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper evidence is essential for ensuring claims are properly
    supported.
    :::

    ::: note
    ::: title
    Note
    :::

    This anti-pattern ensures that claims are properly supported with
    evidence.
    :::

\### 2. Missing boundary/fault test depth for high-risk functions 🟡

-   Ensure thorough testing of high-risk functions.

-   Identify and address any gaps in testing coverage.

    ::: note
    ::: title
    Note
    :::

    This anti-pattern ensures that high-risk functions are properly
    tested.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper testing is essential for ensuring patient safety.
    :::

    ::: admonition
    This anti-pattern ensures that high-risk functions are properly
    tested.
    :::

\### 3. Compliance references without concrete verification links 🟢

-   Provide clear and direct links to compliance evidence.

-   Ensure evidence is properly documented and accessible.

    ::: note
    ::: title
    Note
    :::

    This anti-pattern ensures that compliance references are properly
    linked to evidence.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper documentation and accessibility of evidence are essential for
    ensuring compliance.
    :::

    ::: admonition
    This anti-pattern ensures that compliance references are properly
    linked to evidence.
    :::

Pitfalls 🚨 \-\-\-\-\-\-\--### 1. Underestimating interface timing
effects 🟡

-   Consider the potential impact of interface timing on system
    behavior.

-   Ensure thorough testing of interface timing effects.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly consider interface timing effects may result in
    product failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper consideration of interface timing effects is essential for
    ensuring system behavior.
    :::

    ::: note
    ::: title
    Note
    :::

    This pitfall ensures that interface timing effects are properly
    considered.
    :::

\### 2. Incomplete alarm/fallback path verification 🔴

-   Verify that alarm and fallback paths are properly implemented.

-   Ensure that these paths are thoroughly tested and validated.

    ::: important
    ::: title
    Important
    :::

    Proper verification of alarm and fallback paths is essential for
    ensuring patient safety.
    :::

    ::: note
    ::: title
    Note
    :::

    This pitfall ensures that alarm and fallback paths are properly
    implemented and tested.
    :::

    ::: admonition
    This pitfall ensures that alarm and fallback paths are properly
    implemented and tested.
    :::

\### 3. Weak ownership for unresolved risks 🟢

-   Clearly assign ownership for unresolved risks.

-   Ensure that owners are properly trained and equipped to address
    these risks.

    ::: note
    ::: title
    Note
    :::

    This pitfall ensures that ownership for unresolved risks is properly
    assigned.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper training and equipment of owners are essential for ensuring
    that risks are properly addressed.
    :::

    ::: admonition
    This pitfall ensures that ownership for unresolved risks is properly
    assigned.
    :::

Best Practices 🏆 \-\-\-\-\-\-\-\-\-\-\-\-\--### 1. Keep scenario
definitions deterministic and reproducible 🟢

-   Ensure that scenario definitions are clear and concise.

-   Use standardized notation and formatting for scenario definitions.

    ::: note
    ::: title
    Note
    :::

    This best practice ensures that scenario definitions are clear and
    concise.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper notation and formatting are essential for ensuring
    reproducibility.
    :::

    ::: admonition
    This best practice ensures that scenario definitions are clear and
    concise.
    :::

\### 2. Use quantitative pass/fail thresholds 🟡

-   Establish clear and objective pass/fail criteria.

-   Ensure that these criteria are properly documented and communicated.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly use quantitative pass/fail thresholds may result
    in product failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper use of quantitative pass/fail thresholds is essential for
    ensuring system behavior.
    :::

    ::: note
    ::: title
    Note
    :::

    This best practice ensures that pass/fail criteria are clear and
    objective.
    :::

\### 3. Review residual risk before release recommendation 🔴

-   Thoroughly review residual risk before releasing a product.

-   Ensure that owners are properly trained and equipped to address
    these risks.

    ::: important
    ::: title
    Important
    :::

    Proper review of residual risk is essential for ensuring patient
    safety.
    :::

    ::: note
    ::: title
    Note
    :::

    This best practice ensures that residual risk is properly reviewed.
    :::

    ::: admonition
    This best practice ensures that residual risk is properly reviewed.
    :::

Checklist 📝 \-\-\-\-\-\-\-\--☐ Nominal/boundary/fault scenarios are
covered. ☐ Evidence is traceable and auditable. ☐ Compliance mapping is
explicit. ☐ Open issues include priority and owner.

Additional Deep-Dive Notes 📚
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--### Domain Focus:
Medical 🟢

-   Focus on medical infusion pump use cases and evidence.

    ::: note
    ::: title
    Note
    :::

    This focus ensures that use cases and evidence are properly aligned
    to the medical domain.
    :::

\### Phase Focus: Cross-Phase 🔴

-   Consider use cases and evidence across multiple phases.

    ::: important
    ::: title
    Important
    :::

    Proper consideration of use cases and evidence across multiple
    phases is essential for ensuring patient safety.
    :::

    ::: note
    ::: title
    Note
    :::

    This focus ensures that use cases and evidence are properly
    considered across multiple phases.
    :::

\### Evidence Priorities: functional correctness, timing behavior,
robustness, and traceability 🟡

-   Prioritize evidence collection and analysis based on these criteria.

    ::: note
    ::: title
    Note
    :::

    This prioritization ensures that evidence collection and analysis
    are properly aligned to these criteria.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper prioritization is essential for ensuring that evidence is
    properly collected and analyzed.
    :::

    ::: admonition
    This prioritization ensures that evidence collection and analysis
    are properly aligned to these criteria.
    :::

\### Patterns: baseline-first comparison, fixed acceptance thresholds,
deterministic reruns 🟢

-   Use these patterns to ensure consistency and reproducibility.

    ::: note
    ::: title
    Note
    :::

    These patterns ensure consistency and reproducibility.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper use of these patterns is essential for ensuring consistency
    and reproducibility.
    :::

    ::: admonition
    These patterns ensure consistency and reproducibility.
    :::

\### Anti-Patterns: post-hoc threshold tuning, missing raw artifacts,
incomplete negative-path checks 🔴

-   Avoid these anti-patterns to ensure thorough and accurate testing.

    ::: warning
    ::: title
    Warning
    :::

    Failure to properly avoid these anti-patterns may result in product
    failures or safety issues.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper avoidance of these anti-patterns is essential for ensuring
    thorough and accurate testing.
    :::

    ::: note
    ::: title
    Note
    :::

    This anti-pattern ensures that testing is thorough and accurate.
    :::

\### Pitfalls: hidden assumptions, interface timing drift, weak
requirement-to-test linkage 🟡

-   Consider these pitfalls when designing and testing use cases.

    ::: note
    ::: title
    Note
    :::

    These pitfalls ensure that use cases are properly designed and
    tested.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper consideration of these pitfalls is essential for ensuring
    patient safety.
    :::

    ::: admonition
    These pitfalls ensure that use cases are properly designed and
    tested.
    :::

\### Example Expansion: include one nominal, one boundary, and one fault
scenario per objective 🟢

-   Use these scenarios to demonstrate use case coverage.

    ::: note
    ::: title
    Note
    :::

    These scenarios demonstrate use case coverage.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper use of these scenarios is essential for ensuring use case
    coverage.
    :::

    ::: admonition
    These scenarios demonstrate use case coverage.
    :::

\### Review Heuristic: if a claim cannot be tied to an artifact, mark
confidence as provisional 🔴

-   Use this heuristic to ensure that claims are properly supported.

    ::: important
    ::: title
    Important
    :::

    Proper use of this heuristic is essential for ensuring that claims
    are properly supported.
    :::

    ::: note
    ::: title
    Note
    :::

    This heuristic ensures that claims are properly supported.
    :::

    ::: admonition
    This heuristic ensures that claims are properly supported.
    :::

\### Checklist Extension: capture residual risk, ownership, and next
action for each unresolved item 🟡

-   Use this checklist to track and address open issues.

    ::: note
    ::: title
    Note
    :::

    This checklist ensures that open issues are properly tracked and
    addressed.
    :::

    ::: important
    ::: title
    Important
    :::

    Proper use of this checklist is essential for ensuring that open
    issues are properly tracked and addressed.
    :::

    ::: admonition
    This checklist ensures that open issues are properly tracked and
    addressed.
    :::

Table of Compliance References 📚
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  ----------------------------------- -----------------------------------
  Reference                           Description

  IEC 60601-1:2012                    Medical electrical equipment - Part
                                      1: General requirements for basic
                                      safety and essential performance

  IEC 62304                           Medical device software - Software
                                      life cycle processes

  ISO 14971                           Medical devices - Application of
                                      risk management to medical devices
  ----------------------------------- -----------------------------------

Table of Evidence Priorities 📝
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  ----------------------------------- -----------------------------------
  Priority                            Description

  Functional Correctness              Ensure that the system performs its
                                      intended functions correctly

  Timing Behavior                     Ensure that the system behaves
                                      correctly in terms of timing and
                                      synchronization

  Robustness                          Ensure that the system can
                                      withstand various types of faults
                                      and errors

  Traceability                        Ensure that the system can provide
                                      clear and unambiguous evidence of
                                      its behavior
  ----------------------------------- -----------------------------------

Table of Patterns and Anti-Patterns 📈
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  ----------------------------------- -----------------------------------
  Pattern/Anti-Pattern                Description

  Baseline-First Comparison           Compare artifacts against a common
                                      baseline

  Fixed Acceptance Thresholds         Use fixed thresholds for acceptance
                                      criteria

  Deterministic Reruns                Ensure that reruns of scenarios are
                                      deterministic and reproducible

  Post-Hoc Threshold Tuning           Avoid adjusting thresholds after
                                      the fact

  Missing Raw Artifacts               Ensure that raw data and logs are
                                      properly captured and stored

  Incomplete Negative-Path Checks     Ensure that all possible negative
                                      paths are thoroughly tested
  ----------------------------------- -----------------------------------

Table of Pitfalls 🚨 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  ----------------------------------- -----------------------------------
  Pitfall                             Description

  Hidden Assumptions                  Avoid making assumptions about
                                      system behavior without clear
                                      evidence

  Interface Timing Drift              Consider the potential impact of
                                      interface timing on system behavior

  Weak Requirement-to-Test Linkage    Ensure that requirements are
                                      properly linked to test cases
  ----------------------------------- -----------------------------------

Table of Best Practices 🏆 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  ----------------------------------- -----------------------------------
  Best Practice                       Description

  Keep Scenario Definitions           Ensure that scenario definitions
  Deterministic and Reproducible      are clear and concise

  Use Quantitative Pass/Fail          Establish clear and objective
  Thresholds                          pass/fail criteria

  Review Residual Risk Before Release Thoroughly review residual risk
  Recommendation                      before releasing a product
  ----------------------------------- -----------------------------------

::: note
::: title
Note
:::

This document is intended to provide guidance and best practices for use
case development and evidence collection. It is not a substitute for
regulatory requirements or industry standards.
:::

::: warning
::: title
Warning
:::

Failure to properly develop and test use cases may result in product
failures or safety issues.
:::

::: important
::: title
Important
:::

Use case development and evidence collection should be performed in
accordance with relevant regulatory requirements and industry standards.
:::

::: admonition
This document is intended for use by medical infusion pump developers
and testers. It is not intended for use by the general public.
:::
