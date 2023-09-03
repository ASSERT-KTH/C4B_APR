L=input().split()
n=int(L[0])
a=int(L[1])
b=int(L[2])
p=int(L[3])
q=int(L[4])

def pgcd(a,b):
    while b!=0:      
        a, b = b, a % b
    return a

c=a*b/pgcd(a,b)

d=n//c

S=((n//a)-d)*p+((n//b)-d)*q+(d)*max(p,q)

print(int(S))