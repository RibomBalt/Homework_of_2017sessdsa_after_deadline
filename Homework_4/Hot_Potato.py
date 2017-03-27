import random
from collections import deque


def hot_potato_simulation (number):
    '''
    模拟热土豆，每次随机传递次数，随机数最大为初始人数，最少传一个人
    :param number: 人数
    :return: 最终模拟的结果，是个随机数
    >>> hot_potato_simulation(10) in list(range(10))
    True
    '''
    # 建立队列，存储的是人的序号
    person_queue = deque(range(number))
    # 出队拿土豆
    potato = person_queue.pop()
    while person_queue:
        # 普通的传递
        for i in range(random.randrange(0, number)):
            person_queue.appendleft(potato)
            potato = person_queue.pop()
        # 移除上一个potato
        potato = person_queue.pop()
    return potato


if __name__ == '__main__':
    for i in range(10):
        print(hot_potato_simulation(100))
