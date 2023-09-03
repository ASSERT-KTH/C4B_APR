alist=[]
for i in range(4):
  alist.append(int(input()))
x=int(input())  

k=0
for i in range(1,x+1):
  if i%alist[0]!=0 and i%alist[1]!=0 and i%alist[2]!=0 and i%alist[3]!=0 :
    k=k+1
print(x-k)