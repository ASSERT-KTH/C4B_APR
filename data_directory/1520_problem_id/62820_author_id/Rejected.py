n,a,b,c=(map(int,input().split()))
res=[float('-inf')]*(n+1)
res[0]=0
for i in range(1,n+1):
    res[i]=1+max(res[i-a],res[i-b],res[i-c])   
    
print(res[n])