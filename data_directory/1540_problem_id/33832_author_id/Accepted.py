k= set([(i*(i+1))//2 for i in range(1,45000)])
n = int(input())
f = set([n - i for i in k])
t = k & f
if t:
    print('YES')
else:
    print('NO')