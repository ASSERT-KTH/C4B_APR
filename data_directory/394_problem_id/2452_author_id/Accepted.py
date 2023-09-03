n, k = map(int, input().split())
print(n*(n-1)//2 if k >= n//2 else k*(2*n-2*k-1))