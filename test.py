from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QBrush, QPen
import matplotlib
from PIL import Image
import numpy as np
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Window(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        self.setObjectName("MainWindow")
        self.showMaximized()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.showMaximized()

#        self.canvas = Label(self.centralwidget) #Klasse die von QLabel erbt, s. u.
#        self.canvas = QtWidgets.QWidget(self.centralwidget)
        
        #self.canvas.setGeometry(QtCore.QRect(0, 0, 801, 601))
#        self.setAutoFillBackground(True)
        l = QtWidgets.QVBoxLayout(self.centralwidget)
        sc = MyStaticMplCanvas(self.centralwidget, width=4, height=3, dpi=500)
        l.addWidget(sc)

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
        self.setWindowTitle(_translate("MainWindow", "PyQt5 Drawing Tutorial"))

#Das Label bekommt eine eigene Klasse, damit bezieht sich paintEvent auf das Label
#und nicht auf das CentralWidget
#class Label(QtWidgets.QLabel):
    
#    def __init__(self, parent=None):
#        super(Label, self).__init__(parent=parent)

#    def paintEvent(self, event):
#        super().paintEvent(event)
#        painter = QPainter()
#        painter.begin(self)
#        self.draw(event, painter) #das Zeichnen selbst findet in einer eigenen Methode statt
#        painter.end
    
#    def draw(self, event, painter):
#        painter.setPen(QPen(Qt.green,  0, Qt.SolidLine))
#        painter.drawEllipse(40, 40, 400, 400)
#        painter.drawText(20, 50, "test")

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=4, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot()
        self.axes.set_axis_off()
        self.compute_initial_figure(dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self, dpi):
        pass

class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self, dpi):
        
        d, n = dpi, 100  # Pixeldichte & Anzahl der Iterationen
        r = 2.5  # Fluchtradius (muss größer als 2 sein)

        x = np.linspace(-2.5, 1.5, 4 * d + 1)
        y = np.linspace(-1.5, 1.5, 3 * d + 1)

        A, B = np.meshgrid(x, y)
        C = A + B * 1j

        Z = np.zeros_like(C)
        T = np.zeros(C.shape)

        for k in range(n):
            M = abs(Z) < r
            Z[M] = Z[M] ** 2 + C[M]
            T[M] = k + 1

        
        FracImage = Image.fromarray(T)
        print(FracImage)

        self.axes.imshow(T, 
                         matplotlib.cm.RdGy,
                         animated=True, 
                         interpolation='gaussian'
                        )
        
        

if __name__ == "__main__":
    import sys
    App = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(App.exec())