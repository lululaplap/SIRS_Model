from main import SIR
from main import SIRS
import matplotlib.animation as animation
import matplotlib.pyplot as plt

import sys
args = sys.argv
if len(args)==5:
    N=int(args[1])
    p1=float(args[2])
    p2=float(args[3])
    p3=float(args[4])
else:
    print("N:lattice size (int), p1:p2:p2 probabilities 1, 2 and 3 (int)")
    print(len(args))



S = SIR(N,[p1,p2,p3] )
I = S.simulate(1000)
plt.plot(I/50**2)
plt.show()
