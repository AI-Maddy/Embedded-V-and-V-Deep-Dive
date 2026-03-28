# 🚫 Anti-Patterns --- What Breaks MIL Evidence

::: danger
::: title
Danger
:::

❌ These are the most common reasons MIL evidence packages are
**rejected at SOI**.
:::

-   🚩 Running simulations from the Simulink GUI instead of a script ---
    no reproducibility.
-   🚩 Logging only \"interesting\" signals --- post-hoc analysis
    discovers missing data.
-   🚩 Variable-step solver in evidence runs --- output timing is
    non-deterministic.
-   🚩 Overwriting old run folders instead of creating new ones ---
    evidence tampering risk.
-   🚩 Pass/fail assigned by visual inspection of a plot --- not
    auditable.
-   🚩 Mixing exploration runs and evidence runs in the same folder
    tree.

------------------------------------------------------------------------
