---
title: "Evidence Folder Structure"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 📂 Evidence Folder Structure

``` text
Day11_CodeGeneration/
└── evidence/
    ├── 📋 codegen_settings.json         ← frozen Embedded Coder config
    ├── 📋 env_manifest.json              ← MATLAB version + model hash
    │
    ├── generated_code/
    │   ├── *.c, *.h                      ← generated source
    │   ├── reports/
    │   │   ├── 📊 codegen_report.html    ← block ↔ C traceability
    │   │   ├── 📋 misra_report.html      ← MISRA C:2012 compliance
    │   │   └── 🔒 file_manifest.sha256   ← integrity hashes
    │   └── subsystems/ + integration/
    │
    ├── build/
    │   ├── 📄 FCS_Pitch.o                ← cross-compiled object
    │   ├── 📋 compiler_output.log        ← zero-warning build log
    │   └── 📊 size_report.txt            ← code/data size
    │
    └── traceability/
        ├── 🗺️  req_to_block.csv           ← requirement ↔ block mapping
        ├── 🗺️  block_to_code.csv          ← block ↔ C function mapping
        └── 🗺️  codegen_traceability.csv   ← full chain: req → block → C line
```

