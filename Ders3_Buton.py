import  sys
from  PyQt5 import  QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.pencere()

    def pencere(self):


        self.setWindowTitle("PENCEREM")

        self.buton = QtWidgets.QPushButton("fuıjkhjmf")
        self.buton.setText("Giriş")
        self.buton.move(160, 50)
        self.setGeometry(500, 100, 400, 400)

        self.show()


uygulama = QtWidgets.QApplication(sys.argv)
pen = Pencere()
sys.exit(uygulama.exec_())

