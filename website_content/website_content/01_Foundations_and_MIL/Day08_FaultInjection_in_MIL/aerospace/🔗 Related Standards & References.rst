🔗 Related Standards & References
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance to Fault Injection
   * - **ARP4761**
     - Safety assessment methods: FHA, FMEA, FTA — source of fault scenarios.
   * - **ARP4754A §5.5**
     - Safety assessment and system verification — requires fault analysis evidence.
   * - **DO-178C Table A-7**
     - Verification of outputs — fault injection is part of robustness verification.
   * - **DO-331 §6.4**
     - Model robustness testing — MBDV supplement for fault scenarios at model level.
   * - **DO-254 §6.3**
     - Hardware fault analysis — for combined SW/HW fault modes.
   * - **SAE ARP5107**
     - Common Mode Failure analysis guidelines — drives multi-fault scenarios.

----

.. admonition:: 🚀  Remember

   Fault injection is not about proving the system **works** — nominal tests do that.
   Fault injection is about proving the system **fails safely**.  Every hazard in the
   FHA is a question: "What happens when this goes wrong?"  Your fault injection
   campaign is the answer — and the answer must be documented, quantified, and
   traceable all the way back to the safety assessment.
