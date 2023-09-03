n = int(input())
a = list(map(int, input().split()))
a.sort()
if a % 2:
    print(a[n//2])