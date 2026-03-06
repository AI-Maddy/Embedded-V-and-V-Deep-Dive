Aerospace Use Cases and Examples
================================

Purpose
-------
Provide domain-tailored use cases with evidence expectations aligned to **DO-178C/DO-254 + ARP4754A/ARP4761**.

Representative Use Cases
------------------------
1. Nominal mission/profile operation
2. Boundary-condition operation near limits
3. Fault detection, containment, and recovery
4. Degraded-mode continuation with safety constraints
5. Regression stability after fixes

Domain-Specific Examples
------------------------
- Example A (Nominal): stable flight-control mode tracking with expected disturbances.
- Example B (Boundary): high-workload transition envelope near stability margins.
- Example C (Fault): bus label corruption and sensor disagreement event.

Patterns
--------
- Map each scenario to requirement and hazard identifiers.
- Use one baseline artifact set for comparison across variants.
- Preserve raw captures alongside interpreted findings.

Anti-Patterns
-------------
- Broad “pass” claims without scenario-level evidence.
- Missing boundary/fault test depth for high-risk functions.
- Compliance references without concrete verification links.

Pitfalls
--------
- Underestimating interface timing effects.
- Incomplete alarm/fallback path verification.
- Weak ownership for unresolved risks.

Best Practices
--------------
- Keep scenario definitions deterministic and reproducible.
- Use quantitative pass/fail thresholds.
- Review residual risk before release recommendation.

Checklist
---------
- Nominal/boundary/fault scenarios are covered.
- Evidence is traceable and auditable.
- Compliance mapping is explicit.
- Open issues include priority and owner.

Additional Deep-Dive Notes
--------------------------
- Domain Focus: Aerospace
- Phase Focus: Cross-Phase
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
