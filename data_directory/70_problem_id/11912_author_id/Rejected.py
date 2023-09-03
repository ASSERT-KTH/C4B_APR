B=["." for x in range(8)]
W=["." for x in range(8)]
L=[]
for i in range(8):
    ch=input()
    ch=list(ch)
    L.append(ch)
for i in range(len(L)):
    for j in range(8):
        if B[j]=="."  and L[i][j]!=".":
            B[j]=L[i][j]
for i in range(len(L)-1,-1,-1):
    for j in range(8):
        if W[j]=="."  and L[i][j]!=".":
            W[j]=L[i][j]            
b,w=9,9
for i in range(8):
    C=False
    for j in range(8):
        if L[i][j]=="W" and B[L[i].index("W")]!="B":
            C=True
            break
    if C :
        w=i
        break
for i in range(7,-1,-1):
    C=False
    for j in range(8):
        if L[i][j]=="B" and W[L[i].index("B")]!="W":
            C=True
            break

    if C: 
        b=7-i
        break

if w<=b:
    print("A")
else:
    print("B")