n, k  = map(int, input().split())
s = "1"
next = 2

for i in range(n - 1):
    s = s + str(next) + s
    next += 1

print(s[k - 1])