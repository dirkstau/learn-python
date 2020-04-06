import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

w1 = QWidget()
w1.setGeometry(0,0,500,500)
w1.setWindowTitle("MyFirstGUI")


w1.show()

sys.exit(app.exec_())
