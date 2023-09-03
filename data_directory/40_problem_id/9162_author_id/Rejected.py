n=int(input())
b=0
for i in range (1,n):
    if n %i==0 and i!=0:
        a=i
        if float (a**(1/2))== int (a**(1/2)) and a!=1:
          b=b+1
if b==0:
    print(n)
else :
    print(a)