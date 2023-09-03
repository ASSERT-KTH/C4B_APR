y, k, n = map(int, input().split())
x = k
lst = []
while x + y <= n:
    if (x + y) % k == 0:
        lst.append(x)
    x += k

if len(lst) < 1:
    print(-1)
lst.sort()
for ans in lst:
    print(ans, end=" ")