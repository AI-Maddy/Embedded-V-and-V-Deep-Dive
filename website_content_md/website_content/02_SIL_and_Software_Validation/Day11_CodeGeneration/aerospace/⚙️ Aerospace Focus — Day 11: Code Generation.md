# ⚙️ Aerospace Focus --- Day 11: Code Generation

![Phase: SIL](_images/badge_phase_sil.svg)

![Standard: DO-178C / DO-331](_images/badge_standard_do178c.svg)

![Criticality: DAL-A](_images/badge_criticality_dal.svg)

![Focus: Code Generation](_images/badge_focus_codegen.svg)

::: note
::: title
Note
:::

🔀 **The Transition Point** --- Today the model stops being a simulation
artifact and becomes a **source of production code**. In DO-178C terms,
the model is now a \"design representation\" (DO-331 §MB.6.3) and the
generated code must satisfy **every** objective in Table A-5 (software
coding standards) and Table A-7 (verification of outputs). A single
unverified code-generation setting can propagate a latent fault from a
Simulink block into the flight computer. This day ensures that the
code-generation pipeline itself is trustworthy, traceable, and
evidence-ready.
:::

------------------------------------------------------------------------
