from collections import deque


def radix_sort (tosort, radix=10):
    '''
    以radix进制对整数进行排序，默认为10
    :param tosort: 待排序的Iterable
    :return: 排序完成的list
    >>> radix_sort([1,2,3,10,11,31,21])
    [1, 2, 3, 10, 11, 21, 31]
    '''
    # main队列
    deque_sort = deque(tosort)
    # 基数列表
    deque_list = [deque() for i in range(radix)]
    # 求最大位数，作为遍历次数
    max_len = max(map(lambda x: len(str(x)), tosort))
    for i in range(max_len):
        # 第一阶段：当main队列非空时，添加到基数队列中
        while deque_sort:
            # 从右边弹出元素，通常是低位较大的元素
            n = deque_sort.pop()
            # 求指定位数
            k = n // (radix ** i) % radix
            # 从桶左边加入元素，维持低位较大的靠后
            deque_list[k].appendleft(n)
        for deques in deque_list:
            # 依次把基数队列的元素从右边取出，从右边放进main队列中，先入队的更小
            deque_sort.extend(deques)
            # 清空基数队列
            deques.clear()
    # 返回列表
    return list(deque_sort)
    # 实际上为了节省资源，可以用生成器，可以对返回结果进行遍历，代码如下
    # while deque_sort:
    #     yield deque_sort.popleft()
