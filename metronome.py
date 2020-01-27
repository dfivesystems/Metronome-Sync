from math import sin
from random import randint
import numpy as np
import matplotlib.pyplot as plt

inc = 0.05
k = 0.002
xlim = 100
mncount = 8

class Metronome:
    def __init__(self, idno, initialoffset, mlist):
        self.period = 2
        self.id = idno
        self.offset = initialoffset
        self.oldoffset = self.offset
        self.mlist = mlist
        self.y = np.array([sin(0+self.offset)])
        self.line = None

    def updateoffset(self):
        tempval = 0
        for metn in self.mlist:
            if metn.id == self.id:
                pass
            else:
                tempval += sin(metn.oldoffset-self.oldoffset)
        self.offset = self.oldoffset + (k*tempval)

    def calcyval(self, xval):
        self.y = np.append(self.y, [sin(xval+self.offset)])
        return sin(xval+self.offset)


if __name__ == "__main__":
    x = np.array([0])
    mnlist = list()
    lines  = list()
    for i in range(mncount):
        mnlist.append(Metronome(i, randint(0, 42), mnlist))
    plt.ion()
    fig = plt.figure()
    plt.show()
    ax = fig.add_subplot(111)
    for mn in mnlist:
        mn.line, = ax.plot(x, mn.y, label="Metronome {}".format(mn.id))
    ax.legend()
    fig.canvas.draw()

    for i in np.arange(0+inc, xlim, inc):
        x = np.append(x, [i])
        for mn in mnlist:
            mn.updateoffset()
            mn.calcyval(i)
            mn.line.set_xdata(x)
            mn.line.set_ydata(mn.y)
        for mn in mnlist:
            mn.oldoffset = mn.offset
        i += inc
        ax.relim() 
        ax.autoscale_view(True, True, True) 
        fig.canvas.draw()
        plt.pause(0.001)
