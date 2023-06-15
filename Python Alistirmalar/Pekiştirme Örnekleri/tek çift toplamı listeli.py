while True:
    sayi = int(input("Lütfen Bir Sayı Giriniz :\n"))
    tek_sayilar = []
    cift_sayilar = []
    tek_toplam = 0
    cift_toplam = 0

    for i in range(1, sayi + 1):
        if i % 2 == 0:
            cift_sayilar.append(i)

        else:
            tek_sayilar.append(i)

    print("Aralığımızdaki Tek Sayılarımız {} ve Toplamları = {} ".format(tek_sayilar, sum(tek_sayilar)))
    print("Aralığımızdaki Çift Sayılarımız {} ve Toplamları = {} ".format(cift_sayilar, sum(cift_sayilar)))
