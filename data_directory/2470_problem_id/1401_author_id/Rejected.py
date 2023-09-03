import math


N, M = map(int, input().split())


def check(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

ans = []
for i in range(N + 1, M + 1):
    if check(i):
        ans.append(i)

if len(ans) != 1:
    print("NO")
else:
    print("YES")