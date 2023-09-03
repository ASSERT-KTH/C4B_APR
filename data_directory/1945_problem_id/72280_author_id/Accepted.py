a, b, n = list(map(int, input().split()))
a *= 10
for k in range(10):
    if (a + k) % b == 0:
        a += k
        break
if a % b != 0:
    print(-1)
else:
    print(str(a) + '0' * (n-1))