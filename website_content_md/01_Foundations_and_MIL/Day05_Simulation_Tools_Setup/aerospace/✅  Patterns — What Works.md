# ✅ Patterns --- What Works

::: tip
::: title
Tip
:::

💡 These patterns have been validated against DO-178C
Stage-of-Involvement (SOI) checklists and ARP4754A development assurance
reviews.
:::

1.  **🔗 Hazard-linked thresholds** --- derive every acceptance
    threshold directly from the Functional Hazard Assessment (FHA);
    reference the FHA item ID in the test case.
2.  **⏱️ Explicit timing contracts** --- document bus timing (e.g. ARINC
    429 word-rate 100 words/s, latency ≤ 5 ms) as a first-class
    requirement, not as a footnote.
3.  **📊 Baseline comparison** --- compare nominal *and* stressed traces
    against the same golden baseline to surface regression across
    environmental changes.
4.  **🗂️ Evidence packaging** --- co-locate raw logs, analysis scripts,
    and verdict rationale in a single traceable artifact package.
5.  **🤖 Automated regression** --- script MIL execution so the full
    test suite can be re-run in under 10 minutes on any qualified
    workstation.

------------------------------------------------------------------------
