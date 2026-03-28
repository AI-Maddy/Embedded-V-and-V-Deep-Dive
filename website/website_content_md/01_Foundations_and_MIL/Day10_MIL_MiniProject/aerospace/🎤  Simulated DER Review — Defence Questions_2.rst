🎤  Simulated DER Review — Defence Questions
----------------------------------------------

.. tip::
   💡 Prepare to answer these questions during the simulated review.  Each
   question maps to a specific DO-178C concern.

.. list-table::
   :widths: 5 55 40
   :header-rows: 1

   * - #
     - DER Question
     - Expected Evidence
   * - 1
     - "Show me how PA-REQ-006 (IMU switchover) is verified."
     - SC-FLT-01 verdict.json + raw_log.mat plot showing switchover < 100 ms
   * - 2
     - "How do you know the verdict engine itself is correct?"
     - DO-330 TQL-3 assessment record + independent spot-check of 3 verdicts
   * - 3
     - "What happens if I re-run SC-BDY-01 — will I get the same result?"
     - Determinism verification log (10 % re-run bit-for-bit comparison)
   * - 4
     - "Your model has 4 modes — where is the transition coverage matrix?"
     - Mode-transition table: ATT↔VS, VS↔ALTS, any→OVRD (covered by SC-BDY-01..03, SC-FLT-03)
   * - 5
     - "PA-REQ-011 combines IMU failure and turbulence. Is this a worst-case?"
     - SC-MFT-01 uses Cat B turbulence (moderate); justify why Cat C (severe)
       is not required at MIL level (reserved for SIL/HIL)
   * - 6
     - "What residual risks remain after MIL?"
     - Residual-risk register with items, severity, and assigned owners
   * - 7
     - "Show your traceability from requirement to evidence artifact."
     - traceability_matrix.csv — every req → scenario → verdict → artifact path

----

