a, b, n = map(int, input().split())
if a % b == 0 or a * 10 % b == 0:
    print(a, end='')
    print('0' * n, end='')
elif b - (a % b * 10 % b) >= 10:
    print(-1)
else:
    print(a, end='')
    print(b - (a % b * 10 % b), end='')
    print('0' * (n - 1))