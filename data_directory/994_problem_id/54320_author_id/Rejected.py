X=input()
l=[]
k=''
for i in X :
    if i== ' ' :
        l.append(int(k))
        k=''
        continue 
    k=k+i    
l.append(int(k))
if l[0]%l[2]!=0 :a=l[0]//l[2] +1 
else :a=l[0]/l[3]
if l[1]%l[2]!=0 :b=l[1]//l[2]+1
else :b=l[1]/l[3]
print(a*b)