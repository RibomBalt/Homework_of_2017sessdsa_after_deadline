'''创建一个函数，接受一个参数n，返回n阶杨辉三角。'''
n = int(input())


def printTri(n):
    s = ""
    # 请写下你的代码
    # 用二维列表来记录杨辉三角
    tri = []
    for i in range(n):
        # 第i+1行新列表
        toAdd = []
        for j in range(i + 1):
            # 计算该位置数，若不是1则可以由上方两数相加得到
            # 此处注意：Python中，逻辑与或非优先次序在==之前，和C、Java等不同
            k = 1 if (j == 0) | (j == i) else tri[i - 1][j] + tri[i - 1][j - 1]
            toAdd.append(k)
        tri.append(toAdd)
    # 将列表转换为str，添加空格和回车，并打散为一层
    str_list=[]
    for l in tri:
        # 取出一行的元素，添加空格
        str_list.append(' '.join(map(str, l)))
    # 这里讲所有行串成一个字符串，用换行分隔
    s = '\n'.join(str_list)
    return s


print(printTri(n))
