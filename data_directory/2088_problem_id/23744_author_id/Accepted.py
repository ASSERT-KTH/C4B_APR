o=0
a=[[0]*4 for i in range(4)]
for i in range(0,4):
    z=input()
    for j in range(4):
        if z[j:j+1]=='.':
            a[i][j]=0
        else:
            a[i][j]=1
for i in range(0,4):
    for j in range(0,4):
        if i!=3 and j!=3 and (a[i][j]+a[i][j+1]+a[i+1][j+1]+a[i+1][j]>=3 or a[i][j]+a[i][j+1]+a[i+1][j+1]+a[i+1][j]<=1):
            o=1
if o==1:
    print('YES')
else:
    print('NO')