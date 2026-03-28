---
title: "CI Pipeline Configuration"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 🔄 CI Pipeline Configuration

**GitLab CI Example (`gitlab-ci.yml`)**

``` yaml
  - gate
  - execute
  - verdict
  - package
  - report

  MATLAB_VER: "R2025a"
  CAMPAIGN_FILE: "campaign_manifest.json"

  stage: gate
  script:
    - python3 scripts/env_gate.py
  artifacts:
    reports:
      junit: gate_report.xml

  stage: execute
  needs: [env-gate]
  script:
    - python3 scripts/run_batch.py
  timeout: 4h
  artifacts:
    paths:
      - evidence/
    expire_in: 90 days

  stage: verdict
  needs: [mil-batch]
  script:
    - python3 scripts/verdict_engine.py evidence/*/
  artifacts:
    paths:
      - evidence/*/verdict.json

  stage: package
  needs: [verdict]
  script:
    - bash scripts/evidence_packager.sh evidence/*_campaign
  artifacts:
    paths:
      - evidence/

  stage: report
  needs: [package]
  script:
    - python3 scripts/report_gen.py
  artifacts:
    paths:
      - evidence/**/MIL_Campaign_Report.html
      - evidence/**/traceability.csv
```

**Jenkins Declarative Pipeline (`Jenkinsfile`)**

``` groovy
pipeline {
    agent { label 'matlab-r2025a' }
    options { timeout(time: 6, unit: 'HOURS') }

    stages {
        stage('Environment Gate') {
            steps { sh 'python3 scripts/env_gate.py' }
        }
        stage('Batch Execution') {
            steps { sh 'python3 scripts/run_batch.py' }
        }
        stage('Verdict') {
            steps { sh 'python3 scripts/verdict_engine.py evidence/*/' }
        }
        stage('Evidence Package') {
            steps { sh 'bash scripts/evidence_packager.sh evidence/*_campaign' }
        }
        stage('Report') {
            steps { sh 'python3 scripts/report_gen.py' }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'evidence/**', fingerprint: true
            emailext subject: "MIL Campaign ${currentBuild.result}",
                     body: '${FILE, path="evidence/campaign_summary.json"}'
        }
    }
}
```

