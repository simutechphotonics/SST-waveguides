#SimuTech Group
#Author: Stephen Lin
#Date: 2023
#Ths script is provided by SimuTech's SimuSkills platform.
#Access to this script is provided along with the TECH support package by SimuTech.
#The content provided should NOT be shared publicly.
#The scripts and files included are for educational purpose for SimuTech Group's customers.
#Customers are free to utilize the scripts and files in their own product design flows.

import numpy as np
import matplotlib.pyplot as plt

#PARAMETERS
wavelength = 1310 #used in line 17,18 to load the .npy file

#LOAD FILE
neff = np.load("neff"+str(wavelength)+".npy")
width = np.load("wgwidth"+str(wavelength)+".npy")

#PLOT RESULTS
plt.plot(width*1000,neff,marker="o")
plt.axhline(y = 1.4, color = 'black', linestyle = ':') 
plt.xlabel('Waveguide Width [nm]')
plt.ylabel('Effective Index')
plt.xlim([220, 500])
plt.axvline(x=280, color ='black',linestyle='-')
plt.title("Wavelength: 1310nm, Height = 220nm")\

#create wg label
plt.text(310, 1.6, "280 nm", size=14, rotation=0.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0, 0, 0),
                   fc=(1., 1, 1),
                   )
         )

#create cutoff line
plt.text(468, 1.3, "Single Mode Cutoff\n SiO2 neff = 1.4", size=8, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

#create TE0 label
plt.text(480, 2.8, "TE", size=12, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

#create TM0 label
plt.text(480, 2.25, "TM", size=12, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

#create TE1 label
plt.text(480, 1.85, "TE", size=12, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

#create TM1 label
plt.text(490, 1.47, "TM", size=12, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

plt.show()
print("done");