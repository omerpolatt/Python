import time
import random

class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 1 ,kanal_listesi ="TRT",kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("Televizyon Açık Haldedir")

        else:
            print("Televizyon Açılıyor")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı Durumda")

        else:
            print("Televizyon kapanıyor")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):
        print("Ses Ayaarı İle Oynamaktasınız")

        while True:
            cevap = input("sesi Azalt : '<' \n Sesi Artır : '>'\n SEÇİMİNİZ: ")

            if (cevap ==  "<"):
                print("Ses azaltılıyor..")
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("SES:",self.tv_ses)

            elif (cevap == ">"):
                print("Ses artırılıyor")
                self.tv_ses += 1
                print("SES:",self.tv_ses)

            else:
                print("ses güncellendi",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi+(kanal_ismi)
        print("Kanal eklendi")
        print("KANAL LİSTESİ",kanal_listesi)

    def ratgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]

        print("Şu an ki kanal ",self.kanal)

    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):
        return "TV DURUMU : {} \n TV SES :{}\n ŞU ANKİ KANAL :{}\n".format(self.tv_durum,self.tv_ses,self.kanal)

kumanda = Kumanda() ## kumanda objesi oluşturmuş olduk burada aşağıdaki komutları çağırmak için..

print("""

********** TV UYGULAMASI **********

1. TV AÇ
2. TV KAPAT
3. SES AYARLARI
4. KANAL EKLE
5. KANAL SAYSINI ÖĞRENME
6. RASGELE KANAL GEÇME
7. TV BİLGİLERİ

ÇIKMAK İÇİN 'q' yada 'Q' BASINIZ...

********** TV UYGULAMASI **********
""")

while True:
    islem =input("YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ:")

    if (islem == "q" or islem == "Q"):
        print("Program Sonlanıyor..")
        break

    elif (islem == "1"):
        kumanda.tv_ac()

    elif (islem == "2"):
        kumanda.tv_kapat()

    elif (islem== "3"):
        kumanda.ses_ayarları()

    elif ( islem == "4"):
        kanal_isimleri  = input("KANAL İSİMLERİNİ ',' KOYARAK GİRİNİZ:\n")
        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif (islem=="5"):
        print("KANAL SAYISI:",len(kumanda))

    elif (islem == "6"):
        kumanda.ratgele_kanal()

    elif (islem == "7"):
        print(kumanda)

    else:
        print("GEÇERSİZ İŞLEM")




