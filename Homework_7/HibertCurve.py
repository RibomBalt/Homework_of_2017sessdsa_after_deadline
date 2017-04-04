# -*- encoding:utf-8 -*-
from turtle import *


def hibertCurve4Turtle (n: int, turtle: Turtle, length: int) -> None:
    '''
    使某个turtle运行n阶希尔伯特曲线。下图为2阶。
    
    ┌─┐ ┌─┐
    │ └─┘ │
    └─┐ ┌─┘
    ┌─┘ └─┐
    
    从左下到右下运行
    :param length: 每段小长度
    :param turtle: 海龟
    :param n: 希尔伯特曲线阶数。应当为一个正数
    :return: 
    '''
    # 保证阶数为非负
    assert n >= 0
    if n == 0:
        # 零阶曲线是一个点，旋转180度后即可返回
        turtle.left(180)
        return None
    else:
        # 任意阶曲线都是左下进入，右下离开，初始方向都是上下的
        # 按照文档中给出的顺序，进行递归操作
        turtle.right(90)
        reversed_hibertCurve4Turtle(n - 1, turtle, length)
        # 完成第一阶
        turtle.right(90)
        turtle.fd(length)
        hibertCurve4Turtle(n - 1, turtle, length)
        # 完成第二阶
        turtle.left(90)
        turtle.fd(length)
        turtle.left(90)
        hibertCurve4Turtle(n - 1, turtle, length)
        # 完成第三阶
        turtle.fd(length)
        turtle.right(90)
        reversed_hibertCurve4Turtle(n - 1, turtle, length)
        turtle.right(90)


def reversed_hibertCurve4Turtle (n: int, turtle: Turtle, length: int) -> None:
    """
        使某个turtle运行n阶希尔伯特曲线。下图为2阶。

        ┌─┐ ┌─┐
        │ └─┘ │
        └─┐ ┌─┘
        ┌─┘ └─┐

        从左下到右下运行
        :param length: 每段小长度
        :param turtle: 海龟
        :param n: 希尔伯特曲线阶数。应当为一个正数
        :return: 
    """
    # 保证阶数为非负
    assert n >= 0
    if n == 0:
        # 零阶曲线是一个点，旋转180度后即可返回
        turtle.right(180)
        return None
    else:
        # 任意阶曲线都是右下进入，左下离开，初始方向都是上下的
        # 按照文档中给出的顺序，进行递归操作
        turtle.left(90)
        hibertCurve4Turtle(n - 1, turtle, length)
        # 完成第一阶
        turtle.left(90)
        turtle.fd(length)
        reversed_hibertCurve4Turtle(n - 1, turtle, length)
        # 完成第二阶
        turtle.right(90)
        turtle.fd(length)
        turtle.right(90)
        reversed_hibertCurve4Turtle(n - 1, turtle, length)
        # 完成第三阶
        turtle.fd(length)
        turtle.left(90)
        hibertCurve4Turtle(n - 1, turtle, length)
        turtle.left(90)
        return None


if __name__ == '__main__':
    # 建立turtle和Screen
    t = Turtle()
    s = Screen()
    # 设定参数
    color = '#00FF00'
    n = 7
    length = 4
    # turtle初始化
    t.up()
    t.goto(-250, -250)
    t.down()

    t.seth(90)
    t.speed(10)
    t.color(color)
    # 暴走乌龟，测试用
    # t._tracer(0)
    # t._update()

    # 绘制
    hibertCurve4Turtle(n, t, length)
    s.exitonclick()
