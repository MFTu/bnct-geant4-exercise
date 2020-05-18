
#read data file and draw histogram

import numpy as np
import matplotlib.pyplot as plt

#checkword, particle, energy, unit = np.loadtxt("proton500MeVdata.txt", delimiter =' ', usecols =(0, 1, 2, 3), unpack = True) 

energy = np.loadtxt("proton500MeVBeamOn1e4data_0517_2020.txt", delimiter =' ', usecols =(2), unpack = True)

logenergy = np.log10(energy)

print(energy)
print(logenergy)

print("number of data: ", len(energy))
print("number of data: ", len(logenergy))

#plt.plot([1, 2, 3, 4])

#plt.hist(logenergy, bins=1000, range=(-9.0, 1.0))
plt.hist(logenergy, bins=400, range=(-9.0, 1.0))

#plt.xscale('log')
plt.yscale('log')
#plt.ylabel('some numbers')
plt.xlabel('neutrons energy out of BSA (MeV) log10')
plt.show()


