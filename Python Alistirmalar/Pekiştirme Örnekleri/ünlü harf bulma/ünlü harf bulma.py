#dosyanızdaki sesli harfleri bulmaya yarayan programımız
dosya = input("Dosya Adınızı Giriniz : ")
sesli_harfler = "aeıioöuüAEIİOÖUÜ"
sayac = 0

with open(dosya, "r+", encoding="utf-8") as o_dosya:
    icerik = o_dosya.read()
    print(icerik)

    for i in icerik:

        if i in sesli_harfler:
            sayac += 1

print(sayac)
