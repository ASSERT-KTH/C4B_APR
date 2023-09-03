a, b = map(int, list(input().split()))
c, d = map(int, list(input().split()))
for i in range(0, 2000):
    for j in range(0, 2000):
        if a * i + b == c * j + d:
            print(a * i + b)
            exit(0)
print(-1)