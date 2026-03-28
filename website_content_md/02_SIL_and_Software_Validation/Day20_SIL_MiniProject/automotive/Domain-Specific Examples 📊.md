# Domain-Specific Examples 📊

-   **Nominal (🟢)**: Adaptive cruise and speed regulation under normal
    traffic conditions.
-   **Boundary (🟡)**: Dense stop-and-go scenarios with tight headway
    and timing limits.
-   **Fault (🔴)**: Sensor dropout and invalid CAN frame injection.

Patterns 🔄 \-\-\-\-\-\-\-\-\-- Derive acceptance thresholds from
hazard-linked requirements to ensure that safety-critical functions are
validated against real-world scenarios. - Keep interface timing
contracts explicit and reviewable to maintain clarity and accountability
in communication between components. - Compare nominal and stressed
traces against the same baseline to identify discrepancies and ensure
robustness.
