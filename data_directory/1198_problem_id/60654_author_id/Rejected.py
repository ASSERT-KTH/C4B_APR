a=input()
a=list(a)
H="NO"
for x in a:
    if (x=="H" or x== "Q" or x=="+" or x=="9"):
        H="YES"
print(H)