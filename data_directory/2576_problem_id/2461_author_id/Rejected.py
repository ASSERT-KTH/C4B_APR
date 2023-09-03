k, a, b = map(int, input().split())
print(-1 if max(a, b) < k else a // k + b // k)