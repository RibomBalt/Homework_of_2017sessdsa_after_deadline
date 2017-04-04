import random
import turtle

x = 0


def curvemoveleft (t, a, m, n):
    for i in range(a):
        t.left(m)
        t.forward(n)


def curvemoveright (t, a, m, n):
    for i in range(a):
        t.right(m)
        t.forward(n)


def drawLeave (t):
    t.color('yellow')
    t.begin_fill()
    t.fillcolor('yellow')
    t.left(100)
    t.forward(5)
    curvemoveleft(t, 8, 1.5, 0.95)
    curvemoveleft(t, 100, 0.5, 0.1)
    curvemoveright(t, 20, 5, 0.1)
    curvemoveright(t, 50, 2, 0.15)
    curvemoveleft(t, 20, 5, 0.1)
    curvemoveright(t, 40, 3.5, 0.15)
    curvemoveright(t, 10, 1, 0.4)
    t.left(160)
    curvemoveright(t, 10, 1, 0.4)
    curvemoveright(t, 40, 3.5, 0.15)
    curvemoveleft(t, 20, 5, 0.1)
    curvemoveright(t, 50, 2, 0.15)
    curvemoveright(t, 20, 5, 0.1)
    curvemoveleft(t, 100, 0.5, 0.1)
    curvemoveleft(t, 8, 1.5, 0.95)
    t.forward(5)
    t.end_fill()
    global x
    print(x)
    x += 1


def tree (branchlen, t, i):
    if branchlen > 5:
        m = random.randrange(10, 30)
        n = random.randrange(10, 30)
        s = random.randrange(branchlen - 15, branchlen - 10)
        t.pensize(i)
        t.forward(branchlen)
        t.right(m)
        tree(s, t, i - 2)
        t.left(2 * n)
        tree(s, t, i - 2)
        t.right(2 * n - m)
        t.backward(branchlen)
    else:
        drawLeave(t)


littleTurtle = turtle.Turtle()
littleTurtle.speed(1000)
w = turtle.Screen()
littleTurtle.pensize(20)
littleTurtle.left(90)
littleTurtle.up()
littleTurtle.backward(100)
littleTurtle.down()
littleTurtle.color('brown')
tree(100, littleTurtle, 15)
w.exitonclick()
