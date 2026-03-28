✅ Patterns — What Works for Code Generation
-----------------------------------------------

.. tip::
   💡 Patterns from successful DAL-A code-generation campaigns.

1. **🔒 Lock settings before generation** — Export the Embedded Coder
   configuration set to a ``.mat`` file and hash it.  Any change to code-gen
   settings triggers a full re-generation cycle.

2. **🔀 Generate-then-freeze** — Once code is generated and verified, ``chmod
   444`` the directory.  No manual edits to generated code, ever.

3. **📋 Run Model Advisor *before* generation** — Catching a ``double`` type or
   a missing saturation at model level is 10× cheaper than finding it in
   generated C.

4. **🧪 SIL back-to-back immediately** — Don't wait for Day 13; run a quick
   nominal comparison right after generation.  If MIL ≠ SIL, something is wrong
   with the settings.

5. **📊 Measure code size early** — If generated code is 200 KB and the target
   has 256 KB flash, you have a 78 % budget problem that will only get worse.

6. **🔧 Use ``Reusable function`` packaging** — This generates subsystem functions
   with explicit I/O, enabling independent unit testing at SIL level.

----

