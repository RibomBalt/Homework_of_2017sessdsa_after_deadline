'''
创建一个函数，接受两个字符串作为参数，返回两个字符串字符集合的并集。
如接受的两个字符串为"abc"和"bcd"，返回set([‘a’, ’b’, ’c’,’d’])。
'''
s1 = input()
s2 = input()


def getUnion(s1, s2):
    # 请写下你的代码
    # 原来不止一个送命题……set()可以直接把字符串转变成字符
    return set(s1) | set(s2)


print(sorted(getUnion(s1, s2)))
