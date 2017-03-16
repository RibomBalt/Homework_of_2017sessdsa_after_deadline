# -*- encoding: utf-8 -*-
'''
创建一个函数，接受一个字符串和一个正整数n作为参数，
返回把原字符串字符位置向右移动n个字符的字符串，
例如接受的参数是"abcd"和1，返回的字符串是"dabc"；
接受的参数是"mnbol"和2，返回的字符串是"olmnb"。
(注意：n有可能大于字符串长度)
'''
s = input()
n = int(input())


def reverse(s, n):
    # 请开始你的表演
    # 将过大的n转换成小于长度的n
    n %= len(str(s))
    # 将字符串拆成列表，并延长一倍
    charlist = list(s) * 2
    # 对延长后的字符串进行切片
    res = charlist[len(str(s)) - n : 2 * len(str(s)) - n]
    # 使用字符串的join方法来转换为字符串
    return ''.join(res)


print(reverse(s, n))
