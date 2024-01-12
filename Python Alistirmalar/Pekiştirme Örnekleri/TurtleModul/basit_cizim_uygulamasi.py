import turtle

arka_plan = turtle.Screen()
arka_plan.title("ÇİZİM OYUNU")
arka_plan.bgcolor("#97ffff")

kalem = turtle.Turtle()
kalem.pensize(5)


def sag():
    kalem.forward(50)


def sol():
    kalem.backward(50)


def yon_1():
    kalem.right(30)


def yon_2():
    kalem.left(15)


def temizle():
    arka_plan.clear()
    arka_plan.bgcolor("#97ffff")


arka_plan.listen()

arka_plan.onkey(sag, key="Right")
arka_plan.onkey(sol, key="Left")
arka_plan.onkey(yon_1, key="Up")
arka_plan.onkey(yon_2, key="Down")
arka_plan.onkey(temizle, key="c")

arka_plan.mainloop()