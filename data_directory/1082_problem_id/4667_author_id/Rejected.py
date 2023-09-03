from math import log

a = int(input())
b = int(input())
s = False
n = 0

for i in range(1, int(log(b, a)) + 1):
    if (a ** i) == b:
        s = True
        n = i - 1

if s:
    print('YES\n{}'.format(n))
else:
    print('NO')