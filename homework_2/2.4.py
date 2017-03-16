'''
设计一个三维向量类，并实现向量的加法、减法以及向量与标量的乘法和除法运算
（要求三维向量转字符串方法str(向量对象)返回的结果为“(x,y,z)”的格式）。
提示：重写__init__,__add__,__sub__,__mul__,__truediv__,__str__方法

创建对象的方式为：v=Vector3(x,y,z)

程序输入（用空格分开，向量的表示方式为(x,y,z)）：v1 v2 m n

例如：(2,4,6) (3,6,9) 3 2

程序输出（用空格分开）：v1+v2 v1-v2 v1*m v1/n

例如：(5,10,15) (-1,-2,-3) (6,12,18) (1.0,2.0,3.0)

注意：上面v1表示向量1，v2表示向量2，m表示标量m，n表示标量n，
程序输出里面表示向量之间或向量和标量之间运算的结果，v1/m为非地板除，即结果不取整。
'''


# -*- coding: utf-8 -*-
class Vector3:
    # 在此编写代码
    # 构造函数，用元组来存储数据
    def __init__ (self, x, y, z):
        self.component = (x, y, z)
    # 返回一个新的向量，其中map函数可以把两个向量的元组各项分别相加。
    def __add__ (self, vector):
        return Vector3(*map(lambda x, y: x + y, self.component, vector.component))

    # 返回一个新的向量，其中map函数可以把两个向量的元组各项分别相减。
    def __sub__ (self, vector):
        return Vector3(*map(lambda x, y: x - y, self.component, vector.component))
    # 返回新的向量，其中map函数可以把向量的每个分量乘以系数
    def __mul__ (self, ratio):
        return Vector3(*map(lambda x: x * ratio, self.component))
    # 返回新的向量，其中map函数可以把向量的每个分量除以系数
    def __truediv__ (self, ratio):
        return Vector3(*map(lambda x: x / ratio, self.component))
    # toString方法：按照要求的方式返回
    def __str__ (self):
        return '(%s,%s,%s)' % self.component


data = input().split(' ')
s1, s2, m, n = eval(data[0]), eval(data[1]), int(data[2]), int(data[3])
v1 = Vector3(s1[0], s1[1], s1[2])
v2 = Vector3(s2[0], s2[1], s2[2])
print(str(v1 + v2) + ' ' + str(v1 - v2) + ' ' + str(v1 * m) + ' ' + str(v1 / n))
