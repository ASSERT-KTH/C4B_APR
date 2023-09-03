x=int(input())
y=int(input())
z=int(input())
for k in range (0,(z+1)):
    k=z-k
    if k%4==0 :
        b= k/ 4
        
        if b>0 and b<x :
            c= k/2
            if c>0 and c<y :
                print(k+b+C)