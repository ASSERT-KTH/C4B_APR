k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
ans = 0
for a in range(1, d + 1):
    if a % l == 0 or a % k == 0 or a % m == 0 or a % n == 0:
        ans = ans + 1
print(ans)