string = input()
n, a, b = map(int, string.split())
if a % n != 0 and b % n != 0:
    print(-1)
else:
    print(a // n + b // n)