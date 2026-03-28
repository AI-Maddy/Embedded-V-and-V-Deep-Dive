🧪  Code-Generation Verification Scenarios
--------------------------------------------

.. list-table::
   :widths: 12 40 25 23
   :header-rows: 1

   * - Scenario
     - Description
     - Verification Method
     - Acceptance Criterion
   * - **CG-VER-01**
     - Generated code compiles with zero warnings on target
       compiler at -O1, -Werror.
     - Cross-compilation
     - ``compiler_output.log`` has 0 warnings
   * - **CG-VER-02**
     - No ``double`` type, ``malloc``, ``free``, ``goto``, or
       ``system()`` in generated code.
     - ``codegen_verify.py`` script
     - 0 prohibited constructs found
   * - **CG-VER-03**
     - MISRA C:2012 mandatory rules: zero violations.
       Required rules: zero violations or formal deviation.
     - Polyspace / PC-lint / LDRA
     - MISRA report clean
   * - **CG-VER-04**
     - Codegen report maps every Simulink block to a C source line.
       No unmapped blocks.
     - ``codegen_report.html`` review
     - 100 % block → code coverage
   * - **CG-VER-05**
     - SIL back-to-back: generated C produces identical output
       (within ε) to MIL model for all nominal scenarios.
     - SIL vs MIL comparison (Day 13)
     - ``max|MIL - SIL| < 1e-6`` per signal
   * - **CG-VER-06**
     - Stack usage of generated code fits within FCC stack
       allocation (e.g., 8 KB).
     - Static stack analysis (compiler report)
     - Stack depth ≤ 8192 bytes
   * - **CG-VER-07**
     - WCET of ``FCS_step()`` function fits within 200 Hz frame
       budget (5 ms).
     - Static timing analysis (Day 26)
     - WCET ≤ 4.5 ms (90 % of frame)

----

