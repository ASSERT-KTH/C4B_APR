def happy_sub(n,k):
    print(k)
    if k<n//2+1 or k==n:
        if k!=0 and n%k==0:
            res='YES'
        elif happy_sub(n,10*k+4)=='NO':
            res=happy_sub(n,10*k+7)
        else:
            res='YES'
    else:
        res='NO'
    return res

n=int(input())
print(happy_sub(n,0))