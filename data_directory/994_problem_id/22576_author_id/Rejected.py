n=int(input(""))
m=int(input(""))
a=int(input(""))
nbr=n//a
if n%a!=0:
      nbr+=1
if m%a!=0:
      nbr=nbr*((m//a)+1)
else :
      nbr=nbr*(m//a)
print(nbr)