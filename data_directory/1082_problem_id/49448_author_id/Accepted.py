k = int(input())
l = int(input())

c = 1
while (l / k) != 1 and l - k > 0 and l != 1:
    l /= k
    c += 1
if l / k == 1:
    print('YES')
    print(c - 1)
else:
    print('NO')