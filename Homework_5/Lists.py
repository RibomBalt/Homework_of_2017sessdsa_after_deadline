# -*- encoding:utf-8 -*-
'''
有序表和无序表的类
'''


class Node:
    def __init__ (self, data=None):
        '''
        建立一个节点
        :param data: 
        '''
        self.data = data
        self.next = None


class unorderedList(object):
    def __init__ (self, cacheLength=True, hasTail=False):
        '''
        建立一个无序表。初始长度为0
        :param cacheLength: 是否缓存长度，默认缓存。建议数据量较大时缓存，数据量较小时不缓存
        :param hasTail:是否缓存尾部，默认不缓存。经常使用append方法可以考虑缓存
        '''
        super().__init__(cacheLength)
        self.head = None
        if cacheLength:
            self._length = 0
        if hasTail:
            self._tail = None

    def __len__ (self):
        '''
        返回长度
        :return: 一个整数，无序表长度
        '''
        if hasattr(self, '_length'):
            # 缓存了长度，直接引用
            return self._length
        else:
            # 没有定义长度，则遍历
            node = self.head
            length = 0
            while node is not None:
                node = node.next
                length += 1
            return length

    def __iter__ (self):
        '''
        返回迭代器
        :return: 迭代器
        '''
        return iterUnorderedList(self)

    def __getitem__ (self, index):
        '''
        获取某个位置的元素。若没有，则抛出异常
        代替了__getslice__进行切片
        :param index: 
        :return: 该位置的元素
        '''
        try:
            assert index >= 0
            node = self.head
            for i in range(index):
                node = node.next
            return node.data
        except:
            raise IndexError

    def __setitem__ (self, index, data):
        '''
        对某个位置元素进行赋值。若没有，则抛出异常
        :param index: 
        :param data:
        :return: 该位置的元素
        '''
        try:
            assert index >= 0
            node = self.head
            for i in range(index):
                node = node.next
            node.data = data
        except:
            raise IndexError

    def __str__ (self):
        '''
        返回列表的字符串表示形式。（因为已经iter了，可以直接遍历）
        :return: 
        '''
        return str(list(self))

    def isEmpty (self):
        '''
        判断是否为空
        :return: True if 表为空
        '''
        return None is self.head

    def add (self, data):
        '''
        用append实现add方法，添加在尾部
        :param data: 要添加的数据
        :return: None
        '''
        return self.append(data)

    def append (self, data):
        '''
        在尾部添加元素
        :param data: 要添加的元素
        :return: None
        '''
        if not hasattr(self, '_tail'):
            # 没有tail参数，普通地遍历
            node = self.head
            # 下一个非空，就达到了最后一个
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        else:
            # 有tail参数，特殊处理
            length = len(self)
            if length:
                self._tail.next = Node(data)
            else:
                self._tail = self.head = Node(data)
        # 有缓存长度下，对长度加一
        if hasattr(self, '_length'):
            self._length += 1
        return None

    def extend (self, iterable):
        '''
        批量添加iterable到列表末尾
        :param iterable: 可遍历的元素
        :return: None
        '''
        node = None
        iterable = iter(iterable)
        try:
            if self.isEmpty():
                node = Node(iterable.__next__())
                self.head = node
                if hasattr(self, '_length'):
                    self._length += 1
                for data in iterable:
                    node.next = Node(data)
                    node = node.next
                    if hasattr(self, '_length'):
                        self._length += 1
                # 如果有tail参数
                if hasattr(self, '_tail'):
                    self._tail = node

            else:
                # 列表不空
                node = self.head
                # 遍历到列表尾部
                while node.next is not None:
                    node = node.next
                # 对iterable遍历
                for data in iterable:
                    node.next = Node(data)
                    node = node.next
                    if hasattr(self, '_length'):
                        self._length += 1
                # 如果有tail参数
                if hasattr(self, '_tail'):
                    self._tail = node
        except:
            if (node is not None) and hasattr(self, '_tail'):
                # 这样可以保证node存储的是队尾的元素
                self._tail = node

    def index (self, data):
        '''
        返回某个元素的位置，没有返回-1
        :param data: 待求的序数
        :return: 序号或-1
        '''
        try:
            i = 0
            node = self.head
            # 遍历，当不空时
            while node is not None:
                # 若找到了，则返回序数，否则加1
                if node.data is data:
                    return i
                else:
                    i += 1
                    node = node.next
            # 没有找到，报错
            raise IndexError
        except:
            # 没有找到，所以返回-1
            return -1

    def pop (self, index):
        '''
        移除index处元素并返回。若没有，抛出IndexError
        没有双向链表，故移除末端元素没有优化。
        :return: 移除位置的元素
        '''
        try:
            node = self.head
            # 只有一个元素，没有prev
            if node.next is None:
                self.head = None
                # 有tail，则data
                if hasattr(self, '_tail'):
                    self._tail = None
                if hasattr(self, '_length'):
                    self._length -= 1
                return node.data
            else:
                # 迭代数次，然后准备pop
                for i in range(1, index):
                    node = node.next
                # 先取出下一个元素，然后从结构中删除
                popNode = node.next
                node.next = node.next.next
                if hasattr(self, '_length'):
                    self._length -= 1
                return popNode.data

        except:
            raise IndexError

    def insert (self, data, index):
        '''
        在某个位置插入元素。若位置不合法，抛出IndexError异常
        :param data: 待插入元素
        :param index: 位置
        :return: None
        '''
        if index < 0:
            raise IndexError
        node = self.head
        # 如果一开始为空
        if self.isEmpty() and hasattr(self, '_tail'):
            self.head = self._tail = Node(data)
        # 如果插入在开头
        elif index is 0:
            nodeNext = self.head
            self.head = Node(data)
            self.head.next = nodeNext
        else:
            for i in range(1, index):
                node = node.next
            # 如果恰好到了尾部
            if hasattr(self, '_tail') and (node is self._tail):
                node.next = Node(data)
                self._tail = node.next
            else:
                nodeNext = node.next
                node.next = Node(data)
                node.next.next = nodeNext
        if hasattr(self, '_length'):
            self._length += 1
        return None


