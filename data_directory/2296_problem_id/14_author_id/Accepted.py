n, m = map(int, input().split())
if m % 2 == 1: print(n*(m//2)+n//2)
else: print(n*(m//2))