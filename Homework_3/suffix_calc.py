d_operator={}
# 防止空栈pop出错，定义的占位符。最低优先级
d_operator[' ']=0
d_operator['(']=1
d_operator['^']=4
d_operator['*']=3
d_operator['/']=3
d_operator['+']=2
d_operator['-']=2



def to_suffix(l):
    '''
    Help: 将中缀表达式转换为后缀表达式.

    :param b: 待转换列表
    :return: 转换后列表，其中所有数字均为int
    >>> print(to_suffix('5 * 3 ^ ( 4 - 2 )'.split()))
    [5, 3, 4, 2, '-', '^', '*']
    >>> print(to_suffix([1,'+',2]))
    [1, 2, '+']
    '''
    res=[]
    stack=[' ']
    for i in l:
        if i in d_operator.keys():
            if i =='(':
                stack.append(i)
                continue
            top=stack.pop()
            while d_operator[top]>=d_operator[i]:
                res.append(top)
                top=stack.pop()
            stack.append(top)
            stack.append(i)
        elif i==')':
            top=stack.pop()
            while top != '(':
                res.append(top)
                top=stack.pop()
        else:
            res.append(int(i))
    t=stack.pop()
    while t != ' ':
        res.append(t)
        t=stack.pop()
    return res

import doctest
doctest.testmod()
