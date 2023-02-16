# Scripted Simulation Template: Waveguides
PIC waveguide design script using lumerical and its Python API (LumAPI).
The simulation can be used to find optimal cross section dimensions for desired modes
at selected wavelengths.

## Contents
This template has four parts: 
1. `1_design_wg.py` - Sets up the parameters of the simulation within Python, and calls the Lumerical tools via LumAPI
2. `wg_2d_draw.lsf` - Sets up the simulation objects within Lumerical MODE
3. `wg_2d_neff_sweep_width.lsf` - Example of a LSF sweep script, turned into a Function. Callable via Python. Also still runnable as a script.
4. `2_analys_neff_width.py` - Post simulation data processing. Demonstrates how to load in the raw data extracted from the simulation.

## How to Use
Using Python, run in the following order:
1. 1_design_wg.py
2. 2_analys_neff_width.py

## Prerequisites
- Lumerical
- LumAPI
- NumPy
- Matplotlib
