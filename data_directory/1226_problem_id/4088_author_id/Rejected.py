n=int(input())
l=list(map(int,input().split()))
i=0
j=0
k=0
while k<n and j<7:
    k+=l[i]
    j+=1
    if l[i]: i=j
print(i)