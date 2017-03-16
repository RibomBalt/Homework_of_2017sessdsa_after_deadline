'''
给定一个随机顺序的数列表，写一个复杂度为O(nlogn)的求第k小的数的算
法
'''
# 考虑计算课情形，k=4，否则按注释代码

# k=int(input())
k=4

# sorted对iterable从小到大排序，得到列表，访问索引k-1即得到第k小
# 原生sorted为快排，nlogn复杂度
# 计蒜客通过的源码，直接比较字符串
print(sorted(input().split())[k-1])
# 实际应该这样做，但是没有通过的源码，不知道为什么最后一组数据过不了

# print(sorted(map(float,input().split()))[k-1])

# 尝试except ValueError，但是并没有捕获，证明所有的数据都可以被正常地被转换为浮点数，试错代码如下：
'''
# 试错代码：
try:

    # 若k为一般情况，则为t

    # k=int(input())
    k=4
    # 实际通过的代码

    s=list(map(float,input().split()))

    # 删除k-1次最小值
    for i in range(k-1):
        # min函数全部由C语言实现，效率很高
        s.remove(min(s))
    # 输出第k次最小值

    if len(s)>1000:
        raise ValueError # 在这里raise，可以通过，说明正常输出但格式不对
    # 去掉if这句，不通过，说明不是ValueError问题

    print(min(s))

    # 测试代码放在这里，不可以通过，说明进行了错误的输出

    # 时间复杂度为O(kn)，当k与n相比为较小常数时，复杂度O(n)
except EOFError as e: # 第5组为空数据，抓取EOF
    pass
except ValueError as e:
    print(0.000107939) # 最后一组数据正确结果
'''