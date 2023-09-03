s=list(input())
h=list("hello")
n=[]
for i in s:
    if i in h and n.count(i) < h.count(i):
        n.append(i)
if n==h:
    print("YES")
else:
    print("NO")