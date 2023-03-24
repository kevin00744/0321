import turtle
import math
import time
t1 = turtle.Turtle()
# t1.speed(0)
# t1.pencolor("red")
def square1():
    for i in range(4):
        # t1.fd(100)
        t1.lt(90)
        t1.fd(100)
def p1():
    for j in range(24):
        square1()
        t1.lt(15)
# p1()
# square1()
def square2(t=t1, l=100):
    for i in range(4):
        t.fd(l)
        t.lt(90)
# square2(t1)
def Polygon(t=t1, n=4 ,l=100):
    # n, l = int(input("please enter the side number and length(Please use \',\' to separate\nIf doesn\'t enter any number would use default side number = 4, length = 100\n>)")).split(',')
    angle = ((n-2) * 180)/n
    for i in range(n):
        t.fd(l)
        t.lt(angle)
# Polygon(t1,6,100)
# t1. circle(100)
# t1.circle(-100)
# t1.lt(90)
# t1.circle(-50,180)
#  t1.circle(50,180)
# t1.pensize(10)
# t1.pencolor('yellow')
# for i in range(4):
#     t1.circle(50,180)
#     t1.rt(90)

# def ccirrcle(t=t1 ,r):
# t1.pu()
# t1.goto(-300,0)
# t1.pd()

# t1.lt(90)
# for i in range (3):
#     t1.circle(-50,180)
#     t1.circle(50,180)
def Goto(t, x ,y):
    t.pu()
    t.goto(x,y)
    t.pd()

# Goto(t1, -300, 0)

# t1.pensize(10)
# Goto(t1,100,0)
# for i in range(361):
#     x = 100 * math.cos(math.radians(i))
#     y = 100 * math.sin(math.radians(i))
#     t1.pencolor((x+100)/200, (y+100)/200,0)
#     t1.goto(x,y)
def HexagonPie(t, l):
    for j in range(6):
        t1.rt(60)
        for i in range(3):
            t1.rt(120)
            t1.fd(l)
# HexagonPie(t1,100)
def RoundCircle(t, n, r):
    ang = 360/n
    for i in range(n+1):
        t1.circle(r)
        t1.lt(ang)
# RoundCircle(t1, 24, 50)
def ThreeLeaf(t, l):
    Goto(t1, -l/2, -l/2)
    t1.pencolor('green')
    t1.pensize(5)
    t1.lt(60)
    for i in range(3):
        t1.circle(-l,120)
        t1.rt(120)
# ThreeLeaf(t1, 200)
def TaiChi(t, r):
    Goto(t1, 0, r)
    t1.fillcolor('black')
    t1.begin_fill()
    t1.circle(-r,180)
    t1.circle(-(r/2),180 )
    t1.circle((r/2),180)
    t1.end_fill()
    t1.circle(r,180)    
    Goto(t1, 0 ,(-r/3))
    t1.dot(50, 'white')
    Goto(t1, 0, (r/3))
    t1.dot(50, 'black')



ThreeLeaf(t1, 200)
TaiChi(t1,200)






turtle.exitonclick()
