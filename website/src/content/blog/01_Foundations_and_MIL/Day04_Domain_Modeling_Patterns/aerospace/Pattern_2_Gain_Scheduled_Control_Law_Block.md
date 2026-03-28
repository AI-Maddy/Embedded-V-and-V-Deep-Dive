---
title: "Pattern 2   Gain Scheduled Control Law Block"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---



**🟡 Boundary Condition Pattern**

``` text
Gain table break-points must be tested at:
  ├── Exactly at break-point value          (interpolation edge)
  ├── 1 LSB below break-point               (lower segment)
  ├── 1 LSB above break-point               (upper segment)
  └── Minimum and maximum table extent      (clamping)
```

