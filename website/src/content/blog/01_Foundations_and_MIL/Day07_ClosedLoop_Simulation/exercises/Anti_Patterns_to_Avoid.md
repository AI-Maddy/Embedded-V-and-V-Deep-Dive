---
title: "Anti Patterns to Avoid"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🚫 Anti-Patterns to Avoid

-   Tuning thresholds after seeing failing results. .. warning:: This
    invalidates the integrity of the test and violates **DO-178C**
    principles.
-   Mixing multiple uncontrolled changes in one run. .. admonition::
    Example Avoid combining timing and value changes in a single test
    iteration.
-   Summarizing outcomes without raw evidence pointers. .. note:: Always
    link findings to specific artifacts for traceability.
