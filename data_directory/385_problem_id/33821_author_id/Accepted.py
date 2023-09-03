h1, h2 = map(int, input().split())
diffe = h2-h1
a, b = map(int, input().split())
if h1+a*8>=h2:
    print(0)
elif(a>b):
    num = h2 - h1 - 8 * a
    den = 12 * (a - b)
    print(int((num+den-1)/den))
else:
    print(-1)