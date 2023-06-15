import turtle, random
import winsound  # sesler için

pencere = turtle.Screen()  # Pencere oluşturduk
pencere.bgcolor("black")  # pencere arka plan rengi
pencere.title("UZAY SAVAŞ OYUNU")  # pencere Başlık adı
pencere.bgpic("uzay.gif")  # pencere arka plan resimi
pencere.setup(width=600, height=600)  # pencere boyutlarını ayarladık

# oyunda kullancağımız nesnelerinresimlerini kullanabilmek için tanıttık
turtle.register_shape("ates.gif")
turtle.register_shape("dusman.gif")
turtle.register_shape("oyuncu.gif")

# oyuncu nesnesini oluşturduk
oyuncu = turtle.Turtle()
oyuncu.color("blue")
oyuncu.speed(0)
oyuncu.shape("oyuncu.gif")
oyuncu.setheading(90)  # oyun dik şekilde oynanacağı için geçerli olan ayar
oyuncu.penup()
oyuncu.goto(0, -250)
oyuncu_hizi = 20

# ateş nesnesini oluşturduk
ates = turtle.Turtle()
ates.color("red")
ates.speed(0)
ates.shape("ates.gif")
ates.setheading(90)  # oyun dik şekilde oynanacağı için geçerli olan ayar
ates.penup()
oyuncu.goto(0, -240)
ates_hizi = 20
ates.hideturtle()
ates.turtlesize(1, 1)
ateskontrol = False

yaz = turtle.Turtle()
yaz.color("White")
yaz.speed(0)
yaz.penup()
yaz.goto(0, 200)
yaz.hideturtle()


def atesgit():
    y = ates.ycor()
    y = y + ates_hizi
    ates.sety(y)


def sola_git():
    x = oyuncu.xcor()
    x = x - oyuncu_hizi
    if x < -300:
        x = -300
    oyuncu.setx(x)


def saga_git():
    x = oyuncu.xcor()
    x = x + oyuncu_hizi
    if x > +300:
        x = +300
    oyuncu.setx(x)


def yukari_git():
    y = oyuncu.ycor()
    y = y + oyuncu_hizi
    if y > 270:
        y = +270
    oyuncu.sety(y)


def asagi_git():
    y = oyuncu.ycor()
    y = y - oyuncu_hizi
    if y < -270:
        y = -270
    oyuncu.sety(y)


def ateset():
    global ateskontrol

    winsound.PlaySound("lazer.wav", winsound.SND_ASYNC)  # ateş edildiğinde çıkacxak se ayarlandı

    x = oyuncu.xcor()
    y = oyuncu.ycor() + 20
    ates.goto(x, y)
    ates.showturtle()
    ateskontrol = True


hedefler = []
for i in range(1, 7):
    hedefler.append(turtle.Turtle())

for hedef in hedefler:
    hedef.color("red")
    hedef.speed(0)
    hedef.turtlesize(1, 1)
    hedef.shape("dusman.gif")
    hedef.penup()
    hedef.setheading(90)
    x = random.randint(-280, 280)
    y = random.randint(180, 260)
    hedef.goto(x, y)

# tuş atamaları burada yapıldı
pencere.listen()
pencere.onkey(sola_git, "Left")
pencere.onkey(saga_git, "Right")
pencere.onkey(yukari_git, "Up")
pencere.onkey(asagi_git, "Down")
pencere.onkey(ateset, "space")

while True:
    if ateskontrol:
        atesgit()

    for hedef in hedefler:
        y = hedef.ycor()
        y = y - 2
        hedef.sety(y)

        if hedef.distance(ates) < 20:
            ates.hideturtle()
            hedef.hideturtle()
            hedefler.pop(hedefler.index(hedef))
            winsound.PlaySound("patlama.wav", winsound.SND_ASYNC)

        if hedef.ycor() < -270 or hedef.distance(oyuncu) < 20:
            yaz.write("KAYBETTİNİZ", align="center", font=("Courior", 24, "bold"))

    if len(hedefler) == 0:
        yaz.write("TEBRİKLER KAZANDINIZ", align="center", font=("Courior", 24, "bold"))
