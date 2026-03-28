---
title: "Parallel Execution Strategy"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# ⏱️ Parallel Execution Strategy

``` text
┌─────────────────────────────────────────────────────────────────┐
│             parsim() PARALLEL EXECUTION LAYOUT                 │
│                                                                 │
│  Worker 1  ──► CL-NOM-01 ──► CL-NOM-02 ──► CL-BDY-01 ──►     │
│  Worker 2  ──► CL-BDY-02 ──► FI-SEN-01 ──► FI-SEN-02 ──►     │
│  Worker 3  ──► FI-BUS-01 ──► FI-BUS-02 ──► FI-ACT-01 ──►     │
│  Worker 4  ──► FI-ACT-02 ──► FI-ENV-01 ──► FI-MULTI-01 ──►   │
│                                                                 │
│  Rules:                                                         │
│  • Each worker: independent MATLAB process (no shared state)   │
│  • Max workers: min(CPU cores, MATLAB licenses)                │
│  • Timeout: 3× expected single-run duration per scenario       │
│  • On failure: log error, continue remaining scenarios         │
└─────────────────────────────────────────────────────────────────┘
```

``` matlab
% === parsim() batch execution ===
scenarios = dir('scenarios/*.json');
simIn = [];
for i = 1:numel(scenarios)
    sc = jsondecode(fileread(fullfile('scenarios', scenarios(i).name)));
    simIn(i) = Simulink.SimulationInput('FCS_MIL_Harness');
    simIn(i) = simIn(i).setVariable('scenario', sc);
    simIn(i) = simIn(i).setModelParameter('StopTime', num2str(sc.T_sim));
    simIn(i) = simIn(i).setModelParameter('FixedStep', '0.005');
end

simOut = parsim(simIn, ...
    'ShowProgress', 'on', ...
    'UseFastRestart', 'on', ...
    'TransferBaseWorkspaceVariables', 'on', ...
    'ShowSimulationManager', 'off');

fprintf('✅ %d/%d scenarios completed\n', ...
    sum(~arrayfun(@(s) isempty(s.ErrorMessage), simOut)), numel(simOut));
```

