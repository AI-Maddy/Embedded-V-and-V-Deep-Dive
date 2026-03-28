# 📋 Pre-Closure Checklist

**Gate: Must be 100 % complete before proceeding to SIL Setup (Day 12)**

-   [ ] Embedded Coder / SCADE KCG configuration settings documented and
    hash-locked.
-   [ ] Code generated from verified MIL model (MIL campaign passed ---
    Day 10).
-   [ ] `codegen_report.html` shows 100 % block → code traceability.
-   [ ] Prohibited constructs check (`codegen_verify.py`) passes with 0
    findings.
-   [ ] MISRA C:2012 mandatory rules: 0 violations.
-   [ ] MISRA C:2012 required rules: 0 violations or formal deviation
    record.
-   [ ] Cross-compilation at -O1 succeeds with 0 warnings (`-Werror`).
-   [ ] Code size (text + data + BSS) fits within target flash/RAM
    budget.
-   [ ] Stack usage within FCC allocation.
-   [ ] Generated code directory write-locked (`chmod 444`), SHA-256
    manifest created.
-   [ ] DO-330 tool qualification assessment complete for code generator
    and compiler.
-   [ ] Traceability CSV: requirement → Simulink block → C function → C
    line number.
-   [ ] Quick SIL back-to-back sanity (3 nominal scenarios) confirms MIL
    ≈ SIL.

------------------------------------------------------------------------
