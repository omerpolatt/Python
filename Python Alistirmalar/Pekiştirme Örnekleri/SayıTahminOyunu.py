import random
import time

print("""
**********************
OYUNUMUZA HOŞ GELDİNİZ
**********************""")

rastgele_sayi = random.randint(1, 50)  # randit fonksiyonu ile sayı ürettik
tahmin_hakki = 10

while True:
    tahmin = int(input("...Lütfen Tahmininizi Yazınız : \n"))

    if tahmin < rastgele_sayi:
        time.sleep(1)  # sleep fonksiyonu ile programı uyutmuş olduk
        print("Tahmininiz Yanlış ")
        print("Lütfen Daha Büyük Bir Değer Giriniz")
        tahmin_hakki -= 1

    elif tahmin > rastgele_sayi:
        time.sleep(1)
        print("Tahmininiz Yanlış ")
        print("Lütfen Daha Küçük Bir Değer Giriniz")
        tahmin_hakki -= 1
    else:
        time.sleep(1)
        print("Tahmininiz Doğrudur")
        print("Tebrikler")
        print("Sayımız {} ve {}. Hakkınızda Buldunuz".format(rastgele_sayi, tahmin_hakki))
        break

    if tahmin_hakki == 0:
        print("Maalesef Tahmin Hakkınız Sonlandı")
        print("Sayımız {} idi ".format(rastgele_sayi))
