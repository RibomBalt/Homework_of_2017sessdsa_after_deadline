def iterator():
    x=2
    while True:
        yield x
        x+=3
s=0
i=0
n=int(input())
for x in iterator():
    s+=x
    i+=1
    if n<=i:
        break
print(s)
