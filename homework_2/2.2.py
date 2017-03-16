# -*- coding: utf-8 -*-
'''
创建一个Student 类，Student 类继承上一题中的People 类，并且增加了属性sno（表示学号），sno 表示学号，和增加了方法getSno。

程序输入（用一个空格分开）：姓名 年龄 学号

程序输出：同输入
'''
ins = input().split(' ')
name, age, sno = ins[0], ins[1], ins[2]


class People:
    # 在此编写自己代码
    # 构造方法
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    # get方法
    def getName (self):
        return self.name

    def getAge (self):
        return self.age


class Student(People):
    # 在此编写自己代码
    # 子类构造方法，注意父类构造方法调用，需要传入类名+self
    def __init__ (self, name, age, sno):
        super(Student, self).__init__(name, age)
        self.sno = sno

    # get方法
    def getSno (self):
        return self.sno


s = Student(name, age, sno)
print(s.getName() + ' ' + s.getAge() + ' ' + s.getSno())
