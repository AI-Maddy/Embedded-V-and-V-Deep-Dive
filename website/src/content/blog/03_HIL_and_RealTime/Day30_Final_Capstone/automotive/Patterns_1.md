---
title: "Patterns"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🔹 **Anti-Patterns** 🔹

\### 🔴 **Generic Test Claims** 🚫

Avoid making generic test claims without domain hazard mapping, as this
can lead to inadequate testing and potential safety issues.

\### 🔴 **Pass/Fail Decisions** 🚫

Avoid making pass/fail decisions without quantitative thresholds, as
this can lead to subjective and potentially incorrect conclusions.

\### 🔴 **Evidence Summaries** 🚫

Avoid creating evidence summaries without raw artifact references, as
this can lead to incomplete and inaccurate information.

# 🔹 **Patterns** 🔹

\### 🟢 **Acceptance Thresholds** 📊

Derive acceptance thresholds from hazard-linked requirements to ensure
that the system meets safety standards.

\### 🟡 **Interface Timing Contracts** 🕒

Keep interface timing contracts explicit and reviewable to ensure
seamless interaction between hardware and software components.

\### 🟢 **Nominal and Stressed Traces** 📈

Compare nominal and stressed traces against the same baseline to
identify potential safety issues.
