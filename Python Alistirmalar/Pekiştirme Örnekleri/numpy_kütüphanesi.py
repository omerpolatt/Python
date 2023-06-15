import numpy 

# dizilerin tipipini "dtype" komutu ile öğreniriz
#dizimiz = numpy.array([1,2,4])
#dizimiz = numpy.array(["ö","m"])
#print("Dizi türü : {}".format(dizimiz.dtype))



#normal dizi işlemleri ile bunu yapmazken numpy kullanrak 
#dört işlem gerçeklesştirebiliriz
#dizi1=numpy.array([1,2,3])
#dizi2=numpy.array([4,5,7])

#dizi3 = dizi1 / dizi2
#dizi3 = dizi1 - dizi2
#dizi3 = dizi1 + dizi2
#dizi3 = dizi1 * dizi2
#print(dizi3)



#dizi = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
#print(dizi)
#print(dizi.shape) #shape komutu satır ve sütün sayısını döndürür


#dizi = numpy.array(range(12)).reshape(4,3)
#print(dizi)

#dizi = numpy.random.randint(1,5,size=(2,2))
#print(dizi)

#dizi = numpy.arange(0,12,2).reshape(3,2)
#print(dizi)


#dizi = numpy.array([1,2,3,4,5,6,7,8,9,10])
#matris=dizi.reshape(5,2)
#print(matris)


#dizi = numpy.arange(0,10).reshape(5,2)+5
#print(dizi)
#print(dizi + 5)


#dizi = numpy.ones((3,4))*7



#dizi = numpy.eye(2)
#print(dizi)




#dizi = numpy.array([[1,2,3,4,0],[7,8,9,5,4]])
#print(dizi.max())
#print(dizi.min())


"""
dizi = numpy.arange(5,26)
cift_dizi =[]
for i in dizi:
    if i % 2== 0:
        cift_dizi.append(i)
       
print(cift_dizi)"""



"""
nokta çarpımı
dizi1 = numpy.array([4,9,7])
dizi2= numpy.array([8,1,0])


print(numpy.dot(dizi1,dizi2))"""

"""
dizi = numpy.array([4,9,7,19,375,0,6])

dizi[0:3]=[1,2,4]
print(dizi)"""


"""
dizi = numpy.linspace(0,10,6)
print(dizi)"""

"""
dizi = numpy.array([4,9,7,5,9,0,3,66,5,2,7,1,63,32,0])

print(numpy.array_split(dizi,3))"""

"""
dizi = numpy.array([4,8,7,21,11,6,3,96,7,0,5,5,4,2,5])

bul =numpy.where(dizi %4==0)

print(bul)
for i in bul:
    
    print(dizi[i])"""


"""dizi =numpy.array([[1,9,7],[4,0,17]])
print(dizi.T)"""

"""
dizi1 = numpy.array([4,9,7,4])
dizi2= numpy.array([8,1,0])
dizi3 = numpy.concatenate([dizi1,dizi2])
print(dizi3)"""


































