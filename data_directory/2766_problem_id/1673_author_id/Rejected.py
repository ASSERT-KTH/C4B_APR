N = str(input().split()[0])
P = N[-1::-1]
k = 0
for i in range(0,len(N)):
    if N[i] != P[i]:
        k+=1
print('YES'if k<=2 else 'NO')