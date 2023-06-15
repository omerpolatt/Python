
def not_hesapla(satir):

    satir = satir[:-1] # okuma işleminde \n den ve kendi okuduğu için 2 boşluk durumunu engellemek için yaptık

    liste = satir.split(",")

    isim = liste[0]
    not_1 = int(liste[1])
    not_2 = int(liste[2])
    not_3 = int(liste[3])

    son_not = (not_1 * 3/10) + (not_2 * 3/10) + (not_3 * 4/10)

    if(son_not >= 90):
        harf = "AA"

    elif( 90> son_not >= 80):
        harf = "BA"

    elif (80> son_not >= 70):
        harf = "BB"

    elif (70> son_not >= 60):
        harf = "CB"

    elif( 60>son_not >=50):
        harf = "CC"

    elif (50 > son_not ):
        harf = "FF"




    return "{} Adlı Öğrencinin Notu {} ve Harf Karşılığı {} \n".format(isim,son_not,harf)





with open("notlar.txt","r",encoding="utf-8") as file:

    eklenecekler_listesi = []

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("harf_notları.txt","w",encoding="utf-8") as file_2:
        for i in eklenecekler_listesi:
            file_2.write(i)



