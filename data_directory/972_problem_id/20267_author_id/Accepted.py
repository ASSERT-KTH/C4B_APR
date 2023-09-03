a,b=map(int,input().split())
if a==b and b==0:print('NO')
elif abs(a-b)<=1:print('YES')
else:print('NO')