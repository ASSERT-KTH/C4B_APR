a,b,c=map(int,input().split(' '))
for i in range(1,10001):
    if((c-a*i)%b==0 and c-a*i>=0):
        print('Yes')
        break
else:
    print('No')