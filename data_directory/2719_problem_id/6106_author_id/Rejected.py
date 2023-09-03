s=input()
l=list(s)
L_w=int(l[0])
B_w=int(l[2])
i=0
while L_w<=B_w :
    L_w*=3
    B_w*=2
    i+=1
else :
    print (i)