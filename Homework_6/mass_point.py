import turtle

# 单位时间
dt = 0.1
totalTime = 0


class Vector():
    '''
    定义向量类
    '''

    def __init__ (self, vector):
        if hasattr(vector, '__iter__') or hasattr(vector, '__getitem__'):
            self.data = tuple(vector)
        elif isinstance(vector, Vector):
            self.data = vector.data

    def __add__ (self, other):
        assert len(self.data) == len(other.data)
        return Vector((i + j for i, j in (self.data, other.data)))

    def __sub__ (self, other):
        assert len(self.data) == len(other.data)
        return Vector((i - j for i in self.data for j in other.data))

    def __mul__ (self, other):
        return Vector((other * i for i in self.data))

    def __truediv__ (self, other):
        return Vector((i / other for i in self.data))


class mass():
    def __init__ (self, name, m, site, v, f):
        '''
        建立一个质点
        :param m: 质量
        :param v: 速度（二元组）
        :param f: 力（集合）
        '''
        self.name = str(name)
        self.m = float(m)
        self.site = Vector(site)
        self.v = Vector(v)
        self.f = list(f)

    def __str__ (self):
        '''
        返回质点所有信息
        :return: 
        '''
        return 'name: %s; mass: %f; site: %s; velocity: %s' % (self.name, self.m, self.site, self.v)

    def move (self):
        '''
        先计算本次位移，然后计算本次动量，最后计算本次受力变化
        :return: 
        '''
        self.site = self.site + (self.v * dt)
        for force in self.f:
            self.v = self.v + (force / self.m) * dt
            force.update()
        return True

    def move_turtle (self, turtle):
        self.move()
        turtle.goto(self.site.data)


class Force(Vector):
    '''
    定义受力的基类
    '''

    def __init__ (self, f):
        Vector.__init__(self, f)

    def update (self):
        '''
        子类进行拓展
        :return: 
        '''
        pass


class NearEarthGravity(Force):
    '''
    重力类
    '''
    g = 9.8

    def __init__ (self):
        Force.__init__(self, Vector((0, -self.g)))

    def update (self):
        pass


if __name__ == '__main__':
    aturtle = turtle.Turtle()
    m = mass('ball', 10, (0, 0), (5, 0), [NearEarthGravity()])
    for i in range(100):
        m.move_turtle(aturtle)
    print(aturtle.position())
