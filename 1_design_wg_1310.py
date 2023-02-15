#SimuTech Group
#Author: Stephen Lin
#Date: 2023
#Ths script is provided by SimuTech's SimuSkills platform.
#Access to this script is provided along with the TECH support package by SimuTech.
#The content provided should NOT be shared publicly.
#The scripts and files included are for educational purpose for SimuTech Group's customers.
#Customers are free to utilize the scripts and files in their own product design flows.

# Import Lumapi
# Please note and update the version in the path and update accordingly
import sys, os
sys.path.append("C:\\Program Files\\Lumerical\\v222\\api\\python\\") #Default windows lumapi path
sys.path.append("/opt/lumerical/v212/api/python/lumapi.py") #Default linux lumapi path
sys.path.append(os.path.dirname(__file__)) #Current directory

import lumapi #lumerical's python api
import numpy as np
mode1=lumapi.MODE(); #Creates a MODE object to access MODE related functions

#PARAMS
wavelength=1.31 #in um
modes=4 #number of modes to track
wg_start=0.2 #um 
wg_end=0.8 #um
wg_step=0.02 #um, step size of the waveguide range

code = open('wg_2d_draw.lsf').read() #loads the wg setup file to create the geometry
mode1.eval(code) #executes the code
code = open('wg_2d_neff_sweep_width.lsf').read() #loads the lsf file with the `neff sweep` function, see line 23
mode1.eval(code)
neff = mode1.CalcNeffSweepWidth(wavelength,modes,wg_start,wg_end,wg_step) #calls the neff sweep function written in the lsf file. `neff` is given the return value specified in the lsf file.
wgwidth = np.arange(wg_start,wg_end,wg_step) #sets up an np array, used for plotting. Can also read out from the MODE object, but results are the same.

np.save("neff"+str(int(wavelength*1000)),neff) #save results as .npy files
np.save("wgwidth"+str(int(wavelength*1000)),wgwidth)
print('Complete')