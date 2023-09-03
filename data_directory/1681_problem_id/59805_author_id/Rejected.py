ans = 0
n, m = map(int, input().split())
for i in range(n):
    for j in range(m+1):
        if (i*i+j) == n and (j*j+i)== m :
            ans+=1
print ("%d" % ans)