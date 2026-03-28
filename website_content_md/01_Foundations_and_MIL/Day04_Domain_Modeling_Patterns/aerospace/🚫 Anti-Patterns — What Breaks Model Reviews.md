# 🚫 Anti-Patterns --- What Breaks Model Reviews

::: danger
::: title
Danger
:::

❌ These are the most common model-review rejections in aerospace
programs.
:::

-   🚩 Implicit mode transitions with no guard condition documented.
-   🚩 Magic numbers in gain tables --- DER will require justification
    for every value.
-   🚩 Safety monitors sharing state with the monitored function
    (defeats independence).
-   🚩 Parallel signal paths with inconsistent data types or sample
    rates.
-   🚩 Missing `SATURATED` / `INVALID` status outputs on bus interface
    blocks.
-   🚩 Model structural coverage untested --- DO-331 requires
    model-level MC/DC evidence.
-   🚩 Reconfiguration logic that allows reversion without maintenance
    action.

------------------------------------------------------------------------
