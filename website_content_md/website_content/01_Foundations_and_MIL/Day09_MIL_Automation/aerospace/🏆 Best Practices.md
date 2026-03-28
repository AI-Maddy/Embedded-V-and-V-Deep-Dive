# 🏆 Best Practices

  ------- ---------------------------------------------------------------
  🏷️      Version-tag every campaign:
          `git tag mil_campaign_2026-03-07_abc1234`.

  ⏩      Profile per-scenario execution time; set timeout to 3× P95 to
          catch hangs without false alarms.

  📝      Include a `README.md` inside every evidence folder: campaign
          ID, commit hash, operator, date, MATLAB version, total
          pass/fail count.

  🔒      Store scripts SHA-256 in `env_manifest.json` alongside model
          and param hashes.

  🧬      Run determinism verification as a CI stage (not optional --- a
          failed check blocks the pipeline).

  📊      Trend campaign pass-rate over time: a dropping pass-rate
          signals model regression.
  ------- ---------------------------------------------------------------

------------------------------------------------------------------------
