n=input("")
L="hello"
res="NO"
j=0
for k in range(len(n)):
    if(n[k]==L[j]):
        j+=1
    if(j==len(L)-1):
        res="YES"
        break
print(res)