🛠️  Code-Generation Settings — Critical Decisions
---------------------------------------------------

.. rubric:: 🎛️ Embedded Coder Configuration (``ert.tlc``)

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Setting
     - DAL-A Recommended Value
     - Rationale
   * - **System target file**
     - ``ert.tlc``
     - Embedded Real-Time — no OS dependencies, bare-metal.
   * - **Solver**
     - Fixed-step, ``ode4`` or Discrete
     - Variable-step solvers generate unpredictable timing.
   * - **Fixed-step size**
     - 0.005 s (200 Hz) or 0.01 s (100 Hz)
     - Must match FCC frame rate exactly.
   * - **Data type replacement**
     - ``double → single`` globally
     - Target FCC has no double-precision FPU.
   * - **Overflow action**
     - ``Saturate on integer overflow``
     - ``Wrap`` masks range errors silently.
   * - **Signal storage reuse**
     - ``Off`` for DAL-A
     - Preserves 1:1 block → variable traceability.
   * - **Code interface packaging**
     - ``Reusable function``
     - Allows unit testing of individual subsystems.
   * - **Generate code only**
     - ``On``
     - Separate build step with project cross-compiler.
   * - **Code-gen report**
     - **Always generate**
     - Primary traceability evidence artifact.
   * - **MISRA C:2012 checks**
     - ``On`` (Model Advisor)
     - Pre-generation compliance validation.

.. rubric:: 🔧 SCADE KCG Configuration (Alternative)

.. code-block:: text

   scade -codegen                          \
     -config dal_a.cfg                     \
     -target c                             \
     -root FCS_Pitch_Controller            \
     -output_dir generated_code/           \
     -integration_code on                  \
     -traceability on                      \
     -misra_c_2012 mandatory+required      \
     -proof_obligations on

.. tip::
   💡 SCADE KCG is a **qualified code generator** (DO-330 TQL-1) — its output
   does not require independent verification of the translation.  However,
   the *model* still requires full verification (DO-331).  This is why many
   DAL-A programs choose SCADE: it eliminates the code-review-of-generated-code
   burden, saving hundreds of engineering hours.

----

