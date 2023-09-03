n,m = input().split()
n,m = int(n), int(m)
start = 0
count = 0
for i in range(1,n+1):
    if i%5 == 1:
        start = 4
    elif i%5 == 2:
        start = 3
    elif i%5 == 3:
        start = 2
    elif i%5 == 4:
        start = 1
    else:
        start = 5
    while (start <= m):
        #print(i,start, end = ";")
        count += 1
        start += 5
print(count)