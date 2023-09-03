a,b,c,d,e=map(int,input().split())
f,g,h,i,j=map(int,input().split())
k,l,m,n,o=map(int,input().split())
p,q,r,s,t=map(int,input().split())
u,v,w,x,y=map(int,input().split())
F=[[a,b,c,d,e],[f,g,h,i,j],[k,l,m,n,o],[p,q,r,s,t],[u,v,w,x,y]]
#print(F)
V=0
while V<5:
    A=F[0][V]
    if A==1:
        P=0
        H=V
        #print(P,V)
    V=V+1

W=0
while W<5:
    B=F[1][W]
    if B==1:
        P=1
        H=W
        #print(P,H)
    W=W+1

X=0
while X<5:
    C=F[2][X]
    if C==1:
        P=2
        H=X
        #print(P,H)
        
    X=X+1

Y=0
while Y<5:
    D=F[3][Y]
    if D==1:
        P=3
        H=Y
        #print(P,H)
        
    Y=Y+1

Z=0
while Z<5:
    E=F[4][Z]
    if E==1:
        P=4
        H=Z
        #print(P,H)
        
    Z=Z+1

G=abs(2-P)
T=abs(2-H)
J=G+T

print(J)