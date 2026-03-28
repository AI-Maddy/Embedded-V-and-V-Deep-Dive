---
title: "Deliverable Folder Structure"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 📂 Deliverable Folder Structure

``` text
MIL_Capstone/
├── 📋 campaign_manifest.json          ← frozen scenario matrix
├── 📋 env_manifest.json               ← hash-locked environment
├── 📋 DO330_TQL_Assessment.md         ← tool qualification record
│
├── models/
│   └── FCS_Pitch_Autopilot.slx        ← SUV model (locked hash)
│
├── params/
│   └── aero_params.mat                ← plant + controller gains
│
├── scenarios/
│   ├── SC-NOM-01.json → SC-NOM-02.json
│   ├── SC-BDY-01.json → SC-BDY-04.json
│   ├── SC-FLT-01.json → SC-FLT-04.json
│   ├── SC-MFT-01.json
│   └── SC-TRC-01.json
│
├── scripts/
│   ├── env_gate.py
│   ├── run_capstone.py
│   ├── verdict_engine.py
│   ├── package_evidence.sh
│   └── generate_report.py
│
├── templates/
│   └── capstone_report.html.j2
│
└── evidence/
    └── capstone_20260307_093000/
        ├── 📊 campaign_results.json
        ├── 🗺️  traceability_matrix.csv
        ├── 📄 MIL_Capstone_Report.html
        ├── 🔒 file_manifest.sha256
        ├── 📝 README.md
        │
        ├── SC-NOM-01/
        │   ├── scenario.json
        │   ├── raw_log.mat
        │   └── verdict.json
        │
        ├── SC-FLT-01/
        │   ├── scenario.json
        │   ├── raw_log.mat
        │   ├── fault_event_log.csv
        │   └── verdict.json
        │
        ├── SC-MFT-01/
        │   ├── scenario.json
        │   ├── raw_log.mat
        │   ├── fault_event_log.csv
        │   └── verdict.json
        │
        └── ... (12 scenario folders total)
```

------------------------------------------------------------------------
