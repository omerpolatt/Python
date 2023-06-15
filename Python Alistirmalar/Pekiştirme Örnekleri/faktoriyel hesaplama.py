while True :
    sayi = int(input("Faktoriyeli Hesaplanacak Sayıyı Giriniz : \n"))
    faktoriyel = 1
    if sayi > 0:
        for i in range(1, sayi + 1):
            faktoriyel = faktoriyel * i
        print(faktoriyel)

    elif sayi == 0 or sayi == 1 :
        faktoriyel = 1
        print(faktoriyel)
    else:
        print("Faktoriyel Hesaplanmaz")







