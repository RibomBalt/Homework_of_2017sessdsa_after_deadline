def printFunc (a, b):
    c = a
    d = b
    if a < b:
        a, b = b, a
    while True:

        if (b == 1) | (a % b == 0):
            print(b)
            break
        a %= b
        a, b = b, a
    print((c * d // b))
    return None


s = []
try:
    while True:
        s.append(input().split(' '))
except EOFError as e:
    m = []
    for line in s:
        m.extend(line)
    m.reverse()
    while len(m) is not 0:
        printFunc(int(m.pop()), int(m.pop()))
