Tabular Summary 📊  
------------------  
.. list-table:: Automotive MIL Verification Summary  
   :widths: 20 30 25 25  
   :header-rows: 1  

   * - **Category**  
     - **Examples**  
     - **Standards Alignment**  
     - **Priority**  
   * - Nominal Scenario 🟢  
     - Adaptive cruise control under normal traffic conditions  
     - ISO 26262 Part 6  
     - 🟢  
   * - Boundary Scenario 🟡  
     - Stop-and-go traffic with tight headway constraints  
     - ISO 26262 Part 3  
     - 🟡  
   * - Fault Scenario 🔴  
     - Sensor dropout and invalid CAN frame injection  
     - ISO 26262 Part 5  
     - 🔴  

.. warning:: Ensure all test results are reviewed for compliance with ISO 26262, ISO 21434, and ASPICE SWE.6.
