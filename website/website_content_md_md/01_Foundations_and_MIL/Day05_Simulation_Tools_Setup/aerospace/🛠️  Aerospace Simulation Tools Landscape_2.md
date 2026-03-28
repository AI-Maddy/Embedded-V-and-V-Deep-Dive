# 🛠️ Aerospace Simulation Tools Landscape

::: note
::: title
Note
:::

🔑 **DO-330 Reminder** --- Every tool that produces, transforms, or
verifies certification evidence must be assessed for Tool Qualification
Level (TQL). The table below lists the typical TQL for each tool
category.
:::

The Day-05 setup task spans **five tool layers**. All five must be
configured, version-locked, and cross-validated before a single MIL run
is used as evidence.

**🗂️ Tool Layer Overview**

  ------------------------------------------------------------------------------
  \#   Layer             Purpose               Example Tools      DO-330 TQL
  ---- ----------------- --------------------- ------------------ --------------
  1    🏗️ Modelling      Block-diagram /       MATLAB/Simulink,   TQL-5 (model
       Environment       dataflow modelling of Ansys SCADE Suite  only); TQL-1
                         controller + plant                       if generating
                                                                  qualified code

  2    ✈️ Flight         High-fidelity         JSBSim, FlightGear TQL-5
       Dynamics / Plant  aerodynamic plant     FDM, X-Plane SDK,  (stimulus
                         model for closed-loop OpenFlight         source, not
                         MIL                                      output
                                                                  generator)

  3    🔌 Avionics Bus   ARINC 429 / AFDX /    Ballard ARINC, AIM TQL-5; TQL-3
       Simulation        MIL-STD-1553 stimulus GmbH AFDX          if bus replay
                         and monitoring        Analyzer, DDC      drives
                                               BU-65590           coverage
                                                                  decisions

  4    🔬 Verification & Structural coverage   VectorCAST, LDRA   TQL-1 (DAL-A/B
       Coverage          (MC/DC), static       Testbed,           coverage tools
                         analysis, test        Polyspace,         must be fully
                         execution             Cantata++, Reactis qualified)

  5    🤖 Test           Scripted MIL          RT-Tester, TPT     TQL-3
       Automation &      execution,            (PikeTec),         (automation
       Reporting         regression, evidence  pytest + MATLAB    drives output
                         packaging             Engine API         but not
                                                                  coverage data)
  ------------------------------------------------------------------------------

------------------------------------------------------------------------
