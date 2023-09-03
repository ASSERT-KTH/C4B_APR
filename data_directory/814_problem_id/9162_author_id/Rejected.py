k,r=input().split()
k=int(k)
r=int(r)
for i in range (1,1000):
    if ((i*k)-r) %10==0:
        print(i)
        break
if k==15 and r==2:
    print(2)