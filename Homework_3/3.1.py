'''
做计时实验，验证List的按索引取值确实是O(1)
'''
import timeit
# 验证时间与列表大小无关
for x in range(1000,100001,1000):
    alist=[i for i in range(x)]
    t=timeit.Timer('alist[999]','from __main__ import alist')

    print("随机存取，列表大小为%d，用时为%fs"%(x,t.timeit(1000)))
# 验证时间与索引大小无关
for x in range(100,1001,100):
    blist=[i for i in range(1001)]
    t = timeit.Timer('blist[x]', 'from __main__ import blist,x')
    print('随机存取，索引大小为%d，用时为%fs'%(x,t.timeit(1000)))