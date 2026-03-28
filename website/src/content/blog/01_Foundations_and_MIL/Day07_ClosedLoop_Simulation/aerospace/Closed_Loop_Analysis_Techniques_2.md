---
title: "Closed Loop Analysis Techniques 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🔬 Closed-Loop Analysis Techniques

**1️⃣ Time-Domain Step Response Analysis**

Extract settling time, overshoot, and steady-state error from the
closed-loop time history.

``` python
import numpy as np

def step_response_metrics(time, response, command, tolerance=0.02):
    """Compute T_s, %OS, e_ss from closed-loop step response."""
    final_val  = command
    error      = response - final_val
    e_ss       = abs(error[-1])
    peak       = np.max(response)
    overshoot  = max(0, (peak - final_val) / abs(final_val)) * 100  # %

    # Settling: last time |error| > tolerance * |final_val|
    band       = tolerance * abs(final_val)
    outside    = np.where(np.abs(error) > band)[0]
    t_settle   = time[outside[-1]] - time[0] if len(outside) > 0 else 0.0

    return {"T_s": t_settle, "OS_pct": overshoot, "e_ss": e_ss}
```

**2️⃣ Frequency-Domain Margin Estimation**

Linearise the closed-loop model at the operating point and extract
gain/phase margin.

``` matlab
% === Linearise FCS + plant at cruise trim ===
io = getlinio('FCS_CL_Harness');           % mark loop-break points
linsys = linearize('FCS_CL_Harness', io);
[GM, PM, Wcg, Wcp] = margin(linsys);
fprintf('Gain Margin: %.1f dB @ %.1f rad/s\n', 20*log10(GM), Wcg);
fprintf('Phase Margin: %.1f deg @ %.1f rad/s\n', PM, Wcp);
assert(20*log10(GM) >= 6, 'Gain margin below 6 dB!');
assert(PM >= 45,          'Phase margin below 45 deg!');
```

**3️⃣ PIO Susceptibility Assessment**

Use bandwidth / phase-delay criteria (MIL-STD-1797A) or Neal-Smith
analysis.

``` text
Category I  (no PIO tendency):  ω_BW > 2 rad/s AND τ_p < 0.12 s
Category II (mild tendency):    ω_BW > 1 rad/s AND τ_p < 0.20 s
Category III (PIO prone):       anything worse → FAIL
```

**4️⃣ Limit-Cycle Detection**

Check for sustained oscillations in the residual after the command
transient decays.

``` python
def detect_limit_cycle(signal, time, window_start, fft_threshold=0.01):
    """Return True if a limit cycle is detected in the tail of the signal."""
    idx = time >= window_start
    tail = signal[idx] - np.mean(signal[idx])
    spectrum = np.abs(np.fft.rfft(tail))
    spectrum /= len(tail)
    dominant = np.max(spectrum[1:])  # exclude DC
    return dominant > fft_threshold, dominant
```

------------------------------------------------------------------------
