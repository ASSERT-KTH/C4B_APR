a,b=[int(i) for i in input().split()]
def aval(n):
    t=0
    for i in range(1,n+1):
        if n%i==0:
            t=t+1
    if t==2:
        return 'yes'
z=a+1
while aval(z)!='yes':
    z=z+1
if z==b:
    print('YES')
else:
    print('NO')