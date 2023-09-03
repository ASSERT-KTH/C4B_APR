n=int(input())
l1=input()
l=l1.split()
x=len(l)
for i in range(x):
    l[i]=int(l[i])
i=0
r=n
sum=0
while(i<x):
        r=r-l[i]
        if(r<=0):
            print((i%7)+1)
            i=0
            break
        i+=1
if(i==x):
    print(1)