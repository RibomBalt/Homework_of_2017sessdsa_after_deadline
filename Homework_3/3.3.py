'''
做计时实验，比较List和Dict的del操作符性能
del lst[i]/del dic[key]
'''
from timeit import *
import random



for x in range(1000,10001,1000):
    l=[i for i in range(x)]
    l1 = [i for i in range(x)]
    d={i:i for i in range(x)}
    randomlist=list(range(x))
    random.shuffle(randomlist)
    # 经测试，由于list自动补齐空位，可能出现两次删除序号一样的情况
    # 因此对del(l[0])、del(l[-1])两种情况进行了测试。
    t_list0=Timer('for i in randomlist:\n\tdel(l[0])','from __main__ import l,randomlist')
    t_list1 = Timer('for i in randomlist:\n\tdel(l1[-1])', 'from __main__ import l1,randomlist')
    t_dict=Timer('for i in randomlist:\n\tdel(d[i])','from __main__ import d,randomlist')
    # 执行命令内含遍历，无需再开1000次
    td=t_dict.timeit(1)
    tl=t_list0.timeit(1)
    tl1=t_list1.timeit(1)
    print('数据量为%d，对列表首元素删除，其中字典删除时间为%fs，列表删除时间为%fs，差值为%fs'%(x,td,tl,td-tl))
    print('数据量为%d，对列表尾元素删除，其中字典删除时间为%fs，列表删除时间为%fs，差值为%fs'%(x,td,tl1,td-tl1))
    # 实验结果：del(l[0])时，字典一定快于列表；del(l[-1])时，字典大部分时候慢于列表，少数时候快于列表
    # 原因分析：list.__delitem__()方法是O(n)复杂度，删除最后一个比删第一个快很多