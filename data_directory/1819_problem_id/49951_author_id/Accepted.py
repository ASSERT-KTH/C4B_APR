y, k, n = map(int, input().split())
x = k
lst = []
while x <= n:
    if x > y:
        lst.append(x - y)
    x += k

if len(lst) < 1:
    print(-1)
else:
    lst.sort()
    for ans in lst:
        print(ans, end=" ")