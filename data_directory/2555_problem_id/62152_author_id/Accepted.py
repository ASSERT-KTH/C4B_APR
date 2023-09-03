a = []
a = list(input())
n = 0
b = 0
j = 0

while n < len(a):
    k = a[n]
    if k == '0':
        b = b + 1
    if b == 7:
        j = j + 1
        b = 0
    if k == '1':
        b = 0
    n = n + 1

b = 0
n = 0

while n < len(a):
    k = a[n]
    if k == '1':
        b = b + 1
    if b == 7:
        j = j + 1
        b = 0
    if k == '0':
        b = 0

    n = n + 1

if j >= 1:
    print('YES')
else:
    print('NO')