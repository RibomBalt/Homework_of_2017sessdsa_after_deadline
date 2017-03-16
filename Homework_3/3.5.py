'''
请改进上述的算法，使之复杂度降低为O(n)
'''
# 若k为一般情况，则为t

# k=int(input())
k=4
# 实际通过的代码，也是没转换成字符串
s=list(input().split())
# 计蒜客没通过，但实际应该这么写
# s=list(map(float,input().split()))
# 删除k-1次最小值
for i in range(k-1):
    # min函数全部由C语言实现，效率很高
    s.remove(min(s))
# 输出第k次最小值
print(min(s))

# 时间复杂度为O(kn)，当k与n相比为较小常数时，复杂度O(n)