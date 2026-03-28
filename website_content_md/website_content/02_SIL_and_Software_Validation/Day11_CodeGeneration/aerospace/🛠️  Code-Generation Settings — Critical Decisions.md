# 🛠️ Code-Generation Settings --- Critical Decisions

**🎛️ Embedded Coder Configuration (`ert.tlc`)**

  -------------------------------------------------------------------------------
  Setting               DAL-A Recommended Value          Rationale
  --------------------- -------------------------------- ------------------------
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
  -------------------------------------------------------------------------------

**🔧 SCADE KCG Configuration (Alternative)**

``` text
scade -codegen                          \
  -config dal_a.cfg                     \
  -target c                             \
  -root FCS_Pitch_Controller            \
  -output_dir generated_code/           \
  -integration_code on                  \
  -traceability on                      \
  -misra_c_2012 mandatory+required      \
  -proof_obligations on
```

::: tip
::: title
Tip
:::

💡 SCADE KCG is a **qualified code generator** (DO-330 TQL-1) --- its
output does not require independent verification of the translation.
However, the *model* still requires full verification (DO-331). This is
why many DAL-A programs choose SCADE: it eliminates the
code-review-of-generated-code burden, saving hundreds of engineering
hours.
:::

------------------------------------------------------------------------
