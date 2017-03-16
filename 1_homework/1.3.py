# -*- encoding: utf-8 -*-
"""
创建一个函数，接受两个参数y和m，分别表示年和月，返回此年此月的天数。
（如大月有31天，小月有30天，而闰年的2月有29天，平年则只有28天，
年份如果能被4整除但不能被100整除或者能被400整除为闰年）

def getDays(y,m)

"""
import sys

y, m = map(int, sys.stdin.readline().split())


def getDays(y, m):
    n = 0
    # 请在这里编写代码
    # 嵌套定义函数isLeapYear：被4整除且不被100整除，或者被400整除返回True
    def isLeapYear(n):
        return ((n % 4 == 0) & (n % 100 != 0)) | (n % 400 == 0)
    # 平年各月的天数，下标0-11
    dayInMonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # 闰年2月比平年2月多一天，通过三元表达式实现
    n += 1 if isLeapYear(y) & (m == 2) else 0
    # 调用平年天数，与闰年的修正相加，m: 1-12
    n += dayInMonth[m - 1]
    return n


print(getDays(y, m))
