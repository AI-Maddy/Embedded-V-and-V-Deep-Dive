# Device Control Sequences --- Medical 🏥

Purpose 📝 \-\-\-\-\-\--Document **Medical**-specific details for Day24
HIL Scripting with focus on automation and deterministic replay
controls.

Domain Alignment 🗂️ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Standard
reference: **IEC 62304 + ISO 14971 + IEC 60601 context** - Critical
hazards: incorrect dosage delivery, missed alarm, unsafe therapy
continuation - Relevant interfaces: device buses, sensor links,
alarm/event channels

::: important
::: title
Important
:::

Use the **MEDICS** mnemonic to ensure domain-specific considerations:

-   **M** : Mind the patient safety context
-   **E** : Evaluate critical hazards and risks
-   **D** : Determine relevant interfaces and constraints
-   **I** : Inspect requirements and test artifacts
-   **C** : Consider timing and functional outcomes
-   **S** : Set quantitative acceptance criteria
:::

Examples 📚 \-\-\-\-\-\-\--### Nominal Path 🟢 - **GIVEN** : Therapy
control with validated sensor feedback - **WHEN** : The system is in a
steady state - **THEN** : The therapy is delivered correctly and safely

\### Boundary Path 🟡 - **GIVEN** : Near-threshold dosing and alarm
escalation timing - **WHEN** : The system is in a boundary condition -
**THEN** : The system responds correctly and safely

\### Fault Path 🔴 - **GIVEN** : Sensor spike/dropout and actuator
command rejection path - **WHEN** : The system encounters a fault -
**THEN** : The system fails safely and reports the error

Patterns 🔍 \-\-\-\-\-\-\-\-- Use requirement-linked checks for every
scenario. - Track timing and functional outcomes together. - Keep setup
reproducibility constraints explicit.

Anti-Patterns 🚫 \-\-\-\-\-\-\-\-\-\-\-\-\-- Domain-agnostic statements
without measurable criteria. - Ignoring interface constraints during
analysis. - Closing findings without residual risk statement.

Pitfalls 🚨 \-\-\-\-\-\-\-\-- Missing sensor/actuator fault variants. -
Weak traceability from objective to artifact. - Non-repeatable reruns
from uncontrolled configuration drift.
