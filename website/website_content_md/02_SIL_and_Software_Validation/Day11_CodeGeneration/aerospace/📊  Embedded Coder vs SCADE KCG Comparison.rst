📊  Embedded Coder vs SCADE KCG Comparison
--------------------------------------------

.. list-table::
   :widths: 25 37 38
   :header-rows: 1

   * - Criterion
     - Embedded Coder
     - SCADE KCG
   * - 🔀 Input model
     - Simulink / Stateflow
     - SCADE Suite (Lustre-based)
   * - 🏷️ Target language
     - C, C++, HDL
     - C (deterministic subset)
   * - 📜 DO-330 status
     - **Not pre-qualified** — output must be verified
     - **TQL-1 pre-qualified** — translation exempt from review
   * - 🎯 MISRA compliance
     - Generated code needs external MISRA check
     - Generated code is MISRA-C:2012 compliant by construction
   * - 🔢 Data types
     - Configurable (may produce ``double`` if not constrained)
     - Strictly typed from model; no implicit promotions
   * - 🔧 Traceability
     - codegen_report.html (block ↔ C line)
     - Built-in proof obligations + traceability report
   * - 💰 Verification cost
     - High (code review + MISRA + SIL back-to-back)
     - Lower (model verification sufficient for translation)
   * - 🏗️ Industry usage
     - Wide (transport, defense, industrial)
     - Primarily aerospace / rail (Airbus, Thales)

----

