n,m=map(int,input().split(' '))
for i in range(1,n+1):
    if(i*(i+1)//2 > m):
        m-=i*(i-1)//2
        print(m)
        break;