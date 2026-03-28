🔮 Heuristics
--------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| MIL and SIL outputs differ by > 1e-4          | Check: solver step size, data type           |
|                                               | replacement, optimization level.             |
+-----------------------------------------------+----------------------------------------------+
| MISRA checker reports 50+ "required" viols    | Likely a code-gen setting issue — check      |
|                                               | Model Advisor pre-gen report first.          |
+-----------------------------------------------+----------------------------------------------+
| Generated code is 3× the expected size        | Check: dead-code branches from unused        |
|                                               | model variants or unconditional logging.     |
+-----------------------------------------------+----------------------------------------------+
| Compiler warns about implicit type conversion | Model has a type mismatch (e.g., int → float)|
|                                               | — fix at model level, re-generate.           |
+-----------------------------------------------+----------------------------------------------+
| Stack analysis shows 12 KB for an 8 KB target | Flatten deeply nested subsystems or reduce   |
|                                               | local array sizes.  Re-generate and re-check.|
+-----------------------------------------------+----------------------------------------------+

----

