# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '200407_QMessageBox_and_Popup_Windows.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showPopup = QtWidgets.QPushButton(self.centralwidget)
        self.showPopup.setGeometry(QtCore.QRect(230, 190, 291, 161))
        self.showPopup.setObjectName("showPopup")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.showPopup.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showPopup.setText(_translate("MainWindow", "Show Popup"))
    
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("Consider this important Information!")
        msg.setInformativeText("This tutorial will show you how to use and create"
            +" message boxes with pyqt5. It will explain all of the methods"
            +" associated with the QMessageBox class, like changing the"
            +" default buttons, setting the window title, icon and more!")
        msg.setDetailedText("Beide Ansätze werden für die Corona-Impfung geprüft."
            +" Welcher sich durchsetzen wird, kann zu diesem Zeitpunkt noch nicht"
            +" gesagt werden.")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Ignore)
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()
    
    def popup_button(self, i):
        print(i.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
