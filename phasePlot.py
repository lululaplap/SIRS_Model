from main import SIR
from main import SIRS
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

#f = plt.figure()
plt.title("Mean and varience of infected count with varying probabilities")
sp =  plt.subplot(1, 2,1);
N=50
avgs,var = SIR.phaseSim(25,N)
np.savetxt("PhaseAvg.csv",avgs)
np.savetxt("PhaseVar.csv",var)
plt.imshow(avgs/N**2,vmin=0, vmax=1, cmap='jet', aspect='auto', origin='lower')
plt.title("Average Number of infected cells")
plt.xlabel("p2")
plt.ylabel("p3")
plt.colorbar()

sp =  plt.subplot(1, 2,2);
plt.imshow(var, cmap='jet', aspect='auto', origin='lower')
plt.xlabel("p2")
plt.ylabel("p3")
plt.title("Varience of Number infected cells")
plt.colorbar()

plt.show()
