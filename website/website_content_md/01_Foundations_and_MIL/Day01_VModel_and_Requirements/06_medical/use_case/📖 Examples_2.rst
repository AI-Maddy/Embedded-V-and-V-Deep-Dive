📖 Examples
-----------
**Nominal Scenario** 🟢  
GIVEN validated sensor feedback  
WHEN therapy control is initiated  
THEN the system delivers therapy within specified parameters.

**Boundary Scenario** 🟡  
GIVEN a near-threshold dosing configuration  
WHEN alarm escalation timing is triggered  
THEN the system ensures proper alarm activation without delay.

**Fault Scenario** 🔴  
GIVEN a sensor spike/dropout or actuator command rejection  
WHEN the system detects an anomaly  
THEN it halts therapy and raises a critical alarm.

