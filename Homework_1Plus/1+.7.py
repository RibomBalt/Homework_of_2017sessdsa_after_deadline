try:
    while True:
        n=int(input())
        s=0
        assert n>0
        while n>=3:
            n-=2
            s+=1
        if n==2:
            s+=1
        print(s)
except:
    pass