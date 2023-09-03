n = int(input())
if n <= 2:
    print(n)
elif n % 2 == 0:
    print(max(n*(n-1)*(n-2)//2, (n-1)*(n-2)*(n-3), n*(n-1)*(n-3)))
else:
    print(n*(n-1)*(n-2))