class Node:
    def __init__ (self, data=None):
        '''
        建立一个节点
        :param data: 
        '''
        self.data = data
        self.next = None


class linkedStack:
    def __init__ (self):
        '''
        建立一个空栈
        '''
        self.top = None
        self.length = 0

    def push (self, data):
        '''
        压栈操作
        :param data: 压栈的数据
        :return: self
        '''
        node = Node(data)
        node.next = self.top
        self.top = node
        self.length += 1
        return self

    def pop (self):
        '''
        出栈。若弹空栈则报错。
        :return: 出栈的数据 
        '''
        if self.isEmpty():
            raise IndexError
        node = self.top
        self.top = node.next
        self.length -= 1
        return node.data

    def isEmpty (self):
        '''
        检验是否为空。是返回True
        :return: 
        '''
        return self.top is None

    def __len__ (self):
        '''
        返回大小
        :return: 
        '''
        return self.length


class linkedQueue:
    def __init__ (self):
        '''
        建立空队列。
        '''
        self.head = None
        self.tail = None
        self.size = 0

    def __len__ (self):
        '''
        获取长度
        :return: 长度
        '''
        return self.size

    def isEmpty (self):
        '''
        判断是否空队
        :return: 
        '''
        return self.head is None

    def put (self, data):
        '''
        从队首添加元素
        :param data:元素 
        :return: 本身
        '''
        node = Node(data)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1
        return self

    def get (self):
        '''
        从队尾移除元素
        :param data:元素 
        :return: 元素内容
        '''
        if self.isEmpty():
            raise IndexError
        # 若只有一个元素，特殊处理
        node = self.head
        if self.size is 1:
            self.head = self.tail = None
            return node.data
        # 无法直接获取倒数第二个，所以遍历
        while node.next is not self.tail:
            node = node.next
        # 缓存最后一个，对队尾进行操作
        getNode = self.tail
        self.tail = node
        # 长度-1
        self.size -= 1
        return getNode.data
