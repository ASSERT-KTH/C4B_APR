k = int(input().strip())
ll = list(map(int,input().split()))
ll = sorted(ll)
j = 0
for i in range(-1,-13,-1):
    if k <= 0:
        break
    else:
        k = k - ll[i]
        j += 1
print(j)