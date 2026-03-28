# 🧪 Execution Pattern

\### Nominal Scenario 🟢 1. Run nominal scenario and store baseline
artifacts 📁 2. Verify that baseline artifacts are correctly stored 🟢

\### Boundary Scenario 🟡 1. Inject edge conditions relevant to day
objective 🚨 2. Re-run with controlled variation to confirm
repeatability 🔄 3. Verify that controlled variation does not affect
baseline artifacts 🟡

\### Fault Scenario 🔴 1. Inject fault conditions relevant to day
objective 🚨 2. Re-run with fault injection 🔴 3. Verify that fault
injection affects baseline artifacts as expected 🔴
