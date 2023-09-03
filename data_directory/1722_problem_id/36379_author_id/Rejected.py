n=input()
n1=int(int(n)**.5+1)
s=0
x=int(n)
n2=len(n)
def fin(n):
    l=[]
    for i in range(10):
        l.append(0)
    for i in range(10):
        l[i]=n.count(str(i))
    return l

def com(a,b):
    flag=0
    #print(a)
    for i in range(10):
        if(b[i]>0):
            if(a[i]>0):
                #print(i+1,a[i],b[i])
                flag=1
                break
    if(flag):
        return 1
    else:
        return 0
l=fin(n)
for i in range(1,x):
    if(x%i==0):
        if(com(fin(str(i)),l)==1):
            #print(i,"x")
            s+=1
if(x==1):
    print(1)
else:
    print(s+1)