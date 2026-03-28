---
title: "Evidence Folder Structure Automated"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 📂 Evidence Folder Structure (Automated)

``` text
evidence/2026-03-07_campaign/
├── 📋 campaign_manifest.json          ← frozen scenario matrix
├── 📊 campaign_summary.json           ← execution times + status
├── 🗺️  traceability.csv                ← req → scenario → verdict
├── 📄 MIL_Campaign_Report.html        ← DER-ready HTML report
├── 🔒 file_manifest.sha256            ← integrity hashes
│
├── CL-NOM-01/
│   ├── scenario.json
│   ├── raw_log.mat
│   ├── verdict.json
│   ├── coverage.html
│   └── env_manifest.json
│
├── FI-ACT-01/
│   ├── scenario.json
│   ├── raw_log.mat
│   ├── fault_event_log.csv
│   ├── verdict.json
│   └── env_manifest.json
│
└── ... (one folder per scenario)
```

------------------------------------------------------------------------
