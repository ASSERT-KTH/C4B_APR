d1,d2,d3=[int(s) for s in input().split()]
print(min(d1+d2+d3,2*(d1+d2),2*(d1+d3),2*(d3+d2)))