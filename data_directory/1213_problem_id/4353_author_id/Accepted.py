def tin(n):
    t=n
    r=[]
    while n:
        r.insert(0,str(n%3))
        n//=3
    return '0' if t==0 else ''.join(r)
def tor(x,y):
    x=tin(x)
    y=tin(y)
    x="0"*max(len(y)-len(x),0)+x
    y="0"*max(len(x)-len(y),0)+y
    return int(''.join([str((int(a)+int(b))%3)for a,b in zip(x,y)]),3)
a,c=map(int,input().split())
print(tor(a,tor(a,c)))