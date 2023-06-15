import random

print("TAŞ KAĞIT MAKAS OYUNUA HOŞGELDİNİZ ")


kazanma_sayisi = 0
while True:
    tercih = input("TAŞ KAĞIT MAKAS Hangisini Yaptınız : \t")

    oyun = ["Taş", "Kağıt", "Makas"]
    secim = random.choice(oyun)

    if kazanma_sayisi == 3:
        print("OYUN BİTMİŞTİR ")
        break

    elif kazanma_sayisi < 3:

        if tercih == "Taş":
            if secim == "Taş":
                print("{} --- {} BERABERE SAYI YOK ".format(tercih, secim))
                print("Kazandığınız Oyun Sayısı : {}".format(kazanma_sayisi))

            elif secim == "Kağıt":
                print("{} --- {} KAĞIT KAZANDI ".format(tercih, secim))
                print("Kazandığınız Oyun Sayısı : {}".format(kazanma_sayisi))

            elif secim == "Makas":
                print("{} --- {} TAŞ KAZANDI".format(tercih, secim))
                kazanma_sayisi += 1
                print("Kazandığınız Oyun Sayısı : {}".format(kazanma_sayisi))

        elif tercih == "Kağıt":
            if secim == "Kağıt":
                print("{} --- {} BERABERE SAYI YOK ".format(tercih, secim))
                print("Kazandığınız Oyun Sayısı : {}".format(kazanma_sayisi))

            elif secim == "Taş":
                print("{} --- {} KAĞIT KAZANDI".format(tercih, secim))
                kazanma_sayisi += 1
                print("Kazandığınız Oyun Sayısı : {}".format(kazanma_sayisi))

            elif secim == "Makas":
                print("{} --- {} MAKAS KAZANDI ".format(tercih, secim))
                print("Kazandığınız Oyun Sayısı : {}".format(kazanma_sayisi))

        elif tercih == "Makas":
            if secim == "Kağıt":
                print("{} --- {} MAKAS KAZANDI ".format(tercih, secim))
                kazanma_sayisi += 1
                print("Kazandığınız Oyun Sayısı : {}".format(kazanma_sayisi))

            elif secim == "Makas":
                print("{} --- {} BERABERE SAYI YOK ".format(tercih, secim))
                print("Kazandığınız Oyun Sayısı : {}".format(kazanma_sayisi))

            elif secim == "Taş":
                print("{} --- {} TAŞ KAZANDI".format(tercih, secim))
                print("Kazandığınız Oyun Sayısı : {}".format(kazanma_sayisi))
