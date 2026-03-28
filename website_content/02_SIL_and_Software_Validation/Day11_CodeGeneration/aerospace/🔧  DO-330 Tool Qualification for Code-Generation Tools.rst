🔧  DO-330 Tool Qualification for Code-Generation Tools
---------------------------------------------------------

.. list-table::
   :widths: 25 12 63
   :header-rows: 1

   * - Tool
     - TQL
     - Rationale
   * - 🔀 **Embedded Coder** (Simulink → C)
     - TQL-1 *or* verified output
     - Development tool: output (C code) is part of the software. If output
       is independently verified (review + SIL test + static analysis), TQL-1
       qualification is avoided. Most DAL-A programs choose verification.
   * - 🔀 **SCADE KCG** (SCADE → C)
     - TQL-1 (pre-qualified)
     - KCG has existing DO-330 TQL-1 qualification kit. No additional
       verification of the *translation* is needed; model-level verification
       still required.
   * - 🔨 **Cross-compiler** (C → object code)
     - TQL-1 *or* OCV
     - Object Code Verification (Day 18) can substitute for compiler
       qualification at DAL-A. At DAL-B/C, review of compiler warnings
       + exhaustive testing may suffice.
   * - 📋 **MISRA checker** (Polyspace / PC-lint)
     - TQL-5
     - Verification tool: can fail to detect violations but cannot insert
       errors. TQL-5 = operational requirements only.
   * - 📊 **Simulink Coverage**
     - TQL-5
     - Verification/measurement tool.

----

