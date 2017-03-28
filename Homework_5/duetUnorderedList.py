from .Lists import Node


class duetNode(Node):
    def __init__ (self, data):
        '''
        节点构造函数，继承同一个包里的Node类，添加一个prev属性
        :param data: 
        '''
        super(duetNode, self).__init__(data)
        self.prev = None


class duetUnorderedList():
    '''
    关于双向无序链表的类。这里暂时不含有length属性，采用遍历法
    '''

    # TODO
    def __init__ (self):
        self.head = None
        self.tail = None
