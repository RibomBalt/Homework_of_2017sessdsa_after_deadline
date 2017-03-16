'''创建一个函数，接受一个英文字符串作为参数，返回该字符串的整数表示。
如输入"eight-nine"，返回89，输入"one-two-three-four-five"，返回12345。
（注意：有可能出现zero开头的字符串）
'''
s = input()


def en2num(s):
    # 请写下你的代码
    # 建立字典
    words = dict(
        zero = '0',     one = '1',
        two = '2',      three = '3',
        four = '4',     five = '5',
        six = '6',      seven = '7',
        eight = '8',    nine = '9'
    )
    # 利用split函数分隔成列表，同时用map函数直接获取value的列表
    numbers = map(words.get, str(s).split(sep='-'))
    # 不必考虑舍弃0的问题，直接连接字符串
    return ''.join(numbers)


print(en2num(s))
