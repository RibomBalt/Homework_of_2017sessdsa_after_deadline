def name (func):
    '''
    返回一个函数的名称
    :param func: 函数
    :return: 
    '''
    return func.__name__


def copy (a: str, b: str):
    '''
    a,b两个字符串的最后一步可否用一个复制操作来完成，以及对应的上一个元素
    :param a: 目标串片段
    :param b: 源串片段
    :return: 如果可以，返回一个元组，对应上一个元素的改变值，如果不能，返回None
    '''
    try:
        # 如果末尾相同的话，最后一步可以复制
        return (-1, -1) if a[-1] == b[-1] else None
    except IndexError:
        # 有空串，必然不可以复制
        return None


def add (a: str, b: str):
    '''
    最后一步判断能否进行添加操作
    :param a: 目标串
    :param b: 源串
    :return: 如果可以，返回一个元组，对应上一个元素的改变值，如果不能，返回None
    '''
    # 目标串非空
    return (-1, 0) if a else None


def delete (a: str, b: str):
    '''
    最后一步能否进行删除操作
    :param a: 目标串
    :param b: 源串
    :return: 如果可以，返回一个元组，对应上一个元素的改变值，如果不能，返回None
    '''
    # 源串非空
    return (0, -1) if b else None


# 可操作的方法集合
methods = {
    copy: 5,
    add: 20,
    delete: 20,
}


def minEdit (a: str, b: str):
    '''
    计算最小编辑距离。与对应的过程
    :param a: 第一个字符串，目标
    :param b: 第二个字符串，源
    :return: 返回一个元组，第一个用字符串表示了过程，第二个为结果
    '''
    la, lb = len(a), len(b)
    cache = {}
    for m, n in ((m, n) for m in range(1 + la) for n in range(1 + lb)):
        # 目标串前m个，源串前n个
        if m == 0 and n == 0:
            # 初始情况
            cache[(0, 0)] = ((), 0)
            continue
        else:
            str_a = a[:m]
            str_b = b[:n]
            # 缓存下一步三种方法中的最小值
            method_cache = {}
            # 读取操作和对应的权重
            for func, value in methods.items():
                change = func(str_a, str_b)
                # 判断是否可以进行操作
                if change is not None:
                    # 可以操作，那么暂时记录，这种操作对应的值和操作
                    newValue = value + cache[(change[0] + m, change[1] + n)][1]
                    # 被改变的特征值
                    changed_char = str_a[-1] if change[0] else str_b[-1]
                    newOp = cache[(change[0] + m, change[1] + n)][0] + ('%s:%s' % (name(func), changed_char),)
                    method_cache[newValue] = newOp
                else:
                    continue
            # 如果有元素满足条件，读取最小的
            if method_cache:
                minValue = min(method_cache.keys())
                minOp = method_cache[minValue]
                # 存入缓存
                cache[(m, n)] = (minOp, minValue)
    return cache[(la, lb)]


if __name__ == '__main__':
    print(minEdit('algorithm', 'alligator'))
