# ✅ Patterns --- What Works for Fault Injection

::: tip
::: title
Tip
:::

💡 Fault injection patterns that have survived DER review in DAL-A
programs.
:::

1.  **🗂️ FMEA-first injection planning** --- Start from the ARP4761 FMEA
    work product; create one injection scenario per failure mode; tag
    each with the FMEA item ID.
2.  **⏱️ Time-triggered + state-triggered injection** --- Use
    time-triggered injection for repeatable regression; add
    state-triggered variants (e.g. \"inject when α \> 12°\") for
    corner-case coverage.
3.  **📊 Baseline-then-fault comparison** --- Always run the identical
    scenario without fault injection first; diff the two logs to isolate
    fault effects from nominal dynamics.
4.  **🔄 Incremental severity escalation** --- For each fault type,
    start with the mildest variant (small bias), then escalate to
    worst-case (stuck, runaway); plot detection latency vs. severity to
    find the detection threshold.
5.  **🧩 Combinatorial coverage from FTA cut sets** --- Use the Fault
    Tree minimal cut sets to define multi-fault injection scenarios;
    verify that the system reaches a safe state even when the full cut
    set fires.
6.  **📦 Injection event log** --- Log the exact injection time, target
    signal, fault type, and parameter values in a machine-readable
    `fault_event_log.csv`; this is the DER\'s primary evidence that the
    injection was correct.

------------------------------------------------------------------------
