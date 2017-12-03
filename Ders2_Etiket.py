import  sys
from  PyQt5 import  QtWidgets,QtGui



def Pencere():

    uygulama = QtWidgets.QApplication(sys.argv)

    pencere =QtWidgets.QWidget()

    pencere.setWindowTitle("PENCEREM")

    etiket1 =QtWidgets.QLabel(pencere)
    etiket1.setText("Etiket 1")
    etiket1.move(50,50)

    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("indir.jpg"))
    etiket2.move(200,200)


    pencere.setGeometry(200,100,500,500)
    pencere.show()

    sys.exit(uygulama.exec_())


Pencere()