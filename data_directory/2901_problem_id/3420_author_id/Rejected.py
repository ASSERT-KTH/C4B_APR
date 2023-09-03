c, v0, v1, a, l = map(int, input().split())


pages = v0
if pages>=c:
    print(1)
else:
    for i in range(1, 100000000):
        pages+= min(v0+i*a, v1)
        if pages >= c:
            print(i+1)
            exit()
        pages-=l