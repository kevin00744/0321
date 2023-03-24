import turtle
import math
import time
turtle.setup(960, 540)
t1 = turtle.Turtle() 
t1.speed(0)
t1.ht()

def Goto(t, x ,y):
    t.pu()
    t.goto(x,y)
    t.pd()

def Home(t):
    t.pu()
    t.home()
    t.pd()

def HexagonPie(t, l):
    t.pencolor('black')
    t.pensize(1)
    for j in range(6):
        t.rt(60)
        for i in range(3):
            t.rt(120)
            t.fd(l)
    Home(t)

def RoundCircle(t, n, r):
    ang = 360/n
    for i in range(n):
        t.circle(r)
        t.lt(ang)
    Home(t)

def ThreeLeaf(t, l):
    move_x = -l * math.sqrt(3) / 2
    move_y = -l/2
    Goto(t, move_x, move_y)
    t.pencolor('green')
    t.pensize(5)
    t.lt(60)
    for i in range(3):
        t.circle(-l,120)
        t.rt(120)
    Home(t)

def TaiChi(t, r):
    t.pensize(10)
    t.pencolor('black')
    Goto(t, 0, r)
    t.fillcolor('black')
    t.begin_fill()
    t.circle(-r,180)
    t.circle(-(r/2),180 )
    t.circle((r/2),180)
    t.end_fill()
    t.circle(r,180)    
    Goto(t, 0 ,(-2* r/ 3))
    t.dot(50, 'white')
    Goto(t, 0, (2* r/3))
    t.dot(50, 'black')
    Home(t)

BODY_COLOR =  'red'
BODY_SHADOW = ''
GLASS_COLOR = '#9acedc'
GLASS_SHADOW = ''

def body(t):
    t.pensize(20)
    t.fillcolor(BODY_COLOR)
    t.begin_fill()
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)
    t.right(180)
    t.circle(100, -180)
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)
    t.circle(40, -180)
    t.left(7)
    t.backward(50)
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    t.right(240)
    t.circle(50, -70)
    t.end_fill()

def glass(t):
    t.up()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.down()
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()
    t.right(150)
    t.circle(90, -55)
    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)
    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()

def backpack(t):
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()

def amoung_us(t):
    body(t)
    glass(t)
    backpack(t)
    Home(t)

while True:
    HexagonPie(t1, 200)
    time.sleep(5)
    t1.clear()
    RoundCircle(t1, 24, 100)
    time.sleep(5)
    t1.clear()
    ThreeLeaf(t1, 200)
    time.sleep(5)
    t1.clear()
    TaiChi(t1,200)
    time.sleep(5)
    t1.clear()
    amoung_us(t1)
    time.sleep(5)
    t1.clear()


turtle.exitonclick()

# reference:
# 1. https://docs.python.org/zh-tw/3/library/turtle.html
# 2. https://stackoverflow.com/questions/60917905/turtle-graphics-how-do-i-implement-a-pause-function
# 3. https://docs.python.org/3/library/time.html