🔗 Related Standards & References
------------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance to Code Generation
   * - **DO-178C §6.3**
     - Software coding standards — generated code must comply.
   * - **DO-178C Table A-5**
     - Source code objectives (traceability, accuracy, consistency).
   * - **DO-178C §6.3.4.c**
     - Source-to-object traceability — limits compiler optimization.
   * - **DO-331 §MB.6.3**
     - Model coverage and code-generation requirements for MBDV.
   * - **DO-330 §12**
     - Tool qualification process — code generator and compiler.
   * - **MISRA C:2012**
     - Coding standard for safety-critical C; mandatory for DAL-A.
   * - **ARP4754A §5.4**
     - Development assurance — software as part of system development.
   * - **CAST-32A**
     - Multi-core considerations — relevant if target is multi-core FCC.

----

.. admonition:: 🔀 Remember

   Code generation is not a "push button" step — it is a **design decision**
   with certification consequences.  Every setting in the code-generation
   configuration becomes a line item in the Plan for Software Aspects of
   Certification (PSAC).  Lock the settings, verify the output, hash the
   artifacts, and treat the generated code as what it is: the software that
   will fly.
