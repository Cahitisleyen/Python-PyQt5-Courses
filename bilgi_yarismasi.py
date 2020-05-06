import  sys
from PyQt5 import QtWidgets,QtGui,QtCore
import random
from PyQt5.QtGui import QImage
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.gui()

    def gui(self):
        self.sorular = [["İnsanların grup içi davranışlarının bilimsel çakışmalarını yapan, toplumsal güçleri inceleyen bilim dalı aşağıdakilerden hangisidir?",
            "A) Sosyoloji", "B) Psikoloji", "C) İnsan bilimi)", "D) Antropoloji", "A"],

            ["Aşağıdakilerden hangisi sosyal bilim değildir?",
             "A) Tarih", "B) Biyoloji", "C) Psikoloji", "D) Sosyoloji", "B"],
            ["Sosyolojizm ekolü il ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
             "A)   Bu ekolün Türkiye’deki temsilcisi Ziya Gökalp’tir.",
             "B) Toplumu mutlaklaştıran bir görüştür.",
             "C)   Toplumu birey karşısında etkisiz bir konuma taşır.",
             "D)   Pozitivist ve determinist bir anlayışa.", "C"],

            ["Sosyolojinin teknoloji, gelir dağılımı ve tüketim ile iş bölümünü gibi konularla ilgilenen bölüme ne ad verilir?",
                "A)    Hukuk Sosyolojisi", "B)    Bilgi Sosyolojisi", "C)    Sanayi Sosyolojisi",
                "D)    Ekonomi Sosyolojisi", "D"],

            ["Aşağıdakilerden hangisi bir bilimsel araştırma ilkesi değildir?",
             "A)   Hipotez oluşturma", "B)    Basitlik ve açıklık", "C)  Sınırlılık", "D)   Nesnellik", "A"],

            ["Aşağıdakilerden hangisi bilimsel yöntemin aşamalarından biri değildir?",
             "A)   Sorunu ortaya koymak", "B) Bilgi toplamak", "C)   Tekrar", "D)   Hipotez oluşturma",
             "C"],

            ["Sosyoloji aşağıdakilerden hangisine yanıt aramaz?",
             "A)   İnsanlar neden bir aile kurmuşlardır.", "B)    İnsanlar neden tanrıya inanırlarf.",
             "C)   Niçin bazı insanlar fakirdir.", "D)    Toplumu bir arada tutan kurallar nelerdir.", "D"],

            ["Aşağıdakilerden hangisi sosyolojinin ortaya çıkışını hazırlayan etkenlerden değildir?",
             "A)   Endüstri Devrimi", "B) Fransız ve Amerikan İhtilalleri", "C)  Emperyalist gelişmeler",
             "D)   1. Ve 2. Dünya Savaşları", "D"],

            ["1950’lerde sosyolojik görüşleri ve özellikle yöntem anlayışı ile öne çıkan sosyolog aşağıdakilerden hangisidir?",
                "A)    Ziya Gökalp", "B)  İbrahim Yasa", "C) Cahit Tanyol", "D) Prens Sabahattin", "D"],

            ["Mehmet İzzet’e göre; sosyolojinin ilk amacı aşağıdakilerden hangisidir?",
             "A)   Grup ilişkilerini düzenlemek", "B) Cemiyetleri tasnif etmek",
             "C)   Toplumsal değişimin aşamalarını göstermek", "D)    Toplum-devlet ilişkilerini açıklamak",
             "B"],

            ["Batıcılık İslamcılık ve ulusçuluk görüşlerini sentezleyen ilk sosyolog aşağıdakilerden hangisidir?",
                "A.     Niyazi Berkes", "B.    Hilmi Ziya Ülken", "C.    Prens Sabahattin", "D. Ziya Gökalp",
                "D"],

            ["Aşağıdakilerden hangisi Hilmi Ziya Ülken’in eseri değildir?",
             "A.    Ask Ahlakı", "B.  Aşkı Memnu", "C.   İnsani Vatanperverlik", "D.    Şeytanla Konuşmalar",
             "B"],

            ["Hilmi Ziya Ülken e göre Türkiye’de sosyolojinin ortaya çıkmasındaki dönüm noktası aşağıdakilerden hangisidir?",
                "A.    Tanzimat Fermanı", "B. Fransız Devrimi", "C.  1. Dünya Savaşı",
                "D.    2. Dünya Savaşı", "A"],

            ["Ziya Gökalp’in Cumhuriyet’in kuruluş sürecinde yeni kurulacak devletin ilkelerini anlattığı ve bu nedenle Batılılaşmanın da yolunu açtığı eserinin adı nedir?",
                "A.    Medeni Bilgiler", "B.  Türkçülüğün Esasları",
                "C.    Türkleşmek, İslamlaşmak, Muasırlaşmak",
                "D.    Türkiye Nasıl Kurtarılabilir?", "B"],

        ["Hilmi Ziya Ülken, Anadolucu dünya görüşünü geliştirirken Ziya Gökalp’in Türkçülük fikrini hangi yönüyle eleştirmiştir?",
            "A)    Savaşları engelleyememesi", "B)    Devletin yıkılmasına yol açması",
            "C)    Toplumun geri kalmasına sebep olması", "D) Dünya şartlarında gerçekçi olmaması", "D"],

        ["Aşağıdakilerden hangisi İkinci Meşrutiyet döneminin düşünce ortamında Türkiye’de sosyolojinin kuruluşuna büyük katkı sağlamış isimlerden biridir?",
            "A)    Beşir Fuad", "B)   Said Halim Paşa", "C)  Prens Sabahattin", "D) Ali Suavi", "C"],

        ["1950’lere kadar devlet kurumlarında, liselerde ve kısmen üniversitelerde etkin olan sosyoloji anlayışı; A. Comte, E. Durkheim tarafından geliştirilen sosyolojizm ekolü aşağıdaki isimlerden hangisi tarafından  benimsenip temsil edilmiştir?",
            "A.    Ziya Gökalp", "B.  Prens Sabahattin", "C. Mümtaz Turhan", "D.    Hilmi Ziya Ülken", "A"],

        ["Toplumu gerek maddi gerek manevi olarak bizi kuşatan işler, filler, hareketler, inançlar ve değerler sistemi olarak tanımlayan sosyolog aşağıdakilerden hangisidir?",
            "A)    Hilmi Ziya Ülken", "B) Mehmet İzzet", "C) Ziyaeddin Fahri Fındıkoğlu", "D)   Ziya Gökalp",
            "A"],

        ["Mehmet İzzet’in çalışmalarında kendisine dayanarak aldığı sosyolog aşağıdakilerden hangisidir?",
         "A)   Spencer", "B)  Engels", "C)   Saint Simon", "D)  Durkheim", "D"],

        ["Aşağıdakilerden hangisi Ziya Gökalp in en bilinen kitaplarından biridir?",
         "A.    Bu Ülke", "B.     Türkiye Nasıl Kurtarılabilir?", "C.      Türkçülüğün Esasları",
         "D.      Üç Tarzı Siyaset", "C"],

        ["Hilmi Ziya Ülken’in geliştirdiği düşünce akımı aşağıdakilerden hangisidir?",
         "A.   Türkçülük", "B.    Ümmetçilik", "C.   Batıcılık", "D.    Anadoluculuk ", "D"],

        ["Prens Sabahattin’in Türkiye’de görüşlerini temsil ettiği sosyolog aşağıdakilerden hangisidir?",
         "A)   A. Comte", "B) E. Durkheim", "C)  H. Spencer", "D)   Le Play", "D"],

        ["Hilmi Ziya Ülken’in öğrencilik yıllarında Reşat Kayl ile birlikte el yazması olarak çıkarttığı dergi aşağıdakilerden hangisidir?",
            "A)    Türk Yurdu", "B)   Anadolu", "C)  Genç Kalemler", "D)    Hareket", "B"],

        ["Hilmi Ziya Ülken’in sosyolojide birbirini tamamlayıcı olarak kullanılabileceğini düşündüğü yöntemler aşağıdakilerden hangisinde birlikte ve doğru verilmiştir?",
            "A)    Sosyal monografi-tarama-katılımlı gözlem", "B) Sözlü tarih-içerik analiz-deney",
            "C)    Saha araştırması-tarama-gözlem", "D)   İstatistik yöntem-sosyal monografi-tarihi yöntem", "D"],

        ["Aşağıdakilerden hangisi Mehmet İzzet’in ilgilendiği sorunlardan biri değildir?",
         "A)   Cemiyet ve fert", "B)  Milliyet", "C) Muasır cemiyet ", "D)  Çatışma", "D"],

        ["Aşağıdakilerden hangisi Prens Sabahattin’in eğitim anlayışı ile çelişmektedir?",
         "A)   Eğitim alanında reformlar yapmak", "B) Kızların daha iyi eğitim almalarını sağlamak ",
         "C)   Uygulamalı eğitime önem vermek", "D)   Eğitimde ezberciliğe bir yöntem olarak yer vermek", "D"],

        ["Sosyolojide Anadoluculuk akımının öncüsü olan sosyolog aşağıdakilerden hangisidir?",
         "A.   Ziya Gökalp", "B.  Prens Sabahattin", "C. Hilmi Ziya Ülken", "D. İbrahim Yasa", "C"],

        ["Ziya Gökalp in çocukluk ve gençlik yıllarında görüşlerinin şekillenmesinde etkili olan isimlerden biri değildir ?",
            "A)Tevfik Bey", "B)Hasip Bey", "C) Abdullah Bey", "D)Naim Bey", "C"],

        ["Tabiat bilimleri ile insan bilimlerini birbirinden tamamen ayırmak yerine aralarında uzlaşma sağlanmasını gereğini öne süren sosyolog aşağıdakilerden hangisidir?",
            "A)    Hilmi Ziya Ülken", "B) Ziya Gökalp", "C)  Prens Sabahattin", "D) Mübecel Kıray", "A"],

        ["Aşağıdakilerden hangisi Mehmet İzzet’in toplumların evrimi sorusunda, genetik metodundan yararlandığı Amerikan idealistlerinden biridir?",
            "A)    Beck", "B) Baldwin", "C)  Marx", "D) Weber", "B"],

        ["Aşağıdakilerden hangisi Prens Sabahattin’in sosyolojide izleyenlerden biri değidir?",
         "A)   Nezahat Nurettin Tanyol", "B)  İbrahim Yasa ", "C)    Cahit Tanyol", "D) Cahit Orhan Tutangil",
         "A"],

        ["Hilmi Ziya Ülken'in doğum ve ölüm tarihi aşağıdakilerden hangisidir?",
         "A)   1897-1978", "B)    1900-1985", "C)    1901-1974", " D)   1903-1986","C"],

        [" Ziya Gökalp sosyolojisinde ırkların, cinslerin, kastların, sınıfların, milletlerin eşitliğini hangi ilke ile açıklar?",
             "A) Sosyalizm", "B)   Kapitalizm", " C)  Halkçılık", " D)   Devletçilik ", "C"],

         ["Ziya Gökalp’in çocukluk ve gençlik yıllarında görüşlerinin şekillenmesinde etkili olan isimlerden biri değildir?",
             "A.   Tevfik Bey", "B.   Hasip Bey", "C.    Abdullah Bey", "D.   Naim Bey", "C"],

         ["Mehmet İzzet’e göre aşağıdaki düşünürlerden hangisi siyasete gereğinden fazla zaman ayırdığı için daha fazla toplumsal eserler bırakamamıştır?",
             "A)   Prens Sabahattin", " B)    Mehmet Emin", " C) Salih Zeki", "D)   Ziya Gökalp", "D"],

         ["Hilmi Ziya Ülken’e göre sosyolojide sosyal ilişki kavramının dayandığı temel kavram aşağıdakilerden hangisidir?",
             "A)   Din-ahlak", "B)    İş-organizasyon", "C)  İş-eğitim", "D)    Hukuk-ahlak", "B"],

         ["Prens Sabahattin’in en önemli eseri aşağıdakilerden hangisidir?",
          "A)  Türkçülüğün Esasları", "B) Türkleşmek", "C)   Türkiye Nasıl Kurtulabilir?", "D)  İslamlaşmak",
          "C"],

         ["1914 yılında sosyolojinin İstanbul Üniversitesi'nde bir kürsüye kavuşup ve kurumsallaşmasında etkili olan isim aşağıdakilerden hangisidir?",
             "A.   Ziya Gökalp", "B.    Prens Sabahattin", "C.    Nurettin Topçu", "D.    Hilmi ziya ülken", "A"],

        ["Hilmi Ziya Ülken’in bilimsel kaygı açısından izlediği sosyolog aşağıdakilerden hangisidir?",
              "A)   Ziya Gökalp", "B)  Saint Simon", "C)  Karl Marx", "D)    Max Weber", "A"],

        ["Mehmet İzzet’in milliyet kuramı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
              "A)  Milliyet duygusu ırk, toprak ve insan ile açıklanabilir.",
              "B)  Milliyet, toplumsal hürriyeti sağlayacak bir idealdir.", "C)   Milliyet bir ülküdür.",
              "D)  Milliyet veri olmaktan çok yapıdır.", "A"],

        ["Prens Sabahattin’in toplumsal sorunların çözümünü gördüğü yöntem aşağıdakilerden hangisidir?",
              "A)  Saha araştırması", "B) Gözlem", "C)   Vaka analizi", "D) Mülakat", "B"],



        ["Ziya Gökalp Türkiye’de hangi sosyoloji ekolünün temsilciliğini yapmıştır?",
              "A.  Science Sociale", "B.  Sosyolojizm Ekolü", "C.    Biyoloji", "D. Marksist", "B"],

        ["Aşağıdakilerden hangisi Mehmet İzzet’ in ilgilendiği sorunlardan biri değildir?",
              "A.  Cemiyet ve fert", "B.  Milliyet ", "C.    Sınıf", "D.    Muasır cemiyet", "C"],


        ["Prens Sabahattin’in sosyoloji çizgisi uzun süren bir kesintiden sonra Türkiye’de yeniden canlanmasının nedeni değildir?"
            "A.    Türkiye’de çok partili döneme geçmesi", "B.    Türkiye’ye yapılan Marshall yardımı",
            "C.    Türkiye’nin Amerikan yanlısı siyasete bağlanması",
            "D.    Marksist akımın ülkenin düşünce gündeminde önemli bir yer işgal etmeye başlaması", "D"],

        ["50.  Aşağıdakilerden hangisi Hilmi Ziya Ülken’in bilim sınıflaması içerisinde yer almaz?",
         "A.   Hayat İlmi", "B.   İnsan İlmi", "C.   Kozmik Tabiat İlmi", "D.   Bitki İlmi", "D"]

        ]

        #Birinci oyuncu-----------------------------------------------------------------------------------------------------

        self.rast = random.choice(self.sorular)
        self.harf_label = QtWidgets.QLabel(str(self.rast[0]))
        self.hesapla = QtWidgets.QRadioButton(str(self.rast[1]))
        self.hesapla1 = QtWidgets.QRadioButton(str(self.rast[2]))
        self.hesapla2 = QtWidgets.QRadioButton(str(self.rast[3]))
        self.hesapla3 = QtWidgets.QRadioButton(str(self.rast[4]))
        self.sonuc = QtWidgets.QPushButton("Yanıt")
        self.sonraki = QtWidgets.QPushButton("Sonraki")
        self.dogruS = QtWidgets.QLabel()
        self.yanlisS = QtWidgets.QLabel()
        self.sayac = QtWidgets.QLabel("1.")
        self.cevap = QtWidgets.QPushButton("Yarışma Sonucu")
        self.sonuc1_edit = QtWidgets.QLabel()
        self.sonuc2_edit = QtWidgets.QLineEdit()
        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.sayac)
        h_box1.addWidget(self.harf_label)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.hesapla)
        h_box2.addWidget(self.hesapla1)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.hesapla2)
        h_box3.addWidget(self.hesapla3)

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addWidget(self.sonraki)
        h_box4.addWidget(self.sonuc)

        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addLayout(h_box1)
        v_box2.addStretch()
        v_box2.addLayout(h_box2)
        v_box2.addLayout(h_box3)
        v_box2.addLayout(h_box4)
        v_box2.addWidget(self.sonuc1_edit)

        v_box2.addWidget(self.cevap)
        v_box2.addWidget(self.dogruS)
        v_box2.addWidget(self.yanlisS)

        v_box2.addStretch()

        self.harf_label.setFont(QtGui.QFont(str(self.rast[0]),13,QtGui.QFont.Bold))
        self.hesapla.setFont(QtGui.QFont(str(self.rast[0]), 12, QtGui.QFont.Bold))
        self.hesapla1.setFont(QtGui.QFont(str(self.rast[0]), 12, QtGui.QFont.Bold))
        self.hesapla2.setFont(QtGui.QFont(str(self.rast[0]), 12, QtGui.QFont.Bold))
        self.hesapla3.setFont(QtGui.QFont(str(self.rast[0]), 12, QtGui.QFont.Bold))
        self.sonuc.setFont(QtGui.QFont(str(self.sonuc), 15, QtGui.QFont.Bold))
        self.sonraki.setFont(QtGui.QFont(str(self.sonraki), 15, QtGui.QFont.Bold))
        self.cevap.setFont(QtGui.QFont(str(self.cevap), 15, QtGui.QFont.Bold))
        self.sayac.setFont(QtGui.QFont(str(self.sayac), 13, QtGui.QFont.Bold))
        self.dogruS.setFont(QtGui.QFont(str(self.rast[0]), 13, QtGui.QFont.Bold))
        self.yanlisS.setFont(QtGui.QFont(str(self.rast[0]), 13, QtGui.QFont.Bold))



        self.setLayout(v_box2)
        self.showMaximized()


        self.sonraki.setStyleSheet("background-color: lightgreen")
        self.sonuc.setStyleSheet("background-color: lightgreen")
        self.setWindowTitle("Kim Milyoner Olmak İster")
        label = QLabel(self)
        pixmap = QPixmap('indir.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())






        self.sonuc.clicked.connect(self.sonuclar)
        self.sonraki.clicked.connect(self.hesaplar)
        self.cevap.clicked.connect(self.cevaplar)
        self.show()
        self.sayaci =1
        self.dogru = 0
        self.yanlis = 0
        self.show()

    def hesaplar(self):

        self.rast = random.choice(self.sorular)
        self.harf_label.setText(self.rast[0])
        self.hesapla.setText(self.rast[1])
        self.hesapla1.setText(self.rast[2])
        self.hesapla2.setText(self.rast[3])
        self.hesapla3.setText(self.rast[4])
        self.sayaci +=1
        self.sayac.setText(str(self.sayaci)+str("."))
        if self.sayaci ==21:
            time.sleep(5)
            exit()



    def sonuclar(self):
        if self.hesapla.isChecked():
            if str(self.hesapla.text())[0] == self.rast[5]:
                self.sonuc1_edit.setText("""<h2 style="color:green;">Doğru</h2>""")
                self.dogru +=1
            else:
                self.sonuc1_edit.setText("""<h2 style="color:red;">Yanlış</h2>""")
                self.yanlis +=1

        elif self.hesapla1.isChecked():
            if str(self.hesapla1.text())[0] == self.rast[5]:
                self.sonuc1_edit.setText("""<h2 style="color:green;">Doğru</h2>""")
                self.dogru += 1
            else:
                self.sonuc1_edit.setText("""<h2 style="color:red;">Yanlış</h2>""")
                self.yanlis += 1

        elif self.hesapla2.isChecked():
            if str(self.hesapla2.text())[0] == self.rast[5]:
                self.sonuc1_edit.setText("""<h2 style="color:green;">Doğru</h2>""")
                self.dogru += 1
            else:
                self.sonuc1_edit.setText("""<h2 style="color:red;">Yanlış</h2>""")
                self.yanlis += 1

        elif self.hesapla2.isChecked():
            if str(self.hesapla2.text())[0] == self.rast[5]:
                self.sonuc1_edit.setText("""<h2 style="color:green;">Doğru</h2>""")
                self.dogru += 1
            else:
                self.sonuc1_edit.setText("""<h2 style="color:red;">Yanlış</h2>""")
                self.yanlis += 1

        elif self.hesapla3.isChecked():
            if str(self.hesapla3.text())[0] == self.rast[5]:
                self.sonuc1_edit.setText("""<h2 style="color:green;">Doğru</h2>""")
                self.dogru += 1
            else:
                self.sonuc1_edit.setText("""<h2 style="color:red;">Yanlış</h2>""")
                self.yanlis += 1




    def cevaplar(self):
        self.dogruS.setText(str("Doğru Sayısı :")+str(self.dogru))
        self.yanlisS.setText(str("Yanlış Sayısı :") + str(self.yanlis))
        if self.sayaci ==21:
            time.sleep(5)
            exit()




if __name__=="__main__":

    uygulama = QtWidgets.QApplication(sys.argv)
    pencere =Pencere()

    sys.exit(uygulama.exec_())
