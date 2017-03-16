try:
    n = input()
    int(n)
    s = list(n)
    assert (len(s) == 11)
    assert s[0] == '1'
    print('1')
except:
    print('0')
