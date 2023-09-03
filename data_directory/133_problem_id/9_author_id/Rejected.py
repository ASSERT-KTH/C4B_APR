s = list(map(int, input().split()))
t = list(map(int, input().split()))
xs = [ s[i] - t[i] for i in range(len(s)) ]

demand = []
supply = []
for x in xs:
    if x < 0:
        demand.append(-x)
    else:
        supply.append(x)

res = True
if len(demand):
    res = sum(supply) >= sum(demand) * 2
    if res and len(supply) == 2 and supply[0] % 2 == supply[1] % 2 == 1:
        res = False

print('Yes' if res else 'No')