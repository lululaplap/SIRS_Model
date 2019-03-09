from main import SIR
from main import SIRS
import matplotlib.animation as animation
import matplotlib.pyplot as plt

#f = plt.figure()
plt.title("Mean and varience of infected count with varying probabilities")
sp =  plt.subplot(1, 2,1);

avgs,var = SIR.phaseSim(50,50)
plt.imshow(avgs)
plt.title("Average Number of infected cells")
plt.xlabel("p2")
plt.ylabel("p3")
sp =  plt.subplot(1, 2,2);
plt.imshow(var)
plt.xlabel("p2")
plt.ylabel("p3")
plt.title("Varience of Number infected cells")

plt.show()
