# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:12:43 2019

@author: s1516989
"""


import numpy as np
# import matplotlib.pyplot as plt
from periodic_lattice import Periodic_Lattice
# import matplotlib.animation as animation

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)

class SIR(object):
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
        Icount = np.zeros(int(np.ceil(n/10)))
        for i in range(0,n):
            self.update()
            if i%10==0:
                j = int(i/10)
                Icount[j] = self.countInfected()
        return Icount

    def animate(self,i):
        data = self.update()
        ax1.clear()
        ax1.imshow(data)

    def countInfected(self):
        return np.sum((self.lattice ==1).astype(int))

    @classmethod
    def phaseSim(cls,n=20,N=50):
        x = np.linspace(0.1,1,n)
        y = np.linspace(0.1,1,n)
        print(x)
        print(y)
        avgs = np.zeros((n,n))
        var = np.zeros((n,n))
        for i in range(0,n):
            for j in range(0,n):
                print([i,j])
                p=[0.5,x[i],y[j]]
                S = cls(N,p)
                S.simulate(100)
                data = S.simulate(100)
                avgs[i,j] = np.mean(data)
                var[i,j] = np.var(data)

        return [avgs, var]

class SIRS(SIR):
    def __init__(self,N,p,immune):
        SIR.__init__(self,N,p)
        p1 = (1-immune)/3
        initArray = np.random.choice(a=[0,1,2,3], size=(self.N, self.N),p=[p1,p1,p1,immune])
        self.lattice = Periodic_Lattice(initArray)

    @classmethod
    def immuneSim(cls,d,p,n=10,N=1000):
        ps = np.linspace(0,1,n)
        avgs = np.zeros(n)
        vars = np.zeros(n)
        for i in range(n):
            S = cls(d,p,ps[i])
            S.simulate(100)#equilibrate
            count = S.simulate(1000)
            avgs[i] = np.mean(count)
            vars[i] = np.var(count)
        return [avgs,vars]
def main():
    S = SIR(50,[0.8, 0.1, 0.012] )
    #I = S.simulate(1000)
    #plt.plot(I/50**2)
    ani = animation.FuncAnimation(fig, S.animate)
    #avgs,var = SIR.phaseSim(20,50)
    # plt.imshow(avgs)
    # plt.show()
    # plt.imshow(var)
    # plt.show()


    plt.show()
