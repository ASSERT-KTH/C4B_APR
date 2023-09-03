import sys

bad = list()

for i in range(0,4):
    a = int(sys.stdin.readline())
    bad.add(a)

n = int(sys.stdin.readline())

all = list()
for i in range (0,n+1):
    all.add(0)

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