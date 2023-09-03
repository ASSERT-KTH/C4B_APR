n, a, b = [int(x) for x in input().split()]

if(b+1) < (n-a):
    print(b+1)
else:
    print(n-a)