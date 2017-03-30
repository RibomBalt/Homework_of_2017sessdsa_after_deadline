from .Lists import Node


class deutNode(Node):
    def __init__ (self, data):
        '''
        节点构造函数，继承同一个包里的Node类，添加一个prev属性
        :param data: 
        '''
        super(deutNode, self).__init__(data)
        self.prev = None


class duetUnorderedList():
    '''
    关于双向无序链表的类。这里暂时不含有length属性，采用遍历法
    '''

    # TODO
    def __init__ (self):
        self.head = None
        self.tail = None

    def __len__ (self):
        '''
        返回双向链表的长度
        :return: 长度
        '''
        i = 0
        node = self.head
        while node is not None:
            i += 1
            node = node.next
        return i

    def _iter (self):
        '''
        私有方法：
        一个生成器，可以遍历元素。
        :return: 
        '''
        node = self.head
        while node is not None:
            # 生成元素
            yield node.data
            node = node.next

    def __str__ (self):
        '''
        返回字符串表示形式
        :return: 
        '''
        return list(self._iter())

    def __getitem__ (self, index):
        '''
        获取某位置的元素
        :param index: 
        :return: 
        '''
        node = self.head
        try:
            assert index >= 0
            # 遍历index次，达到需要的位置
            for i in range(index):
                node = node.next
            return node.data
        except:
            # 说明参数不合法
            raise IndexError

    def isEmpty (self):
        '''
        判断本列表是否为空
        :return: True if empty
        '''
        return self.head is None

    def addLast (self, data):
        '''
        向链表的末尾添加元素
        :data: 数据
        :return: None
        '''
        node = deutNode(data)
        # 判断是否为空
        if self.isEmpty():
            self.head = self.tail = node

        else:
            # 互联
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return None

    def addFirst (self, data):
        '''
        向链表开头添加元素
        :param data: 
        :return: 
        '''
        node = deutNode(data)
        if self.isEmpty():
            self.tail = self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def popLast (self):
        '''
        从无序表末尾移除元素。若没有元素，assert异常。
        :return: 被移除的元素
        '''
        node = self.tail
        assert node is not None, 'There are no elements!'
        # 获取前一个元素。可能为空
        self.tail = node.prev
        if self.tail is None:
            # 只有一个元素，删除后为空
            self.head = None
        else:
            self.tail.next = None
        return node.data

    def popFirst (self):
        '''
        从无序表开头移除元素。若没有元素，assert异常。
        :return: 被移除的元素
        '''
        node = self.head
        assert node is not None, 'There are no elements!'
        # 获取前一个元素。可能为空
        self.head = node.next
        if self.head is None:
            # 只有一个元素，删除后为空
            self.tail = None
        else:
            self.head.prev = None
        return node.data

    def index (self, data):
        '''
        获取某个数据第一次出现的位置。若没有返回-1。
        :param data: 
        :return: 
        '''
        index = 0
        node = self.head
        try:
            # 持续循环直到找到或到末尾
            while node.data != data:
                node = node.next
                index += 1
            # 跳出循环，说明找到
            return index
        except:
            # except说明对None操作，没有该元素
            return -1

    def insert (self, data, index):
        '''
        向某个位置插入一个元素。若位置不合法，抛出异常
        :data: 数据
        :index: 序号
        :return: 
        '''
        newNode = deutNode(data)
        node = self.head
        try:
            assert index >= 0
            # 遍历到指定位置，应当是被替换的位置
            for i in range(index):
                node = node.next
            newNode.next = node
            newNode.prev = node.prev
            # 最后一个最有可能是None，因此先动后面的，避免出现异常修改原数据结构
            node.prev = newNode
            newNode.prev.next = newNode
        except:
            raise IndexError
