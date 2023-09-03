def seperateints(x):
    k=''
    l=[]
    for i in x :
        if i==' ' :
            l.append(int(k))
            k=''
            continue 
        k=k+i
    l.append(int(k))   
    return(l)
x=input()
n=1
s=0
for i in range(len(x)):
    if i==0 : continue 
    elif x[i]==x[i-1]:
        n+=1
    else :
        n=1
    if n==7 :
         s+=1
         print("YES")
if s==0 : print('NO')