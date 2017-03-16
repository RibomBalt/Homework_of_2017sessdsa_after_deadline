'''
创建一个函数，接受一个参数n(n>=100)，判断这个数是否为水仙花数
（即满足如果这个数为m位数，则每个位上的数字的m次幂之和等于它本身,
例如1^3 + 5^3+ 3^3 = 153，1^4+6^4+3^4+4^4=1634）,
返回True或者False。
'''
n = int(input())


def isNarcNum(n):
    # 请写下你的代码
    # 获得各位的list，需要用str中转
    num_list = list(str(n))
    # 获得次方
    a = len(num_list)
    # 将中转的str转换回int，得到map object
    num_list = map(int, num_list)
    # 遍历，叠加
    res = 0
    for i in num_list:
        res += i ** a
    # 输出布尔值
    return res == n


print(isNarcNum(n))
