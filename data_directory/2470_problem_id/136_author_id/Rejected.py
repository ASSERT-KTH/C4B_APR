a,b=[int(i) for i in input().split()]
def aval(n):
    t=0
    for i in range(2,n):
        if n%i==0:
            t=1
    return t
z=a+1
t=0
while aval(z)!=0:
    t=t+1
if t==b:
    print('YES')
else:
    print('NO')