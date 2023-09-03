import sys
a,b = input().split()
a=int(a)
b = int(b)
x=a-b
if a==0 and b==0:
    print('NO')
    sys.exit()
if x<0:
    x=-x
if x>1:
    print('NO')
else:
    print('YES')