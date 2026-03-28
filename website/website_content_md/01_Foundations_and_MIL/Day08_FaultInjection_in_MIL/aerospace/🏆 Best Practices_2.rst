🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🏷️
     - Tag every injection scenario with ``FI-{category}-{number}`` (e.g. ``FI-SEN-01``).
   * - 📐
     - Define injection parameters in ``scenario.json``, never as hard-coded model changes.
   * - 🔒
     - Use a **fault injection controller** subsystem — a single block that reads the
       scenario file and applies all faults; never scatter injection logic across the model.
   * - 📊
     - Plot **detection latency histogram** across all scenarios — identify outliers.
   * - 🧬
     - Re-run 20 % of fault scenarios bit-for-bit to confirm deterministic injection.
   * - 🗺️
     - Maintain a **fault coverage matrix**: rows = FMEA items, columns = FI scenarios;
       every cell must be linked or justifiably excluded.

----

