n,k = [int(i) for i in input().split()]
ans = 0
for i in range(k):
    while n >= 2:
        ans +=  2 * n  - 3
        n -= 2
print(ans)