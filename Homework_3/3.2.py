'''
做计时实验，验证Dict的get item和set item都是O(1)的
'''

from timeit import *
# 验证get_item内置函数
for x in range(1000,10001,1000):
    d={i:i for i in range(x)}
    t=Timer('d[999]','from __main__ import d')
    print('字典get_item，容量为%d，时间为%fs'%(x,t.timeit(1000)))
# 验证set_item内置函数
for x in range(1000,10001,1000):
    d={i:i for i in range(x)}
    t=Timer('d[str(x)]=0','from __main__ import d,x')
    print('字典set_item，容量为%d，时间为%fs'%(x,t.timeit(1000)))