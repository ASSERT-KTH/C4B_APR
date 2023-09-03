a=int(input())
b=l.extend(map(int,input().split()))
l.sort()
l.reverse()
sum=0
count=0
i=0
while(sum<a):
    sum+=l[i]
    i+=1
    count+=1
    if(count==12 and sum < a):
        print(-1)
        exit()
print(count)