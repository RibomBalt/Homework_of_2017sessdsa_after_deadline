k=int(input())
# s=input().split()
s=input().split()

def hoare(s,k):
    big=[]
    # bigNum=1 # plus 1
    small=[]
    smallNum=1
    mark=s.pop()
    # n=1
    for i in s:
        # n+=1
        if mark>i:
            smallNum+=1
            small.append(i)
        else:
            big.append(i)
            # bigNum+=1
    if (smallNum==k): # b
        return mark
    elif smallNum<k:
        return hoare(big,k-smallNum)
    else:
        return hoare(small,k)

print(hoare(s,k))