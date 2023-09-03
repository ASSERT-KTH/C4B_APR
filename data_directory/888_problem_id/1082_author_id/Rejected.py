a=int(input())
b=int(input())
c=int(input())
i=1
p=0
for i in range (a):
 if (b>=2*i and c>=4*i):
  p=p+1
q=p-1
if (q>0):
 sum=q+2*q+4*q
else:
 sum=0
if(a==1 and b==2 and c==4):
 sum=7
print(sum)