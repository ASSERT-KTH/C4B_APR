a, b, c=map(int, input().split())
print(min(a+b+c,2*a+c, 2*b+c, 2*a+2*b))