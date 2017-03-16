# -*- encoding:utf-8 -*-
# 二叉排序树法


class node:
    stack = []

    # left is a, right is b
    def __init__ (self, x):
        self.x = x
        self.a = None
        self.b = None

    def __cmp__ (self, other):
        return self.x - other.x

    def __eq__ (self, other):
        return self.x == other.x

# TODO Binary Tree Generator without Recursion
def generate (tree):
    stack = [[tree, 0]]
    t = tree
    while True:
        status = stack.pop()
        if t is None:
            continue
        if status[1] == 0:

            status[1] += 1
            status[0] = t
            t = t.a
            stack.append(status)
            continue
        elif status[1] == 1:
            t=status[0]
            yield t.x
            status[1] += 1
            status[0] = t
            stack.append(status)
            t = t.b
            continue
        else:
            pass


def setup (alist):
    tree_root = node(alist.pop())
    for i in alist:
        node_current = tree_root
        while True:
            if i > node_current.x:
                if node_current.b:
                    node_current = node_current.b
                else:
                    node_current.b = node(i)
                    break
            else:
                if node_current.a:
                    node_current = node_current.a
                else:
                    node_current.a = node(i)
                    break
    return tree_root


if __name__ == '__main__':
    alist = list(map(float, input().split()))
    tree = setup(alist)
    g = generate(tree)
    for i in range(4):
        t = g.__next__()
    print(t)
