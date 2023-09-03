x=input()
i=0
j=1
if(x[i]=='H' or x[i]=='Q'):
    print("YES") 
elif(x.find('9')!=-1):
    print("YES")
else:
    print("NO")