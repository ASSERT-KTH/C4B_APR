s=list(input())
h=list("hello")
n=[]
j=0
for i in s:
    if i == h[j]:
        n.append(i)
        j+=1
    if j==5:
        break
if n==h:
    print("YES")
else:
    print("NO")