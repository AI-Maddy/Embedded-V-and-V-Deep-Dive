---
title: "Code Generation Settings Critical Decisions"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 🛠️ Code-Generation Settings --- Critical Decisions

**🎛️ Embedded Coder Configuration (`ert.tlc`)**

  **System target       `ert.tlc`                        Embedded Real-Time ---
  file**                                                 no OS dependencies,
                                                         bare-metal.

  **Solver**            Fixed-step, `ode4` or Discrete   Variable-step solvers
                                                         generate unpredictable
                                                         timing.

  **Fixed-step size**   0.005 s (200 Hz) or 0.01 s (100  Must match FCC frame
                        Hz)                              rate exactly.

  **Data type           `double → single` globally       Target FCC has no
  replacement**                                          double-precision FPU.

  **Overflow action**   `Saturate on integer overflow`   `Wrap` masks range
                                                         errors silently.

  **Signal storage      `Off` for DAL-A                  Preserves 1:1 block →
  reuse**                                                variable traceability.

  **Code interface      `Reusable function`              Allows unit testing of
  packaging**                                            individual subsystems.

  **Generate code       `On`                             Separate build step with
  only**                                                 project cross-compiler.

  **Code-gen report**   **Always generate**              Primary traceability
                                                         evidence artifact.

  **MISRA C:2012        `On` (Model Advisor)             Pre-generation
  checks**                                               compliance validation.
