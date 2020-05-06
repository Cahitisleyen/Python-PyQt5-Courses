import  sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.gui()

    def gui(self):
        self.sehirler = ['Adana', 'Adıyaman', 'Afyon', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin',
                    'Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale',
                    'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir',
                    'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'İstanbul', 'İzmir',
                    'Kars', 'Kastamonu', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya',
                    'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya',
                    'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak',
                    'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak',
                    'Bartın', 'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce']

        self.oyuncular=["Abdullah Pabur","Abdürrahim Karakoç","Abdurrahman Kızılay","Abdurrahman Önül","Abidin","Acil Servis","Alişan"]
        self.hayvanlar=["Köpek","Kedi","At","Balık","Tavşan","Tavuk","Aslan","Yılan","Keçi","Kuş"]
        self.esyalar=["Masa","Sandalye","Dolap","Koltuk","Buzdolabı","Televizyon","Bilgisayar","Telefon"]

        #Birinci oyuncu-----------------------------------------------------------------------------------------------------
        self.harf_label =QtWidgets.QLabel("<h2>Harf Girin </h2>")
        self.harf_edit= QtWidgets.QLineEdit()
        self.oyuncu_label1 =  QtWidgets.QLabel("<h1>Birinci Oyuncu </h1>")


        self.sehir1_label = QtWidgets.QLabel("Şehir")
        self.sehir1_edit = QtWidgets.QLineEdit()

        self.hayvan1_label = QtWidgets.QLabel("Hayvan")
        self.hayvan1_edit = QtWidgets.QLineEdit()

        self.oyuncu1_label = QtWidgets.QLabel("Oyuncu")
        self.oyuncu1_edit = QtWidgets.QLineEdit()

        self.esya1_label = QtWidgets.QLabel("Eşya")
        self.esya1_edit = QtWidgets.QLineEdit()

        #ikinci oyuncu --------------------------------------------------------------------------------------------------
        self.oyuncu_label2 = QtWidgets.QLabel("<h1>İkinci Oyuncu </h1>")
        self.oyuncu_edit2 = QtWidgets.QLineEdit()

        self.sehir2_label = QtWidgets.QLabel("Şehir")
        self.sehir2_edit = QtWidgets.QLineEdit()

        self.hayvan2_label = QtWidgets.QLabel("Hayvan")
        self.hayvan2_edit = QtWidgets.QLineEdit()

        self.oyuncu2_label = QtWidgets.QLabel("Oyuncu")
        self.oyuncu2_edit = QtWidgets.QLineEdit()

        self.esya2_label = QtWidgets.QLabel("Eşya")
        self.esya2_edit = QtWidgets.QLineEdit()

        self.hesapla = QtWidgets.QPushButton("Hesapla")
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.sonuc1_label = QtWidgets.QLabel("<h3>Birinci Oyuncu Puanı</h3>")
        self.sonuc1_edit =QtWidgets.QLineEdit()
        self.sonuc2_label=QtWidgets.QLabel("<h3>İkinci Oyuncu Puanı</h3>")
        self.sonuc2_edit =QtWidgets.QLineEdit()

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.oyuncu_label1)

     #birinci oyuncu Labels ------------------------------------------------------------------------
        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.sehir1_label)
        h_box2.addWidget(self.oyuncu1_label)
        h_box2.addWidget(self.hayvan1_label)
        h_box2.addWidget(self.esya1_label)

        h_box5=QtWidgets.QHBoxLayout()
        h_box5.addWidget(self.sehir1_edit)
        h_box5.addWidget(self.oyuncu1_edit)
        h_box5.addWidget(self.hayvan1_edit)
        h_box5.addWidget(self.esya1_edit)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.oyuncu_label2)

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addWidget(self.sehir2_label)
        h_box4.addWidget(self.oyuncu2_label)
        h_box4.addWidget(self.hayvan2_label)
        h_box4.addWidget(self.esya2_label)


        h_box6 = QtWidgets.QHBoxLayout()
        h_box6.addWidget(self.sehir2_edit)
        h_box6.addWidget(self.oyuncu2_edit)
        h_box6.addWidget(self.hayvan2_edit)
        h_box6.addWidget(self.esya2_edit)








        v_box1 =QtWidgets.QVBoxLayout()
        v_box1.addWidget(self.harf_label)
        v_box1.addWidget(self.harf_edit)
        v_box1.addLayout(h_box1)
        v_box1.addLayout(h_box2)
        v_box1.addLayout(h_box5)
        v_box1.addLayout(h_box3)
        v_box1.addLayout(h_box4)
        v_box1.addLayout(h_box6)
        v_box1.addStretch()
        v_box1.addWidget(self.hesapla)
        v_box1.addWidget(self.temizle)
        v_box1.addWidget(self.sonuc1_label)
        v_box1.addWidget(self.sonuc1_edit)
        v_box1.addWidget(self.sonuc2_label)
        v_box1.addWidget(self.sonuc2_edit)
        self.setLayout(v_box1)

        self.setFixedSize(450,600)
        self.setStyleSheet("background-color:lightblue")
        self.hesapla.clicked.connect(self.hesaplama)
        self.temizle.clicked.connect(self.temizleme)
        self.show()
    def temizleme(self):
        self.sehir1_edit.clear()
        self.sehir2_edit.clear()
        self.oyuncu2_edit.clear()
        self.oyuncu2_edit.clear()
        self.hayvan1_edit.clear()
        self.hayvan2_edit.clear()
        self.esya1_edit.clear()
        self.esya2_edit.clear()
        self.sonuc1_edit.clear()
        self.esya2_edit.clear()
        self.harf_edit.clear()
    def hesaplama(self):
        sehir1=self.sehir1_edit.text()
        sehir2=self.sehir2_edit.text()
        oyuncu1=self.oyuncu1_edit.text()
        oyuncu2=self.oyuncu2_edit.text()
        hayvan1=self.hayvan1_edit.text()
        hayvan2=self.hayvan2_edit.text()
        esya1=self.sehir1_edit.text()
        esya2=self.esya2_edit.text()
        harf=self.harf_edit.text()
        sonuc1 = 0
        sonuc2 = 0

        if sehir1 in self.sehirler:
            if sehir1.startswith(harf):
                if sehir1 != sehir2:
                    sonuc1 += 10
                else:
                    sonuc1 += 5
            else:
                sonuc1+=0
        else:
            sonuc1+=0

        if sehir2 in self.sehirler:
            if sehir2.startswith(harf):
                if sehir2 != sehir1:
                    sonuc2 += 10
                else:
                    sonuc2 += 5
            else:
                sonuc2 += 0
        else:
            sonuc2 += 0

        if oyuncu1 in self.oyuncular:
            if oyuncu1.startswith(harf):
                if oyuncu1 != oyuncu2:
                    sonuc1 += 10
                else:
                    sonuc1 += 5
            else:
                sonuc1 += 0
        else:
            sonuc1 += 0

        if oyuncu2 in self.oyuncular:
            if oyuncu1.startswith(harf):
                if oyuncu2 != oyuncu1:
                    sonuc2 += 10
                else:
                    sonuc2 += 5
            else:
                sonuc2 += 0
        else:
            sonuc2 += 0

        if hayvan1 in self.hayvanlar:
            if hayvan1.startswith(harf):
                if hayvan1 != hayvan2:
                    sonuc1 += 10
                else:
                    sonuc1 += 5
            else:
                sonuc1 += 0
        else:
            sonuc1 += 0

        if hayvan2 in self.sehirler:
            if hayvan2.startswith(harf):
                if hayvan2 != hayvan1:
                    sonuc2 += 10
                else:
                    sonuc2 += 5
            else:
                sonuc2 += 0
        else:
            sonuc2 += 0

        if esya1 in self.esyalar:
            if esya1.startswith(harf):
                if esya1 != esya2:
                    sonuc1 += 10
                else:
                    sonuc1 += 5
            else:
                sonuc1 += 0
        else:
            sonuc1 += 0

        if esya2 in self.esyalar:
            if esya2.startswith(harf):
                if esya2 != esya1:
                    sonuc2 += 10

                else:
                    sonuc2 += 5
            else:
                sonuc2 += 0
        else:
            sonuc2 += 0

        self.sonuc1_edit.setText(str(sonuc1))
        self.sonuc2_edit.setText(str(sonuc2))

if __name__=="__main__":

    uygulama = QtWidgets.QApplication(sys.argv)
    pencere =Pencere()
    sys.exit(uygulama.exec_())
