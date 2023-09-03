n = int(input().strip())
maxx =  (n // 7)*2
minn = (n // 7)*2
if n % 7 > 1:
    maxx += 2
else:
    maxx += n % 7
print(minn,maxx)