# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:12:43 2019

@author: s1516989
"""


import numpy as np
import matplotlib.pyplot as plt
from periodic_lattice import Periodic_Lattice
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

class SIRS(object):
    def __init__(self,N,p):
        """
        0: susceptible
        1: infected
        2: recovered
        """
        self.p = np.array(p)
        self.N = N
        initArray = np.random.choice(a=[0,1,2], size=(self.N, self.N))
        self.lattice = Periodic_Lattice(initArray)
        self.mask = np.zeros((3,3))
        self.mask[1,0]=1
        self.mask[0,1]=1
        self.mask[2,1]=1
        self.mask[1,2]=1


    def update(self):
        for i in range(0,self.N**2):

            x,y= np.random.randint(0,self.N,2)
            pos = [x,y]
            if self.lattice[x,y] == 1:
                self.lattice[x,y] = np.random.choice(a=[2,1],p=[self.p[1],1-self.p[1]])
            elif self.lattice[x,y] == 2:
                self.lattice[x,y] = np.random.choice(a=[0,2],p=[self.p[2],1-self.p[2]])
            elif self.lattice[x,y] == 0:
                #mask = Periodic_Lattice(np.zeros((self.N,self.N)))
                #print([x,y])
                #mask[x-1:x+2,y-1:y+2]=self.mask
                #print(mask)

                #NN = mask*self.lattice
                NN = [self.lattice[(pos[0]+1)%self.N,pos[1]],self.lattice[pos[0],(pos[1]+1)%self.N],self.lattice[(pos[0]-1)%self.N,pos[1]],self.lattice[pos[0],(pos[1]-1)%self.N]]
                if 1 in NN:
                    self.lattice[x,y] = np.random.choice(a=[1,0],p=[self.p[0],1-self.p[0]])

        return self.lattice

    def simulate(self,n):
        Icount = np.zeros(n)
        for i in range(0,n):
            self.update()
            Icount[i] = self.countInfected()
        return Icount

    def animate(self,i):
        data = self.update()
        ax1.clear()
        ax1.imshow(data)

    def countInfected(self):
        return np.sum((self.lattice ==1).astype(int))

def main():
    S = SIRS(50,[0.5,0.0333,0.5] )
    #I = S.simulate(1000)
    #plt.plot(I/50**2)
    ani = animation.FuncAnimation(fig, S.animate)
    plt.show()

main()
