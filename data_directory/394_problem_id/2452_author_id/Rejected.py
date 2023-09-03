n, k = map(int, input().split())
print(k*(2*n-2*k-1) if k < n else n*(n-1)//2)