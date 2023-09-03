#n = int(input())
n, m = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
l = 0
x = n - m
for a in range(1000):
    for b in range(1000):
        if a**2 + b == n and b** 2 + a ==m:
            l += 1
print(l)