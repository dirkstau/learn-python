"""
Animation der iterativen Berechnung
der Mandelbrotmenge mittels Matritzen.
"""

import numpy as np
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


class MandelbrotSet():

    def __init__(self):
        
        d, self.n = 200, 80  # Pixeldichte & Anzahl der Iterationen
        self.r = 2.5  # Fluchtradius (muss größer als 2 sein)

        x = np.linspace(-2.5, 1.5, 4 * d + 1)
        y = np.linspace(-1.5, 1.5, 3 * d + 1)

        A, B = np.meshgrid(x, y)
        self.C = A + B * 1j

        self.Z = np.zeros_like(self.C)
        self.T = np.zeros(self.C.shape)

    def calcMandelbrotSet(self, plane):
        for k in range(self.n):
            M = abs(self.Z) < self.r
            self.Z[M] = self.Z[M] ** 2 + self.C[M]
            self.T[M] = k + 1
            im = plt.imshow(self.T, cmap=plt.cm.twilight_shifted,
                            animated=True, interpolation='gaussian')
        return im

    def paintMandelbrotSet(self, plaine):
        canvas = QtGui.QPixmap(400, 300)
        plaine.setPixmap(canvas)
        
        painter = QtGui.QPainter(plaine)


        painter.drawLine(10, 10, 300, 200)
        painter.end()    
        


if __name__ == "__main__":
    #pass
    mbs = MandelbrotSet()
    print(mbs.T)
    #im = mbs.calcMandelbrotSet()
    #plt.show()
