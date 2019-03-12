from main import SIR
from main import SIRS
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

import sys
args = sys.argv
if len(args)==3:
    N=int(args[1])
    n=int(args[2])
else:
    print("N:lattice size (int), n:resolution (int)")
x = np.linspace(0,1,n)


#f = plt.figure()
plt.title("Mean and varience of infected count with varying probabilities")
sp =  plt.subplot(1, 2,1);

avgs,var = SIR.phaseSim(n,N)
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
