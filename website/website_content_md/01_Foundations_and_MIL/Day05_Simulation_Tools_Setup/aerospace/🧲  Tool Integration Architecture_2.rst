🧲  Tool Integration Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following shows how the five layers connect for a typical aerospace MIL run:

.. code-block:: text

   ┌────────────────────────────────────────────────────────────────┐
   │               Aerospace MIL Toolchain — Data Flow              │
   ├──────────────────┬─────────────────────────────────────────────┤
   │  Requirements    │  DOORS NG / JAMA → Simulink Requirements     │
   │  (Layer 0)       │  (bidirectional traceability links)          │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  Plant FDM       │  JSBSim / Aerospace Blockset → Simulink      │
   │  (Layer 2)       │  S-Function (6-DOF state vector inputs)      │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  Bus Stimulus    │  Ballard/AIM → loopback → Simulink bus       │
   │  (Layer 3)       │  input blocks (ARINC 429 label stream)       │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  FCS Model       │  Simulink / SCADE controller block           │
   │  (Layer 1)       │  (DAL-A algorithm under test)                │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  Coverage Engine │  VectorCAST / LDRA / Reactis                 │
   │  (Layer 4)       │  (MC/DC data collected per run)              │
   ├──────────────────┼─────────────────────────────────────────────┤
   │  Automation      │  RT-Tester / TPT / pytest orchestration      │
   │  (Layer 5)       │  → evidence package (logs + verdicts + VCRI) │
   └──────────────────┴─────────────────────────────────────────────┘

----

