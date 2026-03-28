⚠️  Pitfalls
------------

.. caution::

   Automation-specific traps in aerospace MIL:

   - 🕳️  **License contention** — ``parsim()`` with 8 workers needs 8 MATLAB licenses
     + 8 Simulink licenses + toolbox licenses.  If the license server is shared,
     workers queue and the campaign takes 4× longer.  Check ``license('inuse')``
     before setting worker count.
   - 🕳️  **Fast Restart cache corruption** — ``UseFastRestart`` caches compiled model
     state; if a scenario changes model parameters that require recompilation, the
     cache serves stale results.  Disable for fault-injection scenarios that modify
     model structure.
   - 🕳️  **CI artifact expiry** — GitLab CI defaults to 30-day artifact retention;
     certification evidence must be retained for product lifetime (20+ years).
     Archive to a separate long-term store.
   - 🕳️  **Path-length limits** — Windows CI runners hit 260-char path limits with
     deeply nested evidence folders.  Use short folder names or run on Linux.
   - 🕳️  **Timezone-dependent timestamps** — Use UTC everywhere in evidence folders and
     logs.  A DER comparing timestamps across time zones will find discrepancies.

----

