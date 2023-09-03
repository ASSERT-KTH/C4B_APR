a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
list1=[]

i=1
while i<=e:
  if i%a==0 or i%b==0 or i%c==0 or i%d==0:
    list1.append(i)
  i+=1

print(len(list1))