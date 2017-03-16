m=int(input())
a=list(map(float, input().split()))
n=int(input())
b=list(map(float, input().split()))
k=sorted(a+b)
if (m+n)%2==0:
    t=k[-1+(m+n)//2]+k[-1+1+(m+n)//2]
    t=t/2
else:
    t=k[-1+(m+n+1)//2]
print('%.5f' %(t,))