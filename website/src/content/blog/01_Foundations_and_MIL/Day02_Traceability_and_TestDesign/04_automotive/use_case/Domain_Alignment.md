---
title: "Domain Alignment"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---



# Domain Alignment 🌐

-   **Standards Referenced**:
    -   ISO 26262: Functional safety for road vehicles (ASIL
        determination and safety goals).
    -   ISO 21434: Cybersecurity engineering for automotive systems.
    -   ASPICE: Process capability for automotive software development.
-   **Critical Hazards**:
    -   🟢 Nominal: Adaptive cruise control maintaining safe distance.
    -   🟡 Boundary: Stop-and-go traffic with tight timing constraints.
    -   🔴 Fault: Sensor dropout leading to invalid CAN frame injection.
-   **Relevant Interfaces**:
    -   CAN (Controller Area Network)
    -   LIN (Local Interconnect Network)
    -   FlexRay
    -   Automotive Ethernet
