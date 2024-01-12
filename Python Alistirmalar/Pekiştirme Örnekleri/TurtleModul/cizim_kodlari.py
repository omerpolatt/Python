import turtle

arka_plan = turtle.Screen()
arka_plan.bgcolor("#97ffff")
arka_plan.title("Turtle Modul")

kalem_1 = turtle.Turtle() #Kalem_1 adında nesnemizi oluşturduk çizimleri bu nesen üzerinden gerçekleştireceğiz
kalem_2 = turtle.Turtle()

#kalem_1.forward(100) # ileri doğru çizim yaparız
#kalem_1.backward(100) #geriye doğru çizim yaparız

#kalem_1.pensize(50) #çizgi boyutunu ayaralmamaızı sağlar
#kalem_1.circle(45) #çember çizdirir

#kalem_1.pencolor("red")#çizgi rengini ayarlar
#kalem_1.pencolor("red") #çizgi rengini ayarlar
"""
kalem_1.fillcolor("red") #çizilen şekillerin içini doldurmak rneklendirmek için kullandık 

kalem_1.begin_fill() # dolguyu başlatır

for i in range(4):
    kalem_1.forward(100)
    kalem_1.right(90)

kalem_1.end_fill() # dolguyu sonlandırır 
"""
#kalem_1.speed(2) #çizim hıznı ayarlarız
"""
kalem_1.color("blue")
for i in range(6):
    kalem_1.circle(30)
    kalem_1.left(60)

kalem_2.color("red")
for i in range(6):
    kalem_2.circle(30)
    kalem_2.left(90)

"""

turtle.done()
