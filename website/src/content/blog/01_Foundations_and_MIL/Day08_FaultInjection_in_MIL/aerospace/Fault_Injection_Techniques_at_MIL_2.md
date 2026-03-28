---
title: "Fault Injection Techniques at MIL 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🛠️ Fault Injection Techniques at MIL

**1️⃣ Signal Override (Switch-Based)**

The simplest technique: a Simulink switch block selects between the
nominal signal and the injected fault value based on a trigger.

``` text
nominal_signal ──┐
                 ├── [Switch] ──► downstream
fault_value    ──┘
                 ▲
                 │  trigger: (sim_time >= T_fault)
```

**Pros:** Easy, deterministic, no model modification. **Cons:** Can only
inject at exposed signal points; cannot model internal corruption.

**2️⃣ Parameter Perturbation**

Modify a model parameter (gain, bias, limit) at runtime to simulate
degradation.

``` matlab
% Inject 2°/s gyro bias ramp starting at T = 40 s
if simTime >= 40
    gyro_bias = min(2.0, (simTime - 40) * 0.4);  % ramp 0.4 °/s²
    imu_output.p = imu_output.p + deg2rad(gyro_bias);
end
```

**Use for:** Sensor drift, gain degradation, threshold corruption.

**3️⃣ Bus-Level Injection**

Manipulate ARINC 429 / AFDX fields directly: SSM bits, BNR data field,
label number, or suppress the label entirely to simulate timeout.

``` python
# ARINC 429 label fault injection
def inject_arinc_fault(label_stream, fault_type, t_inject):
    """Modify ARINC 429 label fields at injection time."""
    for word in label_stream:
        if word.time >= t_inject:
            if fault_type == "SSM_NCD":
                word.ssm = 0b01          # No Computed Data
            elif fault_type == "SSM_FW":
                word.ssm = 0b00          # Failure Warning
            elif fault_type == "STALE":
                word.suppress = True     # stop label transmission
            elif fault_type == "CORRUPT_BNR":
                word.data ^= 0x1FFFF     # flip all BNR bits
    return label_stream
```

**Use for:** Realistic avionics bus fault simulation (stale data, SSM
errors, label corruption).

**4️⃣ Actuator Fault Model**

Replace the nominal actuator model with a fault-mode variant.

``` text
Fault Mode          │ Implementation
════════════════════╪════════════════════════════════════════════
JAM                 │ Output frozen at position when fault fires
RUNAWAY             │ Output ramps to hard-stop at max rate
FREE-FLOAT          │ Output follows aerodynamic hinge moment
RATE DEGRADATION    │ Max rate reduced to X % of nominal
OSCILLATORY         │ Sinusoidal disturbance added to command
```

**5️⃣ Environment Fault Injection**

Inject windshear, icing, or extreme atmosphere deviations into the plant
model.

``` matlab
% Inject 30-kt windshear during approach at 200 ft AGL
if alt_agl <= 200 && alt_agl >= 50
    wind_shear_kts = 30 * (1 - (alt_agl - 50) / 150);  % ramp
    Vwind_x = wind_shear_kts * 0.5144;  % kt → m/s
end
```

**6️⃣ Combinatorial / Multi-Fault Injection**

Inject two or more faults simultaneously or in sequence to test FTA cut
sets.

``` text
┌──────────────────────────────────────────────────────────────┐
│            MULTI-FAULT INJECTION TIMELINE                   │
│                                                              │
│  T = 0 s     Normal operation (baseline)                    │
│  T = 30 s    FAULT A: ADC-1 ARINC 429 label → STALE        │
│  T = 32 s    FAULT B: ADC-2 SSM → NCD                       │
│  T = 35 s    Expected: DISAGREE flag + DEGRADED_MODE entry  │
│  T = 40 s    FAULT C: Elevator actuator jam                 │
│  T = 42 s    Expected: Standby actuator active; crew alert  │
│  T = 60 s    End of scenario                                │
└──────────────────────────────────────────────────────────────┘
```

------------------------------------------------------------------------
