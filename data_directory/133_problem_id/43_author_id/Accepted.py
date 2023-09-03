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

for i in range(len(supply)):
    supply[i] = (supply[i] // 2) * 2

res = True
if len(demand):
    res = sum(supply) >= sum(demand) * 2

print('Yes' if res else 'No')