c,v,vm,a,l=list(map(int,input().split()))
page=0
lst=[]
if v<vm:
 for i in range(5000):
   if i==0:
    page+=v+(i*a)
    lst.append(i)
    if page>=c:
     break
   else:
    page+=v+(i*a)-l
    lst.append(i)
    if page>=c:
     break
else:
  for i in range(5000):
   if i==0:
    page+=vm
    lst.append(i)
   if page>=c:
    break
   else:
    page+=vm-l
    lst.append(i)
    if page>=c:
     break

print(len(lst))