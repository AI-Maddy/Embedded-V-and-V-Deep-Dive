⚠️  Residual-Risk Register Template
--------------------------------------

.. list-table::
   :widths: 10 35 12 15 28
   :header-rows: 1

   * - Risk ID
     - Description
     - Severity
     - Owner
     - Mitigation / Next Action
   * - RR-001
     - Multi-fault scenario (SC-MFT-01) used Cat B turbulence; Cat C
       (severe) not tested at MIL level.
     - Medium
     - V&V Lead
     - Plan Cat C scenario for SIL phase (Day 16).
   * - RR-002
     - Elevator actuator model uses first-order dynamics; real actuator
       has nonlinear backlash.
     - High
     - Plant Eng.
     - Replace with higher-fidelity actuator model before SIL.
   * - RR-003
     - ARINC 429 bus model uses ideal transport delay; no bit-error modeling.
     - Low
     - Avionics Eng.
     - Add bit-error injection at HIL phase (Day 25).
   * - RR-004
     - Coverage measurement relies on Simulink Coverage (TQL-1 tool);
       no independent re-measurement performed.
     - Medium
     - Tool Qual Lead
     - Complete DO-330 TQL-1 qualification data package by SIL entry.

----

