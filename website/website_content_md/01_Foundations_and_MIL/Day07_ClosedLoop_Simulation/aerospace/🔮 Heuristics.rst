🔮 Heuristics
-------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| Settling time increases across runs           | Check if trim state drifted; re-trim and     |
|                                               | recompute.                                   |
+-----------------------------------------------+----------------------------------------------+
| Gain margin < 6 dB at one flight point        | **Do not** tune gain — investigate whether   |
|                                               | the plant model is missing an aero mode.     |
+-----------------------------------------------+----------------------------------------------+
| PIO index shifts from Cat I to Cat II         | Add transport-delay sweep; identify the delay|
|                                               | contribution that pushes category.           |
+-----------------------------------------------+----------------------------------------------+
| Cross-coupling exceeds spec on combined       | Check gain-scheduling alignment between axes;|
| pitch + roll manoeuvre                        | verify decoupling compensator coefficients.  |
+-----------------------------------------------+----------------------------------------------+
| Limit cycle detected in FFT at 8 Hz           | Suspect actuator rate-limiter interaction;   |
|                                               | increase rate limit or add notch filter.     |
+-----------------------------------------------+----------------------------------------------+
| Closed-loop run diverges after 60 s           | Likely integrator wind-up; verify anti-windup|
|                                               | logic fires when actuator saturates.         |
+-----------------------------------------------+----------------------------------------------+

----

