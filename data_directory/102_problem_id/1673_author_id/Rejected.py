d1,d2,d3 = map(int,input().split())
print(min(d1,d2) + min(d1+d2, d3) + min(d1, d2, d3 + min(d1, d2)))