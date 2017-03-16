# -*- coding: utf-8 -*-
'''
创建一个Xdict 类，继承自dict 类(python 中的字典类)，使得Xdict 类支持dict 类的所有操作，
并且增加一个方法getKeys，用于返回给定值对应的键的列表。(例如Xdict 一个实例为xd=Xdict({2:"a", 3:"a", 4:(2,3)})，
则xd.getKeys("a")返回值为[2,3])。

程序输入（一个字典字符串）：

例如：{2:"a", 3:"a", 4:(2,3)}

程序输出：方法getKeys返回的字典中值为"a"的所有键组成的列表，其元素用sorted方法升序排序后用空格分开的字符串

例如：2 3
'''
dct = eval(input())


class Xdict(dict):
    # 在此编写自己代码
    def getKeys (self, v):
        # filter函数功能是：从后面的迭代器中，选出能使前面的函数返回True的元素打包成列表
        # lambda表达式是一个短函数的缩略形式
        return filter(lambda x: self.get(x) == v, self.keys())


print(' '.join(sorted(list(map(str, Xdict(dct).getKeys('a'))))))