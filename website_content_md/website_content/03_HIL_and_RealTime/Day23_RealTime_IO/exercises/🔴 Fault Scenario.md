# 🔴 Fault Scenario

**GIVEN** a fault/negative stimulus is introduced, **WHEN** the fault
variant is executed, **THEN** the system should detect the fault and
demonstrate safe handling/recovery.

🧭 Patterns 🧩 \-\-\-\-\-\-\-\-\-\-\-- Compare every stressed run
against a baseline artifact. - Keep pass/fail logic requirement-driven,
not tool-driven. - Separate observation from interpretation in reports.

🚫 Anti-Patterns ⚠️ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Tuning thresholds
after seeing failing results. - Mixing multiple uncontrolled changes in
one run. - Summarizing outcomes without raw evidence pointers.

⚠️ Pitfalls 🚧 \-\-\-\-\-\-\-\-\-\-\-\-- Hidden dependencies in setup
scripts. - Missing failure classification severity. - Incomplete handoff
notes for unresolved issues.

📚 Examples 📖 \-\-\-\-\-\-\-\-\-\-\-- **Example 1**: Nominal pass with
complete traceability chain. - **Example 2**: Boundary fail revealing
timing jitter limit breach. - **Example 3**: Fault recovery success with
documented residual risk.

✅ Best Practices 🌈 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Keep rerun steps
deterministic. - Store artifacts with version/time metadata. - Review
findings with risk owner before closure.

🧪 Heuristics 🧠 \-\-\-\-\-\-\-\-\-\-\-\-\-- If rerun differs
unexpectedly, treat as investigation trigger. - If claim lacks artifact,
downgrade confidence. - If risk is unresolved, status cannot be final
pass.

🔎 Checklist ✅ \-\-\-\-\-\-\-\-\-\-\--.. list-table:: Pre-Review
Checklist :widths: 20 80 :header-rows: 1

> -   -   Item
>     -   Description
>
> -   -   Functional Evidence
>     -   Functional, timing, robustness evidence captured.
>
> -   -   Verdict Table
>     -   Requirement-linked verdict table completed.
>
> -   -   Residual Risk
>     -   Residual risk and next actions documented.

Phase Focus Note 📌 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--This day emphasizes:
**real-time integration behavior, interface timing, and hardware
realism** in accordance with ARP4754A and DO-254 standards.

::: note
::: title
Note
:::

Ensure all documentation is aligned with the relevant V&V standards to
maintain compliance and traceability.
:::

::: important
::: title
Important
:::

Regularly review and update the checklist to reflect any changes in
project scope or requirements.
:::
