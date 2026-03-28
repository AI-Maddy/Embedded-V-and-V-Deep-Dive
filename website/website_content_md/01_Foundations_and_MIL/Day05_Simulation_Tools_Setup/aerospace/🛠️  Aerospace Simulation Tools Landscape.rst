🛠️  Aerospace Simulation Tools Landscape
-----------------------------------------

.. note::
   🔑 **DO-330 Reminder** — Every tool that produces, transforms, or verifies
   certification evidence must be assessed for Tool Qualification Level (TQL).
   The table below lists the typical TQL for each tool category.

The Day-05 setup task spans **five tool layers**.  All five must be configured,
version-locked, and cross-validated before a single MIL run is used as evidence.

.. rubric:: 🗂️  Tool Layer Overview

.. list-table::
   :widths: 5 25 30 20 20
   :header-rows: 1

   * - #
     - Layer
     - Purpose
     - Example Tools
     - DO-330 TQL
   * - 1
     - 🏗️ Modelling Environment
     - Block-diagram / dataflow modelling of controller + plant
     - MATLAB/Simulink, Ansys SCADE Suite
     - TQL-5 (model only); TQL-1 if generating qualified code
   * - 2
     - ✈️ Flight Dynamics / Plant
     - High-fidelity aerodynamic plant model for closed-loop MIL
     - JSBSim, FlightGear FDM, X-Plane SDK, OpenFlight
     - TQL-5 (stimulus source, not output generator)
   * - 3
     - 🔌 Avionics Bus Simulation
     - ARINC 429 / AFDX / MIL-STD-1553 stimulus and monitoring
     - Ballard ARINC, AIM GmbH AFDX Analyzer, DDC BU-65590
     - TQL-5; TQL-3 if bus replay drives coverage decisions
   * - 4
     - 🔬 Verification & Coverage
     - Structural coverage (MC/DC), static analysis, test execution
     - VectorCAST, LDRA Testbed, Polyspace, Cantata++, Reactis
     - TQL-1 (DAL-A/B coverage tools must be fully qualified)
   * - 5
     - 🤖 Test Automation & Reporting
     - Scripted MIL execution, regression, evidence packaging
     - RT-Tester, TPT (PikeTec), pytest + MATLAB Engine API
     - TQL-3 (automation drives output but not coverage data)

----

