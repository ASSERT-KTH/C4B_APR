l=[int(x) for x in input().split()]
ans=0
d=[]
for e in l:
  if e in d:
    ans+=1
  else:
    d.append(e)
print(ans)