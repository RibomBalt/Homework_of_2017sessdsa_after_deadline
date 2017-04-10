def zero_if_negative (func):
    '''
    装饰器，当输入参数为二元元组时，若元组某一个元素不为正数，则返回空值.否则维持原状。
    :param func: 改变的函数
    :return: 
    '''

    def wrapper (self, item):
        if isinstance(item, tuple) and (item[0] <= 0 or item[1] <= 0):
            return ((), 0)
        else:
            return func(self, item)

    return wrapper


class specialDict(dict):
    '''
    特殊的类，继承了dict，但是getitem使用装饰器
    '''

    @zero_if_negative
    def __getitem__ (self, item):
        '''
        魔改的getitem，达到上述效果
        :param item: 
        :return: 
        '''
        return dict.__getitem__(self, item)


def backpackproblem (treasureDict: list, capacity: int, cacheList: specialDict = specialDict()):
    '''
    解决01背包问题，输出该问题的最优解。动态规划思路，不含重复元素
    :param treasureDict: 剩余宝物列表
    :param capacity: 剩余背包容量
    :param cacheList: 容量为c，前n个元素下的解，元素格式：二元元组，第一个元素是序号元组，第二个元素是总价值
    :return: 解，格式同cacheList元素
    
    >>> print(backpackproblem([{'w':2, 'v':3},{'w':3, 'v':4},{'w':4, 'v':8},{'w':5, 'v':8},{'w':9, 'v':10}], 20 ,specialDict()))
    ((0, 2, 4), 21)
    '''
    # 对每个容量：
    for c in range(1, capacity + 1):
        # 对每个宝物之前的元素数量（不含）
        for num in range(len(treasureDict)):
            # 获取上一轮元素的值
            last = cacheList[(c, num)]
            # 若新元素比容量大，则不必比较与修改
            if treasureDict[num]['w'] > c:
                cacheList[(c, num + 1)] = last
            else:
                # 新元素比容量小，单独考虑选择了新元素的情况
                new = treasureDict[num]['v'] + cacheList[(c - treasureDict[num]['w'], num)][1]
                if new <= last[1]:
                    cacheList[(c, num + 1)] = last
                else:
                    # 选择新元素的更大，进行存储
                    # 第一个元素添加一个num+1序号
                    cacheList[(c, num + 1)] = (cacheList[(c - treasureDict[num]['w'], num)][0] +
                                               (num,), new)

    return cacheList[capacity, len(treasureDict)]


if __name__ == '__main__':
    print(
        backpackproblem([{'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}],
                        20))
