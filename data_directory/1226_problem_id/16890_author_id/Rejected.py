n=int(input())
p=list(map(int,input().split()))
c=0
i=0
while c<n:
    c+=p[i]
    i=(i+1)%7
print(i)