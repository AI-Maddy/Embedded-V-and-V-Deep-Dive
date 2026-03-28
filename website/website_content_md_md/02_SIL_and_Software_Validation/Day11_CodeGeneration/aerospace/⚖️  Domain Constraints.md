# ⚖️ Domain Constraints

::: warning
::: title
Warning
:::

⚠️ For DAL-A software, the code generator is a **development tool**
under DO-330. If its output is not independently verified (review +
test + static analysis), the tool must be qualified to **TQL-1** --- the
most demanding level. Most projects choose to verify the output instead.
:::

  -----------------------------------------------------------------------
  Constraint             Detail
  ---------------------- ------------------------------------------------
  📜 Compliance baseline DO-178C §6.3 (coding standards) + DO-331 §MB.6.3
                         (MBDV \| code gen) + DO-330 §12 (tool
                         qualification)

  🔧 Code-gen tool class **Development tool** --- output must be
                         verified, or tool qualified to TQL-1.

  🎯 Target compliance   MISRA C:2012 (all mandatory + required rules)
                         for DAL-A. Advisory rules reviewed and
                         justified.

  🔢 Numeric constraints No `double` on target (single-core FCC with no
                         FPU double support). All floating-point is
                         `float` (single) or fixed-point `int32`.

  🔒 Optimization limits Compiler optimization ≤ **-O1** for DAL-A to
                         preserve source--object traceability (DO-178C
                         §6.3.4.c).

  📂 Traceability        Every generated C function must trace back to a
                         Simulink block and forward to a requirement ID.
  -----------------------------------------------------------------------

------------------------------------------------------------------------
