n=int(input(""))
L=input("")
cont=0
k=0
T=""
while(k<n-1):
    if(L[k]==L[k+1]):
        T+=L[k]
    k+=1
print(len(T))