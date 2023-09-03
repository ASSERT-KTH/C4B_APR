n,m,z = map(int,input().split())
if n>m:
    a = n
else:
    a = m 
b = 0
for i in range(a,10001):
    if (a%n == 0) and (a%m == 0):
        b = a
        break 
    a = a + 1
if b == 0:
    print(0)
else:
    print(int(z/b))