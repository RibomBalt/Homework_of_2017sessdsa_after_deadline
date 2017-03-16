# -*- encoding: utf-8 -*-
'''创建一个函数，接受两个长度相同的元组，用这两个元组中的所有数据组成一个字典并返回。
如元组(1, 2, 3)和("abc", "def", "ghi")生成字典{1:"abc", 2:"def",3:"ghi"}。
'''
keys = eval(input())
values = eval(input())


def generateDict(keys, values):
    # 请写下你的代码
    # 送命题……zip函数功能是取出各序列的同位元素并重组成元组并打包成列表
    # 第一次出现一行就解决的题←_←
    return dict(zip(keys, values))


print(generateDict(keys, values))
