import  sys
from  PyQt5 import  QtWidgets



def Pencere():

    uygulama = QtWidgets.QApplication(sys.argv)

    okey = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    h_box= QtWidgets.QHBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okey)
    h_box.addWidget(cancel)


    v_box =QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)


    pencere =QtWidgets.QWidget()

    pencere.setWindowTitle("PENCEREM")
    pencere.setLayout(v_box)
    jpg = QIcon("indir.jpg")
    pencere.setWindowIcon(jpg)
    pencere.setGeometry(200,100,500,500)
    pencere.show()

    sys.exit(uygulama.exec_())


Pencere()