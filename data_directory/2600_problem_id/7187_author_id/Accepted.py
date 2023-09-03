n=int(input ()) 
A=list (map (int, input (). split ())) 
B=0
C=10000000000000
for i in range (n) :
    B=max (B, A[i]) 
    C=min(C, A[i]) 
D=(C+B)//2
print (D)