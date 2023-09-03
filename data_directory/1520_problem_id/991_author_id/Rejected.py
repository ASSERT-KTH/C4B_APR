n,a,b,c=map(int,input().split())
m={}
def p(i,q,w,e):
    if i in m:
        return m[i]
    if i<min(q,w,e):
        f=-1
    elif i%min(a,b,c)==0:
        f=int(i//min(a,b,c))
    else:
        f=max(p(i-q,q,w,e)+1,p(i-w,q,w,e)+1,p(i-e,q,w,e)+1)
    m[i]=f
    return f
print(p(n,a,b,c))