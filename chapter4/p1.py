import turtle
import math

print(math.pi)
turtle.getscreen()._root.attributes('-topmost', 1)

bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def poligon(t, length, n, n1):
    angle = 360 / n
    for i in range(n1):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    n = 100
    l = 2* math.pi * r / n
    poligon(t, l, n)

def arc(t, r, angle):
    # number of circle precision
    n = 100
    # number to draw based on angle
    n1 = n * angle / 360
    # length of circumference
    l = 2 * math.pi * r / n
    poligon(t, l, n, int(n1))


arc(bob, 100, 180)

turtle.mainloop()
