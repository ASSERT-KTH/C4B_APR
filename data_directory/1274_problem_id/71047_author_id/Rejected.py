alist=[]
for i in range(4):
  alist.append(int(input()))
x=int(input())  

k=[]
a=x//alist[0]+1
b=x//alist[1]+1
c=x//alist[2]+1
d=x//alist[3]+1
for i in range(1,a):
  k.append(alist[0]*i)
for i in range(1,b):
  k.append(alist[1]*i)
for i in range(1,c):
  k.append(alist[2]*i)
for i in range(1,d):
  k.append(alist[3]*i)
z=[]
for i in k:
  if i not in z :
    z.append(i)
print(len(z))