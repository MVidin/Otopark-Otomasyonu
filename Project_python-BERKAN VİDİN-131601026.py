# !/usr/bin/env python
# -*- coding: cp1254 -*-
  
from msilib import Dialog
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time, locale

parkyerleri=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10',  #Park Yerleri Listesi
        'B1','B2','B3','B4','B5','B6','B7','B8','B9','B10',
        'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10',
        'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10']
dolu_parkyerleri=[] # Dolu olan katlar�n at�laca�� liste
print('kat:',parkyerleri)


# ---------- Bu alanda de�i�iklik yapmay�n�z --------
class Otopark_Otomasyonu(QDialog):



    def ekle(self):
        f = open("Araclar.txt","a") # Ara�lar adl� yeni bir dosya a��yor.
        if(float(self.yuksekligi.text()) <=2.4):   #Y�ksekli�i 2.4 metreden k���k ise a�a��daki i�lemleri yapacak


            self.gSaati.setText(time.strftime("%H:%M")) #Giri� saati k�sm�na zaman� yazar.
            str(self.yeri.setText(parkyerleri[0])) # Park Yerleri adl� listenin ilk eleman�n� programda �al��an yeri k�sm�na yaz�yor
            a = parkyerleri[0] #Park yerlerininin ilk eleman�n� a de�i�kenine at�yor.
            dolu_parkyerleri.append(a) # Dolu park yerleri k�sm�na park yerlerinin ilk eleman�n� ekler.
            parkyerleri.remove(a) #park yerlerinden a de�i�kenine at�lan eleman� ��kar�yor.
            print ("dolu yerler=",dolu_parkyerleri) # Ekrana Dolu Park yerlerini yazd�r�r.
            print ("Katlar=",parkyerleri)# Park yerlerini ekrana yazd�r�r.
            f.write("arac yeri:"+self.yeri.text()+"\n"+
                    "giris saati:"+str(self.gSaati.text())+"\n"+    # Burada yukar�da a��lan dosyaya bilgileri yazar.
                    "yuksekligi:"+self.yuksekligi.text()+"\n"+
                    "plakasi:"+self.plakasi.text()+"\n\n")
            f.close()
        else:
            self.yuksekligi.setText("Y�KSEKL��� 2.4 TEN B�Y�K ARA� G�REMEZ!!!")# Ara� y�ksekli�i 2.4 metreden y�ksek ise y�ksekli�i                                                                                     k�sm�na t�rnak i�indeki k�sm� yazar.



    def cikar(self):
            self.cSaati.setText(time.strftime('%H:%M')) # ��k�s saatini programdaki ��k�� saati yerine yazar.
            a=self.gSaati.text() # giri� Saatini a de�i�kenine atar.
            b=self.cSaati.text() #��k�� saatini b de�i�kenine atar.
            [sa,dk]=a.split(':') # Burada a de�i�kenindeki saati split ile noktal� virg�l� ay�rarak sa ve dk ye atar.
            [sa2,dk2]=b.split(':')
            girisdk=int(sa) * 60 + int(dk) #Giri� saatini dakikaya �eviren i�lem
            cikisdk=int(sa2) * 60 + int(dk2) #��k�� saatini dakikaya �eviren i�lem
            print(float(girisdk))
            print(float(cikisdk))


            topDak=int(cikisdk-girisdk) # Burada dakikaya �evirilen ��k�s saati ile giri� saati aras�ndaki fark� alarak topDak de�i�kenine                                        atar
            print(topDak)
            fiyat=0


            if(float(self.yuksekligi.text())<1.9):   #Yukar�daki saati al�p �eviri yapma k�sm�n� Baki arkada��mdan yard�m alarak                                                               yapt�m.Soraki if bloklar�n� kendim yapt�m.
                if(0<=topDak<60):
                    fiyat=10
                    print(fiyat)
                    self.ucreti.setText("10TL")
                elif(60<=topDak<180):
                    fiyat=15
                    print(fiyat)
                    self.ucreti.setText("15TL")
                elif(180<=topDak<360):
                    fiyat=24
                    print(fiyat)
                    self.ucreti.setText("24TL")
                elif(360<=topDak<720):
                    fiyat=30
                    print(fiyat)
                    self.ucreti.setText("30TL")
                elif(720<=topDak<1440):
                    fiyat=40
                    print(fiyat)
                    self.ucreti.setText("40TL")
            else:
                yfiyat=fiyat + (fiyat*0.2)# Y�ksekli�i 1.9 metreden y�ksek ara�lar� iin ek �cretlendirme k�sm�.Fakat buradaki Kod �cret                                                                             k�sm�na �creti yazd�rm�yor
                self.ucreti.setText(str(yfiyat))








    def __init__(self, parent=None):
        
        super(Otopark_Otomasyonu, self).__init__(parent)

# -------- Formun istenen de�erleri burada tan�mlan�yor ---------- 
        self.plaka = QLabel('Plaka')
        self.yukseklik = QLabel('Y�kseklik')
        self.yer = QLabel('Yer')
        self.gSaat = QLabel('Giri� Saati')
        self.cSaat = QLabel('��k�� Saati')
        self.ucret = QLabel('�creti')

# -------- Formun istenen de�erleri tan�mlama buraya kadar ---------
# 1) .......

# ------- Formda kullan�c�dan al�nan de�erler ---------
        self.plakasi = QLineEdit()
        self.yuksekligi = QLineEdit()
        self.yeri = QLineEdit()
        self.gSaati = QLineEdit()
        self.cSaati = QLineEdit()
        self.ucreti = QLineEdit()

        
        self.kaydet = QPushButton('Kaydet')
        self.cikis = QPushButton('��k��')

        self.connect(self.kaydet, SIGNAL('pressed()'), self.ekle)    # Kaydet butonuna t�kland��u anda ekle isimli bir fonksiyon �a�r�l�r.
        self.connect(self.cikis, SIGNAL('pressed()'), self.cikar)
# ---------- Yukar�daki kodu de�i�tirmeyiniz. Ancak ekleme yapabilirsiniz. -------- 
        izgara = QGridLayout()
        izgara.addWidget(self.plaka, 0, 0,)
        izgara.addWidget(self.yukseklik, 1, 0,)
        izgara.addWidget(self.yer, 3, 0,)
        izgara.addWidget(self.gSaat, 4, 0,)
        izgara.addWidget(self.cSaat, 6, 0,)
        izgara.addWidget(self.ucret, 7, 0,)

        izgara.addWidget(self.plakasi, 0, 1,)
        izgara.addWidget(self.yuksekligi, 1, 1,)
        izgara.addWidget(self.yeri, 3, 1,)
        izgara.addWidget(self.gSaati, 4, 1,)
        izgara.addWidget(self.cSaati, 6, 1,)
        izgara.addWidget(self.ucreti, 7, 1,)

        izgara.addWidget(self.kaydet, 2, 1,)
        izgara.addWidget(self.cikis, 5, 1,)
 
        self.setLayout(izgara)
        self.setWindowTitle('Otopark Otomasyonu, Ara� Giri� Formu')
        
   
    
        
 
uygulama = QApplication([])
pencere = Otopark_Otomasyonu()
pencere.show()
uygulama.exec_()
