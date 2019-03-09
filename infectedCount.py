from main import SIR
from main import SIRS
import matplotlib.animation as animation
import matplotlib.pyplot as plt

S = SIR(50,[0.8, 0.1, 0.012] )
I = S.simulate(1000)
plt.plot(I/50**2)
plt.show()
