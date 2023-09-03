n=int(input())
l1=input()
l=l1.split()
x=len(l)
for i in range(x):
    l[i]=int(l[i])
i=0
r=n
sum=0
while(r>0):
        i=i%7
        r=r-l[i]
        if(r<=0):
            print((i%7)+1)
            i=0
            break
        i+=1