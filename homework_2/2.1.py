# -*- coding: utf-8 -*-
'''
创建一个People 类，People 的属性有name 和age，两个参数在实例化的时候传给构造器，People 类的方法有getName 和getAge，分别返回姓名和年龄。

程序输入（用一个空格分开）：姓名 年龄

程序输出：同输入
'''
ins = input().split(' ')
name, age = ins[0], int(ins[1])


class People:
    # 请在这里编写代码
    # 构造方法
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    # get方法
    def getName (self):
        return self.name

    def getAge (self):
        return self.age


p = People(name, age)
print(p.getName() + ' ' + str(p.getAge()))
