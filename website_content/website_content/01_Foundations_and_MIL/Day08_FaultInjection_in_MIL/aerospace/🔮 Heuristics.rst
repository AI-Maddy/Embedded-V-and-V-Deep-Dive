🔮 Heuristics
-------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| Monitor fails to detect injected fault        | Check injection point — is it upstream of the|
|                                               | monitor's observation point?                 |
+-----------------------------------------------+----------------------------------------------+
| Detection latency exceeds FHA budget by 10 ms | Verify bus timing + frame-age counter        |
|                                               | resolution; 1-frame jitter may explain.      |
+-----------------------------------------------+----------------------------------------------+
| Multi-fault scenario causes model divergence  | Add saturation / integrator reset on mode    |
|                                               | transition; verify anti-windup fires.        |
+-----------------------------------------------+----------------------------------------------+
| Same fault, different severity → wildly       | Investigate non-linear monitor threshold;    |
| different latency                             | small faults may straddle detection boundary.|
+-----------------------------------------------+----------------------------------------------+
| Regression run detects fault 5 ms faster      | Check if trim state or turbulence seed       |
|                                               | changed — both shift the detection baseline. |
+-----------------------------------------------+----------------------------------------------+
| DER asks "why no combined sensor + actuator   | Point to FTA cut set analysis; if no such    |
| fault?"                                       | cut set exists, justify; if it does, add it. |
+-----------------------------------------------+----------------------------------------------+

----

