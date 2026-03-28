🏗️  Code-Generation Pipeline Architecture
--------------------------------------------

.. code-block:: text

   ┌─────────────────────────────────────────────────────────────────────────────┐
   │              AEROSPACE CODE-GENERATION PIPELINE                            │
   │                                                                            │
   │  ┌──────────────────┐                                                      │
   │  │  Verified MIL     │  ← model.slx (hash-locked, MIL-passed)              │
   │  │  Model (Simulink) │  ← params.mat (calibration data)                    │
   │  └────────┬─────────┘                                                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ① CODE-GENERATION SETTINGS REVIEW                │                      │
   │  │     • Solver: fixed-step, discrete or ode4                              │
   │  │     • Target: Embedded Coder → ert.tlc                                  │
   │  │     • Data types: single / int32 (no double on target)                  │
   │  │     • Overflow: Saturate on overflow (no wrap)                          │
   │  │     • Optimizations: constrained by traceability                        │
   │  └────────┬─────────────────────────────────────────┘                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ② CODE GENERATION (Embedded Coder / SCADE KCG)   │                      │
   │  │     • rtwbuild('FCS_Pitch_Autopilot')                                   │
   │  │     • or: scade -codegen -config dal_a.cfg                              │
   │  │     • Output: src/*.c + src/*.h + codegen_report                        │
   │  └────────┬─────────────────────────────────────────┘                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ③ CODE REVIEW & STANDARDS CHECK                   │                      │
   │  │     • MISRA C:2012 compliance (mandatory, DAL-A)                        │
   │  │     • Naming conventions, file structure                                │
   │  │     • Dead code / unreachable path analysis                             │
   │  │     • Traceability: block ↔ source line mapping                         │
   │  └────────┬─────────────────────────────────────────┘                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ④ BUILD & COMPILE (Cross-compiler)                │                      │
   │  │     • Target: PowerPC / ARM Cortex-R (FCC HW)                           │
   │  │     • Compiler: GHS MULTI / Wind River Diab / GCC                       │
   │  │     • Warnings: -Wall -Werror -Wextra                                  │
   │  │     • Optimization: -O1 or -O0 (DAL-A: limited)                         │
   │  └────────┬─────────────────────────────────────────┘                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ⑤ EVIDENCE PACKAGING                              │                      │
   │  │     • codegen_report.html (block → .c traceability)                     │
   │  │     • MISRA report (zero violations for DAL-A)                          │
   │  │     • compiler_output.log (zero warnings)                               │
   │  │     • SHA-256 hashes for model + generated code                         │
   │  └──────────────────────────────────────────────────┘                      │
   └─────────────────────────────────────────────────────────────────────────────┘

----

