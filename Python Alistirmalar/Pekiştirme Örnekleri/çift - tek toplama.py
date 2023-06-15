while True:
    sayi = int(input("Bir Sayı Giriniz:"))
    tekToplam = 0
    ciftToplam = 0
    for i in range(1, sayi + 1):
        if i % 2 == 0:
            ciftToplam += i


        elif i % 2 != 0:
            tekToplam += i

    print(tekToplam)
    print(ciftToplam)
