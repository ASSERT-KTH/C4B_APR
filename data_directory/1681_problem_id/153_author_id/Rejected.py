#n = int(input())
n, m = map(int, input().split())
#s = input()
#c = list(map(int, input().split()))
l = 0
for a in range(1000):
    for b in range(1000):
        if (a - b) * (a + b - 1) == n - m:
            l += 1
print(l)