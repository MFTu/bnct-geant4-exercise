
#read data file and draw histogram

import numpy as np
import matplotlib.pyplot as plt

#checkword, particle, energy, unit = np.loadtxt("proton500MeVdata.txt", delimiter =' ', usecols =(0, 1, 2, 3), unpack = True) 

energy = np.loadtxt("proton500MeVBeamOn1e4data.txt", delimiter =' ', usecols =(2), unpack = True)

print(energy)
print("number of data: ", len(energy))

#plt.plot([1, 2, 3, 4])
plt.hist(energy, bins=1000, range=(1.0e-9, 1.0e1))
plt.xscale('log')
plt.yscale('log')
#plt.ylabel('some numbers')
plt.xlabel('neutrons energy out of BSA (MeV)')
plt.show()


