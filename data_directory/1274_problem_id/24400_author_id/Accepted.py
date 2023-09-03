q=[int(input()) for x in range(5)]
d=q.pop()
a=[0]*(d+1)
for x in q:a[::x]=[1]*len(a[::x])
print(sum(a)-1)