class iterUnorderedList:
    def __init__ (self, linked):
        '''
        建立unorderedList迭代器
        :param linked: 传入的unorderedList参数
        '''
        self.linked = linked.head

    def __next__ (self):
        '''
        下一个元素
        :return: 返回下一个元素，到None时抛出StopIteration
        '''
        if self.linked is None:
            raise StopIteration
        else:
            data = self.linked.data
            self.linked = self.linked.next
            return data


class orderedList(unorderedList):
    # 删一些不必要的属性方法
    dellist = {unorderedList.insert, unorderedList.append}
    for method in dellist:
        del method
    del dellist

    def __init__ (self, cachelength=True):
        '''
        构造函数，构造一个有序表，小的在前
        :param cachelength: 是否缓存长度
        '''
        # 有序表不需要队尾
        super().__init__(cachelength, hasTail=False)
        self.head = None
        if cachelength:
            self.length = 0

    def add (self, data):
        '''
        有序添加一个元素
        :param data: 数据
        :return: None
        '''
        node = self.head
        # 第一个元素就比data大
        if data <= node.data:
            nodeFirst = Node(data)
            nodeFirst.next = node
            self.head = nodeFirst
            if hasattr(self, '_length'):
                self._length += 1
            return None
        else:
            # 一般情况
            while node.next is not None and node.next.data < data:
                node = node.next
            nodeNext = Node(data)
            nodeNext.next = node.next
            node.next = nodeNext
            if hasattr(self, '_length'):
                self._length += 1
            return None

    def _extend (self, iterable):
        '''
        扩展一整个iterable
        思路大概是先对iterable排序，然后按序添加
        :param iterable: 可迭代对象
        :return: None
        '''
        # TODO 这个实在写不完了，就这么挂着吧，表示我想到了要做这么个接口，欢迎Pull Requests
        pass

    def search (self, data):
        '''
        查找一个数据并返回序号。若没有，返回-1，
        :param data: 待查找的数据
        :return: 
        '''
        try:
            node = self.head
            i = 0
            # 仅当小于等于时才有可能在后面出现。
            while node.data <= data:
                if node.data == data:
                    return i
                else:
                    i += 1
                    node = node.next
            return -1
        except:
            return -1


# 测试代码
if __name__ == '__main__':
    uol = unorderedList(True, True)
    print(uol)
    uol.append(0)
    print(uol)
    print(uol.pop(0))
    print(uol)
    uol.extend([1, 2, 3, 4])
    uol.extend([1, 2, 3, 4])
    print(uol)
    uol.insert(index=1, data=-1)
    uol.pop(2)
    print(uol)
