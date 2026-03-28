# 📋 Pre-Closure Checklist

**Gate: Must be 100 % complete before automated MIL evidence is
submitted**

-   [ ] All automation scripts are under version control with locked
    hashes.
-   [ ] `env_gate.py` passes on the CI runner --- no environment drift.
-   [ ] Campaign manifest lists every scenario; no ad-hoc additions
    outside the manifest.
-   [ ] Canary scenario passes before full campaign execution.
-   [ ] All scenarios executed with quantitative verdicts (no \"visual
    inspection\" verdicts).
-   [ ] Determinism verification (10 % re-run) confirms bit-for-bit
    reproduction.
-   [ ] Evidence folders are write-once (`chmod 444`), SHA-256
    manifested.
-   [ ] Traceability CSV links every requirement → scenario → verdict →
    artifact path.
-   [ ] HTML report generated automatically --- no manual edits.
-   [ ] DO-330 TQL assessment record exists for each script component.
-   [ ] CI pipeline config (`gitlab-ci.yml` / `Jenkinsfile`) committed
    and reviewed.
-   [ ] Long-term evidence archive location confirmed (not relying on CI
    artifact retention).

------------------------------------------------------------------------
