---
title: "Embedded Coder vs SCADE KCG Comparison"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  🔀 Input model    Simulink / Stateflow       SCADE Suite (Lustre-based)

  🏷️ Target         C, C++, HDL                C (deterministic subset)
  language                                     

  📜 DO-330 status  **Not pre-qualified** ---  **TQL-1 pre-qualified**
                    output must be verified    --- translation exempt
                                               from review

  🎯 MISRA          Generated code needs       Generated code is
  compliance        external MISRA check       MISRA-C:2012 compliant by
                                               construction

  🔢 Data types     Configurable (may produce  Strictly typed from model;
                    `double` if not            no implicit promotions
                    constrained)               

  🔧 Traceability   codegen_report.html (block Built-in proof
                    ↔ C line)                  obligations + traceability
                                               report

  💰 Verification   High (code review +        Lower (model verification
  cost              MISRA + SIL back-to-back)  sufficient for
                                               translation)

  🏗️ Industry usage Wide (transport, defense,  Primarily aerospace / rail
                    industrial)                (Airbus, Thales)
