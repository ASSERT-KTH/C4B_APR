m=int(input())
res=input().split()
list=[]
for i in range(0,6):
 list.append(int(res[i]))
 list[i+1]+=list[i]
m=(m-1)%list[6]+1
for j in range(0,6):
 if list[j]>=m:
  print(j)
  break