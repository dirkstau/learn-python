import matplotlib.pyplot as plt
import numpy as np

from PyQt5 import (
    QtGui, 
    QtWidgets, 
    QtCore,
)
from PyQt5.QtCore import (
    QRect, 
    QSize, 
    QPoint,
)
from PyQt5.QtWidgets import (
    QRubberBand,
)
from PyQt5.QtGui import (
    QPixmap,
)
from PIL import (
    Image,
)
from PIL.ImageQt import (
    ImageQt,
)


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.showMaximized()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.showMaximized()

        l = QtWidgets.QHBoxLayout(self.centralwidget)

        mbs = MandelbrotSet()

        T = mbs.calcMandelbrotSet()

        cm = mbs.applyColormap()
        cmT = cm(T) * 255

        cm_img = Image.fromarray(cmT.astype('uint8'), mode = "RGBA")
        qimg = ImageQt(cm_img)
        pixmap = QPixmap.fromImage(qimg)

        label = Label()
        label.setPixmap(pixmap)
        label.setSizePolicy(       QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        label.updateGeometry()
        l.addWidget(label)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Mandelbrot Set"))

     
class Label(QtWidgets.QLabel):
    
    def __init__(self):
        super().__init__()
        self.origin = QPoint()
        self.rubberBand = None

#    def paintEvent(self, event):
#        qp = QtGui.QPainter(self)
#        br = QtGui.QBrush(QtGui.QColor(100, 10, 10, 40))  
#        qp.setBrush(br)   
#        qp.drawRect(QtCore.QRect(self.begin, self.end))       

    def mousePressEvent(self, event):
        super(Label, self).mousePressEvent(event)
        self.origin = event.pos()

        if not self.rubberBand:
            self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
            print("Rubber!")
        self.rubberBand.setGeometry(QRect(self.origin, QSize()))
        self.rubberBand.show()

        #self.update()

    def mouseMoveEvent(self, event):
        self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if self.rubberBand:
            self.rubberBand.hide()
        #self.update()


class MandelbrotSet():
    def __init__(self):
        print("MandelbrotSet.__init__ wurde aufgerufen...")


    def applyColormap(self, name=None, lut=None):
        """
        Returns a specific colormap instance, or a default one 
        if *name* is None or if a colormap *name* doesn't exist.
        """
        name = "twilight"
        try:
            cm = plt.get_cmap(name, lut)
        except ValueError: #falls "name" keine exitierende Colormap ist...
            cm = plt.get_cmap()
        return cm


    def calcMandelbrotSet(self, startX=-2.5, stopX=1.5, startY=-1.5, stopY=1.5, dpi=100, iterations=100, divergence_radius=2.5):

        d = dpi 
        n = iterations  # Pixeldichte & Anzahl der Iterationen
        r = divergence_radius  # Fluchtradius (muss größer als 2 sein)

        x = np.linspace(startX, stopX, 4 * d + 1)
        y = np.linspace(startY, stopY, 3 * d + 1)

        A, B = np.meshgrid(x, y)
        C = A + B * 1j

        Z = np.zeros_like(C)
        T = np.zeros(C.shape)

        for k in range(n):
            M = abs(Z) < r
            Z[M] = Z[M] ** 2 + C[M]
            T[M] = k + 1

        T = T / n
        return T


if __name__ == "__main__":
    import sys
    App = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(App.exec())