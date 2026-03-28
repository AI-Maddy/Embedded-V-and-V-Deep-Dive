---
title: "Related Standards  References"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  **DO-178C Table     Verification of outputs of integration process ---
  A-7**               closed-loop is integration-level.

  **DO-331 §6.3**     Model simulation coverage --- closed-loop scenarios
                      contribute to model MC/DC.

  **ARP4754A §5.4**   System verification --- closed-loop captures
                      system-level interaction evidence.

  **MIL-STD-1797A**   Flying Qualities --- defines bandwidth, phase-delay, PIO
                      criteria.

  **MIL-F-8785C**     Flying Qualities --- Dryden turbulence model definition.

  **ARP4761**         Safety assessment --- FHA provides latency budgets used
                      in fault scenarios.

::: admonition
🚀 Remember

An open-loop test proves the controller **computes** correctly. A
closed-loop test proves the system **flies** correctly. Stability
margins, PIO freedom, cross-coupling limits, and fault recoverability
are properties that **only exist when the loop is closed** --- they are
the reason this day exists.
:::
