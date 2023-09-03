a, b, n = list(map(int, input().split()))
a *= 10
for k in range(10):
    if (a + k) % b == 0:
        a += k
        break
if a % b != 0:
    print(-1)
else:
    for i in range(n - 1):
        a *= 10
    print(a)