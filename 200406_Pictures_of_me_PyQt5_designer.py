# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '200406_Pictures_of_me_PyQt5_designer.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 401, 641))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("2014-11-13 16.31.36.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.Natural = QtWidgets.QPushButton(self.centralwidget)
        self.Natural.setGeometry(QtCore.QRect(10, 650, 111, 31))
        self.Natural.setObjectName("Natural")
        self.Artificial = QtWidgets.QPushButton(self.centralwidget)
        self.Artificial.setGeometry(QtCore.QRect(130, 650, 111, 31))
        self.Artificial.setObjectName("Artificial")
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

        self.Natural.clicked.connect(self.show_natural)
        self.Artificial.clicked.connect(self.show_artificial)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show the Coder"))
        self.Natural.setText(_translate("MainWindow", "Natural"))
        self.Artificial.setText(_translate("MainWindow", "Artificial"))

    def show_natural(self):
        self.photo.setPixmap(QtGui.QPixmap("2014-11-13 16.31.36.jpg"))

    def show_artificial(self):
        self.photo.setPixmap(QtGui.QPixmap("2014-11-13 16.32.13.jpg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
