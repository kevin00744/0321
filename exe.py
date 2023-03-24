import turtle
t1 = turtle.Turtle()
# t1.pencolor('red')

# for j in range(24):
#     t1.lt(15)
#     for i in range(4):
#         t1.fd(200)
#         t1.lt(90)
from main.py import Goto
t1.pensize(10)
Goto(t1,100,0)
for i in range(361):
    x = 100 * math.cos(math.radians(i))
    y = 100 * math.sin(math.radians(i))
    t1.pencolor((x+100)/200, (y+100)/200,0)
    t1.goto(x,y)

turtle.exitonclick()
