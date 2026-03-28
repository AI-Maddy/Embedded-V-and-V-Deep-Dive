# 🏆 Best Practices

  ------- ---------------------------------------------------------------
  🔒      Hash the model, parameters, and generated code together in a
          single `env_manifest.json`. Any hash mismatch triggers full
          re-generation.

  📋      Include the code-generation report as a **mandatory** artifact
          in the Software Accomplishment Summary (SAS).

  🧪      Run a quick 3-scenario SIL back-to-back immediately after
          generation (before committing). Catch settings errors early.

  📊      Track generated code size (text + data + BSS) over time. A
          sudden jump means a model change introduced unexpected
          complexity.

  🔒      Store generated code in a separate Git branch (`codegen/v4.2`)
          --- never mix generated and hand-written code in the same
          directory.

  📄      Document every MISRA deviation with a formal rationale form
          signed by the DER. \"Advisory --- not applicable\" is not
          sufficient for DAL-A.
  ------- ---------------------------------------------------------------

------------------------------------------------------------------------
