---
title: "Anti Patterns"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🚫 Anti-Patterns

::: danger
::: title
Danger
:::

❌ These code-generation mistakes have caused program-level rework:
:::

-   🚩 **Manual edits to generated code** --- Breaks the model ↔ code
    traceability. If the generated code needs a fix, fix the *model* and
    re-generate.
-   🚩 **Generating with \`\`double\`\` types on a single-precision
    target** --- Silent promotion to software emulation, blowing the
    WCET budget.
-   🚩 **Compiler optimization \> -O1** --- At DAL-A, aggressive
    optimization (-O2, -O3) can reorder or eliminate code, breaking
    source-to-object traceability and requiring Object Code Verification
    (OCV).
-   🚩 **Skipping MISRA analysis on generated code** --- \"The tool
    generated it, so it\'s fine\" is not a valid DO-178C argument unless
    the tool is TQL-1 qualified.
-   🚩 **No codegen report** --- Without the block ↔ code traceability
    report, there is no evidence that the generated code implements the
    model.
-   🚩 **Wrap on integer overflow** --- In flight code, a wrapped 32-bit
    counter can silently invert a control command sign.

------------------------------------------------------------------------
