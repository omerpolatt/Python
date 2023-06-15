print("Programa Hoşgeldiniz ")
while True:

    print("Programdan Çıkmak İçin '0' tuşuna basınız")

    para = int(input("Para Miktarınızı Giriniz :"))

    if para == 0:
        print("Cıkış Yaptınız")
        break

    elif para > 0:
        ikiyuzluk = int(para / 200)
        yuzluk = int((para - (200 * ikiyuzluk)) / 100)
        ellilik = int((para - (200 * ikiyuzluk) - (yuzluk * 100)) / 50)
        yirmilik = int((para - (200 * ikiyuzluk) - (yuzluk * 100) - (ellilik * 50)) / 20)
        onluk = int((para - (200 * ikiyuzluk) - (yuzluk * 100) - (ellilik * 50) - (yirmilik * 20)) / 10)
        birlik = int((para - (200 * ikiyuzluk) - (yuzluk * 100) - (ellilik * 50) - (yirmilik * 20) - (onluk * 10)) / 1)

        toplam_banknot_sayisi = ikiyuzluk + yuzluk + ellilik + yirmilik + onluk + birlik
        print(
            "Paranızın Banknot Dağılımı = \n {} adet ikiyüzlük \n {} adet yüzlük \n {} adet ellilik \n {} adet "
            "yirmilik \n"
            "{} adet onluk \n {} adet birlik\n".format(ikiyuzluk, yuzluk, ellilik, yirmilik, onluk, birlik))
        print("Toplam Banknot Sayınız : {}".format(toplam_banknot_sayisi))
