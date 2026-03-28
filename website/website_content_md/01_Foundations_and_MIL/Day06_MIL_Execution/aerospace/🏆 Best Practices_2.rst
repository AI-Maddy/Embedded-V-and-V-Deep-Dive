🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🏷️
     - Tag every run folder with ``{date}_{run-id}_{scenario-id}`` for instant lookup.
   * - ⏩
     - Use ``parsim()`` (MATLAB) or ``multiprocessing`` (Python) to run independent
       scenarios in parallel — but never share state between parallel workers.
   * - 📝
     - Write ``run_notes.md`` inside each evidence folder: machine ID, operator,
       any anomalies observed, reason for any manual intervention.
   * - 🔒
     - Set evidence folders to **read-only** (``chmod 444``) immediately after run
       completes; version-control only the manifest, not the raw logs.
   * - 🧬
     - Include a ``canary_check`` scenario — a known-good minimal run whose result
       is used as a sanity gate before processing the full campaign.
   * - 📈
     - Generate summary plots automatically as part of the verdict script, not manually;
       every plot must have title, axis labels, units, requirement ID, and verdict stamp.

----

