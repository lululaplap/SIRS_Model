from main import SIR
from main import SIRS
import matplotlib.animation as animation
import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

S = SIR(50,[0.8, 0.1, 0.012] )
ani = animation.FuncAnimation(fig, S.animate)
plt.show()
