a,b=[int(x)for x in input().split()]
if abs(a-b)not in [0,1] or(a,b==[0,0]):
    print('NO')
else:print('YES')