🔧  DO-330 Tool Qualification for Automation Scripts
------------------------------------------------------

.. tip::
   💡 Your automation scripts are **tools** under DO-330.  The table below shows
   the TQL assignment for each script component.

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Script Component
     - TQL
     - Rationale
   * - 🔒 ``env_gate.py``
     - TQL-5
     - Detects errors (hash mismatch) but does not produce evidence; output is
       advisory — a human reviews the gate result.
   * - 🤖 ``run_batch.py``
     - TQL-5
     - Executes Simulink ``sim()`` — the tool output (raw log) is independently
       verified by the verdict engine.
   * - ✅ ``verdict_engine.py``
     - TQL-3
     - Produces pass/fail verdicts that appear in evidence; output is reviewed but
       could introduce undetected errors (wrong threshold, wrong signal).
   * - 📦 ``evidence_packager.sh``
     - TQL-5
     - Performs file operations (copy, hash, chmod) — output integrity verified
       by SHA-256 manifest check.
   * - 📊 ``report_gen.py``
     - TQL-5
     - Renders data already verified by verdict engine; report is reviewed by DER.
   * - 📈 **Simulink Coverage tool**
     - TQL-1
     - Coverage measurement tool whose output is used directly as MC/DC evidence
       without independent re-verification (DAL-A requirement).

.. warning::
   ⚠️  If the ``verdict_engine.py`` output is used as **sole evidence** without
   independent review, it must be qualified as **TQL-1** — requiring full
   tool qualification data package per DO-330 §12.

----

