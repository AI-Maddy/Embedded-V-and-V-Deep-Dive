# Medical Focus --- Day29 HIL Regression and Automation 🚑

Objective 🎯 \-\-\-\-\-\-\-\--Apply this day in **Medical** context with
explicit safety, compliance, and evidence expectations. The goal is to
ensure that all hardware-in-the-loop (HIL) systems are rigorously tested
to meet the highest standards of safety and reliability in medical
applications.

Phase Context 🔍 \-\-\-\-\-\-\-\-\-\-\-\--Phase: **HIL** Primary focus:
**hardware-integrated timing and interface confidence**. Section focus:
**medical verification workflow**.

Domain Constraints 🚧 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Compliance
baseline: **IEC 62304 + ISO 14971 + IEC 60601 context** - Key hazard
profile: - Incorrect dosage delivery - Missed alarm - Unsafe therapy
continuation - Interface landscape: - Device buses - Sensor links -
Alarm/event channels

Domain-Specific Examples 📊
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- **Nominal** 🟢:
Therapy control with validated sensor feedback. - **Boundary** 🟡:
Near-threshold dosing and alarm escalation timing. - **Fault** 🔴:
Sensor spike/dropout and actuator command rejection path.

Patterns 🔄 \-\-\-\-\-\-\-\-- Derive acceptance thresholds from
hazard-linked requirements to ensure that all tests are relevant and
meaningful. - Keep interface timing contracts explicit and reviewable to
maintain clarity and accountability. - Compare nominal and stressed
traces against the same baseline to identify discrepancies and ensure
consistency.

Anti-Patterns 🚫 \-\-\-\-\-\-\-\-\-\-\-\-\-- Generic test claims without
domain hazard mapping lead to insufficient coverage. - Pass/fail
decisions without quantitative thresholds undermine the reliability of
results. - Evidence summaries without raw artifact references can
obscure the basis for conclusions.

Pitfalls ⚠️ \-\-\-\-\-\-\-\-- Hidden assumptions in environment or
calibration setup can lead to unexpected failures. - Missing
negative-path scenarios for high-criticality behavior can result in
untested vulnerabilities. - Incomplete traceability from requirement to
verdict can compromise the integrity of the validation process.

Best Practices 🌟 \-\-\-\-\-\-\-\-\-\-\-\-\-\-- Tag every artifact with
domain requirement IDs to ensure traceability and accountability. -
Capture timing + functional evidence in the same run package to
streamline the validation process. - Record residual risk and ownership
before closure to ensure that all parties are aware of outstanding
issues.

Heuristics 🧠 \-\-\-\-\-\-\-\-\-\-- If a domain hazard is untested,
confidence is provisional. - If rerun differs unexpectedly, investigate
determinism first to identify potential issues. - If evidence is
indirect, reduce verdict confidence level to reflect uncertainty.

Checklist ✅ \-\-\-\-\-\-\-\--.. note:: Ensure that the following items
are checked before proceeding with the review. - \[ \] Domain hazard
coverage is explicit. - \[ \] Compliance references are mapped to
evidence. - \[ \] Nominal/boundary/fault results are all documented. -
\[ \] Residual risks and next actions are assigned.
