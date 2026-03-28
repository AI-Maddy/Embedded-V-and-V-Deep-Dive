# 📋 Practical Example (ACC)

-   Requirement: "When lead-vehicle distance error exceeds 8 m, ACC
    shall reduce commanded torque within 150 ms and restore time-gap to
    1.8 ± 0.2 s within 3.0 s under nominal road-load conditions."

-   

    Verification plan:

    :   -   🧮 Analysis: control-law and timing budget feasibility.
        -   🧪 Test: nominal/boundary/fault MIL scenarios with logged
            latency.
        -   📋 Inspection: requirement wording, units, assumptions, and
            trace links.

⚠️ Anti-Patterns to Avoid
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- 🔴 Domain-agnostic
statements without measurable criteria. - 🔴 Ignoring bus/interface
timing while claiming functional compliance. - 🟡 Closing findings
without residual-risk statement and owner.
