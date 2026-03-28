🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance to MIL Automation
   * - **DO-330**
     - Software Tool Qualification — governs TQL assignment for automation scripts.
   * - **DO-178C §12**
     - Software verification process — requires documented, repeatable procedures.
   * - **DO-178C Table A-7**
     - Verification of outputs — automated verdicts satisfy these objectives.
   * - **ARP4754A §5.6**
     - Configuration management — applies to scripts, manifests, and evidence.
   * - **DO-331 §6.5**
     - MBDV tool qualification — extends DO-330 for model-based tools.
   * - **IEEE 828**
     - Configuration Management — general guidance for CI-controlled artifacts.

----

.. admonition:: 🚀  Remember

   Automation is not a convenience — it is a **compliance requirement** at scale.
   A manual MIL campaign with 400 scenarios is a human-error minefield: wrong
   parameter file, forgotten log, mismatched version, copy-paste verdict error.
   Automate the pipeline, lock the hashes, generate the reports, and let the DER
   audit the *process* instead of spot-checking the *artifacts*.
