n = int(input())
a = list(map(int, input().split()))
a.sort()
if n % 2:
    print(a[n//2])