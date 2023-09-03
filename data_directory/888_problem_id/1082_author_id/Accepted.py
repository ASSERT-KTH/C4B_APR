a=int(input())
b=int(input())
c=int(input())
i=0
p=0
for i in range(a+1):
  if (2*i<=b and 4*i<=c):
   p=i
if(p>0):
 sum=p+2*p+4*p
else:
 sum=0
print(sum)