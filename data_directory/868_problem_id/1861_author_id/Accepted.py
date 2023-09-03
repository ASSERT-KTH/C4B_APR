a = "6842"
n = int(input())
if n == 0:
    print(1)
else:
    n %= 4
    print(a[n])