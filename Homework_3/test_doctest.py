

def average(*args):
    '''
    >>> print(average(1,2,3,4,5))
    3.0
    >>> average(0,0,0)
    0.0
    >>> 0
    0
    '''
    s=0
    for i in args:
       s+=i
    return s/len(args)

def a():

    pass

import doctest
doctest.testmod()