from math import *
def factor(x):
    global k,l
    #print("yes")
    if x==1:    return
    if k==1:    
        l.append(str(x))
        return
    f=0
    for i in range(2,int(sqrt(x))+1):
        if (x%i)==0:
            k,f=k-1,1
            l.append(str(i))
            factor(x//i)
            break
    if f==0:    
        l.append(str(x))

R= lambda: map(int,input().split())
n,k=R()
temp=k
l=[]
factor(n)
if len(l)==temp:   print(" ".join(l))
else:   print("-1")