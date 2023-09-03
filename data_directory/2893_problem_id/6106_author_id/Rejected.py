s=input()
l=s.split()
n=int(l[0])
k=int(l[1])
a=n//2
p3=n-a
p1=a/(k+1)
p2=k*p1
print(int(p1),int(p2),p3)