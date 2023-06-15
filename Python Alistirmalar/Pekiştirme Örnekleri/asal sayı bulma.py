while True:
    sayi = int(input("Lütfen Bir Değer Giriniz : \t"))

    if sayi < 0:
        print("Negatif Sayıların Asallığı Kontrol Edilmez Lütfen Pozitif Bir Sayı Giriniz !!")

    elif sayi == 0 or sayi == 1:
        print(" 0 ve 1 Değeri Asallığa Uymazlar Asal Değillerdir")
    elif sayi == 2:
        print("2 Değerinin Özel Durumu Vardır Ve Çift Asal Olan Tek Sayımzdır")

    else:
        for i in range(2,sayi+1):
            if sayi % i == 0:
                print("{} Sayımız Asal Değildir".format(sayi))

                break
            else:
                print("{} Sayımız Asaldır".format(sayi))
                break
