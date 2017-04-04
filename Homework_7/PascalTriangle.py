def pascal_triangle (alist, n):
    '''
    创建一个Pascal三角形，并将其输出到给定的列表中
    :param alist: 保存输出的列表
    :param n: 要计算的阶数
    :return: 最后一行的列表（非副本）
    '''
    # 清空列表，防止影响结果
    alist.clear()
    if n == 0:
        # 零阶情况，直接添加列表并返回
        alist.append([1])
        return [1]
    # 否则，获得上一行的数据。共有n个。
    last = pascal_triangle(alist, n - 1)
    # 本行的第一个和最后一个为1，其他的为上一行0+1,1+2,...,n-2+n-1.
    this = [1] + [last[i] + last[i + 1] for i in range(0, n - 1)] + [1]
    alist.append(this)
    return this


def toStr (pascal):
    '''
    一个函数，把帕斯卡三角形改成字符串表示。
    :param pascal: pascal三角形的列表
    :return: 字符串表示
    '''
    res = ''
    for line in pascal:
        # 对每行进行遍历，转换成字符串附加到res后
        res += '\t'.join(list(map(str, line)) + ['\n'])
    return res


if __name__ == '__main__':
    alist = []
    pascal_triangle(alist, 8)
    print(toStr(alist))
