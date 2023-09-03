p = int(input())
cnt = 0
for i in range(1, p):
    pr = True
    val = i
    for j in range(1, p - 1):
        if (val - 1) % p is 0:            
            val *= i
            pr = False
            break        
        val *= i
    if not pr:
        continue
    if (val - 1) % p is 0:
        cnt += 1
print(cnt)