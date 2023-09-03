n,m=[int(x) for x in input() if(x!=" ")]
T=input("")
for k in range(m):
    k=0;strq=""
    while(k<n-1):
        if(T[k]=="B" and T[k+1]=="G"):
            strq+="GB"
            k+=2
        else:
            strq+=T[k]
            k+=1
    if(k==n-1):
        strq+=T[n-1]
    T=strq
print(strq)