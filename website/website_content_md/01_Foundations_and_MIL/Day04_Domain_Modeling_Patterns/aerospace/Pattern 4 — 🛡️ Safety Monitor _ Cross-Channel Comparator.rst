Pattern 4 — 🛡️ Safety Monitor / Cross-Channel Comparator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

Dual/triple redundant channel comparison logic that detects disagreement between
redundant sensors or computation lanes and triggers a fault flag within the latency
budget defined by the FHA.

.. rubric:: Pattern Variants

.. rubric:: 🔵 Dual-Channel Comparator (2oo2)

.. code-block:: text

   Channel_A ─┐
              ├──► |ΔA−B| > THRESHOLD? ──YES──► DISAGREE_FLAG
   Channel_B ─┘                          │
                                        NO
                                         └──► AGREE (use average or Channel_A)

.. rubric:: 🟣 Triple-Voting Median Select (2oo3)

.. code-block:: text

   Ch_A ─┐
   Ch_B ─┼──► Sort(A,B,C) → median value ──► Control Law Input
   Ch_C ─┘
          └──► |max−min| > THRESHOLD? ──YES──► MONITOR_FLAG + log outlier

.. rubric:: Critical Modeling Rules

- Monitor computation must be in a **separate subsystem** from the control law —
  never share state variables between the monitor and the monitored function.
- Latency budget: monitor must assert flag within the time defined in the System
  Safety Assessment (SSA); model the worst-case execution path explicitly.
- All thresholds must be parametric (``Simulink.Parameter``); justify threshold
  values with reference to sensor accuracy budget from the SSA.

----

