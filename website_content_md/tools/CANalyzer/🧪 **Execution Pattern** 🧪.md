# 🧪 **Execution Pattern** 🧪

\### 🟢 Nominal Scenario 🟢

::: note
::: title
Note
:::

Capture baseline artifacts under nominal conditions.

GIVEN: System in nominal state 🟢. WHEN: Run tool with default settings.
THEN: Store baseline artifacts.
:::

\### 🟡 Boundary Scenario 🟡

::: important
::: title
Important
:::

Inject edge conditions to test system limits.

GIVEN: System in boundary state 🟡. WHEN: Run tool with modified
settings. THEN: Verify system response.
:::

\### 🔴 Fault Scenario 🔴

::: warning
::: title
Warning
:::

Introduce faults to test system robustness.

GIVEN: System in fault state 🔴. WHEN: Run tool with fault injection.
THEN: Verify system recovery.
:::
