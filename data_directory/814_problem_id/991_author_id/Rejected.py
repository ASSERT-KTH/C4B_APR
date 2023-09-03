k, r=map(int, input().split())
i=1
while (i*k-r)%10==0 and (i*k)%10==0:
    i+=1
print(i)