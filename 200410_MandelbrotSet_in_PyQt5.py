# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fractal.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QFont
#import Mandelbrot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 349)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 300))
        self.centralwidget.setObjectName("centralwidget")
        self.complexPlaine = QtWidgets.QLabel(self.centralwidget)
        self.complexPlaine.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.complexPlaine.setMinimumSize(QtCore.QSize(400, 300))
        self.complexPlaine.setObjectName("complexPlaine")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MandelbrotSet in PyQt5"))
        #self.complexPlaine.setText(_translate("MainWindow", "complexPlain"))
    
    #def paintMandelbrotSet(self):
        #self.centralWidget = self.complexPlaine
        #mbs = Mandelbrot.MandelbrotSet()
        #mbs.paintMandelbrotSet(self.complexPlaine)

        #canvas = QtGui.QPixmap(400, 300)
        #self.complexPlaine.setPixmap(canvas)
        
        #painter = QtGui.QPainter(self.complexPlaine)
        #painter.begin(self.complexPlaine)
        #painter.setPen(QColor(168, 34, 3))
        #painter.drawLine(10, 10, 300, 200)
        #painter.end() 


    def paintEvent(self, event):
        self.centralWidget = self.complexPlaine
        canvas = QtGui.QPixmap(400, 300)
        self.complexPlaine.setPixmap(canvas)

        painter = QtGui.QPainter(self.complexPlaine)
        painter.begin(self.complexPlaine)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.red)
        painter.setBrush(QtCore.Qt.white)
        painter.drawLine(400, 100, 100, 100)
        painter.end()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.complexPlaine.update()
    #ui.paintMandelbrotSet()
    MainWindow.show()
    sys.exit(app.exec_())
