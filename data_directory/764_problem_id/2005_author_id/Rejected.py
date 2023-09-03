[x1,x2,x3] = [int(x) for x in input().split()]
avg = (x1+x2+x3)/3
print(int(abs(x1-avg)+abs(x2-avg)+abs(x3-avg)))