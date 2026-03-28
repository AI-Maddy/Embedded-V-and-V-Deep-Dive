🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance to MIL Execution
   * - **DO-178C Table A-7**
     - Verification of Outputs — defines what evidence the MIL run must produce.
   * - **DO-331 §6.3**
     - Model simulation, model coverage analysis for MBDV-based verification.
   * - **ARP4754A §5.4**
     - Verification of Function Development — allocates verification activities to phases.
   * - **ARP4761**
     - FHA / FMEA — source of hazard-linked acceptance thresholds.
   * - **DO-330**
     - Tool qualification — applies to Simulink, coverage tools, and verdict scripts.
   * - **MIL-F-8785C**
     - Flying Qualities — defines Dryden turbulence models used as MIL stimuli.

----

.. admonition:: 🚀  Remember

   A MIL run is not a demo — it is a **certification evidence event**.  Every run
   must be scripted, deterministic, hash-verified, and verdict-stamped.  If you
   cannot reproduce a run bit-for-bit on a clean machine tomorrow, the evidence
   it produced is worthless.
