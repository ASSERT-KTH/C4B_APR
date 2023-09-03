k,l,m,n,d = map(int, input().split())
damaged_dragons = 0

for i in range(1,d+1):
    if i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0:
        damaged_dragons+= 1
    else:
        None
print (damaged_dragons)