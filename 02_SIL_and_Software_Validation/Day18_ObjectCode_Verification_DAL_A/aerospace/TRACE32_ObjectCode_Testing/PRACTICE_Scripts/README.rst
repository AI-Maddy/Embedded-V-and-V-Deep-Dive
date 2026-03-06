Aerospace Focus — Day18 ObjectCode Verification DAL A
=====================================================

Objective
---------
Apply this day in **Aerospace** context with explicit safety, compliance, and evidence expectations.

Phase Context
-------------
Phase: **SIL**
Primary focus: **software-level correctness, robustness, and structural evidence**.
Section focus: **aerospace verification workflow**.

Domain Constraints
------------------
- Compliance baseline: **DO-178C/DO-254 + ARP4754A/ARP4761**
- Key hazard profile: loss of control authority, unstable mode transition, stale avionics data
- Interface landscape: ARINC 429/664, AFDX, discrete I/O

Domain-Specific Examples
------------------------
- Nominal: stable flight-control mode tracking with expected disturbances.
- Boundary: high-workload transition envelope near stability margins.
- Fault: bus label corruption and sensor disagreement event.

Patterns
--------
- Derive acceptance thresholds from hazard-linked requirements.
- Keep interface timing contracts explicit and reviewable.
- Compare nominal and stressed traces against the same baseline.

Anti-Patterns
-------------
- Generic test claims without domain hazard mapping.
- Pass/fail decisions without quantitative thresholds.
- Evidence summaries without raw artifact references.

Pitfalls
--------
- Hidden assumptions in environment or calibration setup.
- Missing negative-path scenarios for high-criticality behavior.
- Incomplete traceability from requirement to verdict.

Best Practices
--------------
- Tag every artifact with domain requirement IDs.
- Capture timing + functional evidence in the same run package.
- Record residual risk and ownership before closure.

Heuristics
----------
- If a domain hazard is untested, confidence is provisional.
- If rerun differs unexpectedly, investigate determinism first.
- If evidence is indirect, reduce verdict confidence level.

Checklist
---------
- Domain hazard coverage is explicit.
- Compliance references are mapped to evidence.
- Nominal/boundary/fault results are all documented.
- Residual risks and next actions are assigned.
