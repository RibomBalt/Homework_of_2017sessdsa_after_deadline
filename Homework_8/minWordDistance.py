# 三个函数，传入源、目标字符串，返回元组，第一项是可行性的判断，
# 第二项是给出操作的特征字符，第三项是字符，+表示增加元素，-表示减少元素
# 函数中必须处理a或b为空的情况
copy = lambda a, b: ((b[-1] in b[:-1]) if b else False, b[-1] if b else None, '+')
insert = lambda a, b: (True, b[-1] if b else None, '+')
delete = lambda a, b: (True, a[-1] if a else None, '-')

# 字典，键是名称，值是元组，
# 第一项是判断函数，第二项是权重
operations = {
    # 复制操作，从源中复制一个字符
    'copy': (copy, 5),
    # 添加操作
    'insert': (insert, 20),
    # 删除操作
    'delete': (delete, 20),
}


def minWordDistance (a: str, b: str, operation: dict = operations):
    '''
    求最小单词距离。可以进行的操作和相应权重传入一个字典
    :param operation: 可以进行的操作及权重的字典
    :param a: 第一个字符串（源）
    :param b: 第二个字符串（目标）
    :return: 最小的距离，元组，第一个元素为元组，表示步骤，第二个元素为值
    '''
    # 缓存字典，中间过程。
    # 键是元组(i,j)，取a得前i个和b的前j个
    # 值为元组，第一个元素为元组，表示步骤，第二个元素为值
    opList = {}

    for m, n in ((m, n) for m in range(1 + len(a)) for n in range(1 + len(b))):
        # 若m,n都为0，则结果可以预定
        if m == 0 and n == 0:
            opList[(m, n)] = ((), 0)

        # 动态规划切片
        str_a = a[:m]
        str_b = b[:n]

        # 找到最小距离的缓存字典，键是距离值，值是对应的操作
        cache = {}
        # 对operation进行遍历，获得哪些可行，哪些不可行
        for name, data in operation.items():
            opFunc, value = data
            # 获得对应操作的三个参数
            operable, pattern, add = opFunc(str_a, str_b)

            if operable:
                # 可以进行操作，获取对应操作的上一级
                try:
                    last = opList[(m - 1, n)] if add == '-' else opList[(m, n - 1)]
                except KeyError:
                    # 如果没有这个条目，则可以直接进入下一个遍历
                    continue
                # 添加新操作条目
                newOp = last[0] + (':'.join((name, pattern)),)
                # 获取新值并放入缓存
                newValue = last[1] + value
                cache[newValue] = newOp
            else:
                continue
        if cache:
            # 获取值最小一项的值和操作，之后删掉字典
            minValue = min(cache.keys())
            minOp = cache[minValue]
            del cache
            opList[(m, n)] = (minOp, minValue)

    return opList[(len(a), len(b))]


if __name__ == '__main__':
    print(minWordDistance('algorithm', 'alligator'))
    # (('delete:a', 'delete:l', 'delete:g', 'delete:o', 'delete:r', 'delete:i', 'delete:t', 'delete:h', 'delete:m', 'copy:a', 'copy:l', 'copy:l', 'copy:i', 'copy:g', 'copy:a', 'copy:t', 'copy:o', 'copy:r'), 225)
