data = [int(x) for x in input().split()]
p = data[0] - data[1] 
pf = data[0] - p - data[2]
if pf <=0:
    pf = 0
print(p-pf)