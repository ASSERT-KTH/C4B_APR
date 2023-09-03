inp = int(input())
prime = list()
count = 0

for i in range(2,inp+1):
    ans = 0
    for j in range(2,i - 1):
        if i%j == 0:
            ans = ans + 1
    if ans == 0:
        prime.append(i)

#print(prime)

for i in range(inp+1):
    ans = 0
    for j in prime:
        if i%j == 0:
            ans = ans + 1
    if ans == 2:
        count +=1

print(count)