from main import SIR
from main import SIRS
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import sys
args = sys.argv
if len(args)==3:
    N=int(args[1])
    n=int(args[2])
else:
    print("N:lattice size (int), n:Number of data points(int)")
x = np.linspace(0,1,n)
avgs,vars = SIRS.immuneSim(N,[0.5,0.5,0.5],n=n)
errors = vars/(np.sqrt(100)*N*N)
print(errors)
print(avgs)
np.savetxt("ImmuneAvgs.csv",avgs)
np.savetxt("ImmuneErrors.csv",errors)
plt.plot(x,avgs)
plt.errorbar(x,avgs,xerr=None ,yerr=errors,ls='none')
plt.show()
