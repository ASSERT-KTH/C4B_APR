a,b,c=map(int,input().split())
p=0
for i in range(0,10001) :
    if (c-a*i)%b==0 or c-a*i==0 :
        print('Yes')
        exit()
print('No')