# -*- encoding: utf-8 -*-
'''
创建一个函数，接受一个正整数n作为参数，返回s=1!+2!+3!+……+n!的值。

def factorialSum(n)
'''
n = int(input())
def factorailSum(n):
    s = 0
    # 请在这里编写代码
    factor = 1  # 0的阶乘
    for i in range(1, n + 1):  # 循环从1到n，两端包含
        factor *= i
        s += factor
    return s
print(factorailSum(n))
