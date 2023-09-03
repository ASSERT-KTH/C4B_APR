a, b, n = map(int, input().split())
if b - (a % b * 10 % b) > 10:
    print(-1)
else:
    print(a, end='')
    print((b - (a % b * 10 % b)) % 10, end='')
    print('0' * (n - 1))