sayi = int(input("Bölenlerinin Toplamını Bulacağımız Sayıyı Giriniz :"))
bolen = []

for i in range(1,sayi):
    if sayi % i == 0 :
        bolen.append(i)

print(bolen)
print("Bölenlerin Toplamı : {}".format(sum(bolen))) #sum fonk liste tuple gibi değişkenlerden değer almaktadır



