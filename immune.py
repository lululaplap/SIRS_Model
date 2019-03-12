from main import SIR
from main import SIRS
import matplotlib.animation as animation
import matplotlib.pyplot as plt

avgs,vars = SIRS.immuneSim(100,[0.5,0.5,0.5],n=20)
plt.plot(avgs)
plt.show()
