'''
创建一个函数，接受一个参数max(max>=1000)，调用另一题编写的判断函数，
求100到max之间的水仙花数，返回一个包含换行符的字符串，每个数作为一行输出。
'''
n = int(input())


def writeNarcNum(n):
    # 请写下你的代码
    # 纯复制，嵌套定义
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

    # 存储水仙花的列表
    res = []
    # 遍历
    for i in range(100, n + 1):
        # 调用函数
        if isNarcNum(i):
            # 需要转换成字符串
            res.append(str(i))
    # 拼接
    return '\n'.join(res)


print(writeNarcNum(n))

