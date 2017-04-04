from turtle import *

screen = Screen()
# 新建turtle对象实例
aTurtle = Turtle()


def goUp ():
    aTurtle.setheading(90)
    aTurtle.fd(1)
    return True


def f ():
    # | ...
    aTurtle.fd(100)
    # | ...
    aTurtle.lt(60)
    # | ...


# screen.onkeypress(f, "Up")
# screen.listen()

f()
f()
print('f-finished')

# screen.onkeypress(goUp, 'Up')

# time.sleep(100)

# screen.listen()
