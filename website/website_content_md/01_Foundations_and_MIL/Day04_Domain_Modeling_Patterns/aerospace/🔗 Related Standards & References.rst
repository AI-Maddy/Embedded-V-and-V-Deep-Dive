🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard / Reference
     - Relevance to Domain Modeling Patterns
   * - **DO-178C**
     - Software V&V objectives; MC/DC coverage at source-code level.
   * - **DO-331**
     - MBDV supplement — model coverage, model traceability, and model-based test requirements.
   * - **ARP4754A**
     - System development process; allocates functions to items; defines DAL.
   * - **ARP4761**
     - FHA / FMEA / FTA methods; source of hazard thresholds and latency budgets.
   * - **ARINC 429**
     - Digital information transfer; BNR encoding; SSM definitions; label allocation.
   * - **ARINC 664 Pt. 7**
     - AFDX Virtual Link configuration; BAG / SKEWmax timing parameters.
   * - **MAAB Control Algorithm Modeling Guidelines**
     - Simulink / Stateflow modeling conventions for safety-critical software.

----

.. admonition:: 🚀  Remember

   In aerospace domain modeling, **the pattern IS the argument**.  Choosing the right
   pattern — hierarchical state machine for mode logic, explicit SSM decoding for bus
   interfaces, independent monitors for cross-channel comparison — tells the DER
   exactly how your design handles failures before they reach the hardware.
   Document your pattern choices; they are certification evidence.
