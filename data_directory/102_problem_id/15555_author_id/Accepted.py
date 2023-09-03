a,b,ab=map(int, input().split())
print(min(a+b+ab,2*a+2*b,2*a+2*ab,2*b+2*ab))