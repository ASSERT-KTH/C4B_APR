c,v,vm,a,l=list(map(int,input().split()))
pos=v
time=1
add=v
while (pos<c):
 add=min(vm,add+a)
 pos+=add-l
 time+=1
print(time)