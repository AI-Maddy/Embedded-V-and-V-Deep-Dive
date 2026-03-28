Pattern 1 — 🔄 Hierarchical Mode-Logic State Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

Flight-control law mode transitions: Normal Law → Alternate Law → Direct Law
(Airbus-style) or Normal / Secondary / Direct (Boeing-style).  Also applies to
autopilot engagement/disengagement logic, envelope-protection activation, and
TCAS/ACAS mode arbitration.

.. rubric:: Structure

.. code-block:: text

   ┌──────────────────────────────────────────────────────────┐
   │                   MODE SUPERVISOR (Stateflow)            │
   │                                                          │
   │  [NORMAL_LAW] ──fault──►  [ALTERNATE_LAW]               │
   │       ▲                        │  ──severe fault──►      │
   │       │ recovery (if safe)     ▼                         │
   │       └────────────── [DIRECT_LAW]                       │
   │                                                          │
   │  Entry actions  : latch gain set, arm monitors           │
   │  During actions : execute active law, update status bus  │
   │  Exit actions   : freeze integrators, log transition     │
   └──────────────────────────────────────────────────────────┘

.. rubric:: DO-178C / DO-331 Obligations

+-------------------------------------+----------------------------------------------+
| Obligation                          | Guidance                                     |
+=====================================+==============================================+
| 📊 Decision coverage (MC/DC)        | Every mode-transition condition must be       |
|                                     | independently exercised (DAL-A requirement).  |
+-------------------------------------+----------------------------------------------+
| 🔗 Requirement traceability         | Each transition guard maps to ≥1 system       |
|                                     | requirement ID (e.g. ``FCS-MODE-REQ-017``).   |
+-------------------------------------+----------------------------------------------+
| 🔒 Transition inhibit conditions    | Must be modelled explicitly — not implied     |
|                                     | by absence of a trigger.                      |
+-------------------------------------+----------------------------------------------+
| 🧪 Reachability proof               | Every state must be reachable by ≥1 test      |
|                                     | case; unreachable states are dead code.       |
+-------------------------------------+----------------------------------------------+

.. rubric:: ⚠️  Common Mistakes

- Implicit default transitions that bypass safety interlocks.
- Missing ``exit`` action to freeze integrators on unexpected mode exit.
- Writing guards as compound boolean expressions not decomposed for MC/DC.

----

