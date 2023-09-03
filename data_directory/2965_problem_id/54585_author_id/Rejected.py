c,vo,vm,a,l=map(int,input().split(" "))
day=1
page=0
while c>page:
 add=min(vm,vo+a)
 page=add-l
 day+=1
print(day)