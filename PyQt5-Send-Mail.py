import sys
import  sqlite3
from PyQt5 import  QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.creat_connect()
        self.init_ui()

    def creat_connect(self):
        connect = sqlite3.connect("database.db")

        self.cursor = connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler(kullanıcı_adı TEXT ,parola TEXT)")
        connect.commit()

    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş")
        self.kaydol = QtWidgets.QPushButton("Kaydol")
        self.yazi_alani =QtWidgets.QLabel("")
        self.user =QtWidgets.QLabel("User   :")
        self.password = QtWidgets.QLabel("Parola :")
        self.hatirlat = QtWidgets.QCheckBox("Hatırla")
        self.unuttum = QtWidgets.QPushButton("Şifremi unuttum")



        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.user)
        h_box1.addWidget(self.kullanici_adi)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.password)
        h_box2.addWidget(self.parola)
        #h_box2.addWidget(self.hatirlat)
        h_box2.addStretch()



        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.yazi_alani)
        h_box3.addStretch()

        h_box5 = QtWidgets.QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.hatirlat)
        h_box5.addWidget(self.unuttum)
        h_box5.addStretch()



        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.giris)
        h_box4.addWidget(self.kaydol)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)

        v_box.addLayout(h_box3)
        v_box.addLayout(h_box5)
        v_box.addStretch()
        v_box.addLayout(h_box4)


        self.user.setFixedSize(35,20)
        self.password.setFixedSize(35,20)
        self.kullanici_adi.setFixedSize(120,20)
        self.parola.setFixedSize(120,20)


        self.setLayout(v_box)

        self.giris.clicked.connect(self.login)
        self.kaydol.clicked.connect(self.kaydoll)
        self.unuttum.clicked.connect(self.yenile)





        self.setStyleSheet("background-color:lightblue;")
        self.setGeometry(400,100,300,300)
        self.setFixedSize(300,300)
        self.setWindowTitle("GİRİŞ SİSTEMİ")
        #self.giris.setStyleSheet("background-color: red")
        #self.yazi_alani.setStyleSheet("background-color: red")
        #self.kullanici_adi.setStyleSheet("background-color: red")
        self.show()

    def login(self):

        ad  = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("SELECT * FROM bilgiler WHERE kullanıcı_adı= ? and parola = ?",(ad,par))

        data = self.cursor.fetchall()

        if len(data)==0:
            self.yazi_alani.setText("Yanlış giriş")

        else:
            pencere2.show()
            self.yazi_alani.setText("hoş geldiniz")

    def kaydoll(self):

        pencere3.showMaximized()

    def yenile(self):
        pencere4.showMaximized()

class Pencere2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.gorsel()

    def gorsel(self):
        self.metin=QtWidgets.QLabel(self)
        self.metin.setText("HOŞ GELDİNİZ")
        self.metin.size()



        self.setWindowTitle("           GİRİŞ             ")
        self.setStyleSheet("background-color:lightblue")
        self.setFixedSize(300, 300)



class Pencere3(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.gorsel()
        self.connect()

    def connect(self):

        self.connec = sqlite3.connect("kayitlar.db")
        self.im =self.connec.cursor()

        self.im.execute("CREATE TABLE IF NOT EXISTS kayit(ad TEXT,soyad TEXT,sifre TEXT,email TEXT)")




    def gorsel(self):
        self.ad = QtWidgets.QLabel("    Ad :")
        self.soyad = QtWidgets.QLabel("Soyad :")
        self.adi = QtWidgets.QLineEdit()
        self.soyadi= QtWidgets.QLineEdit()
        self.email = QtWidgets.QLabel("  Email :")
        self.emaili =QtWidgets.QLineEdit()
        self.passwor =QtWidgets.QLabel("  Şifre :")
        self.passworu = QtWidgets.QLineEdit()
        self.kaydet = QtWidgets.QPushButton("Kaydet")

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.ad)
        h_box1.addWidget(self.adi)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.soyad)
        h_box2.addWidget(self.soyadi)
        h_box2.addStretch()

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.email)
        h_box3.addWidget(self.emaili)
        h_box3.addStretch()

        h_box5 = QtWidgets.QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.passwor)
        h_box5.addWidget(self.passworu)
        h_box5.addStretch()

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.kaydet)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box5)
        v_box.addLayout(h_box4)

        self.setLayout(v_box)


        self.ad.setFixedSize(35,20)
        self.adi.setFixedSize(120,20)
        self.soyad.setFixedSize(35,20)
        self.soyadi.setFixedSize(120,20)
        self.email.setFixedSize(35,20)
        self.emaili.setFixedSize(120,20)
        self.passwor.setFixedSize(35,20)
        self.passworu.setFixedSize(120,20)



        self.setWindowTitle("           KAYDOL 2             ")
        self.setStyleSheet("background-color:lightblue")


        self.kaydet.clicked.connect(self.account)

    def account(self):
        ad = self.adi.text()
        soyad = self.soyadi.text()
        email= self.emaili.text()
        sifre = self.passworu.text()

        self.im.execute("INSERT INTO kayit VALUES(?,?,?,?)",(ad,soyad,sifre,email))
        self.connec.commit()

class Pencere4(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.gorsel()

    def gorsel(self):
        self.email_lable = QtWidgets.QLabel("Email :")
        self.email_line =QtWidgets.QLineEdit()
        self.gonder = QtWidgets.QPushButton("Gönder")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.email_lable)
        h_box.addWidget(self.email_line)
        h_box.addStretch()

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box.addWidget(self.gonder)
        h_box1.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)
        v_box.addStretch()

        self.setLayout(v_box)
        self.setWindowTitle("ŞİFRE YENİLEME")
        self.setStyleSheet("background-color :lightblue")
        self.setFixedSize(250,100)

if __name__ == '__main__':
    uygulama = QtWidgets.QApplication(sys.argv)

    pencere = Pencere()
    pencere2 = Pencere2()
    pencere3 = Pencere3()
    pencere4 = Pencere4()
    sys.exit(uygulama.exec_())
