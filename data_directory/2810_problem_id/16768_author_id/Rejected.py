n = int(input())

cost = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cost += (i+j) % (n+1)
        
print(cost)