💡 Additional Deep-Dive Notes
-----------------------------
.. note::
   **Domain Focus**: Medical  
   **Phase Focus**: MIL (Model-in-the-Loop)  

.. important::
   **Evidence Priorities**:  
   - Functional correctness 🟢  
   - Timing behavior 🟡  
   - Robustness 🔴  
   - Traceability 🟢  

.. admonition:: Patterns to Follow  
   - Baseline-first comparison methodology.  
   - Fixed acceptance thresholds for predictable outcomes.  
   - Deterministic reruns to ensure repeatability.  

.. warning::
   **Anti-Patterns**:  
   - Post-hoc threshold tuning 🟡  
   - Missing raw artifacts 🔴  
   - Incomplete negative-path checks 🟡  

.. warning::
   **Pitfalls**:  
   - Hidden assumptions 🔴  
   - Interface timing drift 🟡  
   - Weak requirement-to-test linkage 🟢  

