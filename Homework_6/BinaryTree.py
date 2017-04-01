# -*- encoding:utf-8 -*-
'''
友情提示：整个过程纯属随机，有可能出现一开始直接判定随机结束！
'''
import random
from turtle import *

# 随机取色器，转换为十六进制#xxxxxx形式，前两个固定为黑色和棕色
colors = ['black', 'brown'] + list(map(lambda n: '#' + hex(n)[2:].zfill(6), random.sample(range(0x1000000), 100)))


def generateSuite (turtle, length, leftAngle, rightAngle, width, color):
    '''
    生成递归随机参数
    :param turtle: 绘制的海龟
    :param length: 绘制长度
    :param leftAngle: 左转角度
    :param rightAngle: 右转角度
    :param width: 宽度
    :param color: 颜色
    :return: 
    '''
    # 减小长度，用随机整数
    length -= random.randrange(10) * 1.5
    # 微调角度，用高斯函数
    leftAngle += random.gauss(mu=0, sigma=0.25) * 2
    rightAngle += random.gauss(mu=0, sigma=0.25) * 2
    # 减小宽度，用随机整数：
    width -= random.randrange(2) * 3
    # 改变颜色：使用随机取色器的下一个颜色
    color = colors[colors.index(color) + 1]
    return (turtle, length, leftAngle, rightAngle, width, color)


def drawTree (turtle, length, leftAngle, rightAngle, width, color):
    '''
    绘制分形树的主要函数。
    :param turtle: 绘制的海龟
    :param length: 绘制长度
    :param leftAngle: 左转角度
    :param rightAngle: 右转角度
    :param width: 宽度
    :param color: 颜色
    :return: 
    '''
    try:
        # 递归结束条件
        if length <= 25 or width <= 0:
            raise AssertionError
        # 随机结束！模拟可能被折断的情况！1/15概率
        if random.randrange(15) == 1:
            return
        # 调整turtle的参数，并绘制第一条线
        turtle.pensize(width)
        turtle.color(color)
        turtle.fd(length)
        # 获取turtle此时刻位置与角度信息
        pos = turtle.position()
        head = turtle.heading()
        # 进行左端递归
        turtle.left(leftAngle)
        drawTree(*generateSuite(turtle, length, leftAngle, rightAngle, width, color))
        # 还原
        turtle.seth(head)
        turtle.up()
        turtle.goto(pos)
        turtle.down()
        # 右端递归
        turtle.right(rightAngle)
        drawTree(*generateSuite(turtle, length, leftAngle, rightAngle, width, color))
        # 还原
        turtle.seth(head)
        turtle.up()
        turtle.goto(pos)
        turtle.down()
    except AssertionError:
        # 1/15概率得到一个星星
        if random.randrange(15) == 0:
            turtle.color('#FFFF00')
            turtle.stamp()


def icon_star (r, name):
    '''
    这是一个不重要的函数，嗯.
    它的功能是把turtle的图标换成一个星星
    :r: 最小半径
    :name: 名字
    :return: name
    '''
    import math
    import turtle
    def rs2xy (r, s):
        '''
        内部函数，用来把一个极坐标换成直角坐标，方便生成星星
        :param r: 半径
        :param s: 角度（degree)
        :return: 元组，(x,y)
        '''
        return (r * math.cos(s / 180 * math.pi), r * math.sin(s / 180 * math.pi))

    # 生成各个点的坐标。
    # 最长半径
    R = r * 2 * math.cos(0.1 * math.pi)
    # 得到五角星的生成器
    generate_star = (rs2xy(R if i % 2 == 0 else r, 36 * i) for i in range(10))
    # 注册
    turtle.register_shape(name, tuple(generate_star))

    return name


def main ():
    print('这是Cobalt制作的星星树！如有必要请最大化观看。')
    print('为了避免出现随机不可控情况，请多打开几次本树！')
    screen = Screen()
    aturtle = Turtle()
    # 调整初始方位，图标
    aturtle.seth(90)
    aturtle.up()
    aturtle.goto((0, -300))
    aturtle.down()
    # 设定图标，背景……
    bgpic('SMG-goodbgpic.png')
    icon_star(10, 'star')
    aturtle.shape('star')
    initial = (
        aturtle,
        75,
        25,
        25,
        4 * 3,
        colors[0]
    )
    drawTree(*initial)
    print('树的遍历结束了！请即刻截图，点击屏幕结束')
    screen.exitonclick()


if __name__ == '__main__':
    main()
