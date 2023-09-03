from math import log

a = int(input())
b = int(input())
s = False
n = 0

for i in range(1, 64):
    m = a ** i
    if m == b:
        s = True
        n = i - 1
        if s or (m > b):
            break

if s:
    print('YES\n{}'.format(n))
else:
    print('NO')