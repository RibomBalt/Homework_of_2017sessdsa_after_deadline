n = int(input())


def printTri(n):
    s = ""
    # 请写下你的代码
    # 用二维列表来记录杨辉三角
    def generator(n):
        for i in range(n):
            for j in range(i):
                a = 1 if j==0 else a*(i-j)/j



print(printTri(n))
min([0])
