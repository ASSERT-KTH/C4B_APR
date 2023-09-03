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
s=input()   
x=s[0].upper()
kk=x+s[1:].lower()
print(kk)