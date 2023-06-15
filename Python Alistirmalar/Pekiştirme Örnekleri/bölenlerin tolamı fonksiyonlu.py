def bolen(sayi):
    bolen=[]
    for i in range(1,sayi):
        if sayi % i == 0:
            bolen.append(i)
    print(bolen)
    return print(sum(bolen))


bolen(18)

