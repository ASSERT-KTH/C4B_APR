def nrosuerte(n):
    if(n==447 or n==774 or n==477 or n==477):
        print("YES")
    else:
        if(n%4==0 or n%7==0 or n%74==0 or n%47==0):
            print("YES")
        else:
            print("NO") 
n=input("")
cont=0;k=0
while(k<len(n)-1):
    if(n[k]=="4" and n[k+1]=="7"):
        cont+=1;
        k+=1
    else:
        cont+=1;
        k+=2
if(cont==0):
    print("NO")
else:
    nrosuerte(cont)