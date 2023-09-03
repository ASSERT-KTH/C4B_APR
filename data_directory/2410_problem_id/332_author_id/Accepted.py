n = int(input())
if n == 0:
    print(1)
else:
    ans = 1
    for i in range(n - 1):
        ans *= 3
    print(ans % 1000003)