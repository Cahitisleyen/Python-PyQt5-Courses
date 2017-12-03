import  sys
from  PyQt5 import  QtWidgets



def Window():

    app = QtWidgets.QApplication(sys.argv)

    wimdow =QtWidgets.QWidget()
    button = QtWidgets.QPushButton()
    button.setText("Press Me")


    window.setWindowTitle("My Window")
    window.setFixedSize(300,500)
    
    window.setStyleSheet("background-color:green;")
    window.show()

    sys.exit(app.exec_())


Window()
