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

avgs, vars = SIR.phaseCut(n=n,N=N)
plt.plot(avgs)
plt.show()
