# ⚠️ Residual-Risk Register Template

  ---------------------------------------------------------------------------
  Risk ID  Description              Severity   Owner      Mitigation / Next
                                                          Action
  -------- ------------------------ ---------- ---------- -------------------
  RR-001   Multi-fault scenario     Medium     V&V Lead   Plan Cat C scenario
           (SC-MFT-01) used Cat B                         for SIL phase (Day
           turbulence; Cat C                              16).
           (severe) not tested at                         
           MIL level.                                     

  RR-002   Elevator actuator model  High       Plant Eng. Replace with
           uses first-order                               higher-fidelity
           dynamics; real actuator                        actuator model
           has nonlinear backlash.                        before SIL.

  RR-003   ARINC 429 bus model uses Low        Avionics   Add bit-error
           ideal transport delay;              Eng.       injection at HIL
           no bit-error modeling.                         phase (Day 25).

  RR-004   Coverage measurement     Medium     Tool Qual  Complete DO-330
           relies on Simulink                  Lead       TQL-1 qualification
           Coverage (TQL-1 tool);                         data package by SIL
           no independent                                 entry.
           re-measurement                                 
           performed.                                     
  ---------------------------------------------------------------------------

------------------------------------------------------------------------
