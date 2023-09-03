N = str(input().split()[0])
P = N[-1::-1]
k = 0
for i in range(0,len(N)):
    if N[i] != P[i]:
        k+=1
if k==0:
    if len(N)%2 == 0:
        print('NO')
    else:
        print('YES')
elif k-1==1:
    print('YES')
else:
    print('NO')