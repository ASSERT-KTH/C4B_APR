n, a, b = list(map(int, input().split()))
ans = n - max(a+1, n-b) +1
print(ans)