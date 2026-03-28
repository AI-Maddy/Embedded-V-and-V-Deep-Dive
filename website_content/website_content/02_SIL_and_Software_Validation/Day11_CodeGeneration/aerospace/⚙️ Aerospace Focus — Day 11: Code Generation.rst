⚙️ Aerospace Focus — Day 11: Code Generation
===============================================

.. image:: _images/badge_phase_sil.svg
   :alt: Phase: SIL

.. image:: _images/badge_standard_do178c.svg
   :alt: Standard: DO-178C / DO-331

.. image:: _images/badge_criticality_dal.svg
   :alt: Criticality: DAL-A

.. image:: _images/badge_focus_codegen.svg
   :alt: Focus: Code Generation

.. note::
   🔀 **The Transition Point** — Today the model stops being a simulation
   artifact and becomes a **source of production code**.  In DO-178C terms, the
   model is now a "design representation" (DO-331 §MB.6.3) and the generated
   code must satisfy **every** objective in Table A-5 (software coding standards)
   and Table A-7 (verification of outputs).  A single unverified code-generation
   setting can propagate a latent fault from a Simulink block into the flight
   computer.  This day ensures that the code-generation pipeline itself is
   trustworthy, traceable, and evidence-ready.

----

