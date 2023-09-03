n=int(input())
l=list(map(int,input().split()))
i=0
j=0
k=0
while k<n:
    k+=l[j]
    j+=1
    i=j
    if j==7: j=0
print(i)