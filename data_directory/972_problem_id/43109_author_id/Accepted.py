a,b=[int(x)for x in input().split()]
if (abs(a-b)not in [0,1]) or(a==0 and b==0):
    print('NO')
else:print('YES')