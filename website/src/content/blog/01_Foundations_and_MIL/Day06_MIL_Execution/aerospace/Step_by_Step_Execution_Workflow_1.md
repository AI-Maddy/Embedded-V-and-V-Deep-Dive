---
title: "Step by Step Execution Workflow"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  1a   Select scenario from  Each scenario maps to ≥1 requirement ID from
       matrix                the Verification Plan (VP).

  1b   Load `scenario.json`  Contains: stimuli profiles, acceptance
                             thresholds, turbulence seed, duration,
                             expected mode sequence, bus injection
                             schedule.

  1c   Validate schema       Run `jsonschema` check --- reject malformed
                             scenarios before execution.
  Parameter              Typical Aerospace Value

``` matlab
% === Headless MIL execution (MATLAB/Simulink) ===
load('params.mat');                       % CI-locked parameters
scenario = jsondecode(fileread('scenario.json'));
set_param('FCS_MIL_Harness', 'StopTime', num2str(scenario.T_sim));
set_param('FCS_MIL_Harness', 'FixedStep', '0.005');
set_param('FCS_MIL_Harness', 'Solver', 'ode4');

simOut = sim('FCS_MIL_Harness', 'ReturnWorkspaceOutputs', 'on');

% Save raw log
save(fullfile(scenario.evidence_dir, 'raw_log.mat'), 'simOut');
fprintf('✅ Run complete: %s\n', scenario.id);
```

**Step ④ --- 📊 Signal Logging Strategy**

::: tip
::: title
Tip
:::

💡 **Log everything at full rate** --- storage is cheap; re-running a
5-minute sim because you forgot to log one signal is not.
:::

  🎯 Primary outputs          Pitch / Roll / Yaw commands; surface      
                              deflections                               

  📡 Bus I/O                  ARINC 429 labels: raw word, decoded       
                              value, SSM, age counter, validity flag    

  🔄 Mode state               Active law (NORMAL / ALT / DIRECT),       
                              transition \| trigger, timestamp          

  🛡️ Monitor outputs          Disagree flag, cross-channel delta,       
                              latency from fault to flag assertion      

  🌡️ Environment inputs       Angle of attack, Mach, dynamic pressure   
                              Q, turbulence components (u, v, w)        

  📐 Error signals            Pitch error, roll error, heading error    
                              (RMS computed post-run for verdict)       

  ⚙️ Actuator state           Commanded vs. actual deflection;          
                              rate-limited flag; saturation flag        
