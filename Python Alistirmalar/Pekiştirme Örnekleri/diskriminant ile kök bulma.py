a = int(input("2.Derece Denklemin Baş Katsayısını Yazınız  : "))
b = int(input("2.Derece Denklemde X in Katsayısını Yazınız  : "))
c = int(input("Denklemin Sabit Sayısını Yazınız : "))

d_hesap = b ** 2 - 4 * a * c

if d_hesap > 0:
    kok_1 = ((-b + d_hesap ** 0.5) / 2 * a)
    kok_2 = ((-b - d_hesap ** 0.5) / 2 * a)
    print("Denklemi {}x²+({}x)+({}) olan Denkelmin Diskrimantı {} dir \n".format(a, b, c, d_hesap))
    print("Kökleri {} ve {} dir".format(kok_1, kok_2))

elif d_hesap == 0:
    kok1 = -b / 2 * a
    print("Denklemi {}x²+({}x)+({}) olan Denkelmin Diskrimantı {} dir \n".format(a, b, c, d_hesap))
    print("Denklemin 2 Eşit Kökü Vardır Kökü {} ".format(kok1))

else:
    print("Denklemi {}x²+({}x)+({}) olan Denkelmin Diskrimantı {} dir \n".format(a, b, c, d_hesap))
    print("Denklemin Gerçek Kökü Yoktur")
