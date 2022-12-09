from datetime import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout


def myCalc():
    a = form.lineEdit.text()
    b = form.lineEdit_2.text()

    a = datetime.strptime(a, "%d.%m.%Y")
    b = datetime.strptime(b, "%d.%m.%Y")

    e = (b - a).days
    if e < 2:
        g = 45
    elif e == range(2, 7):
        g = 40
    else:
        g = 35
    cost = e * g
    result = str(cost)
    aa = str(e)

    form.plainTextEdit.appendPlainText(result)
    form.plainTextEdit_2.appendPlainText(aa
                                         )







# Form, Window = uic.loadUiType("myApp4.ui")

app = QApplication([])
window = QWidget()
window.show()
form = QFormLayout()
form.setLayout(window)
form.pushButton.clicked.connect(myCalc)
window.show()
app.exec()