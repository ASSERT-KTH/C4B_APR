n,m=map(int,input().split())
r=max(n,m)-1
g=6-r
if 6%g==0 :
    print('1'+'/'+str(6//g))
else :
    print(str(g)+'/'+'6')