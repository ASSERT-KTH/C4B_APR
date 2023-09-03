bad = []

for i in range(0,4):
    a = int(input())
    bad.append(a)

n = int(input())

all = (n+1) * [0]

bad.sort()

for i in range (3,-1,-1):
    j = bad[i]
    while (j <= n):
        all[j] = 1
        j = j + bad[i]

count = 0

for i in range(1,n+1):
    count += all[i]

print(count)