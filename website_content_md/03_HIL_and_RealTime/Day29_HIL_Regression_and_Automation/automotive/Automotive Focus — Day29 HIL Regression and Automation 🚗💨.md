# Automotive Focus --- Day29 HIL Regression and Automation 🚗💨

Objective 🎯 \-\-\-\-\-\-\-\--Apply this day in **Automotive** context
with explicit safety, compliance, and evidence expectations. The goal is
to ensure that all hardware-in-the-loop (HIL) tests are conducted with a
focus on safety-critical systems, adhering to the highest standards of
verification and validation. This aligns with our mnemonic acronym
**HIL-SAFE** (HIL Integration for Safety Assurance and Functional
Evaluation).

Phase Context 🔍 \-\-\-\-\-\-\-\-\-\-\-\--Phase: **HIL** Primary focus:
**hardware-integrated timing and interface confidence**. Section focus:
**automotive verification workflow**.

Domain Constraints 🚧 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Compliance
baseline: **ISO 26262 (ASIL) + ISO 21434** - Key hazard profile:
unintended acceleration/deceleration, loss of stability, braking
faults - Interface landscape: CAN, LIN, FlexRay, Automotive Ethernet

Domain-Specific Examples 📝
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- **Nominal** 🟢:
Adaptive cruise and speed regulation under normal traffic conditions. -
**Boundary** 🟡: Dense stop-and-go scenarios with tight headway and
timing limits. - **Fault** 🔴: Sensor dropout and invalid CAN frame
injection.

Patterns 🔄 \-\-\-\-\-\-\-\-- Derive acceptance thresholds from
hazard-linked requirements. - Keep interface timing contracts explicit
and reviewable. - Compare nominal and stressed traces against the same
baseline.

Anti-Patterns 🚫 \-\-\-\-\-\-\-\-\-\-\-\-\-- Generic test claims without
domain hazard mapping. - Pass/fail decisions without quantitative
thresholds. - Evidence summaries without raw artifact references.

Pitfalls ⚠️ \-\-\-\-\-\-\-\-- Hidden assumptions in environment or
calibration setup. - Missing negative-path scenarios for
high-criticality behavior. - Incomplete traceability from requirement to
verdict.

Best Practices 🌟 \-\-\-\-\-\-\-\-\-\-\-\-\-\-- Tag every artifact with
domain requirement IDs. - Capture timing + functional evidence in the
same run package. - Record residual risk and ownership before closure.

Heuristics 🧠 \-\-\-\-\-\-\-\-\-\-- If a domain hazard is untested,
confidence is provisional. - If rerun differs unexpectedly, investigate
determinism first. - If evidence is indirect, reduce verdict confidence
level.

Checklist ✅ \-\-\-\-\-\-\-\--.. list-table:: Pre-Review Checklist
:header-rows: 1

> -   -   Item
>     -   Status
>
> -   -   Domain hazard coverage is explicit.
>     -   ☐
>
> -   -   Compliance references are mapped to evidence.
>     -   ☐
>
> -   -   Nominal/boundary/fault results are all documented.
>     -   ☐
>
> -   -   Residual risks and next actions are assigned.
>     -   ☐
