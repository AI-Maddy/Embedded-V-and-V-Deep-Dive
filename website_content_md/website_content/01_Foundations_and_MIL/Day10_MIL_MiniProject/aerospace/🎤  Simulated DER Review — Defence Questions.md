# 🎤 Simulated DER Review --- Defence Questions

::: tip
::: title
Tip
:::

💡 Prepare to answer these questions during the simulated review. Each
question maps to a specific DO-178C concern.
:::

  -------------------------------------------------------------------------
  \#   DER Question                            Expected Evidence
  ---- --------------------------------------- ----------------------------
  1    \"Show me how PA-REQ-006 (IMU           SC-FLT-01 verdict.json +
       switchover) is verified.\"              raw_log.mat plot showing
                                               switchover \< 100 ms

  2    \"How do you know the verdict engine    DO-330 TQL-3 assessment
       itself is correct?\"                    record + independent
                                               spot-check of 3 verdicts

  3    \"What happens if I re-run SC-BDY-01    Determinism verification log
       --- will I get the same result?\"       (10 % re-run bit-for-bit
                                               comparison)

  4    \"Your model has 4 modes --- where is   Mode-transition table:
       the transition coverage matrix?\"       ATT↔VS, VS↔ALTS, any→OVRD
                                               (covered by SC-BDY-01..03,
                                               SC-FLT-03)

  5    \"PA-REQ-011 combines IMU failure and   SC-MFT-01 uses Cat B
       turbulence. Is this a worst-case?\"     turbulence (moderate);
                                               justify why Cat C (severe)
                                               is not required at MIL level
                                               (reserved for SIL/HIL)

  6    \"What residual risks remain after      Residual-risk register with
       MIL?\"                                  items, severity, and
                                               assigned owners

  7    \"Show your traceability from           traceability_matrix.csv ---
       requirement to evidence artifact.\"     every req → scenario →
                                               verdict → artifact path
  -------------------------------------------------------------------------

------------------------------------------------------------------------
