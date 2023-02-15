import numpy as np
import matplotlib.pyplot as plt

wavelength = 1550
neff = np.load("neff"+str(wavelength)+".npy")
width = np.load("wgwidth"+str(wavelength)+".npy")

plt.plot(width*1000,neff,marker="o")
plt.axhline(y = 1.4, color = 'black', linestyle = ':') 
plt.xlabel('Waveguide Width [nm]')
plt.ylabel('Effective Index')
plt.xlim([220, 500])
plt.axvline(x=280, color ='black',linestyle='-')
plt.title("Wavelength: 1310nm, Height = 220nm")\

#wg label
plt.text(310, 1.6, "280 nm", size=14, rotation=0.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0, 0, 0),
                   fc=(1., 1, 1),
                   )
         )

#cutoff
plt.text(468, 1.3, "Single Mode Cutoff\n SiO2 neff = 1.4", size=8, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

#TE0
plt.text(480, 2.8, "TE", size=12, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

#TM0
plt.text(480, 2.25, "TM", size=12, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

#TE1
plt.text(480, 1.85, "TE", size=12, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

#TM1
plt.text(490, 1.47, "TM", size=12, rotation=0.,
         ha="center", va="center",
         bbox=dict( pad = 0, 
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   )
         )

plt.show()
print("done");